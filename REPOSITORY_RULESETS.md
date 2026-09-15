# RAN repository ruleset policy

This document defines the organisation default for repository branch rulesets. It standardises the protection contract while allowing repository-specific CI topology and release controls where they are substantively different.

## Default branch protection

Maintained repositories should protect their default branch with an active ruleset that:

- blocks deletion;
- blocks non-fast-forward updates / force pushes;
- requires pull requests;
- requires review-thread resolution;
- dismisses stale approvals when new commits are pushed;
- has no broad organisation-admin pull-request bypass by default;
- does not require linear history unless a repository has a documented, current reason;
- does not require a second-human approval merely for consistency when the repository's established review model does not require one.

Repository-specific exceptions must be explicit and justified by repository architecture rather than historical configuration.

## Merge methods

The normal product/package default is **squash + merge commit**. Rebase merge is not part of the organisation default.

`RocketsAreNostalgic/.github` is an intentional exception: reusable workflow consumers pin exact provider commits, so normal merge commits preserve reviewed provider head SHAs as reachable ancestors of `main`. Its protected branch should therefore remain **merge-commit only**.

Other repositories may use merge-commit-only behavior when exact commit identity is itself part of the published or consumed contract, but that exception should be documented in the repository.

## Required status checks

When a repository has a terminal CI aggregation job, the ruleset should normally require that single terminal check rather than independently naming every internal lane.

The preferred protected check name is `quality` where the workflow already exposes that stable terminal gate. The terminal job must depend on every ordinary merge-blocking lane and fail unless each required lane succeeds.

Internal lane names may differ by repository. The organisation standardises the protected **contract**, not the workflow topology.

### Check source

A required status check produced by GitHub Actions should be bound to **GitHub Actions** as the expected source/app. Do not leave an Actions-produced required check satisfiable by an arbitrary integration with the same status name.

### Multiple required checks

Multiple protected checks are appropriate where they represent genuinely distinct lifecycle or security gates that are not naturally reducible to one ordinary terminal quality contract.

Current examples include complex release/provenance workflows such as Booster and Booster Bitbucket, where ordinary quality, runtime/archive evidence, and release-candidate readback have different conditional lifecycles. These should not be collapsed solely to make the Rulesets UI look uniform.

A repository that lacks a trustworthy terminal fan-in should keep the checks that actually enforce its current CI contract until a separate workflow change demonstrates that aggregation improves clarity without weakening coverage.

## Review automation

Copilot code review may remain enabled without automatically re-reviewing every push. Stale human approvals should still be dismissed after new commits. Automated re-review on every fixup push is not an organisation requirement.

## Repository classes and intentional differences

- **Ordinary maintained products/packages:** squash + merge commit; no linear-history requirement; stale approvals dismissed; no broad admin bypass; require the terminal `quality` gate from GitHub Actions when one exists.
- **Reusable workflow provider (`.github`):** merge-commit only; no linear-history requirement; stale approvals dismissed; no broad admin bypass. Exact provider commit reachability is part of the consumer contract.
- **Complex release/provenance repositories:** may require more than one GitHub Actions check when distinct conditional lifecycle gates cannot safely be represented by one terminal fan-in.
- **Legacy repositories:** should move toward the ordinary default when touched, but CI/tooling migration should remain separate from unrelated application refactoring where practical.
- **Archived/fixture repositories:** are outside the active normalization requirement unless restored to maintained status.

## Relationship to CI policy

This policy complements `QUALITY_WORKFLOWS.md` and `QUALITY_STANDARDS.md`.

Reusable workflows define shared quality execution; repository rulesets define what evidence is required before merge. A local status name is useful merge evidence but is not, by itself, an unforgeable organisation workflow identity. Organisation-required-workflow enforcement and quality-contract integrity remain a separate follow-up concern.

The guiding principle is:

> **Normalize the protection contract, not the workflow topology.**
