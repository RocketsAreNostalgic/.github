# Initial release starter: G0 contract proposal

**Status: PROPOSED, not implemented or accepted.** This document and
[the generated examples](BOOTSTRAP_STARTER_EXAMPLES.md) are the documentation-only
G0 deliverable for [#81](https://github.com/RocketsAreNostalgic/.github/issues/81),
within #47/#44. The coordinator records the reviewed contract revision and G0
acceptance in #81 before releasing implementation agents. Opening or merging a
documentation PR alone does not qualify product code, a release or a deployment.

## 1. Product decision

Deliver one small, production-ready **initial setup** assistant for a source-ready
WordPress plugin or theme. It proposes a release recipe in a draft PR; the target
maintainer owns the files afterwards. Release Please's normal version/release PRs
continue; later template-update PRs, regeneration and managed-template repair do
not. The current absence of deployed feature state permits a clean format cut,
not reduced production security, reliability or testing.

The consumer is PHP in Booster's bundled GitHub provider, not the shared Actions
publisher. A template ZIP is input to that reader. It is never executed on
WordPress. The generated files become repository code with the same review and
maintenance responsibilities as deliberately copied starter code.

### Supported first recipe

- GitHub.com repository with default branch `main`, one plugin or theme at the
  repository root, and an unambiguous WordPress header and package identity.
- Installable payload is already committed. No dependency installation, asset
  compilation, monorepo discovery, submodule resolution or Git LFS hydration.
- Stable SemVer releases (`X.Y.Z`), a reviewed runtime allowlist, one installable
  `<slug>-<version>.zip` asset. No release-channel configurator in the starter.
- Read-only Quality builds/verifies the exact source; existing shared Profile B
  owns Release Please and exact tested-asset publication.
- No existing release automation or generated-path collisions. An existing
  Quality workflow is a manual-integration case, not permission to replace it.
  The initial recipe does not automatically compose an arbitrary existing CI DAG.
- Straightforward header and optional `readme.txt` version maintenance only.
  Additional version authorities that cannot be kept coherent by that fixed
  recipe require manual setup; do not infer arbitrary package/build conventions.

The examples use PHP 8.2 for syntax checks and Node 24.11.0 for the existing
packaging/verifier adapter family, on GitHub-hosted `ubuntu-24.04`. These are
explicit tooling choices, not a claim to certify every PHP/WordPress version a
target declares. Product-specific tests and additional compatibility requirements
remain target-maintainer work. No artificial Composer project is generated.

Unsupported does not mean insecure or unmanageable by Booster. Explain the exact
limitation and offer manual customization guidance without speculative writes.
Other Booster installation, branch and release-management features keep their
existing eligibility and behavior.

## 2. Recipe before format

The existing pack's generated release workflow contains local two-event
orchestration, merge-parent/PR reconstruction, draft discovery, privileged ZIP
building, upload/publication and Release Please label reconciliation. Merely
changing the manifest would preserve the wrong recipe.

| Existing or proposed responsibility | Disposition and concrete reason |
| --- | --- |
| Local generic draft/tag/label/merged-PR/retry publisher | Delete; the existing shared Profile B workflow owns it. |
| `scripts/upload-release-assets.sh` | Delete from the pack and consumer map; no target-local publisher. |
| Read-only Quality workflow | Supply the small exact-source build/verification job in the examples; no release-candidate shortcut lane. |
| Build and independent archive verification adapters | Keep the concrete source projection, layout, bounds and identity checks; remove publication/credential/state responsibilities. Do not invent an adapter framework. |
| Release Please configuration and manifest | Keep; RP remains the sole version/lifecycle engine. |
| `version.txt` | Keep as the simple strategy's version source; require equality with manifest and WordPress header. This is not a second version calculator. |
| `release-contents.txt` | Keep as explicit maintainer-reviewable payload authority. The exact committed allowlist, not dirty checkout contents, decides the ZIP. |
| Generated ownership/managed-update receipt | Remove. Keep only the local state needed to complete/read back the initial operation. |
| Origin and maintenance information | Keep human-readable support instructions in `RELEASE-STARTER.md` and one small passive `.ran-booster-release-starter.json` origin record for the bounded read-only adoption security check in section 7. Neither grants write authority or managed-template ownership. |
| Initial preview, authorization, identity, conflicts and truthful outcome | Keep; the feature creates remote repository changes. |
| Template-update methods/controls/engine | Remove behavior and UI; the current mandatory host-interface slots need the specific disposition in section 6. |
| Booster host certification, database matrix, updater graph | Not generated. Retain those where needed to qualify Booster itself. |
| Arbitrary build hooks, ecosystem detection and deployment destinations | Outside this starter. |
| Background advisory scanner, cached dashboard/status, notification scheduler or automatic repair | Not part of this delivery. Section 7 retains only the owner-requested on-demand read-only adoption checkpoint plus normal disclosure/subscription guidance. |

### Execution boundaries

```text
Initial operation:
verified pack -> preview of bounded files -> explicit confirmation
-> exact-target recheck -> draft setup PR -> readback -> maintainer ownership

Generated target:
PR / input-free manual dispatch / main push
-> read-only exact-source Quality -> tested ZIP + promotion manifest

Only successful canonical main-push Quality
-> shared Profile B -> Release Please
-> exact candidate Quality when required
-> after approved release-PR merge: fresh main Quality
-> exact tested ZIP promotion -> immutable release/readback
```

A draft PR is not a sandbox. Its Quality job may execute before merge; all such
execution has read-only repository permission, no supplied secrets or persistent
checkout credentials, and no publisher. There is no `pull_request_target` lane.
Main-push publication goes through the existing authenticated shared boundary,
not a new local approximation. Pin every external Action/reusable workflow to a
reviewed full commit SHA. Do not use `secrets: inherit`.

Quality executes the same applicable source/archive checks on ordinary PRs,
Release Please PRs and input-free dispatch. No bot-only skip catalogue, prior-PR
artifact reuse or separate installed-candidate state machine is generated.

## 3. Effective prerequisites, not invented capabilities

The audited shared workflow has **no configurable default-branch input**: its
admission, ref checks and RP target all require `main`. The starter must refuse
another default branch; do not rename it or silently add a shared-workflow feature.

Before the setup PR is represented as ready for use, disclose and verify the
applicable prerequisites: Actions enabled; access to the public pinned reusable
workflow and its pinned Actions; permission to create Release Please PRs; the
caller's required `contents`, `issues`, `pull-requests` and `actions` token scopes;
GitHub-hosted runner/tool availability; and owner-enabled immutable releases.
The target owner must keep merge protections and meaningful existing checks.
A generated workflow cannot silently enable settings or grant itself authority.

Prefer authorized readback where available. The normal setup/Actions token may
not have Administration-read for immutable-release settings; do not add a
standing admin credential just to probe it. In that case list the setting as
**owner verification required**, not verified or automatically configured. This
is an explicit pre-merge operator checklist; immutable publication/readback is
also mandatory during the integration proof. Test at least one target outside
assumptions of RAN organization defaults before advertising general GitHub.com
eligibility. No Blacksmith subscription or AI feature is required by generated
output.

The setup token stays site-controlled and confined to the GitHub client. It needs
only the capabilities actually used for reading and creating the bounded branch,
commit and PR, including GitHub's applicable workflow-file permission. No token is
embedded in templates, generated files, comments, build evidence or logs. Missing
permission is a clear refusal, not a reason to request administration access.

## 4. Single supported pack contract

`consumer_api: 3` identifies the manifest/profile/logical-entry/placeholder
contract. It is not a PHP namespace or general Provider API version. Ordinary
reviewed fixes within this capability set use ordinary pack releases. A changed
capability requires a new reviewed contract, not hidden permission expansion.

### Envelope

`template-pack.json` has exactly these fields. No additional properties at any
object level. Producer emits deterministic UTF-8 JSON with LF; reader/verifier
must reject ambiguous duplicate keys and invalid types consistently.

| Field | Required type/value |
| --- | --- |
| `schema_version` | Integer `1`. |
| `consumer_api` | Integer `3`; no old-format adapter. |
| `pack_version` | String, stable canonical `X.Y.Z`, no leading-zero numeric components. |
| `repository` | Object exactly `{name, id}`: name is `RocketsAreNostalgic/ran-booster-release-bootstrap-templates`; ID is a canonical positive decimal string matching independently fetched repository identity. |
| `release` | Object exactly `{tag, commit}`: tag equals `v` plus `pack_version`; commit is 40 lowercase hex and equals the resolved source/tag/transport target. **No embedded release ID, optional ID or dummy ID.** |
| `profiles` | Object with exactly `source-ready-wordpress-plugin/3` and `source-ready-wordpress-theme/3`. |

Each profile is exactly `{profile_version, entries}`, with integer
`profile_version: 1`. Both profiles contain exactly the five logical entries in
the following table. An entry is exactly `{path, size, sha256, placeholders}`:
`path` is the listed relative pack member, `size` is its positive integer UTF-8
byte length up to 262144, `sha256` is the 64-lowercase-hex digest of those exact
bytes, and `placeholders` is the exact name/type object below (not supplied
replacement values). Shared entries may refer to the same physical member.

| Logical ID | Pack member -> consumer-owned destination | Exact placeholders |
| --- | --- | --- |
| `quality-workflow` | `templates/shared/quality.yml.tmpl` -> `.github/workflows/quality.yml` | `PACKAGE_SLUG: slug` |
| `release-workflow` | `templates/shared/release-please.yml.tmpl` -> `.github/workflows/release-please.yml` | `PACKAGE_SLUG: slug` |
| `release-please-config` | `templates/shared/release-please-config.json.tmpl` -> `release-please-config.json` | `BASE_SHA: sha`, `EXTRA_FILES_JSON: json_fragment`, `PACKAGE_SLUG: slug` |
| `build-release-script` | `templates/shared/build-release.sh.tmpl` -> `scripts/build-release.sh` | `HEADER_PATH: path`, `PACKAGE_SLUG: slug`, `PACKAGE_TYPE: package_type` |
| `verify-release-script` | `templates/shared/verify-release.sh.tmpl` -> `scripts/verify-release.sh` | `HEADER_PATH: path`, `PACKAGE_SLUG: slug`, `PACKAGE_TYPE: package_type`, `UPDATE_URI: github_uri` |

There are six physical files: the manifest and five templates. Do not include
source schemas, tooling, executable dependencies or an undeclared member in the
public ZIP. Deduplicate the currently identical plugin/theme RP config template.
All pack members are inert regular files, not executable members or symlinks.

Tokens are literal `{{RAN_NAME}}`. Values are derived by the consumer from the
verified target, never interpreted as expressions. Slugs match
`[a-z0-9]+(-[a-z0-9]+)*`, bounded to 200 bytes; SHA is 40 lowercase hex; package
type is `plugin` or `theme`; header is one root filename using ASCII letters,
digits, dot, underscore or hyphen (neither dot nor dot-dot). URI is the exact
canonical `https://github.com/<owner>/<repository>` already bound to the target.
Reject control characters, quoting/injection tokens and unresolved/unknown
placeholders. The JSON fragment is serialized by the consumer from its fixed
header/optional readme extra-file map, not accepted as arbitrary JSON text.
Actions expressions such as `${{ github.sha }}` remain literal template content.

The consumer additionally creates `.release-please-manifest.json`, `version.txt`,
`release-contents.txt`, `.ran-booster-release-starter.json` and `RELEASE-STARTER.md`
from its verified inputs. All output
files use Git mode `100644`; scripts are invoked through Bash. It may perform
only the previewed bounded version-annotation edit to the identified header and
optional `readme.txt`, and safely append `/CHANGELOG.md` to the normal
`.prettierignore` when needed. Contradictory/custom version or ignore rules are a
manual case. No target path, mode, operation, permission or trigger can be added
by downloaded metadata. A new output path requires a reviewed consumer change.

### Archive and transport

Preserve the existing pack envelope: at most 2 MiB compressed, 32 members, 64 KiB
manifest, 256 KiB per member, 1 MiB expanded and 200:1 ratio; reject unsafe or
ambiguous paths, duplicate/unlisted members, wrong types, CRC/length/digest
mismatch, NUL/invalid UTF-8 and unsafe substitutions before rendering. Both native
ZIP consumer tests and producer verification must exercise these controls. Their
purpose is bounded handling of remote input, not support for more formats.

Production discovery reads only the canonical repository's published stable
immutable releases. Select the newest eligible stable release under the existing
bounded client request limits and validate it fully; do not walk historical packs
to find an old supported renderer. No eligible release is unavailable; a different
API is unsupported; malformed identity/archive is invalid. None returns a usable
pack or write authority. A failed/unsupported latest stable pack does not silently
fall back. Drafts/prereleases never become production pack input.

Transport must bind actual repository ID, release ID, asset ID, exact tag/source,
non-draft immutable state, one canonical asset, size, GitHub-reported digest and
locally computed SHA-256. Accept `application/zip` or `application/octet-stream`
only, with actual ZIP validation; no second public checksum asset. Re-fetch the
same numeric release/asset identity before confirmation, and invalidate a preview
if discovery or target identity has changed. HTTPS and digest checks do not make
arbitrary workflow content safe; source review remains required.

## 5. Packaging interfaces and producer exchange

Target adapters keep the concrete interface:

```text
bash scripts/build-release.sh <exact-commit> <version> <empty-output-directory>
bash scripts/verify-release.sh <archive-path> <version> <exact-commit>
```

Only exact committed ordinary blobs selected by committed `release-contents.txt`
are payload authority. For this new recipe the allowlist is sorted explicit file
paths, one per line, with no globs, directory expansion or overlap. The consumer
proposes it from its narrow recognized source-ready layout and shows it for
review; unknown payload paths require manual setup. Preserve licenses and required
plugin/theme payload. Reject symlinks, submodules and unresolved LFS pointers.

Require version/header/manifest equality, expected single slug root, exact member
set and bytes, expected Update URI and valid declared compatibility metadata.
Normalize order, permissions, timestamps and locale/timezone; repeated builds
from the same declared tools/source/inputs must be byte-identical. Independent
verification must compare with the committed projection and enforce the existing
WordPress archive bounds (50 MiB compressed, 10000 members, 127826407 expanded
bytes, 200:1 ratio) before unsafe extraction. Product-specific build commands,
network credentials and release mutations have no place in these adapters.
Retain useful existing validator code; do not rewrite a generic archive library
for this migration. A bounded payload PHP syntax check fails on any parse error.

For the pack's **own** build, the new interface is:

```text
pnpm run build -- <output-directory> <repository-id> <tag> <exact-source-commit>
bash scripts/verify-pack.sh <zip-path> <repository-id> <tag> <exact-source-commit>
```

It has no release-ID argument. Keep all meaningful Node/source/render/archive
checks and double-build proof in read-only Quality, adding input-free dispatch.
Replace input-tar promotion with the final verified ZIP and the existing
`ran-profile-b-promotion.json` schema; artifact name is
`ran-booster-release-bootstrap-templates-<run-id>-<attempt>`. One listed public
asset is the fixed pack ZIP. Shared Profile B remains unchanged.

Producer B gives consumer A a non-secret test envelope containing
`producer_sha`, `workflow_run_id`, `run_attempt`, `artifact_id`, `zip_sha256`,
`manifest_sha256`, `pack_version` and the five per-profile template digests.
Retrieve the actual CI artifact through an authorized test harness and verify its
bytes against that envelope. Consumer integration tests take an explicit local
ZIP path, not a latest URL. The harness may supply simulated transport facts for
an unpublished candidate, clearly labeled **fixture**, without putting fake IDs
in the pack or accepting Actions artifacts in production discovery. Test both
plugin/theme renderings and normalized target-file digests through the actual
candidate provider, not Core's older bundled provider.

After publication, separately exercise real GitHub release transport/identity and
the installed Core composition. Candidate-fixture success is not public-release
or installed-feature evidence.

## 6. Initial-only operation and the real host boundary

The initial transaction keeps enough local state to bind user, provider/repository,
package/source revision, target base SHA, exact pack identity, previewed paths and
content, initial operation ID and created branch/commit/PR. A bounded preview
expiry (currently 15 minutes) is retained. Origin metadata is not authority;
confirmation must recompute and compare verified inputs. No receipt migration or
managed-template update state is needed. Package adoption performs only the
bounded read-only provenance/advisory check in section 7.

Known source boundary:

| Owner | Inspected path/symbols and proposed action |
| --- | --- |
| Provider | `src/GitHubProvider.php`: retain five initial `workflow*` operations and current host interface; stop forwarding update operations. |
| Provider | `src/ReleaseDeployments/WorkflowAssistance/GitHubRepositoryReleaseWorkflow.php`: initial status/preview/inspect/setup/outcome only; remove update implementation. |
| Provider | `WorkflowApplicationCoordinator.php`: remove `inspectUpdate`, `setupUpdate`, update-bundle logic and old/new managed-template comparisons; retain exact initial mutation/readback checks. |
| Provider | `SourceReadyAssessor.php`, `ManagedReleaseBundle.php`, state/record classes: use the new fixed file map; remove managed-update assessment/receipt ownership, preserve initial conflicts and operation outcome. |
| Core | `RAN/Admin/ReleaseManagement/ReleaseWorkflowRequestController.php`: allow only `inspect`, `setup`, `outcome`; remove `update_inspect`/`update_setup` dispatch and related request/preview branches. Forged old operations fail before credentials/remote I/O. |
| Core | `ReleaseWorkflowControls.php` composes `ReleaseWorkflowPresenter` and `ReleaseWorkflowDisplay`: remove update buttons, projections/messages and related views/tests; retain initial setup and readback. |
| Core contract | `RAN/RepositoryProvider/RepositoryReleaseWorkflowManagementV2.php` presently REQUIRES both update methods. The sharp-cut initial-only design must not preserve those dead public slots merely for compatibility. |

**G0 host decision:** make the connected Core/provider interface cleanly
initial-only. Introduce `RepositoryReleaseWorkflowManagementV3` with only the five
initial `workflow*` operations (status, preview, inspect, setup, outcome), update
the bundled GitHub provider and Core capability resolution/callers together, and
remove V2/update-method support from the supported composition once the exact
candidate tuple is qualified. There is no V2 compatibility adapter, failure-only
update-method shim or transition-only provider release. The feature is unshipped
and the owner selected a sharp cut; retaining unreachable public update methods
would be compatibility machinery without a supported consumer.

Core must reject forged legacy `update_inspect`/`update_setup` requests during
request validation before credential lookup or provider/remote I/O. Tests cover
that negative boundary and prove no update capability is advertised or reachable.
If source refresh discovers another real V2 consumer, stop and return that concrete
dependency to #81 rather than silently retaining a bridge.

Core's initial-only UI/caller changes belong to integration C, not provider A's
branch. They are part of G1 candidate composition and G2 adoption, not optional
post-release polish. Preserve ordinary release update/deployment controls; those
are unrelated to template maintenance. Agents must refresh/search the exact
caller/test graph before deletion and return any additional concrete coupling.

Initial requests cannot automatically repeat a successful setup, rewrite an
existing PR or replace maintainer files. Preserve bounded operation occupancy and
post-write readback. If a GitHub write acknowledgement is lost, report the exact
known branch/commit/PR or an unverified outcome and stop; do not claim success,
blindly issue a second write, force-update main, delete unknown remote state or
create a general recovery engine. Tests must cover duplicate confirmation,
concurrent requests, target movement and partial/lost responses.

## 7. Production maintenance without another product

**Proposed production boundary:** maintain and secure the supplied starter/shared
components; communicate known defects through existing project channels; target
owners maintain their generated copies. Do not ship background monitoring, a
cached dashboard/status service, scheduler, automatic repair or update engine.
Retain one bounded **on-demand read-only adoption checkpoint**: after Booster has
resolved the canonical package repository and exact observed revision, it may
read the passive origin record and public advisory information described below.
This is a product-scope choice, not a beta exception or a promise of continuous
monitoring.

The initial setup writes `.ran-booster-release-starter.json` at repository root,
in addition to the human-readable setup PR and `RELEASE-STARTER.md`. The JSON is
consumer-owned output, not a downloaded pack entry and not part of the installable
plugin/theme payload. It has exactly this shape:

```json
{
  "schema": "ran-release-starter-origin",
  "schema_version": 1,
  "pack": {
    "repository": "RocketsAreNostalgic/ran-booster-release-bootstrap-templates",
    "repository_id": "<verified positive decimal repository ID>",
    "version": "<canonical X.Y.Z>",
    "tag": "v<X.Y.Z>",
    "commit": "<40-lowercase-hex source commit>",
    "zip_sha256": "<64-lowercase-hex digest>",
    "profile": "source-ready-wordpress-plugin/3"
  },
  "shared_profile_b": {
    "repository": "RocketsAreNostalgic/.github",
    "commit": "<40-lowercase-hex pinned reusable-workflow commit>"
  }
}
```

The theme profile uses `source-ready-wordpress-theme/3`. All keys are required;
additional keys, malformed identity or non-canonical values are invalid. The
record contains no credentials, site/user identifiers, mutable URLs or target
write authority. Initial confirmation binds its values to the already verified
pack/target inputs and previews the file like every other generated path.

When an existing plugin/theme is later **adopted** into Booster, the adoption flow
may read this file from the exact observed repository revision after canonical
repository identity is resolved. Missing, invalid or unrecognised provenance does
**not** block ordinary package adoption: report security status as **not assessed /
unknown** and continue only under the adoption flow's existing authority. A valid
record may be compared, read-only, with **published** security advisories from the
canonical pack/shared-component repositories. Use existing public/authorised
GitHub read access; do not request write or administration credentials for this
check. A merely newer starter is informational and never evidence of a
vulnerability.

The only permitted security outcomes are: recognised origin plus an explicitly
matching published advisory -> show the advisory, affected identity and manual
mitigation/fixed revision; recognised origin with no matching published advisory
-> "no matching known advisory in the checked information", **not** a safety
certificate; missing/invalid origin or unavailable advisory data -> unknown/not
assessed. Advisory matching must use explicit affected/fixed pack versions or
shared-workflow revisions published by the maintainer, not inference from age,
latest version or arbitrary repository contents. The check performs no repository
write, setup, regeneration or automatic repair.

Before public feature acceptance, the designated RAN repository maintainer (Ben
at present) must verify the private report route in the pack/shared component
`SECURITY.md`, own triage/fix/disclosure, and document the supported current
starter/component scope. Publish affected revisions/conditions, fixed release
and manual mitigation, including shared-workflow repins. Keep historical assets
immutable; publish corrected versions and warn against using affected examples.
Current-only maintenance does not mean silence about a defect in an older copy.

Use GitHub repository Security Advisories and linked release/security
announcements, with explicit subscription instructions and a stable public
security page usable without Booster installed. Explain that subscriptions are
opt-in and no exhaustive/push notification guarantee exists. A revised starter
does not repair already copied files or old pinned dependencies. Fixes should
include a focused manual diff/example; arbitrary owner customizations cannot be
automatically certified. No vulnerability details belong in public planning
issues before appropriate disclosure.

Review must confirm that these channels and ownership are operational, not just
links in a template. If a concrete production requirement cannot be met by that
boundary, return it as a narrowly scoped decision; do not quietly grow the G0
starter into a security-monitoring platform.

## 8. Qualification and handoff

G0 review must agree the recipe, schema/map, clean initial-only V3 host cut,
passive origin/adoption security boundary and exact examples. No A/B release on a merely opened PR.
Then A owns provider code; B alone owns overlapping #55/#56 pack code. C owns the
narrow connected Core changes and integrated evidence. No competing writers on
pack schema/templates/build/CI. Do not mutate active provider release #24 or
other agents' documentation branches.

G1 uses named exact provider, producer and Core candidate SHAs, actual ZIP digest,
independent/native ZIP negatives, plugin/theme output, safe initial setup and
inert removed operations. Preserve existing meaningful PHP/Node/host/analysis
checks with a before/after retained/replaced/deleted map. Do not replace host
certification pins merely to make a test green.

G2 records real release/adoption order and actual versions before mutation:
complete provider release -> Core adoption of that released version plus initial
UI/caller changes -> Core archive/quality/release proof -> upgrades on named test
sites -> complete pack release through #55 -> actual installed feature test.
Candidate testing may use unpublished exact artifacts; production dependencies
must resolve. A brief setup-unavailable window is acceptable; no bridge, fake
release ID or partial public pack is introduced to conceal it.

Ben supplies the two disposable-site and plugin/theme fixture repository
identities and safe mutation authority before live operations. For each supported
type, prove installed Booster assessment/preview/confirmation/draft-PR readback;
then, with separately authorized fixture merge/publication, run the generated
Quality/RP/release path and verify/install the resulting exact immutable ZIP.
Exercise pre-merge read-only behavior, changed target, missing settings/permission,
repeat setup and maintainer edits. At least one non-RAN-default-settings fixture
must substantiate external-repository support. Tests on disposable sites meet the
same production criteria; no results are assumed today.

Every implementation and this proposal receive separate `@codex review` and
`@codex security review` requests. Resolve all substantive findings on the final
head. Normal protected merge methods and specific owner approvals remain; Core
bot release proposals use normal merge commits. No settings/secret/site resets,
new analysis floors, broad naming changes or Blacksmith AI delegation. The final
coordinator hands actual evidence to #55/#56/#81/#57/#47; code-ready is not
installed, published or functionally proven.

## 9. Source basis and review status

Audited snapshots (refresh before implementation): `.github`
`8fefa7da961d5fcb36d706a78578ddb5f39ffa4a`, pack
`29a194be54c383e91758665d99461017386fe2e8`, provider
`7cd2c0624e2a41ccd8c2b1e879ac743eddb8f800`, Core
`467070d6f3635f832dc677cb813b13453a2613dd`. These are not release approval or future
certification pins. Existing .github #83 and Core #176 documentation owners are
unaffected by these two new files.

- [Actual shared interface and promotion contract](RELEASE_PROFILE_B.md), backed
  by `.github/workflows/release-profile-b.yml` at the audited `.github` SHA.
- [Pack schema](https://github.com/RocketsAreNostalgic/ran-booster-release-bootstrap-templates/blob/29a194be54c383e91758665d99461017386fe2e8/schema/template-pack.schema.json),
  `templates/shared/{release-please.yml,build-release.sh,verify-release.sh,upload-release-assets.sh}.tmpl`,
  `.github/workflows/quality.yml` and `SECURITY.md` at that same pack SHA.
- [Current mandatory host interface](https://github.com/RocketsAreNostalgic/ran-booster/blob/467070d6f3635f832dc677cb813b13453a2613dd/RAN/RepositoryProvider/RepositoryReleaseWorkflowManagementV2.php)
  and `RAN/Admin/ReleaseManagement/ReleaseWorkflowRequestController.php` at that Core SHA.
- [Provider source](https://github.com/RocketsAreNostalgic/ran-booster-github-provider/tree/7cd2c0624e2a41ccd8c2b1e879ac743eddb8f800/src/ReleaseDeployments/WorkflowAssistance).
- [GitHub reusable workflows](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows),
  [workflow permissions](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax),
  [PR execution security](https://docs.github.com/en/actions/reference/security/securely-using-pull_request_target),
  [security advisories](https://docs.github.com/en/code-security/concepts/vulnerability-reporting-and-management/repository-security-advisories).

**Review checkpoints still open:** accept the narrow stable/main/source-ready
recipe, the required-V2 rejection-slot disposition, and the production
communication model; review examples and contract together. Any amendment updates
both docs and #81 before agents implement. No source behavior or end-to-end proof
is claimed by this proposal.
