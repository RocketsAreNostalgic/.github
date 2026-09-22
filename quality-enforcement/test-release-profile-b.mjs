#!/usr/bin/env node
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { readFileSync } from 'node:fs';

const workflow = readFileSync('.github/workflows/release-profile-b.yml', 'utf8');
const docs = readFileSync('RELEASE_PROFILE_B.md', 'utf8');

const required = [
  "github.event_name == 'workflow_run'",
  "github.event.workflow_run.event == 'push'",
  "github.event.workflow_run.conclusion == 'success'",
  "github.event.workflow_run.head_branch == 'main'",
  'github.event.workflow_run.head_repository.full_name == github.repository',
  'github.event.workflow_run.head_repository.id == github.repository_id',
  'github.event.workflow_run.path == inputs.expected-workflow-path',
  'github.event.workflow_run.head_sha',
  'github.event.workflow_run.id',
  'github.event.workflow_run.run_attempt',
  'persist-credentials: false',
  'git rev-parse HEAD',
  'needs: admit',
  'git/ref/heads/main',
  'target-branch: main',
  'release-pr-head:',
  'artifact-prefix:',
  'promotion-manifest:',
  'actions: write',
  'Ensure exact Release Please candidate has Quality',
  'dispatches',
  'coverage_state()',
  'for attempt in {1..300}',
  'sleep 5',
  '($exact | length) > 0',
  'head_sha=${head_sha}',
  'No successful Quality run covered exact Release Please candidate',
  'test "$(read_candidate_ref)" = "$head_sha"',
  'draft == true',
  'force-tag-creation',
  'all(($root.packages // {})[]?',
  'if has("draft") then .draft else $root.draft end',
  'if has("force-tag-creation") then .["force-tag-creation"] else $root["force-tag-creation"] end',
  'if has("skip-github-release") then .["skip-github-release"] else $root["skip-github-release"] end',
  'skip-github-release',
  'ran-profile-b-promotion',
  'actions/download-artifact@3e5f45b2cfb9172054b4087a40e8e0b5a5461e7c',
  'sha256sum',
  '.target_commitish == $sha',
  '.immutable',
  'gh release upload',
  'prerelease_before',
  'gh api --method PATCH',
  'googleapis/release-please-action@45996ed1f6d02564a971a2fa1b5860e934307cf7',
];
for (const token of required) assert.ok(workflow.includes(token), `missing contract token: ${token}`);

for (const forbidden of [
  '--clobber',
  'autorelease: pending',
  'autorelease: tagged',
  'merge_commit_sha',
  'release-publisher',
  'RAN_RELEASE_PUBLISHER_REPLAY',
  'skip-github-release: true',
  'version_tag=',
  '--prerelease',
  'RAN_IMMUTABLE_RELEASES_ENABLED',
  'immutable-releases\")',
]) assert.ok(!workflow.includes(forbidden), `Profile B must not contain: ${forbidden}`);

const admit = workflow.slice(workflow.indexOf('  admit:'), workflow.indexOf('  release:'));
assert.ok(admit.includes('contents: read'));
assert.ok(!admit.includes('contents: write'));
assert.ok(!admit.includes('pull-requests: write'));

const release = workflow.slice(workflow.indexOf('  release:'));
assert.ok(release.includes('contents: write'));
assert.ok(release.includes('pull-requests: write'));
assert.ok(release.includes('issues: write'));
assert.ok(release.includes('actions: write'));

// Execute the actual pre-publication capture, not a copy of its jq expression.
// End before the first API mutation; every fixture is local JSON only.
const captureStart = workflow.indexOf('            release_id=');
const captureEnd = workflow.indexOf('            gh api --method PATCH', captureStart);
assert.ok(captureStart >= 0 && captureEnd > captureStart, 'missing prerelease capture boundary');
const capture = workflow.slice(captureStart, captureEnd);
assert.ok(capture.includes('prerelease_before='));
assert.ok(!capture.includes('gh '), 'boolean fixture must not invoke GitHub');

const booleanCases = [
  ['prerelease', { id: 1, prerelease: true }, 'true'],
  ['stable', { id: 1, prerelease: false }, 'false'],
  ['missing', { id: 1 }, null],
  ['null', { id: 1, prerelease: null }, null],
  ['string false', { id: 1, prerelease: 'false' }, null],
  ['string true', { id: 1, prerelease: 'true' }, null],
  ['zero', { id: 1, prerelease: 0 }, null],
  ['one', { id: 1, prerelease: 1 }, null],
  ['array', { id: 1, prerelease: [] }, null],
  ['object', { id: 1, prerelease: {} }, null],
];
for (const [name, releaseJson, expected] of booleanCases) {
  const result = spawnSync('bash', ['-c',
    'set -euo pipefail\nrelease_json="$RAN_TEST_RELEASE_JSON"\n'
      + capture + '\nprintf "%s\\n" "$prerelease_before"\n',
  ], {
    encoding: 'utf8',
    env: { ...process.env, RAN_TEST_RELEASE_JSON: JSON.stringify(releaseJson) },
    timeout: 10000,
  });
  assert.ifError(result.error);
  assert.notEqual(result.status, null, `${name}: shell did not exit normally`);
  if (expected === null) {
    assert.notEqual(result.status, 0, `${name}: invalid prerelease metadata must fail closed`);
  } else {
    assert.equal(result.status, 0, `${name}: ${result.stderr}`);
    assert.equal(result.stdout.trim(), expected, `${name}: preserve Release Please's boolean`);
  }
}

// Exercise the actual first promotion lookup. A draft is readable by ID while
// the tag endpoint returns 404, matching the observed production failure.
const promotion = workflow.slice(workflow.indexOf('      - name: Verify and promote exact tested assets'));
const lookupStart = promotion.indexOf('          release_json=');
const lookupEnd = promotion.indexOf('          remote_names=', lookupStart);
assert.ok(lookupStart >= 0 && lookupEnd > lookupStart);
const lookup = promotion.slice(lookupStart, lookupEnd);
assert.ok(!promotion.includes('/releases/tags/'), 'promotion must keep the resolved release ID');
assert.ok(workflow.includes('release-id=%s'));
assert.ok(workflow.includes('RAN_RELEASE_ID: ${{ steps.publication.outputs.release-id }}'));
const exactRelease = { id: 394078148, tag_name: 'v1.3.3', target_commitish: 'a'.repeat(40), draft: true };
for (const [name, fixture, expectedStatus] of [
  ['draft by ID', exactRelease, 0],
  ['published by ID', { ...exactRelease, draft: false, immutable: true }, 0],
  ['wrong ID', { ...exactRelease, id: 2 }, 1],
  ['wrong tag', { ...exactRelease, tag_name: 'v1.3.4' }, 1],
  ['wrong target', { ...exactRelease, target_commitish: 'b'.repeat(40) }, 1],
]) {
  const result = spawnSync('bash', ['-c', `set -euo pipefail
gh() {
  if [[ "$*" == "api repos/example/repo/releases/394078148" ]]; then
    printf '%s\\n' "$RAN_TEST_RELEASE_JSON"
  else
    echo 'Not Found (HTTP 404)' >&2
    return 1
  fi
}
${lookup}`], {
    encoding: 'utf8',
    env: { ...process.env, GITHUB_REPOSITORY: 'example/repo',
      RAN_RELEASE_ID: '394078148', RAN_RELEASE_TAG: 'v1.3.3',
      RAN_ADMITTED_SHA: 'a'.repeat(40), RAN_TEST_RELEASE_JSON: JSON.stringify(fixture) },
    timeout: 10000,
  });
  assert.ifError(result.error);
  assert.equal(result.status, expectedStatus, `${name}: ${result.stderr}`);
}

assert.ok(docs.includes('must support `workflow_dispatch` with no required inputs'));
assert.ok(docs.includes('waits for a successful Quality run whose reported `head_sha` is that exact SHA'));
assert.ok(docs.includes('"draft": true'));
assert.ok(docs.includes('"force-tag-creation": true'));
assert.ok(docs.includes('never uses `--clobber`'));
assert.ok(docs.includes('organization-wide production constraint'));
assert.ok(docs.includes('Administration-read'));
assert.ok(docs.includes('HTTP 403'));
assert.ok(docs.includes('Missing or expired Quality artifact'));

console.log('Profile B release contract OK');
