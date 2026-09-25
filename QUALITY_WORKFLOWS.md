# RAN reusable quality workflows

The workflows under `.github/workflows/` provide the common CI source-quality layer for repositories that have adopted the RAN quality command contract.

They deliberately invoke fixed aggregate commands rather than accepting arbitrary command inputs:

- `quality-node.yml` runs `pnpm check` and emits `RAN Node Quality`.
- `quality-php-library-v2.yml` is the current PHP-library provider. It runs the repository's Composer quality contract on configured PHP floor and current-stable lanes, with strict Composer validation and independent PHP syntax verification on both lanes.
- `quality-wordpress-plugin.yml` is the current mixed WordPress-plugin provider. It runs both canonical Composer and pnpm contracts and emits `RAN WordPress Plugin Quality`.

The historical single-PHP `quality-php-library.yml` provider was retired after the final organisation audit found no maintained default-branch consumer and no merge-intended open pull request pinning it. Compatible maintained PHP consumers use v2 where the reusable PHP baseline is applicable.

The current shared Node lane is intentionally pnpm-specific. RAN's maintained Node house style is pnpm. A repository with a concrete reason to retain another package manager must prove equivalent transferable guarantees as a justified difference rather than treating package-manager diversity as a goal of its own.

## Provider lifecycle policy

Reusable workflow generations represent contract changes, not naming symmetry. A new generation is warranted only when the shared profile contract changes materially enough that existing callers should move through an explicit reviewed migration. The existence of `quality-php-library-v2.yml` does **not** imply that WordPress or Node need a `v2`.

Provider selection is based on the repository's actual maintained source surface, not on which manifests happen to exist today. In particular:

- a **PHP-only WordPress source surface** has no maintained JS/TS/CSS/SCSS source that requires frontend quality tooling; generated assets alone do not create a package-manager requirement;
- a WordPress repository with maintained frontend source must retain the applicable frontend quality contract even if its current package metadata is incomplete;
- a maintained Node repository normally follows the organisation pnpm house style unless a repository-specific constraint justifies a different manager.

Current lifecycle state:

| Provider | Lifecycle state | Intended profile | Active default-branch consumers | Target consumers | Migration / retirement condition |
| --- | --- | --- | --- | --- | --- |
| `quality-php-library-v2.yml` | **CURRENT** | Maintained PHP-library source quality; also the shared PHP source baseline for PHP-only maintained WordPress source surfaces | `ran-updater-support`, `ran-wp-branch-updater`, `ran-wp-release-updater`, `ran-admin-shell`, `ran-booster-bitbucket`, `ran-booster-github-provider` | compatible maintained PHP consumers | Preferred PHP provider for new and migrating compatible consumers. Pure-PHP callers set `node-version: ''`; callers that genuinely need Node provide an exact full version. |
| `quality-wordpress-plugin.yml` | **CURRENT** | Maintained WordPress plugins with PHP plus maintained frontend source represented by Composer and locked pnpm quality contracts | `ran-starter-plugin`, `ran-emailoctopus-jetpack-forms`, `ran-ecwid-shop-teaser`, `ran-enhanced-cover`, `ran-turnstile-for-jetpack-forms`, `ran-duplicate-detector`, `ran-booster-wp-pusher-migrator`, `tnySignature` | compatible maintained mixed WordPress consumers | Keep as the current mixed WordPress contract. Do not create a WordPress `v2` unless a concrete shared contract gap requires an incompatible generation. |
| `quality-node.yml` | **CURRENT** | Maintained pnpm Node repositories | `ran-booster-workbench`, `ran-booster-release-bootstrap-templates` | compatible maintained pnpm Node consumers | Keep as the current pnpm Node contract. Non-pnpm is an explicit justified difference, not the default house style. |

`quality-php-library.yml` is **RETIRED / REMOVED**. It was the historical single-PHP predecessor to v2 and is no longer an available provider. No provider is currently classified **TRANSITIONAL**. The three current providers are intentionally different profiles: PHP source quality, mixed WordPress PHP+pnpm source quality, and pnpm Node source quality. That profile split is substantive and should remain small.

### Current and target consumer pins

Consumers execute immutable provider commits, not mutable release tags. The inventory below records the lifecycle-authoritative provider mapping from the completed quality-foundation review. Repository-specific terminal aggregation and stronger local gates now remain with `.github#65` / `#67` and the existing repository quality children. Completed `.github#7` / `#12` / `#15` are foundation/enforcement-design evidence, not active rollout queues; deferred organisation-required activation is owned by `.github#31`.

| Repository | Repository profile | Caller | Current provider / immutable ref | Target provider / immutable ref | Disposition |
| --- | --- | --- | --- | --- | --- |
| `ran-starter-plugin` | `wordpress-plugin` | `.github/workflows/quality.yml` | `quality-wordpress-plugin.yml@72a90b5826db37d1e94cdcdcf3374ccf58c0aa7d` | same | keep |
| `ran-emailoctopus-jetpack-forms` | `wordpress-plugin` | `.github/workflows/quality.yml` | `quality-wordpress-plugin.yml@72a90b5826db37d1e94cdcdcf3374ccf58c0aa7d` | same | keep |
| `ran-ecwid-shop-teaser` | `wordpress-plugin` | `.github/workflows/quality.yml` | `quality-wordpress-plugin.yml@72a90b5826db37d1e94cdcdcf3374ccf58c0aa7d` | same | keep |
| `ran-enhanced-cover` | `wordpress-plugin` | `.github/workflows/quality.yml` | `quality-wordpress-plugin.yml@72a90b5826db37d1e94cdcdcf3374ccf58c0aa7d` | same | keep |
| `ran-turnstile-for-jetpack-forms` | `wordpress-plugin` | `.github/workflows/quality.yml` | `quality-wordpress-plugin.yml@72a90b5826db37d1e94cdcdcf3374ccf58c0aa7d` | same | keep |
| `ran-duplicate-detector` | `wordpress-plugin` | `.github/workflows/quality.yml` | `quality-wordpress-plugin.yml@72a90b5826db37d1e94cdcdcf3374ccf58c0aa7d` | same | keep |
| `ran-booster-wp-pusher-migrator` | `wordpress-plugin` | `.github/workflows/quality.yml` | `quality-wordpress-plugin.yml@72a90b5826db37d1e94cdcdcf3374ccf58c0aa7d` | same | keep |
| `tnySignature` | `wordpress-plugin`; maintained JS/SCSS source | `.github/workflows/quality.yml` | `quality-wordpress-plugin.yml@72a90b5826db37d1e94cdcdcf3374ccf58c0aa7d` | same | keep |
| `ran-updater-support` | `php-library` | `.github/workflows/ci.yml` | `quality-php-library-v2.yml@788f783d2998994f7aab9691710911ed1bd762c9` | same | keep |
| `ran-wp-branch-updater` | `php-library` | `.github/workflows/ci.yml` | `quality-php-library-v2.yml@788f783d2998994f7aab9691710911ed1bd762c9` | same | keep |
| `ran-wp-release-updater` | `php-library` | `.github/workflows/ci.yml` | `quality-php-library-v2.yml@788f783d2998994f7aab9691710911ed1bd762c9` | same | keep |
| `ran-admin-shell` | `php-library` | `.github/workflows/quality.yml` | `quality-php-library-v2.yml@788f783d2998994f7aab9691710911ed1bd762c9` | same | keep |
| `ran-booster-bitbucket` | `wordpress-plugin`; audited PHP-only maintained source surface | `.github/workflows/quality.yml` | `quality-php-library-v2.yml@788f783d2998994f7aab9691710911ed1bd762c9` | same | keep shared PHP baseline; retain WordPress profile |
| `ran-booster-github-provider` | `php-library` | `.github/workflows/ci.yml` | `quality-php-library-v2.yml@788f783d2998994f7aab9691710911ed1bd762c9` | same | keep |
| `ran-booster-workbench` | `node`; internal planning/development tool | `.github/workflows/quality.yml` | `quality-node.yml@72a90b5826db37d1e94cdcdcf3374ccf58c0aa7d` | same | keep provider; no release/enforcement ceremony implied |
| `ran-booster-release-bootstrap-templates` | `node` | `.github/workflows/quality.yml` | `quality-node.yml@72a90b5826db37d1e94cdcdcf3374ccf58c0aa7d` | same | keep provider; clean Node/pnpm proof target; repository quality acceptance remains local/#65 and any future organisation-required activation belongs to `.github#31` |
| `ran-plugin-library` | `php-library` | none | none | v2 if migration is deliberately restarted later | deferred / not planned in current migration programme |
| `tnyGoogleKey` | historical/private WordPress plugin | none | none | none | out of active estate; re-audit if deliberately revived |

Repositories that remain on a deliberately local quality topology, such as `ran-wp-github-release-updater`, are not evidence that v1 remains live. They require their own migration or justified-difference disposition if they remain in the maintained enforcement estate.

### PHP v2 supersedes retired PHP v1

For compatible maintained PHP consumers, v2 supersedes retired v1. The difference is behavioural rather than cosmetic: v2 executes independently configured PHP floor and current-stable lanes, accepts required PHP extensions, optionally makes an exact Node runtime available for repository-owned checks, and applies strict Composer validation, locked installation, `composer check`, and independent syntax verification on both PHP lanes.

The workflow does **not** currently derive or validate `php-floor` / `php-current` against `composer.json` or another repository support declaration. Alignment of those caller inputs with the repository's authoritative support contract is therefore part of the PR-editable consumer quality contract and must be reviewed/protected accordingly. A future compatible provider hardening may validate that relationship; the current workflow must not be described as proving a declared support floor solely by receiving an input named `php-floor`.

The retired v1 workflow does not define a separate long-lived profile. Historical v1 references are migration history only and must not be restored as new callers.

A PHP-only WordPress repository does not need a separate WordPress-provider generation merely because its repository profile is `wordpress-plugin`. A repository qualifies for this provider choice only when its **maintained source surface has no JS/TS/CSS/SCSS source that requires frontend quality tooling**. It may then use PHP v2 for the shared PHP source baseline while retaining WordPress/runtime/archive/integration evidence locally. `ran-booster-bitbucket` currently meets that source-based condition. A legacy plugin with maintained frontend source must not bypass frontend quality merely because it has not yet added package metadata.

### WordPress remains on the current provider generation

The existing WordPress provider is the desired current contract for maintained plugins that genuinely have both PHP and maintained frontend source with Composer and locked pnpm quality contracts. If a legacy repository has maintained frontend source but incomplete package metadata, normalising that local frontend contract is part of its migration rather than a reason to select the PHP-only provider.

The provider's job is shared source-quality verification, not a generic WordPress/PHP compatibility matrix. Maintained plugins already own materially different support ranges and stronger product evidence: WordPress/PHP compatibility matrices, Jetpack compatibility, Plugin Check, fresh-ZIP install/activation, runtime archives, Core/provider contracts, generated-state checks, and release-candidate proofs. Those checks stay local and feed the repository's terminal quality result where appropriate.

A WordPress `v2` is therefore **not warranted now**. Adding a second generic PHP lane merely to mirror PHP-library v2 would duplicate richer repository-specific compatibility matrices and would run the frontend aggregate redundantly. A future WordPress v2 requires a concrete shared contract gap that cannot be represented compatibly by the present provider plus repository-owned specialist lanes.

### Node remains on the current provider generation

`quality-node.yml` is current and sufficient for maintained pnpm Node repositories. It owns exact-head execution, immutable Actions, locked pnpm installation, exact package-manager identity and the fixed `pnpm check` entry point.

A pnpm target repository that lacks `packageManager`, a lockfile, an exact/stable Node declaration or a truthful aggregate `pnpm check` must fix those local contracts as part of migration. RAN's normal maintained Node house style is pnpm. A repository that retains another manager needs a concrete repository-specific reason and must demonstrate equivalent transferable guarantees as a **JUSTIFIED DIFFERENCE**; package-manager diversity is not itself a reason to create another provider generation.

### Intentionally local/self-validating repositories

A reusable provider is an organisation minimum, not a reason to duplicate evidence mechanically. A repository may be classified **JUSTIFIED DIFFERENCE** only when its local workflow demonstrably preserves **every applicable transferable shared guarantee** from this document and then adds repository-specific evidence that makes the generic reusable wrapper redundant or inappropriate.

Extra specialist checks alone are not sufficient grounds to bypass the baseline. The local topology must still cover, where applicable, exact reviewed PR-head execution, immutable Actions, minimal permissions, credential-free checkout during project-controlled execution, deterministic/locked dependency handling, exact toolchain identity, canonical aggregate quality commands, and equivalent failure propagation.

The current shared standards packages satisfy that condition through their self-validation harnesses:

- `ran-coding-standards` verifies exact PR head, immutable Actions, read-only execution, locked Composer install, the package `composer check` contract, PHP floor/current-style coverage, independent PHP lint, and fresh consumer-root installation of every exported standard.
- `ran-quality-config` verifies exact PR head, immutable Actions, read-only execution, exact Node/pnpm identity, frozen pnpm install, `pnpm check`, packed consumer tests and publishable-package contents.

`ran-booster` remains the high-water WordPress implementation with a specialist evidence/admission lifecycle rather than a generic caller. That disposition remains valid only while its local topology continues to provide equivalent applicable transferable guarantees plus its stronger archive, admission, updater-source, compatibility-matrix and runtime/product evidence. Revisit it if a transferable organisation guarantee is missing; future organisation-required activation/composition changes are coordinated under #31 rather than reopening completed #12.

## Shared baseline guarantees

The reusable workflows own broadly transferable guarantees that should not be reimplemented differently in ordinary consumers:

- third-party Actions are pinned to immutable full commit SHAs;
- workflow permissions are read-only unless a profile proves a stronger permission is necessary;
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
- reusable providers own runner selection; a caller cannot redirect pull-request code to a self-hosted or otherwise privileged runner.

Testing the exact PR head and testing mergeability are separate contracts. The shared source-quality lane proves the reviewed head; repository rulesets/strict integration policy or a merge queue must ensure the head is current with the target branch before merge. A repository may add an explicit merge-integration lane when its product needs stronger base-integration evidence.

Project-specific focused checks remain in the caller repository. Examples include archive/package integrity, WordPress install/activation and compatibility matrices, Plugin Check, provider/runtime contracts, installed-consumer proofs, Windows portability, database CAS tests, deployment/release proofs, or other evidence whose exact shape belongs to the product rather than the organisation source baseline.

## Trust boundary: consumer quality contracts

These reusable profiles deliberately execute the consuming repository's canonical aggregate commands. That makes them useful for consistent verification, but it also means the aggregate scripts and the configuration they transitively consume are part of the pull-request source revision.

The same is true of caller-supplied identity inputs such as `php-floor`, `php-current`, PHP extensions, Node version and pnpm version unless the provider independently derives or validates them. A reviewed workflow invocation is therefore part of the transitive quality contract, not merely plumbing.

A ruleset-required organisation workflow prevents a target-repository pull request from replacing the organisation-owned workflow itself, but **workflow identity alone does not make a PR-controlled quality contract immutable**. A pull request could otherwise replace `composer check` or `pnpm check` with a no-op, weaken lint/static-analysis configuration, change a helper script, or misstate an unvalidated support/toolchain input while leaving the organisation-owned wrapper untouched.

Therefore these reusable profiles must not be treated as a standalone, unforgeable organisation merge-security boundary. Before RAN enables organisation ruleset enforcement for a profile, one of the following must also be true:

1. **Organisation-owned execution (preferred end state).** The ruleset-required workflow owns the authoritative commands/configuration and derives or validates required project identity independently of PR-editable aggregate definitions where necessary. Consumer aggregate commands remain the local developer interface and may run additionally, but they are not the sole authority for the required organisation gate.
2. **Protected consumer contract (transitional path).** Changes to the complete transitive quality contract require independent maintainer/code-owner approval that the PR author cannot self-satisfy. Stale approvals must be dismissed, or approval of the most recent reviewable push must be required, so a later commit cannot weaken the contract after approval.

The protected consumer contract includes, as applicable:

- caller workflow inputs such as PHP floor/current, extensions, Node/pnpm identity and working directory;
- `composer.json` script definitions, support declarations and quality-tool dependencies;
- `package.json` aggregate scripts, runtime/package-manager identity and quality-tool dependencies;
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

A maintained PHP library may call v2:

```yaml
jobs:
  baseline:
    uses: RocketsAreNostalgic/.github/.github/workflows/quality-php-library-v2.yml@<immutable-full-commit-sha> # quality-v2
    with:
      php-floor: '8.2'
      php-current: '8.5'
      php-extensions: zip
      node-version: ''
```

Expected shared contexts: `baseline / PHP 8.2 floor` and `baseline / PHP 8.5 compatibility`. The caller is responsible for keeping these unvalidated PHP-version inputs aligned with the repository's authoritative support contract until the provider derives or validates that relationship itself.

For a pure-PHP consumer with no repository quality command that needs Node, pass `node-version: ''` explicitly. When `node-version` is non-empty, v2 requires a full `major.minor.patch` value and verifies `node --version` before project-controlled commands run. The v2 provider deliberately does not expose a runner input; runner selection remains organisation-owned.

The historical v1 PHP caller is retired. New and restarted compatible maintained PHP migrations target v2.

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

A migrated repository should still expose a local terminal aggregation job named `quality` because it gives maintainers one clear result for all ordinary shared and project-specific lanes. The terminal job must fail if any required shared or repository-specific lane fails or is unexpectedly skipped.

The eventual security/enforcement boundary is an organisation or enterprise ruleset using GitHub's **Require workflows to pass before merging** rule **plus the quality-contract integrity requirement above**. The required workflow must be selected from an organisation-controlled repository/branch/workflow configuration so a target-repository pull request cannot replace it with a look-alike job. Where a required workflow delegates to these reusable profiles, that delegation should use an immutable reviewed provider SHA.

The final enforcement phase should therefore:

1. keep consumer baseline and terminal `quality` jobs for local feedback and diagnosis;
2. configure the appropriate organisation ruleset-required workflow for the repository profile;
3. ensure that required workflow executes the reviewed RAN baseline against the intended source revision;
4. establish either organisation-owned authoritative execution/configuration or independent protected approval for the complete transitive consumer quality contract; and
5. use repository-level required-workflow enforcement as needed for product-specific gates that must not be bypassable by editing a caller workflow.

Do not create organisation required-status rules that treat a consumer-controlled job name as proof of organisation workflow identity. Do not enable an organisation ruleset-required quality workflow while its authoritative checks can still be weakened solely by an unreviewed PR edit to consumer manifests, configuration, caller inputs or helper scripts.

## Inputs

Inputs are limited to project/toolchain identity such as PHP versions, PHP extensions, exact Node or pnpm version, Node-version file, and working directory. They do not allow callers to substitute the quality command, source revision, runner, or disable parts of a selected profile.

A caller-supplied pnpm version is not an override: the shared workflow compares it with `packageManager` and fails on disagreement. The v2 PHP workflow likewise verifies any non-empty Node version exactly after setup. PHP floor/current inputs are not yet cross-checked against repository support metadata, so their integrity remains part of the reviewed/protected consumer contract.

Choose the workflow matching the actual maintained source and tooling surface. Do not omit frontend quality because package metadata is missing, and do not keep a weaker provider generation merely because an older tracker or branch referenced it. Maintained Node repositories normally use pnpm; a different package manager requires an explicit repository-specific justification and equivalent quality guarantees.

## Booster parity boundary

`ran-booster` is the high-water reference, not a template to copy mechanically.

The shared workflows should absorb Booster guarantees that are technology-wide and deterministic. Booster-specific release lifecycle, exact artifact admission/reuse, updater source verification, WordPress/database matrix topology, and runtime/product contracts remain in Booster's local workflow.

A specialist/local workflow may substitute for a reusable provider only while it proves equivalent coverage of every applicable transferable shared guarantee. When a transferable Booster guarantee is stronger than the shared layer, treat that as a baseline-review trigger rather than assuming the lower organisation guarantee is permanently sufficient.
