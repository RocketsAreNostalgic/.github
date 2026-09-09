# RAN reusable quality workflows

The workflows under `.github/workflows/` provide the common CI execution layer for repositories that have adopted the RAN quality command contract.

They deliberately invoke fixed aggregate commands rather than accepting arbitrary command inputs:

- `quality-node.yml` runs `pnpm check` and emits `RAN Node Quality`.
- `quality-php-library.yml` runs `composer check` and emits `RAN PHP Library Quality`.
- `quality-wordpress-plugin.yml` runs both canonical contracts and emits `RAN WordPress Plugin Quality`.

Project-specific focused checks that are not part of the ordinary aggregate contract remain in the caller repository's workflow or `AGENTS.md` contract.

## Caller examples

Consumers must pin these workflows to an immutable full commit SHA. A human-readable release name may be kept in a comment for provenance, but a mutable branch or tag is not the execution reference.

Use the caller job id `baseline` so the profile-specific shared context is predictable.

A Node repository may call:

```yaml
jobs:
  baseline:
    uses: RocketsAreNostalgic/.github/.github/workflows/quality-node.yml@<immutable-full-commit-sha> # quality-v1
    with:
      pnpm-version: '11.13.1'
```

Expected shared context: `baseline / RAN Node Quality`.

A PHP library may call:

```yaml
jobs:
  baseline:
    uses: RocketsAreNostalgic/.github/.github/workflows/quality-php-library.yml@<immutable-full-commit-sha> # quality-v1
    with:
      php-version: '8.4'
```

Expected shared context: `baseline / RAN PHP Library Quality`.

A mixed WordPress plugin may call:

```yaml
jobs:
  baseline:
    uses: RocketsAreNostalgic/.github/.github/workflows/quality-wordpress-plugin.yml@<immutable-full-commit-sha> # quality-v1
    with:
      php-version: '8.4'
      pnpm-version: '11.13.1'
```

Expected shared context: `baseline / RAN WordPress Plugin Quality`.

A release tag such as `quality-v1` may identify a reviewed standards release for upgrade discovery, but consumers execute the exact commit SHA associated with the reviewed revision. A standards upgrade therefore appears as an explicit caller change.

## Stable merge-gate contract

RAN uses **two complementary check identities** for migrated repositories:

1. the profile-specific shared context proves that the repository called the correct organisation baseline; and
2. a terminal local `quality` job proves that all baseline and project-specific merge-required lanes succeeded.

A profile ruleset should therefore require the correct shared context for that profile **and** the terminal local `quality` context. This prevents a WordPress repository from silently replacing the WordPress shared workflow with the Node workflow while preserving a generic success check.

Each consumer must expose a local terminal aggregation job named `quality`. That job must depend on every baseline and project-specific job required for the repository's ordinary merge gate and must fail unless all of those dependencies succeeded.

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
          printf 'baseline=%s\nproject=%s\n' "$BASELINE_RESULT" "$PROJECT_RESULT"
          if [ "$BASELINE_RESULT" != success ] || [ "$PROJECT_RESULT" != success ]; then
            exit 1
          fi
```

Do not create organisation required-status rules until representative consumers have emitted and passed both the exact profile-specific context and terminal `quality` context.

## Inputs

Inputs are limited to project/toolchain identity such as PHP, Node/pnpm version and working directory. They do not allow callers to substitute the quality command or disable parts of a selected profile.

Choose the workflow matching the actual repository profile instead of weakening a broader workflow through skip flags.

## Locked dependency graphs

The shared workflows fail explicitly before installation when their required lockfile is absent. `composer install` is never allowed to fall back to resolving from `composer.json`, and pnpm workflows require `pnpm-lock.yaml` before running the frozen install.

## Supply-chain policy

Third-party actions inside the shared workflows are pinned to immutable full commit SHAs. Version comments record the reviewed release for maintainability. Updates to those pins are reviewed in this repository before consumers adopt the new RAN workflow commit.
