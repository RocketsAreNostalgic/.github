# Repository rulesets

Rulesets select evidence required before merge; [Quality Standards](QUALITY_STANDARDS.md)
defines the checks. Apply the protection contract without forcing identical
workflow topology or changing repository-specific release controls.

## Default branch protection

Maintained default branches should use an active ruleset that blocks deletion
and force pushes, requires pull requests and resolved review threads, dismisses
stale approvals, and grants no broad organisation-admin PR bypass.
`require_last_push_approval` is false by default unless a documented reason
requires it. Linear history and a second human approval are not imposed merely
for consistency. Exceptions need a current architectural reason.

## Merge methods

Product/package defaults permit squash and merge commits; prefer squash for
iterative/agent work, merge when the internal sequence matters. Rebase is not
the default. `.github` is **merge-only** because reviewed provider SHAs must
remain reachable from main. Other exact-identity exceptions must be documented;
local release-proposal merge rules remain mandatory.

<a id="check-source"></a>
<a id="multiple-required-checks"></a>

## Required status checks

Prefer one trustworthy terminal `quality` that depends on every ordinary
merge-blocking lane and fails unless all succeed. Otherwise retain the underlying
required checks. Bind Actions-produced checks to **GitHub Actions** as expected
source; an arbitrary integration emitting the same name must not satisfy them.

Distinct lifecycle/security gates may remain separate, including conditional
archive or release-candidate evidence. Bootstrap's established `Pack inputs`
and `Quality` requirements remain until the #31 decision; the existence of its
new diagnostic terminal does not authorize removing them. A local status is
not proof of organisation-owned workflow identity.

## Review automation

Copilot review may remain enabled without re-reviewing every push; automatic
re-review is not an organisation requirement. Stale human approvals must still
be dismissed. This does not waive independent review where the applicable
protected-contract boundary requires it.

<a id="repository-profiles"></a>
<a id="relationship-to-ci-policy"></a>

## Activation and scope

Follow [enforcement integrity](QUALITY_STANDARDS.md#enforcement-integrity):
organisation-controlled workflow identity and transitive contract protection
must both exist before treating organisation-required checks as the sole merge
security boundary. The [registry design](../../quality-enforcement/README.md)
is dormant; [#31](https://github.com/RocketsAreNostalgic/.github/issues/31) owns
activation and [#139](https://github.com/RocketsAreNostalgic/.github/issues/139)
owns proportionality assessment. This guidance does not activate settings.

Unresolved protection remediation remains in [#16](https://github.com/RocketsAreNostalgic/.github/issues/16)
and #31; this reference does not close it. Deferred repositories are not enrolled
without a new decision. Archived repositories/fixtures are outside active
normalization unless restored; private maintained repositories follow the same
principles, with plan/API limitations recorded instead of claimed protection.

Consult actual rulesets and owning issues for implementation state. Historical
[activation history](https://github.com/RocketsAreNostalgic/.github/issues/31)
is optional evidence, not another maintained inventory. Review settings against
these requirements; a successful workflow cannot prove live protection.
