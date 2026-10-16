---
name: release-please
description: Prepare, operate, review and troubleshoot Release Please releases across RocketsAreNostalgic repositories. Use for release PRs, version classification, shared release profiles, immutable publication, dependency-release sequencing, or changes to release automation.
---

# RAN Release Please

Use the repository's existing release pipeline. Release Please owns version calculation,
changelogs, release PRs, tags and GitHub Release creation. RAN release profiles add
qualification and, where applicable, tested-asset promotion. Neither this skill nor
a green check supplies merge or publication authorization.

## Load the applicable guidance

Read the target repository's AGENTS.md and release guide, then:
- [RAN release trust](https://github.com/RocketsAreNostalgic/.github/blob/main/docs/release/RELEASE_TRUST.md).
- [Profile A](https://github.com/RocketsAreNostalgic/.github/blob/main/docs/release/RELEASE_PROFILE_A.md) for source/library releases.
- [Profile B](https://github.com/RocketsAreNostalgic/.github/blob/main/docs/release/RELEASE_PROFILE_B.md) for authoritative built assets.

Identify the actual profile from the checked-in caller workflow; do not infer it
solely from repository type. Inspect its pinned shared workflow revision when
diagnosing execution. Guidance on main does not prove an older pinned revision
implements the same behaviour. Preserve stronger product/runtime requirements.

Consult official upstream references for the configured action/version and the
specific option or failure under investigation:
- [Release Please repository and overview](https://github.com/googleapis/release-please).
- [GitHub Action configuration and token behaviour](https://github.com/googleapis/release-please-action).
- [Manifest configuration](https://github.com/googleapis/release-please/blob/main/docs/manifest-releaser.md).
- [Configuration options](https://github.com/googleapis/release-please/blob/main/docs/customizing.md).
- [Troubleshooting](https://github.com/googleapis/release-please/blob/main/docs/troubleshooting.md).

## Establish the current release tuple

Inspect current main, open source and bot-owned release PRs, exact heads, reviews,
required checks, active workflow runs, manifest/configuration, tags and releases.
Read release-specific extra-files and runtime/package manifests where present.
Distinguish reviewed source, merged source, draft release, published immutable
release, dependency uptake and installed qualification.

Check the user's existing authorization and active delivery owner before mutation.
Use any applicable standing authorization within its actual scope; do not ask
again for an already-authorized prerequisite. Otherwise present the exact action
and candidate for an owner decision. Coordinate active writers and releases.

## Prepare and deliver

1. Classify the metadata that survives the chosen merge: ordinarily the squash PR
   title, or retained commit subjects. Use repository-supported conventional commit
   and breaking-change rules; let the actual Release Please configuration determine
   version/prerelease progression. Do not calculate a parallel version lifecycle.
2. Qualify the exact source/release PR tuple with local required checks and
   independent review. A changed head needs reconsideration of affected evidence.
   Resolve required findings and check effective merge requirements.
3. Use the repository's required merge method. Core's bot-owned release PRs require
   a merge commit; ordinary Core PRs generally use squash. Organisation .github is
   merge-only. Read current local rules for every satellite; do not export one
   repository's exception to all repositories.
4. Follow the existing shared workflow. Profiles A/B use the automatic GITHUB_TOKEN
   and bounded read-only Quality dispatch for bot PR event suppression. A missing
   ordinary PR run does not justify adding a PAT, secrets: inherit, or bypassing checks.
5. Observe exact successful-main admission and publication. For Profile B, verify
   promotion of the original run/attempt's tested assets rather than rebuilding
   privileged substitute bytes. Follow the profile's exact draft/publication rules.
6. Read back the actual tag target, release identity/state, required immutability
   and asset names/digests where applicable. A merged release PR or successful
   mutation response alone does not establish completed publication.
7. For dependent repositories, adopt the real released version with exact locks
   and required runtime/protocol metadata. Qualify actual vendored/installed copies.
   Candidate source proofs remain distinct from immutable dependency qualification.

Report exact PR/commit/tag/version, check/run links, publication readback,
downstream uptake and remaining acceptance holds. Do not clear manual/UI holds
from automated evidence or close work that has not reached its delivery boundary.

## Diagnose and resume

Locate the failing stage: event/runner allocation, source or release-PR Quality,
main admission, Release Please, artifact custody, draft promotion or final readback.
Inspect actual logs and remote state before retrying; a later failure may follow
an already-created PR, tag, uploaded asset or published release.

Follow Profile A/B troubleshooting and retry boundaries. An open release PR or
no releasable change can be normal non-publication. GITHUB_TOKEN event suppression
can require the existing exact-candidate Quality dispatch. An executed red check
is a real failure; diagnose it rather than suppressing it.

Never move released tags, replace published assets, fabricate lifecycle labels,
hand-edit bot version/changelog output to manufacture completion, or weaken
admission. A broken published build requires the approved next-version path.
Preserve checks, pinned workflow/action identities and trusted artifact custody.

## Change automation only when requested

For an authorized setup or repair, inspect current workflows/configuration first.
Reuse the appropriate RAN profile and existing publication architecture; do not
replace it with a generic upstream example. Keep product construction and runtime
proofs local, apply least privilege and immutable action/workflow pins, and review
the change with the applicable contract checks. Use upstream documentation to
resolve semantics rather than copy third-party skill instructions.
