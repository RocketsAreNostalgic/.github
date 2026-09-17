import { appendFileSync, readFileSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { resolve } from 'node:path';

function fail(message) {
  console.error(`::error::${message}`);
  process.exit(1);
}

function parseArgs(argv) {
  const args = {
    registry: 'quality-enforcement/contracts.json',
    repository: process.env.GITHUB_REPOSITORY || '',
    worktree: '.',
    expectedProfile: '',
  };

  for (let index = 0; index < argv.length; index += 1) {
    const flag = argv[index];
    const value = argv[index + 1];
    if (!value) fail(`Missing value for ${flag}`);

    switch (flag) {
      case '--registry':
        args.registry = value;
        break;
      case '--repository':
        args.repository = value;
        break;
      case '--worktree':
        args.worktree = value;
        break;
      case '--expected-profile':
        args.expectedProfile = value;
        break;
      default:
        fail(`Unknown argument: ${flag}`);
    }
    index += 1;
  }

  return args;
}

function git(worktree, ...args) {
  try {
    return execFileSync('git', ['-C', worktree, ...args], {
      encoding: 'utf8',
      stdio: ['ignore', 'pipe', 'pipe'],
    }).trim();
  } catch (error) {
    const detail = error?.stderr?.toString().trim();
    fail(`Git command failed (${args.join(' ')}): ${detail || error.message}`);
  }
}

function pathExists(worktree, path) {
  return git(worktree, 'ls-tree', '-z', 'HEAD', '--', path).length > 0;
}

function output(name, value) {
  const outputFile = process.env.GITHUB_OUTPUT;
  if (!outputFile) return;
  if (typeof value !== 'string' || /[\r\n]/.test(value)) {
    fail(`Unsafe workflow output value for ${name}`);
  }
  appendFileSync(outputFile, `${name}=${value}\n`);
}

function requireVersion(value, label, { patch = false, allowEmpty = false } = {}) {
  if (allowEmpty && value === '') return;
  const pattern = patch ? /^[0-9]+\.[0-9]+\.[0-9]+$/ : /^[0-9]+\.[0-9]+$/;
  if (!pattern.test(value || '')) fail(`${label} must be an exact ${patch ? 'major.minor.patch' : 'major.minor'} version`);
}

function requireSafeRelativePath(value, label) {
  if (
    typeof value !== 'string' ||
    !value ||
    value.startsWith('/') ||
    value.includes('..') ||
    /[\r\n:]/.test(value)
  ) {
    fail(`${label} must be a safe repository-relative path`);
  }
}

const args = parseArgs(process.argv.slice(2));
if (!/^[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+$/.test(args.repository)) {
  fail(`Invalid repository identity: ${args.repository || '<empty>'}`);
}

const registryPath = resolve(args.registry);
const worktree = resolve(args.worktree);
let registry;
try {
  registry = JSON.parse(readFileSync(registryPath, 'utf8'));
} catch (error) {
  fail(`Cannot read contract registry ${registryPath}: ${error.message}`);
}

if (registry?.schema !== 1 || typeof registry.repositories !== 'object') {
  fail('Unsupported or malformed quality-contract registry');
}

const contract = registry.repositories[args.repository];
if (!contract) fail(`No approved quality contract for ${args.repository}`);
if (!['node', 'php-library', 'wordpress-plugin'].includes(contract.profile)) {
  fail(`Unsupported profile for ${args.repository}: ${contract.profile}`);
}
if (args.expectedProfile && contract.profile !== args.expectedProfile) {
  fail(`Expected profile ${args.expectedProfile}, found ${contract.profile}`);
}
if (!Array.isArray(contract.objects) || contract.objects.length === 0) {
  fail(`No protected objects configured for ${args.repository}`);
}
if (contract.absent !== undefined && !Array.isArray(contract.absent)) {
  fail(`Absent-path contract must be an array for ${args.repository}`);
}
if (!/^[0-9a-f]{40}$/.test(contract.approved_commit || '')) {
  fail(`Invalid approved commit for ${args.repository}`);
}

const seen = new Set();
for (const object of contract.objects) {
  requireSafeRelativePath(object?.path, `protected path in ${args.repository}`);
  if (seen.has(object.path)) fail(`Duplicate protected path: ${object.path}`);
  seen.add(object.path);

  if (!['blob', 'tree'].includes(object.type)) {
    fail(`Unsupported object type for ${object.path}: ${object.type}`);
  }
  if (!/^[0-9a-f]{40}$/.test(object.oid || '')) {
    fail(`Invalid approved object id for ${object.path}`);
  }

  const actualOid = git(worktree, 'rev-parse', `HEAD:${object.path}`);
  const actualType = git(worktree, 'cat-file', '-t', actualOid);
  if (actualType !== object.type) {
    fail(`${object.path} changed object type: expected ${object.type}, found ${actualType}`);
  }
  if (actualOid !== object.oid) {
    fail(
      `${object.path} is outside the centrally approved quality contract: expected ${object.oid}, found ${actualOid}`,
    );
  }
  console.log(`approved ${object.type} ${object.oid} ${object.path}`);
}

for (const path of contract.absent || []) {
  requireSafeRelativePath(path, `absent path in ${args.repository}`);
  if (seen.has(path)) fail(`Duplicate protected/absent path: ${path}`);
  seen.add(path);
  if (pathExists(worktree, path)) {
    fail(`${path} is an unapproved shadow/configuration path and must remain absent`);
  }
  console.log(`approved absent ${path}`);
}

const inputs = contract.inputs || {};
const workingDirectory = inputs['working-directory'] || '.';
requireSafeRelativePath(workingDirectory, 'working-directory');

if (contract.profile === 'node') {
  requireVersion(inputs['pnpm-version'], 'pnpm-version', { patch: true });
  requireSafeRelativePath(inputs['node-version-file'], 'node-version-file');
}

if (contract.profile === 'wordpress-plugin') {
  requireVersion(inputs['php-version'], 'php-version');
  requireVersion(inputs['pnpm-version'], 'pnpm-version', { patch: true });
  requireSafeRelativePath(inputs['node-version-file'], 'node-version-file');
}

if (contract.profile === 'php-library') {
  requireVersion(inputs['php-floor'], 'php-floor');
  requireVersion(inputs['php-current'], 'php-current');
  requireVersion(inputs['node-version'] || '', 'node-version', {
    patch: true,
    allowEmpty: true,
  });
  if (
    typeof inputs['php-extensions'] !== 'string' ||
    !/^[A-Za-z0-9_-]+(?:,[A-Za-z0-9_-]+)*$/.test(inputs['php-extensions'])
  ) {
    fail('php-extensions must be a non-empty comma-separated identifier list');
  }
}

output('profile', contract.profile);
output('approved_commit', contract.approved_commit);
output('node_version_file', inputs['node-version-file'] || '');
output('pnpm_version', inputs['pnpm-version'] || '');
output('php_version', inputs['php-version'] || '');
output('php_floor', inputs['php-floor'] || '');
output('php_current', inputs['php-current'] || '');
output('php_extensions', inputs['php-extensions'] || '');
output('node_version', inputs['node-version'] || '');
output('working_directory', workingDirectory);

console.log(
  `Quality contract accepted for ${args.repository} (${contract.profile}, ${contract.objects.length} protected objects, ${(contract.absent || []).length} required-absent paths).`,
);
