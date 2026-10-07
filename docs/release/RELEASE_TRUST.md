# RAN release-trust policy

## Find the release requirement

| Task | Read |
| --- | --- |
| Review release authority | [Terms](#vocabulary), [invariants](#required-trust-invariants), [manual dispatch](#privileged-manual-dispatch-authority). |
| Classify release-driving changes | [Release classification](#release-classification). |
| Implement or operate a publisher | [Profile A](RELEASE_PROFILE_A.md) for source releases; [Profile B](RELEASE_PROFILE_B.md) for tested-asset promotion and recovery. |
| Find current evidence or owner decisions | [#47 implementation](https://github.com/RocketsAreNostalgic/.github/issues/47), [#57 acceptance](https://github.com/RocketsAreNostalgic/.github/issues/57), [#59 immutability/settings](https://github.com/RocketsAreNostalgic/.github/issues/59). |

## Purpose

Apply equivalent release-trust guarantees wherever repositories can mutate release
PRs, tags, releases, assets, deployments or package publications. Release Please
owns version, changelog, release PR, tag and release lifecycle; Profile B adds exact
tested-asset promotion. Do not duplicate those mechanisms locally. Stronger
product-specific evidence remains required.

Implementation merged, package published, consumer adopted, installed composition
qualified and owner acceptance complete are separate facts. This policy supplies
no merge, publication or acceptance approval.

### Deterministic test fixtures

A release used solely as deliberate, reproducible test data may intentionally
model mutable assets, weaker admission or failure/recovery history. Preserve the
behaviour its consuming tests require. Audit a fixture's production use separately
if its releases also supply production distribution, dependency/package identity,
or evidence authorizing real privileged mutation; “fixture” is not a blanket exemption.

## Vocabulary

- <a id="evidence"></a>**Evidence** qualifies an exact source revision or artifact: source, package,
  compatibility, archive, installation or release-candidate checks.
- <a id="evidence-inputs"></a>**Evidence inputs** include source/build files, dependency manifests and locks,
  packaging/runtime manifests and material quality configuration. Changes require
  fresh qualification; these inputs do not automatically confer mutation authority.
- <a id="release-control"></a>**Release control** decides whether mutation is allowed: workflows, publishers,
  reconciliation/admission logic and promotion configuration. Its approval boundary
  may be stronger than ordinary evidence-input review; do not conflate them.
- <a id="privileged-mutation"></a>**Privileged mutation** changes trusted PR, tag, release, asset, deployment or
  registry state. Credentials alone do not authorize candidate code to qualify itself.
- <a id="artifact-provenance"></a>**Artifact provenance** proves the published bytes are the bytes qualified for
  the exact candidate. Source-only releases instead bind source, tag and release identity.
- <a id="external-approval-or-promotion"></a>**External approval/promotion** is enforced outside the changed release-control
  revision, for example independent ruleset reviewers, protected-environment
  reviewers or a credential broker. Add it when the architecture requires independent
  authorization, not merely to make repositories look alike.

## Required trust invariants

### 1. Exact identity

Bind evidence and publication to an exact revision/candidate; fail closed when
identity cannot be established, rather than inferring it from a floating branch.
Use locked dependency manifests where applicable. Evidence supplied by another
workflow must match the expected repository, workflow, event, conclusion, branch
and SHA; a status name is insufficient.

### 2. Minimal evidence authority

Evidence jobs should be read-only unless their evidence contract necessarily
requires mutation. Production release workflows start with `permissions: {}` and
grant only necessary job scopes. Check out the admitted SHA without persisted
credentials and verify identity before executing release-controlled code.
Never give untrusted PR-head code release-write credentials or execute it through
privileged `pull_request_target`.

### 3. Separated mutation

A bounded publisher verifies successful exact evidence before exercising write
authority. Release Please's release-PR reconciliation is not evidence for tag,
release, asset or deployment mutation. PR qualification and trusted-main
qualification are different facts; state which admits publication.

### 4. Release-control changes

Repository-controlled CI is not an independent reviewer of its own authority.
Where independence is required, changed control must cross an independently
enforced approval boundary before authorizing mutation. Otherwise, an explicitly
accepted exact trusted-main model is valid; do not describe it as independent
approval. Retain existing safeguards until their guarantees have been replaced.

### 5. Artifact identity and publication

Build against qualified source; bind metadata to commit, tag and version; verify
the complete expected asset set and cryptographic digests; promote the tested
bytes across the publication boundary. Privileged rebuild, post-test patch or
repack is not a substitute. Source-only releases need no artificial ZIP proof.

Production GitHub releases are immutable. Correct a build using freshly qualified
source and a new version/tag. A mutable exception needs narrow evidence and an
owner decision in [#59](https://github.com/RocketsAreNostalgic/.github/issues/59);
historical recovery code is not a standing exception.

### 6. Repository settings and bypasses

Inspect effective required PRs, strict checks, resolved review threads, reviewers,
merge methods, bypass actors and protected environments where applicable. Source
control and live settings must agree. A bypass is a defect when it defeats a
claimed boundary; a later independent exact-main admission may still protect
publication. Do not remove a fail-closed settings check to conceal a mismatch:
any redesign of the trust model must be deliberate and documented.

### 7. Third-party action and toolchain identity

Pin release-relevant third-party Actions to immutable SHAs; version comments are
optional. Pin or lock toolchains/package managers where drift could affect
evidence or artifacts. Pin reusable workflow identity where practical.

### 8. Readback and reconciliation

A successful API mutation is not completed publication. Verify actual tag target,
release target/state, required immutability, expected asset names and digests or
manifest identity, and enabled downstream publication identity. Retries and
recovery preserve the same guarantees. Downstream deployment uses the canonical
published artifact; disabled optional WordPress.org deployment cannot block
canonical qualified GitHub publication.

### Privileged manual dispatch authority

`workflow_dispatch` executes the selected branch/tag's workflow definition.
An inline `github.ref == 'refs/heads/main'` guard contains accidents; it cannot
independently constrain a principal able to author and execute another revision.
Record the accepted model for each production write-capable dispatch path:

1. **Independent authority:** a distinct principal/policy outside that workflow
   revision enables mutation, and its author cannot unilaterally change or satisfy it.
2. **Single trusted release principal:** protected/default-branch promotion plus
   exact qualification is the intended boundary; the trusted principal can also
   authorize manual mutation.

Neither ordinary review, an inline guard nor an Environment-scoped secret alone
proves independence. Do not invent a second account, ceremonial approval PR or
self-deferral state machine to claim it. Both models retain least privilege,
exact source/artifact identity and readback. Keep historical/release-controlled
code away from fresh write authority where practical; contract-test the trusted-ref
guard when the operational path is the protected default branch.

Adding a guard only to current `main` does not neutralize older dispatchable refs
at the same workflow path. Prove those refs cannot dispatch or neutralize them
without rewriting release history. An accepted pattern moves current guarded
control to a new path absent from historical refs, removes the old default-branch
path and contract-locks that absence. Source absence alone is not a live platform
proof of dispatch neutralization.

## Accepted architectural patterns

### Source/library release

Read-only exact-source qualification → bounded publisher → exact tag/release and
immutable readback. No separate artifact provenance is required without a built asset.

### Packaged application or plugin release

Add exact build/asset-digest evidence and tested-artifact transfer before bounded
publication/readback. Keep product construction and install proofs local.

### PR-evidence promotion

Prove the relationship between the merged candidate and successful PR evidence,
with effective repository settings preserving that proof's assumptions.

### Trusted-main promotion

Exact trusted-main qualification may admit release independently of PR-level
checks. It does not independently authorize changed release control.

### Exact candidate versus latest `main`

Publishing a qualified earlier candidate after a newer ordinary main commit is
valid where the local contract permits it, with exact identities and unambiguous
release ordering. A contract requiring continued tip identity must prove it.
Read-then-write preflight is neither atomic compare-and-swap nor an independent
boundary against concurrent pushes. Profiles A/B specify their actual tip requirements.
Runner provider is not a semantic invariant: GitHub-hosted Ubuntu 24.04 and the
approved Blacksmith Ubuntu 24.04 runner are acceptable. Provider changes are
trust/operations decisions, not cosmetic consistency work.

### Repository-specific stronger gates

Generic shared quality workflows remain read-only evidence infrastructure unless
separately reviewed as publishers. Do not absorb product release authority merely
for consistency: Booster archive/dependency proofs, WordPress.org contracts,
updater runtime-copy selection, concurrency/race/hard-stop tests and installation
or release-candidate readback remain consumer-owned. Common minimums do not
justify weakening stronger local checks or retaining retired generic lifecycle engines.

### Read-only release liveness

The observer covers only the caller's current root Release Please manifest.
`published` requires one exact merged non-abandoned candidate, matching final
tag/non-draft release and settled `autorelease: tagged`; `reconciled` requires the
separate `release: reconciled` marker with no final tag/public release or
contradictory pending/tagged label, plus a repository-local explanation. Drafts
alone are nonterminal. Grace and exact-SHA active publisher runs defer negative
verdicts; stable stale candidates are stranded. Identity conflicts, abandoned or
ambiguous candidates, API errors and overdue unsettled published labels fail closed.

The observer is read-only; it neither mutates labels nor certifies historical
manifests, asset bytes/digests, immutability, deployment or monitoring cadence.
Historical dispositions belong in [#29](https://github.com/RocketsAreNostalgic/.github/issues/29)
and [#57](https://github.com/RocketsAreNostalgic/.github/issues/57).

Implementation and cases: [current workflow](../../.github/workflows/release-liveness-observer.yml)
and [tests](../../quality-enforcement/test-release-liveness-observer.py);
inspected [workflow](https://github.com/RocketsAreNostalgic/.github/blob/70df865a00734542e6bb663e684d86b8b4757b8e/.github/workflows/release-liveness-observer.yml)
and [tests](https://github.com/RocketsAreNostalgic/.github/blob/70df865a00734542e6bb663e684d86b8b4757b8e/quality-enforcement/test-release-liveness-observer.py).
That revision supports the description, not a guarantee about future code.

## Release classification

### Applicability

Where Conventional Commit metadata drives release significance and PR-controlled
subjects survive into consumed commits, those subjects are release metadata.
Other release models may document a justified difference but still require
intentional, reviewable release metadata.

Each repository owns release-driving types, dependency/breaking-change semantics
and compatible merge methods. Configuration, documentation, tests and effective
merge settings must agree. A release-significant effect—production dependency,
runtime, packaged bytes, API or compatibility change—must use a recognized visible
classification or supported explicit breaking marker, even when implemented as
an internal refactor. Do not impose one organisation-wide type list.

### PR-derived final commit requirements

1. Review the metadata that actually survives the configured merge; preserving
   individual commits changes its source, not the requirement.
2. For mechanically identifiable release-significant changes, CI must fail closed
   on hidden/non-driving subjects unless a supported breaking marker applies.
   Where reliable checking is impractical, document the justified difference and
   the review step owning that decision.
3. Derive permitted types from local release configuration where practical.
4. Invalidate and rerun checks when their mutable PR metadata changes. An earlier
   green check cannot qualify a later title. Editing a title after merge does not
   repair the created commit; use normal reviewed recovery, never protected-history
   rewriting or manual tags/releases.

### Automation boundary

Classification is read-only evidence, not mutation authority. Checks may inspect
PR subjects, exact base/head revisions, paths/manifests and release configuration.
Share helpers only for genuinely common semantics; retain product-specific rules
locally. Release Please owns the release lifecycle; classification checks must
not duplicate that machinery.

### Dependency changes

State release-driving dependency policy in configuration and validation; comparing
the exact base/head Composer `require` maps is one possible check. Development-only
dependencies do not automatically drive releases merely by sharing a manifest.

### Examples

| Local policy/effect | Valid interpretation |
| --- | --- |
| Production adoption drives releases and `deps:` is visible | Use `deps: adopt dependency`; hidden `refactor:` does not describe its release significance. |
| Internal test reorganisation crosses no release-driving boundary | Hidden `refactor:` may be appropriate. |
| Breaking syntax is supported | `refactor!: replace runtime contract` can drive release despite hidden base type. |
| A checked `deps:` title becomes hidden `refactor:` before merge | Rerun classification evidence. |
| Repository deliberately treats dependency-only changes as hidden | No mandatory `deps:` visibility; classify any separately release-significant effect appropriately. |

A green “no user facing commits” result proves metadata was applied, not that its
classification was correct. Reassess metadata after merge-method, release-tool,
type or dependency-policy changes.

## Audit disposition

Review triggers and mutation paths, job credentials, untrusted-code exposure,
source/evidence identity, artifact build/transfer/digests, readback/recovery,
immutability, pinned dependencies, effective settings/bypasses, intended approval
independence and stronger local gates against the invariants above. Record one outcome:

- **CONFORMS:** applicable guarantees satisfied.
- **JUSTIFIED DIFFERENCE:** different implementation, equivalent guarantees and reason recorded.
- **REMEDIATION REQUIRED:** concrete missing/contradicted guarantee with an owning-repository issue.
- **UNKNOWN — MORE EVIDENCE NEEDED:** insufficient current evidence.

Difference alone is not a finding.

## Maintenance

Material release-architecture changes require reassessment and an update to
[#9](https://github.com/RocketsAreNostalgic/.github/issues/9). Update the affected
mechanism documentation/evidence in the same PR where practical; otherwise record
an explicit cross-repository follow-up. Unrelated commits require no blanket refresh.
Route quality adoption to [#65](https://github.com/RocketsAreNostalgic/.github/issues/65),
not release-trust remediation. [#31](https://github.com/RocketsAreNostalgic/.github/issues/31)
retains deferred organisation enforcement; current repository-required checks remain
authoritative. Release completion does not complete separate quality acceptance.
