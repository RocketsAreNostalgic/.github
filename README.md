# Rockets Are Nostalgic organisation guidance

Start with your task, not the whole repository. Repository-local `AGENTS.md`,
contribution guidance and CI define the project-specific development contract;
shared requirements are a minimum and do not remove stronger local gates.

## Required reading by task

| Task | Reading path |
| --- | --- |
| Ordinary development or review | Local `AGENTS.md`, README and contribution guidance → the [Quality Standards navigation](QUALITY_STANDARDS.md#find-the-requirement-for-your-change) for applicable requirements. [Engineering](ENGINEERING.md) explains the common stance and safe review boundary. |
| Change standards, quality tooling or CI | [Quality Standards](QUALITY_STANDARDS.md) → [workflow contract](docs/QUALITY_WORKFLOWS.md) and [ruleset policy](docs/REPOSITORY_RULESETS.md) as applicable. Read the [enforcement design](quality-enforcement/README.md) only when changing that boundary. |
| Prepare or operate a release | Local release guide → [release trust and classification](RELEASE_TRUST.md) → the applicable [Profile A](RELEASE_PROFILE_A.md) or [Profile B](RELEASE_PROFILE_B.md). |
| Implement bootstrap templates | [Frozen bootstrap contract and examples](docs/release/BOOTSTRAP_STARTER_CONTRACT.md); release profiles remain separate contracts. |
| Change public contribution or support intake | [Community Standards](COMMUNITY_STANDARDS.md), then the relevant inherited [contribution](CONTRIBUTING.md), [support](SUPPORT.md), [security](SECURITY.md) or [conduct](CODE_OF_CONDUCT.md) file. |

## Acceptance snapshots and coordination

[Quality acceptance](PHP_QUALITY_MATRIX.md) is the dated quality checkpoint;
[release publisher evidence](RELEASE_PUBLISHERS.md) records release-specific
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

This public `.github` repository supplies GitHub community-health defaults when
a repository has no local equivalent. [Community Standards](COMMUNITY_STANDARDS.md#authority-and-precedence)
defines inheritance, local overrides and the non-negotiable safety boundaries.

For older links, use the [pre-consolidation source snapshot](https://github.com/RocketsAreNostalgic/.github/tree/4e5982757f42fdc640757f4caedc0be03b2da182)
to recover the original file and heading. The former release-classification page
is now [part of release trust](RELEASE_TRUST.md#release-classification); workflow
and ruleset references are under `docs/`, and the frozen bootstrap contract and
examples are under `docs/release/`. Retired quality investigations are linked
from the [historical evidence index](PHP_QUALITY_MATRIX.md#historical-evidence-and-completed-investigations).
