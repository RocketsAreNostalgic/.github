# RAN reusable quality workflows

The workflows under `.github/workflows/` provide the common CI execution layer for repositories that have adopted the RAN quality command contract.

They deliberately invoke fixed aggregate commands rather than accepting arbitrary command inputs:

- `quality-node.yml` runs `pnpm check`.
- `quality-php-library.yml` runs `composer check`.
- `quality-wordpress-plugin.yml` runs both `composer check` and `pnpm check`.

Project-specific focused checks that are not part of the ordinary aggregate contract remain in the caller repository's workflow or `AGENTS.md` contract.

## Caller examples

A Node repository may call:

```yaml
jobs:
  quality:
    uses: RocketsAreNostalgic/.github/.github/workflows/quality-node.yml@quality-v1
    with:
      pnpm-version: '11.13.1'
```

A PHP library may call:

```yaml
jobs:
  quality:
    uses: RocketsAreNostalgic/.github/.github/workflows/quality-php-library.yml@quality-v1
    with:
      php-version: '8.4'
```

A mixed WordPress plugin may call:

```yaml
jobs:
  quality:
    uses: RocketsAreNostalgic/.github/.github/workflows/quality-wordpress-plugin.yml@quality-v1
    with:
      php-version: '8.4'
      pnpm-version: '11.13.1'
```

`quality-v1` is the intended major-version reference after the workflow baseline is accepted and tagged. Consumers must not be pointed permanently at `main`.

## Stable check contract

GitHub renders a called reusable-workflow job using both the caller job and called job names. Callers should use `quality` as the calling job name; these reusable workflows also expose a called job named `quality`. The resulting reusable-workflow status is therefore expected to remain stable for organisation ruleset purposes once the first consumer migrations confirm GitHub's exact rendered context.

Do not create an organisation required-status rule until representative consumers have emitted and passed the exact intended status.

## Inputs

Inputs are limited to project/toolchain identity such as PHP, Node/pnpm version and working directory. They do not allow callers to substitute the quality command or disable parts of a selected profile.

Choose the workflow matching the actual repository profile instead of weakening a broader workflow through skip flags.
