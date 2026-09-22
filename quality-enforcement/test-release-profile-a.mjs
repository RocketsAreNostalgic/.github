#!/usr/bin/env node
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';

const workflow = readFileSync('.github/workflows/release-profile-a.yml', 'utf8');
const required = [
  "inputs.upstream-event == 'push'",
  "inputs.upstream-conclusion == 'success'",
  "inputs.upstream-branch == 'main'",
  'inputs.upstream-repository == github.repository',
  'inputs.upstream-repository-id == github.repository_id',
  'inputs.upstream-workflow-path == inputs.expected-workflow-path',
  'ref: ${{ inputs.admitted-sha }}',
  'persist-credentials: false',
  'git rev-parse HEAD',
  'googleapis/release-please-action@45996ed1f6d02564a971a2fa1b5860e934307cf7',
];
for (const token of required) assert.ok(workflow.includes(token), `missing contract token: ${token}`);
for (const forbidden of [
  'skip-github-release',
  'autorelease: pending',
  'autorelease: tagged',
  'merge_commit_sha',
  'release-publisher',
  'api.github.com',
  'gh api',
]) assert.ok(!workflow.includes(forbidden), `Profile A must not contain: ${forbidden}`);
assert.match(workflow, /\[\[ "\$RAN_ADMITTED_SHA" =~ \^\[0-9a-f\]\{40\}\$ \]\]/);
console.log('Profile A release contract OK');
