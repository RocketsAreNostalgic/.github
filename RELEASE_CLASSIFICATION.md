# RAN release-classification policy

## Purpose

Rockets Are Nostalgic repositories may use different release architectures, merge methods, and changelog rules. Where release automation derives versioning or changelog significance from Conventional Commit metadata, however, the metadata that survives the merge must faithfully represent the repository's own release policy.

This policy defines that organization-level invariant without imposing one universal list of release-driving commit types.

## Applicability

This policy applies when all of the following are true:

- a repository uses Release Please or equivalent automation that derives release significance from Conventional Commit metadata;
- pull requests may be squash-merged, or another merge method causes the pull-request title to become the final commit subject consumed by release automation;
- the repository distinguishes release-driving classifications from hidden or non-release-driving classifications.

Repositories with a different release model may document a justified difference. The relevant invariant is that release significance is derived from deliberate, reviewable metadata rather than accidentally from a presentation-only title.

## Core invariant

When the pull-request title becomes the commit subject consumed by release automation, the title is **release metadata**.

If a change satisfies that repository's release-driving criteria, the final squash title must use a release-driving Conventional Commit classification recognized by that repository's release configuration, or an explicit breaking-change classification where supported.

A hidden type such as `refactor:`, `chore:`, `build:`, `ci:`, `docs:`, `style:`, or `test:` must not be chosen merely because the implementation technique is internal when the resulting change is release-significant under the repository's own rules.

The implementation category and the release category are related but not identical questions. A refactor can still require a release if it changes a production dependency, supported runtime contract, packaged bytes, public API, compatibility boundary, or another condition the repository has explicitly declared release-driving.

## Repository ownership

The organization does not define one universal set of release-driving Conventional Commit types.

Each release-enabled repository remains authoritative for:

- which changes are release-significant;
- which Conventional Commit types are visible to its release automation;
- whether dependency changes use `deps:`, `fix:`, another visible type, or are intentionally non-release-driving;
- whether breaking-change syntax is supported and how it affects versioning;
- which merge methods are compatible with its release identity and publisher contract.

The checked-in Release Please configuration, repository release documentation, tests, and effective merge settings must tell a consistent story.

## Squash-merge requirements

For repositories that use squash merge for ordinary development pull requests:

1. Review the pull-request title as part of the merge gate, not only as prose.
2. Treat the title's Conventional Commit type as the classification of the resulting squash commit.
3. If the pull request contains a mechanically identifiable release-significant change, CI should fail closed when the title uses a hidden or otherwise non-release-driving type.
4. Repository-local checks should derive allowed release-driving types from the repository's own release configuration where practical rather than duplicating a second hard-coded policy.
5. A merge method that preserves individual commits does not remove the need for deliberate release metadata; it only changes which commit metadata Release Please consumes.

Changing a PR title after a squash merge does not repair the already-created commit. Recovery must proceed through the repository's normal reviewed release process rather than rewriting protected history or creating manual tags/releases.

## Automation boundary

Release-classification checks are read-only evidence. They may inspect:

- the pull-request title;
- the exact base and head revisions;
- changed paths or manifests;
- the repository's checked-in release configuration.

They must not gain tag, release, package-publication, or other privileged mutation authority merely because they participate in release selection.

Shared RAN quality infrastructure may provide generic helpers for classification validation where the semantics are genuinely common. Product-specific rules remain local when they depend on repository-specific runtime, packaging, dependency, or compatibility meaning.

## Dependency changes

Production dependency changes are a common mechanically detectable case but are not automatically classified the same way across RAN.

A repository that considers a production dependency change release-driving should make that decision explicit in both its release configuration and its PR validation. For example, a PHP library may compare the `require` map in `composer.json` between the exact PR base and head and require a visible release type when that map changes.

Development-only dependency changes should not be promoted to release-driving status merely because they live in the same manifest unless the repository explicitly chooses that policy.

## Examples

### Release-driving dependency adoption

A repository configures `deps:` as a visible changelog section and changes a production Composer dependency. A squash title of:

`deps: adopt updater support beta.3`

is consistent with the repository's policy.

A title of:

`refactor: consume shared repository path safety`

is not sufficient if the same pull request changes the production dependency and that dependency change is release-driving. After squash, Release Please may see only hidden `refactor:` metadata and skip the release entirely.

### Internal refactor with no release significance

A repository changes internal test support or reorganizes implementation code without crossing any release-driving boundary. If its release policy treats that work as hidden, a `refactor:` title is appropriate.

### Repository with different dependency policy

A repository intentionally treats `deps:` as hidden and documents that dependency-only changes do not independently drive releases. The organization policy does not require changing `deps:` to visible. It does require the repository to classify any release-significant effect using one of the types that its own release process recognizes.

## Relationship to release trust

This policy complements [RELEASE_TRUST.md](RELEASE_TRUST.md).

Release trust governs exact identity, evidence, privileged mutation, provenance, and readback. Release classification governs whether release automation recognizes that a reviewed change belongs in a release at all. A classification check is therefore an evidence input to release selection, not publication authority.

The organization-wide release audit in issue #9 should record classification exposure where merge strategy and Release Please metadata interact. Repository-specific remediation remains in the owning repository when the rule depends on local release semantics.

## Maintenance

When a repository changes its merge method, Release Please configuration, release-driving commit types, dependency policy, or equivalent release-selection semantics, re-check that the source of final commit metadata still matches the release policy.

A green release workflow that reports "no user facing commits" is not proof that the classification was correct; it is only proof that the automation successfully applied the metadata it was given.
