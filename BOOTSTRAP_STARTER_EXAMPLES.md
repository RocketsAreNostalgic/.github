# Initial release starter: concrete G0 examples

**PROPOSED documentation, not deployed templates or execution evidence.** Read
[the contract](BOOTSTRAP_STARTER_CONTRACT.md) with this file. G0 reviews the
rendered workflow/configuration and the two local adapter interfaces before
implementation; producer B must still implement/test the adapters and materialize
the actual template ZIP. These examples are not a claim that an executable
producer/consumer pair already exists.

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
RELEASE-STARTER.md                      origin and maintainer/security handoff
```

The initial diff also shows only the bounded header/optional readme version
annotations and ordinary `.prettierignore` append when needed. Nothing writes
target main, creates repository secrets or silently changes Actions settings.
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

      - uses: actions/setup-node@48b55a011bda9f5d6aeb4c2d9c7362e8dae4041e
        with:
          node-version: '24.11.0'

      - uses: shivammathur/setup-php@f3e473d116dcccaddc5834248c87452386958240
        with:
          php-version: '8.2'
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
          test "$(git show "${SOURCE_SHA}:.release-please-manifest.json" | jq -er '."."')" = "$version"
          work="$(mktemp -d)"
          trap 'rm -rf "$work"' EXIT
          bash scripts/build-release.sh "$SOURCE_SHA" "$version" "$work/one"
          bash scripts/build-release.sh "$SOURCE_SHA" "$version" "$work/two"
          archive="acorn-plugin-${version}.zip"
          cmp "$work/one/$archive" "$work/two/$archive"
          bash scripts/verify-release.sh "$work/one/$archive" "$version" "$SOURCE_SHA"
          # Extraction follows independent member/type/resource verification.
          unzip -q "$work/one/$archive" -d "$work/payload"
          find "$work/payload" -type f -name '*.php' -print0 | xargs -0 -r -n1 php -l
          mkdir -p .ran-booster-release-dist
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

      - uses: actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a
        with:
          name: ran-starter-${{ github.run_id }}-${{ github.run_attempt }}
          path: |
            .ran-booster-release-dist/acorn-plugin-*.zip
            .ran-booster-release-dist/ran-profile-b-promotion.json
          if-no-files-found: error
          retention-days: 30
```

The implementation must use a clean destination and assert exactly one expected
ZIP rather than allow a pre-existing/untracked output to join the artifact glob.
The producer's generated-output tests must include that negative case. A retained
build adapter can already call its verifier; the explicit Quality verification
above documents the required independent check, not a demand for a second
verification framework.

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
    uses: RocketsAreNostalgic/.github/.github/workflows/release-profile-b.yml@8fefa7da961d5fcb36d706a78578ddb5f39ffa4a
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
silently rewritten. A normal `.prettierignore` may receive `/CHANGELOG.md`; the
starter neither creates a formatter dependency nor weakens unrelated checks.
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

The consumer writes `RELEASE-STARTER.md` with the following short structure.
Values in brackets below are replaced from the verified initial pack/target;
they are prose placeholders, not additional template-pack capabilities.

```text
Release starter

Created once by Booster from:
- pack version/profile: [actual pack version] / [actual /3 profile]
- pack source commit and ZIP SHA-256: [actual values]
- shared publisher: RocketsAreNostalgic/.github, [actual pinned commit]
- setup PR: see this file's introducing commit and pull request

You own these files after setup. Booster does not update or repair them.

Before merging:
- review every proposed file and the runtime allowlist;
- confirm main, Actions/reusable-workflow access, required token permissions,
  PR creation, immutable releases and your protected-merge checks;
- check the PR's read-only Quality result and the subsequent main run.

For a release:
- use Conventional Commits and review Release Please's version/changelog PR;
- merge using your repository's approved method;
- require fresh main Quality and immutable release/ZIP readback;
- consumers install the attached ZIP, not GitHub's generated source archive.

Keep the allowlist current when adding runtime files. Add product-specific
checks deliberately; complex builds need a maintainer-owned release setup.
Never overwrite a published release or move its tag to repair a failure.

Security and maintenance:
- use the template pack repository SECURITY.md / private reporting route;
- follow its Security Advisories and linked release announcements;
- watch the pack and shared workflow repositories' release announcements;
- review affected revisions and apply manual fixes, including workflow repins.
Origin records do not prove customized code is currently affected or fixed.
There is no automatic advisory scan, notification guarantee or repair service.
```

The actual output must contain concrete official reporting/announcement links,
not these shorthand descriptions. B updates its outdated managed-update security
policy accordingly; the coordinator verifies the reporting/subscription route
before public feature acceptance. This process applies in production regardless
of user count. No per-site tracking, telemetry, advisory database or new
repository-origin parser is introduced.

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
   the old update controls/routes. Prove the mandatory V2 update slots reject
   without I/O, rather than silently retaining update behavior. Record original
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
   Install/read back the exact plugin/theme asset. Confirm maintenance is now
   target-owned and Booster never overwrites later customizations.
7. Include a repository whose settings do not inherit RAN organization defaults:
   missing prerequisites must be named, not assumed or silently configured.
   Record actual target IDs/SHAs/assets/results without secrets. Unavailable access
   is an explicit acceptance gap.

The tests may use the two existing disposable sites, but their addresses and safe
operation boundaries have not been supplied by this proposal. No new production
releases are required solely to exercise a hypothetical update service. G0 remains
under review until #81 records acceptance; A/B/C do not gain merge/publication/site
authority from these examples.
