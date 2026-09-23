# Support naming pilot preview

Owner: [.github#65](https://github.com/RocketsAreNostalgic/.github/issues/65#rollout-plan-and-agent-handoffs),
with [Support#35](https://github.com/RocketsAreNostalgic/ran-updater-support/issues/35),
[Branch#59](https://github.com/RocketsAreNostalgic/ran-wp-branch-updater/issues/59)
and [Release#60](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/issues/60).

This is a runnable preparation artifact. It produces candidate file copies from
the exact Git commits in `manifest.json`. It does not edit checkouts, install
dependencies, run application code, change locks, or create releases. The active
command/release lanes keep ownership until their recorded handoffs.

## Run

Requirements: PHP 8.2+, Git, local clones containing the three recorded commits;
Python 3 for the tool's tests. No Composer packages are needed by this tool.

```sh
php quality-tools/support-naming/preview.php \
  quality-tools/support-naming/manifest.json \
  /path/to/parent-of-the-three-repositories /tmp/support-preview

python3 quality-tools/support-naming/test_preview.py /path/to/php
```

The output directory must be new and outside all three input repositories. It
contains only the ten proposed changed files plus `preview.json`, not runnable
complete packages. Repeat using a different new output directory; identical
inputs produce identical file bytes. Existing output is never overwritten.

The tool reads pinned Git objects, including files excluded from distribution
archives. It ignores uncommitted working-tree contents. It validates source
hashes, commit object types, expected replacement counts, token-kind spelling,
destination identifier collisions and normalized path boundaries before creating
output. Literal mappings are validated together and cannot overlap or cascade.
Case-folded target aliases are rejected conservatively on every host; files are
created exclusively to prevent filesystem aliases from overwriting output. A validation failure creates no output.
An I/O failure during output creation can leave an incomplete disposable output;
discard it and rerun into a new directory.

**This is not a current-main freshness check.** It deliberately reproduces a
historical candidate. At the real handoff, refresh main and open work, repeat
caller discovery and review the manifest against the handed-over revisions.
Do not simply copy this preview onto a newer branch or advance commit hashes
without reviewing its file hashes, mappings, counts and generated prerequisites.

## Snapshot refresh — 23 September 2026

The manifest now pins the qualified command/rules handoffs:

| Repository | Commit |
| --- | --- |
| Support | `fb7e07a2c7d6fa3a8a690c0ccbe5199c490db6ee` |
| Branch Updater | `e1bc02eb06b0a435f3e2f9e107aa25e91c3150bb` |
| Release Updater | `26b81a7b05d42e76268eb6b7de17de91989d2aa4` |

Handoff evidence is recorded in Support #35, Branch #59 and Release #60, linked
above. The three default branches and open PRs were inspected before this refresh.
Support's open #31 concerns release-observer CI; Branch and Release had no open
PRs. This records the observed boundary, not ownership of those release workflows.

All selected source files, mappings, counts, locks and generated prerequisites
remain byte-identical to the earlier pins. Only the guarded Support and Branch
`composer.json` files changed, through the already-qualified canonical command
updates. Their diffs were reviewed before refreshing their hashes.

Both the historical and refreshed manifests passed the preview guards on PHP
8.4.23. All ten emitted candidate files are byte-identical between those runs:
49 identifier-token edits and 11 literal replacements remain the complete preview
scope. This refresh did not rerun application suites or regenerate the two derived
outputs. Earlier disposable composition evidence below remains historical;
implementation must qualify the actual candidate and its installable dependencies.
Recheck heads, callers and lane ownership again before applying any source change.

## Reviewed scope

| Owner | Before | After |
| --- | --- | --- |
| ArchiveSafety | `normalizePath` | `normalize_path` |
| ArchiveSafety | `entryTypeFailure` | `entry_type_failure` |
| ArchiveSafety | `collisionFailure` | `collision_failure` |
| RepositoryRelativePath, private | `assertDecodedSegmentIsSafe` | `assert_decoded_segment_is_safe` |

The manifest also renames seven file/scoped variable groups: `originOs`,
`entriesByPath`, `previousPath`, `previousDirectory`, `firstSegment`,
`repositoryPaths` and `pathBytes`. It restores Support's method/variable naming
checks and removes the obsolete policy comment, preserving all other rules.
The public parameter `originOs` becomes `origin_os`; caller named arguments are
part of the breaking API change even though positional calls remain valid.

There are **49 identifier-token edits in seven PHP files**, plus **11 explicitly
reviewed literal replacements**: eight API/example occurrences in Support's
README, two executable calls inside Release's no-dev nowdoc, and one obsolete
Support ruleset block. That is ten candidate files before derived outputs.
The generated ArchiveSafety class and runtime-copy metadata bring the eventual
bounded candidate to twelve files, before separately reviewed dependency pins
and release metadata. These are measured edits, not an estimate for Core.

PHP identifiers use reviewed per-file token mappings against exact source
hashes. This is deliberately not a general symbol resolver. Strings, comments
and data keys do not change merely because their text resembles an identifier.
The separate literal entries give a reason and expected count for every
approved non-token edit. Review the manifest itself as executable change intent.

Two caller details require that separate treatment:

- Support's README has the public `originOs:` named argument.
- Release's `tests/Integration/no-dev-consumer.php` stores executable PHP in a
  nowdoc, with `$archiveClass` bound to the generated ArchiveSafety class.
  Ordinary AST/static-call collection can miss both embedded calls.

The suite search also finds unrelated private `normalizePath` methods in Core's
LocalDataRemover, LocalTroubleshootingService and SecretsStorageProvisioner.
Those are different symbols and remain outside this manifest. There were no
additional matches in the audited Provider/Bitbucket/Migrator snapshots; this
is not proof about private workbench code or all downstream installations.

## Qualify a disposable composition

Use complete tracked-file copies/checkouts at the recorded revisions, not
distribution archives: export exclusions omit some tests. Apply the preview
copies only inside those disposable packages.

1. Install Support's locked tools and run its existing `standards:fix` twice,
   then full `composer check`. Verify the second fix is stable and no naming
   findings remain. Execute the README example to cover its named argument.
2. Install Branch/Release's locked tooling. In these disposable compositions
   only, overlay the exact preview Support source/fixture corpus into the
   installed Support package. This is candidate-composition testing, **not**
   proof that the unchanged consumer locks resolve a newly released API.
3. In Release, run `php scripts/sync-updater-support.php`, then the same command
   with `--check`. Never edit `src/Dependency/ArchiveSafety.php` by hand.
4. Recompute only `runtime-copy.json.package_revision` using Release's existing
   identity contract: sort `bootstrap.php`, `runtime.php` and every production
   `src/**/*.php` relative path; concatenate `path + NUL + SHA256(bytes) + LF`;
   SHA256 that payload. Preserve package version, runtime protocol and floors.
   The generated source and metadata are derived outputs, not literal renames.
5. Run Branch's contract/archive/prepared-archive tests, Release's generated
   dependency and runtime identity tests, and its installed no-dev consumer
   test. Search all three candidate trees for leftover old target references,
   preserving deliberate historical records and unrelated symbols.

The real implementation must then use installable immutable dependency pins,
truthful beta breaking-change classification, the new owned-method check when
its reviewed package is available, full required repository/host/WordPress/
Windows CI and exact-head independent review. Do not ship an overlay, invent a
released version, weaken a runtime hash check, or expand an active Profile B PR.

## Recorded rehearsal

On 22 September 2026, the pinned candidate was exercised with PHP 8.4.23 and
Node 24.11.0:

- Thirteen preview-tool tests passed, including exact-token/data preservation,
  pinned-object reads despite a dirty worktree, bad hashes/counts, identifier
  collisions, commit-object verification, token-kind spelling, case aliases,
  literal overlap/cascade refusal, normalized Windows path keys and nested
  containment. Windows path normalization is a portable function test, not a
  claim of a native Windows execution. The hardened preview reproduces all ten
  original candidate files byte-for-byte.
- Support's full existing `composer check` passed with naming suppressions
  removed, including level-8 analysis and release-control tests. Both PHPCBF
  passes exited zero and changed no bytes. PHPStan reported a nonfatal optional
  turbo-extension loading warning in the portable PHP runtime, then no errors.
- Branch's contract, archive-normalisation and prepared-archive tests passed
  against the preview Support source.
- Release sync/check passed; ArchiveSafetyDependencyTest passed 71 assertions.
- Release's real archive-validator delegation test passed 26 assertions. The
  opt-in owned-method check also reports zero errors on preview Support source.
- Support's README example executed successfully, including `origin_os:`.
- The no-dev bootstrap initially rejected the renamed runtime with its old
  content hash. The missing derived update was identified and the exact
  runtime identity recomputed; the identity assertion and installed no-dev
  consumer bootstrap then passed. This is why
  metadata refresh is an explicit prerequisite above, not a bypass.

See the PR/owning issue for the current handoff state.
This rehearsal is not full three-repository CI, release qualification, or merge
authority. No application branch, lockfile, certification pin or fixture script
interface was changed by this preparation.
