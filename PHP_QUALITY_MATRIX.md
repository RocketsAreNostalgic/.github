# PHP quality acceptance matrix

The seven independent repositories in the satellite quality lane are tracked in the [satellite PHP quality matrix](SATELLITE_QUALITY_MATRIX.md). Starter's entries remain here.

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

## Convergence checkpoint — 3 October 2026

This checkpoint supersedes the earlier open/unmerged statuses below only for
the named changes. Historical candidates and unrelated rows remain dated evidence.

| Delivered proposal | Actual merge commit |
| --- | --- |
| [Migrator #55](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/pull/55): #121 naming and #122 released standards | `a0350f6b6056d1a52a37431a8ed1e9a2a08ac401` |
| [Admin Shell #20](https://github.com/RocketsAreNostalgic/ran-admin-shell/pull/20): stat-cache test repair | `f760a29a8106198fbba7b1bf804de03cd38227a4` |
| [Core #227](https://github.com/RocketsAreNostalgic/ran-booster/pull/227): retained-path audit | `90e632cbce245b291318163b0198bc1f06371c47` |
| [Matrix #125](https://github.com/RocketsAreNostalgic/.github/pull/125): tooling decisions and proposal evidence | `2074d678ed6144b4a532fb63e7dab9b2ee59ab66` |

The landed trees match their reviewed candidates. Core's exact merged-head
[Quality 37100129391](https://github.com/RocketsAreNostalgic/ran-booster/actions/runs/37100129391)
passed, including the installed WordPress/database matrix. This delivers the
retained-path inventory, not every disposition or a release-backed satellite certification.

The following documentation proposals remain **open/unmerged**:

- [Core #225](https://github.com/RocketsAreNostalgic/ran-booster/pull/225), base
  `90e632cbce245b291318163b0198bc1f06371c47`, head
  `351100f4feeabcba3661dfad1069ab4350c77d8b`: recovery history and Provider
  qualification notices reconciled; the superseded PHPCS comment delta is gone.
  [Independent review](https://github.com/RocketsAreNostalgic/ran-booster/pull/225#issuecomment-5966089745)
  is clear, all three findings are resolved, and exact-head
  [Quality 37100729061](https://github.com/RocketsAreNostalgic/ran-booster/actions/runs/37100729061)
  passed.
- [Starter #30](https://github.com/RocketsAreNostalgic/ran-starter-plugin/pull/30),
  base `3490bef147580e07b43ab0aa4691b24548adb159`, head
  `49a35cfe86c297b43c85bc08cdf0cd9e4a65d386`: unchanged one-line README
  version correction. Exact-tuple independent review remains clear; the
  [fresh readback](https://github.com/RocketsAreNostalgic/ran-starter-plugin/pull/30#issuecomment-5966058389)
  confirms manifest 0.1.2 and immutable published v0.1.2. No new runtime
  qualification is claimed for this documentation-only refresh.

The #120 source cleanup is proposed separately in
[Core #229](https://github.com/RocketsAreNostalgic/ran-booster/pull/229), base
`90e632cbce245b291318163b0198bc1f06371c47`, head
`16fe91f95d457f5ccb3fa88dc57a1d72923a52f9`. It removes the null-only artifact
limit argument and two unused Dispatcher constructor slots with verified callers
and regression coverage. Exact-tree local Composer checks pass (2,614 tests /
22,495 assertions), pinned frontend checks pass (193 tests), and archive
build/verification covers 443 PHP files. Native archive/installed qualification
and independent actual-PR review are pending at this checkpoint; no merge or
completion of remaining WordPress guards/persisted-state decisions is claimed.

The #122 alignment is separately proposed in
[Core #230](https://github.com/RocketsAreNostalgic/ran-booster/pull/230), base
`90e632cbce245b291318163b0198bc1f06371c47`, head
`e8de763e1389247f864e4854f27f5c44d894a0c1`. PHPStan 2.2.16, WordPress stubs
7.0.1 constrained to the 7.0 line, and WordPress extension 2.0.4 change three
development-package lock records; production package records are identical.
Local Composer checks pass (2,612 tests / 22,493 assertions), pinned frontend
checks pass (25 files / 193 tests), and the locked Composer audit reports no
advisories. Native qualification and independent actual-PR review remain pending.
See the [upgrade checkpoint](QUALITY_UPGRADES_AND_AUDIT.md#convergence-update--3-october-2026)
for the same-source diagnostic comparison; this is not an enforced-level increase.

[#124](https://github.com/RocketsAreNostalgic/.github/issues/124) remains separately
owned. Its diagnostic baseline is captured; the external agent's
[Core #228](https://github.com/RocketsAreNostalgic/ran-booster/pull/228), head
`d9940c36c6859d167d0868878093097b0dea5917`, is a separate unmerged proposal,
not duplicated by these lanes. PHPStan's enforced level remains 1. No level-5/8
zero-findings release gate, merge authorization, release approval or deferred
UI/manual acceptance is introduced. #111 remains retired; #118 remains completed.

## Standards integration and independent follow-up proposals — 3 October 2026

This checkpoint supersedes only the Core candidate's unmerged status below.
Core [#226](https://github.com/RocketsAreNostalgic/ran-booster/pull/226) landed by
owner-authorized squash at `0b724f5cb4b43c89a37fb0008df672488983550b`; its tree
`7783d2ed56743e9689a39657919ba65bb24a9215` matches the reviewed candidate.
[Post-merge Quality37077276282](https://github.com/RocketsAreNostalgic/ran-booster/actions/runs/37077276282)
passed archive, repository quality and all four installed WordPress/database
lanes. Matrix [#123](https://github.com/RocketsAreNostalgic/.github/pull/123)
landed normally at `c33eb0e2358c002232408ebba6f9c919aba659ff`, preserving its
reviewed tree. PHPStan remains level 1; no release or deferred product acceptance
is granted.

At this earlier checkpoint, the following proposals were **open/unmerged**;
the convergence checkpoint above records their subsequent disposition:

| Existing lane | Exact candidate / evidence | Remaining boundary |
| --- | --- | --- |
| #121 Migrator test/helper naming and #122 released standards | [Migrator #55](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/pull/55), base `024d8d5cbf35c46b196df06e053d08dbc542513b`, head `2cd1bc9f470ef981abdf8020ccef9f41cf1a83f5`; final-tree local Composer 130 tests / 1,633 assertions and pinned frontend checks pass; independent review is clear after six actual blanket-directive negative controls closed its finding. | Final-head canonical, independent review and native results are recorded on the PR; no released-Core recertification or manual migration acceptance is implied. |
| #120 retained compatibility audit | [Core #227](https://github.com/RocketsAreNostalgic/ran-booster/pull/227), base `0b724f5cb4b43c89a37fb0008df672488983550b`, head `59f3d66661c20ff24c1038ec19726d54225eeec8`; docs-only retained-path and individual WordPress-guard inventory. | Pending dispositions remain explicit; no runtime removal, newly executed runtime proof or issue closure. |
| #122 independent tooling decisions | [Dated tooling decisions](quality-evidence/tooling-decisions-20261003.md): retain Core Admin Shell and frontend quality-config pins for concrete consumer reasons; Migrator adopts released standards in #55. | Core PHPStan/stub changes remain held for the separately assigned #124 baseline. |
| #122 discovered Admin Shell test-harness repair | [Admin Shell #20](https://github.com/RocketsAreNostalgic/ran-admin-shell/pull/20), base `e7f3a479de0678e5f96cf37d13295cd3c1f6d5a7`, head `9718954a85b6c5a28ea6d0ad019427f707cead28`; local 26 tests / 173 assertions, [native Quality37078549073](https://github.com/RocketsAreNostalgic/ran-admin-shell/actions/runs/37078549073) and [independent review](https://github.com/RocketsAreNostalgic/ran-admin-shell/pull/20#issuecomment-5963191076) pass. | Test stat-cache invalidation preserves the absence assertion; no Core pin or production change. |

#124's Core/Provider level-5 and level-8 diagnostics retain their separate worker.
No higher-level zero-findings gate is introduced for beta.31. Releases, held
satellite certification and #81/#85 interactive acceptance remain paused/deferred
under their existing owners. #111 remains retired and #118 remains completed.

## Core whole-tree condition and parameter candidate — 2 October 2026

This checkpoint records the open [Core #226](https://github.com/RocketsAreNostalgic/ran-booster/pull/226)
candidate for [#119](https://github.com/RocketsAreNostalgic/.github/issues/119).
It is not landed acceptance; older dated snapshots and other repository rows
remain historical evidence, not a new implementation queue.

- **Exact candidate:** base `e0f7046521ad3c3b8ab265721efa27b53360d806`,
  head `7332d2103234f390c398b21755e7e9e7146e3ddc`, tree
  `7783d2ed56743e9689a39657919ba65bb24a9215`.
- **Effective scope:** Yoda conditions, unused parameters (including inherited
  and interface implementations), and reserved parameter names apply throughout
  owned PHP. The 29 all-rule test/harness suppressions are removed. Required
  native/public signatures, callback slots, implicit template uses and exact
  runtime/security fixtures retain specific explained exceptions. Seven
  positive/negative controls exercise the locked checker and reject blanket
  suppressions. [Core's scope inventory](https://github.com/RocketsAreNostalgic/ran-booster/blob/7332d2103234f390c398b21755e7e9e7146e3ddc/docs/php-standards-coverage.md)
  records the inherited WordPress-Extra/PHPCompatibilityWP/RAN profile and
  remaining boundaries; this does not imply every WordPress-Docs rule is active.
- **Qualification:** full local Composer checks pass on the exact final tree
  (2,612 tests / 22,493 assertions), including PHPCS, PHPStan, syntax, gettext
  and generated-asset verification. Unchanged frontend sources pass pinned
  Node 24.11.0 / pnpm 11.7.0 checks (25 test files). Independent
  [opened-PR review](https://github.com/RocketsAreNostalgic/ran-booster/pull/226#issuecomment-5962454910)
  found an installed-fixture artifact/slug collision; the final head corrects
  those two lines and has no remaining scoped review findings.
  [Final-head native run](https://github.com/RocketsAreNostalgic/ran-booster/actions/runs/37072481271)
  completed **SUCCESS**, refreshed 3 October 2026: Runtime archive, Repository
  quality, all four installed WordPress/database lanes and terminal Quality
  passed. Release-candidate-only readback is intentionally skipped for this
  source PR; installed qualification comes from the full WordPress matrix.
  This is source-candidate qualification, not release or product acceptance.
- **Unchanged boundaries:** PHPStan remains level 1 with existing shipped-file
  coverage; dependency locks, runtime API contracts and wire/storage keys are
  unchanged. Broader retained-path review [#120](https://github.com/RocketsAreNostalgic/.github/issues/120),
  Migrator helpers [#121](https://github.com/RocketsAreNostalgic/.github/issues/121),
  and development-tool alignment [#122](https://github.com/RocketsAreNostalgic/.github/issues/122)
  stay separate. #119, Core #167 and programme #65 are not closed by this proposal.
  The owner has paused release work; no merge, release, satellite certification
  or deferred UI/production-onboarding acceptance is granted.

## Migrator shipped-analysis coverage protection — 1 October 2026

This checkpoint supersedes only the Migrator coverage status below; previous
dated evidence and other owners' rows remain intact.

- **Landed:** [Migrator #50](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/pull/50)
  was owner-authorized squash-merged at `c5f1b7a9b6f6ed38f017d43a209cd9c0e921e010`
  from reviewed head `272c867cba23443ca7f7307d345b58e4549cdf34`, base
  `e343b536587ba860043e0dad827834b6b4f77966`. Landed tree
  `6e5256c001b33511d511e20069220731c15de1e0` matches the qualified candidate.
- **Protection:** required repository Quality downloads the existing single-build
  runtime ZIP, verifies its recorded digest and exact source metadata, and compares
  all shipped PHP with locked PHPStan 2.2.16 CLI discovery and source bytes. Imports,
  analysis/scan exclusions, file-extension filters and configured stub exclusions
  use the engine's semantics; scan-only declarations do not establish coverage.
  The current package's 15 PHP files pass. The aggregate's disposable real-builder
  control rejects a newly shipped, uncovered `assets/uncovered.php`, then proves
  imported direct selection, exclusions, stub/scan-only/extension handling and
  changed-byte refusal. Discovery must be reviewed on a future tooling upgrade.
- **Candidate qualification:** [Quality 36792967243](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/actions/runs/36792967243)
  passed all five jobs on PHP 8.2.34, including the actual downloaded ZIP guard;
  full aggregate: 102 tests / 1,096 assertions, clean level 6 and all retained
  certification negative controls. Local PHP 8.3.6 Composer/frontend/archive
  checks passed. Published-head local and native ZIP SHA-256 agree at
  `52ccbd05ef6fdc35e510e8b13fc602239f0aa8ed5fa4e42304d8170ffe3a2151`.
  [Hosted code review](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/pull/50#issuecomment-5921816268)
  found no major issues; no unresolved review threads. Separate hosted security
  review was usage-limited, not passed; the existing pre-publication deferral remains.
- **Post-merge:** [Quality 36793581236](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/actions/runs/36793581236)
  passed on the landed squash SHA: runtime archive, certified Core and repository
  Quality. PR-only baseline and terminal jobs intentionally skipped on push;
  the exact candidate supplied their passing evidence.
- **Boundaries:** runtime source/APIs, dependency locks, PHPStan level 6 and exact
  Core beta.22 `cd328286d8b00557f8400ffdcfb0549888ec76ca` certification are unchanged.
  [Release #43](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/pull/43)
  remains held for its existing owner's exact-candidate installed-site acceptance;
  no release publication occurred. [Migrator #42](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/issues/42)
  and programme #65 remain open for broader acceptance;
  Core #167 owns connected naming and level-7 typing stays separate. CI provisioning
  [research #111](https://github.com/RocketsAreNostalgic/.github/issues/111#issuecomment-5921835140)
  is a separate delivered report/proposal, with no consolidation rollout authorized.

## Migrator PHPStan adoption and release handoff — 30 September 2026

This scoped checkpoint supersedes older current-state readings of Migrator's
analysis gate and Release Please candidate below. Dated source snapshots remain
intact; other repository rows and owners are unchanged.

- **Migrator #48:** [PR #48](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/pull/48)
  squash-merged at `e343b536587ba860043e0dad827834b6b4f77966` from reviewed
  head `ef8e2fae4ba96ae9e0359fd2204a8ffd72c91080`; merge tree
  `ad870e408cb49bd46088a5246cc0c53eb96fb16e` exactly matches the qualified
  candidate. Blocking PHPStan level 6 targets PHP 8.2 and directly analyzes all
  15 shipped PHP files: recursive `src/` and `views/`, `index.php`, and the
  plugin entry point. It retains exact certified Core beta.22
  `cd328286d8b00557f8400ffdcfb0549888ec76ca`, Portability API 2 / Admin
  Interaction API 2. The new PHPStan development dependency and blocking
  analysis check are the intended quality changes. No runtime API or production
  dependency changed; the certified host, release allowlist, archive/runtime/
  host gates and published version are unchanged. Level 7's 14 boundary-typing
  findings remain separate
  later work.
- **Final-head qualification:** [Quality 36712916276](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/actions/runs/36712916276)
  passed all five jobs on PHP 8.2.34: shared baseline, runtime archive,
  certified Core contract, repository Quality, and terminal quality. The
  aggregate records 102 tests / 1,095 assertions, zero PHPStan errors, and the
  negative controls including replacement-tree refusal. Final-head code review
  completed without new findings; all three P2 threads were fixed, answered,
  and resolved.
- **Post-merge:** [Quality 36713631680](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/actions/runs/36713631680)
  passed on the squash SHA, including runtime archive, certified Core, and
  repository Quality. Its aggregate again records 102 tests / 1,095 assertions,
  clean analysis, and the negative controls. PR-only baseline and terminal jobs
  correctly skipped on push; the passing exact-candidate run supplies that
  evidence.
- **Security review:** hosted review was usage-limited and explicitly deferred
  by Ben until before public release. It is not a passing review.
- **Release handoff:** [Release Please 36713934298](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/actions/runs/36713934298)
  succeeded: exact Quality admission, Release Please, and candidate Quality
  qualification passed; exact asset download/promotion steps were skipped.
  [Release PR #43](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/pull/43)
  remains open at beta.10, head `c24777c7a54ba1f5ffcb40bd9c886eb8d8652188`,
  based on main `e343b536587ba860043e0dad827834b6b4f77966`. The separate
  exact-candidate installed-site acceptance hold remains outstanding; this
  workflow is not release approval.
- **Remaining ownership:** Migrator #42 remains open for separately owned
  command/naming acceptance and later level-7 boundary typing. Core #167 owns
  connected Core naming. Programme #65 remains open for broader acceptance.

## Branch bootstrap and Starter exclusion reconciliation — 30 September 2026

This scoped checkpoint supersedes the Branch coverage gap and Starter follow-up
in the 29 September audit. Other repositories retain their dated evidence.

- **Branch:** [#66](https://github.com/RocketsAreNostalgic/ran-wp-branch-updater/pull/66)
  squash-merged at `7bddf0791d4aefe0d5930422b642fca00d10db2d`.
  Blocking PHPStan level 5 directly selects all 36 `src/` PHP files plus
  `bootstrap.php` (37 production paths). The ordinary Composer tests run actual
  analysis in an isolated fixture: unchanged bootstrap passes; an injected
  undefined function must fail specifically on that bootstrap. Dependencies,
  runtime behavior and analysis level are unchanged.
- **Qualification:** reviewed head `465adb1e8dcdaca1ed028fb8b36bb5b159115d67`
  and merge share tree `0c98dcdefa3d0db482cad57338372c6bb709fd4a`.
  [Candidate CI 36700894675](https://github.com/RocketsAreNostalgic/ran-wp-branch-updater/actions/runs/36700894675)
  and [main CI 36702321759](https://github.com/RocketsAreNostalgic/ran-wp-branch-updater/actions/runs/36702321759)
  passed PHP 8.2, PHP 8.5, installed no-dev consumer and terminal quality.
  Independent final-head code review completed without suggestions or unresolved
  threads. Automated security review was usage-limited; Ben explicitly waived it
  for this PR and authorized squash merge. It is not reported as passed.
  [Release Please 36702477206](https://github.com/RocketsAreNostalgic/ran-wp-branch-updater/actions/runs/36702477206)
  succeeded; no new version or release PR resulted.
- **Starter:** at `3490bef147580e07b43ab0aa4691b24548adb159`,
  packaged [`index.php`](https://github.com/RocketsAreNostalgic/ran-starter-plugin/blob/3490bef147580e07b43ab0aa4691b24548adb159/index.php)
  contains only strict-types declaration and silence comments, with no plugin
  behavior. Its omission from direct PHPStan paths is an intentional, narrow
  no-behavior exclusion accepted by Ben on 30 September. It does not reopen
  [Starter #24](https://github.com/RocketsAreNostalgic/ran-starter-plugin/issues/24)
  or require a new analyzer regression. Reassess this disposition if executable
  behavior is added; no broader root-file exclusion is implied.

Branch's bootstrap slice is complete. Branch #59 and programme #65 remain open
for their separately owned connected-contract and broader acceptance work.

## Suite and Starter source reconciliation — 29 September 2026

This checkpoint supersedes current-state readings of older rows for the eight
revisions listed here. The satellite matrix remains authoritative for Admin
Shell and the other independent plugins. This is a source/configuration audit
and a recheck of existing GitHub run results, not a fresh execution of the suites.
Counts below enumerate tracked PHP selected by direct `paths` at the recorded
commit; they do not count symbol-discovery directories as analyzed production.

### Exact source, analysis and locked tools

| Repository / immutable main | Direct analysis and observed boundary | Locked PHPStan / RAN standards |
| --- | --- | --- |
| [Core `1e7611901a2966524886b8e6c14efc4f87a71101`](https://github.com/RocketsAreNostalgic/ran-booster/tree/1e7611901a2966524886b8e6c14efc4f87a71101) | 1; 345 tracked PHP paths. `autoload.php`, `index.php`, plugin/uninstall entrypoints, `RAN/`, `views/`, `assets/`; scan directory is symbol discovery. | 2.2.8 / v1.0.0 at `6af816a02b7d1108ad5c990e9d0fda0af0a13de7` |
| [Bitbucket `186ffd350854a528472cca66958a0a6011457834`](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/tree/186ffd350854a528472cca66958a0a6011457834) | 8; 20 tracked PHP paths. Entrypoint, autoloader, index, `src/`, `views/`; maintained-PHP scope guard is required. | 2.2.8 / v1.0.0 at `6af816a02b7d1108ad5c990e9d0fda0af0a13de7` |
| [GitHub Provider `d9f18a10d593d88d0373e377197553c02ee664f2`](https://github.com/RocketsAreNostalgic/ran-booster-github-provider/tree/d9f18a10d593d88d0373e377197553c02ee664f2) | 1; 23 production paths + foundation contract. `src/` and `tests/foundation-contract.php`; execution requires the pinned candidate Core host. | 2.2.14 / dev-main at `0b03e61a4bb558deeb6bc6b6399f44c0ec95e5be` |
| [Branch Updater `212a0d38dd7d766c6c8d8b7f29ebcf1de075802b`](https://github.com/RocketsAreNostalgic/ran-wp-branch-updater/tree/212a0d38dd7d766c6c8d8b7f29ebcf1de075802b) | 5; 36 `src/` paths. `src/` only; installed `bootstrap.php` is outside direct analysis. | 2.2.13 / v1.0.0 at `6af816a02b7d1108ad5c990e9d0fda0af0a13de7` |
| [Release Updater `27889528442fc4e49ca060959218d5ec288c3055`](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/tree/27889528442fc4e49ca060959218d5ec288c3055) | 8; 36 production paths. Both root runtime files and explicit production roots; `scanDirectories` is not the coverage proof. | 2.2.13 / v1.0.0 at `6af816a02b7d1108ad5c990e9d0fda0af0a13de7` |
| [Updater Support `6a9cdbc9eb1bbecbafcbe16da931c98928d035e8`](https://github.com/RocketsAreNostalgic/ran-updater-support/tree/6a9cdbc9eb1bbecbafcbe16da931c98928d035e8) | 8; two `src/` paths. `src/`; tests remain separately checked. | 2.2.13 / v1.0.0 at `6af816a02b7d1108ad5c990e9d0fda0af0a13de7` |
| [Migrator `829d823afd87923a20f8170671d2f456465424d9`](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/tree/829d823afd87923a20f8170671d2f456465424d9) | No PHPStan dependency, configuration or `analyze` command. Syntax fix is landed; missing analysis remains an open #42 acceptance item. | absent / dev-main at `0b03e61a4bb558deeb6bc6b6399f44c0ec95e5be` |
| [Starter `3490bef147580e07b43ab0aa4691b24548adb159`](https://github.com/RocketsAreNostalgic/ran-starter-plugin/tree/3490bef147580e07b43ab0aa4691b24548adb159) | 1; 36 selected tracked PHP paths. Entrypoint, uninstall, `inc/`, `templates/`; packaged `index.php` is outside direct analysis. | 2.2.13 / v1.0.0 at `6af816a02b7d1108ad5c990e9d0fda0af0a13de7` |

All eight locks retain PHPCS 3.13.6 and WPCS 3.4.1. Their local PHPCompatibility
ranges are 8.2+ except Starter's 8.4–8.5 range. Provider and Migrator still lock
the older RAN revision; this is pending consumer adoption, not permission to
rewrite an active owner's lockfile.

### Commands, host requirements and execution evidence

Each linked run's jobs were re-read on 29 September. Required jobs passed;
intentional skips are identified explicitly. A green run proves only the
configured scope at that revision.

| Repository | Required local/CI contract | Existing main evidence |
| --- | --- | --- |
| Core | `check`: i18n, tests, admin-shell, syntax, standards, analysis. PHP ^8.2; main native runtime evidence is PHP 8.2. | [36424780232](https://github.com/RocketsAreNostalgic/ran-booster/actions/runs/36424780232) — Runtime archive, repository/runtime lanes and terminal Quality passed; release-candidate readback skipped for ordinary main. |
| Bitbucket | Independent `check`: scope, standards, syntax/regressions. Required `check:host`: analysis, units, candidate validator, `check`. PHP ^8.2; Core beta.29 `ffc11fc8e40618624a785b7fca5193029c6d492e`. | [36580768684](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/actions/runs/36580768684) — Runtime archive, repository/runtime lanes and terminal Quality passed; release-candidate readback skipped for ordinary main. |
| GitHub Provider | Independent `check`: validation, syntax, standards, foundation/release tests. Required `check:host`: host contract, analysis, implementation tests. PHP ^8.2; candidate Core `3dfccf389fae6ee9e54e141f5b97b0d9b7aca2ff`, not released-host certification. | [36567027254](https://github.com/RocketsAreNostalgic/ran-booster-github-provider/actions/runs/36567027254) — All listed native quality jobs, including terminal `quality`, passed. |
| Branch Updater | `check`: validation, standards, analysis, tests, syntax. PHP ^8.2; PHP 8.2/8.5 plus installed no-dev Composer consumer. | [36360325595](https://github.com/RocketsAreNostalgic/ran-wp-branch-updater/actions/runs/36360325595) — All listed native quality jobs, including terminal `quality`, passed. |
| Release Updater | `check`: validation, Support parity, live Composer audit, syntax, standards, analysis, unit/no-dev tests. PHP ^8.2; PHP 8.2/8.5 plus Windows, MySQL and WordPress integration. | [36422014824](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/actions/runs/36422014824) — All listed native quality jobs, including terminal `quality`, passed. |
| Updater Support | `check`: validation, syntax, standards, analysis, contract/standards/release tests. PHP ^8.2; PHP 8.2/8.5. | [35933082000](https://github.com/RocketsAreNostalgic/ran-updater-support/actions/runs/35933082000) — All listed native quality jobs, including terminal `quality`, passed. |
| Migrator | `check`: syntax, standards, units and release/syntax contracts. PHP ^8.2; exact Core beta.22 `cd328286d8b00557f8400ffdcfb0549888ec76ca`, Portability/Admin Interaction API 2. | [35973387190](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/actions/runs/35973387190) — Runtime archive, certified Core contract and repository Quality passed; PR/dispatch-only baseline and terminal `quality` skipped on push. |
| Starter | `check`: syntax, standards, units/quality controls, analysis. PHP >=8.4 <8.6; native PHP 8.4/8.5 and WordPress 7.0 archive install/activation. | [36237308155](https://github.com/RocketsAreNostalgic/ran-starter-plugin/actions/runs/36237308155) — All listed native quality jobs, including terminal `quality`, passed. |

Bitbucket's separate [installed proof 36580766975](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/actions/runs/36580766975)
remains part of its accepted evidence. Provider's current main follows #30 and
its workflow explicitly uses candidate Core #177; it must not be described as
qualification against released Core or Core main. Core #193 is still a separate
open naming candidate, not part of the Core main row above.

### Remaining work and ownership

- **Branch bootstrap:** direct level-5 coverage and its regression landed in
  [Branch #66](https://github.com/RocketsAreNostalgic/ran-wp-branch-updater/pull/66);
  the 30 September checkpoint above records candidate/main CI and review evidence.
- **Migrator:** missing analysis is confirmed. [#42](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/issues/42)
  now has an active command-parity worker; PHPStan adoption is that lane's separate
  planned slice. Release #43 remains held for installed-site acceptance.
- **Starter:** the packaged `index.php` silence guard is an intentional narrow
  no-behavior exclusion, as recorded above. Closed #24 remains accepted; revisit
  the exclusion if this file gains executable behavior.
- **Core/Provider/Branch connected work:** remains with Core #167 and existing
  package owners. Main configurations and a candidate-host CI pass do not close
  public naming, dependency adoption or released-host certification.
- **Completed bounded lanes:** Bitbucket #78–#88 and central #102, Support #35,
  Release Updater #60, and Starter #24 remain completed as scoped. Their older
  historical rows are not a new implementation queue. Release/publication holds
  and owner-held UI acceptance remain unchanged.

This checkpoint does not complete the estate-wide #65 acceptance checklist.
Future-file drift protection and explicit per-repository exceptions still need
review where not already evidenced; the satellite guards and Bitbucket #88 are
bounded proofs, not an all-estate guarantee.

## Admin Shell acceptance checkpoint — 28 September 2026

This checkpoint supersedes the historical Admin Shell rows below. Other package
rows retain their own dated evidence and ownership.

| Surface | Current evidence |
| --- | --- |
| Landed source | Commands #14 at `dd8fbed71ad94578d8c96adb3f114e6d7babc349`; shared standards #15 at `3453fdb73532bf355c9e8dd0a230c0eac6118492`; blocking analysis #16 at `aea62ff76281f776fb986cb47d9ece620457c166`. |
| Role/support | Build-time Composer library; PHP >=8.0, locked platform 8.0.30; resources model WordPress 6.5. No runtime library/plugin registration or consumer lock adoption. |
| Locked tools | RAN v1.0.0; PHPCS 3.13.6; WPCS 3.4.1; PHPCompatibility 10.0.0-alpha2, Paragonie 2.0.0-alpha2, WP 3.0.0-alpha2; PHPStan 2.2.16; WP stubs 6.5.7; PHPUnit 9.6.36. |
| Commands | `check` = `lint:syntax`, `standards`, `analyze`, `test`; `standards:fix` runs both matching resource/tooling rulesets and correctly handles successful PHPCBF exit 1. |
| Standards/syntax | Resources use RANWordPressLibrary; standalone CLI/tools/tests use RAN + PHPCompatibility without WordPress polyfills. Syntax additionally covers preview fixtures and explicitly discovers the extensionless CLI. Real-binary negative/fix/repeatability and failure-propagation tests are retained. |
| Analysis | Blocking level 5, PHP 8.0 target, 512 MB; all six maintained PHP paths: CLI, renderer and four tools. WordPress stubs/PHPCS source are symbol discovery only. No baseline or ignored errors. Tests/preview fixtures retain their separate gates. |
| Analysis limit | Level 6 measured 28 missing parameter/return/iterable-value declarations in SyncCommand. A future ratchet is separate from accepting the evidenced level-5 floor. |
| Distribution acceptance | [Admin Shell #17](https://github.com/RocketsAreNostalgic/ran-admin-shell/pull/17), merge `85902698496e7e40ae876e7b98733a7d0ab810d9`, reviewed head `483c06433e2210c6a5d38ad095fe8ea1c9f3904a`, identical tree `d0934bbe9c4957e89b81d1fc7179a7849de7c61f`: committed export installed by real Composer, immutable metadata/provenance and drift negatives, stable synchronization, no-dev removal preserving consumer bytes. Dist installation and every installed file are verified; repository agent instructions are excluded. |
| Execution/reviews | #16 exact-head Quality 36237161226 passes PHP 8.0/8.5 and terminal quality; zero unresolved threads; final-head automated code review and fresh manual security reconciliation recorded on the PR. Its automated security summary remained stale and is not represented as a new automated review. #17 local PHP 8.4.23 aggregate passes 22 tests / 145 assertions and native PHP 8.0/8.5 CI passes; final-head code review and fresh manual source-security assessment are recorded on #17; the late metadata finding is resolved by #18 below. |
| Metadata follow-up | [Admin Shell #18](https://github.com/RocketsAreNostalgic/ran-admin-shell/pull/18), merge `7de4946cfe6be6a3da854d576cedd45e385d2ebd`, head `368d2d855285706484d26c8803f5d1f226584ca7`, identical tree `5427fb59abccebe59a2e0652c675108b3be0a661`: exported Composer manifest is preserved and runtime-loading metadata rejected. Exact-head aggregate: 22 tests / 149 assertions; native PHP 8.0/8.5 [Quality 36420326724](https://github.com/RocketsAreNostalgic/ran-admin-shell/actions/runs/36420326724) and separate exact-head code/security reviews pass. A committed `autoload.files` negative control fails the actual distribution test. All #17/#18 review threads are resolved. |
| Protected contract | Updated `quality-enforcement/contracts.json` for the accepted tree, including tooling rules, analyzer config, CLI/tools and archive attributes. Registry validation is separate from live ruleset activation; no settings/enforcement rollout is claimed. |

The local workflow is PR-only: matching merge-tree identity carries the reviewed
proof, and no separate post-merge workflow is invented. Actual plugin release
allowlists, installed WordPress and deferred UI acceptance remain consumer-owned.
No package tag, Packagist publication or consumer adoption is included here.

## Bitbucket maintained-PHP coverage drift checkpoint — 29 September 2026

This is the current Bitbucket source checkpoint. The owned-naming checkpoint below
remains historical evidence for #78–#87. [Bitbucket #63](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/issues/63)
is closed bounded history; #65 retains residual programme acceptance.

| Disposition | Exact evidence |
| --- | --- |
| Merged source | [#88](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/pull/88) squash/main `186ffd350854a528472cca66958a0a6011457834` from reviewed head `8522a6080da09fe03f048e6d82329f2b9ee001b0`, identical tree `e17b74f4b1e1532c22f755710dc505fdbd8a65f8`. #78–#87 remain merged. Core-independent `check` now discovers maintained product PHP and checks direct PHPStan and PHPCS/PHPCBF selection; inherited `check:host` retains the guard. Tests and purpose-built fixtures have separate scope. |
| Candidate evidence | Exact-head Quality `36569540954` and certified-Core installed proof `36569540260` passed. Local host aggregate passed PHPStan level 8/all 20 shipped paths, 197 tests / 2,250 assertions, release-candidate validator 1 valid / 12 invalid, PHPCS, syntax and actual-Composer negative controls for new product paths and narrowed/excluded configuration. Exact published-head archive SHA-256 `ad1855d1fe5cdacae2f1cdd1af5b872e61cf06dc80b421bf9299d22bdaeccda3`. Eight P2 code findings were fixed and resolved; final code review clear and zero unresolved threads. Hosted security review returned a usage limit, not a pass; the owner authorized #88 squash merge with this disclosed. |
| Current main checks | Post-merge [Quality 36580768684](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/actions/runs/36580768684) and [certified-Core installed proof 36580766975](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/actions/runs/36580766975) passed on the squash commit. [Release Please 36581061893](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/actions/runs/36581061893) passed on the squash SHA; release automation is not publication authority. |
| Open / held | No Bitbucket implementation PR remains open. [Release #75](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/pull/75) remains held at `e6a6632305a8f799c2a04b843bd27bdb6cf7976a`; dispatched Quality `36555896639` passed, while bot PR Quality `36555899650` and installed proof `36555898585` were action_required. Its merge/publication requires a separate decision. |

The PHP 8.2/8.5, WordPress 7.0+, certified Core beta.29, API 11/16,
runtime, archive and installed-host gates remain. This local guard does not close
estate-wide coverage/reference drift or Core #167 connected compatibility.

## Bitbucket owned-naming checkpoint — 29 September 2026

This checkpoint supersedes older Bitbucket statements that shared-standard
adoption and owned naming are wholly planned. It distinguishes delivered main
from open candidates; it does not certify the connected Core naming migration.
Bitbucket #63 remains closed bounded history, with residual acceptance and live
ownership in [#65](https://github.com/RocketsAreNostalgic/.github/issues/65).

| Disposition | Exact evidence |
| --- | --- |
| Merged baseline | Main `99f8159579b783656dae83478f7fc3a17a31f016` through #87. #78 adopts coding-standards v1.0.0; #79–#86 migrate owned identifiers through Provider/Validator; #87 enforces naming across current and future production files, removes four local blanket suppressions and includes index.php. All twenty shipped PHP paths are directly checked. #87 reviewed head `7916ff141dde0bb2be8c972fed755d0a61fb1859` preserved tree `7f6301470100030ff8c8c4daf02f961d66228988`. |
| Candidate proof | #87 exact-head Quality `36533617240` passed runtime archive, PHP 8.2/8.5, repository quality and terminal Quality; certified-Core installed proof `36533611031` passed. Local host aggregate 197 tests / 2,247 assertions, candidate validator 1 valid / 12 invalid and exact-head archive SHA-256 `3476b7221866380164708a4b94201391c6977927223f4cfd336474d65f41caff` passed. Eight actual-command negative controls, fixture/future-class positives, autoloader token parity and two byte-stable fixers passed on the byte-identical candidate tree. Final-head code review clear, zero review threads; hosted security review returned a usage limit and is not represented as passing. The owner made the #87 merge decision with that limitation disclosed. |
| Current main checks | #87 post-merge Quality `36555639339`, certified-Core installed proof `36555638521` and Release Please `36555856368` passed on the actual squash commit. #86's post-merge runs also passed historically. Source qualification is distinct from release publication. |
| Held release | [Bitbucket #75](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/pull/75) at `e6a6632305a8f799c2a04b843bd27bdb6cf7976a`: dispatched exact-candidate Quality `36555896639` passed, including release-candidate installed readback; bot pull_request Quality `36555899650` and installed proof `36555898585` remain action_required. Separate release/publication decision required. |

The locked standard is v1.0.0 at
`6af816a02b7d1108ad5c990e9d0fda0af0a13de7`. Blocking PHPStan 8 directly covers
all 20 shipped PHP paths. PHP 8.2/8.5 lanes, WordPress 7.0+, Provider API 11 /
Add-on API 16 and exact certified Core beta.29
`ffc11fc8e40618624a785b7fca5193029c6d492e` remain unchanged. Independent
`check` runs standards, syntax and the syntax/discovery regression;
`check:host` additionally requires analysis, units and candidate validation.
Archive and certified installed-host proof remain mandatory. No new audit gate,
version bump, dependency change, runtime guard removal or publication is bundled.

The precise Core method/parameter/DTO exceptions remain connected-contract debt
owned by Core #167. Tests and purpose-built fixtures retain separate scope.
Future-file enforcement, a green formatter, or completed local renames do not
close programme-wide matrix/drift/reference or connected compatibility
acceptance. Upgrade/live-audit policy was delivered through organisation #97;
future policy or consumer changes require their own reviewed evidence. Refresh
live owning issues before selecting another implementation slice.

## Bitbucket syntax and condition acceptance — 28 September 2026

Historical Bitbucket source checkpoint: `6c9e4c44bc1832495913826e999fb091701184dd`.
The owned-naming checkpoint above supersedes its current-status statements.
This supersedes pending syntax/condition work in the dated analysis checkpoint
below. Residual acceptance remains with [#65](https://github.com/RocketsAreNostalgic/.github/issues/65);
[Bitbucket #63](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/issues/63)
stays closed with its operative handoff at the top.

| Disposition | Evidence / boundary |
| --- | --- |
| Merged: syntax failure propagation | [Bitbucket #76](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/pull/76), merge `2d8bd45c56f398941a81d691363fb38ca2cb4f35`, reviewed head `0967a41707c1dc4c652f0c4bc44e524f211f986f`. Parser, discovery and empty-selection failures propagate; disposable actual-command regression runs in independent `check`. Restoring the previous command fails that regression. |
| Merged: Yoda conditions | [Bitbucket #77](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/pull/77), merge `6c9e4c44bc1832495913826e999fb091701184dd`, reviewed head `2593cb8fa7451fc9aa1d8725f77908e2ad377637`, identical tree `88e8a80beac1ce9db675d27fcfc79959a44a3db2`. Removes only the Yoda exclusion and reverses one side-effect-free strict pagination comparison. |
| Retained proof | Blocking level 8 on all 20 shipped PHP paths; full local host aggregate 196 tests / 2,241 assertions; candidate validator 1 valid / 12 invalid. Pagination characterization passes before/after (3 tests / 40 assertions). Old-condition negative control fails actual `composer check`; two canonical fixer passes are byte-stable. |
| Exact candidate / reviews | #77 archive SHA-256 `000de37206f6e2b0855af992b4e83010165f8230dc185858ad2133befe97304f`; native Quality [36409871859](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/actions/runs/36409871859) and installed proof [36409871139](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/actions/runs/36409871139) pass. Separate exact-head code/security reviews are clean; no unresolved threads at merge. |
| Open / held | No Bitbucket implementation PR remains open at this batch checkpoint. Release Please [#75](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/pull/75) is separate and held; this row does not qualify it or authorize publication. |
| Planned, not claimed | Shared-standard version adoption and scoped owned-name migration require fresh caller/exception inventory and coordination with Core #167. The locked standard predates inherited-method enforcement. Broader naming, matrix/drift/reference and upgrade/audit policy acceptance remain open. |

#76 post-merge Quality `36409469777`, installed proof `36409469189` and
Release Please `36409701513` all passed. #77 post-merge Quality [36412770675](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/actions/runs/36412770675)
and installed proof [36412770199](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/actions/runs/36412770199)
passed on the actual merged commit. Release Please
[36412933793](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/actions/runs/36412933793)
failed at its exact-candidate Quality step after updating #75. The release head
`3d1f92b8e280679495b1b55d90f21a1e1a99e55a` has Quality `36412970741` and
installed proof `36412970176` at `action_required`; its qualification remains
blocked. This is separate from the passing merged-source checks, and no release
publication occurred.
Core beta.29 certification, PHP 8.2/8.5 lanes, WordPress support, Provider API
11 / Add-on API 16, dependency locks and publication controls are unchanged.
The organisation level-8 matrix PR [#91](https://github.com/RocketsAreNostalgic/.github/pull/91)
also merged at `eee0c8246c51de78e3c246e73cb7e5877703c907` using the owner's
one-off regular-merge exception; that exception is not general merge authority.
Other package rows and historical inventory counts are not requalified here.

## Bitbucket level-8 acceptance — 28 September 2026

This records the landed level-8 analysis checkpoint; the syntax/condition
checkpoint above supplies the later batch disposition. Earlier coverage/enforcement
checkpoints below are historical. [Bitbucket #74](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/pull/74)
landed at `7b87a77eb98b16aa163c28358386605f28860d5b` from reviewed head
`bf5bb55485e1c856f85dd368460fd356c5341e5d`, preserving tree
`dd4187aca4f0501de881bba7d442def35016966c`.

| Acceptance surface | Landed evidence |
| --- | --- |
| Direct analysis | Blocking PHPStan level 8: `autoload.php`, plugin entrypoint, `src/`, `views/`, `index.php`; all 20 shipped PHP paths match the archive inventory. Directory roots cover future PHP files. |
| Locked tools | PHPStan 2.2.8, phpstan-wordpress 2.0.3, wordpress-stubs 6.9.4, PHPUnit 11.5.56, PHPCS 3.13.6, WPCS 3.4.1; RAN standards remain locked at `0b03e61a4bb558deeb6bc6b6399f44c0ec95e5be`. |
| Runtime / certified host | PHP 8.2+, WordPress 7.0+, Provider API 11 / Add-on API 16. Core beta.29 tag target `ffc11fc8e40618624a785b7fca5193029c6d492e`, archive source `ff35be100a9f5c6cd77a84bcfc3734227106b0b8`, production dependencies only. |
| Commands | Independent `check` retains PHPCS/syntax. Required `check:host` runs `analyze`, unit tests, candidate validator and `check`; native Repository quality feeds terminal Quality. `standards` / `standards:fix` use the same PHPCS/PHPCBF ruleset. Separate certified installed proof remains required evidence. |
| Positive / negative analysis | Every intermediate level 3–8 clean. Nullable method-call probe passes 3/7, fails default `analyze` and `check:host` at 8 before tests; probe removed. |
| Behaviour / archive | 196 tests / 2,238 assertions; candidate validator 1 valid / 12 invalid, PHPCS, syntax, strict Composer validation and exact-candidate archive verification pass. |
| Native / review | PHP 8.2/8.5, repository, runtime archive, terminal Quality and certified-Core WordPress 7.0.3 installed proof pass. Separate exact-head code/security reviews and Copilot have no actionable findings; zero unresolved threads at merge. |

The preceding #70–#73 slices documented the section return shape, removed three
checks redundant against a native array type, modelled the filterable HTTP
response as `mixed` with an analysis-only stub, and removed the redundant
`method_exists()` after `is_wp_error()` narrowing. Nested response/ref validation,
transport classification and hostile-input guards remain. The level promotion
itself changed only configuration and four guidance files: no new suppressions,
production casts, dependency/host/API changes or coverage exclusions.

Successful post-merge runs on the actual merged commit:
[Quality 36404964013](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/actions/runs/36404964013),
[Certified Core installed proof 36404962903](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/actions/runs/36404962903),
and [Release Please 36405203248](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/actions/runs/36405203248).
This records implementation acceptance, not publication: the latest published
artifact at this checkpoint is still v0.1.0-beta.14. Release PR #75 is separate.

At this earlier checkpoint, shared-standard adoption, naming/condition acceptance
and a reproduced `lint:syntax` discovery-failure defect remained open. The syntax
and Yoda items subsequently landed in #76/#77 as recorded above; owned naming,
shared-standard adoption and programme matrix/drift/reference policy remain open. The old locked
standard also predates inherited-method enforcement; green configured PHPCS is
not proof of completed naming. Tests/fixtures retain their purpose-built scope.
Other package rows are not requalified by this checkpoint.

## Bitbucket shipped-PHP coverage acceptance — 28 September 2026

Historical coverage checkpoint; level-8 acceptance above supersedes its
level-3 and pending-promotion statements. This checkpoint supersedes the
proposed view/index coverage increment in the
27 September blocking-analysis checkpoint below. [Bitbucket #69](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/pull/69)
landed as `80895ee9ffe0bf4e49b38939115c8946438f5a60` from reviewed head
`0b0a4cfc6f62142e0fffb4d5680c10442cd36081`. Both trees are
`230555708705a7d57aabe48b9d4d7d6794aa1977`.

| Shipped scope | Files | Direct analysis |
| --- | ---: | --- |
| `autoload.php`, plugin entrypoint | 2 | Blocking level 3 |
| `src/Bitbucket/` | 16 | Blocking level 3 via `src/` |
| `views/documentation.php` | 1 | Blocking level 3 via `views/` |
| `index.php` | 1 | Blocking level 3; inert file included |
| **Total** | **20** | **All shipped PHP directly covered** |

Directory roots include future PHP files under `src/` and `views/`. Bootstrap,
Core and WordPress symbols remain analysis context, not additional direct roots.
Tests, fixtures and the unshipped release verifier retain their separate checks.
No generated PHP copy exists in this package's release allowlist.

The implementation changes only analysis configuration and contributor/release
guidance. Level 3, locked tools, runtime PHP, dependency locks and the exact Core
beta.29 tuple recorded below are unchanged. The temporary documentation-view
return-type violation failed `check:host` during analysis before PHPUnit; the
probe was removed. Final local aggregate passed: all 20 paths clean, 196 tests /
2,159 assertions, candidate validator (1 valid / 12 invalid), PHPCS and syntax.
Exact implementation-candidate archive build/verification passed; the final
head's native runtime archive and certified installed proof also passed.

Final-head code/security reviews were clean, both earlier release-guidance
findings resolved, and all applicable checks passed. Successful post-merge runs
at `80895ee9ffe0bf4e49b38939115c8946438f5a60`:
[Quality 36357893395](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/actions/runs/36357893395),
[Certified Core installed proof 36357892887](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/actions/runs/36357892887),
and [Release Please 36357983946](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/actions/runs/36357983946).

This closes the identified shipped-path coverage gap, not the wider quality
programme. Higher analysis levels, shared-standard version adoption and
connected naming/API work remain separate decisions under #65 and the package
owners. No release publication or new certified Core composition is claimed.
Dates in this checkpoint use Europe/London; GitHub run timestamps may show
27 September UTC.

## Bitbucket blocking analysis checkpoint — 27 September 2026

Historical enforcement checkpoint; its proposed view/index increment is
superseded by the 28 September coverage acceptance above.

This package-only checkpoint supersedes Bitbucket's advisory-analysis statements
in the 23 September snapshot below. It does not requalify other repository rows.
[Bitbucket #68](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/pull/68)
was squash-merged at `5e0732e0ea386402b239d6982c753bc1f0f4b6d5` from reviewed
head `39921fa24c50d67d196bba8b12814cde4df7ca3b`; both have tree
`346724672790f3a4e8bd6acc1e35cffd4042df41`.

`composer check` remains Core-independent PHPCS plus syntax. `composer check:host`
now runs required level-3 `analyze`, unit tests, release-candidate contracts and
`check`, in that order. The separate advisory CI step was removed; analysis
failure propagates through Repository quality to terminal Quality. The focused
`composer analyze` uses the same configuration. `standards` and `standards:fix`
remain the PHPCS/PHPCBF pair. RELEASE.md and contributor/agent guidance agree.

The certified host remains Core v1.0.0-beta.29, tag target
`ffc11fc8e40618624a785b7fca5193029c6d492e`, archive source
`ff35be100a9f5c6cd77a84bcfc3734227106b0b8`, with only its locked production
dependencies installed. Set `RAN_BOOSTER_CORE_PATH` and
`RAN_BOOSTER_CORE_VENDOR_AUTOLOAD` as documented in the add-on. Runtime support
remains PHP 8.2+ / WordPress 7.0+. PHPStan 2.2.8 and WordPress extension 2.0.3
remain locked; no level, roots, baseline, dependency or runtime source changed.

### Shipped PHP coverage at the landed revision

The release allowlist selects 20 PHP files. Direct analysis is distinguished
from bootstrap/autoloader symbol availability; loading a symbol is not proof
that its implementation or an included view is directly analysed.

| Scope | Count | Disposition |
| --- | --- | --- |
| `autoload.php`, `ran-booster-bitbucket.php` | 2 | Direct blocking level 3. |
| All PHP under `src/Bitbucket/` | 16 | Direct blocking level 3 through the `src` directory root, including future PHP files there. |
| `views/documentation.php` | 1 | Shipped executable view, outside direct roots. Included by `Plugin`; inclusion alone is not direct coverage evidence. |
| `index.php` | 1 | Shipped inert “Silence is golden” file, outside direct roots. |
| Core production contracts, Composer/WordPress symbols and `tests/phpstan-bootstrap.php` | Outside shipped add-on PHP | Bootstrap/autoloader/extension context; not additional directly analysed add-on roots. |
| `scripts/verify-release.php`, tests and fixtures | Not shipped | Outside direct analysis roots; retained syntax/test/archive checks have separate purposes. |
| Generated PHP copies | 0 | No generated-copy exclusion is needed for the allowlisted PHP. |

The smallest next coverage proposal is to measure `views/` and `index.php` at
unchanged level 3 against the same certified host, then add those roots only
with clean results and a negative control proving view failures reach the host
aggregate. This is a proposal, not landed coverage. Higher levels, shared-standard
version adoption and connected API/naming work remain separate reviewed slices
coordinated through #65 and the existing package owners.

### Qualification and retained gates

Final-head code and security reviews completed clean after both Codex/Copilot
findings about stale RELEASE.md wording were fixed and resolved. Native Quality,
Repository quality, PHP 8.2/8.5, runtime archive, separate Certified Core installed
proof and GitGuardian passed. Local implementation proof recorded zero analysis
errors, 196 tests / 2,159 assertions and release-candidate validation (1 valid /
12 invalid). A temporary source return-type violation failed `check:host` before
PHPUnit; it was removed before the final clean aggregate.

Successful post-merge runs on `5e0732e0ea386402b239d6982c753bc1f0f4b6d5`:
[Quality 36355112140](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/actions/runs/36355112140),
[Certified Core installed proof 36355111457](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/actions/runs/36355111457),
and [Release Please 36355229655](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/actions/runs/36355229655).
The installed proof remains a separate workflow, not a terminal Quality dependency.
Release-candidate install readback remains conditional. No release publication,
new certified composition or programme-wide acceptance is claimed.

## Release Updater naming and exception acceptance — 27 September 2026

This checkpoint supersedes Release Updater's proposed status in the dated
26 September checkpoint below. Other repository rows remain dated evidence.
The owner-authorized implementation stack is squash-merged in dependency order.
Each dependent PR was retargeted with its complete reviewed tree unchanged,
then received fresh native CI and separately requested code/security reviews.
All actionable review threads were resolved before merging; each merge tree
matches its qualified candidate.

| PR | Reviewed final head | Squash merge | Successful post-merge runs |
| --- | --- | --- | --- |
| [#89](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/pull/89) | `f81c0f237ad529167495859c8372bd66536ba0e7` | `292021627b09389086c79cbccd0ba61967f4b305` | [CI 36327464181](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/actions/runs/36327464181); [Release Please 36327579636](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/actions/runs/36327579636) |
| [#90](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/pull/90) | `967532565ea32d1e912a7a71ca92a1852afc8235` | `afe771850a8461e5cd23b168ebddfe0053c674eb` | [CI 36327855092](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/actions/runs/36327855092); [Release Please 36327972845](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/actions/runs/36327972845) |
| [#91](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/pull/91) | `7ac5be8ab58c7476e550df6d527b33b33bbb044d` | `3d0f2942b18590c9cd5ab264a6c63d44ae9087e2` | [CI 36328265492](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/actions/runs/36328265492); [Release Please 36328383429](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/actions/runs/36328383429) |
| [#92](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/pull/92) | `a2700e62bd7090cf664a842c1094f8e77fb15efb` | `5ad94e972446f08c7408828cf7e4ac42c2eee78d` | [CI 36328610084](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/actions/runs/36328610084); [Release Please 36328744769](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/actions/runs/36328744769) |

The final main checkpoint is `5ad94e972446f08c7408828cf7e4ac42c2eee78d`.
Owned-method and variable naming now cover all 35 maintained production PHP
files and both scripts through path rules, including future files. All 36
shipped PHP files retain direct blocking level-8 analysis. Generated
ArchiveSafety retains namespace-only parity and its PHPCS exclusion;
purpose-built fixture interfaces remain exempt from mechanical naming changes.
The [acceptance record](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/blob/5ad94e972446f08c7408828cf7e4ac42c2eee78d/QUALITY_ACCEPTANCE.md)
documents the retained security/native/JSON/bootstrap/fixture exceptions and
seven declaration-local PHPStan exceptions. No broad production naming waiver,
analysis baseline or lower analysis level is introduced.

Native PHP 8.2/8.5, WordPress 6.5/7.1, MySQL CAS, Windows, JavaScript,
no-dev consumers, live Composer audit and generated/runtime-copy checks remain.
Negative controls and repeated PHPCBF stability evidence are recorded in the
implementation PRs. The final local full run was 474 tests / 24,739 assertions
with the two known portable-PHP `GLOB_BRACE` errors; it is not a green aggregate.
Native CI supplies separate successful qualification.

The coordinated lifecycle/runtime change advances the cross-copy protocol to 5;
both protocol-4/5 load orders fail closed without replacing or mutating the
established broker. Final runtime content identity is
`07696b27292b1c999714e31b06f2fd0d79d0d3e19e334eb17136c37b027c9a24`.
Package version remains `1.0.0-beta.8`. The [held release #70](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/pull/70)
requires a separate owner publication decision.

The bounded Core audit at `0c1ace618331a23e068cec6e54a896c634bc8f76` and
[Core #167 handoff](https://github.com/RocketsAreNostalgic/ran-booster/issues/167#issuecomment-5845449902)
identify the later coordinated dependency/protocol-metadata/test adoption.
No new Core host tuple is certified by this package acceptance. This checkpoint
supplies the final matrix reconciliation for [Release Updater #60](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/issues/60);
the wider #65 programme and Migrator's separate release proof remain open work.

## Release Updater residual acceptance checkpoint — 26 September 2026

Historical pre-merge checkpoint; superseded by the 27 September landed record above.
This superseded only Release Updater's older remaining-work descriptions.
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

Release Updater routing reconciled on 27 September and Bitbucket on 29 September;
other owner routing below retains its dated scope.

Bitbucket's [maintained-PHP coverage drift checkpoint](#bitbucket-maintained-php-coverage-drift-checkpoint--29-september-2026)
is the current source record: #78–#88 are merged, with blocking level-8 analysis
of all 20 shipped PHP files, naming enforcement across current and future
production paths, and a semantic scope guard in `check`. Do not restart
shared-standard adoption, the naming cohorts,
the analysis promotion, completed view/index coverage or resolved model findings
from older audit rows. Connected Core contracts and held release #75 retain
their separate owners and decisions.

[#65's residual-owner ledger](https://github.com/RocketsAreNostalgic/.github/issues/65#residual-programme-ownership-after-66-closure)
retains the previously unchecked programme responsibilities from owner-closed
#66: matrix upkeep, drift validation, contributor coordination and
reference/pilot acceptance. Upgrade/live-audit policy was delivered in #97;
closure of #66 did not complete the other consumer work. Existing repository
children keep their claims.

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
Remaining naming and exception implementation subsequently landed through
[local #89](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/pull/89)–[#92](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/pull/92).
The [27 September acceptance checkpoint](#release-updater-naming-and-exception-acceptance--27-september-2026)
records the final reviewed heads, merged-main qualification and matrix reconciliation.
[Release Updater #60](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/issues/60)
is the acceptance/closure record, not a queue to restart completed naming,
parameter, condition or exception slices. Publication and the coordinated
Core dependency/protocol-metadata/test adoption remain separate decisions.
Do not treat the historical suppression lists as current.
[Release Updater #70](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/pull/70)
merged and published as immutable v1.0.0-beta.9 at
`27889528442fc4e49ca060959218d5ec288c3055`. Core/Provider consumer
adoption remains separate. [Migrator #43](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/pull/43)
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
