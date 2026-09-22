#!/usr/bin/env node
import assert from 'node:assert/strict';
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

assert.ok(docs.includes('must support `workflow_dispatch` with no required inputs'));
assert.ok(docs.includes('"draft": true'));
assert.ok(docs.includes('"force-tag-creation": true'));
assert.ok(docs.includes('never uses `--clobber`'));
assert.ok(docs.includes('organization-wide production constraint'));
assert.ok(docs.includes('Administration-read'));
assert.ok(docs.includes('HTTP 403'));
assert.ok(docs.includes('Missing or expired Quality artifact'));

console.log('Profile B release contract OK');
