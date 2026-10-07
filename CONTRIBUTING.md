# Contributing

Thank you for contributing to a Rockets Are Nostalgic project.

Before making changes, read the repository's local `AGENTS.md`, README, development documentation, and any local `CONTRIBUTING.md`. Repository-local engineering guidance and CI define the required development and validation contract.

Install dependencies from tracked lockfiles and run the checks required by the repository before proposing a change. Add focused runtime, integration, compatibility, generated-artifact, or release proofs when the project contract requires them.

Use the repository's commit and release conventions. Where a repository uses Release Please or otherwise requires Conventional Commits, use a Conventional Commit **pull-request title** for an ordinary squash merge configured to use that title: that title becomes the final squash subject consumed by Release Please, rather than the individual branch commit subjects. If the approved merge method preserves individual commits, their subjects remain release inputs; review the metadata that actually survives that merge. Treat release-driving subjects as release metadata: a release-significant change must use a release-driving classification recognized by that repository's own release policy, or a supported explicit breaking classification. See the [RAN release-classification policy](https://github.com/RocketsAreNostalgic/.github/blob/main/docs/release/RELEASE_TRUST.md#release-classification).

The organisation `.github` repository is a deliberate **merge-only** exception: reusable-workflow consumers pin exact reviewed provider commits, which must remain reachable from `main`. Product-specific release-proposal merge rules still apply; Booster's bot-owned release proposals require a merge commit. Consult the repository's release guide before proposing a merge method. This contribution guide does not authorize merge or publication.

Do not include credentials, secrets, signed URLs, customer data, private source, private repository or site identities, full production logs, private workbench material, vulnerability details, or other sensitive information in commits, issues, or pull requests. Replace private identities with neutral labels and reduce examples to non-sensitive reproducers.

Use `SUPPORT.md` for ordinary support and non-sensitive defects. Use `SECURITY.md` for vulnerabilities; never submit vulnerability details through a public issue or pull request.

Organization-wide requirements and the local-override rules are defined in the [RAN Community Standards](https://github.com/RocketsAreNostalgic/.github/blob/main/docs/COMMUNITY_STANDARDS.md).
