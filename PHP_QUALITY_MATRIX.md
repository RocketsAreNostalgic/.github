# PHP quality acceptance matrix

Owner: [#66](https://github.com/RocketsAreNostalgic/.github/issues/66), under
[#65](https://github.com/RocketsAreNostalgic/.github/issues/65).
Command-policy proposal: [#69](https://github.com/RocketsAreNostalgic/.github/pull/69).
Snapshot: 22 September 2026.

This records the seven active Booster PHP packages, Starter and Admin Shell at
the exact default revisions below. It is a configuration and execution-path
audit, not a fresh passing run of all nine suites or a declaration that every
row meets the proposed policy. Open migration PRs are recorded separately.
The manifests, locks, rulesets, analysis configurations, contributor contracts
and workflows at each linked revision are the source of each row.

## Revisions and support contracts

| Repository / quality issue | Audited default revision | Declared PHP / WordPress | Configured PHP CI lanes |
| --- | --- | --- | --- |
| [Core #167](https://github.com/RocketsAreNostalgic/ran-booster/issues/167) | [51613e42df959b76795a1b438de59a06053fb614](https://github.com/RocketsAreNostalgic/ran-booster/tree/51613e42df959b76795a1b438de59a06053fb614) | `^8.2` / WP 7.0+ | 8.2; WordPress/database matrix separately |
| [Bitbucket #63](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/issues/63) | [95c6b760acfdb75961ea9e1b76610a864c16b048](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/tree/95c6b760acfdb75961ea9e1b76610a864c16b048) | `^8.2` / WP 7.0+ | Independent 8.2/8.5; host and installed proof 8.2 |
| [GitHub Provider #25](https://github.com/RocketsAreNostalgic/ran-booster-github-provider/issues/25) | [ebeb6166b9806b006f1224fa5b291473040a0b86](https://github.com/RocketsAreNostalgic/ran-booster-github-provider/tree/ebeb6166b9806b006f1224fa5b291473040a0b86) | `^8.2` / WP 7.0+ host contract | Independent and implementation 8.2/8.5; host contract 8.2 |
| [Branch Updater #59](https://github.com/RocketsAreNostalgic/ran-wp-branch-updater/issues/59) | [15253ac03878b01da254d6702a9753103354d8e9](https://github.com/RocketsAreNostalgic/ran-wp-branch-updater/tree/15253ac03878b01da254d6702a9753103354d8e9) | `^8.2` / no package-wide WP floor declared in PHPCS | 8.2/8.5; installed Composer consumer 8.2 |
| [Release Updater #60](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/issues/60) | [a5efe7a422524000ed2ec7a7e16fba28b7c25b3a](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/tree/a5efe7a422524000ed2ec7a7e16fba28b7c25b3a) | `^8.2` / WP 6.5+ | 8.2/8.5; Windows, MySQL and installed WP proofs 8.2 |
| [Updater Support #35](https://github.com/RocketsAreNostalgic/ran-updater-support/issues/35) | [d395c37b2a76e5a5e10d9855b3277cde1cec4df3](https://github.com/RocketsAreNostalgic/ran-updater-support/tree/d395c37b2a76e5a5e10d9855b3277cde1cec4df3) | `^8.2` / no WP runtime floor claimed | 8.2/8.5 |
| [Migrator #42](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/issues/42) | [696ee7ed73a3782875205dc3b86419389dbab31a](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/tree/696ee7ed73a3782875205dc3b86419389dbab31a) | `^8.2` / WP 7.0+ | 8.2 |
| [Starter #24](https://github.com/RocketsAreNostalgic/ran-starter-plugin/issues/24) | [31f48fda13d7b9671f88d0ecf249af6aad251c52](https://github.com/RocketsAreNostalgic/ran-starter-plugin/tree/31f48fda13d7b9671f88d0ecf249af6aad251c52) | `>=8.4 <8.6` / WP 7.0+ | 8.4; no 8.5 lane in the inspected caller |
| [Admin Shell #13](https://github.com/RocketsAreNostalgic/ran-admin-shell/issues/13) | [098cfd970f91c3701259fc393697b722d6e2546e](https://github.com/RocketsAreNostalgic/ran-admin-shell/tree/098cfd970f91c3701259fc393697b722d6e2546e) | `>=8.0`; build-time tooling; ruleset records WP 6.5 | 8.0/8.5 |

Declared support and executed versions are different evidence. The table does
not turn a missing CI version into an approved support exception, or impose a
WordPress runtime dependency on a host-neutral library.

## Locked tools

Core, Bitbucket, GitHub Provider, both updaters, Updater Support, Migrator and
Starter all lock `ran/coding-standards` at
`0b03e61a4bb558deeb6bc6b6399f44c0ec95e5be`, PHPCS **3.13.6**, WPCS **3.4.1**,
`phpcompatibility/php-compatibility` **10.0.0-alpha2**,
`phpcompatibility/phpcompatibility-paragonie` **2.0.0-alpha2**, and
`phpcompatibility/phpcompatibility-wp` **3.0.0-alpha2**.

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
| Starter | 2.2.13 | 2.0.4 | 9.6.35 | PHP-CS-Fixer 3.95.15 and PHPCBF |
| Admin Shell | None configured | None | 9.6.36 | No focused fixer script exposed |

## Source coverage and analysis enforcement

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
| Updater Support | `.` excluding vendor/Node dependencies | **Blocking level 8:** `src/`. |
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

### Independent syntax surfaces

| Repository | Default-branch syntax path | Adoption consideration |
| --- | --- | --- |
| Core | Workflow sweeps repository PHP excluding vendor, Node dependencies and workbench with `find -exec php -l ... \;` | Child parser failure does not propagate from `find`; repair in coordinated command/wiring work. PHPCS is a separate check. |
| Bitbucket | `lint:syntax`: repository PHP excluding vendor and analysis/test caches, `find` piped to `xargs` | Child parser failure propagates; discovery failure is not protected by pipefail. |
| GitHub Provider | `lint:syntax`: `src/`, `tests/`, `find` piped to `xargs`; shared CI additionally sweeps repository PHP | PR #26 adds pipefail without changing source selection. |
| Branch Updater | `lint`: `src/`, `tests/`, `scripts/`, then `bootstrap.php`; shared CI also sweeps repository PHP | PR #60 renames and adds pipefail. |
| Release Updater | `lint:syntax`: PHP runner covers `bootstrap.php`, `runtime.php`, `src/`, `scripts/`, `tests/`; shared CI also sweeps repository PHP | Uses `PHP_BINARY` and propagates parser exits; missing configured paths are currently skipped. Preserve Windows behavior when improving discovery checks. |
| Updater Support | `lint:php`: `src/`, `tests/`, `find` piped to `xargs`; shared CI also sweeps repository PHP | PR #36 renames and adds pipefail. |
| Migrator | `lint:php`: repository PHP excluding vendor/Node/Git using `find -exec`; shared PR CI also sweeps repository PHP | Standalone child-failure defect remains in this default snapshot; coordinate with active Profile B PR #41, then quality #42. |
| Starter | No focused parser script; shared WordPress CI sweeps repository PHP excluding dependencies | Add canonical focused syntax command during adoption; retain independent CI proof. |
| Admin Shell | No focused parser script; shared PHP CI sweeps repository `*.php` excluding dependencies | Include the extensionless CLI in its future explicit scope; do not assume the generic sweep covers it. |

The shared workflow parser loops reject failed `php -l` calls. Their file
enumeration uses process substitution; successful child checks alone are not
proof that discovery-error handling meets the new command contract. Preserve
those checks and assess discovery failure separately when hardening shared CI.

## Ordinary commands and additional required evidence

All commands in this table are current default-branch names. Canonical command
adoption is proposed or outstanding, not silently treated as already landed.

| Repository | Local ordinary contract and focused commands | Additional CI / environment evidence to retain |
| --- | --- | --- |
| Core | `composer check` includes i18n/POT and fixture parity, localisation contract, characterization/PHPUnit/bootstrap tests, release-state/fallback contracts, immutable Admin Shell parity, `lint:php` and `analyze`; formatter `lint:php:fix`; `pnpm check` remains required | Published template-pack check; exact runtime archive and conditional candidate readback; WordPress 7.0/7.0.3 with MySQL 8.0/8.4 and MariaDB 10.11, activation/localisation/storage, updater execution, native-lock, hard-stop and intake-race proofs. Existing workflow has lifecycle-specific admission/skip logic. |
| Bitbucket | `check` is PHPCS + syntax. Host-backed `check:repository` adds unit and release-state contracts. `analyse` is advisory; formatter `lint:php:fix` | Exact Core source/production autoloader; runtime archive, conditional candidate install and `Quality` fan-in. `installed-proof.yml` separately proves the certified Core/add-on installation; it is not a dependency of that fan-in. |
| GitHub Provider | Independent `check`: strict validation, syntax, PHPCS, foundation and Node release-control tests. Host-backed `analyze` and `test:implementation` separate; formatter aliases `format` / `format:php` / `standards:fix` | Exact certified Core contract, implementation PHP matrix, release classification and terminal `quality`. Proposed `check:host` in #26 retains these gates. |
| Branch Updater | `check`: strict validation, PHPCS, analysis, architecture/archive/prepared-archive/runner/hard-stop/journal/identifier/error-code and release-control contracts, syntax; formatter `standards:fix` | Installed no-dev Composer consumer and release classification; both remain represented in terminal `quality`. |
| Release Updater | `check`: strict validation, shared-copy parity, live `audit:composer`, syntax, PHPCS, analysis, unit tests and no-dev consumer. Focused `lint:php`, `format:php`, `analyze`; `pnpm check` covers Node control tooling | MySQL CAS isolation/setup-failure proof, Windows portability, installed WordPress 6.5/7.1 integration and terminal `quality`. No-dev install is already inside `check`; preserve it there during renaming. |
| Updater Support | `check`: strict validation, parser, `standards`, `analyze`, archive-safety contract and release-workflow Node tests; formatter `standards:fix` | Shared 8.2/8.5 profile and terminal `quality`; no certified host needed. |
| Migrator | `check`: parser, `standards`, PHPUnit and release-candidate contract; `pnpm check` covers shipped CSS | Single runtime archive and certified Core API proof. Default workflow runs non-archive PHP gates separately and a PR terminal `quality`; release migration #41 owns replacement lifecycle wiring. |
| Starter | `check`: `lint` (`cs:check` + `standards:full`), PHPUnit and `analyze`; `format` runs `cs` then `standards:fix`; `pnpm check` includes generated-asset freshness | Shared WordPress profile plus project release-workflow/archive contract, built archive and installed WordPress activation; terminal `quality`. See [formatter investigation](STARTER_PHP_FORMATTER_AUDIT.md). |
| Admin Shell | `check`: PHPUnit render/sync contracts + `phpcs`; no Node/frontend command contract | Shared PHP floor/current validation and syntax; terminal `quality`. Preserve consumer-owned resource/provenance and distribution boundaries. |

An additional workflow existing does not establish that branch protection
requires it. This audit traces configured commands and dependencies; it does
not certify repository rulesets or organisation enforcement activation.

### Certified hosts

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

### Live audit and dependency resolution

Release Updater's `audit:composer` invokes `composer audit --locked
--no-interaction` inside `check`. Keep its existing failures blocking. Advisory
data and lookup availability can change without a lockfile change; this is not
offline deterministic evidence. The other eight inspected `check` graphs do
not invoke a live Composer audit. This inventory does not add one implicitly.
No-dev consumer proofs also run Composer resolution in isolated temporary
projects; retain their declared environment requirements and existing placement.

## Shared-package reconciliation and suite decisions

[`ran-coding-standards#1`](https://github.com/RocketsAreNostalgic/ran-coding-standards/issues/1)
is an existing implementation/release tracker, not a request to create another
standards package. Implementation PR #2 merged on 11 September. Its current
default revision is the same `0b03e61a...` candidate locked by the eight
consumers above. The package exports all four standards with the intended
inheritance; plugin/library profiles are currently thin named extension points.
It has a tracked lock, strict validation, structural/consumer-boundary checks,
positive and negative syntax/compatibility/prefix fixtures, stable-root install
proof and a separate fresh WordPress-consumer install in CI.

[Package CI run 34622592664](https://github.com/RocketsAreNostalgic/ran-coding-standards/actions/runs/34622592664)
succeeded on that exact default candidate. This is observed historical CI,
not a rerun. The package still has no published GitHub release at audit time.
Its consumer-install fixture's synthetic `1.0.0` version and README `^1.0`
example are not evidence of a released version.

Keep #1 open for explicit reference-consumer/release-evidence reconciliation and
the owner-controlled release decision. Do not recreate completed package work,
reopen completed organisation migration #7, or treat the newer command-policy
programme as a prerequisite for proving the older shared ancestry existed.
Current Starter/Core locks prove consumption, not full acceptance of the new
command and formatter contract.

| Existing convention | Consumers / disposition |
| --- | --- |
| camelCase methods/variables and non-Yoda accommodation | Core, Bitbucket, GitHub Provider, Branch Updater, Release Updater, Migrator: local, documented exceptions |
| camelCase accommodation while retaining inherited Yoda rules | Updater Support: actual divergence; no silent condition-style rewrite |
| Shared default naming/condition rules plus stronger docs/generic checks | Starter: retain its clean-reference identity and local exceptions |
| Direct WordPress-Extra on resources; tools/tests excluded from those style rules | Admin Shell: build-time role requires a deliberate scope decision |

No suite overlay or blanket suppression is approved by this matrix. Settle the
forward-looking Booster condition/naming convention under #66 with explicit
Updater Support disposition. Keep identity, runtime support, bootstrap/native
primitive, security and fixture exceptions local. A rule shared by six packages
is evidence to review, not authority to weaken the seventh.

The existing shared-package README owns the conservative PHPCS 3/WPCS 3 version
boundary. Keep reviewed root PHPCompatibility alpha requirements until an
equivalent consumer installation is proved. A versioned package release,
PHPCS-generation change or analysis upgrade requires its own reviewed lockfile
change and applicable Starter/Core evidence. Exact PHPStan patch equality is
not a substitute for comparable coverage and enforcement. A broader upgrade
cadence, suite overlay and drift automation remain open decisions under #66.

## Execution evidence and remaining acceptance

The command-adoption PRs below passed their required CI on these exact heads.
They were open at this snapshot; that evidence does not describe default-branch
adoption or approval of this documentation.

| PR | Tested head | Observed evidence |
| --- | --- | --- |
| [Updater Support #36](https://github.com/RocketsAreNostalgic/ran-updater-support/pull/36) | `035d5cca54e1be421d25581747a21d5988ef4ead` | [CI 35749459276](https://github.com/RocketsAreNostalgic/ran-updater-support/actions/runs/35749459276): PHP 8.2/8.5, terminal quality |
| [Branch Updater #60](https://github.com/RocketsAreNostalgic/ran-wp-branch-updater/pull/60) | `71e6f9787e1d52a2c402cc3775f48e11da128d2c` | [CI 35749475312](https://github.com/RocketsAreNostalgic/ran-wp-branch-updater/actions/runs/35749475312): PHP 8.2/8.5, installed consumer/classification, terminal quality |
| [GitHub Provider #26](https://github.com/RocketsAreNostalgic/ran-booster-github-provider/pull/26) | `c1a661e7c9ddb6ef2df982bdec2661f1ef1e7b68` | [CI 35749478950](https://github.com/RocketsAreNostalgic/ran-booster-github-provider/actions/runs/35749478950): PHP 8.2/8.5, host contract/implementation, classification, terminal quality |

Migrator's active Profile B PR #41 was separately observed at
`659199735d83eed1306fd8fc56ccc92340b2961a`. Re-audit its merged result before
applying #42; default-branch publisher tests listed above are not instructions
to restore retired machinery. The same rule applies to subsequent coordinated
Profile B consumers.

Remaining acceptance is source-specific: complete the canonical commands,
repair parser failure/discovery handling, decide Starter's formatter replacement
with behavioral proof, add evidenced analysis for Migrator/Admin Shell, expand
coverage and review advisory enforcement separately, settle suite style and
upgrade/drift policy, and reconcile exact reviewed heads after merges.
Workbench and fixtures retain their purpose-based exemptions; Plugin Library
and inactive repositories retain their separate recorded dispositions.
