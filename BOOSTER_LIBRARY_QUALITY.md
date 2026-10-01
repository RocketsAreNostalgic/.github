# Booster library recipe — retired

Retired on 1 October 2026 after the [adoption audit](https://github.com/RocketsAreNostalgic/.github/issues/111#issuecomment-5929488158)
found no second compatible consumer. Provider owns its consolidated provisioning,
phase controls and regression tests locally. Existing shared quality workflows
and other consumers are unchanged.

The original action is preserved at immutable historical commit
`6e81370238e33c5b77641355a772557912f7fee7` (introduced by #115). Its removal must land
after Provider's reintegration PR, once main no longer references the action.
History is retained for provenance and rollback; do not adopt the retired action.

Consolidation benefited Provider; the additional cross-repository abstraction was
not justified. Require a demonstrated second matching contract before another
extraction. See #111 for measurements and limitations; wider research stays open.
