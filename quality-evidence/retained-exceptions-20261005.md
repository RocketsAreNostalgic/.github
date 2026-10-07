# Booster retained-exception scope — 5 October 2026

## How to read this dated evidence

This is the 5 October occurrence-level audit, not the current implementation
queue. Later candidates, delivered changes and remaining acceptance decisions
have one home in the [dated acceptance record](../PHP_QUALITY_MATRIX.md#current-candidate-checkpoint--7-october-2026).
Preserve the revisions and exposure counts below as historical measurements;
subsequent implementations do not retroactively change their scope.

Retained from [PR132's frozen source](https://github.com/RocketsAreNostalgic/.github/blob/b574d2d1a64766db94a11bfc110c456be7fab99a/quality-evidence/retained-exceptions-20261005.md),
with structural reuse coordinated in [#65](https://github.com/RocketsAreNostalgic/.github/issues/65#issuecomment-6034280845).
Retention does not approve PR132 or the separate PR134 policy proposal. Live
claims remain in existing issues; this review aid is not another handoff ledger.

Dated review aid under organisation #65 and adopted #128, not a new permanent
registry. Policy revision: `ff6ddb6731dd4151b39dc8d8c0464a253d88caf8`.
Current source was compared with actual locked checker selection and existing
behavioral evidence. Diagnostic exposure counts are sizing evidence, not counts
of proven runtime defects or automatically approved migrations.

| Repository | Exact main at audit | Standards population / analysis |
| --- | --- | --- |
| Core | `48e86ebd5d6ca153311f60bc385173349ed81e30` | Maintained source/test/tool standards; 345 maintained first-party Core PHP paths directly analyzed at required level 5; bundled dependency PHP is a separate archive population. |
| Branch Updater | `729a15c30f088236d0702b52d4a9cbe15c851508` | PHPCS selects 37 of 51 tracked PHP: 36 src plus bootstrap. Analysis level 5 includes bootstrap. |
| Release Updater | `0649dbb106fdbe8428b66a4f1efa0c52a03ddd99` | PHPCS selects 94 of 95 PHP; generated ArchiveSafety parity covers the excluded copy. All 36 shipped PHP analyzed at level 8. |
| Updater Support | `ea902004f5f11def976a6c1cae75303985ada302` | PHPCS selects all 5 PHP; both production files analyzed at level 8. |
| Admin Shell | `f760a29a8106198fbba7b1bf804de03cd38227a4` | Resource checker selects 1 PHP and 1 CSS; standalone checker selects 13 PHP. Analysis covers 7 production/tool/CLI paths at level 5; 2 previews have syntax-only treatment. |

The four dependency repositories have no open implementation issue or PR at
initial inventory refresh. Their earlier completed migration issues remain
closed. Core/Branch proposals opened after this audit have their own exact
base/head reviews and CI; they are not merged-main acceptance evidence.

## Bounded native-exception proposals

Core's eight whole-category file directives plus the SecretsFile XML exception
hide unrelated future AlternativeFunctions findings. Required native operations
have concrete private-file, inode, descriptor-lock, atomic replacement, bounded
capture or throwing-JSON reasons. Narrowing is annotation/configuration work;
no executable-token changes, API changes or guard removal are needed. Existing
StandardsCoverageTest can prove unrelated operations remain checked. Shipped
ExceptionNotEscaped directives still support the independent installed Plugin
Check gate and are not obsolete merely because shared standards 1.0.1 omit that
message in the development checker.

Branch's four native file guards hide 17 operation findings plus one silenced
missing-path observation. ArchiveValidator retains bounded ZIP reads and stream
closure; PreparedArchive retains private permissions, device/inode custody and
identity-checked deletion; FileAttemptStore retains descriptor locking,
JSON_THROW_ON_ERROR, atomic sibling replacement and readback; FileMutationLock
retains the exact flock descriptor. Exact operation annotations and four
unrelated-call probes extend its existing checker test. No developer profile
migration or dependency change is bundled.

## Unresolved acceptance at the 5 October audit

| Surface | Evidence and next bounded decision |
| --- | --- |
| Core owned public slots/names | Reserved names in Plugin.php:20, Theme.php:22, ManagedRepository.php:22, RepositoryReference.php:15 and RepositoryDescriptor.php:19, plus unused owned renderer slots in RepositoryDetailRenderer.php:17/24 and ReleaseManagementDisplay.php:819/824, need connected caller/named-argument disposition. Public visibility is not a foreign contract. No API change is included in native narrowing. |
| Core mutable comparison order | RAN/Storage/Database.php:189/194 observes expected version before get_option can invoke a mutating filter. Retain ordering; the existing version tests do not specifically inject that filter mutation. Add a focused behavioral proof when this group is taken up. |
| Branch development profile | 13 test PHP and 1 script (1,483 lines) remain outside PHPCS. Explicit locked-checker selection exposes 616 errors / 15 warnings, 340 fixable. Distinguish common conventions from genuine CLI/native fixture contracts before migration; source distribution includes these files. Future-file and blanket-suppression protections also remain separate gaps. |
| Release native operations | Removing broad AlternativeFunctions/NoSilencedErrors exclusions exposes 543 warnings across 49 files: 63 production, 32 tools, 448 tests. Start with the 7 production files and 2 tools using exact operation reasons; do not treat a config-only mapping of existing codes to paths as complete occurrence acceptance. |
| Release tests | Temporary naming exposure reports 2,058 diagnostics in 52 test files, including foreign signatures. Eight Yoda file exclusions and fixture unused/reserved allowances require grouped disposition, not one large automatic rewrite. |
| Release other exceptions | Preserve prepared-value SQL/CAS, validated table identifiers, bounded canonical opaque tokens, generated namespace-only ArchiveSafety parity and actual reflection/native seams. Global JSON/URL/error and broad test exceptions still need scope acceptance. Existing explicit analysis roots lack a dedicated future-file coverage control. |
| Release documentation | QUALITY_ACCEPTANCE.md and docs/testing.md still present completed #60/#70/protocol-5 work as pending. Correct current status while preserving historical evidence; do not repeat those migrations. |
| Support | No production suppressions. Five exact CLI exception-message annotations remain necessary with locked standards 1.0.0. Existing naming negative controls pass; a small extension for actual discovery and blanket-suppression negatives would close the remaining protection gap. No production or API change is needed. |
| Admin Shell standalone convention | Its RAN + full PHPCompatibility profile correctly avoids WordPress runtime assumptions, but locked RAN 1.0.0 only supplies syntax checking. Common formatting, owned naming and Yoda are not enforced for CLI/tools/tests. Apply existing inherited/scoped rules and representative negatives; no new shared engine or package feature is demonstrated necessary. |
| Admin Shell previews | Two ordinary preview PHP files have documented syntax-only treatment without a concrete reason common convention/compatibility would impair their purpose. Account for them or establish the actual fixture exception. Closed #13 references in README also need current-status correction. |

Release native exposure uses twelve AlternativeFunctions codes: chmod, unlink,
file_put_contents, mkdir, rename, fread, rmdir, fclose, is_writable, fwrite,
file_get_contents and fopen, plus NoSilencedErrors.Discouraged. Separate global
JSON/URL and trusted metadata-read allowances remained during that probe, so
543 is not an inventory of every exception. Preserve custody replacement
refusal, deletion fencing, SQL races and no-dev helper provenance during later
work. Hand-editing generated ArchiveSafety is not an acceptable fix.

## Admin Shell consumer identity

Core keeps the immutable development pin
`7fee7a1cebb24c8dcbf1bfd1c9b9c9455fa73efb`. Current Admin resources and SyncCommand
are byte-identical to that pin. Core synchronized PHP SHA-256 is
`a5ba855de3918a91703177d35275ddececb8e6858c2d5351ee2513275490a5be`;
CSS is `cbd3f5e6bdc6fe7360281610e5dd37367efb90e0f86b20cb4b693d8e371c35b2`.
Existing immutable checks protect source reference, hashes, installed/locked
metadata, safe paths and symlink rejection. Distribution contracts cover real
Composer installation, committed export bytes, stable sync, metadata drift and
no-dev removal preserving consumer files. No pin change or runtime/UI change
is justified by this inventory. Completed #13–20 work remains delivered;
new #128 convention acceptance is a distinct requirement. Level 6 diagnostics
remain separately scoped, not an active fix in this tranche.

## Checks and limits

Branch and Support unchanged-main full composer checks passed. Release locked
PHPCS, level-8 analysis and generated parity passed; focused boundary tests
passed 90 tests / 738 assertions. That is not fresh full Release Composer,
Windows, MySQL or installed WordPress certification. Admin bounded discovery
and resource-provenance checks passed; no new full main CI run is claimed for
its PR-only workflow. Native proposals record their own checks separately.

No dependencies, releases, settings or issue states change through this audit.
Release and manual/UI/operational holds recorded by this audit are not waived;
see the acceptance record for their subsequent dated disposition.
