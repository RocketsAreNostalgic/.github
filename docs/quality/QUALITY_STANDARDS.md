# RAN Quality Standards

## Scope and authority

Maintained RAN repositories follow this baseline for their actual code surfaces.
Local `AGENTS.md`, CI, tests, runtime declarations, locks and release contracts
supply project requirements. They may strengthen or specialize the baseline, not
silently weaken it. Stronger existing gates require an explicit reviewed
decision before removal. Missing tooling does not exempt applicable code from
these requirements.

Booster supplies reference evidence, not automatic organisation policy. Assess
stronger transferable practices for benefit, applicability and cost before
adoption; product-specific release and runtime architecture stays local. Starter
is the clean reference project used to qualify shared standards. Justified
configurations need not be identical.

## What applies

| Surface / profile | Required checks |
| --- | --- |
| Maintained PHP / `php-library` | Strict Composer validation, locked installation, shared standards, declared-range compatibility, independent syntax, maintained-production static analysis and behavioural, characterization and contract tests. PHPStan is the default; an existing equivalent is acceptable. |
| WordPress / `wordpress-plugin` | PHP plus applicable frontend checks, generated-asset and localisation parity, distributed-archive integrity, clean installation and activation and materially different supported WordPress, PHP and database boundaries. WordPress.org products need applicable Plugin Check evidence. |
| JavaScript/TypeScript / `node` | ESLint, formatting, applicable type checks, behavioural, unit and asset tests; Stylelint for CSS/SCSS; generated-artifact freshness, locked dependencies and declared toolchain. |
| `mixed` | Every applicable constituent requirement. |
| `fixture` | Document its purpose and necessary checks; justify production gates that would invalidate it. |
| `legacy` | Name the target profile and gaps; stage migration without avoidable new debt. This is temporary. |

Use mature shared or upstream tools. WordPress PHP uses PHPCS/WPCS and
preferably PHPCompatibilityWP. PHPCS checks and PHPCBF fixes use identical
rules, paths and exclusions. PHPCBF is the PHP fixer. A second formatter needs a
concrete unmet need and explicit review. Replacing a formatter must preserve
intended checks, reject known violations and produce stable results on repeated
runs.

WordPress frontend derives through shared RAN exports from
`@wordpress/eslint-plugin`, `@wordpress/prettier-config` and
`@wordpress/stylelint-config`. Prettier formats supported frontend code and text
unless incompatible. Use supported ESLint configuration, separate CSS/SCSS
exports and local `.editorconfig` consistent with the formatter. Environments,
globals, frameworks, browser support, source paths, project identity, runtime
settings and justified overrides stay local. Shared packages need tests and
independent releases; runtime libraries do not own coding policy. Install only
needed frontend exports.

Workbenches and fixtures retain recorded exemptions and useful interfaces;
security requirements still apply. Policy adoption does not reactivate inactive
or deferred repositories, including Plugin Library. Fixture command names need
not match production commands where their purposes differ.

## Commands and evidence

Local and CI checks must agree. `composer check` and the package manager's
`check` aggregate the applicable deterministic checks: formatting, linting,
compatibility, static analysis, type checks, tests and generated-state parity.
pnpm is the Node house style; another manager requires a concrete reason and
equivalent guarantees. Shared PHP CI may supply validation and syntax checks
without duplication inside `check`.

| Composer command | Contract |
| --- | --- |
| `check` | Non-mutating ordinary aggregate. |
| `lint:syntax` | Independent parser sweep. |
| `standards` / `standards:fix` | PHPCS checks WPCS and compatibility; PHPCBF applies matching fixes. |
| `analyze` | Analysis with declared paths, level and blocking or advisory status. |
| `test` | Ordinary deterministic tests, including local workflow and contract tests. |
| `check:host` | Required checks against an identified host application revision and setup. |
| `test:integration` | Required checks in a purpose-built integration environment. |

Use the applicable command names; do not add empty scripts. When renaming a
command, record its replacement; retain aliases only for actual callers.
`standards`, `analyze` and `test` do not rewrite source. Handle filenames
safely; propagate parser, interpreter, discovery and required-check failures.
Empty success must not hide failure. Repeated fixes must be stable; command
renaming does not change gates or defenses.

Checks may sit outside ordinary aggregates when they require privileges, an
external service, a destructive or dedicated integration environment, or a
release or deployment operation. Document the reason; every merge-required lane
still feeds terminal CI `quality`. Focused product checks remain required. For
host checks, verify the intended application revision and setup. A similarly
structured checkout or an arbitrary sibling directory is not enough. Keep
independent checks without making the host application a production dependency.

<a id="booster-naming-during-beta"></a>

## Booster PHP coverage and conventions

These additional requirements apply to maintained Booster ecosystem work,
including matching consumers. They are not an organisation-wide PHPStan Level 5
mandate and do not impose retrospective acceptance requirements on historical
releases. Adoption scope and delivery are tracked in
[#128](https://github.com/RocketsAreNostalgic/.github/issues/128); the adopted
policy decision is
[#134](https://github.com/RocketsAreNostalgic/.github/pull/134).

Every maintained first-party PHP file enters its approved PHPCS profile and
direct PHPStan analysis at **level 5 or stronger**, preserving higher gates:
tests, fixtures, scripts, entrypoints at the root, in nested directories or
without a file extension included. Use recursive roots or discovery with
precisely anchored, reviewed exemptions. Added or relocated files must be
covered automatically or fail coverage. Symbol discovery via
`scanFiles`/`scanDirectories` is not direct analysis.

Independently discover maintained files and files intended for distribution,
then compare them with actual checker selection, exclusions and effective
required rules. Comparing two copies of the same inclusion list is insufficient.
Keep source distributions distinct from runtime ZIPs, and check the file
populations for syntax, standards, compatibility and analysis separately. An
exemption from one gate does not waive another. Use scoped invocations to
prevent synthetic symbols from affecting production analysis. Route conflicting
fixtures to a suitable check or obtain a reviewed exemption; do not omit
development trees. A directory called `tests` is not exempt.

Use the locked checkers to prove that known violations fail. These negative
controls must cover new, nested, relocated or excluded maintained files,
development-directory name collisions, inherited configuration and weakened
rules or severities. Accepted exceptions must pass while out-of-scope violations
fail. Annotation guards account for accepted directive forms and case variants.
Exclude dependencies, caches and runtime state rather than broadly suppressing
rules. Generated-style exclusions require checked authoritative source and
verified parity with generated output and its provenance. Syntax-only coverage
requires justification.

Use WordPress-Extra-derived conventions. Owned functions, methods, properties,
parameters and local variables use `snake_case`, including public and inherited
implementations. Check declarations that upstream WPCS skips and prove those
checks reject known violations. Preserve actual foreign signatures, never
blanket class exemptions. Keep PSR-4 namespaces and class filenames and the
deliberate `WordPress.Files.FileName.NotHyphenatedLowercase` and
`WordPress.Files.FileName.InvalidClassFileName` exclusions. Retain Yoda without
changing evaluation order. Require accurate public contracts, useful types and
non-obvious explanations; full optional WordPress-Docs is not imposed, stronger
local documentation checks survive.

Runtime code and templates retain applicable input, escaping, nonce, SQL and
localisation checks. Standalone and CLI code omits only demonstrably
inapplicable framework rules; Composer packaging alone does not prove
independence. Tests retain conventions and compatibility. Justify allowances for
lifecycle methods, globals, CLI behavior or synthetic fixtures; helper code is
not exempt. Compatibility and analysis prove different properties.

Coordinate API renames across declarations, implementations, callers, named
arguments, registered callbacks and string references, tests and documentation.
Certify connected exact revisions; update compatibility declarations and genuine
pins before release. PHP renames do not authorize changes to hooks, wire
protocols, JSON or persisted schemas. Coexistence aliases require a demonstrated
mixed-version need and a removal condition.

## Exceptions require review

Use ordinary annotations or ruleset comments and existing PR or issue decisions.
Every exception needs the smallest practical diagnostic and code span, a
concrete reason and a reference to its reviewed scope. A comment or green
checker is not acceptance. Ignores covering an entire category or sniff remain
broad even on one line. Whole-file or directory allowances need evidence for
their entire scope, including future code. Re-enable bounded disables; blanket
all-rule suppression is forbidden in maintained code. Malformed and
negative-test fixtures need intentional boundaries and necessary identifiers.

Maintained-file analysis exemptions require explicit owner disposition; expose
new or widened exemptions in PR acceptance summaries. Reproduce checker
limitations with locked tools and focused controls where practical. Temporary
debt needs an owner and a removal condition; it is not automatically accepted.
Resolve justification, fix violations or obtain explicit recorded limitations
before acceptance. Remove stale annotations, not defenses. Shared waivers
require reviewed applicability and representative tests; repetition alone is
insufficient. Project-specific exceptions remain local.

Preserve these behavioral boundaries:

- Filesystem exceptions explain the required locking, atomicity, file identity or
  private-file behavior. Do not exempt whole alternative-functions categories.
- JSON exceptions explain the required flags, error handling, byte identity or
  independence from framework functions;
  “deterministic” alone is insufficient.
- Internal exception data is not HTML: escape at rendering boundaries and retain
  output checks. SQL and output exceptions require source or behavior evidence when
  checkers cannot trace receivers or fragments; zero diagnostics cannot certify them.
- Base64 used for authentication or opaque protocols needs an explained purpose
  and input boundaries; encoding
  alone is not executable obfuscation.
- Read-only navigation need not gain a nonce; validate input, preserve capability and
  access checks and perform no protected mutation.

<a id="shared-package-versions-consumer-upgrades-and-live-advisories"></a>

## Reproducible inputs and upgrades

Track required lockfiles; missing locks fail rather than resolve new graphs.
Validate Composer strictly before installation. Align declared and CI
toolchains; pnpm must exactly match `packageManager`. Pin shared workflows and
third-party Actions to full immutable SHAs; tags are discovery labels, not
execution references.

Prefer compatible released packages or owner-accepted immutable Git revisions in
manifests and lockfiles. Review changed surfaces, support floors, resolved graph
and coupled contracts; update manifests and locks together. Run the required
local, CI, host and archive checks against the exact consumer revisions. Record
identities before and after the change, affected rules, exceptions and evidence
in existing PRs. Package CI does not certify consumers. Review needed releases
and advisories promptly; no uniform versions, automatic estate bumps or fixed
upgrade cadence is implied.

Preserve adopted blocking `composer audit --locked --no-interaction`. Lookup
failure is unavailable evidence: retry the same locked candidate, not claim
security. Advisory waivers need narrow owner approval; exclusions, fail-open
behavior, relocation or removal need policy review and CI evidence. No new audit
is imposed where none was adopted.

<a id="enforcement-integrity"></a>

## CI evidence and enforcement

CI uses minimal permissions, credential-free project execution unless an
operation requires credentials, immutable Actions and fixed profile commands
without inputs that allow arbitrary commands or skip checks. Applicable shared
diagnostic contexts plus terminal `quality` must cover every required lane and
fail unless all succeed. Require statuses emitted by the selected supported
provider. [Workflow contracts](QUALITY_WORKFLOWS.md) describe implementation and
limits.

Status names do not prove authority. Organisation enforcement needs an
organisation-controlled required workflow **and** integrity of its complete
transitive contract: aggregate commands, dependencies, lockfiles, configuration,
helpers, tests, workflow callers and inputs identifying the checked project.
Prefer organisation-owned execution; alternatively require independent
maintainer or code-owner review authors cannot self-satisfy, dismissing stale
approvals or requiring latest-push approval. Identify each repository's actual
delegated surface.

Until both boundaries are protected, verification evidence is not the sole
organisation merge-security boundary. Version and verify the baseline, recording
any gaps between Starter and Booster. Activate rulesets only for repositories
qualified against that baseline; do not block repositories before they are
ready. The [registry implementation](../../quality-enforcement/README.md) is
dormant pending decisions in #31 and #139, not active protection.

## Review and qualification

Reviewers reject missing or bypassed gates, weakened coverage or support,
unjustified exceptions, differences between local and CI checks,
non-reproducible inputs and unprotected authority. Automation does not replace
exception judgment, owner acceptance or evidence from installed, manual or UI
checks. Standards and static analysis need separate verdicts; merge and
publication remain separate decisions. Follow the repository's documented
approval process; Ben retains specific merge and publication decisions for
coordinated work in #65.

Transferable findings name checked sibling repositories and code surfaces,
evidence, dispositions and remaining owners in existing issues or PRs.
[#136](https://github.com/RocketsAreNostalgic/.github/issues/136) records actual
gaps and repairs; policy is not a claim of estate-wide enforcement.

Extend existing tools and guards. New helpers, sniffs or profiles need a proven
gap or reusable need and the smallest practical change; abstractions need actual
consumers. No second interpreter, per-file registry, annotation language or
engine. Related exceptions may share behavioral evidence. Make it possible to
identify every covered use and its justification; a separate test, issue or
approval for each annotation is unnecessary. Keep mechanical cleanup separately
reviewable from behavioral, security or type changes.

Shared-standard publication requires the **same exact candidate** qualified
against Core and Starter; qualify Booster adoption before wider-estate rollout.
Record revisions, scope, accepted exceptions and checks in existing PRs or #65.
Mechanism changes update affected guidance and evidence in the same PR or record
cross-repository follow-up; unrelated commits do not invalidate scoped evidence.
Current work ownership and delivery plans remain in
[#65](https://github.com/RocketsAreNostalgic/.github/issues/65).
