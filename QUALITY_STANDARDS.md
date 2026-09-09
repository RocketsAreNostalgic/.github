# RAN Quality Standards

## Status and scope

This document defines the organisation-wide software quality baseline for Rockets Are Nostalgic (RAN) repositories.

The goal is consistent quality with project-appropriate configuration. Repositories do not need identical configuration files, dependency versions, runtime ranges, CI topology, or test suites. They do need to derive from the applicable RAN baseline, preserve the local project contract, and make deviations explicit.

The intended hierarchy is:

**Organisation policy -> shared configs -> reusable CI -> repository-specific configuration -> organisation enforcement.**

These standards apply to maintained RAN repositories according to their technology and quality profile. Fixtures, archived repositories, and intentionally unsupported projects may use a reduced surface only where that reduction is necessary to preserve their purpose. `legacy` is a migration state, not a permanent exemption.

## Reference high-water implementation

`RocketsAreNostalgic/ran-booster` is the reference high-water implementation for RAN quality engineering.

The organisation should strive for parity with Booster where a gate is broadly transferable, including:

- immutable third-party Action references and minimal workflow permissions;
- checkout without persisted Git credentials before project-controlled commands run;
- exact declared Node/package-manager toolchains and locked dependency installation;
- strict Composer manifest/lock validation before installation;
- PHPCS/WPCS and PHP compatibility checks;
- static analysis for maintained production PHP;
- deterministic frontend formatting/linting and asset tests;
- independent PHP syntax validation;
- behavioural, characterization, contract, or integration tests appropriate to the code surface;
- deterministic package/archive verification where a repository ships an installable artifact;
- runtime install/activation/compatibility evidence where the product contract requires it;
- one reviewable terminal merge gate that cannot pass unless all ordinary required evidence succeeds.

Booster-specific release-candidate admission, artifact-reuse provenance, updater-source verification, deployment semantics, provider contracts, release state machines, and other product-specific evidence remain local to Booster. The aim is parity in transferable quality guarantees, not duplication of Booster's architecture or CI size.

When Booster adopts a stronger broadly applicable quality invariant, reviewers should assess whether it belongs in this standard and the shared RAN tooling rather than allowing the organisation baseline to drift permanently below the reference implementation.

## Authority and precedence

Quality policy does not replace a repository's engineering contract.

1. Repository-local `AGENTS.md`, CI, runtime declarations, lockfiles, release documentation, and tests remain authoritative for project-specific requirements.
2. Shared RAN quality packages and workflows provide the organisation baseline for the technologies they cover.
3. Repository-local configuration may add or specialize project-specific requirements but must not silently weaken applicable organisation invariants.
4. A local exception must be narrow, documented, and attributable to a concrete compatibility, runtime, fixture, generated-code, legacy-contract, or architectural requirement.
5. Documentation must not make a mandatory CI or project-contract gate optional.
6. A stronger reviewed local gate remains required until an explicit reviewed decision removes it; adoption of the organisation minimum never justifies lowering an existing repository contract.

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
- Ordinary CI must execute project-controlled code with the minimum practical token permissions and without persisted checkout credentials unless a documented workflow operation genuinely requires them.

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

Maintained production PHP must also have static analysis at an appropriate strictness. PHPStan is the RAN default unless a repository has an existing equivalent. A maintained repository without static analysis is a migration gap requiring a documented exception or `legacy` classification; absence alone does not make the gate non-applicable.

A project-specific PHPCS or static-analysis exception must not be promoted into the shared RAN standard merely because one mature repository requires it.

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
- fail the shared quality lane when a required lockfile is absent rather than allowing the package manager to resolve a new graph;
- validate Composer configuration strictly before installation;
- keep declared Node, package-manager, Composer, PHP, WordPress, and other toolchain constraints aligned with CI and documentation;
- for pnpm repositories, the version executed by shared CI must exactly match the version declared in `packageManager`;
- shared RAN packages must arrive through lockfile changes reviewed in the consuming repository;
- shared RAN workflow callers must execute an immutable full commit SHA, so a workflow change reaches consumers through an explicit reviewed update rather than a moved branch or tag;
- third-party Actions in shared workflows must be pinned to immutable full commit SHAs.

Human-readable release tags may be recorded beside immutable SHAs for provenance and upgrade discovery, but a mutable tag is not the execution reference.

## Canonical command contract

Repositories should expose predictable aggregate quality commands where the relevant ecosystem exists.

### Node and frontend projects

The repository's authoritative package manager must expose a script named `check`. Invoke it with that repository's package manager, for example `pnpm check`, `npm run check`, or `yarn check`.

For a pnpm repository, `pnpm check` means: run the ordinary deterministic Node/frontend source-quality baseline for the repository.

The aggregate must include every applicable deterministic formatter, linter, type check, unit/asset test, and tracked generated-artifact freshness check that can run in a standard isolated CI environment without privileged mutation, deployment credentials, external service availability, or a purpose-built destructive/integration environment.

A check may remain outside the aggregate only when it objectively requires one of those non-standard environments or is specifically a release/publication/deployment proof. That exclusion must be documented in the repository contract, and if the check is required for ordinary merge approval it must still feed the terminal CI `quality` gate.

A repository may not omit an applicable ordinary deterministic check merely by declaring it outside the aggregate.

The current shared RAN Node workflow is pnpm-specific because that matches the maintained RAN Node estate. A non-pnpm repository must use an equivalent local or future manager-specific shared lane rather than introducing a second package manager solely to consume the pnpm workflow.

### Composer/PHP projects

A Composer repository must expose `composer check` as its ordinary deterministic PHP source-quality baseline.

The aggregate must include every applicable deterministic PHP formatter check, PHPCS/WPCS check, PHP compatibility check, unit/characterization/contract test suite, static-analysis gate, and other ordinary source-quality check that can run in a standard isolated CI environment.

Shared PHP CI additionally validates Composer configuration strictly and performs an independent PHP syntax sweep. These checks need not be duplicated inside `composer check` when the shared profile lane already guarantees them.

As with frontend checks, exclusions are limited to concrete environment, privilege, destructive-integration, release, publication, or deployment requirements; they must be documented, and ordinary merge-required checks must still feed the terminal CI `quality` gate.

Repositories may retain focused commands such as `composer test`, `composer standards`, package-manager lint/format commands, integration tests, Plugin Check, archive validation, or targeted compatibility proofs. Aggregate commands do not replace focused evidence required by `AGENTS.md` or CI.

## CI contract

RAN provides reusable GitHub Actions workflows for common source-quality profiles. Repository workflows may call those workflows and add project-specific jobs.

Shared organisation workflows must:

- use minimal permissions;
- pin third-party Actions to immutable full commit SHAs;
- check out without persisted Git credentials before project-controlled commands run;
- require the profile's tracked lockfiles before installation;
- enforce exact package-manager identity where the profile defines one;
- invoke the canonical local aggregate command rather than accept a caller-supplied weaker substitute.

Consumers must pin the reusable RAN workflow itself to an immutable full commit SHA.

Every migrated maintained repository must expose two distinct merge-protection guarantees:

1. the applicable profile-specific shared status, such as `baseline / RAN WordPress Plugin Quality`, `baseline / RAN PHP Library Quality`, or `baseline / RAN Node Quality`, proving that the repository did not substitute a weaker shared profile; and
2. a local terminal job named exactly `quality`, proving that every shared and project-specific lane required for ordinary merge approval succeeded.

The terminal job must depend on all required lanes and must fail unless each required dependency succeeds. Project-specific jobs may be stricter than the organisation baseline and remain mandatory through this terminal gate.

Before an organisation ruleset requires either status across a repository group, every targeted repository must already emit and pass the intended exact contexts reliably.

## Quality profiles and applicability

A profile requirement is mandatory when its triggering code surface exists. A repository may only omit it through the narrow documented-exception process above.

### `wordpress-plugin`

Required gates:

- when maintained PHP exists: strict Composer validation, PHPCS/WPCS, PHP compatibility against the declared supported range, independent PHP syntax validation, and static analysis;
- when maintained JavaScript or TypeScript exists: the applicable WordPress-derived ESLint baseline and deterministic formatting;
- when maintained CSS or SCSS exists: the applicable WordPress-derived Stylelint baseline and deterministic formatting;
- when behavioural production code exists: automated behavioural tests at the narrowest practical layer;
- when inherited or compatibility-sensitive behaviour exists: characterization or contract coverage where that is the most reliable regression boundary;
- when tracked generated runtime assets exist: deterministic freshness/parity verification;
- when tracked translation templates or generated localisation artifacts exist: deterministic localisation parity/freshness verification;
- when an installable plugin archive is part of the supported distribution contract: deterministic archive construction/content/integrity verification feeding `quality`;
- when deployable runtime plugin code exists: at least one clean install/activation smoke proof, with broader WordPress/PHP/database matrix coverage where materially different supported boundaries require runtime proof;
- when the repository targets WordPress.org: applicable Plugin Check evidence;
- tracked lockfiles and locked installs for every package ecosystem that supports them;
- the profile-specific shared status plus terminal local `quality` status.

A concrete environment or legacy constraint may temporarily defer one of these gates only through the documented-exception or `legacy` process. A missing test/static-analysis/runtime proof is not automatically non-applicable merely because the repository does not currently have it.

### `php-library`

Required gates:

- strict Composer validation and deterministic installation;
- the applicable shared RAN PHP coding standard;
- PHP compatibility against the declared supported range;
- independent PHP syntax validation;
- static analysis for maintained production PHP;
- automated tests for behavioural production code;
- characterization/contract tests where inherited or compatibility-sensitive public behaviour warrants them;
- a tracked Composer lockfile for reproducible RAN development/CI;
- the profile-specific shared status plus terminal local `quality` status.

### `node`

Required gates:

- ESLint for maintained JavaScript/TypeScript source;
- Prettier or the documented organisation formatter for supported source formats;
- automated tests for behavioural production code;
- Stylelint when maintained CSS/SCSS exists;
- tracked package-manager lockfile and locked installation;
- an authoritative package-manager `check` script implementing the deterministic aggregate contract;
- exact declared package-manager execution where the shared profile supports it;
- the profile-specific shared status plus terminal local `quality` status.

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
- missing or ignored lockfiles where deterministic locking is required;
- a package-manager version that disagrees with the repository's exact declared toolchain;
- an authoritative package-manager `check` script or `composer check` that omits an applicable ordinary deterministic gate;
- missing static analysis for maintained production PHP without a reviewed exception or legacy classification;
- missing package/archive or install/activation proof where the product profile triggers it;
- a merge-required focused check that does not feed the terminal local `quality` job;
- a repository emitting terminal `quality` while using the wrong or weaker profile-specific shared workflow;
- CI that runs materially different checks from the documented local contract without explanation;
- documentation that weakens mandatory CI or `AGENTS.md` requirements;
- a reusable organisation workflow or third-party Action referenced through a mutable branch or tag instead of an immutable full commit SHA;
- project-controlled CI commands running with persisted checkout credentials without a documented operational need;
- removal of an already-adopted test, static-analysis, runtime, or compatibility gate without an explicit reviewed decision.

Repository-specific wording, source paths, supported versions, tool versions, test topology, runtime globals, prefixes, namespaces, text domains, and justified compatibility exceptions may differ where they reflect the actual project contract.

## Rollout and enforcement

Organisation enforcement follows this order:

1. define the standard;
2. implement and version shared configurations and reusable source-quality workflows;
3. prove the standard in the clean Starter reference and compare it against the Booster high-water reference;
4. record any justified Starter/Booster parity gaps before declaring the baseline stable;
5. migrate maintained repositories through reviewable PRs;
6. verify the profile-specific and terminal `quality` statuses across representative repositories;
7. apply organisation rulesets only to repositories that already conform.

Organisation rules are the minimum. Individual repositories may impose stronger checks, and the baseline must not be used as a reason to remove them.

No repository should be made non-mergeable merely because an organisation-required status was enabled before that repository had been migrated to emit it.
