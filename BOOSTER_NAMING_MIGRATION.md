# Booster beta naming migration: declarations, dependencies and sequence

Owner workstream: `.github#65`, policy/evidence child `#66`; policy PR `#69`,
evidence PR `#70`. This extends the [shared-rule audit](BOOSTER_SHARED_RULES_AUDIT.md).
It proposes the migration cohorts; it does not rename application code or
release a new API generation.

## Decision

The owner has confirmed that public APIs may change during beta. Target
WordPress `snake_case` for RAN-owned methods, properties, parameters and locals,
including public members. Existing camelCase use is debt to address, not an
approved suite convention. Preserve exceptional names only where a concrete
external contract requires them. Coordinate the connected packages and their
certified host checks; do not add coexistence aliases by default.

This follows the [WordPress naming guidance](https://developer.wordpress.org/coding-standards/wordpress-coding-standards/php/#naming-conventions),
which also identifies parameter renaming as a breaking change for PHP named
arguments. This member/variable migration does not reconsider the deliberately
separate PSR-4 class/filename policy.

## What the original count did and did not mean

The earlier 24,128 naming diagnostics comprise 2,269 method declarations and
21,859 variable/property occurrences. Repeated reads contribute repeatedly.
The new AST pass parses **997 tracked PHP files**, including the 42 outside the
current PHPCS selection, and joins every method diagnostic to its declaration.

It identifies 6,221 file/scope/name groups with reported variable occurrences,
2,707 reported parameter declarations and 971 reported property declarations
(including promoted properties). These categories overlap: promoted parameters
are also properties, and parameters are also variable groups. They must not be
summed as unique symbols, required edits or implementation effort. Closure
captures may appear in more than one lexical group.

The public-method inventory below includes unreported camelCase candidates;
property counts are declarations matched to actual diagnostics. “Runtime” means
outside `tests/` and `scripts/`, not proof of an externally supported API.

| Package | Public runtime method candidates | Private/protected runtime method candidates | Flagged public runtime properties | Runtime methods absent from old diagnostics |
| --- | ---: | ---: | ---: | ---: |
| Core | 832 | 1,071 | 85 | 332 |
| Bitbucket | 45 | 44 | 0 | 54 |
| GitHub Provider | 106 | 152 | 0 | 89 |
| Branch Updater | 49 | 41 | 9 | 26 |
| Release Updater | 116 | 155 | 4 | 8 |
| Updater Support | 3 | 1 | 0 | 0 |
| Migrator | 20 | 21 | 0 | 0 |
| **Total** | **1,171** | **1,485** | **98** | **509** |

The 2,656 runtime method candidates count declarations, including implementations
of the same interface and three methods in Release Updater's generated Support
copy. They are not 2,656 unique API operations. The inventory contains every
public candidate with its class, file and line, including whether PHPCS reported
it. Public visibility is a review dimension, not an automatic exemption.

## A second enforcement gap: WPCS skips child classes

In the locked WPCS 3.4.1 [method-name sniff](https://github.com/WordPress/WordPress-Coding-Standards/blob/ec2ff942335f33683a5957a85d138753876a05cf/WordPress/Sniffs/NamingConventions/ValidFunctionNameSniff.php),
`process_method_declaration()` returns early for a class with an `extends` or
`implements` clause. It does not establish that each skipped method actually
implements an external signature. A new private method in a RAN interface
implementation also escapes this check.

Of the 509 additional runtime candidates, **506 are in selected inheriting or
interface-implementing classes**; the other three are in the intentionally
excluded generated Support copy. A focused negative control containing an
interface `inheritedName()`, its implementation, and an unrelated private
`unrelatedCamelCase()` reported only the interface declaration: one error,
exit 1. This confirms the local locked sniff behavior independently of the AST.

Consequently, removing local suppressions and getting green PHPCS is necessary
but insufficient. The migration needs a small shared RAN enforcement extension
for owned methods that upstream skips, plus explicit external-signature
exceptions. Prove a compliant implementation passes, a newly introduced owned
camelCase method in that implementation fails, and required PHP/PHPUnit names
remain valid. Do not maintain a blanket class-level inheritance exemption or
introduce a second PHP formatter.

## Concrete dependency cohorts

| Contract owner | Verified consumers/boundaries | Migration consequence |
| --- | --- | --- |
| Updater Support | Branch Updater calls `ArchiveSafety::normalizePath`, `entryTypeFailure`, `collisionFailure`; Release Updater contains a generated, namespace-rewritten copy | Rename the three public methods and private `RepositoryRelativePath::assertDecodedSegmentIsSafe`; update callers and fixtures. Update Release Updater's pinned Support dependency and regenerate through its sync script; do not hand-edit the generated copy. |
| Branch Updater | Core's `AdmittedBranchHostAdapter` implements Branch contracts; eight camelCase implementation relationships found | Update interface declarations, Core adapters, Branch implementations and their test doubles together. Example: `AdmittedArchiveSource::verifyCurrentHead`. |
| Core provider contracts | GitHub Provider has 52 and Bitbucket has 28 camelCase implementation relationships to Core contracts | Coordinate Core and both providers, their interface generations/compatibility declarations and exact certified-host revisions. Core bundles GitHub Provider, while Provider implements Core-owned contracts; this is a mutually dependent migration cohort. |
| Core add-on facades and DTOs | Migrator reads Core properties such as `targetVerified` and `credentialId`, and uses Core administration/portability facades | Rename DTO declarations, promoted constructor parameters, property reads, facade methods and test doubles as a Core/Migrator cohort. Existing Admin Interaction and Portability API 2 compatibility checks must reflect the new incompatible contract rather than continuing to claim the old generation. |
| Release Updater | Core and Provider depend on its released package; the runtime is also exposed through a bounded bootstrap/facade and generated-copy machinery | Separate internal PHP names from wire keys and runtime-copy metadata. Recompute required generated/hash state and run no-dev consumer, installed WordPress, Windows and runtime-copy proofs for the exact candidate. |

The AST inventory identifies 88 cross-package interface/implementation
relationships and 170 statically resolved cross-package call candidates.
These are lower bounds for coordination, not a complete call graph. Receiver
resolution is limited to direct static classes, `$this`, simple declared
parameter/property types and immediately instantiated receivers. It does not
prove dynamic or chained calls are absent. The generated-copy relationship was
verified separately from its source and sync script.

Current Composer requirements confirm Core pins Provider, Support, Branch and
Release Updater; Provider pins Support and Release Updater; Branch pins Support.
Release Updater owns a development Support pin and embeds its reviewed copy.
Add-ons rely on certified Core contracts rather than declaring the whole host
as a production Composer dependency.

## Names that need more than declaration replacement

- **Named arguments:** 768 sites were parsed, 266 with camelCase labels. Rename
  parameter declarations and labels together. Promoted parameters couple the
  constructor label and property name.
- **Callback/reflection strings:** 810 exact method-name string candidates were
  found. They include registered callbacks, mocks, reflection and unrelated
  data; inspect them rather than replacing every matching string globally.
- **Dynamic getter construction:** Core's `AbstractPackage::__get()` and
  `Storage\PackageModel::__get()` construct `'get' . ucfirst($name)`. Ordinary
  symbol references do not expose those callers. Update the mechanism and
  prove the resulting property access; do not leave an accidental legacy
  adapter to mask incomplete renaming.
- **External values:** WordPress/PHP API names, response-object properties,
  database columns, hook identifiers, serialized values and wire/JSON keys
  are not automatically PHP naming defects. Preserve those data contracts
  unless separately migrating them, and scope unavoidable access exceptions
  to the actual external boundary.
- **Actual external method signatures:** keep PHP magic methods such as
  `__toString`, PHPUnit lifecycle signatures, and any demonstrated third-party
  overrides. A custom method added to a `RuntimeException` subclass is owned
  by RAN; extending that class does not make the custom name externally fixed.
  The inspected production ancestors outside these seven packages are PHP
  exception classes, not an external provider interface dictating the suite's
  current camelCase convention.

## Implementation sequence and acceptance

1. **Set the enforcement contract.** Land the reviewed naming decision and
   add/prove the narrow owned-method check above. Keep these changes separate
   from release workflow primitives. Do not promote a blanket camelCase overlay.
2. **Pilot the leaf Support API.** It has four reported method declarations,
   three public and one private. Prepare its full naming cleanup and the exact
   Branch/Release consumer changes before releasing the incompatible names.
   This exercises public renames and generated-copy handling at manageable size.
3. **Prepare upstream updater and Core/provider cohorts.** Develop on isolated
   branches with an explicit old-to-new symbol manifest and exact candidate
   dependency/host tuples. Stage the library dependency updates, Core adapters,
   Provider and Bitbucket contracts together; qualify the actual composition,
   not each package against an obsolete host. Keep live Profile B ownership
   intact and rebase after that lane lands where files overlap.
4. **Migrate Core/Migrator facade and DTO boundaries together.** Cover named
   arguments, properties, registered callbacks, compatibility rejection of an
   incompatible host, and installed behavior. Update current agent/contributor
   guidance that currently presents camelCase as a permanent convention.
5. **Finish internal/test names and restore rules by completed scope.** Remove
   the corresponding broad method/variable suppressions; make any temporary
   migration exclusions explicit, bounded and removable. Preserve real fixture
   behavior and source exclusions with separate measured coverage decisions.
6. **Qualify and release by compatible cohort.** Run each repository's full
   required local/CI gates and focused consumer/contract tests on exact heads.
   Classify API-breaking changes visibly under the existing beta release
   policy; update pins and certification metadata through reviewed changes.
   Check old-to-new mapping for collisions and leftover owned references.
   Owner merge/release authorization remains separate.

Private methods/locals that have no cross-package boundary can be changed in
bounded parallel slices. That is an execution convenience, not a permanent
exclusion of public code. The existing small alignment/suppression PRs remain
independent and need not wait for the whole naming migration.

## Active lanes, exemptions and limits

On this refresh, all seven defaults still match the revisions in the original
shared-rule audit. Bitbucket Profile B PR #64 is active at
`5c2b5b417d88ee050edb2d48a5d0f9d25358e6da`; this pass changes no consumer
Composer files, workflows or runtime code. Existing quality PRs and bot-owned
release PRs keep their current ownership.

Workbench and dedicated fixtures retain the owner-confirmed command/style
exemptions. A fixture that calls a changed API may need a focused consumer
update; that is not authority to normalize its scripts or rewrite intentional
historical fixtures. The inspected public fixture plugin/theme/workflow entry
points contain no direct Booster API calls. The updater dummy deliberately
bundles the older updater generation and uses its named arguments; do not
silently convert that historical fixture to the current package.

This is a seven-package inventory with targeted supporting-fixture inspection,
not a complete estate-wide caller census. Private operational scripts, code
embedded inside strings, downstream forks and installations still require
cohort-specific checks. No application source was executed by the AST audit.
No production names, API versions, package pins, tags or releases changed.

## Evidence and bounded re-checks

[Machine-readable declaration/caller inventory](quality-evidence/booster-naming-inventory.json)
contains exact source revisions, category counts, all public runtime method
candidates, flagged public properties, interface relationships and representative
call sites. Paths and original diagnostic scopes remain explicit.

After repeating the relevant PHPCS probes as a new local measurement in the disposable
lab, run with PHP 8.4.23 and `nikic/php-parser` 5.8.0:

```sh
php -d memory_limit=1G quality-evidence/inventory-php-names.php \
  /tmp/booster-audit /path/to/parser/vendor/autoload.php /tmp/naming-raw.json
python3 quality-evidence/summarize-php-names.py \
  /tmp/booster-audit /tmp/naming-raw.json /tmp/booster-naming-inventory.json
```

The join checks source SHA-256 hashes against the parsed inputs, reports parser
errors, and requires every original method diagnostic to resolve to a declaration.
Raw AST data from a rerun is a new local measurement and is not committed. Record the rerun's source/tool inputs independently; parser candidate names are
not independently asserted WPCS violations; upstream heuristics, existing scope
and external signatures still require the dispositions described above.
