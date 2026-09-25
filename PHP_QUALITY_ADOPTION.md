# PHP quality command adoption

Owner: [#65](https://github.com/RocketsAreNostalgic/.github/issues/65).
Contract: [QUALITY_STANDARDS.md](QUALITY_STANDARDS.md#php-command-meanings).

This ledger records the initial bounded command-adoption slice and its current
landing status, updated for landed slices on 24 September 2026 (UTC). The complete nine-repository
source/coverage/tool inventory and observed execution evidence live in
[PHP_QUALITY_MATRIX.md](PHP_QUALITY_MATRIX.md). Neither document declares full
suite acceptance or transfers active release/quality claims.

## Current landing status

| Repository / owner | Recorded revision | Canonical-command status |
| --- | --- | --- |
| [Updater Support #35](https://github.com/RocketsAreNostalgic/ran-updater-support/issues/35) | `6a9cdbc9eb1bbecbafcbe16da931c98928d035e8` | #36 merged; `check`, `lint:syntax`, `standards`, `standards:fix`, `analyze`, `test` present. #40 additionally activates owned-method regression enforcement. |
| [Branch Updater #59](https://github.com/RocketsAreNostalgic/ran-wp-branch-updater/issues/59) | `d382d09e4490ed4438d9ebaea2a06d69d59f0ce3` | #60 merged; all six canonical names present. Installed no-dev consumer remains required in CI. |
| [GitHub Provider #25](https://github.com/RocketsAreNostalgic/ran-booster-github-provider/issues/25) | `7cd2c0624e2a41ccd8c2b1e879ac743eddb8f800` | #26 merged; all six canonical names and separate certified-host `check:host` present. |
| [Release Updater #60](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/issues/60) | `65b31c0aca26363a87180fa5f9ac7081fd661eb9` | #66 commands retained; #67–#76 coverage sequence complete (excluding held release #70): all 36 shipped PHP files directly analysed at level 8. Live audit, generated parity and no-dev proof remain in check; naming/condition acceptance remains open. |
| [Migrator #42](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/issues/42) | `829d823afd87923a20f8170671d2f456465424d9` | #46 fixed parser/discovery failure propagation and added lint:syntax; lint:php retained for CI. No standards:fix or analyze command yet. #45 separately repinned release workflow. |

The original Support/Branch/Provider cohort all declare PHP `^8.2` and use shared floor/current lanes at 8.2/8.5.
Support/Branch now lock published coding-standards v1.0.0 at
`6af816a02b7d1108ad5c990e9d0fda0af0a13de7`; Provider still locks the older
`0b03e61a4bb558deeb6bc6b6399f44c0ec95e5be` candidate. All retain PHPCS 3.13.6,
WPCS 3.4.1 and explicit root PHPCompatibility alpha requirements. Support has
no WordPress analysis extension because its source does not require one;
Branch/Provider use it for their WordPress source. Levels remain 8, 5 and
host-backed 1 respectively.

Post-merge evidence for the landed slices is linked in the matrix's
[24 September checkpoint](PHP_QUALITY_MATRIX.md#24-september-2026-landed-slice-checkpoint).
Provider #26 is complete; do not recreate it. The older Support/Branch rows
remain the recorded adoption revisions, not a new estate-wide source audit.

## Command migration mapping

| Repository | Previous interface | Landed canonical mapping |
| --- | --- | --- |
| Updater Support | `lint:php` = parser; individual tests directly in `check` | `lint:syntax`; `test` aggregates the same tests and is called by `check` |
| Branch Updater | `lint` = parser; individual tests directly in `check` | `lint:syntax`; `test` aggregates the same tests and is called by `check` |
| GitHub Provider | `lint:php`; `standards` aliases it | `standards` directly runs the same PHPCS invocation; remove `lint:php` |
| GitHub Provider | `format:php`; `format` and `standards:fix` alias it | `standards:fix` directly runs the same PHPCBF invocation; remove `format` / `format:php` |
| GitHub Provider | `test:foundation` and `test:release-control` called directly by `check` | `test` aggregates both; `check` calls `test`; both focused scripts remain |
| GitHub Provider | `lint:syntax` and `validate:strict` | Same names and scope; syntax also propagates discovery failure |
| GitHub Provider | `analyze`, `test:implementation`, and CI's `php tests/host-contract.php` | Retain both focused scripts; add `test:host-contract`; `check:host` runs host contract, analysis and implementation tests in that order |

These mappings preserve the same executable checks after alias
expansion. Provider host checks remain outside independent `check`, with the same exact certified
Core fixture and required CI matrix. No level, source scope, runtime dependency,
style exception or release lifecycle change is implied by these mappings.

## GitHub Provider certified-host evidence

The certified Core revision is
`ffc11fc8e40618624a785b7fca5193029c6d492e` (Booster `v1.0.0-beta.29`,
Provider API 11). The authoritative checkout and verification steps are in the
provider's [CI workflow at the refreshed default revision](https://github.com/RocketsAreNostalgic/ran-booster-github-provider/blob/7cd2c0624e2a41ccd8c2b1e879ac743eddb8f800/.github/workflows/ci.yml).

| Required lane | PHP | Evidence retained by command adoption |
| --- | --- | --- |
| `baseline` | 8.2 / 8.5 | Independent `composer check` and the shared parser sweep |
| `host-contract` | 8.2 | Exact package/Core SHA verification and `tests/host-contract.php` |
| `implementation` | 8.2 / 8.5 | Exact package/Core SHA verification, blocking level-1 PHPStan and implementation PHPUnit; `check:host` also repeats the host contract |
| `release-classification` | Node 24.11.0 | Required PR-title/release-significance classification |

All four job IDs remain dependencies of terminal `quality`. Local host evidence
requires setting `RAN_BOOSTER_CORE_PATH` and verifying the checkout equals the
certified SHA before invoking `check:host`; the host-contract test checks API
shape and does not itself authenticate the Git revision. A passing API-shape
test against another Core checkout is not equivalent certification.

## Remaining programme work

Release Updater #60's analysis inventory and coverage increments are complete:
all 36 shipped PHP files are directly analysed at level 8. See the matrix's
[coverage closeout checkpoint](PHP_QUALITY_MATRIX.md#release-updater-coverage-closeout-checkpoint--24-september-2026)
for exact-main CI, retained gates and remaining exceptions. Next is residual
standards/naming acceptance, with a fresh connected-caller/dependency plan before
API changes. Release #70 remains held; no release authorization follows from
coverage completion. Migrator release qualification remains separately owned.


- Starter supplies clean-reference evidence; Booster's coordinated Profile B
  migration supplies mature-reference evidence. The latter is not a prerequisite
  for the PR which produces it.
- The seven-package matrix plus Starter/Admin Shell was delivered by merged
  .github#70 and is refreshed alongside this ledger. Maintain it as slices land;
  do not recreate #70 or interpret the matrix as universal execution proof.
- Starter formatter consolidation and Support owned-method enforcement have
  landed. Remaining commands, consumer naming/condition debt, upgrades and
  proportionate drift validation stay under #65/#66 and the owning children.
  Core #54 now records completed release proof and handoff to #167;
  refresh that owning issue and its exact tuple before connected API work.
- Workbench and fixtures retain purpose-based exemptions. Plugin Library stays
  deferred; inactive repositories are not reactivated by this ledger.
