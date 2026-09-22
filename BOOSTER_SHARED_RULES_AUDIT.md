# Booster shared-rules impact assessment

Measured 22 September 2026 for [#66](https://github.com/RocketsAreNostalgic/.github/issues/66).
This is evidence for a decision, not an implemented or approved shared-rule change.
No consumer source, Composer file, workflow, lock or shared standard was changed.
The experiment used disposable copies and verified all 1,447 tracked snapshot
files against their Git blob identities after the probes.

## Findings

All seven packages use the same locked quality-tool graph and derive from the
same RAN WordPress ancestry. All **955 PHP files selected by their current
rulesets pass**, with zero errors and warnings. The seven snapshots contain
997 tracked PHP files; the difference is source selection, not a tool-version
mismatch. This is a PHPCS result, not a fresh run of their full quality suites.

All seven disable the WordPress camelCase method/variable checks. Six disable
Yoda conditions; Updater Support retains that rule. All seven currently permit
PHPCS to report warnings. Unlike the earlier Starter configuration, there is
no `-n` suppression in these seven ordinary PHPCS commands/rulesets.

Restoring WordPress method/variable naming and Yoda checks, while making the
existing assignment/array-alignment rules errors, gives:

| Package | PHP checked / tracked | Method-name diagnostics | Variable/property diagnostics | Yoda diagnostics | Alignment changes |
| --- | ---: | ---: | ---: | ---: | ---: |
| Core | 694 / 694 | 1,655 | 16,704 | 114 | 0 |
| Bitbucket | 19 / 47 | 35 | 242 | 1 | 0 |
| GitHub Provider | 67 / 67 | 184 | 1,669 | 11 | 0 |
| Branch Updater | 37 / 50 | 64 | 285 | 12 | 0 |
| Release Updater | 92 / 93 | 274 | 2,534 | 42 | 0 |
| Updater Support | 5 / 5 | 4 | 31 | 0 | 0 |
| WP Pusher Migrator | 41 / 41 | 53 | 394 | 1 | 0 |
| **Total** | **955 / 997** | **2,269** | **21,859** | **181** | **0** |

These are diagnostic occurrences, **not unique identifiers or required edit
counts**. Repeated reads of one variable generate multiple diagnostics.
Existing path and inline exceptions remain in effect; the experiment does not
estimate violations in excluded code. The candidate contains 24,309 findings,
all non-autofixable by this locked PHPCBF generation.

PHPCBF's alignment-only passes changed zero files in every package; second
passes were byte-stable and the corresponding checks passed. Yoda-only passes
also changed zero files, but left the findings above unresolved. That second
result is **lack of autofix support**, not evidence that the stricter Yoda gate
passes. Full naming enforcement was inspected, not automatically renamed.

A deliberate alignment-defect control under Updater Support's current rules
returned PHPCS exit 2 with two fixable warnings. The proposed error promotion
returned exit 2 with two fixable errors. Both block today. Moving alignment into
an explicit shared contract need not produce a suite formatting sweep.

## Naming requires a coordinated migration

The flagged methods include actual public contracts, such as
[Branch Updater's `AdmittedArchiveSource::verifyCurrentHead()`](https://github.com/RocketsAreNostalgic/ran-wp-branch-updater/blob/15253ac03878b01da254d6702a9753103354d8e9/src/Contract/AdmittedArchiveSource.php).
Changing these identifiers requires coordinated declarations, implementations,
callers, fixtures and potentially named-argument handling. PHPCBF cannot supply
that migration. Test helpers and implementation locals also contribute heavily
to the totals; they must not all be labelled public-API exceptions.

| Package | Naming outside `tests/` and `scripts/` | Yoda outside those paths | Yoda in tests/scripts |
| --- | ---: | ---: | ---: |
| Core | 12,279 | 93 | 21 |
| Bitbucket | 277 | 1 | 0 |
| GitHub Provider | 1,142 | 9 | 2 |
| Branch Updater | 349 | 12 | 0 |
| Release Updater | 1,201 | 13 | 29 |
| Updater Support | 22 | 0 | 0 |
| Migrator | 192 | 1 | 0 |

“Outside tests/scripts” is a path classification, not a proof that every item
is a public API. There are 129 Yoda findings outside those paths and 52 within
them. Updater Support needs no condition-style weakening to converge on the
WordPress default; the six other packages would need reviewed condition edits.
No conditional expressions were changed in this experiment.

## Broad suppressions have smaller, separable cleanup opportunities

A second probe enables the three recurring unused-parameter, useless-override
and reserved-keyword-parameter rule families, retaining other local exceptions.
It finds 320 warnings, none autofixable:

| Package | Unused parameters | Useless overrides | Reserved keyword parameters |
| --- | ---: | ---: | ---: |
| Core | 215 | 0 | 56 |
| Bitbucket | 0 | 0 | 1 |
| GitHub Provider | 10 | 0 | 9 |
| Branch Updater | 1 | 1 | 1 |
| Release Updater | 14 | 0 | 8 |
| Updater Support | 0 | 0 | 0 |
| Migrator | 0 | 0 | 4 |

This does not establish 320 defects. For example, Branch Updater's unused
`$context` belongs to a callback signature, and its apparently redundant
constructor also declares a promoted readonly property. These need narrow
justifications, not deletion based only on a sniff message.

Concrete candidates for the eventual implementation:

- Remove the now-unneeded unused-parameter suppression in Bitbucket, subject
  to the implementation head's fresh check.
- Remove the zero-finding useless-override suppressions in Core and Release
  Updater. Do not propagate them into a shared suite profile.
- GitHub Provider's ten unused-parameter findings are all in tests. Release
  Updater's fourteen are also all in tests. Replace whole-repository suppression
  with identified test-stub/callback exceptions where justified.
- Core has 203 unused-parameter findings in tests and twelve elsewhere. Review
  the twelve runtime cases and the test contracts before choosing narrow scope.
- Keep WordPress hook/signature, native filesystem/atomicity, canonical JSON,
  exact namespace, generated-copy and security-boundary exceptions local and
  justified. Repetition alone does not make them shared coding policy.

## Source selection remains part of the decision

- Bitbucket excludes 28 tracked PHP files: 26 under tests, its release verifier,
  and `index.php`. Its current production roots are entrypoint, autoloader,
  `src/` and `views/`. Do not report these counts as whole-repository parity.
- Branch Updater excludes twelve test/support files and its consumer-fixture
  preparation script. This is an explicit existing contract: syntax and
  executable tests cover them separately. Expansion needs its own measured
  treatment of intentionally non-production fixtures.
- Release Updater excludes the generated `src/Dependency/ArchiveSafety.php`,
  whose byte parity with Updater Support is checked separately.
- The other four snapshots select all tracked PHP files. Inline suppressions
  still apply; a file being selected does not mean every sniff runs on every line.

Workbench and dedicated fixture repositories remain outside this experiment
and retain the owner's purpose-based exemptions. Tests inside a production
repository still need an explicit coverage contract; they are not automatically
exempt because a separate fixture repository can be exempt.

## Proposed direction for owner review

1. **One PHPCS/PHPCBF authority and one shared WordPress ancestry.** The seven
   tool versions already align; retain them. Express common suite rules once,
   while retaining product identity and genuine boundary exceptions locally.
   Canonical script adoption remains necessary, especially Migrator's missing
   focused fixer command, but it does not resolve the rule decisions below.
2. **Keep alignment blocking.** No suite source churn is indicated. A shared
   alignment guarantee should survive a consumer's warning-display choices;
   prove it with a negative control rather than assuming severity labels suffice.
3. **Prefer the WordPress Yoda baseline across the suite.** This preserves
   Updater Support's existing enforcement and removes six blanket exceptions.
   It requires 181 reviewed findings to be addressed at these scopes, with
   behavior/contract tests on each implementation candidate. Do not add a
   second formatter just to automate these rewrites.
4. **Apply the owner's subsequent beta naming decision.** Public visibility
   does not freeze RAN-owned APIs. Target WordPress `snake_case` for methods,
   properties, parameters and locals, with coordinated declarations, callers,
   named arguments, tests and releases. Preserve only demonstrated external
   signature constraints. The [declaration/caller follow-up](BOOSTER_NAMING_MIGRATION.md)
   replaces the earlier open choice between a Booster camelCase convention and
   snake_case migration. It also identifies methods hidden by WPCS's inheritance
   heuristic, beyond the diagnostic counts in this historical probe.
5. **Remove or narrow demonstrated redundant suppressions and reconcile
   coverage separately.** Use the concrete findings above. These smaller edits
   can be reviewed independently of naming, release architecture and bulk
   production rewrites.

This recommends an implementation sequence; it does not start it. No new shared
profile, consumer rule edit, source rewrite, dependency change or workflow
change has been proposed in an implementation PR by this experiment.

## Revisions, method and limits

The [machine-readable results](quality-evidence/booster-rule-results.json)
contain full source revisions, locked tool versions/references, effective local
rule exceptions, diagnostic samples, path exclusions, control results and
second-pass measurements. The [reproduction harness](quality-evidence/measure-booster-rules.py)
runs the primary baseline and candidate comparison against disposable clean
Git checkouts pinned to the exact recorded revisions. It verifies each checkout
HEAD and rejects tracked modifications or untracked files before probing; the
inventory enumerates only Git-tracked PHP paths, so ignored/generated PHP does
not enter revision-labelled evidence.

| Repository | Exact default-branch snapshot |
| --- | --- |
| ran-booster | [`51613e42df959b76795a1b438de59a06053fb614`](https://github.com/RocketsAreNostalgic/ran-booster/tree/51613e42df959b76795a1b438de59a06053fb614) |
| ran-booster-bitbucket | [`95c6b760acfdb75961ea9e1b76610a864c16b048`](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/tree/95c6b760acfdb75961ea9e1b76610a864c16b048) |
| ran-booster-github-provider | [`ebeb6166b9806b006f1224fa5b291473040a0b86`](https://github.com/RocketsAreNostalgic/ran-booster-github-provider/tree/ebeb6166b9806b006f1224fa5b291473040a0b86) |
| ran-booster-wp-pusher-migrator | [`23ac6e35e8a521bfc5c4b2bc7a53698ec7df36c2`](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/tree/23ac6e35e8a521bfc5c4b2bc7a53698ec7df36c2) |
| ran-updater-support | [`d395c37b2a76e5a5e10d9855b3277cde1cec4df3`](https://github.com/RocketsAreNostalgic/ran-updater-support/tree/d395c37b2a76e5a5e10d9855b3277cde1cec4df3) |
| ran-wp-branch-updater | [`15253ac03878b01da254d6702a9753103354d8e9`](https://github.com/RocketsAreNostalgic/ran-wp-branch-updater/tree/15253ac03878b01da254d6702a9753103354d8e9) |
| ran-wp-release-updater | [`78f30caac2384e6c91188ba780aadc8af2f6fdd4`](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/tree/78f30caac2384e6c91188ba780aadc8af2f6fdd4) |

The snapshots were refreshed before execution. Release Updater and Migrator
have newer defaults than the initial nine-repository matrix; these results are
bound to the revisions above, not to moving branches or active PR heads.

Execution used PHP 8.4.23 and the common locked PHPCS 3.13.6, WPCS 3.4.1,
RAN standard `0b03e61a4bb558deeb6bc6b6399f44c0ec95e5be`, and matching PHPCSUtils,
PHPCSExtra and PHPCompatibility packages. All eight relevant tool package
versions/references were compared against every consumer lock. The external
tool-only installation supplies the sniffs; consumer dependencies, application
code, Composer scripts and host integrations were not executed.

For the primary candidate, remove only the local disabled severity/exclusions
for `WordPress.NamingConventions.ValidFunctionName.MethodNameInvalid`,
`WordPress.NamingConventions.ValidVariableName` and `WordPress.PHP.YodaConditions`.
Keep other local rules and source selection. Set the existing generic assignment
alignment sniff's `error` property true and the WordPress array-alignment rule's
type to error. Run PHPCS selecting those five sniff families; measure alignment
and Yoda PHPCBF passes independently from restored snapshots. The broader
exception probe separately enables just the three named recurring rule families.

Reproduce the primary measurements with the seven exact tracked source trees
under a disposable directory, a PHP binary and the matching registered tool
installation:

```sh
python3 quality-evidence/measure-booster-rules.py /tmp/booster-audit /path/to/php /path/to/vendor
```

Use full tracked trees, including tests, rather than an export-ignore-pruned
release archive. Raw local logs are not committed. No result here certifies PHP
8.2/8.5 execution, semantic equivalence of future renames/condition edits,
all-estate CI success, or code excluded by current file/inline policy.
