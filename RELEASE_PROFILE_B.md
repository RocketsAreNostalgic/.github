# RAN Profile B release contract

Profile B extends Profile A for repositories that publish an authoritative separately built release asset.

The repository's Quality workflow owns product-specific construction and verification. The shared release workflow owns only authenticated admission, Release Please, bounded release-PR Quality dispatch, and promotion of the exact artifact already tested by the triggering successful main Quality run.

## Thin caller

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
    uses: RocketsAreNostalgic/.github/.github/workflows/release-profile-b.yml@<approved-immutable-ref>
    with:
      expected-workflow-path: .github/workflows/quality.yml
      release-pr-head: release-please--branches--main--components--<component>
      artifact-prefix: <repository-artifact-prefix>
```

Do not use `secrets: inherit`. The reusable workflow uses the caller's automatic `GITHUB_TOKEN`.

## Release Please prerequisite

The consumer's manifest configuration must set:

```json
{
  "draft": true,
  "force-tag-creation": true
}
```

and must not set `skip-github-release: true`.

Release Please remains authoritative for version calculation, changelog, release PRs, tag identity and GitHub Release creation. Profile B requires Release Please to create the release as a draft so the tested artifact can be attached before immutable publication. Forced tag creation gives the draft an exact Git ref immediately and avoids inventing a parallel tag lifecycle.

The shared workflow verifies this configuration from the admitted commit before invoking Release Please.

## Immutable-release platform prerequisite

Profile B assumes the owner-managed GitHub immutable-release policy is already enabled for the consumer repository. In RAN this is an organization-wide production constraint owned by #47/#57, not a repository workflow preference.

GitHub's immutable-release settings endpoint requires repository Administration-read. The automatic `GITHUB_TOKEN` cannot request that permission, and an empirical Profile B contract probe returned HTTP 403. The shared release workflow therefore does not introduce a higher-privilege standing token merely to re-authenticate an administrator-controlled platform setting.

The workflow still publishes only after all tested assets are attached and then requires the published API response to report `immutable == true`. If the owner-managed platform control is changed, that is an architecture/settings violation to be reconciled under #57 rather than a reason to add broader workflow credentials.

## Quality prerequisite

The canonical Quality workflow must support `workflow_dispatch` with no required inputs, just as Profile A does. Release Please uses the automatic `GITHUB_TOKEN`, so the shared workflow may need to dispatch Quality at the exact bot-owned release-PR head when ordinary pull-request events are suppressed.

Quality must remain read-only.

For every run that can become a production release, Quality uploads one run-bound Actions artifact named:

```text
<artifact-prefix>-<run-id>-<run-attempt>
```

That artifact contains the tested release assets plus `ran-profile-b-promotion.json` (or the caller-selected promotion-manifest filename).

## Promotion manifest

Schema version 1:

```json
{
  "schema": "ran-profile-b-promotion",
  "schema_version": 1,
  "repository": "RocketsAreNostalgic/example",
  "quality_commit": "<40-hex exact main Quality SHA>",
  "source_commit": "<same 40-hex SHA>",
  "tag": "v1.2.3",
  "assets": [
    {
      "name": "example-1.2.3.zip",
      "sha256": "<64-hex digest>"
    }
  ]
}
```

The asset set is bounded to 1–8 flat file names. Each listed file must exist in the downloaded run-bound artifact and match its declared SHA-256 digest.

Repository-local Quality may keep richer product metadata alongside this manifest. The shared promoter does not interpret package layout, Core certification, runtime dependency projection, WordPress compatibility, or install/runtime evidence.

## Promotion transaction

After exact successful-main admission:

1. Require the admitted SHA is still `main`.
2. Run Release Please normally.
3. Qualify an exact open Release Please candidate when one exists.
4. Resolve at most one GitHub Release whose `target_commitish` is the admitted SHA.
5. If Release Please reported a newly created release, require its output SHA and tag to identify that exact draft.
6. Download the exact triggering Quality artifact by workflow run ID and attempt.
7. Verify repository/SHA/tag binding and every declared asset digest.
8. Accept an already-present asset only when its GitHub-reported digest is exact. Missing draft assets are uploaded once. Conflicting or unexpected assets fail closed.
9. Publish the draft only when immutable releases are enabled.
10. Read back exact tag target, asset names/digests, non-draft state and `immutable == true`.

The workflow never uses `--clobber`.

## Retry behavior

The GitHub Release itself is the only promotion state.

- No release targeted at the admitted SHA: ordinary non-release main run; no promotion.
- Exact draft with no/missing expected assets: resume by uploading only missing exact assets.
- Exact draft with exact assets: publish.
- Conflicting or unexpected draft asset: fail closed.
- Exact immutable published release with exact assets: successful no-op.
- Published release missing/conflicting expected assets: fail closed.
- Missing or expired Quality artifact: fail closed; never rebuild substitute bytes.
- Wrong tag target or more than one release targeted at the admitted SHA: fail closed.

The promoter may rediscover a draft after a lost acknowledgement by its exact admitted target SHA. It does not reconstruct Release Please merge geometry, parse Release Please lifecycle labels, maintain candidate markers, or recompute SemVer.

## Repository-local responsibilities

Remain local:

- deterministic artifact construction;
- archive layout/allowlist rules;
- product-specific metadata;
- installation/runtime/Core/dependency evidence;
- any downstream product deployment adapter.

Shared Profile B does not weaken these checks. It changes only who owns generic release orchestration.
