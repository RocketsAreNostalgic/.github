#!/usr/bin/env node
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { readFileSync, writeFileSync, mkdtempSync, mkdirSync, rmSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

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
  '.conclusion != "action_required"',
  '($usable | length) > 0',
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
  'https://uploads.github.com/repos/${GITHUB_REPOSITORY}/releases/${RAN_RELEASE_ID}/assets?name=${name}',
  'prerelease_before',
  'gh api --method PATCH',
  'googleapis/release-please-action@45996ed1f6d02564a971a2fa1b5860e934307cf7',
];
for (const token of required) assert.ok(workflow.includes(token), `missing contract token: ${token}`);

for (const forbidden of [
  '--clobber',
  'gh release upload',
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

// Execute the actual candidate-coverage classifier. A GitHub-created Release
// Please PR may have a pull_request run recorded as action_required with zero
// jobs; that is non-execution and must fall through to exact-head dispatch.
const coverageStart = workflow.indexOf('          coverage_state() {');
const coverageEnd = workflow.indexOf('\n\n          state="$(coverage_state)"', coverageStart);
assert.ok(coverageStart >= 0 && coverageEnd > coverageStart, 'missing candidate coverage classifier');
const coverageFunction = workflow.slice(coverageStart, coverageEnd)
  .split('\n').map(line => line.replace(/^          /, '')).join('\n');

const qualityWorkflowId = 42;
const candidateHead = 'c'.repeat(40);
const candidateBranch = 'release-please--branches--main--components--example';
const candidateRepository = 'example/repo';
const exactRun = (event, status, conclusion) => ({
  workflow_id: qualityWorkflowId,
  path: '.github/workflows/quality.yml',
  event,
  status,
  conclusion,
  head_branch: candidateBranch,
  head_repository: { full_name: candidateRepository },
  head_sha: candidateHead,
});
const gatedPullRequest = exactRun('pull_request', 'completed', 'action_required');
const coverageCases = [
  ['gated pull request only', [gatedPullRequest], 'absent'],
  ['gated pull request plus active dispatch',
    [gatedPullRequest, exactRun('workflow_dispatch', 'in_progress', null)], 'active'],
  ['gated pull request plus failed dispatch',
    [gatedPullRequest, exactRun('workflow_dispatch', 'completed', 'failure')], 'failed'],
  ['gated pull request plus successful dispatch',
    [gatedPullRequest, exactRun('workflow_dispatch', 'completed', 'success')], 'success'],
  ['executed pull request failure', [exactRun('pull_request', 'completed', 'failure')], 'failed'],
  ['executed pull request success', [exactRun('pull_request', 'completed', 'success')], 'success'],
];
for (const [name, runs, expected] of coverageCases) {
  const result = spawnSync('bash', ['-c',
    'set -euo pipefail\n'
      + 'workflow_id=42\n'
      + 'head_sha="$RAN_TEST_HEAD_SHA"\n'
      + 'RAN_RELEASE_PR_HEAD="$RAN_TEST_HEAD_BRANCH"\n'
      + 'GITHUB_REPOSITORY="$RAN_TEST_REPOSITORY"\n'
      + 'export RAN_QUALITY_WORKFLOW_PATH=.github/workflows/quality.yml\n'
      + 'gh() { printf "%s\\n" "$RAN_TEST_RUNS"; }\n'
      + coverageFunction
      + '\ncoverage_state\n',
  ], {
    encoding: 'utf8',
    env: {
      ...process.env,
      RAN_TEST_HEAD_SHA: candidateHead,
      RAN_TEST_HEAD_BRANCH: candidateBranch,
      RAN_TEST_REPOSITORY: candidateRepository,
      RAN_TEST_RUNS: JSON.stringify({ workflow_runs: runs }),
    },
    timeout: 10000,
  });
  assert.ifError(result.error);
  assert.equal(result.status, 0, name + ': ' + result.stderr);
  assert.equal(result.stdout.trim(), expected, name);
}

// Execute the actual classification capture at publication resolution.
// Every fixture is local JSON only; preserve legitimate false and reject non-booleans.
const captureStart = workflow.indexOf("          # Capture Release Please's classification");
const captureEnd = workflow.indexOf('          release_id=', captureStart);
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
assert.ok(workflow.includes('prerelease=%s'));
assert.ok(workflow.includes('RAN_RELEASE_PRERELEASE: ${{ steps.publication.outputs.prerelease }}'));
assert.ok(workflow.includes('RAN_RELEASE_ID: ${{ steps.publication.outputs.release-id }}'));
const exactRelease = { id: 394078148, tag_name: 'v1.3.3', target_commitish: 'a'.repeat(40), draft: true, prerelease: false };
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
      RAN_RELEASE_ID: '394078148', RAN_RELEASE_TAG: 'v1.3.3', RAN_RELEASE_PRERELEASE: 'false',
      RAN_ADMITTED_SHA: 'a'.repeat(40), RAN_TEST_RELEASE_JSON: JSON.stringify(fixture) },
    timeout: 10000,
  });
  assert.ifError(result.error);
  assert.equal(result.status, expectedStatus, `${name}: ${result.stderr}`);
}

// Run the entire promotion step against a local API simulator, including raw
// uploads, publication and immutable readback. Unexpected/tag-based calls fail.
const promotionScript = promotion.slice(promotion.indexOf('        run: |') + '        run: |'.length)
  .split('\n').map(line => line.replace(/^          /, '')).join('\n');
for (const scenario of ['stable', 'prerelease', 'published', 'deleted-before-upload',
  'drift-id', 'drift-tag', 'drift-target', 'drift-draft', 'drift-draft-null',
  'drift-stable-to-prerelease', 'drift-prerelease-to-stable',
  'early-stable-to-prerelease', 'early-prerelease-to-stable']) {
  const dir = mkdtempSync(join(tmpdir(), 'profile-b-promotion-'));
  try {
    mkdirSync(join(dir, 'promotion'));
    const assets = [ ['example.zip', Buffer.from([0, 1, 2, 255, 10])], ['example.zip.sha256', Buffer.from('checksum fixture\n')] ]
      .map(([name, bytes]) => {
        writeFileSync(join(dir, 'promotion', name), bytes);
        return { name, sha256: createHash('sha256').update(bytes).digest('hex') };
      });
    writeFileSync(join(dir, 'promotion', 'ran-profile-b-promotion.json'), JSON.stringify({
      schema: 'ran-profile-b-promotion', schema_version: 1, repository: 'example/repo',
      quality_commit: 'a'.repeat(40), source_commit: 'a'.repeat(40), tag: 'v1.3.3', assets,
    }));
    const published = scenario === 'published';
    const originalPrerelease = scenario === 'prerelease' || scenario.endsWith('prerelease-to-stable');
    writeFileSync(join(dir, 'state.json'), JSON.stringify({ ...exactRelease,
      draft: !published, immutable: published, prerelease: originalPrerelease,
      assets: published ? assets.map(a => ({ name: a.name, digest: 'sha256:' + a.sha256 })) : [],
    }));
    writeFileSync(join(dir, 'calls.json'), '[]');
    writeFileSync(join(dir, 'gh'), `#!/usr/bin/env node
const fs = require('node:fs');
const crypto = require('node:crypto');
const assert = require('node:assert/strict');
const args = process.argv.slice(2);
assert.equal(args.shift(), 'api');
let method = 'GET', input, endpoint, header, field;
while (args.length) {
  const arg = args.shift();
  if (arg === '--method') method = args.shift();
  else if (arg === '--input') input = args.shift();
  else if (arg === '-H') header = args.shift();
  else if (arg === '-F') field = args.shift();
  else { assert.equal(endpoint, undefined); endpoint = arg; }
}
const calls = JSON.parse(fs.readFileSync('calls.json'));
calls.push({ method, endpoint }); fs.writeFileSync('calls.json', JSON.stringify(calls));
const state = JSON.parse(fs.readFileSync('state.json'));
const api = 'repos/example/repo/releases/394078148';
if (method === 'GET') {
  assert.equal(endpoint, api);
  if (calls.filter(c => c.method === 'GET').length === 1 && process.env.RAN_TEST_SCENARIO.startsWith('early-')) {
    state.prerelease = !state.prerelease;
  }
  // Simulate an external edit after upload, on the response used to publish.
  if (calls.filter(c => c.method === 'GET').length === 2) {
    switch (process.env.RAN_TEST_SCENARIO) {
      case 'drift-stable-to-prerelease': state.prerelease = true; break;
      case 'drift-prerelease-to-stable': state.prerelease = false; break;
      case 'drift-id': state.id = 2; break;
      case 'drift-tag': state.tag_name = 'v9.9.9'; break;
      case 'drift-target': state.target_commitish = 'b'.repeat(40); break;
      case 'drift-draft': state.draft = false; state.immutable = true; break;
      case 'drift-draft-null': state.draft = null; break;
    }
  }
} else if (method === 'POST') {
  const url = new URL(endpoint);
  assert.equal(url.origin + url.pathname, 'https://uploads.github.com/' + api + '/assets');
  if (process.env.RAN_TEST_SCENARIO === 'deleted-before-upload') process.exit(1);
  assert.equal(state.draft, true);
  assert.equal(header, 'Content-Type: application/octet-stream');
  const name = url.searchParams.get('name');
  assert.equal(input, 'promotion/' + name);
  assert.ok(!state.assets.some(a => a.name === name));
  state.assets.push({ name, digest: 'sha256:' + crypto.createHash('sha256').update(fs.readFileSync(input)).digest('hex') });
} else if (method === 'PATCH') {
  assert.equal(endpoint, api); assert.equal(field, 'draft=false');
  assert.equal(state.assets.length, 2);
  state.draft = false; state.immutable = true;
} else throw Error('unexpected API mutation');
fs.writeFileSync('state.json', JSON.stringify(state));
console.log(JSON.stringify(state));
`, { mode: 0o755 });
    const result = spawnSync('bash', ['-c', promotionScript], {
      cwd: dir, encoding: 'utf8', timeout: 20000,
      env: { ...process.env, PATH: dir + ':' + process.env.PATH,
        GITHUB_REPOSITORY: 'example/repo', RAN_RELEASE_ID: '394078148',
        RAN_RELEASE_TAG: 'v1.3.3', RAN_ADMITTED_SHA: 'a'.repeat(40),
        RAN_RELEASE_PRERELEASE: String(originalPrerelease),
        RAN_PROMOTION_MANIFEST: 'ran-profile-b-promotion.json',
        RAN_PUBLICATION_STATE: published ? 'published' : 'draft', RAN_TEST_SCENARIO: scenario },
    });
    assert.ifError(result.error);
    const calls = JSON.parse(readFileSync(join(dir, 'calls.json')));
    const mutations = calls.filter(c => c.method !== 'GET');
    const state = JSON.parse(readFileSync(join(dir, 'state.json')));
    if (scenario === 'deleted-before-upload') {
      assert.notEqual(result.status, 0);
      assert.equal(state.assets.length, 0);
      assert.equal(state.draft, true);
      assert.deepEqual(mutations.map(c => c.method), ['POST']);
    } else if (scenario.startsWith('early-')) {
      assert.notEqual(result.status, 0);
      assert.deepEqual(mutations, [], 'classification drift before upload must prevent all mutations');
    } else if (scenario.startsWith('drift-')) {
      assert.notEqual(result.status, 0, scenario + ': changed release must fail closed');
      assert.equal(state.assets.length, 2);
      assert.deepEqual(mutations.map(c => c.method), ['POST', 'POST'],
        scenario + ': no publication PATCH after changed identity/state');
    } else {
      assert.equal(result.status, 0, scenario + ': ' + result.stderr);
      assert.deepEqual(mutations.map(c => c.method), published ? [] : ['POST', 'POST', 'PATCH']);
      assert.equal(state.immutable, true);
      assert.equal(state.prerelease, originalPrerelease);
    }
  } finally { rmSync(dir, { recursive: true, force: true }); }
}

assert.ok(docs.includes('must support `workflow_dispatch` with no required inputs'));
assert.ok(docs.includes('waits for a successful Quality run whose reported `head_sha` is that exact SHA'));
assert.ok(docs.includes('conclusion: action_required'));
assert.ok(docs.includes('"draft": true'));
assert.ok(docs.includes('"force-tag-creation": true'));
assert.ok(docs.includes('never uses `--clobber`'));
assert.ok(docs.includes('organization-wide production constraint'));
assert.ok(docs.includes('Administration-read'));
assert.ok(docs.includes('HTTP 403'));
assert.ok(docs.includes('Missing or expired Quality artifact'));

console.log('Profile B release contract OK');
