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
outside its directory. This selection is inferred from the exact finder source
and tracked paths; it has not been measured by executing PHP-CS-Fixer here.

PHPCS separately selects the project through `<file>.</file>` with dependency
exclusions. It retains `RANWordPressPlugin`, Starter-specific WordPress-Docs,
generic class/control-flow/comment checks and local identity/support settings.
The narrow second finder does not mean the production plugin lacks a style
gate.

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

These rules overlap PHPCS/PHPCBF's formatting responsibilities. This source
audit has not established that every fixer outcome is equivalent to, or weaker
than, the effective PHPCS rules after local/inline exceptions. Neither deletion
nor a project-wide finder expansion is justified solely by the apparent overlap.

## Recommended implementation boundary

Prefer one PHPCS/PHPCBF style authority if representative comparison proves it
preserves every intended check. Retain Starter's stronger docs/generic checks;
do not copy Booster naming/Yoda exceptions into the clean reference. If the
comparison identifies a useful unique behavior, first decide whether a narrow
PHPCS rule can express it. Retain a second formatter only for a documented need
with matching scope and stable combined output.

The next implementation PR should:

1. Use PHP 8.4 and the tracked lock; record PHP-CS-Fixer's actual selected file
   list and PHPCS's actual file/rule lists. Include the two tools' different
   directory/dotfile behavior in the evidence.
2. On a disposable copy, compare each currently enabled fixer family with the
   effective PHPCS/PHPCBF behavior. Use the archive helper and representative
   OOP, mixed PHP/HTML template and test files. Include negative fixtures for
   syntax and intended style violations; retain any stronger useful check or
   provide an explicit reviewed replacement.
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

No Starter source, rules, dependencies or workflow were changed in this
investigation. PHP/Composer is unavailable in the audit workspace, so formatter
equivalence, actual violation counts and repeated-format stability remain
execution requirements for #24. The structural/source findings above are
sufficient to scope that PR, not to authorize removing an existing check.
