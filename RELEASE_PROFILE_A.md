# RAN Profile A release contract

Profile A is the default release architecture for repositories that do not publish an authoritative separately built release asset.

The consumer repository owns the `workflow_run` trigger because GitHub reusable workflows cannot subscribe to another repository's events on behalf of the caller. The caller passes the triggering Quality identity to the organisation-owned reusable workflow.

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
    uses: RocketsAreNostalgic/.github/.github/workflows/release-profile-a.yml@<approved-immutable-ref>
    with:
      admitted-sha: ${{ github.event.workflow_run.head_sha }}
      upstream-event: ${{ github.event.workflow_run.event }}
      upstream-conclusion: ${{ github.event.workflow_run.conclusion }}
      upstream-branch: ${{ github.event.workflow_run.head_branch }}
      upstream-repository: ${{ github.event.workflow_run.head_repository.full_name }}
      upstream-repository-id: ${{ github.event.workflow_run.head_repository.id }}
      upstream-workflow-path: ${{ github.event.workflow_run.path }}
      expected-workflow-path: .github/workflows/quality.yml
    secrets: inherit
```

The caller must name the canonical Quality workflow in `workflows:` and pass the canonical workflow path explicitly. Consumers pin the reusable workflow to an approved immutable organisation ref.

## Contract

The reusable workflow admits only a successful same-repository `push` Quality run on `main`, with the expected workflow path and a canonical 40-character SHA. It checks out that exact SHA with persisted credentials disabled and verifies HEAD before Release Please receives write authority.

Release Please owns version calculation, prerelease progression, changelog generation, release-PR lifecycle, tags and GitHub Releases.

Profile A intentionally does not implement:

- SemVer or changelog policy;
- Release Please branch/title/label parsing;
- merge-parent or tree reconstruction;
- candidate markers;
- manual Release Please lifecycle reconciliation;
- historical release recovery;
- a generic Actions API workflow/run reread.

A consumer needing an authoritative separately built release asset is Profile B, not Profile A.
