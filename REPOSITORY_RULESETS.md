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

Current examples include complex release/provenance workflows such as Booster and Booster Bitbucket, where ordinary quality, runtime/archive evidence, and release-candidate readback have different conditional lifecycles. `ran-booster-release-bootstrap-templates` likewise keeps separate `Pack inputs` and `Quality` checks because it does not currently expose a trustworthy terminal fan-in over both jobs. These checks should not be collapsed solely to make the Rulesets UI look uniform.

A repository that lacks a trustworthy terminal fan-in should keep the checks that actually enforce its current CI contract until a separate workflow change demonstrates that aggregation improves clarity without weakening coverage.

## Review automation

Copilot code review may remain enabled without automatically re-reviewing every push. Stale human approvals should still be dismissed after new commits. Automated re-review on every fixup push is not an organisation requirement.

## Repository profiles

The current maintained public repository mapping is:

| Repository | Profile | Merge methods | Protected CI contract |
| --- | --- | --- | --- |
| `.github` | Reusable workflow provider / organisation infrastructure | merge only | Provider review; organisation-required workflow enforcement is tracked separately in #12 |
| `ran-updater-support` | PHP library | squash + merge | `quality` from GitHub Actions |
| `ran-wp-branch-updater` | PHP library with installed-consumer proof | squash + merge | `quality` from GitHub Actions |
| `ran-wp-release-updater` | Mixed updater library with specialist integration lanes | squash + merge | `quality` from GitHub Actions |
| `ran-starter-plugin` | WordPress plugin reference | squash + merge | `quality` from GitHub Actions |
| `ran-emailoctopus-jetpack-forms` | WordPress plugin | squash + merge | `quality` from GitHub Actions |
| `ran-ecwid-shop-teaser` | WordPress plugin | squash + merge | `quality` from GitHub Actions |
| `ran-enhanced-cover` | WordPress plugin | squash + merge | `quality` from GitHub Actions |
| `ran-turnstile-for-jetpack-forms` | WordPress plugin | squash + merge | `quality` from GitHub Actions |
| `ran-booster` | Complex release/provenance product | squash + merge | `Runtime archive`, `Quality`, and `Release candidate install readback`, all from GitHub Actions |
| `ran-booster-bitbucket` | Complex release/provenance add-on | squash + merge | `Runtime archive`, `Quality`, and `Release candidate install readback`, all from GitHub Actions |
| `ran-booster-release-bootstrap-templates` | Release-integrity templates | squash + merge | `Pack inputs` and `Quality`, both from GitHub Actions |
| `ran-plugin-library` | Library pending quality-profile migration | squash + merge | No required CI status until a trustworthy gate exists |
| `ran-admin-shell` | Library in quality-gate migration | squash + merge | Add `quality` after the repository-side fan-in change lands |
| `tnyGmaps` | Legacy WordPress plugin | squash + merge | No normalized required CI status yet |
| `tnySignature` | Legacy WordPress plugin | squash + merge | No normalized required CI status yet |
| `wp-duplicate-detector` | Legacy WordPress plugin | squash + merge | No normalized required CI status yet |
| `ran-coding-standards` | Shared quality tooling | squash + merge target | Remediation tracked in #16: require its stable `quality` gate and resolved review threads |
| `ran-quality-config` | Shared quality tooling | squash + merge target | Remediation tracked in #16: require its stable `quality` gate |

Archived repositories and fixtures are outside the active normalization requirement unless restored to maintained status. Private maintained repositories are governed by the same policy in principle, but current plan/API limitations prevent the same live ruleset audit used for public repositories.

## Relationship to CI policy

This policy complements `QUALITY_WORKFLOWS.md` and `QUALITY_STANDARDS.md`.

Reusable workflows define shared quality execution; repository rulesets define what evidence is required before merge. A repository-local terminal status is useful merge evidence, but it is **not** an authoritative organisation workflow identity: a pull request may still be able to edit the caller, aggregate command, or transitive quality configuration.

Before RAN treats any local `quality` status as part of an authoritative organisation-level merge-enforcement boundary, the prerequisites in `QUALITY_WORKFLOWS.md` and #12 must be satisfied: organisation-controlled workflow identity plus quality-contract integrity through organisation-owned authoritative execution/configuration or independently protected approval of the complete transitive consumer contract. Until then, repository-local required statuses remain useful repository-level evidence, not an unforgeable organisation security boundary.

The guiding principle is:

> **Normalize the protection contract, not the workflow topology.**
