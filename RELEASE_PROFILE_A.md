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
    uses: RocketsAreNostalgic/.github/.github/workflows/release-profile-a.yml@<approved-immutable-ref>
    with:
      expected-workflow-path: .github/workflows/quality.yml
```

Do not use `secrets: inherit`. The reusable workflow uses the caller's automatic `GITHUB_TOKEN`. GitHub does not permit a called workflow to elevate token permissions, so the caller job explicitly grants only the scopes required by Release Please.

The caller names the canonical Quality workflow in `workflows:` and supplies its canonical path. Consumers pin the reusable workflow to an approved immutable organisation ref.

## Contract

The read-only admission job requires the actual caller event to be `workflow_run`, then reads the actual event payload and admits only a successful same-repository `push` Quality run on `main` with the expected path and canonical SHA. It checks out that exact SHA without persisted credentials and verifies HEAD.

Only after admission does a separate write-capable job run. Immediately before Release Please it requires current `main` still to equal the admitted SHA, and Release Please is explicitly targeted at `main`. Workflow concurrency serializes Profile A release runs.

Release Please owns version calculation, prerelease progression, changelog generation, release-PR lifecycle, tags and GitHub Releases.

The main-tip check is a fail-closed stale-run guard, not an atomic compare-and-swap with a concurrent push. The architecture deliberately requires the admitted Quality revision still to be current main when Release Please begins; a newer main revision receives its own Quality/release lifecycle.

Profile A intentionally does not implement SemVer/changelog policy, Release Please branch/title/label parsing, merge-parent/tree reconstruction, candidate markers, manual lifecycle reconciliation, historical recovery, or generic Actions API run rereads.

Repositories whose Release Please-created PR cannot obtain required read-only Quality through normal event behavior must add the smallest exact-head Quality dispatch needed by their merge policy; that is candidate qualification, not release publication semantics, and should be evaluated during consumer migration.
