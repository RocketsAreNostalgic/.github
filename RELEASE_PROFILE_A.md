# RAN Profile A release contract

Profile A is the default release architecture for repositories that do not publish an authoritative separately built release asset.

The consumer owns the `workflow_run` trigger. GitHub preserves the caller event context in the called workflow, so admission reads `github.event.workflow_run` directly rather than trusting forwarded identity strings.

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
    uses: RocketsAreNostalgic/.github/.github/workflows/release-profile-a.yml@<approved-immutable-ref>
    with:
      expected-workflow-path: .github/workflows/quality.yml
      release-pr-head: release-please--branches--main--components--<component>
```

Do not use `secrets: inherit`. The reusable workflow uses the caller's automatic `GITHUB_TOKEN`. GitHub does not permit a called workflow to elevate token permissions, so the caller job explicitly grants only the scopes required by Release Please.

The caller names the canonical Quality workflow in `workflows:`, supplies its canonical path, and supplies the canonical Release Please branch name from its configuration. Consumers pin the reusable workflow to an approved immutable organisation ref.

Release Please uses the automatic `GITHUB_TOKEN`, so GitHub suppresses ordinary workflow events caused by its release-PR mutation. Profile A therefore includes one bounded qualification step: after Release Please runs, it finds exactly one bot-owned open candidate at the configured branch, binds its exact head SHA, and dispatches the repository's existing read-only Quality workflow only when no successful or in-flight pull-request/workflow-dispatch run already covers that exact head. This is merge qualification, not release/version state.

## Contract

The read-only admission job requires the actual caller event to be `workflow_run`, then reads the actual event payload and admits only a successful same-repository `push` Quality run on `main` with the expected path and canonical SHA. It checks out that exact SHA without persisted credentials and verifies HEAD.

Only after admission does a separate write-capable job run. Immediately before Release Please it requires current `main` still to equal the admitted SHA, and Release Please is explicitly targeted at `main`. Workflow concurrency serializes Profile A release runs.

Release Please owns version calculation, prerelease progression, changelog generation, release-PR lifecycle, tags and GitHub Releases.

The main-tip check is a fail-closed stale-run guard, not an atomic compare-and-swap with a concurrent push. The architecture deliberately requires the admitted Quality revision still to be current main when Release Please begins; a newer main revision receives its own Quality/release lifecycle.

Profile A intentionally does not implement SemVer/changelog policy, Release Please branch/title/label parsing, merge-parent/tree reconstruction, candidate markers, manual lifecycle reconciliation, historical recovery, or generic Actions API run rereads.

The candidate Quality dispatch is part of the shared Profile A contract because `GITHUB_TOKEN` event suppression is common to Release Please consumers with required PR checks. Repository Quality remains repository-owned and read-only; the shared workflow does not interpret its result beyond avoiding duplicate dispatch.
