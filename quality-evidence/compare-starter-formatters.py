#!/usr/bin/env python3
"""Run only in a disposable Starter archive with its locked tools installed.
Usage: python3 compare-starter-formatters.py /absolute/disposable/starter output.json
Requires php on PATH. Does not execute application code or Composer scripts.
"""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

root = Path(sys.argv[1]).resolve()
output = Path(sys.argv[2]).resolve()
php = shutil.which('php')
assert php and (root / 'vendor/autoload.php').is_file()
assert not (root / '.git').exists(), 'Use a disposable archive, not a Git checkout'
env = {'PATH': os.environ['PATH'], 'HOME': tempfile.mkdtemp(prefix='formatter-home-')}
fix = [php, 'vendor/bin/php-cs-fixer', 'fix', '--config=scripts/.php-cs-fixer.php',
       '--allow-risky=yes', '--using-cache=no', '--sequential', '--path-mode=override']
cs = [php, 'vendor/bin/phpcs', '--standard=.phpcs.xml', '--parallel=1', '-q', '--report=json']
cbf = [php, 'vendor/bin/phpcbf', '--standard=.phpcs.xml', '--parallel=1', '-q']

def run(cmd):
    p = subprocess.run(cmd, cwd=root, env=env, capture_output=True, text=True, timeout=120)
    if cmd[:len(cbf)] == cbf and p.returncode not in (0, 1, 2, 3):
        raise RuntimeError(p.stdout + p.stderr)
    return {'exit': p.returncode, 'stdout': p.stdout.replace(str(root), '<starter>'),
            'stderr': p.stderr.replace(str(root), '<starter>')}

def check(path):
    return {'fixer': run(fix + ['--dry-run', '--diff', str(path)]), 'phpcs': run(cs + [str(path)])}

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

base = '''<?php
/**
 * Formatter evidence.
 *
 * @package RanPlugin
 */

/**
 * Build example values.
 *
 * @return array Example values.
 */
function ran_starter_plugin_formatter_evidence() {
	$short       = 'a';
	$longer_name = 'b';
	$values      = array( 'one', 'two' );
	if ( 'a' === $short ) {
		$values[] = $short . $longer_name;
	}
	return $values;
}
'''
fixtures = {
    'baseline': base,
    'line-ending': base.replace('\n', '\r\n'),
    'trailing-code': base.replace("$short       = 'a';", "$short       = 'a';  "),
    'trailing-comment': base.replace('Formatter evidence.', 'Formatter evidence.  '),
    'single-quote': base.replace("'a'", '"a"'),
    'long-array': base.replace("array( 'one', 'two' )", "[ 'one', 'two' ]"),
    'comma-before': base.replace("'one',", "'one' ,"),
    'comma-after': base.replace("'one', 'two'", "'one','two'"),
    'concat': base.replace('$short . $longer_name', '$short.$longer_name'),
    'alignment': base.replace('$short       =', '$short =').replace('$values      =', '$values ='),
    'braces': base.replace('evidence() {', 'evidence()\n{').replace("$short ) {", "$short )\n\t{"),
    'syntax': base.replace("$short       = 'a';", "$short       = ;"),
}
result = {'php': run([php, '-v']), 'fixtures': {}, 'representatives': {}}
work = Path(tempfile.mkdtemp(prefix='formatter-cases-', dir=root))
try:
    def fixture_case(item):
        name, contents = item
        path = work / (name + '.php')
        path.write_bytes(contents.encode())
        row = {'before': check(path)}
        if name == 'alignment':
            row['phpcs_with_warnings'] = run(cs + ['-w', str(path)])
        if name == 'syntax':
            row['parser'] = run([php, '-l', str(path)])
        else:
            row['phpcbf'] = run(cbf + [str(path)])
            row['after_phpcbf'] = check(path)
            first = digest(path)
            row['phpcbf_second'] = run(cbf + [str(path)])
            row['phpcbf_stable'] = first == digest(path)
            path.write_bytes(contents.encode())
            row['fixer_apply'] = run(fix + [str(path)])
            row['after_fixer'] = check(path)
            row['combined_cbf'] = run(cbf + [str(path)])
            first = digest(path)
            row['combined_check'] = check(path)
            row['combined_second_fixer'] = run(fix + [str(path)])
            row['combined_second_cbf'] = run(cbf + [str(path)])
            row['combined_stable'] = first == digest(path)
        result['fixtures'][name] = row
        print(name, flush=True)
    with ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(fixture_case, fixtures.items()))

    def representative_case(relative):
        # Keep the original path: inline/path-based exclusions remain meaningful.
        path = root / relative
        original = path.read_bytes()
        try:
            row = {'before': check(path)}
            row['fixer_apply'] = run(fix + [relative])
            row['after_fixer'] = check(path)
            row['cbf_apply'] = run(cbf + [relative])
            first = digest(path)
            row['after_combined'] = check(path)
            row['second_fixer'] = run(fix + [relative])
            row['second_cbf'] = run(cbf + [relative])
            row['combined_stable'] = first == digest(path)
            path.write_bytes(original)
            row['cbf_only'] = run(cbf + [relative])
            first = digest(path)
            row['after_cbf_only'] = check(path)
            row['cbf_only_second'] = run(cbf + [relative])
            row['cbf_only_stable'] = first == digest(path)
            result['representatives'][relative] = row
            print(relative, flush=True)
        finally:
            path.write_bytes(original)

    with ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(representative_case, [
            'scripts/build-release.php', 'inc/Base/Config.php',
            'templates/features/auth.php', 'tests/Unit/ExampleFeatureControllerTest.php']))
finally:
    output.write_text(json.dumps(result, indent=2, sort_keys=True).replace(str(work), '<fixtures>') + '\n')
    shutil.rmtree(work)
    shutil.rmtree(env['HOME'])
