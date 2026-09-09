# RAN reusable quality workflows

The workflows under `.github/workflows/` provide the common CI source-quality layer for repositories that have adopted the RAN quality command contract.

They deliberately invoke fixed aggregate commands rather than accepting arbitrary command inputs:

- `quality-node.yml` runs `pnpm check` and emits `RAN Node Quality`.
- `quality-php-library.yml` runs `composer check` and emits `RAN PHP Library Quality`.
- `quality-wordpress-plugin.yml` runs both canonical contracts and emits `RAN WordPress Plugin Quality`.

The current shared Node lane is intentionally pnpm-specific because that matches the maintained RAN Node estate. A non-pnpm repository should use an equivalent local or future manager-specific shared lane rather than add pnpm solely to consume this workflow.

## Shared baseline guarantees

The reusable workflows own broadly transferable guarantees that should not be reimplemented differently in every repository:

- third-party Actions are pinned to immutable full commit SHAs;
- workflow permissions are read-only unless a future profile proves a stronger permission is necessary;
- `pull_request_target` callers are rejected before checkout or project-controlled execution;
- ordinary `pull_request` runs explicitly check out `github.event.pull_request.head.sha`; non-PR calls use `github.sha`;
- the checked-out commit is verified before project-controlled commands run, so source-quality evidence binds to the exact reviewed revision rather than GitHub's synthetic PR merge commit;
- checkout does not persist Git credentials while project-controlled commands run;
- required lockfiles must exist before dependency installation;
- pnpm consumers must execute the exact version declared in `packageManager`;
- Composer profiles run `composer validate --strict --no-check-publish --no-check-all` before installation;
- Composer installs use the reviewed lockfile and do not resolve an untracked dependency graph;
- PHP profiles run the repository's `composer check` contract and then an independent syntax sweep whose failure propagates out of the workflow;
- pnpm profiles run frozen installation followed by the repository's `pnpm check` contract.

These guarantees intentionally mirror the broadly transferable source-quality posture of `ran-booster`, the RAN high-water reference implementation.

Testing the exact PR head and testing mergeability are separate contracts. The shared source-quality lane proves the reviewed head; repository rulesets/strict integration policy or a merge queue must ensure the head is current with the target branch before merge. A repository may add an explicit merge-integration lane when its product needs stronger base-integration evidence.

Project-specific focused checks remain in the caller repository. Examples include archive/package integrity, WordPress install/activation and compatibility matrices, Plugin Check, provider/runtime contracts, deployment/release proofs, or other evidence whose exact shape belongs to the product rather than the organisation source baseline.

## Caller examples

Consumers must pin these reusable workflows to an immutable full commit SHA. A human-readable release name may be kept in a comment for provenance, but a mutable branch or tag is not the execution reference.

Use the caller job id `baseline` so the profile-specific shared context remains predictable for humans and diagnostics.

A pnpm Node repository may call:

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

## Consumer aggregation versus merge enforcement

Consumer-owned status names are **evidence, not an unforgeable workflow identity**. A pull request that can edit its caller workflow can manufacture a successful job with the same displayed status name. Therefore neither `baseline / RAN WordPress Plugin Quality` nor a local terminal `quality` status is sufficient by itself to prove that an organisation-owned workflow executed.

A migrated repository should still expose a local terminal aggregation job named `quality` because it gives maintainers one clear result for all ordinary shared and project-specific lanes:

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

The security/enforcement boundary is an organization or enterprise ruleset using GitHub's **Require workflows to pass before merging** rule. That required workflow must be selected from an organisation-controlled repository/branch/workflow configuration so a target-repository pull request cannot replace it with a look-alike job. Where the required workflow delegates to these reusable profiles, that delegation should use an immutable reviewed provider SHA.

The final enforcement phase should therefore:

1. keep the consumer `baseline` and terminal `quality` jobs for local feedback and diagnosis;
2. configure the appropriate organisation ruleset-required workflow for the repository profile;
3. ensure that required workflow executes the same reviewed RAN baseline against the intended source revision; and
4. use repository-level required-workflow enforcement as needed for product-specific gates that must not be bypassable by editing a caller workflow.

Do not create organization required-status rules that treat a consumer-controlled job name as proof of organisation workflow identity.

## Inputs

Inputs are limited to project/toolchain identity such as PHP version, exact pnpm version, Node-version file, and working directory. They do not allow callers to substitute the quality command, source revision, or disable parts of a selected profile.

A caller-supplied pnpm version is not an override: the shared workflow compares it with `packageManager` and fails on disagreement.

Choose the workflow matching the actual repository profile instead of weakening a broader workflow through skip flags.

## Booster parity boundary

`ran-booster` is the high-water reference, not a template to copy mechanically.

The shared workflows should absorb Booster gates that are technology-wide and deterministic. Booster-specific release lifecycle, exact artifact admission/reuse, updater source verification, WordPress/database matrix topology, and runtime/product contracts remain in Booster's local workflow.

When a transferable Booster guarantee is stronger than this shared layer, treat that as a baseline-review trigger rather than assuming the lower organisation guarantee is permanently sufficient.
