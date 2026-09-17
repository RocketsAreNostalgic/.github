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
- the reviewed source commit from which the approval was derived; and
- exact Git object IDs for the repository-owned files or trees that determine
  the authoritative quality contract.

A required workflow owned by this repository checks out the exact target
revision and this policy repository at `job.workflow_sha`, then runs
`validate-contract.mjs`. The validator resolves each protected target path from
`HEAD` and requires its Git object type and object ID to match the central
registry before the shared quality provider is allowed to run.

The provider inputs also come from the central registry. In particular, a PHP
consumer cannot weaken its own floor/current inputs in a target-repository pull
request and a Node consumer cannot substitute a different pnpm identity through
its caller.

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
- scripts transitively invoked by the aggregate; and
- tests/fixtures that constitute the authoritative behavioural or contract
  harness.

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

When a protected target object needs to change:

1. make the target-repository change in its normal pull request;
2. review the new quality semantics and complete the repository's ordinary CI;
3. derive the new protected object IDs from the exact reviewed target revision;
4. update `contracts.json` in a separate reviewed `.github` change;
5. only after the central contract is approved should the target change become
   eligible under the organisation-required workflow; and
6. retain stronger repository-specific required checks independently unless an
   explicit later review proves them redundant.

The registry update is therefore an explicit organisation-policy decision, not
a way for the target pull request to approve itself.

## Representative proof evidence

The three supported profiles have each been exercised through a disposable
pull request with the same positive / negative / restored pattern. The proof
callers are evidence only and were closed without merge.

### Node — Bootstrap Templates

`ran-booster-release-bootstrap-templates#21` proves the pure pnpm profile.

- approved-contract required-workflow run `35229917347` succeeded;
- commit `6a369cf16b0e0a4a10d0fc6f271f9826d444e28c` changed only
  `package.json#scripts.check` from `pnpm test` to `true`;
- repository-owned run `35230167165` still passed `Pack inputs`, shared Node
  quality, `Quality`, and terminal `quality`;
- organisation run `35230167761` rejected the changed `package.json` blob before
  running the organisation Node baseline; and
- restored required-workflow run `35230315256` succeeded.

The protected Node surface includes the complete `tests` and `scripts` trees so
the aggregate cannot be weakened indirectly through a helper that its protected
test harness executes.

### PHP library — Admin Shell

`ran-admin-shell#12` proves PHP v2 and central ownership of `php-floor`,
`php-current`, extensions, and optional Node identity.

- approved-contract repository run `35232299642` and required-workflow run
  `35232299880` succeeded;
- commit `71a5e38b73b9b03783d7c4936d163996443ab444` changed only
  `composer.json#scripts.check` to `true`;
- repository-owned `Quality` run `35232546187` still succeeded;
- organisation run `35232546416` rejected the changed `composer.json` blob and
  skipped the PHP baseline; and
- final restored head `fc60b04816c2fd130c8f63b36364da9f1d5398c6`
  passed repository run `35232974087` and required-workflow run `35232974291`.

### WordPress plugin — Starter

`ran-starter-plugin#21` proves the mixed Composer + pnpm profile while Starter's
stronger archive/install evidence remains repository-owned.

- approved-contract repository run `35232373052` and required-workflow run
  `35232372886` succeeded;
- commit `1503ac6007128eb119655fbbd8428568e3e436b8` changed only
  `package.json#scripts.check` to `true`;
- repository run `35232631692` still passed the shared WordPress baseline,
  project-specific archive/install evidence, and terminal `quality`;
- organisation run `35232632076` rejected the changed `package.json` blob and
  skipped the organisation WordPress baseline; and
- final restored head `49db641d73fbe962e0cddd37486f181ca766c06f`
  passed repository run `35232928169` and required-workflow run `35232929039`.

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

Consumer repositories must not treat a local job named `quality` as a
substitute for this boundary. Local terminal jobs remain useful diagnostics and
repository merge evidence, but the organisation enforcement authority is the
required workflow plus this protected contract.

## Rollout

Organisation ruleset activation is an administrator action after the required
workflow implementation and each target repository's contract entry have been
reviewed. Enrol repositories incrementally:

1. classify the repository against one of the supported profiles;
2. audit its complete transitive authority-bearing quality surface;
3. add and review its central contract entry;
4. prove the required workflow on that exact repository before targeting it;
5. add the repository to the matching organisation required-workflow rule; and
6. keep stronger local required checks until a separate review demonstrates
   that any one of them is truly redundant.

Do not target a repository that has no entry in `contracts.json`; the validator
will deliberately fail closed with `No approved quality contract`.
