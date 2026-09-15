# RAN release-publisher audit

This document records the implementation-level audit of current production release publishers. It complements `RELEASE_TRUST.md`: that document defines the trust model; this document records how the current repositories implement it and where concrete drift remains.

The audit deliberately does **not** require one generic Release Please workflow. Repositories with different artifact, recovery, deployment, or provenance contracts may keep different workflow topology when the same transferable trust properties are preserved.

## Transferable publisher invariants

For a production write-capable release path, the organisation default is:

1. **No ambient workflow write authority.** Start with `permissions: {}` and grant only the write scopes required by the mutating job.
2. **Qualify exact current `main` before the first mutation.** A successful historical CI run is not enough if `main` has moved. Before Release Please, tag, release, label, asset, or deployment mutation, establish that the exact successful same-repository trusted-main revision is still the revision being acted on, or use a stronger repository-specific admission proof.
3. **Bind evidence to exact workflow/repository identity.** When publication consumes another workflow's evidence, verify the expected repository, workflow, event, conclusion, branch and SHA rather than trusting a status name alone.
4. **Use immutable Action identities.** Release-relevant third-party Actions are pinned to commit SHAs, with version comments where useful.
5. **Pin release toolchains where they execute release control.** Node, pnpm, and similar publisher runtimes use exact versions or an equivalently immutable lock when version drift could alter release decisions.
6. **Check out exact evidence revisions.** Where checkout is needed, use the exact admitted SHA, disable persisted credentials, and verify identity before executing release-controlled repository code.
7. **Keep recovery explicit.** Recovery/retry paths are repository contracts, not organisation boilerplate. They must preserve the same exact identity and readback guarantees as the normal publication path.
8. **Preserve artifact provenance.** Artifact publishers consume the exact tested artifact where practical, or independently prove any necessary rebuild against the exact admitted commit, manifest and digest.
9. **Read publication back.** Verify tag/release target, release state, expected assets and digests, and immutability where the release model supports it.
10. **Runner brand is not a semantic invariant.** GitHub-hosted Ubuntu 24.04 and the approved Blacksmith Ubuntu 24.04 runner are both acceptable. A change of runner provider is a trust/operations decision, not housekeeping for visual consistency.
11. **Do not flatten stronger local authority models.** Booster-family self-deferral, WordPress.org deployment controls, candidate dispatch, and package-specific recovery stay local until the release-trust architecture work demonstrates a safe common abstraction.

## Current production publisher matrix

| Repository | Publisher class | Admission before privileged mutation | Runtime / runner | Publication and recovery | Audit disposition |
| --- | --- | --- | --- | --- | --- |
| `ran-updater-support` | Source/library release | Successful same-repository `CI` `workflow_run`; exact-current-main preflight is being added before Release Please | GitHub-hosted Ubuntu 24.04; Node 24.11.0 | Exact publisher, immutable-release acknowledgement/readback; one bounded historical bootstrap recovery remains local | Keep architecture; land exact-main preflight |
| `ran-wp-branch-updater` | Source/library release with historical pending-release recovery | Successful same-repository `CI` `workflow_run`; recovery preflight proves exact current main before Release Please | Blacksmith Ubuntu 24.04; Node 24.11.0 | Explicit historical pending-release recovery, then Release Please, then exact publisher/readback | Recovery is justified and remains repository-specific |
| `ran-wp-release-updater` | Runtime/library release | Successful same-repository `CI` `workflow_run`; exact-current-main preflight is being added before Release Please | Blacksmith Ubuntu 24.04; Node is being pinned from mutable `24` to 24.11.0 | Exact publisher and immutable-release readback | Land exact-main + exact-Node correction |
| `ran-enhanced-cover` | WordPress artifact publisher/deployer | Successful same-repository `Quality` `workflow_run`; exact Quality checkout and Release Please merge proof before mutation | Blacksmith Ubuntu 24.04; pinned Actions; project-locked build toolchain | Publishes exact Quality artifacts, immutable readback, optional protected WordPress.org deployment | Current profile; retain product-specific artifact/deployment flow |
| `ran-emailoctopus-jetpack-forms` | WordPress artifact publisher/deployer | Successful same-repository `Quality` `workflow_run`; exact Quality checkout and Release Please merge proof before mutation | Blacksmith Ubuntu 24.04; pinned Actions; project-locked build toolchain | Publishes exact Quality artifacts and supports protected deployment/recovery | Current profile; retain local details |
| `ran-turnstile-for-jetpack-forms` | WordPress artifact publisher/deployer | Successful same-repository `Quality` `workflow_run`; exact Quality checkout and Release Please merge proof before mutation | Blacksmith Ubuntu 24.04; pinned Actions; project-locked build toolchain | Publishes exact Quality artifacts and supports protected deployment/recovery | Current profile; retain local details |
| `ran-ecwid-shop-teaser` | WordPress artifact publisher with candidate/recovery lifecycle | Main push entry, but write admission independently proves the live ruleset, exact merged PR, exact Quality evidence and source/tree identity before mutation | Blacksmith Ubuntu 24.04; pinned Actions; project-locked build toolchain | Secretless candidate dispatch/recovery, exact artifact provenance, isolated manual publication, protected WordPress.org deployment | Governance-contract reconciliation is being completed in repository issue #18/PR #20 |
| `ran-starter-plugin` | Starter/reference WordPress plugin | Direct `main` push invokes Release Please; no equivalent trusted-main Quality-evidence admission exists in the release workflow | `ubuntu-latest`; Release Please referenced by mutable `v5.0.0` tag; workflow-level write permissions | Minimal default Release Please flow | **Legacy outlier.** Harden before treating this as a release-publisher reference implementation |
| `ran-booster-release-bootstrap-templates` | Release-integrity template-pack publisher | Successful exact `Quality` `workflow_run` is re-read by run/workflow/repository/SHA identity before exact checkout and mutation | Blacksmith Ubuntu 24.04; Node 24.11.0; pinned Actions | Quality input archive, release-ID-bound deterministic pack, immutable publication/readback | Strong specialized profile; no normalization needed |
| `ran-booster` | Complex product release/provenance authority | Successful same-repository `Quality` `workflow_run`, exact checkout/current-main and merged-PR proof; changes to release-authority paths self-defer privileged reconciliation | Blacksmith Ubuntu 24.04; pinned Actions/project toolchains | Runtime archive/provenance, candidate install readback, immutable publication/reconciliation | Keep specialized; release-authority model belongs to #9 / Booster #119 |
| `ran-booster-bitbucket` | Complex add-on release/provenance authority | Successful same-repository `Quality` `workflow_run`, exact checkout/current-main and merged-PR proof; release-authority changes self-defer | Blacksmith Ubuntu 24.04; pinned Actions/project toolchains | Runtime archive/provenance, candidate readback, immutable publication/reconciliation | Keep specialized; coordinate architecture with #9 |

`ran-plugin-library`, `ran-coding-standards`, and `ran-quality-config` do not currently have production Release Please workflows and are therefore outside this publisher matrix.

## Audit conclusions

### Immediate concrete drift

- `ran-wp-release-updater`: mutable Node major `24` in the write-capable publisher. Pin to `24.11.0`.
- `ran-updater-support` and `ran-wp-release-updater`: Release Please can currently mutate before the later publisher code discovers that `main` moved away from the successful CI candidate. Add a read-only exact-current-main preflight before the Release Please Action.
- `ran-starter-plugin`: publisher generation is materially behind the maintained release-trust baseline: mutable Action reference, floating runner, workflow-level write permissions, and no exact trusted-main Quality admission before Release Please mutation. Treat this as a focused migration rather than a one-line normalization.

### Intentional differences

- The branch updater's recovery publisher is not a missing shared helper. It exists to recover a specific class of historical pending Release Please candidate while re-proving historical CI and current ancestry. Do not copy it to sibling publishers without the same failure mode.
- Runner provider is not normalized. Both current Ubuntu 24.04 runner families are accepted infrastructure; exact release behavior matters more than matching runner labels.
- Ecwid's push-triggered entry is acceptable only because the workflow independently proves the live governance contract and exact Quality/candidate identity before write mutation. It should not be copied as a simpler alternative to `workflow_run` admission.
- Booster, Booster Bitbucket, and bootstrap-template publication contain stronger release/provenance gates that are intentionally local.

## Relationship to other work

- `RELEASE_TRUST.md` / issue #9 owns the architectural question of release authority, including whether Booster-family self-deferral should be replaced by a clearer independent promotion boundary.
- Issue #12 owns authoritative organisation quality-workflow identity and transitive quality-contract integrity.
- This audit owns transferable **publisher implementation** invariants and concrete workflow drift; it does not replace either trust-boundary discussion.
