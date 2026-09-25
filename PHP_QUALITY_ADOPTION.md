# PHP quality command adoption

Owner: [#65](https://github.com/RocketsAreNostalgic/.github/issues/65).
Contract: [QUALITY_STANDARDS.md](QUALITY_STANDARDS.md#php-command-meanings).

This ledger records the initial bounded command-adoption slice and its
24 September 2026 landing checkpoints. The nine-repository dated
source/coverage/tool inventory and observed execution evidence live in
[PHP_QUALITY_MATRIX.md](PHP_QUALITY_MATRIX.md). Neither document declares full
suite acceptance, transfers active claims or substitutes a historical revision
for a fresh implementation baseline.

Routing reconciliation, 25 September: [#66](https://github.com/RocketsAreNostalgic/.github/issues/66)
is owner-closed delivery evidence, not an active queue. Its unresolved programme
responsibilities are explicitly retained in
[#65's residual-owner ledger](https://github.com/RocketsAreNostalgic/.github/issues/65#residual-programme-ownership-after-66-closure)
and the existing repository children, not waived or marked complete.

## Recorded landing checkpoints

| Repository / owner | Recorded revision | Canonical-command status at that checkpoint |
| --- | --- | --- |
| [Updater Support #35](https://github.com/RocketsAreNostalgic/ran-updater-support/issues/35) | `6a9cdbc9eb1bbecbafcbe16da931c98928d035e8` | [#36](https://github.com/RocketsAreNostalgic/ran-updater-support/pull/36) merged; `check`, `lint:syntax`, `standards`, `standards:fix`, `analyze`, `test` present. [#40](https://github.com/RocketsAreNostalgic/ran-updater-support/pull/40) additionally activates owned-method enforcement. |
| [Branch Updater #59](https://github.com/RocketsAreNostalgic/ran-wp-branch-updater/issues/59) | `d382d09e4490ed4438d9ebaea2a06d69d59f0ce3` | [#60](https://github.com/RocketsAreNostalgic/ran-wp-branch-updater/pull/60) merged; all six canonical names present. Installed no-dev consumer remains required in CI. |
| [GitHub Provider #25](https://github.com/RocketsAreNostalgic/ran-booster-github-provider/issues/25) | `7cd2c0624e2a41ccd8c2b1e879ac743eddb8f800` | [#26](https://github.com/RocketsAreNostalgic/ran-booster-github-provider/pull/26) merged; six canonical names and separate certified-host `check:host` present. |
| [Release Updater #60](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/issues/60) | `65b31c0aca26363a87180fa5f9ac7081fd661eb9` | [#66](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/pull/66) commands retained; local #67–#76 coverage sequence complete (excluding held release #70): all 36 shipped PHP files direct at level 8. Live audit, generated parity and no-dev proof retained; residual naming/standards remain owned locally. |
| [Migrator #42](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/issues/42) | `829d823afd87923a20f8170671d2f456465424d9` | [#46](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/pull/46) fixed parser/discovery failure propagation and added lint:syntax; lint:php retained for CI. No standards:fix or analyze yet at that checkpoint. [#45](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/pull/45) separately repinned release workflow. |

The original Support/Branch/Provider cohort declares PHP `^8.2` and uses shared
floor/current lanes at 8.2/8.5 at these recorded revisions. Support/Branch lock
coding-standards v1.0.0 at `6af816a02b7d1108ad5c990e9d0fda0af0a13de7`;
Provider locks the older `0b03e61a4bb558deeb6bc6b6399f44c0ec95e5be` candidate.
All retain PHPCS 3.13.6, WPCS 3.4.1 and explicit root PHPCompatibility alpha
requirements. Support has no WordPress analysis extension because its source
does not require one; Branch/Provider use it for WordPress source. Recorded
levels are 8, 5 and host-backed 1 respectively.

Post-merge evidence is linked in the matrix's
[24 September checkpoint](PHP_QUALITY_MATRIX.md#24-september-2026-landed-slice-checkpoint).
Provider command PR #26 is delivered; do not recreate it. Older rows remain
recorded adoption revisions, not a new estate-wide source audit. Refresh the
linked owner before changing source or a dependency/host composition.

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

These mappings preserve the same executable checks after alias expansion.
Provider host checks remain outside independent `check`, with the same exact
certified Core fixture and required CI matrix. No level, source scope, runtime
dependency, style exception or release lifecycle change is implied.

## GitHub Provider certified-host evidence

The certified Core revision in the recorded Provider checkpoint is
`ffc11fc8e40618624a785b7fca5193029c6d492e` (Booster `v1.0.0-beta.29`,
Provider API 11). Checkout and verification steps are in the
[exact Provider CI revision](https://github.com/RocketsAreNostalgic/ran-booster-github-provider/blob/7cd2c0624e2a41ccd8c2b1e879ac743eddb8f800/.github/workflows/ci.yml).

| Required lane | PHP | Evidence retained by command adoption |
| --- | --- | --- |
| `baseline` | 8.2 / 8.5 | Independent `composer check` and the shared parser sweep |
| `host-contract` | 8.2 | Exact package/Core SHA verification and `tests/host-contract.php` |
| `implementation` | 8.2 / 8.5 | Exact package/Core SHA verification, blocking level-1 PHPStan and implementation PHPUnit; `check:host` also repeats the host contract |
| `release-classification` | Node 24.11.0 | Required package-specific PR-title/release-significance classification |

All four job IDs feed terminal `quality` at that checkpoint. Local host proof
requires setting `RAN_BOOSTER_CORE_PATH` and verifying the certified checkout
before `check:host`; the host-contract test checks API shape, not Git identity.
A passing shape test against another Core checkout is not equivalent
certification. A later Core release does not automatically repin the Provider.

### Retained Provider title check, not a second release engine

At the recorded revision, the
[Provider's actual classification script](https://github.com/RocketsAreNostalgic/ran-booster-github-provider/blob/7cd2c0624e2a41ccd8c2b1e879ac743eddb8f800/scripts/release-classification.mjs)
requires a release-driving Conventional Commit title when a PR changes `src/`
or the production `require` map in `composer.json`. It accepts a type visible
in that package's Release Please changelog configuration or an explicit `!`
breaking marker. It does not calculate the next version, manage lifecycle
labels, publish a release or supply recovery authority. This is the narrow
product-specific rule deliberately retained in the
[#50 migration record](https://github.com/RocketsAreNostalgic/.github/issues/50#issuecomment-5778745871),
not the retired generic estate classifier. The linked CI revision binds a
candidate dispatch to the unique same-repository bot-owned Release Please PR
and exact head before applying that same title rule. Preserve this documented
boundary; neither retaining nor deleting an unrelated generic classifier is
implied by the job name.

## Remaining programme work and current handoffs

Release Updater's 36-file level-8 coverage and its matrix reconciliation landed
through local #76 and [organisation #82](https://github.com/RocketsAreNostalgic/.github/pull/82).
See the matrix's
[coverage closeout checkpoint](PHP_QUALITY_MATRIX.md#release-updater-coverage-closeout-checkpoint--24-september-2026)
for exact-main CI, retained gates and exceptions. Subsequent condition enforcement
landed in [Release Updater #77](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/pull/77);
its current owner [#60](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/issues/60)
records remaining naming/parameter/exception work and actual next claims. The
dated matrix is not a reason to repeat completed slices. Release Updater
[#70](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/pull/70) remains
held; coverage/condition success is not release authorization. Migrator
[#43](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/pull/43)
retains its separate exact-candidate installed-site acceptance.

- Starter supplies clean-reference evidence. Core's release migration and
  mechanical command handoff are complete under organisation #54; residual
  mature-reference quality stays with
  [Core #167](https://github.com/RocketsAreNostalgic/ran-booster/issues/167).
  Do not restore the completed release reservation or infer full quality adoption.
- The initial matrix came from merged organisation #70; later checkpoints are
  measured updates, not universal execution proof. Maintain them as slices land.
- Starter formatter consolidation and Support owned-method enforcement are
  delivered. Remaining commands, naming/condition debt, upgrades, live-audit
  policy, contributor coordination and proportionate drift proof stay under
  **#65 and the existing repository children**. Closed #66 supplies evidence,
  not an active backlog. Wider plugins use #67 and completed #61 handoffs.
- Connected API/dependency work still needs fresh claims and an installable exact
  composition. The separate template feature under #81 does not freeze
  unrelated quality work or grant authority over its branches.
- Workbench/fixtures keep purpose-based exemptions. Plugin Library stays
  deferred; no inactive repository is reactivated by this ledger.

Use fully qualified cross-repository links in handoffs and keep operative status
consistent with dated evidence. This documentation reconciliation changes no
check, package version, dependency, certification pin or active claim.
