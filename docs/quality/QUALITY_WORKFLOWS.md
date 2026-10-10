# Reusable quality workflow reference

[Quality Standards](QUALITY_STANDARDS.md) defines required outcomes. This reference
explains the existing providers and what their code establishes. Product-specific
archive, installed-runtime, database, host, Windows, release and deployment checks
stay in consumer repositories and feed their required merge evidence.

## Choose a provider

Choose by maintained source, not merely existing manifests. Generated assets alone
do not create a frontend toolchain requirement; missing package metadata does not
excuse checks for maintained frontend source.

| Workflow in `.github/workflows/` | Applicable contract | Diagnostic contexts with caller job `baseline` |
| --- | --- | --- |
| `quality-php-library-v2.yml` | PHP libraries and PHP-only WordPress source; separate configured PHP floor/current lanes, local WordPress evidence retained. | `baseline / PHP <floor> floor`, `baseline / PHP <current> compatibility` |
| `quality-wordpress-plugin.yml` | Mixed WordPress PHP and maintained frontend; Composer plus locked pnpm. Product compatibility matrices remain local. | `baseline / RAN WordPress Plugin Quality` |
| `quality-node.yml` | Maintained pnpm projects; another manager needs a justified equivalent local contract. | `baseline / RAN Node Quality` |

Use the supported providers listed above and their emitted status contexts.
A new provider generation requires a substantive contract change. Specialist
local workflows may substitute
only when every applicable transferable guarantee is demonstrated; extra product
checks alone do not justify dropping the shared baseline. This permits shared
package self-tests and Booster's richer composition while preserving parity.

## Provider execution and limits

The providers reject `pull_request_target` before checkout and verify the exact
PR head, or `github.sha` for other events. They pin third-party Actions, use
read-only contents permission, disable persisted checkout credentials and own
runner selection. Callers cannot choose another source revision, arbitrary
quality command, skip flag or privileged/self-hosted runner.

Composer profiles require tracked manifests and lockfiles, run
`composer validate --strict --no-check-publish --no-check-all`, install from the
lock and invoke `composer check`. pnpm profiles require manifests and a lockfile, compare
requested pnpm with `packageManager`, verify the installed version, use frozen
installation and invoke `pnpm check`.

PHP profiles additionally run `php -l` over discovered `*.php` files outside
the root `vendor` and `node_modules` directories.
**This is not complete maintained-PHP discovery:**
it does not select PHP files with other extensions or no extension, including
mixed-content templates outside the `*.php` pattern. A parser failure in a
selected file fails the check. All three PHP syntax steps write the NUL-separated
file list to a temporary file in a checked command before parsing it, so discovery
failures also fail the step. [PR143](https://github.com/RocketsAreNostalgic/.github/pull/143)
delivered this repair; the earlier process-substitution loop could hide a failing
`find`. Existing immutable consumer pins require separate adoption of a repaired
provider revision.

Consumers remain responsible for complete maintained-file coverage, including
PHP outside the `*.php` pattern. [#136](https://github.com/RocketsAreNostalgic/.github/issues/136)
records the delivered consumer repairs and adoption dispositions. A passing
provider or aggregate check does not prove that all required files were selected.

Exact-head proof is separate from mergeability. Strict integration rules or a
merge queue must establish freshness against the target branch; add product
integration proof where needed. Provider source inspection does not establish
live ruleset activation, consumer scope or full-estate acceptance.

## Inputs and caller examples

Inputs describe project/toolchain identity and working directory. Review them
against the consumer support contract: PHP floor/current are **not** derived from
or checked against Composer support declarations. Node/pnpm providers use the
specified Node-version file; truthful exact/stable Node declarations remain a
consumer obligation. The shared development minimum is Node 24.21.0 within Node 24 LTS.
PHP v2 defaults to 24.21.0 and verifies a nonempty Node input as exact
`major.minor.patch`; pure-PHP callers explicitly pass `node-version: ''`.
Node and mixed callers pin 24.21.0 in their package toolchain metadata.
Existing immutable provider pins adopt this default only when deliberately
updated to a qualified provider revision.

Pin every provider to a reviewed full commit SHA. Tags are optional provenance
comments, not execution references. For example:

```yaml
jobs:
  baseline:
    uses: RocketsAreNostalgic/.github/.github/workflows/quality-php-library-v2.yml@<reviewed-full-commit-sha>
    with:
      php-floor: '8.2'
      php-current: '8.5'
      php-extensions: zip
      node-version: ''
```

These are example support inputs, not organisation-wide support floors. A Node
caller selects `quality-node.yml` and its exact declared `pnpm-version`; a mixed
WordPress caller selects `quality-wordpress-plugin.yml`, `php-version` and exact
`pnpm-version`. Optional `node-version-file` and `working-directory` must identify
the actual checked project. Inputs never override the manifest's package-manager
identity. Provide the required locks and metadata, and ensure aggregate commands run the
claimed checks. Do not select a weaker provider to avoid these requirements.

## Consumer aggregation and protection

A local terminal `quality` depends on every ordinary merge-blocking lane and
fails unless all succeed. Preserve stronger local checks and distinct conditional
release gates. Its status is useful evidence, not unforgeable workflow identity.
Follow [ruleset policy](REPOSITORY_RULESETS.md) and
[enforcement integrity](QUALITY_STANDARDS.md#enforcement-integrity).

Review the complete chain of delegated behavior: aggregate commands,
dependencies, lockfiles, configuration, helpers, tests and workflow callers.
Also review inputs identifying the checked project and environment, including
PHP ranges and extensions, Node and pnpm versions, working directory and support
declarations. Accepting an input does not independently prove its truth.
Organisation-required execution must come
from organisation-controlled repository/branch/workflow configuration, with any
reusable delegation pinned immutably. The separate
[registry implementation](../../quality-enforcement/README.md) is dormant pending
[#31](https://github.com/RocketsAreNostalgic/.github/issues/31) and
[#139](https://github.com/RocketsAreNostalgic/.github/issues/139); it supplies no
current activation claim.

## Inspected implementation

Current mechanisms: [organisation workflow sources](../../.github/workflows),
[shared WordPress rules](https://github.com/RocketsAreNostalgic/ran-coding-standards/blob/main/RANWordPress/ruleset.xml),
[owned-method checker](https://github.com/RocketsAreNostalgic/ran-coding-standards/blob/main/RANOwnedMethods/Sniffs/NamingConventions/ValidMethodNameSniff.php)
and [package controls](https://github.com/RocketsAreNostalgic/ran-coding-standards/blob/main/tests/run.php).

| Evidence group | What it establishes and limits |
| --- | --- |
| Organisation providers at [ff58c659264cf1b7dcb78c130c1dd8def4579a33](https://github.com/RocketsAreNostalgic/.github/tree/ff58c659264cf1b7dcb78c130c1dd8def4579a33/.github/workflows): `quality-node.yml`, `quality-php-library-v2.yml`, `quality-wordpress-plugin.yml` | Inspected source establishes the checkout, input, install, fixed-command and checked PHP-discovery mechanisms above. [PR143's contract](https://github.com/RocketsAreNostalgic/.github/blob/ff58c659264cf1b7dcb78c130c1dd8def4579a33/quality-enforcement/test-php-syntax-contract.py) exercises the three actual PHP syntax steps, including discovery and parser failures. This does not establish complete maintained-file selection, consumer pin adoption, support metadata validation or organisation activation. |
| Shared PHP rules at [4fb34cf349021d6b65430a4f93ce4de3e221e0a5](https://github.com/RocketsAreNostalgic/ran-coding-standards/tree/4fb34cf349021d6b65430a4f93ce4de3e221e0a5): `RANWordPress/ruleset.xml`, `RANWordPressLibrary/ruleset.xml`, `RANWordPressPlugin/ruleset.xml`, `RANOwnedMethods/Sniffs/NamingConventions/ValidMethodNameSniff.php`, `tests/run.php` | Inspected inheritance supplies WordPress-Extra/PHPCompatibilityWP, deliberate filename/exception-data decisions and blocking alignment; opt-in owned-method checking covers inherited declarations. Package tests contain actual selection/suppression/target controls. Source inspection is not a fresh test run, consumer adoption or release qualification. |

These revisions identify inspected evidence, not new consumer pins. Mechanism
changes update this reference and its evidence in the same PR or record a
cross-repository follow-up. Unrelated source commits do not require refreshing the group.
