# RAN community inheritance and overrides

## Status and scope

GitHub inherits community-health defaults from this public organisation `.github`
repository when no local equivalent exists. Every RAN public intake surface must
preserve the [support disclosure rules](../SUPPORT.md), [private security route](../SECURITY.md)
and [Contributor Covenant 2.1 conduct rules](../CODE_OF_CONDUCT.md). These are
unconditional boundaries, including no public private-identity disclosure for
reproduction; local wording cannot weaken them.

## Authority and precedence

Local `AGENTS.md`, CI, lockfiles and project guidance govern development.
[Contributing](../CONTRIBUTING.md) defines the shared contribution/review baseline.
Local community files override inherited files only where GitHub supports it;
they may add product requirements but cannot weaken safety, privacy, disclosure,
conduct or mandatory engineering gates.

## Required community-health surface

Public supported RAN and legacy TNY WordPress plugins must inherit or supply:

- `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `SUPPORT.md`, `SECURITY.md`;
- bug, feature, support and detail-free security-help issue forms;
- issue chooser configuration and a pull-request template.

Private, fixture, archived or intentionally unsupported repositories may reduce
intake when public contribution/support is not offered; bring the full surface
into compliance before public support. Name exclusions in [#62](https://github.com/RocketsAreNostalgic/.github/issues/62)
with dated evidence; an exclusion is not certification.

## New repositories and local overrides

New/generated repositories inherit the defaults [regardless of visibility](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file),
subject to the reduced-intake scope above. Do not copy generic files: a local
override needs a documented product reason. Check recognised root, `docs/` and
`.github/` locations before adding/removing overrides; each can shadow defaults.
A removed local file is not inherited as a repository-relative path: repair
links to the canonical organisation URL. READMEs should link local contribution,
support and security policies; WordPress `readme.txt` should expose useful routes.

<a id="conduct"></a>
<a id="public-support-and-disclosure-safety"></a>
<a id="security-reporting"></a>

## Reporting routes

Follow the linked support, security and conduct policies. Advertised support and
security routes must exist and be reachable. Local `SECURITY.md` must name the
most concrete available private route and supported security-fix releases.
When private reporting is unavailable, public security help requests may only
ask for a confidential route without vulnerability details.

<a id="contribution-and-validation-guidance"></a>

## Issue templates

The default chooser disables unrestricted blank external issues. Any valid local
issue template or `.github/ISSUE_TEMPLATE/config.yml` suppresses the inherited
set: GitHub does not combine them. Supply the complete required local surface.
Every public form must exclude vulnerabilities and sensitive material, require
neutral labels for private identities and include a safety acknowledgement.
Product-specific diagnostic fields may differ.

## Pull requests

Retain summary/rationale, verification, confirmation of required checks,
documentation impact, disclosure-safety confirmation and acknowledgement that
review does not authorize merge or release. Local templates may add checks;
local contribution guidance must name actual project commands without making
mandatory gates conditional.

## Review standard

Missing safety boundaries, unavailable routes, weakened required checks or
partial local template sets are defects. Diagnose against the authoritative
health files above; do not duplicate their full text into another policy.
