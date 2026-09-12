# RAN reusable quality workflows

The workflows under `.github/workflows/` provide the common CI source-quality layer for repositories that have adopted the RAN quality command contract.

They deliberately invoke fixed aggregate commands rather than accepting arbitrary command inputs:

- `quality-node.yml` runs `pnpm check` and emits `RAN Node Quality`.
- `quality-php-library.yml` runs `composer check` and emits `RAN PHP Library Quality`.
- `quality-php-library-v2.yml` runs the repository's Composer quality contract on both its PHP floor and current-stable PHP, with strict Composer validation and independent PHP syntax verification on both lanes.
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
- PHP v2 consumers that request Node must provide a full `major.minor.patch` Node version and the installed binary is verified against it;
- Composer profiles run `composer validate --strict --no-check-publish --no-check-all` before installation;
- Composer installs use the reviewed lockfile and do not resolve an untracked dependency graph;
- PHP profiles run the repository's `composer check` contract and then an independent syntax sweep whose failure propagates out of the workflow;
- pnpm profiles run frozen installation followed by the repository's `pnpm check` contract;
- reusable providers own their runner selection; a caller cannot redirect pull-request code to a self-hosted or otherwise privileged runner.

These guarantees intentionally mirror the broadly transferable source-quality posture of `ran-booster`, the RAN high-water reference implementation.

Testing the exact PR head and testing mergeability are separate contracts. The shared source-quality lane proves the reviewed head; repository rulesets/strict integration policy or a merge queue must ensure the head is current with the target branch before merge. A repository may add an explicit merge-integration lane when its product needs stronger base-integration evidence.

Project-specific focused checks remain in the caller repository. Examples include archive/package integrity, WordPress install/activation and compatibility matrices, Plugin Check, provider/runtime contracts, deployment/release proofs, or other evidence whose exact shape belongs to the product rather than the organisation source baseline.

## Trust boundary: consumer quality contracts

These reusable profiles deliberately execute the consuming repository's canonical aggregate commands. That makes them useful for consistent verification, but it also means the aggregate scripts and the configuration they transitively consume are part of the pull-request source revision.

A ruleset-required organisation workflow prevents a target-repository pull request from replacing the organisation-owned workflow itself, but **workflow identity alone does not make a PR-controlled quality contract immutable**. For example, a pull request could otherwise replace `composer check` or `pnpm check` with a no-op, weaken a lint/static-analysis configuration, or change a helper script invoked by the aggregate while leaving the organisation-owned wrapper untouched.

Therefore these reusable profiles must not be treated as a standalone, unforgeable organisation merge-security boundary. Before RAN enables organisation ruleset enforcement for a profile, one of the following must also be true:

1. **Organisation-owned execution (preferred end state).** The ruleset-required workflow owns the authoritative commands/configuration (including versioned shared RAN standards) independently of PR-editable aggregate definitions. Consumer `composer check` / package-manager `check` commands remain the local developer interface and may run additionally, but they are not the sole authority for the required organisation gate.
2. **Protected consumer contract (transitional path).** Changes to the complete transitive quality contract require independent maintainer/code-owner approval that the PR author cannot self-satisfy. Stale approvals must be dismissed, or approval of the most recent reviewable push must be required, so a later commit cannot weaken the contract after approval.

The protected consumer contract includes, as applicable:

- `composer.json` script definitions and quality-tool dependencies;
- `package.json` aggregate scripts and quality-tool dependencies;
- lockfiles where changing the resolved quality-tool graph could alter the gate;
- PHPCS/WPCS, PHPCompatibility, PHPStan, ESLint, Prettier, Stylelint and test-runner configuration;
- project scripts/configuration transitively invoked by `composer check` or the package-manager `check` command;
- caller/local quality workflow files that decide which project-specific checks feed terminal `quality`.

The exact file set is repository-specific because aggregate scripts may delegate to additional tracked files. A repository must document/protect that transitive set rather than assuming the two manifest files are sufficient.

Until organisation-owned execution or protected-contract review is actually configured, these workflows provide strong deterministic verification evidence but **must not be advertised or configured as the sole organisation enforcement control**.

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

A quality-v1 PHP library may call:

```yaml
jobs:
  baseline:
    uses: RocketsAreNostalgic/.github/.github/workflows/quality-php-library.yml@<immutable-full-commit-sha> # quality-v1
    with:
      php-version: '8.4'
```

Expected shared context: `baseline / RAN PHP Library Quality`.

An updater-family PHP library using quality v2 may call:

```yaml
jobs:
  baseline:
    uses: RocketsAreNostalgic/.github/.github/workflows/quality-php-library-v2.yml@<immutable-full-commit-sha> # quality-v2
    with:
      php-floor: '8.2'
      php-current: '8.5'
      php-extensions: zip
      node-version: '24.11.0'
```

Expected shared contexts: `baseline / PHP 8.2 floor` and `baseline / PHP 8.5 compatibility`.

The v2 PHP provider deliberately does not expose a runner input. Pull requests in caller repositories can edit their caller workflow, so runner selection must remain organisation-owned rather than allowing a PR to redirect project-controlled commands to a self-hosted or otherwise privileged runner. When `node-version` is non-empty, v2 also requires a full `major.minor.patch` value and verifies `node --version` before project-controlled commands run.

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

A release tag such as `quality-v1` or `quality-v2` may identify a reviewed standards release for upgrade discovery, but consumers execute the exact commit SHA associated with the reviewed revision. A standards upgrade therefore appears as an explicit caller change.

## Consumer aggregation versus merge enforcement

Consumer-owned status names are **evidence, not an unforgeable workflow identity**. A pull request that can edit its caller workflow can manufacture a successful job with the same displayed status name. Therefore neither a shared baseline context nor a local terminal `quality` status is sufficient by itself to prove that an organisation-owned workflow executed.

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

The eventual security/enforcement boundary is an organization or enterprise ruleset using GitHub's **Require workflows to pass before merging** rule **plus the quality-contract integrity requirement above**. The required workflow must be selected from an organisation-controlled repository/branch/workflow configuration so a target-repository pull request cannot replace it with a look-alike job. Where a required workflow delegates to these reusable profiles, that delegation should use an immutable reviewed provider SHA.

The final enforcement phase should therefore:

1. keep the consumer `baseline` and terminal `quality` jobs for local feedback and diagnosis;
2. configure the appropriate organisation ruleset-required workflow for the repository profile;
3. ensure that required workflow executes the same reviewed RAN baseline against the intended source revision;
4. establish either organisation-owned authoritative execution/configuration or independent protected approval for the complete transitive consumer quality contract; and
5. use repository-level required-workflow enforcement as needed for product-specific gates that must not be bypassable by editing a caller workflow.

Do not create organization required-status rules that treat a consumer-controlled job name as proof of organisation workflow identity. Do not enable an organisation ruleset-required quality workflow while its authoritative checks can still be weakened solely by an unreviewed PR edit to consumer manifests/configuration.

## Inputs

Inputs are limited to project/toolchain identity such as PHP versions, PHP extensions, exact Node or pnpm version, Node-version file, and working directory. They do not allow callers to substitute the quality command, source revision, runner, or disable parts of a selected profile.

A caller-supplied pnpm version is not an override: the shared workflow compares it with `packageManager` and fails on disagreement. The v2 PHP workflow likewise verifies any non-empty Node version exactly after setup.

Choose the workflow matching the actual repository profile instead of weakening a broader workflow through skip flags.

## Booster parity boundary

`ran-booster` is the high-water reference, not a template to copy mechanically.

The shared workflows should absorb Booster gates that are technology-wide and deterministic. Booster-specific release lifecycle, exact artifact admission/reuse, updater source verification, WordPress/database matrix topology, and runtime/product contracts remain in Booster's local workflow.

When a transferable Booster guarantee is stronger than this shared layer, treat that as a baseline-review trigger rather than assuming the lower organisation guarantee is permanently sufficient.
