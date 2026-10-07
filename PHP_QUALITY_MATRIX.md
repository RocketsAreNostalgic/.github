# PHP quality acceptance

Policy lives in [Quality Standards](QUALITY_STANDARDS.md); this page records
bounded acceptance and remaining decisions. Closed #66 is delivered evidence;
its residual commitments remain under #65 and existing repository issues.
This consolidation does not re-run consumer checks, raise levels, approve
exceptions, change dependencies or authorize releases.

<a id="current-candidate-checkpoint--7-october-2026"></a>

## Acceptance snapshot — 7 October 2026, 08:41 UTC

This fixed snapshot transcribes the responsible controllers' linked handoffs
and the [frozen PR132 evidence checkpoint](https://github.com/RocketsAreNostalgic/.github/blob/b574d2d1a64766db94a11bfc110c456be7fab99a/PHP_QUALITY_MATRIX.md#current-candidate-checkpoint--7-october-2026).
It is not new independent qualification or approval of that documentation PR.
Subsequent operations, ownership and changed qualification belong in
[coordination #65](https://github.com/RocketsAreNostalgic/.github/issues/65),
with its existing [analysis #127](https://github.com/RocketsAreNostalgic/.github/issues/127)
and [standards #128](https://github.com/RocketsAreNostalgic/.github/issues/128) workstreams;
this dated snapshot must not be read as their live state.

| Repository | Delivery state at checkpoint | Remaining acceptance | Evidence |
| --- | --- | --- | --- |
| Core | Candidate stack; not delivered to main. | Repair qualification and four exception dispositions; separate release decision. | [Candidate details](#core-candidate-qualification-and-remaining-gap) |
| Release Updater | Parent-branch integration only. | Main-target qualification and owner decision. | [Controller handoff](https://github.com/RocketsAreNostalgic/.github/issues/65#issuecomment-6034269606) |
| Branch Updater | Delivered to main; post-merge checks passed. | No residual Branch integration finding; wider acceptance remains scoped. | [Delivery evidence](https://github.com/RocketsAreNostalgic/.github/issues/65#issuecomment-6034269606) |
| Updater Support | Parent-branch integration only. | Further parent-target qualification and owner decision. | [Controller handoff](https://github.com/RocketsAreNostalgic/.github/issues/65#issuecomment-6034269606) |
| GitHub Provider | Delivered to main; post-merge checks passed. | Release decision and immutable Core adoption. | [Delivered-source evidence](#delivered-lane-b-source) |
| Bitbucket | Delivered to main; certified beta31 installed proof passed. | Release decision and separate future-host certification. | [Delivered-source evidence](#delivered-lane-b-source) |
| Migrator | Delivered to main; exact release candidate qualified. | Owner installed/manual acceptance and release decision. | [Delivered-source and candidate evidence](#delivered-lane-b-source) |
| Admin Shell | Main-target candidate; unmerged. | Exact cumulative review and native qualification. | [Frozen candidate evidence](https://github.com/RocketsAreNostalgic/.github/blob/b574d2d1a64766db94a11bfc110c456be7fab99a/PHP_QUALITY_MATRIX.md#current-candidate-checkpoint--7-october-2026) |
| Shared coding standards | Main-target candidate; unmerged. | Cumulative qualification; exact Starter/Core proof before release. | [Frozen candidate evidence](https://github.com/RocketsAreNostalgic/.github/blob/b574d2d1a64766db94a11bfc110c456be7fab99a/PHP_QUALITY_MATRIX.md#current-candidate-checkpoint--7-october-2026) |

The linked records retain PR chains, maintained-PHP populations, analysis levels,
exact revisions and run results. Coverage describes the stated revision only;
PHPCS/WPCS have no PHPStan level system, and analysis coverage is distinct from
style acceptance. Qualified candidate trees, default-branch delivery, publication
and consumer adoption are separate claims. No blanket exception acceptance follows.

Branch delivery bound main `9ab9be281a2fa3dabb072d7a80505a54ef9eb366` to tree
`88ec71f18622d437caf32087a248f5448ac23c01`; [CI37594935138](https://github.com/RocketsAreNostalgic/ran-wp-branch-updater/actions/runs/37594935138)
passed all four required jobs. The standalone profile was retained; no package
publication or consumer update followed from that development-quality stack.
The [Lane A parent-fold record](https://github.com/RocketsAreNostalgic/.github/issues/65#issuecomment-6033842955)
and [Core refresh](https://github.com/RocketsAreNostalgic/.github/issues/65#issuecomment-6033828160)
supply the preceding bounded evidence. The [6 October ledger](https://github.com/RocketsAreNostalgic/.github/issues/65#issuecomment-6027025243)
retains original pairs where findings or integration changed the candidate.

Admin #25/shared #15 are cumulative candidates. Their earlier green #24/#14
runs did not establish protection against effective PHPStan `ignoreErrors`;
the frozen checkpoint records the locked-checker guard repairs. Cumulative
review/native qualification was pending at the cutoff. Neither was delivered or published;
shared release still requires exact-candidate Starter/Core proof.

### Delivered Lane B source

| Delivered PR | Main revision | Verified tree | Post-merge evidence |
| --- | --- | --- | --- |
| [Provider #65](https://github.com/RocketsAreNostalgic/ran-booster-github-provider/pull/65) | `db90f3c470bd4149b5931b119aa62e43c7ff59ec` | `d24aa21555d098f80503c5aa158cd0bde760ec4d` | [CI 37583233815](https://github.com/RocketsAreNostalgic/ran-booster-github-provider/actions/runs/37583233815) success |
| [Bitbucket #102](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/pull/102) | `0e1e44b0ccd0fd4ce5d846d947b79a2ce5120e87` | `1699dda0a495653c4cd5f205daabd7dd39b552ea` | [Quality 37583248694](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/actions/runs/37583248694) success; certified beta31 installed proof 37583528602 success |
| [Migrator #65](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/pull/65) | `486d7aba3dce88ae4c7c8cf23f20d143e878d902` | `13e338dccefa998c5b89216ac10d575074b54f53` | [Quality 37584807685](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/actions/runs/37584807685) success |

These are owner-authorized source squashes with independently matched trees and
reviewed sole parents. All twelve original Lane B proposals are closed as
superseded, not falsely marked merged; their branches and reviews are preserved.
Migrator's main runtime archive, certified provenance and repository Quality
passed; intentionally skipped baseline/terminal wrappers are not executed checks.
No release was merged or published by Lane B. Provider #59, Bitbucket #95 and
Migrator #43 are regenerated release proposals, distinct from source delivery.
Provider #59 and Bitbucket #95 received clear independent release-pair reviews
5439496402/5439499218; Ben's publication decision remains separate. Migrator #43's [recorded qualification](https://github.com/RocketsAreNostalgic/.github/issues/65#issuecomment-6033971914)
records clear review 5439537219 and five passing canonical jobs at exact head
`e3d2052b846fd749f48a0e17b94f55ff262f7686`; two clean builds reproduced native ZIP
SHA-256 `432b54648628fdaacc29a39fde4e1d91f4abc698f13f319cf3e00eb09308196c`.
Owner installed/manual acceptance remains uncleared. Release Please merges use
regular merge commits. Migrator's manual acceptance must bind its exact candidate,
ZIP digest and released host; green automation cannot clear that hold.

### Core candidate qualification and remaining gap

The [frozen candidate record](https://github.com/RocketsAreNostalgic/.github/blob/b574d2d1a64766db94a11bfc110c456be7fab99a/PHP_QUALITY_MATRIX.md#core-candidate-qualification-and-remaining-gap)
retains #258/#259 exact pairs, independent reviews, native results and the
limited two-lane named-Theme proof. #260/#261's earlier green candidate still
allowed a future extensionless entrypoint under a new root to escape both
inventories; no omission from the recorded 710-file population was found. Two exact immutable
historical rejection fixtures remained reviewed exemptions. The published repair at
`fda3d4ac7fd489fd1dc29915772c2d950a9e9dca` has focused evidence, with renewed
independent/native qualification pending at this checkpoint. Green predecessor
runs do not qualify that changed head or establish its future-file guarantee.

The four #259 occurrences remain **pending owner disposition**: captured renderer
fragments in `RepositoryDetailRenderer.php` and passive request selection in
`DeploymentAdminPresenter.php`. Behavioral/negative controls and reasons are
evidence, not acceptance. Other CLI, native-I/O, security and SQL allowances
retain their existing recorded disposition; these changes do not reaccept them.
Core's separate #249 regression/supersession disposition remains explicit.

## Outstanding acceptance and holds

- The four Core #259 occurrences above require owner disposition; source and
  negative-test evidence does not accept them. Core #249's separate regression
  and supersession disposition remains explicit in the linked coordinator record.
- At the cutoff, extensionless-entrypoint repair qualification, Lane A cumulative
  integration and shared/Admin candidates remained with their assigned issue owners.
  Earlier green runs do not qualify changed heads or close future-file gaps.
- Core258's consumer audit found no necessary Lane B source migration. Earlier
  source composition remains bound to Core `654fca22`; beta31 certification is
  unchanged. Future-host claims require an actually published host and fresh
  archive/runtime proof. An API-shape check alone does not establish checkout identity.
- Core beta.32, Provider beta.14, Bitbucket beta.16 and Migrator beta.10 release
  decisions are separate from source delivery. Migrator manual acceptance binds
  the exact candidate, ZIP digest and released host: supported/unsupported provider
  cases, stale/conflicting rows, partial exact cleanup/recovery, disabled adopted
  target and both load orders. Historical beta7 regression is not that acceptance.
  Preserve UI/installed journeys
  deferred under #81/#85 and operational criteria under #57; green automation
  does not clear them. Ben retains specific merge/publication decisions.
- Plugin Library stays deferred. Workbench and purpose-built fixtures retain
  their recorded exemptions; the historical updater dummy is not silently
  upgraded to a current runtime. Private scripts, dynamic strings, downstream
  forks and installed consumers require the relevant cohort-specific checks.
- Shared-package qualification and individual repository guards do not establish
  organisation-wide acceptance or close #65. A stronger local gate remains required.

The [5 October occurrence review](quality-evidence/retained-exceptions-20261005.md)
retains exact revisions, native-operation invariants and diagnostic exposure.
Its implementation notes are dated candidate evidence, not universal exception
acceptance or a fresh instruction to repeat completed work.

## Earlier accepted slices

These compact rows preserve dated evidence without presenting old revisions as
current main. The linked full records retain source/tool identities, exact PR
heads, merge trees, run results and disclosed limitations. Nothing here freshly
requalifies an unchanged row.

| Surface | Recorded disposition | Evidence |
| --- | --- | --- |
| Core level 5, 5 October | #248 landed at `48e86ebd5d6ca153311f60bc385173349ed81e30`; required level 5, zero findings. Levels 6–8 remain separately scoped. | [Post-merge Quality 37249520706](https://github.com/RocketsAreNostalgic/ran-booster/actions/runs/37249520706); [dated PR132 record](https://github.com/RocketsAreNostalgic/.github/blob/b574d2d1a64766db94a11bfc110c456be7fab99a/PHP_QUALITY_MATRIX.md#historical-delivery-and-exception-checkpoint--5-october-2026). |
| Starter formatter and reference | #25 removed PHP-CS-Fixer while retaining blocking alignment, negative/fix/repeatability controls and stronger local documentation checks; #27 adopted released standards. Original PHP 8.5 and reference limitations are not erased by consolidation. | [Starter formatter investigation](https://github.com/RocketsAreNostalgic/.github/blob/4e5982757f42fdc640757f4caedc0be03b2da182/STARTER_PHP_FORMATTER_AUDIT.md) |
| Canonical commands and Provider host | Support/Branch/Provider command migrations delivered. Independent `check` and required exact-certified `check:host` remain distinct; focused checks still feed terminal quality. Provider's package-specific title rule checks release significance, not lifecycle or publication authority. | [Command-adoption evidence](https://github.com/RocketsAreNostalgic/.github/blob/4e5982757f42fdc640757f4caedc0be03b2da182/PHP_QUALITY_ADOPTION.md) |
| Release Updater | #60 implementation, 36 shipped files at level 8, naming/exception reconciliation and protocol 5 work delivered; #70 published beta.9 at `27889528442fc4e49ca060959218d5ec288c3055`. Later quality work does not redo it; Core adoption remains a separate composition decision. | [Command-adoption evidence](https://github.com/RocketsAreNostalgic/.github/blob/4e5982757f42fdc640757f4caedc0be03b2da182/PHP_QUALITY_ADOPTION.md) |
| Admin Shell, 29 September | #19 delivered seven maintained production/tool/CLI paths at level 5 and semantic discovery protection; PR-only CI supplied tree-matched qualification, not an invented post-merge run. Later #128 common-convention/preview work is distinct. | [Satellite evidence](https://github.com/RocketsAreNostalgic/.github/blob/4e5982757f42fdc640757f4caedc0be03b2da182/SATELLITE_QUALITY_MATRIX.md) |
| TnySignature, 29 September | #9 delivered discovery of first-party PHP and direct level 5 selection protection at `d438225c4ec5513a57e464b41e5f203a5498a65a`. | [Satellite evidence](https://github.com/RocketsAreNostalgic/.github/blob/4e5982757f42fdc640757f4caedc0be03b2da182/SATELLITE_QUALITY_MATRIX.md) |
| Turnstile, 29 September | #38 protected seven shipped PHP paths/direct level 5 selection at `33c7e2fa91c8a99c96dcd3606e19daef8705810c`. | [Satellite evidence](https://github.com/RocketsAreNostalgic/.github/blob/4e5982757f42fdc640757f4caedc0be03b2da182/SATELLITE_QUALITY_MATRIX.md) |
| Ecwid, 29 September | #39 protected all ten PHP entries in the finished ZIP/direct level 5 selection at `6a3a94c69292f928e3eb9b805f63c7596ceecc4e`. | [Satellite evidence](https://github.com/RocketsAreNostalgic/.github/blob/4e5982757f42fdc640757f4caedc0be03b2da182/SATELLITE_QUALITY_MATRIX.md) |
| EmailOctopus, 29 September | #41 protected 15 finished-ZIP PHP paths/direct level 3 selection at `41fb873983a344eeef1d3179b1516153dd7d8ee0`. | [Satellite evidence](https://github.com/RocketsAreNostalgic/.github/blob/4e5982757f42fdc640757f4caedc0be03b2da182/SATELLITE_QUALITY_MATRIX.md) |
| Enhanced Cover, 29 September | #33 protected eight finished-ZIP paths/direct level 4 selection at `08125cfd641f31c39a9b3f8f3abc97b6616a08b3`; eleven production paths is the earlier, different source population. | [Satellite evidence](https://github.com/RocketsAreNostalgic/.github/blob/4e5982757f42fdc640757f4caedc0be03b2da182/SATELLITE_QUALITY_MATRIX.md) |
| Duplicate Detector, 29 September | #28 protected eleven finished-ZIP paths/direct level 5 selection at `6e88335c1b6fd77e24a7819525e4ae8806252a3f`; two tools separately remain level 3. UI#15/settings#16 holds are separate. | [Satellite evidence](https://github.com/RocketsAreNostalgic/.github/blob/4e5982757f42fdc640757f4caedc0be03b2da182/SATELLITE_QUALITY_MATRIX.md) |

The satellite guards included uncovered-file negative controls. Their rows do
not close estate-wide drift work, create plugin releases or infer unavailable
security-review results. Check the linked source for each actual CI topology;
PR-only qualification and skipped jobs are not post-merge passing checks.

## Retained tooling and audit decisions

The [upgrade policy](QUALITY_STANDARDS.md#shared-package-versions-consumer-upgrades-and-live-advisories)
is authoritative. The following are bounded consumer decisions, not uniform
version requirements or standing instructions to upgrade other owners' locks.

- The 3 October #122 decision retained Core Admin Shell pin
  `7fee7a1cebb24c8dcbf1bfd1c9b9c9455fa73efb`: resource/sync bytes matched package
  main. Later adoption must regenerate real provenance and qualify Core;
  byte identity does not mean the latest build tooling was adopted. Admin #20's
  stat-cache repair was package-local; it did not update Core's pin.
- Core's frontend quality-config pin `751edd097e3902efb93992bf47401a1a4f4b1fa8`
  remains an accepted immutable Git distribution. The compared newer change
  affected only package-local development locks, not exported configuration;
  registry publication remains optional [package #5](https://github.com/RocketsAreNostalgic/ran-quality-config/issues/5).
- Migrator #55's released-standards adoption and test/helper naming landed;
  do not restart that migration. Its qualification did not raise the analysis
  floor or certify a new host. Core #230's development-tool update also landed;
  the prior #124 capture hold in the original #122 report is historical.
- The 29 September audit-placement inventory found an explicit blocking locked
  Composer audit in Release Updater; it found none in the other inspected
  manifests/workflows. That bounded finding does not exclude other security
  scans or claim present-day placement. Preserve adopted audit behavior;
  lookup failure is unavailable evidence, never a clean result.

[Tooling decision evidence](https://github.com/RocketsAreNostalgic/.github/blob/4e5982757f42fdc640757f4caedc0be03b2da182/quality-evidence/tooling-decisions-20261003.md) retains before/after refs, hashes, advisory scope and
qualification. [Upgrade/audit inventory](https://github.com/RocketsAreNostalgic/.github/blob/4e5982757f42fdc640757f4caedc0be03b2da182/QUALITY_UPGRADES_AND_AUDIT.md) retains the inspected script/workflow revisions.
Neither an empty advisory snapshot nor package CI establishes general security,
consumer acceptance or new release compatibility.

## Historical evidence and completed investigations

Substantive policy has one home in Quality Standards. These immutable links
preserve prior documents, including their original anchors, without leaving old
agent claims and implementation instructions in the ordinary reading path.

| Historical record | Surviving decision / use |
| --- | --- |
| [Historical acceptance matrix](https://github.com/RocketsAreNostalgic/.github/blob/4e5982757f42fdc640757f4caedc0be03b2da182/PHP_QUALITY_MATRIX.md) | Full 23 September source/tool/coverage audit and dated 24 September–4 October acceptance, original candidate/main distinctions, evidence and limitations. |
| [Command-adoption evidence](https://github.com/RocketsAreNostalgic/.github/blob/4e5982757f42fdc640757f4caedc0be03b2da182/PHP_QUALITY_ADOPTION.md) | Old→canonical command mapping, certified-host setup/identity and narrow Provider title-classification boundary. |
| [Satellite evidence](https://github.com/RocketsAreNostalgic/.github/blob/4e5982757f42fdc640757f4caedc0be03b2da182/SATELLITE_QUALITY_MATRIX.md) | Per-repository tests, scope populations, exact trees/runs and explicit unavailable-review disclosures. |
| [Naming investigation](https://github.com/RocketsAreNostalgic/.github/blob/4e5982757f42fdc640757f4caedc0be03b2da182/BOOSTER_NAMING_MIGRATION.md) | Snake-case decision and coordinated API/named-argument/callback/generated-copy safeguards now in policy; declarations/caller inventory remains evidence, not an outstanding count or complete call graph. |
| [Shared-rule investigation](https://github.com/RocketsAreNostalgic/.github/blob/4e5982757f42fdc640757f4caedc0be03b2da182/BOOSTER_SHARED_RULES_AUDIT.md) | Historical PHPCS diagnostic exposure, hidden inheritance-check gap and suppressed-rule probes; diagnostic occurrences are not unique symbols or proven defects. |
| [Starter formatter investigation](https://github.com/RocketsAreNostalgic/.github/blob/4e5982757f42fdc640757f4caedc0be03b2da182/STARTER_PHP_FORMATTER_AUDIT.md) | Completed single-formatter investigation; finite PHP 8.4 examples do not prove universal equivalence or PHP 8.5 execution. |
| [Retired recipe disposition](https://github.com/RocketsAreNostalgic/.github/blob/4e5982757f42fdc640757f4caedc0be03b2da182/BOOSTER_LIBRARY_QUALITY.md) | Shared recipe retired under #111; Provider owns provisioning locally. Original action removal depended on Provider reintegration landing and main no longer referencing it; this consolidation does not authorize removing executable code. Require a demonstrated second matching contract before another extraction; wider research remains separate. Historical action commit `6e81370238e33c5b77641355a772557912f7fee7` preserves rollback provenance. |
| [Tooling decision evidence](https://github.com/RocketsAreNostalgic/.github/blob/4e5982757f42fdc640757f4caedc0be03b2da182/quality-evidence/tooling-decisions-20261003.md) | Exact #122 comparison and scoped advisory evidence; later landing disposition is summarized above. |

Machine-readable [rule results](quality-evidence/booster-rule-results.json),
[naming inventory](quality-evidence/booster-naming-inventory.json) and
[Starter formatter results](quality-evidence/starter-formatter-results.json)
remain unchanged with their adjacent audit scripts and path/sniff lists.
Those scripts are investigation aids, not canonical provenance or reproducible
build systems. Any rerun is a new measurement with separately recorded inputs;
old snapshots do not certify moving branches, all-estate CI or future edits.
