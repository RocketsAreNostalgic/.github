# Protected quality contract implementation

**Dormant, not active organisation protection.** The required-workflow and hash
registry design is retained pending [activation #31](https://github.com/RocketsAreNostalgic/.github/issues/31)
and [proportionality assessment #139](https://github.com/RocketsAreNostalgic/.github/issues/139).
Historical canaries prove bounded mechanisms, not live enrollment or approval
to expand this system. Ordinary contribution uses
[Quality Standards](../docs/quality/QUALITY_STANDARDS.md); this reference is for
maintainers assessing or operating the design if authorized.

## Trust boundary and contract model

Requiring an organisation workflow alone does not protect PR-editable aggregates,
configs or delegated helpers. This design checks a centrally reviewed contract
before executing the provider. It is one implementation of
[enforcement integrity](../docs/quality/QUALITY_STANDARDS.md#enforcement-integrity),
not a requirement to introduce registries elsewhere.

`contracts.json` associates repository/profile and centrally owned provider
inputs with exact Git blob/tree identities and required-absent paths.
`approved_commit` records provenance; matching protected objects, absence rules
and inputs—not an entire product revision—defines approval.

Required workflows verify `job.workflow_repository`/`job.workflow_file_path`,
check out the target PR head (otherwise `github.sha`) and policy at
`job.workflow_sha`, then invoke `validate-contract.mjs`. The validator fails on
missing enrollment, wrong profile, changed object type/identity or newly present
forbidden paths. It emits the central provider inputs. Terminal `required-quality`
requires both validation and the immutable provider to succeed. `.github` itself
is deliberately skipped and must not be enrolled as its own consumer.

<a id="what-belongs-in-the-protected-surface"></a>

## Protect the smallest complete surface

Include aggregates, tool dependencies/locks, caller workflows/fan-in/inputs,
configuration, package-manager hooks, implicit ignore files, delegated scripts
and authoritative tests/fixtures. A whole tree is appropriate only when every
file under it belongs to that harness. Do not protect product implementation
merely because tests execute it.

Account for implicit precedence: protect selected configuration and require
shadow alternatives absent, or invoke an explicit protected path. A protected
manifest alone cannot stop a new pnpm hook. Tracked `vendor`/`node_modules` must
remain absent so installation materializes the reviewed locked graph rather
than reusing attacker-controlled metadata/binaries. Export attributes, nested
attribute overrides and generated wrappers can also alter what tests prove.

The retained Admin entry illustrates these boundaries: recursive CLI/tool trees,
root export attributes, absent `resources/.gitattributes`, protected PHPCS files
and forbidden alternative PHPCS filenames. Explicit PHPUnit/PHPStan configuration
paths avoid their default filename precedence. These are implementation examples,
not proof that its historical entry matches current main.

<a id="approval-lifecycle"></a>
<a id="stale-or-superseded-approvals"></a>

## Approval and changed heads

If activated, changing protected semantics follows this sequence:

1. Propose/review the consumer change and complete its ordinary CI.
2. Derive object identities, absent paths and inputs from that exact reviewed head.
3. Review a separate `.github` contract update; prove it against that target.
4. Only after central approval is the target eligible under the required workflow.
   Retain stronger local checks unless separately reviewed as redundant.

Protected objects, absence state or authority inputs changing makes approval
stale: derive/review/prove again. Product-only changes need no registry refresh,
but the workflow must rerun on the new head and revalidate the contract. Abandoned
or superseded targets require closing unlanded central approvals; if central
approval already landed, restore the approved default-branch contract through a
reviewed change and canary it before expansion. Target PRs cannot approve
themselves. This operational lifecycle is conditional on activation, not today's
ordinary contribution burden.

<a id="control-plane-canary-procedure"></a>
<a id="emergency-rollback"></a>
<a id="required-workflow-identity"></a>
<a id="rollout"></a>

## Canary, rollout and rollback

Material control-plane changes require review at an exact central SHA and an
affected-profile representative proof: positive validation/provider/terminal
success, an actual bypass negative where relevant, then restored positive
success on that same candidate. Historical proof callers are disposable and
must not become alternate production gates.

An authorized administrator enrolls incrementally only after auditing each
complete transitive surface, reviewing its entry and proving the exact target.
Do not target repositories without entries: missing contracts deliberately fail
closed. Preserve stronger local/runtime/release evidence, including Booster's
specialist composition. No historical canary authorizes activation.

For a central defect, an owner/admin may narrowly disable the affected rule or
remove affected repositories temporarily while retaining local required checks,
review and merge policies. Revert/correct centrally through normal reviewed PRs;
do not patch consumers to manufacture bypasses. Prove repaired/reverted canaries
before re-enabling. Temporary disablement is controlled recovery followed by
restoration, never an alternate merge path.

<a id="protected-surface-re-audit"></a>

## Re-audit if activated

The organisation quality programme owner (#7 or its named successor) records
protected-surface re-audit in the existing tracker at least quarterly **while
rules are active**, and at each contract refresh, rollout wave or material
provider/package-manager/tool/config-format change. No dormant quarterly process
is asserted here.

Look beyond current hashes for new implicit configuration, ignore files, hooks,
helpers, fixture trees, wrappers and prebuilt dependencies. Newly authoritative
inputs must become protected objects, required-absent paths or explicit protected
configuration. Broad historical inventories do not prove continuing completeness.

<a id="representative-proof-evidence"></a>
<a id="node--bootstrap-templates"></a>
<a id="php-library--admin-shell"></a>
<a id="wordpress-plugin--starter"></a>
<a id="booster"></a>

## Inspected source and historical proof

Current sources: [registry](contracts.json), [validator](validate-contract.mjs)
and [required/provider workflows](../.github/workflows).

At [.github 70df865a00734542e6bb663e684d86b8b4757b8e](https://github.com/RocketsAreNostalgic/.github/tree/70df865a00734542e6bb663e684d86b8b4757b8e/quality-enforcement),
inspection of `contracts.json` and `validate-contract.mjs`, alongside
[required workflow sources](https://github.com/RocketsAreNostalgic/.github/tree/70df865a00734542e6bb663e684d86b8b4757b8e/.github/workflows),
establishes the object/absence/input validation and workflow-identity mechanisms
above. It does not prove complete consumer inventories, current activation or
passing execution against current consumer heads.

[Design/canary #28](https://github.com/RocketsAreNostalgic/.github/pull/28) retains
Node, PHP-v2 and mixed WordPress positive/negative/restored runs: altered aggregates
or implicit configuration could pass local CI but fail the protected contract.
Those closed, unmerged consumer proof PRs are optional historical evidence, not
current acceptance. Their exact sources and limitations remain in that record.
Update this reference with mechanism changes or track a cross-repository follow-up;
unrelated commits do not require evidence refresh.
