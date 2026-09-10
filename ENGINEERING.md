# How RAN builds software

Rockets Are Nostalgic is small by design. I build and publish these plugins and tools, and I want the repositories to be useful to people who install the software, read the code, contribute a change, or review it with an agent.

Small should not mean ad hoc.

Across maintained RAN repositories, the baseline is straightforward:

- keep sensitive things private;
- make changes reviewable;
- use repeatable automated quality checks;
- test the behaviour that matters;
- keep commits, releases, and merges deliberate;
- let the actual project decide which tools are applicable.

The point is not to make every repository look the same. It is to make the level of confidence reasonably consistent.

## One baseline, different projects

RAN projects do not all have the same code surface, so they should not all have the same configuration.

A maintained WordPress plugin with PHP, JavaScript, and CSS needs a broader quality surface than a small PHP library, a fixture, or a configuration-only repository. The shared standard is therefore about the guarantees a project should provide, not about copying the same dependency list everywhere.

Where the code exists, I expect the strongest sensible combination of the normal tools for that ecosystem. That generally means things such as:

- PHPCS with WordPress Coding Standards and PHP compatibility checks for maintained WordPress PHP;
- static analysis for maintained production PHP where the project profile calls for it;
- PHPUnit, integration, characterization, contract, or other focused behavioural tests;
- ESLint for maintained JavaScript or TypeScript;
- Prettier for deterministic formatting;
- Stylelint for maintained CSS or Sass;
- TypeScript checking where TypeScript exists;
- build, generated-file, packaging, installation, compatibility, or release checks when those are part of the product contract.

A repository should not gain a tool merely to satisfy a checklist. Equally, an applicable quality gate should not disappear just because the surrounding project has not adopted it yet. Missing quality infrastructure is a migration gap, not proof that the check is unnecessary.

## Security before convenience

Security reporting should use a private route. Public issues and pull requests are not the place for vulnerability details, credentials, tokens, private source, customer data, private repository or site identities, signed URLs, or full production logs.

The same boundary applies during development and review. Code, scripts, workflows, hooks, package commands, and instructions introduced by an untrusted pull request are untrusted until reviewed.

PR-controlled commands should run only in an isolated, credential-free environment appropriate for untrusted code. CI is useful only when it provides the same containment and cannot expose persistent trusted state or secrets. A human saying “run it” can authorize execution; it cannot make an unsafe execution environment safe.

## Contributions are welcome, but the project contract still matters

RAN repositories are public working projects, not anonymous code drops. Contributions should be focused, reviewable, and aligned with the repository they change.

A project may define its own contribution, support, security, release, and development guidance. Those local documents exist because the details really do differ between projects: supported versions, commands, package managers, integration environments, release topology, and user-facing support boundaries are not organization-wide constants.

The shared community baseline still applies: be respectful, keep sensitive material out of public intake, use the correct support or security route, and do not weaken mandatory engineering checks in contribution guidance.

Review, a response to an issue, or discussion of a feature does not create a promise to merge, release, support, or deliver it.

## Humans and agents review against the same standard

Agent review is part of the normal engineering workflow, not a separate lower-trust shortcut.

RAN review should look at correctness, security, architecture, readability, dependencies, tests, compatibility, dead code, performance where relevant, and the evidence used to claim a change is safe.

A review is tied to the exact revision that was reviewed. If the base or head changes, the previous verdict may be stale and affected checks need to be reconsidered.

Reviewers should also inspect changed instruction-bearing files before following them. A pull request must not be able to redefine the rules used to judge itself simply by changing an `AGENTS.md`, workflow, local skill, prompt, or contribution document.

The goal is not to manufacture comments. A clean change should be approved cleanly; a real defect should be explained with its impact and a concrete remedy.

## Quality is proved, not assumed

Commands such as `composer check`, `pnpm check`, or another project aggregate are useful contracts, but the command name is not evidence by itself.

The repository should make clear what its aggregate checks actually cover, and CI should include the additional checks required by that product: static analysis, integration tests, compatibility matrices, generated assets, package verification, Plugin Check, runtime installation, or release proofs where applicable.

Local development and CI should tell the same story. Dependencies should come from tracked lockfiles where the ecosystem supports them, declared toolchain versions should match what CI executes, and reusable workflows and third-party Actions should be pinned immutably where they form part of the trust boundary.

Where a repository ships an installable artifact, confidence in the source tree is not enough. The artifact and, where useful, a clean installation of it should be proved too.

## Merge protection is part of the engineering system

A green local command is useful evidence; it is not the whole merge contract.

Maintained repositories should use GitHub checks and branch or ruleset protection appropriate to the project so required evidence cannot simply be skipped. Review threads that contain required findings should be resolved before merge, and strict status policies may require a branch to be current with its target before otherwise successful checks count.

The exact merge method may differ by repository, but final history should remain intentional. RAN uses Conventional Commits as the common history baseline, including squash-merge PR titles where that title becomes the final commit.

Release automation and deployment are separate from review. Passing review authorizes a change to progress; it does not silently authorize a release.

## The repository remains authoritative

This document describes the RAN stance. It does not replace the engineering contract of an individual repository.

Repository-local `AGENTS.md`, CI, lockfiles, runtime declarations, tests, release documentation, and contribution guidance remain authoritative for project-specific requirements. Shared RAN standards are a minimum, not a reason to remove a stronger local gate that has already been adopted.

Exceptions should be narrow and concrete. A compatibility constraint, generated file, fixture contract, legacy migration, or unusual runtime boundary can justify a local exception. “This repository has always done it differently” is not enough on its own.

## What I am trying to optimize for

I do not want RAN repositories to accumulate process for its own sake. I do want someone looking at a change—human or agent—to be able to answer a few important questions without guesswork:

- What is this change trying to do?
- What could it break?
- What evidence says it works?
- What security boundary does it cross?
- What version of the code was actually reviewed and tested?
- What still needs a project-specific check before merge or release?

If those answers are clear, the tooling is doing its job.

The detailed community, security, quality, CI, and repository-specific standards live alongside this document in the organization `.github` repository and in each project's own documentation. This page is the short version: the common engineering stance they are meant to implement.
