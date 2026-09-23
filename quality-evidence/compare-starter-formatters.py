#!/usr/bin/env python3
"""Audit aid for repeating Starter formatter comparisons in a disposable environment.
Usage: python3 compare-starter-formatters.py /absolute/disposable/starter output.json REVISION SOURCE_MANIFEST
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
requested_revision = sys.argv[3]
source_manifest_path = Path(sys.argv[4]).resolve()
manifest_envelope = json.loads(source_manifest_path.read_text())
assert isinstance(manifest_envelope, dict)
revision = manifest_envelope.get('revision')
source_manifest = manifest_envelope.get('files')
assert revision == requested_revision, 'Requested revision differs from authoritative source manifest'
assert isinstance(source_manifest, dict) and source_manifest
assert len(revision) == 40 and all(c in '0123456789abcdef' for c in revision)
php = shutil.which('php')
assert php and (root / 'vendor/autoload.php').is_file()
assert not (root / '.git').exists(), 'Use a disposable archive, not a Git checkout'
for relative, expected in source_manifest.items():
    path = root / relative
    assert path.is_file(), f'Manifest source file missing: {relative}'
    assert hashlib.sha256(path.read_bytes()).hexdigest() == expected, f'Source bytes differ from manifest: {relative}'
installed_json = root / 'vendor/composer/installed.json'
assert installed_json.is_file(), 'Composer installed metadata is required'
installed_data = json.loads(installed_json.read_text())
installed_packages = installed_data.get('packages', installed_data)
installed = {p['name']: {'version': p.get('version'), 'reference': (p.get('source') or {}).get('reference')} for p in installed_packages}
lock_data = json.loads((root / 'composer.lock').read_text())
locked = {p['name']: {'version': p.get('version'), 'reference': (p.get('source') or {}).get('reference')} for p in lock_data.get('packages-dev', []) + lock_data.get('packages', [])}
for name in ('friendsofphp/php-cs-fixer','squizlabs/php_codesniffer','wp-coding-standards/wpcs','ran/coding-standards'):
    assert name in installed and name in locked, f'Missing formatter tool identity: {name}'
    assert installed[name] == locked[name], f'Installed formatter tool differs from reviewed lock: {name}'

env = {'PATH': os.environ['PATH'], 'HOME': tempfile.mkdtemp(prefix='formatter-home-')}
fix = [php, 'vendor/bin/php-cs-fixer', 'fix', '--config=scripts/.php-cs-fixer.php',
       '--allow-risky=yes', '--using-cache=no', '--sequential', '--path-mode=override']
cs = [php, 'vendor/bin/phpcs', '--standard=.phpcs.xml', '--parallel=1', '-q', '--report=json']
cbf = [php, 'vendor/bin/phpcbf', '--standard=.phpcs.xml', '--parallel=1', '-q']

def run(cmd):
    p = subprocess.run(cmd, cwd=root, env=env, capture_output=True, text=True, timeout=120)
    is_phpcs = len(cmd) > 1 and cmd[1].endswith('/phpcs')
    is_phpcbf = len(cmd) > 1 and cmd[1].endswith('/phpcbf')
    is_fixer = len(cmd) > 1 and cmd[1].endswith('/php-cs-fixer')
    is_parser = len(cmd) >= 2 and cmd[0] == php and cmd[1] == '-l'
    allowed = (0, 4, 8) if is_fixer else (0, 1, 2) if is_phpcs else (0, 1, 2, 3) if is_phpcbf else (0, 255) if is_parser else (0,)
    if p.returncode not in allowed:
        raise RuntimeError(f'Unexpected tool exit {p.returncode}: {p.stdout}{p.stderr}')
    if is_phpcs:
        try:
            json.loads(p.stdout)
        except json.JSONDecodeError as error:
            raise RuntimeError(f'PHPCS did not emit a valid JSON report: {p.stdout}{p.stderr}') from error
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
work = None
try:
    result = {'php': run([php, '-v']), 'fixtures': {}, 'representatives': {}}
    work = Path(tempfile.mkdtemp(prefix='formatter-cases-', dir=root))
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
except BaseException:
    if work is not None:
        shutil.rmtree(work, ignore_errors=True)
    shutil.rmtree(env['HOME'], ignore_errors=True)
    raise

def compact_tool(tool, value):
        row = {'exit': value['exit']}
        if tool == 'phpcs' and value.get('stdout', '').strip():
            report = json.loads(value['stdout'])
            messages = [m for details in report.get('files', {}).values() for m in details.get('messages', [])]
            row['diagnostics'] = sorted({m['source'] for m in messages})
            totals = report.get('totals', {})
            row['totals'] = {k: totals.get(k, 0) for k in ('errors', 'fixable', 'warnings')}
        return row

def compact_value(key, value):
        if isinstance(value, dict) and 'exit' in value:
            tool = 'phpcs' if key in ('phpcs', 'phpcs_with_warnings') else key
            return compact_tool(tool, value)
        if isinstance(value, dict):
            return {k: compact_value(k, v) for k, v in value.items()}
        return value

try:
    shutil.rmtree(work)
    compact = {
            'revision': revision,
            'scope': 'Disposable formatter-only experiment; application dependency extraction incomplete',
            'php': subprocess.run([php, '-r', 'echo PHP_VERSION;'], cwd=root, env=env, check=True, capture_output=True, text=True).stdout,
            'fixtures': compact_value('fixtures', result['fixtures']),
            'representatives': compact_value('representatives', result['representatives']),
        }
    finder = subprocess.run(
            [php, '-r', 'require "vendor/autoload.php"; $c = require "scripts/.php-cs-fixer.php"; foreach ($c->getFinder() as $f) echo $f->getRelativePathname(), PHP_EOL;'],
            cwd=root, env=env, check=True, capture_output=True, text=True
        )
    phpcs_report = json.loads(run(cs)['stdout'])
    sniff_list = subprocess.run([php, 'vendor/bin/phpcs', '--standard=.phpcs.xml', '-e'], cwd=root, env=env, check=True, capture_output=True, text=True).stdout
    compact['baseline'] = {
            'fixer_exit': check(root / 'scripts/build-release.php')['fixer']['exit'],
            'fixer_files': [line for line in finder.stdout.splitlines() if line],
            'phpcs_exit': 0 if phpcs_report.get('totals', {}).get('errors', 0) == 0 else 2,
            'phpcs_files': len(phpcs_report.get('files', {})),
            'phpcs_sniffs': sum(1 for line in sniff_list.splitlines() if line.lstrip().startswith('- ')),
        }
    representative = result['representatives'].get('tests/Unit/ExampleFeatureControllerTest.php', {})
    compact['representative_fixer_diff'] = representative.get('before', {}).get('fixer', {}).get('stdout', '')
    output.write_text(json.dumps(compact, indent=2, sort_keys=True).replace(str(work), '<fixtures>') + '\n')
    
finally:
    shutil.rmtree(work, ignore_errors=True)
    shutil.rmtree(env['HOME'], ignore_errors=True)

