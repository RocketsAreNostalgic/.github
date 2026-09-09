# RAN reusable quality workflows

The workflows under `.github/workflows/` provide the common CI execution layer for repositories that have adopted the RAN quality command contract.

They deliberately invoke fixed aggregate commands rather than accepting arbitrary command inputs:

- `quality-node.yml` runs `pnpm check`.
- `quality-php-library.yml` runs `composer check`.
- `quality-wordpress-plugin.yml` runs both `composer check` and `pnpm check`.

Project-specific focused checks that are not part of the ordinary aggregate contract remain in the caller repository's workflow or `AGENTS.md` contract.

## Caller examples

Consumers must pin these workflows to an immutable full commit SHA. A human-readable release name may be kept in a comment for provenance, but a mutable branch or tag is not the execution reference.

A Node repository may call:

```yaml
jobs:
  baseline:
    uses: RocketsAreNostalgic/.github/.github/workflows/quality-node.yml@<immutable-full-commit-sha> # quality-v1
    with:
      pnpm-version: '11.13.1'
```

A PHP library may call:

```yaml
jobs:
  baseline:
    uses: RocketsAreNostalgic/.github/.github/workflows/quality-php-library.yml@<immutable-full-commit-sha> # quality-v1
    with:
      php-version: '8.4'
```

A mixed WordPress plugin may call:

```yaml
jobs:
  baseline:
    uses: RocketsAreNostalgic/.github/.github/workflows/quality-wordpress-plugin.yml@<immutable-full-commit-sha> # quality-v1
    with:
      php-version: '8.4'
      pnpm-version: '11.13.1'
```

A release tag such as `quality-v1` may identify a reviewed standards release for upgrade discovery, but consumers execute the exact commit SHA associated with the reviewed revision. A standards upgrade therefore appears as an explicit caller change.

## Stable check contract

GitHub renders called reusable-workflow jobs using a composite caller/called job name. RAN therefore does **not** use that nested context as the organisation merge-protection contract.

Each consumer should expose a local terminal aggregation job named `quality`. That job must depend on every baseline and project-specific job required for the repository's ordinary merge gate and must fail unless all of those dependencies succeeded.

Example:

```yaml
jobs:
  baseline:
    uses: RocketsAreNostalgic/.github/.github/workflows/quality-wordpress-plugin.yml@<immutable-full-commit-sha> # quality-v1
    with:
      php-version: '8.4'
      pnpm-version: '11.13.1'

  project:
    runs-on: ubuntu-latest
    steps:
      - run: ./scripts/project-specific-checks.sh

  quality:
    name: quality
    if: ${{ always() }}
    needs:
      - baseline
      - project
    runs-on: ubuntu-latest
    steps:
      - name: Require all quality lanes
        env:
          BASELINE_RESULT: ${{ needs.baseline.result }}
          PROJECT_RESULT: ${{ needs.project.result }}
        run: |
          test "$BASELINE_RESULT" = success
          test "$PROJECT_RESULT" = success
```

This gives organisation rulesets one stable local `quality` context while allowing a repository to add focused integration, archive, generated-artifact, compatibility, or release checks without changing the required-status name.

Do not create an organisation required-status rule until representative consumers have emitted and passed this exact terminal `quality` context.

## Inputs

Inputs are limited to project/toolchain identity such as PHP, Node/pnpm version and working directory. They do not allow callers to substitute the quality command or disable parts of a selected profile.

Choose the workflow matching the actual repository profile instead of weakening a broader workflow through skip flags.

## Supply-chain policy

Third-party actions inside the shared workflows are pinned to immutable full commit SHAs. Version comments record the reviewed release for maintainability. Updates to those pins are reviewed in this repository before consumers adopt the new RAN workflow commit.
