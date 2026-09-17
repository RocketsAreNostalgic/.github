# Required quality enforcement contracts

This directory is the organisation-owned integrity layer used by the required
quality workflows under `.github#12`.

The reusable quality providers already give RAN deterministic source-quality
execution, but they intentionally invoke repository-owned aggregate commands
such as `composer check` and `pnpm check`. Requiring the organisation workflow
identity alone therefore does not stop a target pull request from weakening its
own aggregate, configuration, test harness, helper scripts, or unvalidated
caller inputs while keeping the same displayed status names.

The protected-contract layer closes that gap without moving product-specific
quality topology into `.github`.

## Contract model

`contracts.json` contains one entry per enforcement-ready repository. Each
entry records:

- the repository quality profile;
- organisation-approved provider inputs;
- the reviewed source commit from which the approval was derived;
- exact Git object IDs for the repository-owned files or trees that determine
  the authoritative quality contract; and
- where necessary, repository-relative paths that are explicitly required to
  remain absent so a pull request cannot introduce a higher-precedence shadow
  configuration, package-manager hook, or prebuilt dependency tree.

A required workflow owned by this repository checks out the exact target
revision and this policy repository at `job.workflow_sha`, then runs
`validate-contract.mjs`. The validator resolves each protected target path from
`HEAD` and requires its Git object type and object ID to match the central
registry before the shared quality provider is allowed to run. It also checks
every `absent` path and fails if that path has appeared in the target revision.

The provider inputs also come from the central registry. In particular, a PHP
consumer cannot weaken its own floor/current inputs in a target-repository pull
request and a Node consumer cannot substitute a different pnpm identity or
working directory through its caller.

The required terminal job fails unless both protected-contract validation and
the immutable shared provider succeed.

## What belongs in the protected surface

Protect the smallest complete transitive surface that can change what the
canonical aggregate proves. Depending on the repository this normally includes:

- the local quality workflow and its provider/fan-in topology;
- `composer.json` / `package.json` aggregate definitions and quality-tool
  dependencies;
- lockfiles when they determine the quality-tool graph;
- PHPCS/WPCS/PHPCompatibility/PHPStan/ESLint/Prettier/Stylelint/test-runner
  configuration;
- package-manager project configuration and install hooks such as `.npmrc`,
  `pnpm-workspace.yaml`, and pnpm hook files;
- implicitly consumed ignore files such as `.gitignore`, `.prettierignore`, or
  `.stylelintignore` where they can change what a protected command checks;
- scripts transitively invoked by the aggregate; and
- tests/fixtures that constitute the authoritative behavioural or contract
  harness.

Dependency installation must start from the reviewed source tree and the
protected lockfiles. Tracked `vendor/` or `node_modules/` trees are therefore
required to remain absent for Composer/pnpm profiles: otherwise an installer may
reuse pre-existing metadata, binaries, or package contents instead of
materialising the reviewed dependency graph from the lock.

Some tools discover configuration by filename or precedence rather than by an
explicit protected path. In that case the contract must either protect the
selected file **and** require higher-precedence alternatives to remain absent,
or the aggregate must invoke an explicit protected configuration path. For
example, Admin Shell protects `phpcs.xml.dist` and requires `.phpcs.xml`,
`.phpcs.xml.dist`, and `phpcs.xml` to remain absent so an implicit `phpcs -p`
run cannot be redirected to a permissive shadow standard.

Likewise, a pnpm profile must not protect only `package.json` and the lockfile:
a newly introduced package-manager config or hook can change how the protected
aggregate executes without changing either file. Existing package-manager
configuration belongs in `objects`; unapproved alternative config/hook paths
belong in `absent`.

A whole Git tree object is appropriate when every file below that directory is
part of the authority-bearing harness. This deliberately means a legitimate
change to that harness requires a central contract refresh. That is the
protected approval boundary; silently allowing those files to change would
recreate the bypass this mechanism exists to prevent.

Do **not** protect ordinary product implementation merely because tests execute
it. Product/source changes must remain reviewable in the target repository
without a `.github` registry update. Protect the harness that decides whether
those changes pass, not the product being tested.

## Approval lifecycle

When a protected target object or required-absent policy needs to change:

1. make the target-repository change in its normal pull request;
2. review the new quality semantics and complete the repository's ordinary CI;
3. derive the new protected object IDs and required-absence rules from the exact
   reviewed target revision;
4. update `contracts.json` in a separate reviewed `.github` change;
5. prove that central candidate against the unchanged exact target revision;
6. only after the central contract is approved should the target change become
   eligible under the organisation-required workflow; and
7. retain stronger repository-specific required checks independently unless an
   explicit later review proves them redundant.

The registry update is therefore an explicit organisation-policy decision, not
a way for the target pull request to approve itself.

### Stale or superseded approvals

A registry entry approves the exact Git objects derived from one reviewed target
revision. It is not an approval of a mutable branch name.

- If the target PR head changes after the contract objects are derived, the
  central registry change is stale. Re-derive the contract from the new exact
  head and repeat review/proof; do not reuse the previous approval.
- If the target PR is abandoned, superseded, or closed before the registry
  change lands, close the corresponding central approval rather than carrying
  speculative object IDs forward.
- If a central contract entry has already landed for a target revision that will
  not land, restore the entry from the target repository's current approved
  default-branch contract in a separate reviewed `.github` change and canary the
  restored entry before expanding enforcement.
- After a central contract refresh lands, rerun the required workflow on the
  unchanged target head. A subsequent target-head change restarts the approval
  cycle.

`approved_commit` records the provenance of the reviewed contract; enforcement
still relies on the exact protected object IDs, required-absence policy, and
centrally owned provider inputs.

## Control-plane canary procedure

The required workflows, validator, registry schema, and contract semantics form
a high-blast-radius enforcement control plane. Material changes must be proven
before estate-wide rollout.

1. Create the central change on a reviewed `.github` branch and freeze its exact
   candidate SHA.
2. Exercise every affected profile through an enrolled representative repository
   using a disposable caller pinned to that exact central SHA.
3. Require a positive exact-contract pass through the protected-contract check,
   immutable provider, and terminal `required-quality` job.
4. When the change addresses a bypass class, include a negative proof showing
   the weakened/shadowed contract fails before the organisation baseline is
   trusted.
5. Restore the representative contract and prove it green again on the same
   central candidate.
6. Merge the central change only after representative proof and review are
   clean; then stage organisation-rule expansion incrementally rather than
   targeting the whole estate at once.

PR #28 established the initial Node, WordPress, and PHP-v2 representative
pattern using Bootstrap Templates, Starter, and Admin Shell respectively.

## Emergency rollback

A defective central enforcement change must be recoverable without weakening
repository-owned quality rules.

1. An organisation owner/admin may temporarily disable the affected required
   workflow rule, or remove only the affected repositories from that rule, to
   stop a central control-plane defect from blocking unrelated product work.
2. Leave all stronger repository-local required checks, review requirements, and
   merge policies in place during that temporary disablement.
3. Revert or correct the defective `.github` change through the normal reviewed
   pull-request path; do not patch consumer repositories to manufacture a bypass.
4. Re-run the representative canary set against the exact repaired/reverted
   central revision.
5. Re-enable the organisation rule only after the restored control plane is
   proven green.

Temporary disablement is an emergency recovery action, not an alternate merge
path. It must be narrow, owner/admin-controlled, and followed by restoration of
the organisation-required boundary.

## Protected-surface re-audit

Re-audit a repository's authority-bearing surface whenever its contract is
refreshed and during each enforcement rollout wave. Also re-audit after material
provider, package-manager, test-runner, lint/format tool, or configuration-format
changes.

The audit should actively look for new implicit inputs rather than only comparing
the existing registry: higher-precedence config names, ignore files, package
manager hooks, helper scripts, test/fixture trees, generated command wrappers,
and prebuilt dependency directories can all change what the aggregate proves.
Any newly authoritative input must be protected as an exact object, required to
remain absent, or removed from implicit discovery by an explicit protected
command/configuration path.

## Representative proof evidence

The three supported profiles have each been exercised through a disposable
pull request with positive / negative / restored evidence. The proof callers are
evidence only and were closed without merge.

### Node — Bootstrap Templates

`ran-booster-release-bootstrap-templates#21` proves the pure pnpm profile.

- commit `6a369cf16b0e0a4a10d0fc6f271f9826d444e28c` changed only
  `package.json#scripts.check` from `pnpm test` to `true`;
- repository-owned run `35230167165` still passed local quality while
  organisation run `35230167761` rejected the changed protected package blob;
- a later `.npmrc` / `script-shell=/bin/true` negative proof likewise left local
  run `35235390134` green while required run `35235390672` rejected the
  required-absent shadow path; and
- final central candidate `ba124001933f7febf15262c002aefec02aab3ef8`
  passed repository run `35239134905` and required run `35239135572`.

The protected Node surface includes the complete `tests` and `scripts` trees so
the aggregate cannot be weakened indirectly through a helper that its protected
test harness executes. Package-manager shadow configuration, hook paths, and
prebuilt `node_modules/` content are centrally constrained rather than being
implicitly trusted.

### PHP library — Admin Shell

`ran-admin-shell#12` proves PHP v2 and central ownership of `php-floor`,
`php-current`, extensions, and optional Node identity.

- commit `71a5e38b73b9b03783d7c4936d163996443ab444` changed only
  `composer.json#scripts.check` to `true`;
- repository-owned `Quality` run `35232546187` still succeeded while
  organisation run `35232546416` rejected the changed Composer object before
  the PHP baseline; and
- final central candidate `ba124001933f7febf15262c002aefec02aab3ef8`
  passed repository run `35239182921` and required run `35239183776`.

Admin Shell's protected aggregate invokes
`phpunit --configuration phpunit.xml.dist` explicitly, so the protected PHPUnit
configuration does not rely on automatic filename precedence.

### WordPress plugin — Starter

`ran-starter-plugin#21` proves the mixed Composer + pnpm profile while Starter's
stronger archive/install evidence remains repository-owned.

- commit `1503ac6007128eb119655fbbd8428568e3e436b8` changed only
  `package.json#scripts.check` to `true`;
- repository run `35232631692` still passed local/shared evidence while
  organisation run `35232632076` rejected the changed protected package object;
- review identified implicit Stylelint and Prettier inputs: `.stylelintignore`
  is required absent, while the approved `.gitignore` and `.prettierignore`
  blobs are protected; and
- final central candidate `ba124001933f7febf15262c002aefec02aab3ef8`
  passed repository run `35239152367` and required run `35239152954`.

### Booster

`ran-booster` remains the high-water composition reference for a specialist
local topology. Its runtime/archive/release evidence is not replaced by the
generic provider contract. Before it is enrolled in organisation enforcement,
its corresponding central contract must preserve the applicable shared quality
authority while its stronger repository-specific rules remain required.

## Required workflow identity

Each required workflow asserts `job.workflow_repository` and
`job.workflow_file_path`, then checks out this repository at `job.workflow_sha`.
This binds contract data and validation code to the same organisation-owned
workflow revision that GitHub is executing rather than to a mutable target
branch.

The consumer-required workflows deliberately skip when `github.repository` is
`RocketsAreNostalgic/.github`; the policy repository is their source, not a
consumer contract. Organisation rules must likewise target enrolled consumer
repositories rather than treating the policy repository as a consumer.

Consumer repositories must not treat a local job named `quality` as a
substitute for this boundary. Local terminal jobs remain useful diagnostics and
repository merge evidence, but the organisation enforcement authority is the
required workflow plus this protected contract.

## Rollout

Organisation ruleset activation is an administrator action after the required
workflow implementation and each target repository's contract entry have been
reviewed. Enrol repositories incrementally:

1. classify the repository against one of the supported profiles;
2. audit its complete transitive authority-bearing quality surface, including
   implicitly discovered package-manager/tool configuration, ignore files, hook
   paths, and pre-existing dependency trees;
3. add and review its central object and required-absent contract entries;
4. prove the required workflow on that exact repository before targeting it;
5. add the repository to the matching organisation required-workflow rule; and
6. keep stronger local required checks until a separate review demonstrates
   that any one of them is truly redundant.

Do not target a repository that has no entry in `contracts.json`; the validator
will deliberately fail closed with `No approved quality contract`.
