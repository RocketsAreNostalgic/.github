# Shared-quality upgrades and Composer audit inventory

Owner: [organisation quality #65](https://github.com/RocketsAreNostalgic/.github/issues/65).
Snapshot: 29 September 2026 (UTC). Policy: [Quality Standards](QUALITY_STANDARDS.md#shared-package-versions-consumer-upgrades-and-live-advisories).

## Closeout decisions — 3 October 2026

The [current closeout checkpoint](PHP_QUALITY_MATRIX.md#current-closeout-proposals--3-october-2026)
records the separately qualified documentation merges and remaining proposals.
Migrator #56 is merged at `a9d2fb71f6c739278351a4af48d107ddb4973a18`;
its contract wording correction changes neither tooling nor certification.
Core #225 and #232 documentation are merged at `555d6eea` and `116b840a`
respectively; their qualification and remaining source proposal are recorded
in the matrix.
Ben approved #39/#44 administrative closure with the residual criteria retained
under #57, and rejected legacy debug-capture retention for the disposable test
sites. The resulting reader-removal source proposal still requires its own
qualification and merge decision. None of these decisions changes the accepted
tooling pins, enforced PHPStan level 1 or the release pause.

## Source integration update — 3 October 2026

Core [#230](https://github.com/RocketsAreNostalgic/ran-booster/pull/230) is now
landed at `0145bb2f9be4866e46e109cb160ed788cbc25e53`, following #228 and #229.
The final reviewed head `243b73aafdcdaeae37edf19e21698e704218e20a` and landed
commit share tree `bf2fb937d77e31bcdf9eb02450828abc1e6a66cc`. Its refreshed
local checks pass (2,615 tests / 22,502 assertions; 193 frontend tests), and
native archive, repository quality and all four installed lanes pass on the
final candidate. Exact merged-main [Quality 37103932804](https://github.com/RocketsAreNostalgic/ran-booster/actions/runs/37103932804)
also passes archive, repository quality and all four installed lanes.

The [source integration checkpoint](PHP_QUALITY_MATRIX.md#source-integration-checkpoint--3-october-2026)
records the final source tuples and qualification. Earlier candidate counts and
toolchain comparisons below remain historical; they are not silently relabelled
as post-merge results. Retained Admin Shell and frontend quality-config pins,
production dependencies, enforced PHPStan level 1 and paused release boundaries
are unchanged.

## Convergence update — 3 October 2026

The [current matrix checkpoint](PHP_QUALITY_MATRIX.md#convergence-checkpoint--3-october-2026)
records exact landed commits and current source proposals. Migrator #55 and Admin
Shell #20 are now merged; the earlier proposal wording below is historical.
Core's Admin Shell and frontend quality-config pins remain retained for the
recorded consumer reasons. No package adoption is inferred from unchanged bytes.

Core's [#230 proposal](https://github.com/RocketsAreNostalgic/ran-booster/pull/230)
compares base `90e632cbce245b291318163b0198bc1f06371c47` with head
`e8de763e1389247f864e4854f27f5c44d894a0c1`: PHPStan 2.2.8 → 2.2.16,
WordPress stubs 6.9.4 → 7.0.1 (constrained to `~7.0.0`) and WordPress analysis
extension 2.0.3 → 2.0.4. Exactly three development-package lock records change;
production dependency records and runtime source are unchanged. Local canonical
Composer/frontend checks pass and the locked advisory result is empty. Independent
actual-PR review is clear; exact-head [Quality 37101149792](https://github.com/RocketsAreNostalgic/ran-booster/actions/runs/37101149792)
passes native archive, repository quality and all four installed lanes. The
matrix records separate local proof of the combined #229 + #230 tree.

In the historical controlled comparison on production source `90e632cbce245b291318163b0198bc1f06371c47`,
diagnostic findings at levels 1/5/8 move from
0/272/783 to 0/272/782 with no new messages. The single removed nullable-target
finding in `AssistedWebhookFacade` is improved modelling of an existing guard,
not a source defect fix. This controlled comparison supplements the external
#124 baseline without taking over that lane or raising the enforced level 1.

#124 retains separate diagnostic/fix ownership. Its captured baseline does not
raise the enforced PHPStan level or silently qualify later toolchain results.
This update introduces no dependency change, new advisory gate, source merge,
release approval or blanket closure; historical audit scope below is unchanged.

## Bounded consumer decisions — 3 October 2026

The [#122 tooling checkpoint](quality-evidence/tooling-decisions-20261003.md)
records exact before/after refs, generated-file parity, advisory scope and
qualification. It supplements the historical inventory below:

- Migrator's [#55 proposal](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/pull/55)
  adopts released coding standards `^1.0` with the owned test/helper naming
  enforcement. Keep other locked packages and Core certification references
  unchanged; qualify the target-only update and negative controls together.
- Retain Core's current Admin Shell pin: resource and sync implementation bytes
  are unchanged. Package-local development tooling does not become a consumer
  requirement. Any later adoption must regenerate real provenance and qualify
  Core; generated-byte identity alone is not latest-tooling adoption.
- Retain frontend quality-config's accepted immutable SHA: only its own
  development lock changed, and the inspected Core lock already contains the
  corresponding updated transitive versions. Registry publication remains
  optional package #5.
- Admin Shell [#20](https://github.com/RocketsAreNostalgic/ran-admin-shell/pull/20)
  separately corrects a distribution-test stat-cache observation after child
  Composer removal. It does not change Core's pin or weaken the assertion.

These were reviewed decisions/proposals at this earlier checkpoint, not blanket
dependency updates or release approval. The Core PHPStan/WordPress-stub hold
pending #124 baseline capture is superseded by the convergence update above.
Historical audit placement below is not silently requalified.

## Observed current placement

This is a bounded review of default-branch `composer.json` scripts and the
`.github/workflows/` YAML files of Booster Core, six connected PHP packages and the seven independent
repositories in the [satellite matrix](SATELLITE_QUALITY_MATRIX.md). The Starter frontend
consumer's accepted SHA distribution is recorded below; it is not claimed to
have a Composer manifest. Search terms alone are insufficient to identify an
audit: `audit` also describes source review and `--no-audit` in npm installs.

| Reviewed surface | Composer audit disposition | Evidence |
| --- | --- | --- |
| [Release Updater](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/blob/27889528442fc4e49ca060959218d5ec288c3055/composer.json) | Explicit `audit:composer = composer audit --locked --no-interaction`; `check` calls it, so a nonzero result blocks the required shared PHP baseline and terminal `quality`. | [Manifest](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/blob/27889528442fc4e49ca060959218d5ec288c3055/composer.json), [caller workflow](https://github.com/RocketsAreNostalgic/ran-wp-release-updater/blob/27889528442fc4e49ca060959218d5ec288c3055/.github/workflows/ci.yml) and [shared PHP v2 workflow](https://github.com/RocketsAreNostalgic/.github/blob/62ee68aee4ad8afefee47d25f1168ac3efcbee60/.github/workflows/quality-php-library-v2.yml). |
| [Booster Core](https://github.com/RocketsAreNostalgic/ran-booster/blob/1e7611901a2966524886b8e6c14efc4f87a71101/composer.json), [Support](https://github.com/RocketsAreNostalgic/ran-updater-support/blob/6a9cdbc9eb1bbecbafcbe16da931c98928d035e8/composer.json), [Branch](https://github.com/RocketsAreNostalgic/ran-wp-branch-updater/blob/212a0d38dd7d766c6c8d8b7f29ebcf1de075802b/composer.json), [Provider](https://github.com/RocketsAreNostalgic/ran-booster-github-provider/blob/e3d8af8de9c88858affc85a6d9c130472ae9d6f4/composer.json), [Bitbucket](https://github.com/RocketsAreNostalgic/ran-booster-bitbucket/blob/86a5e7178940420e233effcc0bc351f37fde8c57/composer.json), [Migrator](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/blob/829d823afd87923a20f8170671d2f456465424d9/composer.json) | No explicit `composer audit` command in the reviewed manifests or repository workflow files. Their other source and release gates remain as they are. | Linked default-branch manifests at the named revisions and the `.github/workflows/` directories at those revisions. |
| [Admin Shell](https://github.com/RocketsAreNostalgic/ran-admin-shell/blob/7de4946cfe6be6a3da854d576cedd45e385d2ebd/composer.json), [TnySignature](https://github.com/RocketsAreNostalgic/tnySignature/blob/1a09ee067ea41a01f2f28fbcf16f962899796133/composer.json), [Turnstile](https://github.com/RocketsAreNostalgic/ran-turnstile-for-jetpack-forms/blob/201c043c08ed1273ec1b4ae7df80f68c74befc61/composer.json), [Ecwid](https://github.com/RocketsAreNostalgic/ran-ecwid-shop-teaser/blob/e6847652309351da3a1aa1afc38175d35d0b371c/composer.json), [EmailOctopus](https://github.com/RocketsAreNostalgic/ran-emailoctopus-jetpack-forms/blob/3cc7f352d5985e854967057abc724fd06844b62d/composer.json), [Enhanced Cover](https://github.com/RocketsAreNostalgic/ran-enhanced-cover/blob/e180a1bb276c0b80678a313223c481b4b9e7510a/composer.json), [Duplicate Detector](https://github.com/RocketsAreNostalgic/ran-duplicate-detector/blob/6e741b89f31652d5eeae84b4b82d0039ffc8396a/composer.json) | No explicit `composer audit` command in the reviewed manifests or repository workflow files. Completed quality acceptance does not claim an advisory scan. | [Satellite acceptance matrix](SATELLITE_QUALITY_MATRIX.md) and linked manifests. |

This inventory establishes explicit audit placement in the reviewed scripts and
workflows; it does not assert that dependency downloads are offline or rule out
arbitrary scripts, hosting policies, separate security scans or future changes.
Recheck the affected consumer's latest files when an upgrade is proposed.

## Current shared package distribution and next upgrade

- [RAN coding standards v1.0.0](https://github.com/RocketsAreNostalgic/ran-coding-standards/releases/tag/v1.0.0) is a released shared PHP baseline. Starter and Booster have accepted consumer proof in #65. Other consumers vary: for example, Support and Branch lock v1.0.0, while Provider and several satellites currently declare `dev-main`; check the *resolved lock entry* before claiming an upgrade. Existing owner work and certified host combinations remain independent.
- [Frontend quality config](https://github.com/RocketsAreNostalgic/ran-quality-config/tree/751edd097e3902efb93992bf47401a1a4f4b1fa8) has owner-accepted immutable Git distribution at `751edd097e3902efb93992bf47401a1a4f4b1fa8`, with Starter and Booster manifests **and** pnpm locks pinned to it and passing consumer main CI. [Registry publication #5](https://github.com/RocketsAreNostalgic/ran-quality-config/issues/5) is separately planned. A registry release would require a new consumer upgrade review, not an in-place reinterpretation of the existing lock.
- The next concrete package update is initiated by a consumer owner against a specific released version or immutable revision; document the manifest/lock diff and exact candidate checks under that owner's issue. This policy checkpoint does not move Core, Bitbucket, Plugin Library or any release branch.

The [version and audit policy](QUALITY_STANDARDS.md#shared-package-versions-consumer-upgrades-and-live-advisories)
governs future upgrades. Live lookup errors remain blocking where an audit is
already required; no check or dependency was changed by this documentation.

