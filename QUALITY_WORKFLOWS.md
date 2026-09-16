# RAN reusable quality workflows

The workflows under `.github/workflows/` provide the common CI source-quality layer for repositories that have adopted the RAN quality command contract.

They deliberately invoke fixed aggregate commands rather than accepting arbitrary command inputs:

- `quality-node.yml` runs `pnpm check` and emits `RAN Node Quality`.
- `quality-php-library.yml` is the legacy single-PHP predecessor to the current PHP-library contract and emits `RAN PHP Library Quality`.
- `quality-php-library-v2.yml` is the current PHP-library provider. It runs the repository's Composer quality contract on both its PHP floor and current-stable PHP, with strict Composer validation and independent PHP syntax verification on both lanes.
- `quality-wordpress-plugin.yml` is the current mixed WordPress-plugin provider. It runs both canonical contracts and emits `RAN WordPress Plugin Quality`.

The current shared Node lane is intentionally pnpm-specific because that matches the maintained RAN Node estate. A non-pnpm repository should use an equivalent local or future manager-specific shared lane rather than add pnpm solely to consume this workflow.

## Provider lifecycle policy

Reusable workflow generations represent contract changes, not naming symmetry. A new generation is warranted only when the shared profile contract changes materially enough that existing callers should move through an explicit reviewed migration. The existence of `quality-php-library-v2.yml` does **not** imply that WordPress or Node need a `v2`.

Current lifecycle state:

| Provider | Lifecycle state | Intended profile | Active default-branch consumers | Target consumers | Migration / retirement condition |
| --- | --- | --- | --- | --- | --- |
| `quality-php-library-v2.yml` | **CURRENT** | Maintained PHP-library source quality; also the shared PHP source baseline for PHP-only maintained WordPress plugins where the mixed WordPress provider would manufacture a Node surface | `ran-updater-support`, `ran-wp-branch-updater`, `ran-wp-release-updater` | `ran-plugin-library`, `ran-admin-shell`, and the PHP-only baseline of `ran-booster-bitbucket` after their repository-local migrations | Preferred PHP provider for new and migrating compatible maintained consumers. Pure-PHP callers set `node-version: ''`; callers that need Node provide an exact full version. |
| `quality-php-library.yml` | **LEGACY / DEPRECATION** | Historical single-PHP PHP-library source baseline | none on maintained default branches | none | Do not add new consumers. Retire only after every maintained PHP-source target has moved to v2 and no open PR/branch intended for merge still pins v1. |
| `quality-wordpress-plugin.yml` | **CURRENT** | Maintained WordPress plugins with both Composer and locked pnpm quality contracts | `ran-starter-plugin`, `ran-emailoctopus-jetpack-forms`, `ran-ecwid-shop-teaser`, `ran-enhanced-cover`, `ran-turnstile-for-jetpack-forms`, `ran-duplicate-detector` | `ran-booster-wp-pusher-migrator` and maintained legacy WordPress plugins once their local quality/toolchain contracts are migrated | Keep as the current WordPress contract. Do not create a WordPress `v2` unless a concrete shared contract gap requires an incompatible generation. |
| `quality-node.yml` | **CURRENT** | Maintained pnpm Node repositories | none yet | `ran-booster-workbench`, `ran-booster-release-bootstrap-templates` | Keep as the current Node contract. Consumer migrations must first expose a truthful locked `pnpm check` contract and stable Node/package-manager identity; that is a repository migration, not a provider-generation gap. |

There is no provider currently classified **TRANSITIONAL**. The three current providers are intentionally different profiles: PHP source quality, mixed WordPress PHP+pnpm source quality, and pnpm Node source quality. That profile split is substantive and should remain small.

### PHP v2 supersedes PHP v1

For compatible maintained PHP consumers, v2 supersedes v1. The difference is behavioural rather than cosmetic: v2 proves the declared PHP floor and current-stable PHP independently, accepts the repository's required PHP extensions, optionally makes an exact Node runtime available for repository-owned checks, and applies strict Composer validation, locked installation, `composer check`, and independent syntax verification on both PHP lanes.

The v1 workflow does not define a separate long-lived profile that justifies permanent coexistence. It remains only as a deprecation bridge while the remaining maintained PHP consumers move.

A PHP-only WordPress repository does not need a separate WordPress-provider generation merely because its repository profile is `wordpress-plugin`. If it has no package-managed Node surface, it may use the current PHP v2 provider for the shared PHP source baseline while retaining WordPress/runtime/archive/integration evidence in its local workflow. This is a capability-driven provider choice, not a downgrade of the repository's WordPress profile.

### WordPress remains on the current provider generation

The existing WordPress provider is the desired current contract for maintained plugins that genuinely have both Composer and locked pnpm quality surfaces. Its job is shared source-quality verification, not a generic WordPress/PHP compatibility matrix.

Maintained plugins already own materially different support ranges and stronger product evidence: WordPress/PHP compatibility matrices, Jetpack compatibility, Plugin Check, fresh-ZIP install/activation, runtime archives, Core/provider contracts, generated-state checks, and release-candidate proofs. Those checks should stay local and feed the repository's terminal quality result where appropriate.

A WordPress `v2` is therefore **not warranted now**. In particular, adding a second generic PHP lane merely to mirror PHP-library v2 would duplicate richer repository-specific compatibility matrices and would run the frontend aggregate redundantly. A future WordPress v2 requires a concrete shared contract gap that cannot be represented compatibly by the present provider plus repository-owned specialist lanes.

### Node remains on the current provider generation

`quality-node.yml` is current and sufficient for the maintained Node targets identified by the organisation migration programme. It owns exact-head execution, immutable Actions, locked pnpm installation, exact package-manager identity and the fixed `pnpm check` entry point.

A target repository that lacks `packageManager`, a lockfile, an exact/stable Node declaration or a truthful aggregate `pnpm check` must fix those local contracts as part of migration. That is not a reason to weaken or version the provider.

### Intentionally local/self-validating repositories

A reusable provider is an organisation minimum, not a requirement to duplicate evidence mechanically. Repositories whose local CI is itself a conformance harness may remain intentionally distinct when the local workflow proves more specific package-provider behaviour that a generic caller would only duplicate. The current shared standards packages (`ran-coding-standards` and `ran-quality-config`) are examples: their local workflows include fresh consumer/package verification in addition to their ordinary aggregate checks.

Likewise `ran-booster` remains the high-water WordPress implementation with a specialist evidence/admission lifecycle. It consumes the shared coding/frontend standards but should not gain a redundant reusable baseline solely for visual consistency. Revisit that disposition only if a transferable organisation guarantee is missing from Booster's local workflow or #12 establishes an organisation-required execution boundary that needs a different composition.

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

A maintained PHP library should call v2:

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

For a pure-PHP consumer with no repository quality command that needs Node, pass `node-version: ''` explicitly. The v2 provider deliberately does not expose a runner input. Pull requests in caller repositories can edit their caller workflow, so runner selection must remain organisation-owned rather than allowing a PR to redirect project-controlled commands to a self-hosted or otherwise privileged runner. When `node-version` is non-empty, v2 requires a full `major.minor.patch` value and verifies `node --version` before project-controlled commands run.

The legacy v1 PHP workflow remains available only during the deprecation window for already-staged callers. New or restarted maintained migrations must target v2 rather than adding another v1 pin.

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

Choose the workflow matching the actual maintained quality surface. Do not add a package manager merely to satisfy a broader provider, and do not keep a weaker provider generation merely because an older tracker or branch referenced it.

## Booster parity boundary

`ran-booster` is the high-water reference, not a template to copy mechanically.

The shared workflows should absorb Booster gates that are technology-wide and deterministic. Booster-specific release lifecycle, exact artifact admission/reuse, updater source verification, WordPress/database matrix topology, and runtime/product contracts remain in Booster's local workflow.

When a transferable Booster guarantee is stronger than this shared layer, treat that as a baseline-review trigger rather than assuming the lower organisation guarantee is permanently sufficient.
