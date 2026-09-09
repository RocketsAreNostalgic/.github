# RAN Quality Standards

## Status and scope

This document defines the organisation-wide software quality baseline for Rockets Are Nostalgic (RAN) repositories.

The purpose of the baseline is consistent quality with project-appropriate configuration. Repositories do not need identical configuration files, dependency versions, supported runtime ranges, or test suites. They do need to derive from the applicable RAN baseline, preserve the project contract, and make deliberate deviations explicit.

The intended hierarchy is:

**Organisation policy -> shared configs -> reusable CI -> repository-specific configuration -> organisation enforcement.**

These standards apply to maintained RAN repositories according to their technology and quality profile. Fixtures, archived repositories, and intentionally unsupported projects may use a reduced surface where the reduction is necessary to preserve their purpose. `legacy` is a migration state, not a permanent exemption.

## Authority and precedence

Quality policy does not replace a repository's engineering contract.

1. Repository-local `AGENTS.md`, CI, runtime declarations, lockfiles, release documentation, and tests remain authoritative for project-specific requirements.
2. Shared RAN quality packages provide the organisation baseline for the technologies they cover.
3. Repository-local configuration may add or narrow project-specific requirements but must not silently weaken applicable organisation invariants.
4. Where a local exception is necessary, it must be narrow, documented, and attributable to a real compatibility, runtime, fixture, generated-code, legacy-contract, or architectural requirement.
5. Documentation must not make a mandatory CI or project-contract gate optional.

## Core invariants

Maintained source code must use appropriate automated quality tooling where a mature tool exists for the technology.

- Dependencies and toolchains must be reproducible from tracked lockfiles where the ecosystem supports lockfiles.
- Local development and CI must invoke equivalent authoritative quality gates.
- Generated, vendored, third-party, cache, coverage, and runtime state should be excluded from source-quality checks rather than accommodated with broad rule suppression.
- Quality configuration should extend shared or upstream standards rather than duplicate them unnecessarily.
- Exceptions must be scoped to the smallest practical rule, file, path, fixture, or compatibility boundary.
- Every exception to a required profile gate must be documented in reviewed repository guidance or configuration with the concrete reason it cannot or should not apply.
- Warnings and disabled rules that express an organisation-wide decision belong in the shared RAN standard; repository-specific deviations remain local.
- A repository must not claim support for a runtime or platform range that its compatibility checks contradict.

## WordPress PHP

Maintained WordPress PHP code must use WordPress Coding Standards (WPCS) through PHP_CodeSniffer.

The RAN shared PHP coding-standard package should provide the common WPCS baseline and organisation-wide deviations. Repository-local PHPCS configuration should provide project identity and support information such as:

- minimum supported WordPress version;
- PHP compatibility range;
- namespace and global prefix;
- text domain;
- project-specific source paths;
- justified fixture, inherited-API, legacy-contract, generated-code, or integration exceptions.

PHP compatibility checks must cover the repository's declared supported PHP range. PHPCompatibilityWP is the preferred baseline for maintained WordPress PHP projects unless a documented project constraint requires an equivalent mechanism.

A project-specific PHPCS exception must not be promoted into the shared RAN standard merely because one mature repository requires it.

## JavaScript and TypeScript

WordPress-facing JavaScript and TypeScript should derive from the official `@wordpress/eslint-plugin` baseline.

The shared RAN ESLint configuration may add organisation-wide rules, compatibility defaults, or common ignores. Repository-local configuration remains responsible for:

- browser, Node, worker, test, and build environments;
- runtime globals such as `wp`, `jQuery`, or `$`;
- React or TypeScript applicability;
- project source globs;
- generated and vendor paths;
- justified project-specific rule exceptions.

ESLint configuration should use the current configuration model supported by the repository's declared ESLint generation. Legacy repositories may migrate configuration shape separately from application refactoring.

## Prettier

Prettier is the standard formatter for supported frontend and text formats unless a documented incompatibility exists.

WordPress projects should derive formatting from `@wordpress/prettier-config` through the shared RAN frontend-quality package. RAN should not duplicate WordPress formatting decisions without an intentional organisation-level reason.

Repositories may add local format overrides only where file type, generated output, embedded syntax, or another concrete project requirement demands them.

## CSS and SCSS

WordPress CSS and SCSS should derive from the official `@wordpress/stylelint-config` baseline through the shared RAN frontend-quality package.

The shared configuration may provide separate CSS and SCSS exports and may adopt organisation-wide additions only after they have been shown to work across representative repositories.

Repository-local Stylelint configuration remains responsible for:

- CSS versus SCSS applicability;
- source globs;
- browser-support policy where project-specific;
- generated/vendor exclusions;
- project-specific selector or framework exceptions.

Preferences that exist only in the starter or one plugin are not organisation standards until deliberately adopted here.

## EditorConfig

Maintained repositories should carry a local `.editorconfig` because editors consume it directly and GitHub does not provide organisation inheritance for EditorConfig.

RAN should keep a reference baseline aligned with its formatter decisions. Local differences should be limited to project file types, generated files, or other concrete project constraints.

## Lockfiles and toolchains

Where supported by the ecosystem:

- install from tracked lockfiles in local development and CI;
- do not replace locked installs with dependency updates in setup scripts;
- keep declared Node, package-manager, Composer, PHP, WordPress, and other toolchain constraints aligned with CI and documentation;
- shared RAN packages must arrive through lockfile changes reviewed in the consuming repository;
- shared RAN workflow callers must execute an immutable full commit SHA, so a workflow change reaches consumers through an explicit reviewed update rather than a moved branch or tag.

Human-readable release tags may be recorded beside an immutable workflow SHA for provenance and upgrade discovery, but a mutable tag is not the execution reference.

## Canonical command contract

Repositories should expose predictable aggregate quality commands where the relevant ecosystem exists.

### Node and frontend projects

The repository's authoritative package manager must expose a script named `check`. Invoke it with that repository's package manager, for example `pnpm check`, `npm run check`, or `yarn check`.

For a pnpm repository, `pnpm check` means: run the ordinary deterministic Node/frontend source-quality baseline for the repository.

The aggregate must include every applicable deterministic formatter, linter, type check, unit/asset test, and tracked generated-artifact freshness check that can run in a standard isolated CI environment without privileged mutation, deployment credentials, external service availability, or a purpose-built destructive/integration environment.

A check may remain outside the aggregate only when it objectively requires one of those non-standard environments or is specifically a release/publication/deployment proof. That exclusion must be documented in the repository contract, and if the check is required for ordinary merge approval it must still feed the terminal CI `quality` gate.

A repository may not omit an applicable ordinary deterministic check merely by declaring it outside the aggregate.

### Composer/PHP projects

A Composer repository must expose `composer check` as its ordinary deterministic PHP source-quality baseline.

The aggregate must include every applicable deterministic PHP formatter check, PHPCS/WPCS check, PHP compatibility check, unit test suite, static-analysis gate already adopted by the project, and other ordinary source-quality check that can run in a standard isolated CI environment.

As with frontend checks, exclusions are limited to concrete environment, privilege, destructive-integration, release, publication, or deployment requirements; they must be documented, and ordinary merge-required checks must still feed the terminal CI `quality` gate.

Repositories may retain focused commands such as `composer test`, `composer standards`, package-manager lint/format commands, integration tests, Plugin Check, archive validation, or targeted compatibility proofs. Aggregate commands do not replace focused evidence required by `AGENTS.md` or CI.

## CI contract

RAN should provide reusable GitHub Actions workflows for common quality profiles. Repository workflows may call those workflows and may add project-specific jobs.

Shared organisation workflows must pin third-party actions to immutable full commit SHAs. Their consumers must also pin the reusable RAN workflow itself to an immutable full commit SHA.

Every migrated maintained repository must expose a local terminal job named exactly `quality`. That job must depend on every shared and project-specific lane required for ordinary merge approval and must fail unless all required dependencies succeed.

The terminal local `quality` context is the organisation merge-protection contract. Nested reusable-workflow contexts such as `baseline / quality` are implementation details and must not become the organisation-required status.

Before an organisation ruleset requires `quality` across a repository group, every targeted repository must already emit and pass that exact terminal context reliably.

## Quality profiles and applicability

A profile requirement is mandatory when its triggering code surface exists. A repository may only omit it through the narrow documented-exception process above.

### `wordpress-plugin`

Required gates:

- when maintained PHP exists: PHPCS/WPCS and PHP compatibility against the declared supported range;
- when maintained JavaScript or TypeScript exists: the applicable WordPress-derived ESLint baseline and deterministic formatting;
- when maintained CSS or SCSS exists: the applicable WordPress-derived Stylelint baseline and deterministic formatting;
- when behavioural production code exists: automated behavioural tests at the narrowest practical layer, unless a concrete testability/environment constraint is documented;
- when tracked generated runtime assets exist: deterministic freshness/parity verification;
- tracked lockfiles and locked installs for every package ecosystem that supports them;
- a terminal local `quality` CI job aggregating every ordinary merge-required lane.

Static analysis is required when the repository has adopted it as part of its reviewed contract. Removing an adopted static-analysis gate requires an explicit reviewed decision rather than being treated as non-applicable.

### `php-library`

Required gates:

- the applicable shared RAN PHP coding standard;
- PHP compatibility against the declared supported range;
- automated tests for behavioural production code unless a concrete constraint is documented;
- tracked Composer lockfile where the repository policy tracks one, with deterministic installation;
- a terminal local `quality` CI job.

Static analysis is required when adopted by the repository contract.

### `node`

Required gates:

- ESLint for maintained JavaScript/TypeScript source;
- Prettier or the documented organisation formatter for supported source formats;
- automated tests for behavioural production code unless a concrete constraint is documented;
- Stylelint when maintained CSS/SCSS exists;
- tracked package-manager lockfile and locked installation;
- a package-manager `check` script implementing the deterministic aggregate contract;
- a terminal local `quality` CI job.

### `mixed`

Uses every applicable mandatory gate from the constituent PHP and Node/WordPress surfaces rather than choosing only one side.

### `fixture`

Only checks necessary to preserve and validate the documented fixture contract are required. The repository must identify itself as a fixture and document why production-profile gates that would alter the fixture are not applicable.

A fixture must not be made production-like if doing so changes what it is intended to test.

### `legacy`

A temporary migration classification for a maintained repository that does not yet conform to its target profile. The repository must identify the target profile and the known baseline gaps. New changes must not introduce additional avoidable quality debt merely because migration is incomplete.

Migration should be staged so tooling changes are not unnecessarily mixed with unrelated application refactoring.

## Shared-package boundaries

The RAN PHP shared standard should own only organisation-wide PHP rules and deviations. It must not contain repository prefixes, namespaces, text domains, runtime support ranges, fixture-specific suppressions, or mature-project compatibility exceptions.

The RAN frontend-quality package should expose independent ESLint, Prettier, Stylelint CSS, and Stylelint SCSS entry points. A repository should install only the parts it needs.

Shared standards must have their own tests or fixtures and an independent release lifecycle. Runtime libraries such as `ran-plugin-library` are not the canonical home for coding policy.

## Review standard

Code review should treat the following as defects when the applicable profile or triggering code surface requires them:

- missing or bypassed applicable quality tooling;
- a local config that silently weakens the shared RAN baseline without a narrow documented exception;
- project-specific settings embedded in a supposedly shared organisation config;
- broad suppression used instead of excluding generated/vendor code or documenting a narrow exception;
- runtime support declarations that disagree with compatibility checks;
- missing or ignored lockfiles where the ecosystem supports deterministic locking;
- an authoritative package-manager `check` script or `composer check` that omits an applicable ordinary deterministic gate;
- a merge-required focused check that does not feed the terminal local `quality` job;
- CI that runs materially different checks from the documented local contract without explanation;
- documentation that weakens mandatory CI or `AGENTS.md` requirements;
- a reusable organisation workflow referenced through a mutable branch or tag instead of an immutable full commit SHA;
- removal of an already-adopted static-analysis or test gate without an explicit reviewed decision.

Repository-specific wording, source paths, supported versions, tool versions, test topology, runtime globals, prefixes, namespaces, text domains, and justified compatibility exceptions may differ where they reflect the actual project contract.

## Rollout and enforcement

Organisation enforcement follows this order:

1. define the standard;
2. implement and version shared configurations;
3. prove the standard in a clean reference repository and a mature complex repository;
4. migrate maintained repositories through reviewable PRs;
5. verify the terminal local `quality` status across representative repositories;
6. apply organisation rulesets only to repositories that already conform.

Organisation rules are the minimum. Individual repositories may impose stronger checks.

No repository should be made non-mergeable merely because an organisation-required status was enabled before that repository had been migrated to emit it.
