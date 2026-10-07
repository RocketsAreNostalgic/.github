# RAN repository ruleset policy

This document defines the organisation default for repository branch rulesets. It standardises the protection contract while allowing repository-specific CI topology and release controls where they are substantively different.

## Default branch protection

Maintained repositories should protect their default branch with an active ruleset that:

- blocks deletion;
- blocks non-fast-forward updates / force pushes;
- requires pull requests;
- requires review-thread resolution;
- dismisses stale approvals when new commits are pushed;
- does **not** require approval of the most recent reviewable push (`require_last_push_approval: false`) unless a repository documents a reason to do so;
- has no broad organisation-admin pull-request bypass by default;
- does not require linear history unless a repository has a documented, current reason;
- does not require a second-human approval merely for consistency when the repository's established review model does not require one.

Repository-specific exceptions must be explicit and justified by repository architecture rather than historical configuration.

## Merge methods

The normal product/package default is **squash + merge**. Rebase merge is not part of the organisation default. Squash is the ordinary choice for iterative or agent-developed pull requests; merge commits are appropriate when the internal commit sequence is intentionally worth preserving.

`RocketsAreNostalgic/.github` is an intentional exception: reusable workflow consumers pin exact provider commits, so normal merge commits preserve reviewed provider head SHAs as reachable ancestors of `main`. Its protected branch should therefore remain **merge-only**.

Other repositories may use merge-only behavior when exact commit identity is itself part of the published or consumed contract, but that exception should be documented in the repository.

## Required status checks

When a repository has a trustworthy terminal CI aggregation job, the ruleset should normally require that single terminal check rather than independently naming every internal lane.

The preferred protected check name is `quality` where the workflow exposes a stable terminal gate that depends on every ordinary merge-blocking lane and fails unless each required lane succeeds. Merely having a job named `quality` is not sufficient. If the job does not aggregate the complete merge-blocking contract, retain the underlying required checks instead.

Internal lane names may differ by repository. The organisation standardises the protected **contract**, not the workflow topology.

### Check source

A required status check produced by GitHub Actions should be bound to **GitHub Actions** as the expected source/app. Do not leave an Actions-produced required check satisfiable by an arbitrary integration with the same status name.

### Multiple required checks

Multiple protected checks are appropriate where they represent genuinely distinct lifecycle or security gates that are not naturally reducible to one ordinary terminal quality contract.

Current examples include complex release/provenance workflows such as Booster and Booster Bitbucket, where ordinary quality, runtime/archive evidence, and release-candidate readback have different conditional lifecycles. `ran-booster-release-bootstrap-templates` now exposes a local terminal `quality` fan-in over its repository-owned `Pack inputs` lane and the shared Node baseline, but its live ruleset deliberately continues to require the established `Pack inputs` and `Quality` contexts while organisation-required enforcement is proved under #31. Do not remove those existing requirements merely because the new diagnostic terminal exists.

A repository that lacks a trustworthy terminal fan-in should keep the checks that actually enforce its current CI contract until a separate workflow change demonstrates that aggregation improves clarity without weakening coverage.

## Review automation

Copilot code review may remain enabled without automatically re-reviewing every push. Stale human approvals should still be dismissed after new commits. Automated re-review on every fixup push is not an organisation requirement.

## Repository profiles

The [recorded repository mapping](https://github.com/RocketsAreNostalgic/.github/blob/4e5982757f42fdc640757f4caedc0be03b2da182/REPOSITORY_RULESETS.md#repository-profiles)
preserves the inspected profiles, merge methods and protected contexts as
historical evidence. Consult [quality acceptance](PHP_QUALITY_MATRIX.md),
existing repository issues and live rulesets for subsequent changes; this
policy is not a second current-status inventory.

The recorded unresolved obligations remain: organisation-required enforcement
is coordinated under [#31](https://github.com/RocketsAreNostalgic/.github/issues/31);
shared-tooling protection remediation under
[#16](https://github.com/RocketsAreNostalgic/.github/issues/16) requires the stable
`quality` gate for Coding Standards and Quality Config, plus resolved review
threads for Coding Standards. Plugin Library migration remains deferred/not
planned. Recorded legacy gaps for `tnyGmaps` and `wp-duplicate-detector`, and
`tnySignature`'s pending organisation-required enforcement, are not certified
closed by this consolidation.

Archived repositories and fixtures are outside the active normalization requirement unless restored to maintained status. Private maintained repositories are governed by the same policy in principle, but current plan/API limitations prevent the same live ruleset audit used for public repositories.

## Relationship to CI policy

[Reusable workflows](QUALITY_WORKFLOWS.md) define shared quality execution;
[Quality Standards](QUALITY_STANDARDS.md#ci-contract) defines the CI contract.
Rulesets govern which evidence is required before merge. A repository-local
status remains useful evidence without becoming an authoritative organisation
workflow identity.

[Enforcement integrity](QUALITY_STANDARDS.md#enforcement-integrity) is the
authoritative requirement for organisation-controlled workflow identity and
quality-contract protection. The completed design is recorded in #12;
activation prerequisites remain under #31. Repository-local required statuses
must not be presented as that organisation security boundary before both
requirements are satisfied.

> **Normalize the protection contract, not the workflow topology.**
