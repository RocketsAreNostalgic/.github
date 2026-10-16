# Set up releases in a new RAN repository

Use this guide for a new helper library, plugin or theme. Read the parent
[Release Please skill](../SKILL.md) first. Create a reviewed setup PR; setup does
not itself authorize activating publication or releasing a version.

## 1. Establish the target

Inspect the actual repository and ask only for missing decisions:
- Package identity, repository visibility and default branch. Current shared
  Profiles A/B require main; do not silently rename another default branch.
- Library/source distribution or a separately built installable artifact.
- Stable versus prerelease version policy and intended first release.
- Existing tags, version sources, workflows, supported runtimes and quality gates.

Treat existing files or automation as an integration case. Preserve useful CI
rather than overwriting it. Do not copy another repository's bootstrap SHA,
package name, workflow pin or beta policy without checking applicability.

## 2. Choose the publication profile

| Target | Normal starting point | Local responsibility |
| --- | --- | --- |
| Composer helper library distributed from tagged source | [Profile A](https://github.com/RocketsAreNostalgic/.github/blob/main/docs/release/RELEASE_PROFILE_A.md) | Composer/package identity, quality and real consumer contracts |
| WordPress plugin/theme distributed as an installable built ZIP | [Profile B](https://github.com/RocketsAreNostalgic/.github/blob/main/docs/release/RELEASE_PROFILE_B.md) | Deterministic build, independent archive verification and relevant installed proof |
| Another distribution shape | Inspect the authoritative published payload | Select A/B from actual custody needs, not repository branding |

For a simple source-ready plugin/theme, use the approved
[starter contract](https://github.com/RocketsAreNostalgic/.github/blob/main/docs/release/BOOTSTRAP_STARTER_CONTRACT.md)
and [file/workflow examples](https://github.com/RocketsAreNostalgic/.github/blob/main/docs/release/BOOTSTRAP_STARTER_EXAMPLES.md).
Its automatic recipe requires committed payload and stable versions; it does
not support inferred Composer installation, asset builds or arbitrary existing CI.
A plugin with compiled/vendored output or a beta policy needs explicit local
build/version integration under Profile B. The starter's manual/UI acceptance
status does not establish acceptance for a newly configured repository.

Use [Updater Support](https://github.com/RocketsAreNostalgic/ran-updater-support)
as an existing source-library example and
[Bitbucket](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket)
as a packaged-plugin example. Their current configuration is evidence to inspect,
not a universal template or permission to copy their product-specific checks.

## 3. Prepare the concrete files

| File or area | Setup requirement |
| --- | --- |
| release-please-config.json | Correct strategy/package identity, tag shape, version policy and necessary extra-files |
| .release-please-manifest.json | Deliberate baseline coherent with actual history/version policy |
| Read-only canonical CI/Quality workflow | PR and main-push qualification plus input-free workflow_dispatch on the exact requested revision |
| .github/workflows/release-please.yml | Thin caller from the selected profile, pinned to an approved full organisation commit |
| Local release guide and AGENTS.md | Exact checks, merge method, first-release steps, shared skill link and retrieval route |
| Profile B build/verifier and packaging inputs | Actual complete payload, safe archive, coherent version/metadata, tested artifact and promotion manifest |

For a PHP library, inspect upstream's php strategy and manifest configuration.
For WordPress, keep every real version source coherent: header, optional readme,
version.txt/Composer metadata and runtime-copy manifests as applicable. Use
supported extra-files/annotations rather than another version engine. The simple
starter deliberately uses the simple strategy; another maintained plugin may use
php. Choose from actual version sources, not the existence of composer.json alone.

Consult [upstream manifest configuration](https://github.com/googleapis/release-please/blob/main/docs/manifest-releaser.md)
and [configuration options](https://github.com/googleapis/release-please/blob/main/docs/customizing.md)
for initial-version, prerelease and bootstrap behaviour. An initial-version choice
is not necessarily the next emitted version: qualify the first releasable commit
against the selected policy. If bootstrap-sha is used, choose a real verified
history boundary; never insert a fixture or unrelated repository SHA.

Copy caller structure from the selected current RAN profile and replace all
repository-specific values. Bind workflow name/path and bot release branch to
the actual configuration. Use automatic GITHUB_TOKEN with the documented job
permissions, no secrets: inherit, and no privileged PR-code execution.
For Profile B, retain draft/force-tag-creation prerequisites and exact run-bound
artifact promotion; build and verify before privileged publication.

## 4. Check execution prerequisites

Verify available evidence for owner-managed Actions/reusable-workflow access,
allowed pinned Actions, runners, bot PR creation, immutable releases and effective
required checks/review/merge settings. Report settings you cannot inspect as
unverified; do not infer them from organisation membership or a generic 403.
Ask the responsible administrator only for a concrete unavailable prerequisite;
do not request broader tokens just to bypass the normal workflow.

Keep preparation separate from activation: read-only Quality may already run on
a setup PR, and merging it can start main Quality/publication. Identify these
effects in the PR and establish required settings before activating the pipeline.
Do not add administration probes to product code as a substitute.

## 5. Qualify the setup and first release

- Validate configuration against the applicable upstream schema; check exact
  extra-file/version edits and a real Release Please candidate through the
  existing read-only qualification or a disposable fixture.
- Exercise ordinary PR, exact release-candidate dispatch and main-push Quality
  paths; preserve existing meaningful product checks.
- For Profile B, test deterministic construction and independent archive/member/
  metadata verification, artifact naming and SHA/tag/version binding. Include
  meaningful invalid-input controls and relevant installed plugin/theme proof.
- Review the actual setup PR independently, including triggers, permission
  boundaries, workflow pins and what a merge activates.
- After authorized setup delivery, verify main checks and the real bot release
  candidate. Merge only under applicable owner authorization and repository rules.
- Read back the first published version/tag/commit, required immutability and
  exact assets where applicable. Separately qualify Packagist or other downstream
  distribution if requested; GitHub publication alone does not prove it.

Report the setup PR, profile/pins, first-version policy, validation, settings
gaps and remaining acceptance. Use the parent skill's troubleshooting for a
failed first release; never repair it by moving a tag or replacing public assets.
