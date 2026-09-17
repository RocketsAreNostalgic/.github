# Required quality enforcement contracts

This directory is the organisation-owned integrity layer used by the required
quality workflow proof under `.github#12`.

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
transitional approval boundary; silently allowing those files to change would
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

## Proof strategy

The rollout uses disposable target-repository pull requests to prove the
composition before organisation rules are activated:

- **Node:** `ran-booster-release-bootstrap-templates` proves the pure pnpm
  profile. A negative proof replaces `pnpm check` with a no-op: repository-owned
  statuses still pass, while the central contract rejects the changed
  `package.json` blob before the provider is trusted.
- **WordPress:** `ran-starter-plugin` proves the mixed Composer + pnpm profile
  while its stronger archive/install evidence remains repository-owned.
- **PHP:** `ran-admin-shell` proves PHP v2 and central ownership of
  `php-floor`, `php-current`, extensions, and optional Node identity. A negative
  proof weakens the target caller's PHP floor and must be rejected by the
  central workflow even if the repository's local caller accepts it.
- **Booster:** remains the high-water composition proof for a specialist local
  topology. Its runtime/archive/release evidence is not replaced by the generic
  provider contract.

Disposable proof callers are evidence only and are closed without merge.
Organisation ruleset activation is a separate administrator action after the
proof implementation and repository contract entries have been reviewed.

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
