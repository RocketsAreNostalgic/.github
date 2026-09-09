# RAN Community Standards

## Status and scope

This document defines the organization-wide community-health baseline for Rockets Are Nostalgic (RAN) repositories.

GitHub uses the community-health files in this public `.github` repository as defaults when a repository does not provide its own file of the same type. Repository-local files are allowed and are expected where project-specific contribution, support, release, or security guidance is needed.

For public, supported RAN and legacy TNY WordPress plugins, this baseline is mandatory. Those repositories must either inherit the complete organization defaults or provide local equivalents that preserve the requirements below.

Private, fixture, archived, or intentionally unsupported repositories may use a reduced local intake surface when public contribution and support are not offered. Before such a repository becomes publicly supported, its community-health surface must be brought into compliance with this standard.

## Authority and precedence

Community-health guidance does not replace a repository's engineering contract.

1. Repository-local `AGENTS.md`, CI configuration, lockfiles, and project documentation are authoritative for development and validation requirements.
2. Repository-local community-health files override the organization defaults where GitHub supports an override.
3. Local overrides may add project-specific requirements, but must not weaken the safety, privacy, disclosure, or conduct boundaries in this standard.
4. The organization defaults provide the safe minimum when no local equivalent exists.

A local `CONTRIBUTING.md` or pull-request template should therefore name the actual checks required by that repository rather than copying commands from another project.

## Required community-health surface

Public, supported RAN WordPress plugins must provide, locally or by inheritance:

- `CODE_OF_CONDUCT.md`
- `CONTRIBUTING.md`
- `SUPPORT.md`
- `SECURITY.md`
- a bug-report issue form
- a feature-request issue form
- a support-question issue form
- a detail-free security-reporting-help form
- issue chooser configuration
- a pull-request template

The repository README should link to the applicable contribution, support, and security policies when local versions exist. WordPress.org-facing `readme.txt` files should expose the appropriate support and security routes where doing so is useful to installed users.

## Conduct

RAN uses Contributor Covenant 2.1 as the organization baseline.

Conduct reports must use the private enforcement route in `CODE_OF_CONDUCT.md`. Public issues and pull requests are not an appropriate channel for conduct complaints containing private or sensitive information.

## Public support and disclosure safety

Public issues and pull requests must never contain information that should remain private merely because it would make reproduction easier.

The following organization-wide rules apply to every public intake surface:

- Never publish credentials, tokens, webhook secrets, WordPress salts, database contents, customer data, signed URLs, private source, release assets that are not already public, or other secrets.
- Never publish private repository identities or private site identities. Replace them with neutral labels and reduce the report to a non-sensitive reproducer.
- Never publish full production logs, private workbench material, Dex identifiers, or similarly unnecessary internal context.
- Vulnerability details, exploit steps, and sensitive reproduction traces must never be submitted through ordinary public issues or pull requests.
- If a useful reproducer cannot be produced without private material, do not publish that material. Use an appropriate private route instead.

These are unconditional redaction rules. A public issue or pull request may not create a "needed for reproduction" exception for private repository or site identity.

## Security reporting

Security reports should use the repository's private vulnerability-reporting capability when it is enabled.

If a private GitHub reporting form is unavailable, the public fallback must contain no vulnerability details. The reporter may only request a confidential contact route using the `Security reporting help` form or an equivalent detail-free mechanism.

Every security route advertised by a repository must actually exist and be reachable. Repository-local `SECURITY.md` files should provide the most concrete private route available for that repository and state which releases receive security fixes.

## Contribution and validation guidance

`CONTRIBUTING.md` must remain aligned with the repository's actual development contract.

- Follow the repository's `AGENTS.md` where present.
- Install dependencies from tracked lockfiles.
- Run the repository-required pre-commit and CI-equivalent checks before proposing a change.
- Do not make mandatory project gates conditional in `CONTRIBUTING.md` when `AGENTS.md` or CI requires them unconditionally.
- Add focused runtime, integration, compatibility, generated-artifact, or release proofs when the repository contract requires them.
- Follow the repository's commit and release conventions; use Conventional Commits where the repository uses Release Please or otherwise requires them.
- Never commit secrets, private runtime state, or generated release artifacts unless the repository explicitly tracks that artifact class.

The organization default deliberately avoids prescribing technology-specific check commands. Local plugin policies should name the exact Composer, pnpm, PHPUnit, WordPress integration, parity, or other gates that apply to that repository.

## Issue templates

The default issue chooser disables unrestricted blank external issues and provides bounded forms for bugs, features, support, and security-reporting help.

Every public issue form must:

- state that vulnerabilities do not belong in the form;
- prohibit sensitive material and private repository/site identities;
- require neutral labels for private identities;
- include an appropriate safety acknowledgement before submission.

A repository may replace the default forms with project-specific versions, for example to request WordPress, PHP, database, plugin, or provider versions.

Important: if a repository defines any valid local issue template or local `.github/ISSUE_TEMPLATE/config.yml`, GitHub does not combine it with the organization default issue-template set. The repository is therefore responsible for providing the complete local intake surface it needs and preserving every safety boundary above.

## Pull requests

The organization pull-request template establishes the minimum review context:

- summary and rationale;
- verification performed;
- confirmation that applicable repository-required checks were run;
- documentation impact;
- confirmation that no secrets, sensitive material, private repository/site identities, or vulnerability details were included;
- acknowledgement that review does not itself authorize merge or release.

Repository-local PR templates may add project-specific checks, but must retain the disclosure-safety boundary.

## Review standard

Community-health changes should be reviewed against this document as an organization baseline.

A reviewer should treat the following as defects rather than stylistic preferences:

- a public intake path that permits sensitive or private identity disclosure;
- a security or support route that is advertised but unavailable;
- a public issue form that omits the security boundary;
- a PR template that permits private repository/site identity or vulnerability disclosure;
- contribution guidance that weakens mandatory repository checks;
- a partial local issue-template set that unintentionally suppresses required organization defaults.

Repository-specific wording, diagnostic fields, validation commands, supported versions, and support scope may differ where those differences reflect the actual project contract.
