# RAN release-publisher audit

This document records the implementation-level audit of current production release publishers. It complements `RELEASE_TRUST.md`: that document defines the trust model; this document records how current repositories implement it and where concrete drift remains.

The audit deliberately does **not** require one generic Release Please workflow. Repositories with different artifact, recovery, deployment, or provenance contracts may keep different workflow topology when the same applicable trust properties are preserved.

## Transferable publisher invariants

For a production write-capable release path, the organisation default is:

1. **No ambient workflow write authority.** Start with `permissions: {}` and grant only the write scopes required by the mutating job.
2. **Separate release-PR reconciliation from publication authority.** A Release Please action may reconcile its managed pull request against the repository target branch. That mutation is not itself publication evidence. Before creating tags, publishing releases/assets, reconciling a release as complete, or deploying externally, the publisher must establish the exact trusted candidate required by its release model.
3. **Do not overclaim read-then-write checks.** Re-reading `main` immediately before a later API mutation can reject stale triggers, but it is not an atomic compare-and-swap with a concurrent push. Treat such checks as defence in depth, not as an independent authorization boundary.
4. **Bind evidence to exact workflow/repository identity.** When publication consumes another workflow's evidence, verify the expected repository, workflow, event, conclusion, branch and SHA rather than trusting a status name alone.
5. **Use immutable Action identities.** Release-relevant third-party Actions are pinned to commit SHAs, with version comments where useful.
6. **Pin release toolchains where they execute release control.** Node, pnpm, and similar publisher runtimes use exact versions or an equivalently immutable lock when version drift could alter release decisions.
7. **Check out exact evidence revisions.** Where checkout is needed, use the exact admitted SHA, disable persisted credentials, and verify identity before executing release-controlled repository code.
8. **Keep recovery explicit.** Recovery/retry paths are repository contracts, not organisation boilerplate. They must preserve the same exact identity and readback guarantees as the normal publication path.
9. **Preserve artifact provenance.** Artifact publishers consume the exact tested artifact where practical, or independently prove any necessary rebuild against the exact admitted commit, manifest and digest.
10. **Read publication back.** Verify tag/release target, release state, expected assets and digests, and immutability where the release model supports it.
11. **Runner brand is not a semantic invariant.** GitHub-hosted Ubuntu 24.04 and the approved Blacksmith Ubuntu 24.04 runner are both acceptable. A runner-provider change is a trust/operations decision, not housekeeping for visual consistency.
12. **Do not flatten stronger local authority models.** Booster-family self-deferral, WordPress.org deployment controls, candidate dispatch, and package-specific recovery stay local until the release-trust architecture work demonstrates a safe common abstraction.

### Exact candidate versus latest `main`

A successful exact `main` qualification identifies a specific trusted candidate. It does **not** imply that every repository must abort publication merely because a later ordinary commit reached `main` before the candidate was published. Some release models legitimately publish the already-qualified earlier version, provided the tag, release target, artifacts and readback remain bound to that exact candidate and release ordering remains unambiguous.

Repositories whose semantics require the candidate still to be the tip of `main` must prove that condition as part of their local release contract. A standalone read-then-write branch check is not sufficient to turn that condition into an atomic authorization boundary.

## Current production publisher matrix

The disposition terms are those required by `RELEASE_TRUST.md`.

| Repository | Publisher class | Admission and publication model | Runtime / runner | Disposition | Rationale / follow-up |
| --- | --- | --- | --- | --- | --- |
| `ran-updater-support` | Source/library release | Successful same-repository `CI` `workflow_run`; Release Please reconciles its managed PR; exact publisher validates checkout, candidate, source/release state and immutable publication before finalization | GitHub-hosted Ubuntu 24.04; Node 24.11.0 | **CONFORMS** | Release Please PR reconciliation is not treated as publication evidence; exact publisher/readback owns publication admission. The rejected non-atomic preflight experiment was closed unmerged in `RocketsAreNostalgic/ran-updater-support#26`. |
| `ran-wp-branch-updater` | Source/library release with historical pending-release recovery | Successful same-repository `CI` `workflow_run`; bounded recovery can reconcile one historical pending candidate while re-proving historical CI/current ancestry; normal exact publisher revalidates publication identity | Blacksmith Ubuntu 24.04; Node 24.11.0 | **JUSTIFIED DIFFERENCE** | Recovery exists for a specific historical-pending-release failure mode and should not be copied to siblings without that requirement. |
| `ran-wp-release-updater` | Runtime/library release | Successful same-repository `CI` `workflow_run`; Release Please reconciles its managed PR; exact publisher proves the release merge/runtime identity and immutable publication state | Blacksmith Ubuntu 24.04; Node 24.11.0 | **CONFORMS** | Mutable Node `24` drift was corrected by `RocketsAreNostalgic/ran-wp-release-updater#50`. |
| `ran-enhanced-cover` | WordPress artifact publisher/deployer | Successful same-repository `Quality` `workflow_run`; exact Quality revision and merged Release Please candidate are proven; tested artifacts are carried into immutable publication and optional protected WordPress.org deployment | Blacksmith Ubuntu 24.04; pinned Actions; project-locked build toolchain | **CONFORMS** | Stronger artifact/deployment checks are repository-specific, not organisation boilerplate. |
| `ran-emailoctopus-jetpack-forms` | WordPress artifact publisher/deployer | Successful same-repository `Quality` `workflow_run`; exact qualified candidate and tested assets are verified before publication/deployment | Blacksmith Ubuntu 24.04; pinned Actions; project-locked build toolchain | **CONFORMS** | Retain local artifact and deployment details. |
| `ran-turnstile-for-jetpack-forms` | WordPress artifact publisher/deployer | Successful same-repository `Quality` `workflow_run`; exact qualified candidate and tested assets are verified before publication/deployment | Blacksmith Ubuntu 24.04; pinned Actions; project-locked build toolchain | **CONFORMS** | Retain local artifact and deployment details. |
| `ran-ecwid-shop-teaser` | WordPress artifact publisher with candidate/recovery lifecycle | Push-triggered entry, but publication admission independently proves the live governance contract, exact merged PR, exact Quality evidence and source/tree identity; manual publication is isolated from build authority | Blacksmith Ubuntu 24.04; pinned Actions; project-locked build toolchain | **JUSTIFIED DIFFERENCE** | The push-triggered topology is acceptable only with its stronger exact candidate/evidence proof. Governance contract was reconciled by `RocketsAreNostalgic/ran-ecwid-shop-teaser#19` and follow-up `RocketsAreNostalgic/ran-ecwid-shop-teaser#20`. |
| `ran-starter-plugin` | Starter/reference WordPress plugin | Successful same-repository `Quality` `workflow_run` from a trusted `main` push is re-read by workflow/run/repository/SHA identity before exact checkout and pinned Release Please mutation; the bot-managed release PR receives an explicit read-only Quality dispatch for its exact head; any created source-only release/tag is read back against the exact qualified commit | GitHub-hosted Ubuntu 24.04; pinned Release Please action; project-locked quality toolchain | **CONFORMS** | Legacy direct-push publisher was hardened by `RocketsAreNostalgic/ran-starter-plugin#19`, closing `RocketsAreNostalgic/ran-starter-plugin#17`. End-to-end verification proved main Quality → Release Please → exact release-PR Quality, including terminal `quality` from GitHub Actions. |
| `ran-booster-release-bootstrap-templates` | Release-integrity template-pack publisher | Successful exact `Quality` `workflow_run` is re-read by run/workflow/repository/SHA identity; publication consumes tested pack inputs and finalizes a release-ID-bound deterministic pack with immutable readback | Blacksmith Ubuntu 24.04; Node 24.11.0; pinned Actions | **JUSTIFIED DIFFERENCE** | Release-ID-bound deterministic pack construction is a product-specific integrity requirement. |
| `ran-booster` | Complex product release/provenance authority | Successful same-repository `Quality` lifecycle, exact checkout/merged-PR evidence, runtime archive and candidate proofs; release-control changes currently self-defer privileged reconciliation | Blacksmith Ubuntu 24.04; pinned Actions/project toolchains | **JUSTIFIED DIFFERENCE** | Existing self-deferral is fail-closed but is not an independent principal. The architectural replacement is tracked separately by `RocketsAreNostalgic/ran-booster#119` and `RocketsAreNostalgic/ran-booster#126`; #9 owns that decision. |
| `ran-booster-bitbucket` | Complex add-on release/provenance authority | Successful same-repository `Quality` lifecycle with exact candidate/runtime archive/readback proofs and local release-control deferral | Blacksmith Ubuntu 24.04; pinned Actions/project toolchains | **JUSTIFIED DIFFERENCE** | Keep specialized provenance/candidate gates local; coordinate any authority-model redesign through #9 rather than normalizing mechanically. |

## Repositories without a production write-capable release path

The audit also checked maintained shared/support repositories that might otherwise look like omissions:

- `ran-plugin-library` has no checked-in `.github/workflows` directory and no detected production release mutator; release-related matches are documentation/examples rather than publication code.
- `ran-coding-standards` has only its read-only `Quality` workflow (`contents: read`) and no detected checked-in production release mutator.
- `ran-quality-config` has only its read-only `Quality` workflow (`contents: read`) and no detected checked-in production release mutator.

They are therefore not release-enabled repositories under the `RELEASE_TRUST.md` audit definition at present. If any gains a tag/release/package/deployment mutator, it enters this matrix at that point.

## Audit conclusions

### Concrete remediation

- `ran-wp-release-updater`: **completed** — write-capable publisher Node is now pinned to exact 24.11.0 via `RocketsAreNostalgic/ran-wp-release-updater#50`.
- `ran-starter-plugin`: **completed** — legacy direct-push publication was replaced by exact successful Quality admission, immutable Release Please action identity, explicit exact-head Quality for the bot release PR, and exact tag/release readback via `RocketsAreNostalgic/ran-starter-plugin#19` / `RocketsAreNostalgic/ran-starter-plugin#17`.

There are no remaining **REMEDIATION REQUIRED** repositories from the implementation-level publisher audit. Broader release-authority architecture remains separately owned by #9.

### Reviewed differences that are intentional

- Runner provider is not normalized merely for visual consistency.
- Branch-updater recovery remains local because it addresses a specific historical pending-release state.
- Updater-support and release-updater allow Release Please to reconcile its managed PR before the later exact publisher admits final publication. This is accepted because the PR mutation is not treated as release evidence; tag/release publication remains bound to the exact publisher contract and readback.
- A non-atomic current-`main` preflight is not mandated as a security boundary. Repositories that require tip-of-main publication must enforce that as part of their local release semantics rather than relying on a read-then-write check.
- Ecwid's push-triggered entry is a justified topology difference because its downstream publication path independently proves the exact governance/evidence/candidate identity.
- Booster, Booster Bitbucket and bootstrap-template publication retain stronger specialized provenance gates.

## Relationship to other work

- `RELEASE_TRUST.md` / issue #9 owns the architectural question of release authority, including whether Booster-family self-deferral should be replaced by a clearer independent promotion boundary.
- Issue #12 owns authoritative organisation quality-workflow identity and transitive quality-contract integrity.
- This audit owns transferable **publisher implementation** invariants and concrete workflow drift; it does not replace either trust-boundary discussion.
