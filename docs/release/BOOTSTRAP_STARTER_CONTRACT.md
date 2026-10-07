# Initial release starter contract

Booster's initial release starter proposes a release setup in a draft PR for a
source-ready WordPress plugin or theme. The maintainer reviews the proposal and
owns the generated files. Release Please manages subsequent version and release
PRs; Booster does not regenerate, update or repair the copied starter files.

The supported operations are status, preview, inspection, setup and outcome
readback. The PHP reader in Booster's bundled GitHub provider validates the
pack ZIP as data; it never executes the templates on WordPress. Generated files
become repository code subject to normal review and maintenance.

**Delivery status reported in #81, reviewed 7 October 2026:**
[#81](https://github.com/RocketsAreNostalgic/.github/issues/81) records source
integration and immutable component publication as delivered. The combined
plugin/theme setup → generated release → installed product journey remains
unaccepted. UI work and owner-verified manual/end-to-end testing remain deferred
until Ben confirms interactive verification can resume; required notices and
in-app guidance remain tracked in
[#85](https://github.com/RocketsAreNostalgic/.github/issues/85). These documents
define the approved product, not proof of complete delivery.

## 1. Supported targets and boundaries

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

The consumer derives a reviewed PHP syntax runtime from the target's unambiguous
`Requires PHP` header. The first recipe accepts only declared `major.minor` values
in the reviewed set `7.4`, `8.0`, `8.1`, `8.2`, `8.3`, `8.4`, `8.5`; another or
missing value is a manual-setup case. Generated Quality uses that exact value for
the bounded payload syntax check on GitHub-hosted `ubuntu-24.04`. The generated
target adapters are Bash and do not install Node or a package manager merely
because the producer repository itself is Node-based. These are explicit tooling
choices, not a claim to certify every PHP or WordPress version a target declares.
Product-specific tests and additional compatibility requirements remain the
target maintainer's responsibility. No artificial Composer project is generated.

Unsupported does not mean insecure or unmanageable by Booster. Explain the exact
limitation and offer manual customization guidance without speculative writes.
Other Booster installation, branch and release-management features keep their
existing eligibility and behavior.

## 2. Generated files and execution

The [examples](BOOTSTRAP_STARTER_EXAMPLES.md#1-files-and-local-responsibilities)
show the generated file set. Read-only Quality builds and verifies the package;
shared Profile B owns Release Please and publication. Target-local scripts only
build and independently verify the archive. `version.txt`, the Release Please
manifest and the WordPress header must agree. The committed `release-contents.txt`
file selects the payload.

`RELEASE-STARTER.md` explains maintainer responsibilities. The passive
`.ran-booster-release-starter.json` origin record supports the read-only advisory
check in section 7; neither file gives Booster continuing write authority.
Arbitrary build hooks, automatic ecosystem detection and extra deployment
destinations are outside the supported recipe. No template-update engine,
background scanner, cached status service, notification scheduler or automatic repair is supplied. Booster's own host certification,
database tests and updater integration checks are not generated into targets.

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

## 3. Setup and execution prerequisites

The shared workflow requires **default branch `main`**: its
admission, ref checks and RP target all require `main`. The starter must refuse
another default branch; do not rename it.

Assessment, preview and creation of the initial draft setup PR may proceed before
the owner completes Actions, runner, bot-PR or immutable-release configuration.
These are execution prerequisites, not gates on receiving the recipe. Continue
to enforce supported-target eligibility, verified pack transport, user/nonce,
repository identity, current HEAD, exact confirmation-time re-fetch, file conflicts
and actual workflow-file/branch/PR write authority. Successful setup means
**“Setup PR created”**, not “All settings verified” or “Release automation ready.”

Before activating the corresponding automation, the owner must configure Actions;
access to the public pinned reusable workflow and its pinned Actions; GitHub-hosted
runner/tool availability; permission for Release Please to create PRs; the caller's
required `contents`, `issues`, `pull-requests` and `actions` token scopes; and
immutable releases. Preserve meaningful checks and merge protections. Recommend
completing this configuration before merging/activating workflows, while explaining
that read-only Quality can already run on the setup PR and a merge can trigger
main-push Quality and the shared release workflow. A draft PR or its merge is not
an inert configuration step.

Booster does not query repository/org immutability settings, even optionally with
a more privileged credential. Do not add Administration permission, attestation,
settings polling, automatic configuration or organization enumeration. Describe
administrative settings as **owner-managed and not checked by Booster**. This does
not weaken the template pack's mandatory trusted immutable transport or the
supplied recipe's strict immutable publication/readback requirement. No opt-out,
permissive publisher or fallback is supplied. Test a target outside assumptions
of RAN organization defaults before advertising general GitHub.com eligibility.
No Blacksmith subscription or AI feature is required by generated output.

Static setup-PR and `RELEASE-STARTER.md` guidance must remain useful when no job
can run: disabled Actions, rejected workflow/policy, or runner/account constraints
cannot be explained by an annotation inside a job that never starts. Point to the
[shared Profile B contract](RELEASE_PROFILE_B.md) for publication and retry
boundaries. Executing jobs may explain observed failures using bounded existing
evidence; a generic 403 does not establish which administrative setting is wrong.

The publisher attaches tested assets, publishes the draft, then checks
`immutable == true`. Misconfiguration can therefore leave a **public mutable
release and a failed job**; never claim publication was prevented or rolled back.
Inconclusive readback means the publication outcome is unknown. Enabling the
setting and blindly rerunning does not make an existing mutable release immutable.
The maintainer must inspect the actual release/tag/assets and Release Please
version, manifest and lifecycle state, then follow a reviewed next-version path;
no asset replacement, tag movement, label repair or automatic rollback is provided.
Retries retain the original event/SHA, exact run/attempt artifact custody and
current-main admission rules; manual Quality dispatch is not publisher admission.

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
| `pack_version` | String, stable canonical `X.Y.Z`, no leading-zero numeric components and at most 63 ASCII bytes. |
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
| `quality-workflow` | `templates/shared/quality.yml.tmpl` -> `.github/workflows/quality.yml` | `PACKAGE_SLUG: slug`, `PHP_VERSION: php_version` |
| `release-workflow` | `templates/shared/release-please.yml.tmpl` -> `.github/workflows/release-please.yml` | `PACKAGE_SLUG: slug` |
| `release-please-config` | `templates/shared/release-please-config.json.tmpl` -> `release-please-config.json` | `BASE_SHA: sha`, `EXTRA_FILES_JSON: json_fragment`, `PACKAGE_SLUG: slug` |
| `build-release-script` | `templates/shared/build-release.sh.tmpl` -> `scripts/build-release.sh` | `HEADER_PATH: path`, `PACKAGE_SLUG: slug`, `PACKAGE_TYPE: package_type` |
| `verify-release-script` | `templates/shared/verify-release.sh.tmpl` -> `scripts/verify-release.sh` | `HEADER_PATH: path`, `PACKAGE_SLUG: slug`, `PACKAGE_TYPE: package_type`, `UPDATE_URI: github_uri` |

There are six physical files: the manifest and five templates. Do not include
source schemas, tooling, executable dependencies or an undeclared member in the
public ZIP. Both profiles share the same RP config template.
All pack members are inert regular files, not executable members or symlinks.

Tokens are literal `{{RAN_NAME}}`. Values are derived by the consumer from the
verified target, never interpreted as expressions. Slugs match
`[a-z0-9]+(-[a-z0-9]+)*`, bounded to 100 ASCII bytes; `php_version` is one of
`7.4`, `8.0`, `8.1`, `8.2`, `8.3`, `8.4`, `8.5` and must equal the target's
verified `Requires PHP` header; SHA is 40 lowercase hex; package type is `plugin`
or `theme`; header is one root filename using ASCII letters, digits, dot,
underscore or hyphen (neither dot nor dot-dot). URI is the exact
canonical `https://github.com/<owner>/<repository>` already bound to the target.
Reject control characters, quoting/injection tokens and unresolved/unknown
placeholders. Before setup, require the canonical version to be at most 63 bytes,
`<slug>-<version>.zip` to be at most 200 bytes, and
`release-please--branches--main--components--<slug>` to be at most 200 bytes;
refuse rather than rely on filesystem/ref implementation limits. The JSON fragment
is serialized by the consumer from its fixed header/optional readme extra-file
map, not accepted as arbitrary JSON text.
Actions expressions such as `${{ github.sha }}` remain literal template content.

The consumer additionally creates `.release-please-manifest.json`, `version.txt`,
`release-contents.txt`, `.ran-booster-release-starter.json` and `RELEASE-STARTER.md`
from its verified inputs. All output
files use Git mode `100644`; scripts are invoked through Bash. It may perform
only the previewed bounded version-annotation edit to the identified header and
optional `readme.txt`. Formatter/ignore configuration remains maintainer-owned;
the starter does not edit `.prettierignore` or add formatter-specific policy.
Contradictory/custom version rules are a manual case. No target path, mode, operation, permission or trigger can be added
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
to find an old supported renderer. If no eligible release exists, report the pack as unavailable. A different API
is unsupported; malformed identity or archive content is invalid. None returns a usable
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
are payload authority. The allowlist is sorted explicit file
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
A bounded payload PHP syntax check fails on any parse error.

The pack's **own** build interface is:

```text
pnpm run build -- <output-directory> <repository-id> <tag> <exact-source-commit>
bash scripts/verify-pack.sh <zip-path> <repository-id> <tag> <exact-source-commit>
```

It has no release-ID argument. Read-only Quality runs the Node, source, rendering
and archive checks, including double-build proof and input-free dispatch.
Promotion uses the final verified ZIP and the existing
`ran-profile-b-promotion.json` schema; artifact name is
`ran-booster-release-bootstrap-templates-<run-id>-<attempt>`. One listed public
asset is the fixed pack ZIP. Shared Profile B retains publication ownership;
separately reviewed shared diagnostics do not move publisher logic into the pack.

The producer gives the provider consumer a non-secret test envelope containing
`producer_sha`, `workflow_run_id`, `run_attempt`, `artifact_id`, `zip_sha256`,
`manifest_sha256`, `pack_version` and the five per-profile template digests.
Retrieve the actual CI artifact through an authorized test harness and verify its
bytes against that envelope. Consumer integration tests take an explicit local
ZIP path, not a latest URL. The harness may supply simulated transport facts for
an unpublished candidate, clearly labeled **fixture**, without putting fake IDs
in the pack or accepting Actions artifacts in production discovery. Test both
plugin/theme renderings and normalized target-file digests through the actual
candidate provider identified in the test evidence.

After publication, separately exercise real GitHub release transport/identity and
the installed Core composition. Candidate-fixture success is not public-release
or installed-feature evidence.

## 6. Initial operation and host interface

The initial transaction keeps enough local state to bind user, provider/repository,
package/source revision, target base SHA, exact pack identity, previewed paths and
content, initial operation ID and created branch/commit/PR. A bounded preview
expiry (currently 15 minutes) is retained. Origin metadata is not authority;
confirmation must recompute and compare verified inputs. No managed-template
update state is needed. Package adoption performs only the
bounded read-only provenance/advisory check in section 7.

The supported Core/provider composition uses
`RepositoryReleaseWorkflowManagementV3`, with only the five initial `workflow*`
operations: status, preview, inspect, setup and outcome. V2 compatibility
adapters, update-method shims and template-maintenance controls are outside this
contract. Ordinary release update and deployment controls remain supported;
those do not maintain the starter files.

Core accepts only `inspect`, `setup` and `outcome` requests for this feature.
Forged `update_inspect` or `update_setup` requests must fail validation before
credential lookup or provider/remote I/O. Tests prove that no template-update
capability is advertised or reachable. Any newly discovered dependency on V2
requires an explicit decision in
[#81](https://github.com/RocketsAreNostalgic/.github/issues/81), not an implicit
compatibility bridge.

Initial requests cannot automatically repeat a successful setup, rewrite an
existing PR or replace maintainer files. Preserve bounded operation occupancy and
post-write readback. If a GitHub write acknowledgement is lost, report the exact
known branch/commit/PR or an unverified outcome and stop; do not claim success,
blindly issue a second write, force-update main, delete unknown remote state or
create a general recovery engine. Tests must cover duplicate confirmation,
concurrent requests, target movement and partial/lost responses.

## 7. Maintenance and advisory checks

Maintain and secure the supplied starter/shared
components; communicate known defects through existing project channels; target
owners maintain their generated copies. Do not ship background monitoring, a
cached dashboard/status service, scheduler, automatic repair or update engine.
Retain one bounded **on-demand read-only adoption checkpoint**: after Booster has
resolved the canonical package repository and exact observed revision, it may
read the passive origin record and public advisory information described below.
This check does not provide continuous monitoring.

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
assessed. Advisory matching uses the bounded machine-readable index below; prose is never
parsed for affected identity. The check performs no repository write, setup,
regeneration or automatic repair.

### Machine-readable advisory matching

The canonical pack repository maintains
`security/release-starter-advisories.json` on its default branch as the small
current matching index. It is maintenance metadata, not part of the public pack
ZIP and not copied into target repositories. Adoption fetches it only from the
already identity-verified canonical pack repository. Bound the response to 64 KiB
and 64 advisory entries. Missing/unavailable/invalid index data makes the adoption
security result **unknown/not assessed**; it never falls back to prose matching.

The document has exactly `{schema, schema_version, advisories}`, with
`schema: "ran-release-starter-advisories"`, integer `schema_version: 1`, and
an array of unique advisory objects. Each advisory is exactly:

```json
{
  "ghsa_id": "GHSA-xxxx-xxxx-xxxx",
  "repository": "RocketsAreNostalgic/ran-booster-release-bootstrap-templates",
  "affected": {
    "pack_versions": ["1.2.3"],
    "shared_profile_b_commits": []
  },
  "fixed": {
    "pack_version": "1.2.4",
    "shared_profile_b_commit": null
  }
}
```

`repository` is exactly either the canonical pack repository or
`RocketsAreNostalgic/.github`. `ghsa_id` is canonical uppercase
`GHSA-[23456789cfghjmpqrvwx]{4}-[23456789cfghjmpqrvwx]{4}-[23456789cfghjmpqrvwx]{4}`.
`affected.pack_versions` contains unique canonical stable versions (each at most
63 bytes); `affected.shared_profile_b_commits` contains unique 40-lowercase-hex
commits. At least one affected list is non-empty. A pack-repository advisory uses
pack versions; a `.github` advisory uses shared Profile B commits. `fixed`
contains exactly the corresponding fixed identity and the other field is null.
No ranges, wildcards, "latest", branch names or free-form conditions are accepted.

For every index entry, the checker must also retrieve the referenced **published**
GitHub Security Advisory from the named canonical repository and require its
`ghsa_id`/repository identity to agree. An index entry whose advisory is absent,
withdrawn, inaccessible or not published makes the security result unknown; do
not treat the index alone as an advisory. A warning is emitted only when the
validated origin's exact pack version or shared Profile B commit occurs in the
corresponding validated affected list. Fixed identities are displayed as manual
mitigation targets, not automatically installed. Duplicate GHSA IDs, unknown
fields, malformed identities or oversized data
invalidate the whole index for that check. Within each advisory, affected
identities must be unique and must not equal its fixed identity. Different
published advisories may identify the same affected version or commit and name
different fixes. Return every independently verified matching advisory with its
own manual mitigation target.

Maintainers update the index as part of publishing/maintaining the corresponding
Security Advisory and focused manual fix guidance. Tests cover exact pack and
workflow matches, no match, malformed/duplicate/oversized index, unpublished or
missing GHSA, unavailable API/index and fixed-identity display.

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
boundary, return it as a narrowly scoped decision; keep this starter within its
defined scope.

## 8. Qualification and acceptance

Qualification identifies the exact provider, producer and Core commits and the
actual ZIP digest. It covers independent archive verification and rejection of
malformed archives by both the verifier and native ZIP tools. Test both plugin
and theme output, safe setup and rejection of unsupported operations. Preserve meaningful PHP, Node, host-integration and static-analysis
gates. Changing a certification pin does not substitute for proving compatibility.

Use the [test exchange and acceptance runbook](BOOTSTRAP_STARTER_EXAMPLES.md#8-exact-test-exchange-and-acceptance-runbook).
It requires installed plugin and theme journeys, a target outside RAN settings
defaults, read-only pre-merge execution, permission and repeat-operation tests,
protected-merge proof and installation of the immutable ZIP. Candidate tests may
use explicitly identified unpublished artifacts; production dependencies must
resolve to real releases. Source or fixture success is not installed acceptance.

Ben must identify and authorize the two disposable sites and fixture repositories.
Fixture merges and publication need separate approval. Disposable tests still
meet production criteria; no settings, secrets or site resets are implied.
Record incomplete or failed requirements in
[#81](https://github.com/RocketsAreNostalgic/.github/issues/81) and keep required
[#85 notices and guidance](https://github.com/RocketsAreNostalgic/.github/issues/85)
open until their installed lifecycle tests pass. Delivery ownership, release
order and review arrangements belong in those work issues. They do not alter the
product contract or grant merge/publication authority.

## 9. Implementation references and decision provenance

[Profile B implementation evidence](RELEASE_PROFILE_B.md#implementation-evidence)
links the publisher's current code and tests alongside the inspected revision.
For navigation, the producer's [current qualification guide](https://github.com/RocketsAreNostalgic/ran-booster-release-bootstrap-templates/blob/main/docs/QUALIFICATION.md)
and [delivery evidence in #55](https://github.com/RocketsAreNostalgic/.github/issues/55)
cover pack construction and exchange; [#81](https://github.com/RocketsAreNostalgic/.github/issues/81)
owns connected implementation and installed acceptance. Inspect the relevant
implementation revision when changing its mechanism; neither this contract nor
an earlier inspection certifies a later execution.

Optional decision history: [contract approval #84](https://github.com/RocketsAreNostalgic/.github/pull/84),
[strict immutability](https://github.com/RocketsAreNostalgic/.github/issues/81#issuecomment-5839238578),
[proposal and execution prerequisites](https://github.com/RocketsAreNostalgic/.github/issues/81#issuecomment-5839475013),
[failure diagnostics](https://github.com/RocketsAreNostalgic/.github/issues/81#issuecomment-5839662944)
and [overlapping advisory identities](https://github.com/RocketsAreNostalgic/.github/issues/81#owner-decision--overlapping-advisory-identities-29-september-2026).
The [original source inspection](https://github.com/RocketsAreNostalgic/.github/blob/70df865a00734542e6bb663e684d86b8b4757b8e/docs/release/BOOTSTRAP_STARTER_CONTRACT.md#9-source-basis-and-review-status)
is retained as historical provenance, not a current certification pin.
