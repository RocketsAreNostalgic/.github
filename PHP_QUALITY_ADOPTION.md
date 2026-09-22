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
| GitHub Provider | `lint:php`; `standards` aliases it | `standards` directly runs the same PHPCS invocation; remove `lint:php` |
| GitHub Provider | `format:php`; `format` and `standards:fix` alias it | `standards:fix` directly runs the same PHPCBF invocation; remove `format` / `format:php` |
| GitHub Provider | `test:foundation` and `test:release-control` called directly by `check` | `test` aggregates both; `check` calls `test`; both focused scripts remain |
| GitHub Provider | `lint:syntax` and `validate:strict` | Same names and scope; syntax also propagates discovery failure |
| GitHub Provider | `analyze`, `test:implementation`, and CI's `php tests/host-contract.php` | Retain both focused scripts; add `test:host-contract`; `check:host` runs host contract, analysis and implementation tests in that order |

The independent aggregate must retain the same executable checks after alias
expansion. Provider host checks remain outside it, with the same exact certified
Core fixture and required CI matrix. No level, source scope, runtime dependency,
style exception or release lifecycle change is implied by these mappings.

## GitHub Provider certified-host evidence

The certified Core revision is
`ffc11fc8e40618624a785b7fca5193029c6d492e` (Booster `v1.0.0-beta.29`,
Provider API 11). The authoritative checkout and verification steps are in the
provider's [CI workflow at the audited default revision](https://github.com/RocketsAreNostalgic/ran-booster-github-provider/blob/ebeb6166b9806b006f1224fa5b291473040a0b86/.github/workflows/ci.yml).

| Required lane | PHP | Evidence retained by command adoption |
| --- | --- | --- |
| `baseline` | 8.2 / 8.5 | Independent `composer check` and the shared parser sweep |
| `host-contract` | 8.2 | Exact package/Core SHA verification and `tests/host-contract.php` |
| `implementation` | 8.2 / 8.5 | Exact package/Core SHA verification, blocking level-1 PHPStan and implementation PHPUnit; the proposed `check:host` also repeats the host contract |
| `release-classification` | Node 24.11.0 | Required PR-title/release-significance classification |

All four job IDs remain dependencies of terminal `quality`. Local host evidence
requires setting `RAN_BOOSTER_CORE_PATH` and verifying the checkout equals the
certified SHA before invoking `check:host`; the host-contract test checks API
shape and does not itself authenticate the Git revision. A passing API-shape
test against another Core checkout is not equivalent certification.

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
