# RAN release-trust policy

## Purpose

Rockets Are Nostalgic repositories do not need identical release workflows. They do need the same release-trust guarantees wherever those guarantees apply.

This policy defines the organisation-level trust invariants for repositories that can create or modify release pull requests, tags, GitHub releases, published build artifacts, WordPress.org deployments, package-registry publications, or equivalent privileged repository state.

The governing principle is:

> Same release-trust guarantees where applicable; not necessarily the same release architecture.

Repository-specific gates may be stronger than this policy and should remain local when they prove product-specific properties. Shared quality infrastructure is evidence infrastructure, not automatically release authority.

This policy is maintained under the organisation-wide audit in RocketsAreNostalgic/.github#9. Source-quality profile adoption and reusable quality-workflow rollout remain separately owned by RocketsAreNostalgic/.github#7.

### Deterministic test fixtures

The existence of a GitHub release workflow does not by itself make a repository a production release-trust target.

Repositories whose published releases exist solely as deterministic test fixtures are a justified difference when their release state is test data rather than production distribution, production dependency identity, or independent release-authority evidence. Their relevant invariant is that the fixture state is deliberate, reproducible, and matched by the consuming test suite.

A fixture may therefore intentionally model behaviour that would be inappropriate for a production publisher, including mutable release assets, weaker admission settings, unusual release history, or other controlled failure/recovery states. The organisation should not harden those characteristics merely for consistency when doing so would change the behaviour the tests are meant to exercise.

A fixture repository enters the production release-trust audit only when its published state is also used as one of the following:

- production distribution;
- production dependency or package identity;
- trusted evidence that authorizes real privileged repository or publication mutation.

If a fixture crosses one of those boundaries, audit the production use separately from its fixture role rather than treating the test fixture label as a blanket exemption.

## Vocabulary

### Evidence

Evidence is a result that qualifies a specific source revision or artifact for a later decision. Examples include source-quality checks, package tests, runtime archive verification, compatibility checks, install readback, and release-candidate validation.

Release-relevant evidence should:

- execute against the exact source revision being qualified;
- use locked dependency manifests where applicable;
- use appropriately pinned third-party Actions and toolchains;
- use read-only or otherwise minimal permissions when mutation is not required;
- never execute untrusted pull-request head code through a privileged `pull_request_target` path;
- distinguish untrusted PR qualification from trusted `main` or release qualification;
- fail closed when the expected source identity cannot be established.

A reusable quality workflow may produce baseline evidence. That does not make it a release publisher.

### Evidence inputs

Evidence inputs are files or facts whose change can invalidate existing evidence and therefore require fresh qualification. Typical examples include:

- `composer.json` and `composer.lock`;
- `package.json` and package-manager lock files;
- source and build inputs;
- runtime packaging manifests;
- generated-runtime manifests or dependency selections;
- source-quality configuration when it materially changes the qualification contract.

Evidence inputs are not automatically privileged release authority. A dependency manifest can require new evidence without gaining the authority to decide whether repository write permissions may be exercised.

### Release control

Release control is code or configuration that decides whether privileged release mutation is allowed. Typical examples include:

- release workflows;
- publisher or reconciliation scripts;
- release-candidate admission logic;
- logic that decides whether write permissions may be exercised;
- configuration governing release mutation or promotion.

Changing release control can require a stronger approval or promotion boundary than changing ordinary evidence inputs. Repositories should not collapse evidence inputs and release control into one generic list unless they genuinely require identical treatment.

### Privileged mutation

Privileged mutation is any action that changes trusted repository or publication state, including:

- opening or modifying release pull requests with write authority;
- creating or moving tags;
- creating, editing, publishing, or deleting GitHub releases;
- uploading or replacing release assets;
- publishing to WordPress.org or another package/deployment registry;
- modifying equivalent privileged release state.

Privileged mutation must be separated from untrusted PR-head execution. A privileged mutator should consume already-qualified exact evidence rather than treating possession of write credentials as permission to run arbitrary candidate code and decide its own quality.

### Artifact provenance

Artifact provenance is the proof that the bytes published are the bytes that were qualified for the exact release candidate.

For repositories that publish separately built artifacts, the release path should, as applicable:

- build against the exact qualified revision;
- bind artifact metadata to the candidate commit, tag, and version;
- verify a cryptographic digest;
- verify the expected file or asset set;
- carry the tested artifact across the publication boundary rather than silently rebuilding different bytes;
- verify the final tag and release target after publication;
- read back the published asset set and relevant digests;
- use immutable publication when the repository's release model supports it.

Source-only or library releases may legitimately have no separate packaged artifact. In that case exact source, tag, release-target, and publication identity are the relevant provenance chain.

### External approval or promotion

An external approval or promotion boundary is an authorization mechanism that is not controlled solely by the release-control code being changed in the same repository revision.

Examples can include:

- appropriately configured repository rulesets or path-scoped reviewers;
- protected environments with required reviewers;
- an equivalent independently configured policy mechanism.

Use such a boundary when independent authorization is actually intended. Do not simulate an independent principal with a ceremonial follow-up pull request or a repository-controlled self-deferral state machine when no independent principal exists.

A repository is not required to add a human or external approval step merely for consistency. The need for independent authorization is an architectural decision based on the authority being protected.

### Repository-specific stronger gates

Product-specific proofs remain owned by the repository that understands them. Examples include:

- Booster runtime-archive composition and dependency-surface policy;
- WordPress.org deployment contracts;
- updater runtime-copy selection;
- package-specific concurrency, race, hard-stop, or installation proofs;
- release-candidate install readback.

The organisation policy defines common trust properties. It does not replace stronger local contracts.

## Required trust invariants

### 1. Exact identity

Release-relevant evidence and privileged publication must be bound to an exact revision or candidate identity.

A release path must fail closed rather than infer identity from a floating branch when exact identity is required. If evidence was produced by another workflow or job, the publisher must establish that the evidence belongs to the exact candidate it is about to publish.

### 2. Minimal evidence authority

Quality and evidence-production jobs should be read-only unless mutation is part of the evidence contract itself and cannot reasonably be separated.

Pull-request qualification must not give untrusted PR-head code release-write credentials. `pull_request_target` must not be used to execute untrusted head code with privileged authority.

### 3. Separated mutation

Write authority should live in a bounded publication or reconciliation path. The mutator should verify the successful evidence and exact candidate before exercising that authority.

A successful PR check and a successful trusted-main qualification are different facts. Repositories may rely on one or both, but the release architecture must state which one actually admits publication.

### 4. Release-control changes

Repository-controlled CI cannot be treated as an independent reviewer of changes to its own release authority.

Where independent authorization is required, release-control changes must cross an independently enforced boundary before the changed control can authorize privileged mutation.

Where independent authorization is not required, the repository may use exact trusted-main qualification as its release boundary, provided this is an explicit accepted model rather than accidental self-approval presented as independence.

Existing safeguards should not be removed until the guarantee they provide has been replaced.

### 5. Artifact identity and publication

Repositories publishing build artifacts must prove the identity of the published bytes across build, transfer, and publication boundaries.

If a repository permits rebuilding or replacing assets for an existing tag, that must be an explicit recovery contract. It must preserve exact source/tag identity, re-run the repository's required artifact proofs, and read back the resulting publication. Mutable recovery is not equivalent to immutable provenance and must be documented as a deliberate exception where retained.

Where immutable GitHub releases are compatible with the release model, prefer them and verify immutability after publication. A repository that deliberately retains mutable recovery must record why immutability would remove a required operational capability and what compensating provenance/readback guarantees apply.

### 6. Repository settings and bypasses

The audit must consider the effective repository settings that underpin the claimed release model, including:

- required pull requests;
- strict required status checks;
- required review-thread resolution;
- required reviewers where used;
- allowed merge methods where they affect identity assumptions;
- bypass actors;
- protected environment rules where used.

A bypass is a release-trust defect when it defeats a boundary the release architecture claims to rely on. It is not automatically a release-trust defect when release admission occurs later through a separate exact trusted-main qualification that the bypass does not skip.

Checked-in release control and effective repository settings must agree. If a publisher requires a bypass-free ruleset, the live ruleset must satisfy that requirement; deleting the publisher's fail-closed check is not an acceptable substitute unless the trust model is deliberately redesigned and documented.

### 7. Third-party action and toolchain identity

Third-party Actions used in release-relevant evidence or privileged mutation should be pinned to immutable commit SHAs. Human-readable version comments may accompany the SHA.

Toolchains and package managers should use exact or appropriately locked versions where drift could change release evidence or artifact output.

### 8. Readback and reconciliation

Publication is not complete merely because a create/upload command returned success.

Where applicable, the publisher should read back and verify:

- tag target;
- release target and draft/published state;
- immutable state where required;
- expected asset names;
- artifact digests or manifest identity;
- downstream publication identity, such as a WordPress.org deployment contract.

Recovery and retry paths must preserve the same identity guarantees as the normal path.

## Accepted architectural patterns

### Source/library release

A source-only library can use:

```text
read-only exact-revision CI
→ successful exact trusted-main qualification
→ bounded write-scoped publisher
→ exact tag/release target verification
→ immutable release/readback where supported
```

It does not need WordPress-plugin ZIP provenance if no separately built ZIP is published.

### Packaged application or plugin release

A packaged release can use:

```text
exact source qualification
→ artifact build
→ artifact identity/digest evidence
→ bounded publisher consuming the exact tested artifact
→ tag/release verification
→ asset readback
→ immutable publication where compatible
→ downstream deployment from the canonical published artifact
```

Repository-specific build and install proofs should remain local.

### PR-evidence promotion

A repository may qualify an exact PR candidate and later promote that evidence, provided the publisher proves the relationship between the merged candidate and the successful evidence and the effective repository settings preserve the assumptions on which that proof relies.

### Trusted-main promotion

A repository may instead treat successful exact `main` qualification as the release gate. In that model a PR-level bypass does not automatically bypass release evidence, because publication still waits for the separately qualified exact `main` revision.

This model is not an independent review of changed release control. If independent authorization for release-control changes is required, add an external boundary rather than describing trusted-main self-qualification as independence.

## Shared workflow boundary

Organisation-owned reusable quality workflows should remain generic, read-only quality infrastructure unless a separate architectural review establishes a reusable publisher with an appropriate authority model.

Do not move product-specific publication or trust boundaries into shared quality workflows merely for consistency. In particular, generic quality workflows should not own:

- Booster archive provenance;
- WordPress.org publication;
- updater runtime-copy selection;
- package-specific hard-stop or race tests;
- repository-specific release admission or mutation policy.

Consumers should pin reusable workflow identity where practical. Consumer-owned specialist gates remain consumer-owned.

## Audit disposition

Each release-enabled repository must receive one explicit disposition:

- **CONFORMS** — the applicable release-trust invariants are satisfied;
- **JUSTIFIED DIFFERENCE** — the implementation differs from a common pattern but provides equivalent applicable guarantees, with the reason recorded;
- **REMEDIATION REQUIRED** — a concrete trust guarantee is missing or contradicted by current repository state; an owning-repository issue must track it;
- **UNKNOWN — MORE EVIDENCE NEEDED** — current evidence is insufficient to make a defensible classification.

Difference alone is not a finding.

## Audit questions

For each repository, establish at least:

- What creates or modifies release PRs, tags, releases, assets, deployments, or registry state?
- What trigger enters the privileged path?
- Which jobs receive write permissions or publication credentials?
- Can PR-head-controlled code receive those credentials?
- What exact source identity is qualified?
- What proves that privileged publication consumes that successful qualification?
- Where are release artifacts built?
- What binds those bytes to the source candidate?
- What digest and file-set checks exist?
- What is read back after publication?
- Are releases immutable, and if not, what explicit recovery model requires mutability?
- Are third-party Actions pinned?
- What effective ruleset and bypass actors apply?
- Does any bypass defeat a boundary the publisher relies on?
- Is independent approval or promotion intended, and if so, what external mechanism enforces it?
- What specialist repository gates must remain local?

## Relationship to source quality

`.github#7` owns shared quality-profile adoption, shared coding/config packages, reusable read-only quality workflows, source-quality migration, terminal quality fan-in, and staged quality enforcement.

`.github#9` and this policy own release authority, privileged mutation, release-control paths, exact release-candidate identity, artifact provenance, publication/readback, repository bypass policy where it affects release trust, and independent authorization boundaries.

When an audit finds a quality-profile adoption problem rather than a release-trust problem, track it under `.github#7` rather than expanding the release-trust remediation.

## Maintenance

When a release architecture changes materially, reassess the repository against this policy and update the organisation ledger in `.github#9`.

Do not weaken a stronger repository-local gate merely to match the organisation minimum. Do not add ceremony that provides no additional guarantee for the repository's actual release model.
