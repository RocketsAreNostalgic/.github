# Independent tooling decisions for organisation #122 — 3 October 2026

This checkpoint covers only Migrator coding-standards adoption, Core Admin Shell pin review, and frontend quality-config drift. Core PHPStan/WordPress declarations remain held for the separately owned #124 baseline. No release, merge, workflow approval or blanket issue closure is implied.

| Component | Before | Reviewed candidate/current main | Decision |
| --- | --- | --- | --- |
| Migrator `ran/coding-standards` | `dev-main`, `0b03e61a4bb558deeb6bc6b6399f44c0ec95e5be` | `v1.0.0`, `6af816a02b7d1108ad5c990e9d0fda0af0a13de7` | Adopt released `^1.0` in the combined #121 naming candidate, proposed in [Migrator PR55](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/pull/55); final head `2cd1bc9f470ef981abdf8020ccef9f41cf1a83f5` has clear independent review; native qualification is tracked there. |
| Core `ran/admin-shell` | `dev-main`, `7fee7a1cebb24c8dcbf1bfd1c9b9c9455fa73efb` | package main `e7f3a479de0678e5f96cf37d13295cd3c1f6d5a7` | Explicitly retain current immutable consumer pin for this tranche. |
| Core frontend quality-config | `751edd097e3902efb93992bf47401a1a4f4b1fa8` | `4e7e8925416385e1c947d3b6508acc38e2f78043` | Retain accepted Git SHA; exported configuration has no drift. |

Consumer baseline inspected: Core `0b724f5cb4b43c89a37fb0008df672488983550b`, Migrator `024d8d5cbf35c46b196df06e053d08dbc542513b`.

## Migrator: qualify the released standards, jointly with #121

The released package adds the opt-in `RANOwnedMethods` rule, which checks owned inherited/implementing methods that WPCS skips. It also promotes assignment/array alignment diagnostics to errors. Existing default profiles do not implicitly enable the method rule; #121 explicitly owns migration and activation. Package API/dependency changes are confined to development tooling.

The only added package requirement is `phpcsstandards/phpcsutils:^1.2.2`; Migrator already locks compatible `1.2.3` at `5f35d9408c54d7b529501f3c688b6eae562aea1f`. PHP `>=7.4`, PHPCS `^3.13.6`, WPCS `^3.4.1`, and installer `^1.1` remain unchanged. Migrator's PHP floor is 8.2. The standards package remains MIT-licensed; Migrator's GPL-2.0-or-later licence is unchanged. The target update must retain every other locked package and the supported Core source/certification references. Migrator PR55 final candidate `2cd1bc9f470ef981abdf8020ccef9f41cf1a83f5` changes only the standards lock entry. Full local Composer checks pass 130 tests /1,633 assertions and pinned frontend checks pass. Independent review verified coherent names/callers and preserved production source, Core pins and historical installed expectations; its initial blanket-directive guard finding was fixed with six actual negative controls. The subsequent six test-name word-boundary corrections passed exact-head Composer checks (130 tests /1,633 assertions) and [affected final review](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/pull/55#issuecomment-5963335692). Native [Quality37079834362](https://github.com/RocketsAreNostalgic/ran-booster-wp-pusher-migrator/actions/runs/37079834362) belongs to this latest head; its result is recorded on the PR. The predecessor's successful run is historical, not substituted for this head. Final candidate locked advisory retrieval returned no advisories or abandoned packages.

Upgrade guidance: change `ran/coding-standards` to `^1.0`, perform a target-only Composer update with minimal changes, explicitly activate the owned-method rule for audited owned paths, retain narrow external PHPUnit signatures, and qualify the resulting canonical check including its negative enforcement controls. No higher PHPStan level or released-host certification follows from this adoption.

## Admin Shell: retention and a separate test-harness repair

The compared package range changes tooling, package tests, README, composer development dependencies, workflow configuration, and export exclusions. `resources/admin-shell.php`, `resources/admin-shell.css`, and `tools/SyncCommand.php` are byte-identical. The CLI entrypoint adds a bounded missing-`$argv` diagnostic; no observed Core sync failure requires that guard. Package development requirements and scripts do not install or run transitively as consumer development checks. No runtime autoload is introduced.

Core's generated files match both package references:

- PHP SHA-256: `a5ba855de3918a91703177d35275ddececb8e6858c2d5351ee2513275490a5be`.
- CSS SHA-256: `cbd3f5e6bdc6fe7360281610e5dd37367efb90e0f86b20cb4b693d8e371c35b2`.
- Unchanged sync tool SHA-256: `3ce5f87248d700fa86b23dac90cdaa127ca860daee0b041e27c3eadf964a4aae`.

Retaining the existing lock and provenance is justified: package-main quality work is already delivered in its own repository, while consumer adoption would change lock/provenance without changing generated rendering. A later deliberate adoption must target only Admin Shell, regenerate provenance through its real sync command, preserve these PHP/CSS bytes where still applicable, and pass immutable Admin Shell plus complete Core qualification. Do not claim latest build-tool adoption from generated-byte identity alone.

Independent execution uncovered an existing package distribution-test defect: after a child Composer process removes the dev-only package, PHP retains the test process's earlier directory stat result. Unmodified main reproducibly fails the final absence assertion; invalidating the stat cache makes the full existing distribution contract pass. This is not a failure to remove the installed package.

[Admin Shell PR20](https://github.com/RocketsAreNostalgic/ran-admin-shell/pull/20) adds only an explanation and targeted `clearstatcache(true, path)` before the unchanged assertion. Base `e7f3a479de0678e5f96cf37d13295cd3c1f6d5a7`; head `9718954a85b6c5a28ea6d0ad019427f707cead28`; tree `07a0c5f69114c1ba04e5e9d94a540e3a15f37ac1`. Canonical candidate `composer check` passes on PHP 8.3.6 / Composer 2.9.0: coverage, syntax, PHPCS, PHPStan, and PHPUnit 26 tests / 173 assertions. Final-head native [Quality run 37078549073](https://github.com/RocketsAreNostalgic/ran-admin-shell/actions/runs/37078549073) is SUCCESS. [Independent actual-PR review](https://github.com/RocketsAreNostalgic/ran-admin-shell/pull/20#issuecomment-5963191076) is clear. Core's pin remains unchanged by this repair.

## Frontend quality-config: development-lock-only drift

`git diff --name-only 751edd097e3902efb93992bf47401a1a4f4b1fa8..4e7e8925416385e1c947d3b6508acc38e2f78043` returns only `pnpm-lock.yaml` (12 additions/12 deletions). Manifest, export maps, peer requirements, ESLint/Prettier/Stylelint source, README and licence are unchanged. The changed package-local lock updates brace-expansion 1.1.18→1.1.21 and 5.0.9→5.0.12, and fast-uri 3.1.7→3.1.8. Core already locks 1.1.21, 5.0.12 and 3.1.8 respectively. The dependency's development lock does not govern Core's resolved graph.

No consumer update, registry publication or repeated security-maintenance programme is needed to resolve this discrepancy. Optional registry distribution remains [quality-config #5](https://github.com/RocketsAreNostalgic/ran-quality-config/issues/5), whose live scope explicitly accepts the immutable Git-SHA consumers. #118 stays completed; #111 remains retired.

## Advisory and qualification scope

Fresh `composer audit --locked --format=json` snapshots for the unchanged Core, Migrator baseline, and Admin Shell package-main PHP development graphs returned empty `advisories` and `abandoned` arrays. This is a scoped registry check, not proof of general security or newly qualified release compatibility. The Migrator candidate advisory result must accompany its final lockfile. No fresh npm-wide security claim is made here; quality-config retention is based on exact source/export identity and inspected consumer lock entries.

No product source or Core composer files were modified by this audit. Existing release holds, interactive acceptance deferrals and #124 ownership remain unchanged.
