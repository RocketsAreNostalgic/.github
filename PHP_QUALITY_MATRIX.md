# PHP quality acceptance matrix

Owner: [#65](https://github.com/RocketsAreNostalgic/.github/issues/65) with the existing repository quality children.
Closed [#66](https://github.com/RocketsAreNostalgic/.github/issues/66) is policy/tooling delivery evidence, not an active queue.
Delivered command policy: [#69](https://github.com/RocketsAreNostalgic/.github/pull/69).
Full source snapshot: 23 September 2026 (UTC); subsequent dated checkpoints
record scoped changes. Unchanged rows are not freshly requalified.

This records the seven active Booster PHP packages, Starter and Admin Shell at
the exact default revisions below. It is a configuration and execution-path
audit, not a fresh passing run of all nine suites or a declaration that every
row meets the adopted policy. Open migration PRs are recorded separately.
The manifests, locks, rulesets, analysis configurations, contributor contracts
and workflows at each linked revision are the source of each row.

## Release Updater residual acceptance checkpoint — 26 September 2026

This supersedes only Release Updater's older remaining-work descriptions.
Other repositories retain their dated evidence and owners.

| Evidence | Current disposition |
| --- | --- |
| Landed main | `58851628c93f554e89ae75bde9ee37e7cf57a5a9`, through result/proof cohorts [#86](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/pull/86)–[#88](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/pull/88). Post-merge [CI 36232990862](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/actions/runs/36232990862) and [Release Please 36233087302](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/actions/runs/36233087302) passed. |
| Landed scope | All 36 shipped PHP paths remain directly analysed at level 8. Conditions and reserved-parameter slices are landed. Owned-method naming is enforced for 11 completed files; variables for 10. Remaining naming is not waived. |
| Proposed archive/provider cohorts | [#89](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/pull/89) at `f81c0f237ad529167495859c8372bd66536ba0e7`; [#90](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/pull/90) at `e5e5554edeabd44da3c00089179f5d9f086eb134`. Native quality and separately requested code/security reviews passed. Copilot's three constructor-test findings on the provider PR are addressed by committed regression tests. |
| Proposed lifecycle/runtime cohort | [#91](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/pull/91) at `d7ef334d4c05c9213c3dd3b08f72f016af0f3b29`. Selected-state and broker naming must land with the explicit protocol-5 transition; the original protocol-4 mixed-copy finding is not waived. Current candidate/review evidence belongs to that PR. |
| Proposed final enforcement/exception acceptance | [#92](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/pull/92) at `e8ccef78b6ede66d77b82a0532ecc906d8ca533d`. Covers all 35 maintained production PHP files plus the two scripts through path rules, including future files. Generated helper parity/direct analysis and purpose-built fixture boundaries remain; retained exceptions are inventoried in its `QUALITY_ACCEPTANCE.md`. |
| Local execution limit | Portable PHP's two known `GLOB_BRACE` architecture errors are not a passing full aggregate. Native CI is separate evidence. All stronger runtime, archive, WordPress/MySQL, Windows, no-dev and live-audit gates remain. |
| Connected adoption | Core `0c1ace618331a23e068cec6e54a896c634bc8f76` still locks updater `0.1.0-beta.7`, declares protocol 4 and has two `protocolVersion()` assertions. Change the dependency, metadata and assertions together in a later installable adoption; no new Core tuple is certified here. |

The stack is proposed, not landed. After owner-authorized sequential merges,
record each actual main SHA and post-merge qualification, then reconcile this
checkpoint before closing [Release Updater #60](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/issues/60).
The package version is unchanged by these implementation PRs; the owner-held
[release #70](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/pull/70)
and subsequent Core adoption remain separate decisions. No programme-wide or
Migrator release closeout is implied.

## Current routing and superseded work selections — 25 September 2026

[#65's residual-owner ledger](https://github.com/RocketsAreNostalgic/.github/issues/65#residual-programme-ownership-after-66-closure)
retains the previously unchecked programme responsibilities from owner-closed
#66: matrix upkeep, upgrade/live-audit decisions, drift validation, contributor
coordination and reference/pilot acceptance. Closure did not waive that work or
complete consumer adoption. Existing repository children keep their claims.

Core's [#54 release handoff](https://github.com/RocketsAreNostalgic/ran-booster/issues/167#issuecomment-5819326356)
and all five [#61 WordPress handoffs](https://github.com/RocketsAreNostalgic/.github/issues/61)
are complete. Their former in-flight reservations no longer apply; residual
quality stays in [Core #167](https://github.com/RocketsAreNostalgic/ran-booster/issues/167),
organisation #67 and the local children. Refresh actual API/dependency/host
claims before overlap; completed release proof is not blanket mutation authority.

Release Updater's coverage and matrix reconciliation are delivered through
[local #76](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/pull/76)
and [organisation #82](https://github.com/RocketsAreNostalgic/.github/pull/82).
Its later [condition slice #77](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/pull/77)
removed the global Yoda suppression while retaining scoped fixture exclusions.
Follow [Release Updater #60](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/issues/60)
for remaining naming/parameter/exception work and subsequent exact evidence;
do not repeat the old inventory or treat the 24 September suppression list as
current. [Release Updater #70](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/pull/70)
remains held by the owner. [Migrator #43](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/pull/43)
retains its own exact-candidate installed-site acceptance.

The dated checkpoints below preserve measurements and historical next-work
selections, not current reservations or implementation assignments. This routing
correction runs no runtime suite and changes no policy, check, dependency, host
pin, release or active claim. Current operational routing is this section and
the linked owning issues, not superseded present-tense prose in an older snapshot.

## Release Updater coverage closeout checkpoint — 24 September 2026

This package-only checkpoint supersedes the older Release Updater coverage
statements below. Its then-pending matrix/condition work is superseded by the
25 September routing above. Other package rows remain dated evidence, not a fresh estate audit.

| Evidence | Verified disposition |
| --- | --- |
| Default revision | `65b31c0aca26363a87180fa5f9ac7081fd661eb9`, generated-helper [#76](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/pull/76) merged; tree `d61bd10d7fd69a74768d2440dee3088c3f6faea5` matches its reviewed head. |
| Direct analysis | All 36 shipped PHP files: `bootstrap.php`, `runtime.php` and 34 files under `src/`. PHPStan 2.2.13, WordPress extension 2.0.4, blocking level 8, no baseline. `scanDirectories` provides discovery in addition to explicit analysis roots. |
| Narrow PHPStan exceptions | Five declaration-local `property.unusedType` exceptions for resolver Reflection seams, one `method.unused` for the broker Reflection seam, one `phpstanWP.wpConstant.fetch` for sealed direct-filesystem policy. Bodies remain analysed. |
| Shared/generated ownership | coding-standards v1.0.0 at `6af816a02b7d1108ad5c990e9d0fda0af0a13de7`; updater-support beta.4 at `357db930b407941bd19a9e890c925d3d16ae9b15`. ArchiveSafety is directly analysed but retains its generated-code PHPCS exclusion and mandatory namespace-only parity check. |
| Commands and runtime | Six canonical commands retained; `check` still includes strict metadata, generated parity, live locked audit, syntax, PHPCS, analysis, unit and no-dev tests. PHPCS 3.13.6 / WPCS 3.4.1; PHP `^8.2`, WordPress floor 6.5. |
| Exact-main execution | [CI 36070662579](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/actions/runs/36070662579) and [Release Please 36070886402](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/actions/runs/36070886402) passed. Native PHP 8.2/8.5, WordPress 6.5/7.1, MySQL CAS, Windows and JavaScript still feed terminal quality. |
| Review and local limits | #76 head `3240ea32d38efa03ac10c5fa0111d7948a2aa0dc` received separate code/security reviews with no Codex findings. Copilot listed no findings despite its recommendation label. Local suite: 467 tests / 24,695 assertions, two portable-PHP `GLOB_BRACE` errors; native CI passed. Sequential no-dev proof passed after a concurrent fixture-copy race. |

The coverage sequence (#67–#69, #71–#76) is delivered; do not restart that
inventory or treat symbol discovery as the remaining state. At this checkpoint,
method/variable/Yoda suppressions remained, reserved-keyword parameter checks
were disabled, and `RANOwnedMethods` was not active. Later condition work is
recorded above; full standards/naming acceptance remains with the local owner.
Security, bootstrap and fixture exceptions remain distinct from migration debt.
PHPCS/PHPCBF scope matched, but configuration alone was not final
negative-control/repeated-fix evidence for the remaining naming scope.

Core [#54](https://github.com/RocketsAreNostalgic/.github/issues/54) records
completed beta.30 release proof and an explicit handoff to Core #167. Its older
open/no-handoff status below is historical. A connected naming/API cohort still
needs fresh ownership, caller and dependency/host composition evidence.

Release Updater [#60](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/issues/60)
remains open for residual acceptance; its coverage-matrix landing is complete
through organisation #82. [Release PR #70](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/pull/70)
is held until the agreed migration is complete; successful coverage CI does not
authorize a release. This checkpoint makes no new claim about Migrator's current candidate.

## 24 September 2026 landed-slice checkpoint

This checkpoint supersedes the older pending-command and syntax-defect statuses
in the 23 September snapshot below. Its historical next-work selection is itself
superseded by the current routing above. Other rows remain dated evidence, not a
fresh audit or execution of the whole estate.

| Package | Refreshed main / landed slice | Acceptance and evidence |
| --- | --- | --- |
| GitHub Provider | `7cd2c0624e2a41ccd8c2b1e879ac743eddb8f800`, [#26](https://github.com/RocketsAreNostalgic/ran-booster-github-provider/pull/26) | Canonical commands and separate `check:host` landed. Exact certified Core unchanged. [Post-merge CI](https://github.com/RocketsAreNostalgic/ran-booster-github-provider/actions/runs/35939652100) and [Release Please](https://github.com/RocketsAreNostalgic/ran-booster-github-provider/actions/runs/35939804562) passed. |
| Release Updater | `458b1c3a224498891145e6af9e7aeb27e2c881de`, [#66](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/pull/66) | `standards`, `standards:fix` and `test` landed; expanded `check` order unchanged. [Post-merge CI](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/actions/runs/35958345069) and [Release Please](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/actions/runs/35958519618) passed. Level-8 analysis still covers a subset, not all production PHP. |
| Migrator | `829d823afd87923a20f8170671d2f456465424d9`; syntax [#46](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/pull/46) merged at `79a0b742a4236fbb556262f0bb2f574cbc1965bb`, then release repin [#45](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/pull/45) | `lint:syntax` propagates parser/discovery failures; `lint:php` forwards for the retained CI caller. Negative regression rejects the original implementation. [Exact-head PR proof](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/actions/runs/35968489297), [syntax-merge Quality](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/actions/runs/35971723162) and [Release Please](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/actions/runs/35971969710) passed. No PHPStan or focused fixer adoption is claimed. |

All three quality slices received exact-head code/security review. Their runtime
source, locked dependency identities and certified hosts were preserved. Migrator's
new regression ran in the required PR baseline; the push-only local Quality job
does not independently rerun it. The #45 workflow repin is separate release work.

Support's owned-method enforcement and Starter's formatter consolidation remain
delivered evidence; do not restart them. The coding-standards v1.0.0 release and
initial four consumers are delivered, not estate-wide activation or Core adoption.
Starter main has since advanced to `f05f0c667eb950e692e9eb4f98480d40dfe1a76b`;
its older full matrix row below is deliberately retained as a dated audit.

### Historical next-work selection at that checkpoint — superseded

The following selection is retained as dated history, not operative instructions.
Use the current routing and local claims above instead.

- **Release gate:** Migrator [#43](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/pull/43)
  is the beta.10 release candidate, refreshed to
  `b7e178f38a411c3796a6d1e4851f1a6aa2555496` at this checkpoint. Automated
  candidate Quality passed ([run](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/actions/runs/35973714819)).
  Its `RELEASE.md` still requires exact-candidate reproducibility and fresh
  installed-site migration/refusal/recovery proof. Older candidate evidence
  cannot approve this candidate. No release merge/publication is authorised here.
- **Ownership gate:** Core [#54](https://github.com/RocketsAreNostalgic/.github/issues/54)
  remains open with no explicit handoff. Connected updater/provider/Migrator API
  naming and dependency/certification changes stay reserved.
- **Next independent slice:** read-only Release Updater [#60](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/issues/60)
  inventory mapping every shipped PHP file to direct level-8 analysis, symbol
  discovery, generated-copy exclusion, or uncovered scope. Produce a bounded
  coverage proposal; do not lower level 8 or silently promote coverage.
- **Separate later work:** Migrator command completion and PHPStan adoption,
  remaining consumer naming/condition choices, shared-package version adoption,
  Starter/Core reference acceptance, upgrade/live-audit policy, proportionate
  drift validation and contributor coordination with #62. Refresh ownership
  before implementation; do not churn Migrator's candidate during site proof.

## Historical audit — 23 September 2026

All remaining sections through the end of this document are historical evidence
at the linked 23 September revisions. Present-tense statuses and remaining-work
lists below describe that audit date, not current instructions or ownership.
The 24 September checkpoint above supersedes its command and parser statuses;
refresh the owning issues before selecting work. Do not restart delivered slices.

### Revisions and support contracts

| Repository / quality issue | Audited default revision | Declared PHP / WordPress | Configured PHP CI lanes |
| --- | --- | --- | --- |
| [Core #167](https://github.com/RocketsAreNostalgic/ran-booster/issues/167) | [000e1a55e8de95e381d6f4b9b3a98971119f336a](https://github.com/RocketsAreNostalgic/ran-booster/tree/000e1a55e8de95e381d6f4b9b3a98971119f336a) | `^8.2` / WP 7.0+ | 8.2; WordPress/database matrix separately |
| [Bitbucket #63](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/issues/63) | [001478d21098effec9219d4aae907762727b60b4](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/tree/001478d21098effec9219d4aae907762727b60b4) | `^8.2` / WP 7.0+ | Independent 8.2/8.5; host and installed proof 8.2 |
| [GitHub Provider #25](https://github.com/RocketsAreNostalgic/ran-booster-github-provider/issues/25) | [0e6911552f5b7e7d3812d0c03600037888e1dfd4](https://github.com/RocketsAreNostalgic/ran-booster-github-provider/tree/0e6911552f5b7e7d3812d0c03600037888e1dfd4) | `^8.2` / WP 7.0+ host contract | Independent and implementation 8.2/8.5; host contract 8.2 |
| [Branch Updater #59](https://github.com/RocketsAreNostalgic/ran-wp-branch-updater/issues/59) | [d382d09e4490ed4438d9ebaea2a06d69d59f0ce3](https://github.com/RocketsAreNostalgic/ran-wp-branch-updater/tree/d382d09e4490ed4438d9ebaea2a06d69d59f0ce3) | `^8.2` / no package-wide WP floor declared in PHPCS | 8.2/8.5; installed Composer consumer 8.2 |
| [Release Updater #60](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/issues/60) | [97a6fbdfcc47dc67b128a3a4007f39dc1d57c11f](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/tree/97a6fbdfcc47dc67b128a3a4007f39dc1d57c11f) | `^8.2` / WP 6.5+ | 8.2/8.5; Windows, MySQL and installed WP proofs 8.2 |
| [Updater Support #35](https://github.com/RocketsAreNostalgic/ran-updater-support/issues/35) | [6a9cdbc9eb1bbecbafcbe16da931c98928d035e8](https://github.com/RocketsAreNostalgic/ran-updater-support/tree/6a9cdbc9eb1bbecbafcbe16da931c98928d035e8) | `^8.2` / no WP runtime floor claimed | 8.2/8.5 |
| [Migrator #42](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/issues/42) | [e0bfcf2040e3d9159230d18ec24d30d21a40d160](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/tree/e0bfcf2040e3d9159230d18ec24d30d21a40d160) | `^8.2` / WP 7.0+ | 8.2 |
| [Starter #24](https://github.com/RocketsAreNostalgic/ran-starter-plugin/issues/24) | [0e8a5e6c71f8bd718603f0697efd07ee8e50e4a6](https://github.com/RocketsAreNostalgic/ran-starter-plugin/tree/0e8a5e6c71f8bd718603f0697efd07ee8e50e4a6) | `>=8.4 <8.6` / WP 7.0+ | 8.4; no 8.5 lane in the inspected caller |
| [Admin Shell #13](https://github.com/RocketsAreNostalgic/ran-admin-shell/issues/13) | [098cfd970f91c3701259fc393697b722d6e2546e](https://github.com/RocketsAreNostalgic/ran-admin-shell/tree/098cfd970f91c3701259fc393697b722d6e2546e) | `>=8.0`; build-time tooling; ruleset records WP 6.5 | 8.0/8.5 |

Declared support and executed versions are different evidence. The table does
not turn a missing CI version into an approved support exception, or impose a
WordPress runtime dependency on a host-neutral library.

### Locked tools

The eight shared-profile consumers lock PHPCS **3.13.6**, WPCS **3.4.1**,
`phpcompatibility/php-compatibility` **10.0.0-alpha2**,
`phpcompatibility/phpcompatibility-paragonie` **2.0.0-alpha2**, and
`phpcompatibility/phpcompatibility-wp` **3.0.0-alpha2**. Shared-package adoption
is no longer uniform:

| Consumers | Locked `ran/coding-standards` | Owned-method overlay |
| --- | --- | --- |
| Starter, Branch Updater, Release Updater | Released `v1.0.0`, `6af816a02b7d1108ad5c990e9d0fda0af0a13de7`, manifest `^1.0` | Not selected |
| Updater Support | The same released `v1.0.0` / `^1.0` | `RANOwnedMethods` explicitly enabled |
| Core, Bitbucket, GitHub Provider, Migrator | `dev-main`, locked `0b03e61a4bb558deeb6bc6b6399f44c0ec95e5be` | Not available in that older locked candidate |

Admin Shell also locks PHPCS **3.13.6** and WPCS **3.4.1**, but directly consumes
WordPress-Extra and PHPCompatibility **9.3.5**. It has neither the shared RAN
package nor the PHPCompatibilityWP/Paragonie packages in its lock.

| Repository | PHPStan | WordPress analysis extension | PHPUnit | Other PHP formatter |
| --- | --- | --- | --- | --- |
| Core | 2.2.8 | 2.0.3 | 11.5.56 | PHPCBF from the PHPCS lock |
| Bitbucket | 2.2.8 | 2.0.3 | 11.5.56 | PHPCBF |
| GitHub Provider | 2.2.14 | 2.0.4 | 11.5.56 | PHPCBF |
| Branch Updater | 2.2.13 | 2.0.4 | None; executable PHP contracts | PHPCBF |
| Release Updater | 2.2.13 | 2.0.4 | 11.5.56 | PHPCBF |
| Updater Support | 2.2.13 | None; source does not require it | None; executable PHP contracts | PHPCBF |
| Migrator | None configured | None | 11.5.56 | No focused fixer script exposed |
| Starter | 2.2.13 | 2.0.4 | 9.6.35 | PHPCBF only; PHP-CS-Fixer removed |
| Admin Shell | None configured | None | 9.6.36 | No focused fixer script exposed |

### Source coverage and analysis enforcement

Repository-wide PHPCS selections below retain their actual vendor, generated,
cache and local exclusions; they do not mean every file is checked under every
sniff. Narrow security/runtime exceptions remain in the referenced rulesets.
The four plugin consumers use `RANWordPressPlugin`; the four library consumers
use `RANWordPressLibrary`; Admin Shell retains direct ancestry.

| Repository | PHPCS source selection | PHPStan analysed paths and status |
| --- | --- | --- |
| Core | `.` excluding vendor, Node dependencies, workbench and caches/output | **Blocking level 1:** `autoload.php`, `index.php`, `ran-booster.php`, `uninstall.php`, `RAN/`. `views/` is not an analysis root. Vendored release-updater discovery is not analysed coverage. |
| Bitbucket | `autoload.php`, plugin entry, `src/`, `views/`; tests/scripts outside PHPCS selection | **Advisory level 3:** `autoload.php`, plugin entry, `src/`; host bootstrap required. `continue-on-error: true` applies to the analysis step. `views/` is not an analysis root. |
| GitHub Provider | `.` excluding vendor and analysis/test caches | **Blocking level 1 with certified host:** `src/` and `tests/foundation-contract.php`; not part of independent `check`. |
| Branch Updater | `src/` and `bootstrap.php`; fixtures/maintenance scripts intentionally use syntax and executable contracts | **Blocking level 5:** `src/`; bootstrap/tests/scripts are not analysis roots. |
| Release Updater | `.` excluding dependencies/caches/workspaces/output and generated `src/Dependency/ArchiveSafety.php`; parity checked separately | **Blocking level 8:** the exact subset below. `scanDirectories: src` supplies symbols and does not analyse all production PHP. |
| Updater Support | `.` excluding vendor/Node dependencies; `RANOwnedMethods` covers the same scope | **Blocking level 8:** `src/`. |
| Migrator | `.` excluding dependencies/Git/caches | No configured PHPStan gate; adoption remains a separate task. |
| Starter | `.` excluding vendor/Node dependencies, including Starter-local WordPress-Docs and generic checks | **Blocking level 1:** plugin entry, `uninstall.php`, `inc/`, `templates/`; `index.php`, tests and scripts are not analysis roots. |
| Admin Shell | `resources/`, `tools/`, `tests/`; WordPress-Extra excludes tools/tests, compatibility still applies | No configured PHPStan gate. Extensionless `bin/ran-admin-shell` is outside PHPCS roots and `*.php` syntax selection. |

Release Updater's level-8 roots in `phpstan.neon` are:

```text
src/Archive/
src/Contract/
src/WordPress/OwnedArchiveStore.php
src/WordPress/StagedPackageManifest.php
src/WordPress/PendingInstallState.php
src/WordPress/BindingState.php
src/Runtime/ReleaseFailure.php
src/Runtime/RequestProtocolValidator.php
src/Runtime/RuntimeCopySelector.php
src/Runtime/SelectedRuntimeState.php
src/Provider/GitHub/GitHubApiClient.php
src/Provider/GitHub/GitHubArtifactCustodyFailure.php
src/Provider/GitHub/GitHubArtifactStore.php
src/Provider/GitHub/GitHubCredentialResolver.php
src/Provider/GitHub/GitHubReleaseAdapter.php
src/Provider/GitHub/GitHubReleaseReadUnavailable.php
src/Provider/GitHub/ProspectiveReleaseArtifact.php
src/Provider/GitHub/ProspectiveReleaseInspection.php
```

#### Independent syntax surfaces

| Repository | Default-branch syntax path | Adoption consideration |
| --- | --- | --- |
| Core | Workflow sweeps repository PHP excluding vendor, Node dependencies and workbench with `find -exec php -l ... \;` | Child parser failure does not propagate from `find`; repair in coordinated command/wiring work. PHPCS is a separate check. |
| Bitbucket | `lint:syntax`: repository PHP excluding vendor and analysis/test caches, `find` piped to `xargs` | Child parser failure propagates; discovery failure is not protected by pipefail. |
| GitHub Provider | `lint:syntax`: `src/`, `tests/`, `find` piped to `xargs`; shared CI additionally sweeps repository PHP | Still no pipefail on main; open PR #26 supplies it. |
| Branch Updater | `lint:syntax`: `src/`, `tests/`, `scripts/`, then `bootstrap.php`; shared CI also sweeps repository PHP | Renaming and pipefail landed in #60. |
| Release Updater | `lint:syntax`: PHP runner covers `bootstrap.php`, `runtime.php`, `src/`, `scripts/`, `tests/`; shared CI also sweeps repository PHP | Uses `PHP_BINARY` and propagates parser exits; missing configured paths are currently skipped. Preserve Windows behavior when improving discovery checks. |
| Updater Support | `lint:syntax`: `src/`, `tests/`, `find` piped to `xargs`; shared CI also sweeps repository PHP | Renaming and pipefail landed in #36. |
| Migrator | `lint:php`: repository PHP excluding vendor/Node/Git using `find -exec`; shared PR CI also sweeps repository PHP | Standalone child-failure defect remains on the refreshed main after merged Profile B #41; quality #42 owns follow-up. |
| Starter | `lint:syntax`: repository PHP excluding vendor/Node/Git, through Bash pipefail and `xargs`; shared CI also sweeps repository PHP | Landed in #25; independent parser proof retained. |
| Admin Shell | No focused parser script; shared PHP CI sweeps repository `*.php` excluding dependencies | Include the extensionless CLI in its future explicit scope; do not assume the generic sweep covers it. |

The shared workflow parser loops reject failed `php -l` calls. Their file
enumeration uses process substitution; successful child checks alone are not
proof that discovery-error handling meets the new command contract. Preserve
those checks and assess discovery failure separately when hardening shared CI.

### Ordinary commands and additional required evidence

All commands in this table are read from the exact default-branch revisions
above. Support, Branch and Starter have adopted the canonical surfaces;
other rows retain the actual remaining differences.

| Repository | Local ordinary contract and focused commands | Additional CI / environment evidence to retain |
| --- | --- | --- |
| Core | `composer check` includes i18n/POT and fixture parity, localisation contract, characterization/PHPUnit/bootstrap tests, release-state/fallback contracts, immutable Admin Shell parity, `lint:php` and `analyze`; formatter `lint:php:fix`; `pnpm check` remains required | Published template-pack check; exact runtime archive and conditional candidate readback; WordPress 7.0/7.0.3 with MySQL 8.0/8.4 and MariaDB 10.11, activation/localisation/storage, updater execution, native-lock, hard-stop and intake-race proofs. Existing workflow has lifecycle-specific admission/skip logic. |
| Bitbucket | `check` is PHPCS + syntax. Host-backed `check:host` adds unit and release-candidate contracts. `analyze` is advisory; formatter `standards:fix` | Exact Core source/production autoloader; runtime archive, conditional candidate install and terminal `quality` fan-in. `installed-proof.yml` separately proves the certified Core/add-on installation; it is not a dependency of that fan-in. |
| GitHub Provider | Independent `check`: strict validation, syntax, PHPCS, foundation and Node release-control tests. Host-backed `analyze` and `test:implementation` separate; formatter aliases `format` / `format:php` / `standards:fix` | Exact certified Core contract, implementation PHP matrix, release classification and terminal `quality`. Proposed `check:host` in #26 retains these gates. |
| Branch Updater | `check`: strict validation, PHPCS, analysis, architecture/archive/prepared-archive/runner/hard-stop/journal/identifier/error-code and release-control contracts, syntax; formatter `standards:fix` | Installed no-dev Composer consumer plus the baseline feed terminal `quality`; no separate release-classification job remains. |
| Release Updater | `check`: strict validation, shared-copy parity, live `audit:composer`, syntax, PHPCS, analysis, unit tests and no-dev consumer. Focused `lint:php`, `format:php`, `analyze`; `pnpm check` covers Node control tooling | MySQL CAS isolation/setup-failure proof, Windows portability, installed WordPress 6.5/7.1 integration and terminal `quality`. No-dev install is already inside `check`; preserve it there during renaming. |
| Updater Support | `check`: strict validation, parser, `standards`, `analyze`, `test` aggregates archive-safety, owned-method regression and release-workflow tests; formatter `standards:fix` | Shared 8.2/8.5 profile and terminal `quality`; no certified host needed. |
| Migrator | `check`: parser, `standards`, PHPUnit and release-candidate contract; `pnpm check` covers shipped CSS | Single runtime archive and certified Core API proof. Merged #41 supplies Profile B wiring. Workflow retains non-archive PHP gates and a PR/dispatch terminal `quality`; do not recreate retired lifecycle machinery. |
| Starter | `check`: `lint:syntax`, `standards`, `test` (unit + quality contract), `analyze`; `standards:fix` is PHPCBF; build wrapper accepts PHPCBF exit 1; `pnpm check` includes generated-asset freshness | Shared WordPress profile plus project release-workflow/archive contract, built archive and installed WordPress activation; terminal `quality`. See [formatter investigation](STARTER_PHP_FORMATTER_AUDIT.md). |
| Admin Shell | `check`: PHPUnit render/sync contracts + `phpcs`; no Node/frontend command contract | Shared PHP floor/current validation and syntax; terminal `quality`. Preserve consumer-owned resource/provenance and distribution boundaries. |

An additional workflow existing does not establish that branch protection
requires it. This audit traces configured commands and dependencies; it does
not certify repository rulesets or organisation enforcement activation.

#### Certified hosts

- **GitHub Provider:** Core `ffc11fc8e40618624a785b7fca5193029c6d492e`, released
  `v1.0.0-beta.29`, Provider API 11. Its workflow verifies exact source and host
  SHAs before `host-contract` and implementation PHP 8.2/8.5. Local setup needs
  `RAN_BOOSTER_CORE_PATH` and explicit SHA verification.
- **Bitbucket:** the same tag-target SHA, with archive-source SHA
  `ff35be100a9f5c6cd77a84bcfc3734227106b0b8`, recorded in
  `extra.ran-booster-core-certification`. Install Core's locked production
  dependencies only and supply `RAN_BOOSTER_CORE_PATH` and
  `RAN_BOOSTER_CORE_VENDOR_AUTOLOAD`. Preserve Provider API 11 / Add-on API 16
  compatibility and the separate installed-archive proof.
- **Migrator:** default certification is Core `v1.0.0-beta.22`,
  `cd328286d8b00557f8400ffdcfb0549888ec76ca`, Portability API 2 / Admin
  Interaction API 2. The ordinary PHPUnit bootstrap is package-owned; the exact
  Core API check is a separate CI contract. This is not permission to point its
  ordinary tests at an arbitrary sibling or update its certification for naming
  symmetry.

#### Live audit and dependency resolution

Release Updater's `audit:composer` invokes `composer audit --locked
--no-interaction` inside `check`. Keep its existing failures blocking. Advisory
data and lookup availability can change without a lockfile change; this is not
offline deterministic evidence. The other eight inspected `check` graphs do
not invoke a live Composer audit. This inventory does not add one implicitly.
No-dev consumer proofs also run Composer resolution in isolated temporary
projects; retain their declared environment requirements and existing placement.

### Shared-package reconciliation and suite decisions

[`ran-coding-standards#1`](https://github.com/RocketsAreNostalgic/ran-coding-standards/issues/1)
tracks the existing package. [v1.0.0](https://github.com/RocketsAreNostalgic/ran-coding-standards/releases/tag/v1.0.0)
was published on 23 September at `6af816a02b7d1108ad5c990e9d0fda0af0a13de7`.
Shared Profile A / Release Please owns its lifecycle; do not recreate the
package or manually tag a replacement. The release retains the four baseline
profiles and adds opt-in `RANOwnedMethods`. Assignment/array alignment errors
remain blocking even with warnings hidden. Package availability, consumer
version adoption and owned-method activation are three separate facts.

| Current naming/condition disposition | Consumers |
| --- | --- |
| Broad owned-method/variable and Yoda suppressions remain | Core, Bitbucket, GitHub Provider, Branch Updater, Release Updater |
| Method/variable suppressions remain; Yoda exemption removed | Migrator |
| Pilot names/locals migrated; inherited WordPress variable/Yoda rules retained; additional owned-method check active | Updater Support |
| PHPCS/PHPCBF only, explicit blocking alignment and stronger docs/generic checks; owned-method overlay not selected | Starter |
| Direct WordPress-Extra on resources, with tools/tests outside those style rules | Admin Shell |

These suppressions describe migration debt, not newly approved permanent
exceptions. The normative policy requires WordPress snake_case for RAN-owned
methods, properties, parameters and locals, including public beta APIs.
Support needs no new Yoda waiver. Migrator's landed Yoda cleanup must not be
recreated. Condition-style convergence for the still-suppressed consumers
remains separate reviewed work. Preserve concrete external signatures and
local identity/runtime/security/fixture exceptions.

WPCS 3.4.1 skips method declarations in derived/implementing classes. Support
now tests the additional enforcement explicitly; neither a green WPCS check
nor merely locking v1.0.0 proves that boundary in other consumers. Do not
activate the overlay across unresolved connected APIs in a documentation PR.

The shared-package README retains the PHPCS 3/WPCS 3 boundary and explicit
root PHPCompatibility alpha requirements. Published-package adoption uses
reviewed installable lock updates; a PHPCS generation or analysis upgrade needs
separate qualification. Patch-version equality does not prove equal coverage.
Broader upgrade cadence and proportionate drift validation remain under #66.

### Execution evidence and remaining acceptance

The following existing runs were read from GitHub at the source refresh; this
documentation work did not rerun the estate. Each run reports success on the
exact audited default revision above. Configured lifecycle/advisory/conditional
gates retain their meaning; a successful workflow is not proof that every
conditional lane executed or that unadopted commands have landed.

| Repository | Observed main-run evidence |
| --- | --- |
| Core | [Quality 35840821194](https://github.com/RocketsAreNostalgic/ran-booster/actions/runs/35840821194) |
| Bitbucket | [Quality 35773826154](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/actions/runs/35773826154) and separate [installed proof 35773825376](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/actions/runs/35773825376) |
| GitHub Provider | [CI 35785696579](https://github.com/RocketsAreNostalgic/ran-booster-github-provider/actions/runs/35785696579); canonical-command #26 is still open |
| Branch Updater | [CI 35893102918](https://github.com/RocketsAreNostalgic/ran-wp-branch-updater/actions/runs/35893102918) |
| Release Updater | [CI 35893108548](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/actions/runs/35893108548) |
| Updater Support | [CI 35933082000](https://github.com/RocketsAreNostalgic/ran-updater-support/actions/runs/35933082000) and [Release Please 35933221013](https://github.com/RocketsAreNostalgic/ran-updater-support/actions/runs/35933221013) |
| Migrator | [Quality 35785701037](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/actions/runs/35785701037) |
| Starter | [Quality 35886298027](https://github.com/RocketsAreNostalgic/ran-starter-plugin/actions/runs/35886298027); same-SHA cancelled run is not the passing evidence |
| Admin Shell | No workflow run returned for the exact default SHA; PR-only caller. No new execution proof claimed. |

#### Landed slices and reference limitations

- Support command #36 and Branch command #60 are merged. Provider
  [#26](https://github.com/RocketsAreNostalgic/ran-booster-github-provider/pull/26)
  remains open at `c1a661e7c9ddb6ef2df982bdec2661f1ef1e7b68`; its historical green
  CI is not default-branch adoption or current-base qualification.
- Starter [#25](https://github.com/RocketsAreNostalgic/ran-starter-plugin/pull/25)
  merged at `4f712793653a338416046deae9a2146b745cf781`: PHP-CS-Fixer/config/callers
  removed, alignment retained in PHPCS, canonical commands and a negative/fix/
  repeatability contract added. Published-standard #27 then merged at the
  audited head. The [formatter audit](STARTER_PHP_FORMATTER_AUDIT.md) is historical
  rationale, not instructions to redo this consolidation. PHP 8.5 execution
  remains absent from Starter's inspected caller.
- Support #39, Branch #63 and Release #65 adopted real coding-standards v1.0.0.
  Support's subsequent [#40](https://github.com/RocketsAreNostalgic/ran-updater-support/pull/40)
  enables owned-method enforcement: reviewed `f5cc734f61f8c5d7dd371fe54cf4357efa4d6a5e`,
  merged `6a9cdbc9eb1bbecbafcbe16da931c98928d035e8`, identical tree
  `2bc41f8d75a4bdcb4ae91347a10a82486287247d`. Exact-head native PHP 8.2/8.5,
  code/security reviews and post-merge CI passed. Three positive/negative
  regressions cover inherited/implementing owned methods and narrow external
  signatures. Removing the opt-in fails the tests; two PHPCBF passes leave PHP
  byte-stable. No production exceptions were introduced.
- Support's naming pilot and direct-consumer adoption have shipped as Support
  beta.4, Branch beta.6 and Release beta.8. These are runtime-adoption evidence
  recorded in the owning issues, distinct from subsequent development-tool
  adoption and not permission to alter Core pins.
- Migrator Profile B #41 merged at `23ac6e35e8a521bfc5c4b2bc7a53698ec7df36c2`.
  Its refreshed main still has the standalone `find -exec` failure-propagation
  defect and no PHPStan gate; #42 owns these separate quality gaps.
- [Published-package reference proof](https://github.com/RocketsAreNostalgic/ran-coding-standards/issues/1#issuecomment-5796195966)
  records full Starter Composer/frontend checks, and isolated Core constituent
  PHP proof at `000e1a55e8de95e381d6f4b9b3a98971119f336a`. Core's original
  aggregate timed out in PHPCS; same-rule parallel PHPCS and normal-mode
  analysis subsequently passed. This is not a successful original aggregate,
  frontend/installed qualification, or a Core dependency adoption. Core still
  locks the older shared candidate. The live-main Quality run above qualifies
  that committed composition, not the isolated published-package experiment.

Remaining work: finish unlanded command surfaces (including Provider #26 and
Release Updater), parser failure/discovery handling, separately scoped analysis
adoption/coverage and advisory decisions, remaining shared-package consumers,
and naming/condition enforcement. #66 also retains upgrade/drift policy,
reference acceptance and contributor-documentation coordination with #62.
Core [#54](https://github.com/RocketsAreNostalgic/.github/issues/54) remains open
without an explicit handoff at refresh; connected API/cohort work stays reserved.
This matrix neither transfers those claims nor closes broader quality children.
Workbench/fixture exemptions and deferred/inactive repository dispositions remain.
