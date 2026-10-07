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

- At the snapshot cutoff, [Core candidate details](#core-candidate-qualification-and-remaining-gap)
  recorded four pending #259 owner dispositions, repair qualification and the
  separate #249 regression/supersession disposition.
- [The snapshot](#acceptance-snapshot--7-october-2026-0841-utc) records pending
  Lane A cumulative integration and shared/Admin qualification at the cutoff;
  follow the linked issue owners for subsequent work.
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

The [5 October occurrence review](https://github.com/RocketsAreNostalgic/.github/blob/70e1321efc0b7cce7d6330b58cc0dd5a60e5ae66/quality-evidence/retained-exceptions-20261005.md)
retains exact revisions, diagnostic exposure and detailed native-operation
invariants as optional evidence. Later implementations do not constitute
blanket exception acceptance or instructions to repeat completed migrations.
Disposition of this historical commitment was not established by this bounded
review; resolve through #65 before repeating work: at Core
`48e86ebd5d6ca153311f60bc385173349ed81e30`, `RAN/Storage/Database.php:189/194`
observes the expected version before `get_option` can invoke a mutating filter.
Preserve that evaluation order and add focused behavioral proof when the group
is taken up; the recorded version tests did not inject that mutation.

Retained exception work must preserve private-file/device/inode custody,
identity-checked deletion, descriptor locking, atomic replacement/readback,
bounded archive reads and stream closure; throwing/byte-stable JSON; prepared
SQL/CAS and validated identifiers; opaque-token boundaries; real reflection and
native seams; and namespace-only ArchiveSafety generation parity. Do not hand
edit generated copies. Existing installed Plugin Check and no-dev provenance
remain distinct from development-checker silence. Apply the current
[exception policy](QUALITY_STANDARDS.md#exceptions-and-native-operations) and
record actual disposition in existing issues; the historical exposure counts
are neither proof of defects nor accepted exemptions.

## Earlier accepted slices

Completed delivery evidence is optional history in the
[pre-move accepted-slices record](https://github.com/RocketsAreNostalgic/.github/blob/70e1321efc0b7cce7d6330b58cc0dd5a60e5ae66/PHP_QUALITY_MATRIX.md#earlier-accepted-slices):
exact source/tool identities, PR heads, merge trees, runs and limitations. It
covers Core's level-5 delivery, command/formatter migrations and satellite
coverage. It does not requalify current main; later work must preserve stronger
local gates and distinguish PR-only or skipped checks from post-merge passes.

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
- Starter retains its blocking alignment, negative/fix/repeatability controls
  and stronger local documentation checks. Historical PHP 8.4 examples do not
  establish universal formatter equivalence or PHP 8.5 execution.
- Provider's independent `check` and required exact-certified `check:host`
  remain distinct, with focused checks feeding terminal quality. Its narrow
  title rule checks release significance, not lifecycle or publication authority.
- Duplicate Detector's UI #15/settings #16 holds remain separate from delivered
  quality work. Completed Release Updater protocol-5 work does not itself
  establish Core composition; consumer adoption remains a separate decision.
- The shared recipe remains retired under #111; Provider owns provisioning
  locally. Original action removal required Provider reintegration on main and
  no remaining main reference. Require a demonstrated second matching contract
  before another extraction; wider research is separate. This consolidation
  authorizes no executable removal.

Completed Migrator #55/Core #230 changes and the old #124 capture hold are
[historical tooling context](https://github.com/RocketsAreNostalgic/.github/blob/70e1321efc0b7cce7d6330b58cc0dd5a60e5ae66/PHP_QUALITY_MATRIX.md#retained-tooling-and-audit-decisions),
not instructions to restart their work. Preserve adopted audit behavior under
the upgrade policy; lookup failure is unavailable evidence, not a clean result.

## Historical evidence and completed investigations

For provenance only, the [pre-move evidence index](https://github.com/RocketsAreNostalgic/.github/blob/70e1321efc0b7cce7d6330b58cc0dd5a60e5ae66/PHP_QUALITY_MATRIX.md#historical-evidence-and-completed-investigations)
links the original acceptance, adoption, satellite, naming, shared-rule,
formatter, recipe and tooling investigations, including original anchors and
rollback identities. Historical diagnostics are measurements, not approved
exceptions or proven defects. Today's requirements live in
[Quality Standards](QUALITY_STANDARDS.md); unresolved decisions remain above.

Machine-readable [rule results](../../quality-evidence/booster-rule-results.json),
[naming inventory](../../quality-evidence/booster-naming-inventory.json) and
[Starter formatter results](../../quality-evidence/starter-formatter-results.json)
remain unchanged with their adjacent audit scripts and path/sniff lists.
Those scripts are investigation aids, not canonical provenance or reproducible
build systems. Any rerun is a new measurement with separately recorded inputs;
old snapshots do not certify moving branches, all-estate CI or future edits.
