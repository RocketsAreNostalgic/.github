# Rockets Are Nostalgic organisation guidance

Start with your task, not the whole repository. Repository-local `AGENTS.md`,
contribution guidance and CI define the project-specific development contract;
shared requirements are a minimum and do not remove stronger local gates.

## Required reading by task

| Task | Reading path |
| --- | --- |
| Ordinary development or review | Local `AGENTS.md`, README and contribution guidance → the [Quality Standards navigation](docs/quality/QUALITY_STANDARDS.md#find-the-requirement-for-your-change) for applicable requirements. [Engineering](docs/ENGINEERING.md) explains the common stance and safe review boundary. |
| Change standards, quality tooling or CI | [Quality Standards](docs/quality/QUALITY_STANDARDS.md) → [workflow contract](docs/quality/QUALITY_WORKFLOWS.md) and [ruleset policy](docs/quality/REPOSITORY_RULESETS.md) as applicable. Read the [enforcement design](quality-enforcement/README.md) only when changing that boundary. |
| Prepare or operate a release | Local release guide → [release trust and classification](docs/release/RELEASE_TRUST.md) → the applicable [Profile A](docs/release/RELEASE_PROFILE_A.md) or [Profile B](docs/release/RELEASE_PROFILE_B.md). |
| Implement bootstrap templates | [Frozen bootstrap contract and examples](docs/release/BOOTSTRAP_STARTER_CONTRACT.md); release profiles remain separate contracts. |
| Change public contribution or support intake | [Community Standards](docs/COMMUNITY_STANDARDS.md), then the relevant inherited [contribution](CONTRIBUTING.md), [support](SUPPORT.md), [security](SECURITY.md) or [conduct](CODE_OF_CONDUCT.md) file. |

## Acceptance snapshots and coordination

[Quality acceptance](docs/quality/PHP_QUALITY_MATRIX.md) is the dated quality checkpoint;
[release publisher evidence](docs/release/RELEASE_PUBLISHERS.md) records release-specific
qualification and unresolved release obligations. Neither replaces policy or
constitutes permission to merge or publish.

Current work ownership and sequencing belong in existing issues:
[quality coordination #65](https://github.com/RocketsAreNostalgic/.github/issues/65),
[release delivery #81](https://github.com/RocketsAreNostalgic/.github/issues/81)
and [onboarding acceptance #85](https://github.com/RocketsAreNostalgic/.github/issues/85),
which remains mandatory before feature completion.
The UI/manual end-to-end acceptance deferral and Plugin Library deferral remain
in force unless an explicit newer owner decision supersedes them. Non-UI work
may continue within existing claims and automated gates; deferred acceptance
must not be reported as passed.

## Specialist references and historical evidence

The task references above preserve implementation contracts and operational
runbooks. Dated evidence and immutable source links in the acceptance documents
preserve completed investigations and superseded checkpoints; they are not
additional required reading for every change or claims about today's branches.
The [support-naming tool](quality-tools/support-naming/README.md) is a bounded
specialist reference, not a new rollout queue.

This public `.github` repository supplies GitHub community-health defaults when
a repository has no local equivalent. [Community Standards](docs/COMMUNITY_STANDARDS.md#authority-and-precedence)
defines inheritance, local overrides and the non-negotiable safety boundaries.

For links to the former root paths, use the [pre-move source snapshot](https://github.com/RocketsAreNostalgic/.github/tree/70e1321efc0b7cce7d6330b58cc0dd5a60e5ae66)
to recover the original file and heading. Engineering and community guidance
now live under `docs/`, quality references under `docs/quality/`, and release
references under `docs/release/`. Earlier investigations remain optional
[historical evidence](docs/quality/PHP_QUALITY_MATRIX.md#historical-evidence-and-completed-investigations).
