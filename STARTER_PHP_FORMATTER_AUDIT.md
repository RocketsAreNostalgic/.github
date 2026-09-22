# Starter PHP formatter investigation

Owner: [Starter #24](https://github.com/RocketsAreNostalgic/ran-starter-plugin/issues/24).
Programme: [.github #66](https://github.com/RocketsAreNostalgic/.github/issues/66).
Inspected Starter revision: `31f48fda13d7b9671f88d0ecf249af6aad251c52`.

## Findings

Starter's second formatter has a much narrower surface than its name suggests.
[`scripts/.php-cs-fixer.php`](https://github.com/RocketsAreNostalgic/ran-starter-plugin/blob/31f48fda13d7b9671f88d0ecf249af6aad251c52/scripts/.php-cs-fixer.php)
uses `->in(__DIR__)`, which selects the configuration's `scripts/` directory.
The lock pins PHP-CS-Fixer 3.95.15 at
`3e47e5d50046f87e3244acde2fe655d1a3b72555`.

That version's [Finder](https://github.com/PHP-CS-Fixer/PHP-CS-Fixer/blob/3e47e5d50046f87e3244acde2fe655d1a3b72555/src/Finder.php)
selects `.php` files and, in normal v3 mode, ignores dotfiles. Its
[Future mode](https://github.com/PHP-CS-Fixer/PHP-CS-Fixer/blob/3e47e5d50046f87e3244acde2fe655d1a3b72555/src/Future.php)
can change that default; the inspected repository/shared workflow does not set
`PHP_CS_FIXER_FUTURE_MODE`.

The tracked tree has 43 PHP files. In normal v3 mode, the configured finder
therefore selects just **`scripts/build-release.php`**. The hidden fixer config
is excluded, and the plugin entrypoints, `inc/`, `templates/` and tests lie
outside its directory. Executing the locked configuration on PHP 8.4.23
confirmed that one-file selection; its dry run passed.

PHPCS separately selects the project through `<file>.</file>` with dependency
exclusions. It retains `RANWordPressPlugin`, Starter-specific WordPress-Docs,
generic class/control-flow/comment checks and local identity/support settings.
The narrow second finder does not mean the production plugin lacks a style
gate. An actual PHPCS run selected 42 files, excluding the hidden fixer config,
and passed with zero errors or warnings. The effective ruleset listed 360
sniffs. The measured [file list](quality-evidence/starter-phpcs-files.txt) and
[sniff list](quality-evidence/starter-phpcs-sniffs.txt) are retained.

## Actual command behavior

| Command | Current operation |
| --- | --- |
| `composer cs:check` | PHP-CS-Fixer dry run/diff, cache disabled by CLI; current finder is scripts-only |
| `composer standards:full` | Project PHPCS check, including its shared and stronger local rules |
| `composer lint` | Runs both of the above |
| `composer check` | `lint`, ordinary PHPUnit, then blocking level-1 WordPress-aware PHPStan |
| `composer cs` / `cs:sequential` | Mutating second formatter, same finder; normal/forced sequential execution |
| `composer standards:fix` | PHPCBF on the PHPCS selection |
| `composer format` | PHP-CS-Fixer first, then PHPCBF |
| `composer build` | `format`, then asset build; it is a mutating build command |

The config enables line endings, trailing-whitespace cleanup (including
comments), single quotes, long array syntax, comma spacing, concatenation
spacing, operator/assignment alignment and same-line braces. It sets
`indentation_type` twice: the later `false` wins. Statement, method-chain and
array indentation fixers are also explicitly disabled in favor of WordPress
rules. The config enables caching, but the Composer commands explicitly disable
it. The locked `braces` fixer is [deprecated](https://github.com/PHP-CS-Fixer/PHP-CS-Fixer/blob/3e47e5d50046f87e3244acde2fe655d1a3b72555/src/Fixer/Basic/BracesFixer.php).

These rules overlap PHPCS/PHPCBF's formatting responsibilities, but the runtime
comparison below demonstrates an alignment-enforcement difference. Neither
deletion nor a project-wide finder expansion preserves the current contract
automatically.

## Recommended implementation boundary

Prefer one PHPCS/PHPCBF style authority if representative comparison proves it
preserves every intended check. Retain Starter's stronger docs/generic checks;
do not copy Booster naming/Yoda exceptions into the clean reference. If the
comparison identifies a useful unique behavior, first decide whether a narrow
PHPCS rule can express it. Retain a second formatter only for a documented need
with matching scope and stable combined output.

The next implementation PR should:

1. Use the PHP 8.4 baseline and measured file/rule lists below. Repeat them
   against the implementation candidate if its source, lock or rules change;
   preserve the distinction between directory and dotfile selection.
2. Build on the negative fixtures and representative-file results below.
   Resolve the observed alignment difference explicitly: retain the intended
   check, add a reviewed PHPCS replacement, or approve its retirement.
   These finite examples do not prove equivalence for every PHP construct
   or inline suppression.
3. Apply the proposed formatting path twice and verify byte stability. Run its
   corresponding checks after each pass so a second formatter cannot hide a
   conflict by rewriting the first formatter's result. Keep broad source
   rewrites separate from command adoption.
4. Adopt `lint:syntax`, `standards`, `standards:fix`, `analyze`, `test` and
   non-mutating `check` with the agreed scope. Audit callers before removing
   `cs:*`, `lint`, `format` or `standards:full`: Composer's `build`,
   `RELEASE.md` and `PRE-RELEASE-CHECKLIST.md` currently call these surfaces.
5. Preserve PHP `>=8.4 <8.6`, WP 7.0+, ordinary unit/analysis checks, frontend
   freshness, release-workflow/archive tests and installed activation. Explicitly
   resolve the missing 8.5 CI proof before claiming execution across the entire
   declared range.

No tracked Starter source, rules, dependencies or workflow were changed in this
investigation. The runtime comparison below extends the initial source audit;
command adoption and any exception replacement remain implementation work
owned by #24.

## Runtime evidence (22 September 2026)

The experiment used a disposable archive of the inspected revision, PHP 8.4.23
CLI (Static PHP CLI build), Composer 2.8.12, and the unchanged Starter lock.
PHP-CS-Fixer 3.95.15, PHPCS/PHPCBF 3.13.6, WPCS 3.4.1 and the shared standard
at `0b03e61a4bb558deeb6bc6b6399f44c0ec95e5be` were used. The recorded installed
package versions/references matched the lock. The application dependency
`ran/plugin-lib` failed archive extraction and was absent on disk; all other
locked package directories were present. Composer generated the tool autoloader
with scripts/plugins disabled. PHPCS standards were registered explicitly from
the installed `phpcodesniffer-standard` packages. This is a formatter experiment,
not a successful full Composer install, application test, or CI proof.

The runtime archive SHA-256 was
`5fa2b5f1cc9d7f79b19718926b4f4f0bb6949db52073b2fabf8ae52de3993af5`;
this records the downloaded artifact, not an independently signed provenance
claim. Composer's SHA-256 matched its published checksum:
`f446ea719708bb85fcbf4ef18def5d0515f1f9b4d703f6d820c9c1656e10a2f2`.

The [comparison harness](quality-evidence/compare-starter-formatters.py) records
exit codes, diagnostics and second-pass byte stability. It checks PHP-CS-Fixer
and PHPCS before changes, after each formatter and after the combined sequence.
It separately measures PHPCBF alone. Explicit `--path-mode=override` selects
negative fixtures and representative files outside the configured finder; those
runs investigate a hypothetical broader scope, not today's `composer cs` scope.
Execution is sequential within each case, with four independent cases in
parallel. PHP-CS-Fixer's cache is disabled and its runner is sequential; PHPCS
uses one worker per case. Neither application PHP nor Composer scripts run.

Reproduce against a disposable archive with its locked dependencies and PHPCS
standards installed, with PHP 8.4 on `PATH`:

```sh
php -r 'require "vendor/autoload.php"; $c = require "scripts/.php-cs-fixer.php"; foreach ($c->getFinder() as $f) echo $f->getRelativePathname(), PHP_EOL;'
php vendor/bin/phpcs --standard=.phpcs.xml --report=json -v
php vendor/bin/phpcs --standard=.phpcs.xml -e
python3 /path/to/quality-evidence/compare-starter-formatters.py "$PWD" /tmp/starter-formatters.json
```

Do not run the harness in a working checkout with concurrent edits: it restores
representative files after temporary formatting. Keep generated dependency/tool
state and raw local logs outside the consumer repository's tracked files.

### Detection is not equivalent

The clean synthetic control passed both tools. Each style mutation was rejected
by PHP-CS-Fixer (exit 8). PHPCS rejected nine of the ten style mutations (exit 2)
but accepted assignment misalignment (exit 0). The malformed-syntax fixture was
rejected by PHP-CS-Fixer (exit 4), PHPCS (`Generic.PHP.Syntax.PHPSyntax`, exit 2)
and `php -l` (exit 255).

| Deliberate defect | PHPCS diagnostic under the current command |
| --- | --- |
| CRLF line endings | `Generic.Files.LineEndings.InvalidEOLChar` |
| Trailing whitespace in code | `Squiz.WhiteSpace.SuperfluousWhitespace.EndLine` |
| Trailing whitespace in docblocks | `Squiz.WhiteSpace.SuperfluousWhitespace.EndLine` |
| Unnecessary double quotes | `Squiz.Strings.DoubleQuoteUsage.NotRequired` |
| Short array syntax | `Universal.Arrays.DisallowShortArraySyntax.Found` |
| Space before array comma | `Universal.WhiteSpace.CommaSpacing.SpaceBefore` |
| Missing space after array comma | `Universal.WhiteSpace.CommaSpacing.NoSpaceAfter` |
| Missing concatenation spaces | `Squiz.Strings.ConcatenationSpacing.PaddingFound` |
| Misaligned adjacent assignments | Accepted |
| Function/control opening braces on the following line | `Generic.Functions.OpeningFunctionBraceKernighanRitchie.BraceOnNewLine`, `Squiz.ControlStructures.ControlSignature.SpaceAfterCloseParenthesis`, `WordPress.WhiteSpace.ControlStructureSpacing.OpenBraceNotSameLine` |

For representative source files, the archive helper, `inc/Base/Config.php` and
`templates/features/auth.php` passed both checks before formatting.
`tests/Unit/ExampleFeatureControllerTest.php` passed PHPCS but failed the
explicitly widened fixer check: PHP-CS-Fixer proposed array-arrow alignment and
assignment realignment. Today's configured finder does not check that test file.
Simply widening it would introduce source churn despite a passing existing gate.

### Autofixing, repeatability and disposition

PHPCBF fixed all nine PHPCS-rejected style fixtures (exit 1 means fixes made).
Each then passed both checks. PHPCBF left the accepted misalignment unchanged;
that fixture continued to fail PHP-CS-Fixer. Running PHPCS with `-w` exposed two
fixable `Generic.Formatting.MultipleStatementAlignment.NotSameWarning` warnings.
Starter's ruleset supplies `-n`, so its ordinary check and fixer suppress them.
The alignment behavior is therefore available in PHPCS but is not enforced by
the current command.

PHPCBF alone was byte-stable on its second pass for all eleven valid fixtures
and all four representative files. The combined PHP-CS-Fixer then PHPCBF path
also passed both checks after its first complete pass and was byte-stable on a
second pass for those fifteen cases. No conflict was observed in this sample.
The malformed-syntax case was checked but intentionally not autofixed. The
[compact results](quality-evidence/starter-formatter-results.json) retain exit
codes, diagnostic identities, stability results and the representative test diff.
All tracked archive files, including Composer manifests and locks, matched the
original source snapshot after the experiment.

Recommendation: proceed toward one PHPCS/PHPCBF authority, but do not describe
removal of PHP-CS-Fixer as behavior-preserving yet. Decide whether alignment is
an intended blocking rule and at what scope. A reviewed change to the specific
PHPCS alignment diagnostic is a narrower candidate than enabling every warning.
If alignment is deliberately retired, record that policy change explicitly.
Re-test array-arrow and assignment behavior on the implementation candidate,
including the test-file example above; the warning control proves the synthetic
assignment case, not every alignment variant.

These are finite formatter examples on PHP 8.4, not proof of universal tool
equivalence, PHP 8.5 execution, or the full Starter quality suite. The initial
out-of-project fixture attempt hit PHPCBF's base-path write failure and was
excluded from the recorded results; the final harness places fixtures inside
the disposable archive and fails on abnormal PHPCBF exit codes. This work
changes only organisation evidence and its reproduction harness. Starter
Composer/CI/release adoption remains with the coordinated implementation lane.
