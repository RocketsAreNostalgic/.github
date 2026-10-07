# RAN Quality Standards

<a id="status-and-scope"></a>
<a id="authority-and-precedence"></a>
<a id="reference-high-water-implementation"></a>
<a id="core-invariants"></a>

## Scope and authority

Maintained RAN repositories follow this baseline for their actual code surfaces.
Local `AGENTS.md`, CI, tests, runtime declarations, locks and release contracts
supply project requirements. They may strengthen or specialize the baseline,
not silently weaken it. Stronger existing gates require an explicit reviewed
decision before removal. Missing tooling is a migration gap, not non-applicability.

Booster supplies reference evidence, not automatic organisation policy. Assess
stronger transferable practices for benefit, applicability and cost before
adoption; product-specific release/runtime architecture stays local. Starter
supplies clean-reference qualification. Justified configurations need not be identical.

<a id="find-the-requirement-for-your-change"></a>
<a id="quality-profiles-and-applicability"></a>
<a id="wordpress-plugin"></a>
<a id="php-library"></a>
<a id="node"></a>
<a id="mixed"></a>
<a id="fixture"></a>
<a id="legacy"></a>
<a id="wordpress-php"></a>
<a id="php-formatting-authority"></a>
<a id="javascript-and-typescript"></a>
<a id="prettier"></a>
<a id="css-and-scss"></a>
<a id="editorconfig"></a>
<a id="shared-package-boundaries"></a>

## What applies

| Surface / profile | Required checks |
| --- | --- |
| Maintained PHP / `php-library` | Strict Composer validation, locked installation, shared standards, declared-range compatibility, independent syntax, maintained-production static analysis and behavioural/characterization/contract tests. PHPStan is the default; an existing equivalent is acceptable. |
| WordPress / `wordpress-plugin` | PHP plus applicable frontend checks, generated-asset/localisation parity, distributed-archive integrity, clean install/activation and materially different supported WordPress/PHP/database boundaries. WordPress.org products need applicable Plugin Check evidence. |
| JavaScript/TypeScript / `node` | ESLint, formatting, applicable type checks, behavioural/unit/asset tests; Stylelint for CSS/SCSS; generated-artifact freshness, locked dependencies and declared toolchain. |
| `mixed` | Every applicable constituent requirement. |
| `fixture` | Document its purpose and necessary checks; justify production gates that would invalidate it. |
| `legacy` | Name target profile/gaps; stage migration without avoidable new debt. This is temporary. |

Use mature shared/upstream tools. WordPress PHP uses PHPCS/WPCS and preferably
PHPCompatibilityWP. PHPCS checks and PHPCBF fixes use identical rules/paths/exclusions.
PHP-CS-Fixer is migration debt: remove dependency/configuration/cache/callers,
preserve intended checks and prove negative controls/stable fixes. A second
formatter needs a concrete unmet need and explicit review; Starter has no exemption.

WordPress frontend derives through shared RAN exports from
`@wordpress/eslint-plugin`, `@wordpress/prettier-config` and
`@wordpress/stylelint-config`. Prettier formats supported frontend/text unless
incompatible. Use supported ESLint configuration, separate CSS/SCSS exports and
local formatter-aligned `.editorconfig`. Environments/globals, frameworks, browser
support, source paths, identity/runtime settings and justified overrides stay
local. Shared packages need tests and independent releases; runtime libraries do
not own coding policy. Install only needed frontend exports.

Workbench/fixtures retain recorded exemptions and useful interfaces; security
still applies. Inactive/deferred repositories, including Plugin Library, are not
reactivated. Do not rename fixture commands merely for symmetry.

<a id="canonical-command-contract"></a>
<a id="php-command-meanings"></a>
<a id="node-and-frontend-projects"></a>
<a id="composerphp-projects"></a>
<a id="adoption-and-role-based-exceptions"></a>

## Commands and evidence

Local and CI checks must agree. `composer check` and the package manager's
`check` aggregate applicable deterministic ordinary formatting, linting,
compatibility, analysis/types, tests and generated-state parity. pnpm is the
Node house style; another manager requires a concrete reason/equivalent guarantees.
Shared PHP CI may supply validation/syntax without duplication inside `check`.

| Composer command | Contract |
| --- | --- |
| `check` | Non-mutating ordinary aggregate. |
| `lint:syntax` | Independent parser sweep. |
| `standards` / `standards:fix` | PHPCS/WPCS/compatibility check / matching PHPCBF fixer. |
| `analyze` | Analysis with declared paths, level and blocking/advisory status. |
| `test` | Ordinary deterministic tests, including local workflow/contract tests. |
| `check:host` / `test:integration` | Required exact-certified host / purpose-built integration checks. |

Adopt applicable names during bounded migration; no empty scripts. Record removed
names/replacements; aliases need actual callers. `standards`, `analyze` and `test`
do not rewrite source. Handle filenames safely; propagate parser, interpreter,
discovery and required-check failures. Empty success must not hide failure.
Repeated fixes must be stable; command renaming does not change gates or defenses.

Only concrete privilege, external-service, destructive/integration-environment or
release/deployment needs justify checks outside ordinary aggregates. Document
them; every merge-required lane still feeds terminal CI `quality`. Focused product
checks remain required. Verify certified-host checkout identity/setup, not arbitrary
siblings or shape alone; preserve independent checks without making the host a
production dependency.

<a id="booster-naming-during-beta"></a>
<a id="next-beta-booster-php-acceptance"></a>
<a id="common-convention-and-scope"></a>
<a id="default-coverage-and-reviewed-exemptions"></a>

## Booster PHP coverage and conventions

These additional requirements apply to the Booster ecosystem under
[#128](https://github.com/RocketsAreNostalgic/.github/issues/128) and adopted
[#134](https://github.com/RocketsAreNostalgic/.github/pull/134), for the beta after
beta.31 and matching consumers; not retrospectively to beta.31 or the wider estate.

Every maintained first-party PHP file enters its approved PHPCS profile and
direct PHPStan analysis at **level 5 or stronger**, preserving higher gates:
tests, fixtures, scripts, root/nested and extensionless entrypoints included.
Use recursive roots/discovery with anchored reviewed exemptions. Added/relocated
files must be covered automatically or fail coverage. Symbol discovery via
`scanFiles`/`scanDirectories` is not direct analysis.

Compare independently discovered maintained/distribution populations with actual
checker selection, exclusions and effective required rules, not two copies of
one inclusion list. Distinguish source distributions/runtime ZIPs and
syntax/standards/compatibility/analysis populations; one exemption does not waive
another gate. Isolate production inference from synthetic symbols with scoped
invocations; conflicting fixtures need routing/reviewed exemptions, not omission
of development trees. A directory called `tests` is not exempt.

Real locked-checker negative controls must cover new/nested/relocated or excluded
maintained files, development-directory name collisions, inherited configuration
and rule/severity weakening. Accepted exceptions must pass while out-of-scope
violations fail. Annotation guards account for accepted directive forms/case
variants. Exclude dependencies/caches/runtime state rather than broadly suppressing
rules. Generated-style exclusions require checked authoritative source and
verified generation/provenance parity. Syntax-only coverage requires justification.

Use WordPress-Extra-derived conventions, owned `snake_case` functions/methods/
properties/parameters/locals including public/inherited implementations, and
checks/negative controls for declarations upstream WPCS skips. Preserve actual
foreign signatures, never blanket class exemptions. Keep PSR-4 namespaces/class
filenames and the deliberate `WordPress.Files.FileName.NotHyphenatedLowercase`
and `WordPress.Files.FileName.InvalidClassFileName` exclusions. Retain Yoda without
changing evaluation order. Require accurate public contracts, useful types and
non-obvious explanations; full optional WordPress-Docs is not imposed, stronger
local documentation checks survive.

Runtime/templates retain applicable input, escaping, nonce, SQL and localisation
checks. Standalone/CLI code omits only demonstrably inapplicable framework rules;
Composer packaging alone does not prove independence. Tests retain conventions/
compatibility with justified lifecycle/global/CLI/synthetic allowances, not helper
exemptions. Compatibility and analysis prove different properties.

Coordinate API renames across declarations, implementations, callers, named
arguments, registered callbacks/strings, tests and documentation. Certify connected
exact revisions; update compatibility declarations and genuine pins before release.
PHP renames do not authorize hook/wire/JSON/persisted-schema changes. Coexistence
aliases require mixed-version need/removal condition. Do not repeat completed work.

<a id="exceptions-and-native-operations"></a>

## Exceptions require review

Use ordinary annotations/ruleset comments and existing PR/issue decisions. Every
exception needs the smallest practical diagnostic/span, concrete reason and
traceable reviewed scope. A comment or green checker is not acceptance.
Category/sniff ignores remain broad even on one line. Whole-file/directory
allowances need evidence for their entire scope, including future code. Re-enable
bounded disables; blanket all-rule suppression is forbidden in maintained code.
Malformed/negative fixtures need intentional boundaries and necessary identifiers.

Maintained-file analysis exemptions require explicit owner disposition; expose
new/widened exemptions in PR acceptance summaries. Reproduce checker limitations
with locked tools/focused controls where practical. Temporary debt needs owner/
removal condition, not automatic acceptance. Resolve justification, fix violations
or obtain explicit recorded limitations before acceptance. Remove stale annotations,
not defenses. Shared waivers require reviewed applicability/representative tests;
repetition alone is insufficient. Project-specific exceptions remain local.

Preserve these behavioral boundaries:

- Filesystem exceptions establish exact locking, atomicity, identity/private-file
  needs, not whole alternative-functions categories.
- JSON exceptions establish flags, errors, byte identity/framework independence;
  “deterministic” alone is insufficient.
- Internal exception data is not HTML: escape at rendering boundaries and retain
  output checks. SQL/output exceptions require source/behavior evidence when
  checkers cannot trace receivers/fragments; zero diagnostics cannot certify them.
- Authentication/opaque-protocol Base64 needs purpose/input boundaries; encoding
  alone is not executable obfuscation.
- Read-only navigation need not gain a nonce; validate input, preserve capability/
  access checks and perform no protected mutation.

<a id="lockfiles-and-toolchains"></a>
<a id="shared-package-versions-consumer-upgrades-and-live-advisories"></a>

## Reproducible inputs and upgrades

Track required lockfiles; missing locks fail rather than resolve new graphs.
Validate Composer strictly before installation. Align declared/CI toolchains;
pnpm must exactly match `packageManager`. Pin shared workflows/third-party Actions
to full immutable SHAs; tags are discovery labels, not execution references.

Prefer compatible released packages or owner-accepted immutable Git revisions
in manifests/locks. Review changed surfaces, support floors, resolved graph and
coupled contracts; update manifests/locks together and qualify exact consumer
local/CI/host/archive gates. Record before/after identities, affected rules,
exceptions and evidence in existing PRs. Package CI does not certify consumers.
Review needed releases/advisories promptly; no uniform versions, automatic
estate bumps or fixed upgrade cadence is implied.

Preserve adopted blocking `composer audit --locked --no-interaction`. Lookup
failure is unavailable evidence: retry the same locked candidate, not claim
security. Advisory waivers need narrow owner approval; exclusions, fail-open
behavior, relocation/removal need policy review and CI evidence. No new audit
is imposed where none was adopted.

<a id="ci-contract"></a>
<a id="enforcement-integrity"></a>
<a id="rollout-and-enforcement"></a>

## CI evidence and enforcement

CI uses minimal permissions, credential-free project execution unless an operation
requires credentials, immutable Actions and fixed profile commands without
arbitrary-command/skip inputs. Applicable shared diagnostic contexts plus terminal
`quality` must cover every required lane and fail unless all succeed. Retired
PHP-v1 status is not a required check. [Workflow contracts](QUALITY_WORKFLOWS.md)
describe implementation and limits.

Status names do not prove authority. Organisation enforcement needs an
organisation-controlled required workflow **and** integrity of its complete
transitive contract: aggregates/dependencies/locks, configurations, helpers/tests,
caller topology and identity inputs. Prefer organisation-owned execution;
alternatively require independent maintainer/code-owner review authors cannot
self-satisfy, dismissing stale approvals or requiring latest-push approval.
Identify each repository's actual delegated surface.

Until both boundaries are protected, verification evidence is not the sole
organisation merge-security boundary. Prove/version the baseline with Starter/
Booster parity gaps recorded, migrate/qualify repositories, then activate rulesets
only for ready targets. Do not block unmigrated repositories prematurely.
The [registry implementation](../../quality-enforcement/README.md) is dormant
pending #31/#139 decisions, not active protection.

<a id="review-standard"></a>
<a id="reuse-existing-tools-and-protect-the-agreed-contract"></a>
<a id="qualification-and-release-boundaries"></a>
<a id="delivery-order-and-ownership"></a>

## Review and qualification

Reviewers reject missing/bypassed gates, weakened scope/support, unjustified
exceptions, local/CI mismatches, non-reproducible inputs and unprotected authority.
Automation does not replace exception judgment, owner acceptance or installed/
manual/UI evidence. Standards/analysis need separate verdicts; merge/publication
remain separate decisions. Follow the repository's documented approval process;
Ben retains specific merge/publication decisions for coordinated work in #65.

Transferable findings name checked sibling repositories/surfaces, evidence,
dispositions and remaining owners in existing issues/PRs. [#136](https://github.com/RocketsAreNostalgic/.github/issues/136)
records actual gaps/repairs; policy is not a claim of estate-wide enforcement.

Extend existing tools/guards. New helpers/sniffs/profiles need a proven gap or
reusable need and the smallest practical change; abstractions need actual
consumers. No second interpreter, per-file registry, annotation language or
engine. Reuse behavioral evidence across grouped exceptions with occurrence
traceability, not a new test/issue/approval ritual per annotation. Keep mechanical
cleanup separately reviewable from behavioral/security/type changes.

Shared-standard publication requires the **same exact candidate** qualified
against Core and Starter; qualify Booster adoption before wider-estate rollout.
Record revisions, scope, accepted exceptions and checks in existing PRs/#65.
Mechanism changes update affected guidance/evidence in the same PR or record
cross-repository follow-up; unrelated commits do not invalidate scoped evidence.
Temporary sequencing remains in [#65](https://github.com/RocketsAreNostalgic/.github/issues/65).
