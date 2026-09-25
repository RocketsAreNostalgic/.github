# Initial release starter: concrete G0 examples

**Frozen G0 examples, not deployed templates or execution evidence.** Read
[the contract](BOOTSTRAP_STARTER_CONTRACT.md) with this file. G0 was accepted in
[#84](https://github.com/RocketsAreNostalgic/.github/pull/84); producer B must still
implement/test the adapters and materialize the qualified template ZIP. These
examples do not claim an executable producer/consumer pair already exists. Later
owner decisions distinguish proposal delivery from owner-managed execution
configuration without changing this workflow/file-map contract.

The fictional target is `example/acorn-plugin`, root plugin `acorn-plugin.php`,
slug `acorn-plugin`, version `0.1.0`. The forty `1` characters in `bootstrap-sha`
are explicitly a **fixture base**, not a real commit or adoption pin. The consumer
substitutes an actual verified base SHA in a real proposal. The reusable-workflow
and Action references below are real audited source pins, not floating examples.

## 1. Files and local responsibilities

```text
.github/workflows/quality.yml           read-only exact-source checks/build
.github/workflows/release-please.yml    thin shared publisher caller
release-please-config.json              RP simple strategy and bounded extra files
.release-please-manifest.json           initial RP version state
version.txt                            RP simple version source
release-contents.txt                    explicit committed payload file list
scripts/build-release.sh               deterministic projection/ZIP adapter
scripts/verify-release.sh              independent archive/source verification
.ran-booster-release-starter.json       passive origin for read-only adoption check
RELEASE-STARTER.md                      origin and maintainer/security handoff
```

The initial diff also shows only the bounded header/optional readme version
annotations. Formatter/ignore configuration remains target-maintainer owned.
Nothing writes target main, creates repository secrets or silently changes Actions
settings.
Existing target files at any generated path make automatic setup a conflict.

Compared with the old recipe, `upload-release-assets.sh` and
`.ran-booster-release-profile.json` disappear. There is no template-update
receipt or polling job. The publication body disappears from the local release
workflow. The new Quality file supplies the actual tested-artifact boundary;
`RELEASE-STARTER.md` explains the one-time handoff rather than granting ownership.
File count is not the goal: every surviving local responsibility has a reason.

## 2. Generated Quality workflow

This one job runs the same path for PRs, main pushes and input-free dispatch.
It does not identify bot accounts, reconstruct merged PRs, skip a candidate's
checks or reuse a different run's artifact. No Composer/npm build is inferred.

```yaml
name: Quality

on:
  pull_request:
    branches: [main]
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read

concurrency:
  group: quality-${{ github.workflow }}-${{ github.event_name == 'pull_request' && github.ref || github.sha }}
  cancel-in-progress: ${{ github.event_name == 'pull_request' }}

jobs:
  quality:
    name: Quality
    runs-on: ubuntu-24.04
    timeout-minutes: 15
    steps:
      - uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd
        with:
          fetch-depth: 0
          persist-credentials: false
          ref: ${{ github.event_name == 'pull_request' && github.event.pull_request.head.sha || github.sha }}

      - name: Verify exact source
        shell: bash
        env:
          SOURCE_SHA: ${{ github.event_name == 'pull_request' && github.event.pull_request.head.sha || github.sha }}
        run: |
          set -euo pipefail
          [[ "$SOURCE_SHA" =~ ^[0-9a-f]{40}$ ]]
          test "$(git rev-parse HEAD)" = "$SOURCE_SHA"

      - uses: shivammathur/setup-php@f3e473d116dcccaddc5834248c87452386958240
        with:
          php-version: '{{RAN_PHP_VERSION}}'
          coverage: none

      - name: Build and check the exact installable package
        shell: bash
        env:
          SOURCE_SHA: ${{ github.event_name == 'pull_request' && github.event.pull_request.head.sha || github.sha }}
        run: |
          set -euo pipefail
          export TZ=UTC LC_ALL=C
          test "$(git rev-parse HEAD)" = "$SOURCE_SHA"
          version="$(git show "${SOURCE_SHA}:version.txt")"
          [[ "$version" =~ ^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$ ]]
          test "${#version}" -le 63
          archive="acorn-plugin-${version}.zip"
          test "${#archive}" -le 200
          test "$(git show "${SOURCE_SHA}:.release-please-manifest.json" | jq -er '."."')" = "$version"
          work="$(mktemp -d)"
          trap 'rm -rf "$work"' EXIT
          bash scripts/build-release.sh "$SOURCE_SHA" "$version" "$work/one"
          bash scripts/build-release.sh "$SOURCE_SHA" "$version" "$work/two"
          cmp "$work/one/$archive" "$work/two/$archive"
          bash scripts/verify-release.sh "$work/one/$archive" "$version" "$SOURCE_SHA"
          # Extraction follows independent member/type/resource verification.
          unzip -q "$work/one/$archive" -d "$work/payload"
          find "$work/payload" -type f -name '*.php' -print0 | xargs -0 -r -n1 php -l
          # Never merge a tracked/untracked output tree or symlink into evidence.
          test ! -e .ran-booster-release-dist
          test ! -L .ran-booster-release-dist
          mkdir .ran-booster-release-dist
          cp "$work/one/$archive" ".ran-booster-release-dist/$archive"
          digest="$(sha256sum ".ran-booster-release-dist/$archive" | cut -d ' ' -f 1)"
          jq -n \
            --arg repository "$GITHUB_REPOSITORY" \
            --arg source "$SOURCE_SHA" \
            --arg tag "v$version" \
            --arg name "$archive" \
            --arg digest "$digest" \
            '{schema:"ran-profile-b-promotion",schema_version:1,
              repository:$repository,quality_commit:$source,source_commit:$source,
              tag:$tag,assets:[{name:$name,sha256:$digest}]}' \
            > .ran-booster-release-dist/ran-profile-b-promotion.json
          test "$(find .ran-booster-release-dist -mindepth 1 -maxdepth 1 -type f | wc -l)" -eq 2

      - uses: actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a
        with:
          name: ran-starter-${{ github.run_id }}-${{ github.run_attempt }}
          path: |
            .ran-booster-release-dist/acorn-plugin-*.zip
            .ran-booster-release-dist/ran-profile-b-promotion.json
          include-hidden-files: true
          if-no-files-found: error
          retention-days: 30
```

The output destination must be newly created and contain exactly the expected ZIP
and manifest. Producer tests include a pre-existing tree, an extra ZIP and a
symlink as negative cases. A retained build adapter can already call its verifier;
the explicit Quality verification above documents the required independent check,
not a demand for a second verification framework.

PHP syntax is a modest useful starter check, not a claim of semantic correctness
or a comprehensive declared-platform compatibility suite. Real target tests are
an intentional maintainer extension. The feature's own integration tests still
prove plugin activation/theme installation, safe repository changes and the
release workflow end to end; they are not copied into every generated project.

A setup PR may run this code before merge. It receives no supplied secrets and
only read-only contents permission. The privileged workflow below cannot admit
its PR/dispatch runs. Review actual initial-PR execution in a fixture, not only
this YAML's syntax. A privileged `pull_request_target` shortcut is not acceptable.

## 3. Generated release caller

```yaml
name: Release Please

on:
  workflow_run:
    workflows: [Quality]
    types: [completed]
    branches: [main]

permissions: {}

jobs:
  release:
    permissions:
      contents: write
      issues: write
      pull-requests: write
      actions: write
    uses: RocketsAreNostalgic/.github/.github/workflows/release-profile-b.yml@2df8eb927d3d9a43870b4ba039e956e50f41e050
    with:
      expected-workflow-path: .github/workflows/quality.yml
      release-pr-head: release-please--branches--main--components--acorn-plugin
      artifact-prefix: ran-starter
```

No `secrets: inherit`, local publisher steps, independent concurrency/retry state,
release-ID query, label reconciliation, tag reconstruction or ZIP rebuild appears
here. The shared workflow owns authenticated main admission, RP, exact candidate
dispatch and final promotion/readback. The caller uses its repository's automatic
token, not a token from RAN or from WordPress. RAN organization defaults do not
supply missing permissions/settings to a repository owned by someone else.

## 4. Version and payload inputs

`release-please-config.json` for the fixture with a conventional `readme.txt`:

```json
{
  "bootstrap-sha": "1111111111111111111111111111111111111111",
  "draft": true,
  "force-tag-creation": true,
  "packages": {
    ".": {
      "release-type": "simple",
      "package-name": "acorn-plugin",
      "changelog-path": "CHANGELOG.md",
      "include-component-in-tag": false,
      "include-v-in-tag": true,
      "extra-files": [
        {"type": "generic", "path": "acorn-plugin.php"},
        {"type": "generic", "path": "readme.txt"}
      ]
    }
  }
}
```

The consumer generates the exact `extra-files` array from verified paths. With no
readme it includes only the header; there is no raw user-supplied JSON parameter.
For this fixture the verified `Requires PHP: 8.2` header supplies
`{{RAN_PHP_VERSION}} = 8.2`; targets outside the reviewed PHP-version set are a
manual-setup case.
The RP simple strategy owns `version.txt`; it updates the annotated header and
optional readme. The builder verifies equality and does not calculate or patch a
version after tests. No `skip-github-release: true` is permitted.

`.release-please-manifest.json`:

```json
{".": "0.1.0"}
```

`version.txt`:

```text
0.1.0
```

`release-contents.txt` for a concrete minimal plugin:

```text
LICENSE
acorn-plugin.php
readme.txt
```

The exact initial WordPress header annotation is bounded and shown in the PR:

```php
<?php
/**
 * Plugin Name: Acorn Plugin
 * x-release-please-start-version
 * Version: 0.1.0
 * x-release-please-end
 * Requires at least: 7.0
 * Requires PHP: 8.2
 * Update URI: https://github.com/example/acorn-plugin
 */
```

`readme.txt` retains its contents and receives the same bounded markers around
its existing `Stable tag: 0.1.0` line. Conflicting or ambiguous metadata is not
silently rewritten. The starter does not edit formatter configuration or invent a
formatter dependency; target-owned formatting policy remains target-owned.
The implementation must exercise a real RP candidate to prove these annotations
and version sources stay coherent, not merely assert that the marker text exists.

## 5. Necessary theme differences

The second example is `example/acorn-theme`, slug `acorn-theme`. The five template
logical IDs and workflow graph are identical. The consumer supplies type `theme`,
header `style.css`, matching Update URI and the theme profile `/3`. Only the
literal slug occurrences, header/verification inputs and runtime file list differ;
there is no separate theme publication subsystem.

A minimal classic-theme fixture has:

```text
LICENSE
index.php
style.css
```

The initial `extra-files` array contains only `style.css` unless that repository
also has the supported conventional readme. The header example is:

```css
/*
Theme Name: Acorn Theme
x-release-please-start-version
Version: 0.1.0
x-release-please-end
Requires at least: 7.0
Requires PHP: 8.2
Update URI: https://github.com/example/acorn-theme
*/
```

A block theme can use its already-committed `theme.json`/templates under the same
source-ready rule when the assessor and fixture genuinely prove the required
layout. Do not claim support simply from a `.css` header or add framework-specific
compilation. The initial minimum fixture is classic theme; any advertised extra
layout needs explicit positive and negative evidence within the same narrow scope.

## 6. Adapter review contract

The complete script bodies are implementation deliverables, not hidden publisher
code. Review the current concrete adapters against these requirements, retaining
useful safety code rather than writing a new ZIP framework:

| Adapter | Must do | Must not do |
| --- | --- | --- |
| `build-release.sh` | Resolve the explicit commit; read allowlist, header and version inputs from it; project only exact regular Git blobs; normalize timestamp/order/modes; build `<slug>-<version>.zip`; report failures truthfully. | Install dependencies, execute the target's PHP, read dirty payload, dereference symlinks/submodules, call GitHub, create drafts, compute a new version or accept a release ID. |
| `verify-release.sh` | Independently check safe archive/member/resource envelope before extraction; compare the complete member set and bytes with the same committed projection; validate slug/header/version/Update URI and required payload. | Trust only filename/checksum, ignore extra files, infer build outputs, mutate the archive or query publication state. |

The production acceptance tests supply real builder/verifier bodies, run two
identical-input builds, and inject dirty/untracked files, unsafe allowlists,
symlinks, wrong root/version/URI, extra members and digest/resource failures.
Neither this table nor an illustrative YAML block is executable feature proof.

## 7. Human-readable handoff instead of managed state

The consumer writes the passive `.ran-booster-release-starter.json` origin record
defined by the contract and `RELEASE-STARTER.md` with the following short
structure. Values in brackets below are replaced from the verified initial
pack/target; they are prose placeholders, not additional template-pack
capabilities. The JSON file is committed repository metadata but is deliberately
excluded from `release-contents.txt` and therefore from the installable ZIP.

```text
Release starter

Created once by Booster from:
- pack version/profile: [actual pack version] / [actual /3 profile]
- pack source commit and ZIP SHA-256: [actual values]
- shared publisher: RocketsAreNostalgic/.github, [actual pinned commit]
- setup PR: see this file's introducing commit and pull request

You own these files after setup. Booster does not update or repair them.

Setup PR created does not mean release automation is ready. You may receive this
proposal before configuring execution settings; Booster does not query repository
or organization immutability settings or require Administration permission.

Before activating workflows (recommended before merging):
- review every proposed file and the runtime allowlist;
- configure Actions/reusable-workflow access, runner availability, runtime token
  permissions, bot PR creation, immutable releases and protected-merge checks;
- distinguish the site-controlled setup credential from runtime GITHUB_TOKEN;
- review the PR's read-only Quality execution: a draft PR can run before merge;
- review what merging activates: main Quality and the shared release workflow;
- check the PR Quality result and subsequent main run when execution is available.
Administrative settings are owner-managed and not checked by Booster. Publication
remains strictly immutable; this recipe has no permissive publication mode.

For a release:
- use Conventional Commits and review Release Please's version/changelog PR;
- merge using your repository's approved method;
- require fresh main Quality and immutable release/ZIP readback;
- consumers install the attached ZIP, not GitHub's generated source archive.

Keep the allowlist current when adding runtime files. Add product-specific
checks deliberately; complex builds need a maintainer-owned release setup.
Never overwrite a published release or move its tag to repair a failure.

If no workflow runs, inspect Actions/workflow-policy acceptance and runner/account
availability in GitHub; in-job diagnostics cannot run before a job starts. For an
executing failure, use its stage/outcome and the shared Profile B publication and
retry guidance. A 403 alone does not identify a disabled setting or prove that no
branch, tag, draft or asset was created.
Publication precedes immutable readback. A confirmed public mutable release stays
public despite a red job; an inconclusive readback leaves the outcome unknown.
Enabling immutability and blindly rerunning cannot qualify that old release.
Inspect actual Release Please version/manifest/lifecycle and release/tag/asset state
before taking a maintainer-owned next-version path. No automatic rollback, label
repair, asset replacement or tag movement is supplied. Respect original event/SHA,
exact run/attempt artifact custody and current-main admission on retry. Manual
Quality dispatch does not admit publication. An open release PR or no releasable
change can be ordinary non-publication; do not infer failure merely from no release.

Security and maintenance:
- use the template pack repository SECURITY.md / private reporting route;
- follow its Security Advisories and linked release announcements;
- watch the pack and shared workflow repositories' release announcements;
- review affected revisions and apply manual fixes, including workflow repins.
Origin records do not prove customized code is currently affected or fixed.
On package adoption, Booster may validate the exact observed repository's passive
origin record and compare it read-only with published advisories for the canonical
pack/shared components. A specific match produces a warning and manual mitigation;
no match means only no matching known advisory in the checked information; missing,
invalid or unavailable provenance/advisory data is unknown/not assessed and does
not by itself block ordinary adoption. A newer starter alone is not a vulnerability.
There is no background scan, notification guarantee or repair service.
```

The actual output must contain concrete official reporting/announcement links,
not these shorthand descriptions. Link publication/retry guidance to the existing
[shared Profile B contract](RELEASE_PROFILE_B.md) using a concrete canonical URL in
generated output; keep the setup PR and handoff usable without Booster or a
successful Actions run. B updates its outdated managed-update security
policy accordingly; the coordinator verifies the reporting/subscription route
before public feature acceptance. This process applies in production regardless
of user count. No per-site tracking, telemetry, advisory database, scheduler or
write-capable adoption service is introduced. The bounded origin parser/check is
part of the reviewed initial-only contract and grants no setup/update authority.

## 8. Exact test exchange and acceptance runbook

These steps belong to the integration/test harness, not generated project files:

1. B records its actual source SHA and uploads the twice-built/verified API-3 ZIP
   plus manifest/render evidence in its CI artifact. Record run/attempt/artifact
   IDs and SHA-256; do not publish a partial API-3 release to provide a fixture.
2. A downloads that exact authorized artifact into the test environment, verifies
   its declared digests and invokes the actual candidate PHP reader with that
   local ZIP. Label simulated transport as fixture-only. Produce both generated
   file sets and compare them with B's output using identical target inputs.
3. C qualifies the candidate provider inside an exact Core candidate that removes
   the old update controls/routes and adopts the clean initial-only
   `RepositoryReleaseWorkflowManagementV3` contract. Prove V2/update methods are
   absent from the supported provider/Core composition and forged legacy update
   operations fail request validation before credentials or remote I/O. Exercise
   the read-only adoption security checkpoint against the bounded
   `security/release-starter-advisories.json` index with matching, non-matching,
   missing, invalid, duplicate, oversized, unpublished-GHSA and unavailable
   advisory/provenance fixtures; none may grant write authority, parse advisory
   prose for identity or infer vulnerability merely from age. Record original
   certified-host checks separately from this new composition.
4. With explicit approval and real immutable versions, release the complete
   provider, adopt/qualify/release it with the connected Core changes, upgrade the
   named disposable sites, and publish/read back the complete pack via Profile B.
5. Against named plugin and theme fixture repositories, prove actual installed
   assessment -> preview -> confirmation -> initial draft PR -> identity/content
   readback. Test changed target/pack, missing permissions, conflicting automation,
   repeat confirmation and lost response; no false success or duplicate writes.
6. Verify PR execution stays read-only before authorizing fixture merge. Then
   prove main Quality -> RP proposal -> exact candidate Quality -> separately
   authorized release merge -> fresh main Quality -> immutable ZIP publication.
   Prove the actual protected release PR can satisfy its required checks at the
   exact head/event/check source, distinguishing branch protection from rulesets
   and unsupported merge queues; green dispatch alone is not that evidence.
   Install/read back the exact plugin/theme asset. Confirm maintenance is now
   target-owned and Booster never overwrites later customizations.
7. Include a repository whose settings do not inherit RAN organization defaults:
   create the setup PR with incomplete execution settings but valid write
   authority, then qualify execution after owner configuration. Missing execution
   prerequisites must be named, not assumed, queried by an admin probe or silently
   configured. Missing setup write authority still prevents the operation.
   Record actual target IDs/SHAs/assets/results without secrets. Unavailable access
   is an explicit acceptance gap.

The tests may use the two existing disposable sites, but their addresses and safe
operation boundaries have not been supplied by these examples. No new production
releases are required solely to exercise a hypothetical update service. G0 is frozen;
A/B/C do not gain merge/publication/site authority from these examples.
