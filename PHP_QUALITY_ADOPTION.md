# PHP quality command adoption

Owner: [#65](https://github.com/RocketsAreNostalgic/.github/issues/65).
Contract: [QUALITY_STANDARDS.md](QUALITY_STANDARDS.md#php-command-meanings).

This is the initial bounded Profile A slice of #66. It does not claim that the
full Booster acceptance matrix, shared-style decisions or drift tooling are
complete. Refresh each row when its implementation lands and record the final
revision and actual CI/review evidence in its linked issue.

## Initial reference snapshots

| Repository / issue | Audited default revision | Required source quality | Environment-specific evidence |
| --- | --- | --- | --- |
| [Updater Support #35](https://github.com/RocketsAreNostalgic/ran-updater-support/issues/35) | `d395c37b2a76e5a5e10d9855b3277cde1cec4df3` | PHPCS/WPCS/PHPCompatibility; parser sweep of `src`/`tests`; blocking PHPStan level 8 on `src`; contract/workflow tests | No certified host required |
| [Branch Updater #59](https://github.com/RocketsAreNostalgic/ran-wp-branch-updater/issues/59) | `15253ac03878b01da254d6702a9753103354d8e9` | PHPCS on shipped `src`/`bootstrap.php`; parser sweep also covers tests/scripts; blocking level 5 on `src`; domain/control tests | Required installed no-dev Composer-consumer proof |
| [GitHub Provider #25](https://github.com/RocketsAreNostalgic/ran-booster-github-provider/issues/25) | `ebeb6166b9806b006f1224fa5b291473040a0b86` | PHPCS/WPCS/PHPCompatibility; parser sweep of `src`/`tests`; independent foundation/control tests | Required certified-host contract, blocking level 1 on `src` plus foundation contract, and implementation PHPUnit |

All three declare PHP `^8.2` and use the shared PHP quality floor/current lanes
at 8.2/8.5. Their inspected locks share `ran/coding-standards` revision
`0b03e61a4bb558deeb6bc6b6399f44c0ec95e5be`, PHPCS 3.13.6, WPCS 3.4.1 and the
reviewed PHPCompatibility alpha generation. The explicit root compatibility
requirements are intentional; command adoption does not remove them or update
dependency graphs. Updater Support has no WordPress analysis extension; the
other two use it for their actual WordPress source surface.

## Command migration mapping

| Repository | Previous interface | Intended canonical interface |
| --- | --- | --- |
| Updater Support | `lint:php` = parser; individual tests directly in `check` | `lint:syntax`; `test` aggregates the same tests and is called by `check` |
| Branch Updater | `lint` = parser; individual tests directly in `check` | `lint:syntax`; `test` aggregates the same tests and is called by `check` |
| GitHub Provider | `lint:php` = PHPCS; `format`/`format:php` = PHPCBF; separate implementation commands | `standards` / `standards:fix`; independent `test`; additional `check:host` |

The independent aggregate must retain the same executable checks after alias
expansion. Provider host checks remain outside it, with the same exact certified
Core fixture and required CI matrix. No level, source scope, runtime dependency,
style exception or release lifecycle change is implied by these mappings.

## Remaining programme work

- Starter supplies clean-reference evidence; Booster's coordinated Profile B
  migration supplies mature-reference evidence. The latter is not a prerequisite
  for the PR which produces it.
- Complete the seven-package Booster matrix, plus Starter/Admin Shell, under
  #66. Record tool versions, source coverage and enforcement together.
- Resolve suite style, upgrades, formatter overlap and proportionate drift
  checks through the remaining #65/#66 work. Preserve existing policy meanwhile.
- Workbench and fixtures retain purpose-based exemptions. Plugin Library stays
  deferred; inactive repositories are not reactivated by this ledger.
