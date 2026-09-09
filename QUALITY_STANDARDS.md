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
- keep declared Node, pnpm, Composer, PHP, WordPress, and other toolchain constraints aligned with CI and documentation;
- version shared RAN standards so an upstream standards change reaches consumers through an explicit dependency or workflow update rather than silently through `main`.

## Canonical command contract

Repositories should expose predictable aggregate quality commands where the relevant ecosystem exists.

### Node

`pnpm check` means: run the ordinary deterministic Node/frontend quality baseline for the repository.

It should include applicable formatting checks, ESLint, Stylelint, frontend tests, and deterministic generated-artifact verification. Specialist checks may remain separate where they are expensive, environment-specific, release-specific, or deliberately outside the ordinary source-quality gate.

### Composer/PHP

`composer check` means: run the ordinary deterministic PHP quality baseline for the repository.

It should include applicable PHP formatting checks, PHPCS/WPCS, PHP compatibility, unit tests, static analysis, and other deterministic PHP source gates adopted by the repository.

Repositories may retain focused commands such as `composer test`, `composer standards`, `pnpm lint`, `pnpm format`, integration tests, Plugin Check, archive validation, or targeted generated-asset checks. Aggregate commands do not replace focused evidence required by `AGENTS.md` or CI.

## CI contract

RAN should provide versioned reusable GitHub Actions workflows for common quality profiles. Repository workflows may call those workflows and may add project-specific jobs.

A maintained repository must have one obvious quality result suitable for merge protection. The preferred public contract is a stable `quality` check or an equivalently stable status defined by the applicable profile.

Reusable workflow references must be versioned or pinned. Repositories must not depend permanently on an unversioned shared workflow reference such as `@main`.

Before an organisation ruleset requires a status across a repository group, every targeted repository must already emit the intended status reliably.

## Quality profiles

RAN uses a small number of profiles to describe the expected baseline.

### `wordpress-plugin`

Expected where applicable:

- PHPCS/WPCS;
- PHP compatibility;
- PHP tests;
- ESLint;
- Stylelint;
- Prettier;
- deterministic generated-artifact checks;
- project-specific integration/release checks defined locally.

### `php-library`

Expected where applicable:

- shared PHP coding standard;
- PHP compatibility;
- tests;
- static analysis where adopted.

### `node`

Expected where applicable:

- ESLint;
- Prettier;
- tests;
- Stylelint when styles exist.

### `mixed`

Uses the applicable PHP and Node baselines together.

### `fixture`

Uses only the checks necessary to preserve its fixture contract. A fixture must not be made production-like if that would change what it is intended to test.

### `legacy`

A temporary migration classification for maintained repositories that do not yet conform to the applicable modern profile. Migration should be staged so tooling changes are not unnecessarily mixed with unrelated application refactoring.

## Shared-package boundaries

The RAN PHP shared standard should own only organisation-wide PHP rules and deviations. It must not contain repository prefixes, namespaces, text domains, runtime support ranges, fixture-specific suppressions, or mature-project compatibility exceptions.

The RAN frontend-quality package should expose independent ESLint, Prettier, Stylelint CSS, and Stylelint SCSS entry points. A repository should install only the parts it needs.

Shared standards must have their own tests or fixtures and an independent release lifecycle. Runtime libraries such as `ran-plugin-library` are not the canonical home for coding policy.

## Review standard

Code review should treat the following as defects rather than stylistic preferences when the applicable profile requires them:

- missing or bypassed applicable quality tooling;
- a local config that silently weakens the shared RAN baseline without justification;
- project-specific settings embedded in a supposedly shared organisation config;
- broad suppression used instead of excluding generated/vendor code or documenting a narrow exception;
- runtime support declarations that disagree with compatibility checks;
- missing or ignored lockfiles where the ecosystem supports deterministic locking;
- `composer check` or `pnpm check` that no longer represents the documented ordinary quality baseline;
- CI that runs materially different checks from the documented local contract without explanation;
- documentation that weakens mandatory CI or `AGENTS.md` requirements;
- unversioned dependencies on shared RAN workflows or standards where an update could change consumer behaviour without a reviewable PR.

Repository-specific wording, source paths, supported versions, tool versions, test topology, runtime globals, prefixes, namespaces, text domains, and justified compatibility exceptions may differ where they reflect the actual project contract.

## Rollout and enforcement

Organisation enforcement follows this order:

1. define the standard;
2. implement and version shared configurations;
3. prove the standard in a clean reference repository and a mature complex repository;
4. migrate maintained repositories through reviewable PRs;
5. verify stable quality status names;
6. apply organisation rulesets only to repositories that already conform.

Organisation rules are the minimum. Individual repositories may impose stronger checks.

No repository should be made non-mergeable merely because an organisation-required status was enabled before that repository had been migrated to emit it.
