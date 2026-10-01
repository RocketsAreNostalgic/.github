# Opt-in Booster library quality recipe

This bounded recipe was authorized under #111 on 1 October 2026. Its first and only
approved consumer is the GitHub Provider pilot, PR #40. It moves that pilot's
repeated setup and phase controls into one maintained action. It does not replace
`quality-php-library-v2.yml`, change its consumers, or authorize wider adoption.

## Contract and use

`.github/actions/booster-library-quality/action.yml` is a composite action with two
required inputs: `php-version` (8.2 or 8.5) and `booster-sha` (40 lowercase hex
characters). It fixes Node at 24.11.0, PHP extensions at zip, Composer at v2, the
host repository at `RocketsAreNostalgic/ran-booster`, and the commands at
`composer check`, independent broad PHP syntax checking, then `composer check:host`.
There are no command hooks, optional phases, caches, artifacts or release outputs.
A future consumer with different requirements needs a separately reviewed scope.

The action checks out the exact PR head (or non-PR event SHA) into `package`,
verifies it and the locked manifests, provisions tools once, validates Composer,
and installs locked dependencies once. It runs the complete baseline while the
sibling `booster` checkout and Core environment are absent, then checks out and
verifies the exact candidate host and runs the host aggregate. Both checkouts
have credential persistence disabled. `pull_request_target` is rejected before
checkout. All third-party actions are pinned to full commit SHAs.

The source-quality operations are derived from `quality-php-library-v2.yml` at
`788f783d2998994f7aab9691710911ed1bd762c9`; the phase controls are extracted from
Provider PR #40 at `6773c600871ffc3bc5f3a2125096f0b75273a12e`. Future baseline
changes need deliberate review across these two shared entry points. Consumers
no longer maintain copies of the recipe or its guard. The broader v2 provider
remains unchanged to keep this pilot isolated from existing adopters.

```yaml
implementation:
  name: Implementation PHP ${{ matrix.php }}
  runs-on: blacksmith-2vcpu-ubuntu-2404
  timeout-minutes: 15
  permissions:
    contents: read
  strategy:
    fail-fast: false
    matrix:
      php: ['8.2', '8.5']
  steps:
    - uses: RocketsAreNostalgic/.github/.github/actions/booster-library-quality@<reviewed-full-commit-sha>
      with:
        php-version: ${{ matrix.php }}
        booster-sha: <reviewed-candidate-Core-commit-sha>
```

A composite action preserves existing caller job/check names, but cannot set job
permissions, runner selection, timeout, matrix or terminal admission. Each caller
must retain the reviewed ephemeral Linux runner above, read-only contents with
all other implementation-job permissions disabled, both PHP lanes, fail-fast
false, and a terminal gate that requires all lanes to succeed even after a failure,
skip or cancellation. No secrets, privileged environments or preceding project
commands belong in this job. Reserve `package` and `booster` paths and invoke the
recipe once per job. Local development continues to use the package aggregates.

This is an opt-in specialist step abstraction, not the organisation-required
workflow/enforcement wrapper described in QUALITY_WORKFLOWS.md. Its caller is
part of the reviewed quality contract. It cannot enforce its own pin or prevent a
PR from replacing its caller or aggregate commands. Review remains necessary.
Provider separately retains its no-vendor host-contract runner, release
classification/canonical dispatch admission and required lowercase `quality`.
Archive, clean installation, platform and privileged release boundaries stay
separate; this recipe produces candidate-source evidence only.

## Shared-state trade-off

The extracted guard compares tracked source bytes, locked dependency bytes and
symlink targets, and the baseline's GitHub environment/path command files. It
refuses missing/failed baselines, wrong identities, changed locks/dependencies and
phase state inside the source checkout. These controls detect accidental drift.
They are not authentication or a hostile-code sandbox: phases share a runner UID,
filesystem and environment, and hostile code can forge snapshots or change other
state. Centralizing the script does not restore process isolation. Sequential
phases also couple retries and can increase elapsed CI time.

The ten paired Provider prototype runs observed 108.5 seconds less summed job
execution on average and 6.7 seconds more elapsed group span. These are historical
topology measurements, not measurements of this new shared revision, billed
minutes, or a proven PHP 8.5 provisioning fix. The run-linked report remains in
Provider's `docs/ci-provisioning-pilot.md`. No broad savings forecast follows.

## Validation, upgrades and rollback

Run on Linux with Bash/GNU utilities, Git and Node 24.11.0:

```sh
bash -n .github/actions/booster-library-quality/ci-quality-phase.sh
node --test quality-enforcement/test-booster-library-quality.mjs quality-enforcement/test-ci-quality-phase.mjs
```

The contract workflow runs these checks on PRs and main changes. The executable
phase fixtures use disposable repositories and command doubles; the input tests
execute the action's actual validation shell. Real Provider PHP 8.2/8.5 CI must
also pass against the exact central pin, with full baseline, PHPStan and PHPUnit,
and unchanged separate host-contract/classification/terminal gates. Central tests
own recipe behavior; consumer tests own the pin, matrix, Core identity and gates.

Land the central PR with a **merge commit**, per CONTRIBUTING.md, preserving the
reviewed action commit reachable from main. Then land the qualified Provider
opt-in with its normal approved method. If the action changes during review,
update the Provider pin and requalify both exact revisions. No mutable tag/main
pin, automatic rollout, ruleset change or release publication is part of this work.

Rollback recipe extraction by restoring Provider's qualified local pilot at
`6773c600871ffc3bc5f3a2125096f0b75273a12e`; rollback consolidation entirely by
restoring its split topology/shared pin at `556f19923f6564f1bbd5cecee089d6b136afc5cd`.
Keep terminal admission, separate host contract, classification and both PHP lanes
in either case. Existing consumers need no change; keep central commits reachable.
#111, #65 and Provider #38 remain open for their wider work.
