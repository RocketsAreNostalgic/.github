#!/usr/bin/env python3
"""Execute the providers' actual syntax steps; discovery failures must not pass."""
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap

ROOT = Path(__file__).resolve().parents[1]
BASH = shutil.which('bash')
PHP = shutil.which('php')
assert BASH and PHP, 'The contract requires Bash and PHP.'


def executable(path, source):
    path.write_text(source)
    path.chmod(0o755)


def check(script, case):
    with tempfile.TemporaryDirectory(prefix='ran-syntax-contract-') as temporary:
        root = Path(temporary)
        work, tools, scratch = (root / name for name in ('work', 'tools', 'scratch'))
        for directory in (work, tools, scratch):
            directory.mkdir()
        env = dict(os.environ, PATH=str(tools) + os.pathsep + os.environ['PATH'], TMPDIR=str(scratch))
        calls = root / 'calls.jsonl'
        # Log the true argument boundary, then use the real interpreter/parser.
        executable(tools / 'php', f'''#!{sys.executable}
import json, subprocess, sys
with open({str(calls)!r}, 'a') as log: log.write(json.dumps(sys.argv[1:]) + '\\n')
sys.exit(subprocess.call([{PHP!r}, *sys.argv[1:]]))
''')
        paths = ['plain.php', 'space name.php', 'line\nbreak.php', 'nested/vendor/owned.php']
        for path in paths + ['vendor/ignored.php', 'node_modules/ignored.php']:
            target = work / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text('<?php echo "valid";' if path in paths else '<?php invalid syntax')
        (work / 'entrypoint').write_text('<?php invalid syntax')
        expected = 0
        if case == 'empty':
            for path in paths:
                (work / path).unlink()
        elif case.startswith('find-'):
            partial = "printf './plain.php\\0'\n" if case == 'find-partial' else ''
            executable(tools / 'find', '#!/bin/bash\n' + partial + 'echo discovery-failed >&2\nexit 23\n')
            expected = 23
        elif case.startswith('parser-'):
            # Force a known order to check failure at both the first and middle entry.
            ordered = ['plain.php', 'space name.php', 'line\nbreak.php']
            bad = ordered[0 if case == 'parser-first' else 1]
            (work / bad).write_text('<?php function broken( {')
            listing = ''.join('./' + path + '\0' for path in ordered)
            executable(tools / 'find', f'#!{sys.executable}\nimport sys\nsys.stdout.write({listing!r})\n')
            expected = 255
        elif case == 'missing-php':
            (tools / 'php').unlink()
            for command in ('find', 'mktemp', 'rm'):
                (tools / command).symlink_to(shutil.which(command))
            env['PATH'] = str(tools)
            expected = 127
        elif case == 'mktemp-failure':
            executable(tools / 'mktemp', '#!/bin/bash\nexit 73\n')
            expected = 73
        result = subprocess.run([BASH, '-c', script], cwd=work, env=env, text=True, capture_output=True)
        assert result.returncode == expected, (case, result.returncode, result.stdout, result.stderr)
        actual = [json.loads(line) for line in calls.read_text().splitlines()] if calls.exists() else []
        if case == 'normal':
            assert sorted(actual) == sorted([['-l', './' + path] for path in paths]), actual
        elif case in ('empty', 'find-empty', 'find-partial', 'missing-php', 'mktemp-failure'):
            assert not actual, (case, actual)
        elif case.startswith('parser-'):
            count = 1 if case == 'parser-first' else 2
            assert actual == [['-l', './' + path] for path in ordered[:count]], actual
        assert not list(scratch.iterdir()), (case, 'temporary discovery list was not cleaned')


steps = 0
for filename, expected_count in (('quality-php-library-v2.yml', 2), ('quality-wordpress-plugin.yml', 1)):
    source = (ROOT / '.github/workflows' / filename).read_text()
    blocks = re.findall(r'      - name: Lint all PHP files\n(?:(?:        [^\n]*\n))*?        run: \|\n((?:          [^\n]*\n)+)', source)
    assert len(blocks) == expected_count, (filename, 'syntax step extraction changed', len(blocks))
    for index, block in enumerate(blocks):
        for case in ('normal', 'empty', 'find-empty', 'find-partial', 'parser-first', 'parser-middle', 'missing-php', 'mktemp-failure'):
            check(textwrap.dedent(block), case)
        steps += 1
        print(f'PASS {filename} syntax step {index + 1}: 8 actual-command controls')
assert steps == 3
