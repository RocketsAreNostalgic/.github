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

Because GitHub's workflow-dispatch API accepts a branch or tag ref rather than an immutable commit SHA, the shared workflow binds the Release Please branch to the exact candidate SHA immediately before dispatch and then waits for a successful Quality run whose reported `head_sha` is that exact SHA. A successful run for a newer branch head does not qualify the originally admitted candidate. The candidate branch must still resolve to the bound SHA when qualification succeeds. The wait is bounded to approximately 25 minutes inside a 30-minute release job so a legitimate full Quality run can complete without turning qualification into an unbounded observer.

GitHub may record the automatic bot-created `pull_request` Quality run as completed with `conclusion: action_required` and no jobs. Profile B treats that specific record as non-execution rather than failed qualification, then uses the exact-head `workflow_dispatch` fallback. An actually executed exact candidate run that completes unsuccessfully still fails closed.

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
9. Revalidate the captured release ID, tag, admitted target SHA, original prerelease boolean and expected draft/published state on the post-upload response before publication. Metadata changes fail closed before the publication PATCH. Publish the draft, then require immutable readback. The workflow does not query the administrative setting; a misconfigured repository can publish a mutable release and then fail.
10. Read back exact tag target, asset names/digests, non-draft state and `immutable == true`.

The original boolean `prerelease` classification is captured during publication resolution and retained through initial promotion validation, pre-publication validation and final readback. Changes in either direction fail closed; stable `false` is valid.

The resolved Release Please release ID is carried through promotion and readback, with its tag and admitted target SHA checked again. Draft releases are read through `/releases/{release_id}` because `/releases/tags/{tag}` can return HTTP 404 before publication. This uses the existing release identity; it does not create a replacement release.

Asset uploads use the captured release ID's endpoint on `uploads.github.com`, sending the exact verified file as the raw request body. Publishing also targets that same ID. No mutation re-resolves the tag to select a release; deletion/recreation under the same tag therefore fails closed against the original ID.

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

## Troubleshooting

Proposal delivery and execution prerequisites are separate. The initial starter PR can be proposed before owner-managed immutability, Actions, runner and bot-PR settings are ready. Complete these prerequisites before merging or activating workflows, and review what can run on both the setup PR and its merge. Booster does not verify administrative settings. Strict immutable publication remains required; there is no permissive mode.

The executing publisher reports its failing stage, bounded repository/SHA/release identity and original Quality run/attempt. It does not print API bodies, diagnose an administrative setting from a generic 403, or claim that failure means no remote mutation occurred. Release Please can already have created or changed a branch, PR, tag or draft before a later failure.

| Observed stage/condition | Maintainer action and retry boundary |
| --- | --- |
| No workflow run, Actions disabled, policy or invalid YAML rejection | Read the Actions UI and workflow validation messages; verify owner-managed Actions policies and workflow configuration. No job exists to emit custom diagnostics. Review source fixes normally. |
| Job queued, runner unavailable, account/billing constraint | Inspect runner availability and account limits in GitHub. Job diagnostics cannot run before allocation. Preserve the original event/revision when retrying. |
| Current-main admission fails | Inspect whether the admitted SHA is stale or the API read failed. A stale successful Quality run is normal non-publication; use the current main push Quality run. Manual or PR Quality does not admit publication. |
| Release Please fails or bot PR creation is refused | Inspect the action error, bot PR policy, job permissions and branch/tag rules. A 403 alone does not identify which setting is wrong. Inspect existing remote state before any rerun. |
| Exact candidate Quality fails/times out, or required checks block merge | Inspect the exact PR head, event and required-check source. A green dispatched run alone is insufficient proof for protected merge. Distinguish branch protection, rulesets and unsupported merge queues; do not disable checks or broaden tokens. |
| Quality build or artifact verification fails | Fix product construction in read-only Quality. Do not run target-owned troubleshooting scripts in the privileged publisher. |
| Artifact download fails or artifact expires | Check the triggering run ID and attempt. Never rebuild substitute bytes or substitute another attempt's artifact. A new main push Quality run must establish new custody where needed. |
| Draft upload/verification fails | Inspect the identified draft, exact tag/target, names and digests. Only the same admitted revision, original run/attempt artifact and still-current main may resume missing exact draft assets; conflicts fail closed. Never replace assets or move tags. |
| Publication acknowledgement/readback unavailable or identity changed | Outcome is unknown. Inspect the exact release ID and remote state before retrying: publication or uploads may already have happened. No rollback is implied. |
| Published mutable release confirmed | Publication happened; the job is red because strict immutable qualification failed. Do not blindly rerun or assume rollback. Use the next-version path below. |
| Exact immutable published release with exact assets | Retry can be a no-op only within the original admission/custody constraints. |

An open release PR or no releasable change is normal non-publication. Release Please remains the classification authority; this workflow does not reproduce its version or label decision engine. Successful candidate Quality is also separate from protected merge qualification.

### Published mutable release: next-version path

Enabling the owner-managed setting affects future publication; it does not make an already published mutable release immutable. Keep the failed job's evidence and inspect the actual Release Please PR, manifest/version, tag, release and lifecycle state. A failed publisher does not imply Release Please did not advance that state. A maintainer must establish a legitimate next release through the normal reviewed Release Please process, confirm the new version and exact main revision, and obtain a fresh qualifying main push Quality artifact before publication. Verify the new release's actual immutable readback. Do not automatically edit lifecycle labels, replace assets, move tags, delete releases or replay the old version. If Release Please state is inconsistent, stop for maintainer investigation rather than inventing a repair.

Rerunning a release job does not change its original event/SHA or its upstream Quality run/attempt. The admitted revision must still be current main and the original artifact must still be available. Dispatching Quality manually is not publisher admission. These limits also apply after fixing permission or owner-managed execution settings.
