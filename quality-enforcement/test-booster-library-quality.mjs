import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { spawnSync } from "node:child_process";
import test from "node:test";

const action = readFileSync(new URL("../.github/actions/booster-library-quality/action.yml", import.meta.url), "utf8");
const steps = action.split(/^    - name: /m).slice(1);
const step = (name) => {
  const found = steps.find((text) => text.startsWith(`${name}\n`));
  assert.ok(found, name);
  return found;
};
const shell = (name) => step(name).split("      run: |\n")[1].replace(/^        /gm, "").trim();

test("only fixed baseline and host phases are exposed; all actions pinned", () => {
  assert.match(action, /using: composite/);
  const inputs = action.split("inputs:\n")[1].split("runs:\n")[0];
  assert.deepEqual([...inputs.matchAll(/^  ([a-z-]+):$/gm)].map((m) => m[1]), ["php-version", "booster-sha"]);
  for (const match of action.matchAll(/^      uses: (.+)$/gm)) assert.match(match[1], /@[0-9a-f]{40}(?: #.*)?$/);
  assert.doesNotMatch(action, /continue-on-error|always\(\)|secrets\.|actions\/cache@|working-directory: \$|persist-credentials: true/);
  for (const s of steps.filter((s) => /\n      run:/.test(s))) assert.match(s, /\n      shell: bash\n/);
});

test("input validation rejects mutable, malformed and injected identities before checkout", () => {
  assert.ok(action.indexOf("Validate recipe inputs") < action.indexOf("Check out exact package revision"));
  const code = shell("Validate recipe inputs");
  const run = (php, sha) => spawnSync("bash", ["-e", "-c", code], { env: { ...process.env, RAN_PHP_VERSION: php, RAN_BOOSTER_HOST_SHA: sha } }).status;
  for (const php of ["8.2", "8.5"]) assert.equal(run(php, "a".repeat(40)), 0);
  for (const php of ["", "8.3", "latest", "8.5\necho bad"]) assert.notEqual(run(php, "a".repeat(40)), 0);
  for (const sha of ["", "main", "a".repeat(39), "g".repeat(40), "a".repeat(40) + "\necho bad"]) assert.notEqual(run("8.2", sha), 0);
});

test("source identity and manifests are checked before exactly one locked install", () => {
  const checkout = step("Check out exact package revision");
  assert.match(checkout, /persist-credentials: false/);
  assert.match(checkout, /github\.event\.pull_request\.head\.sha \|\| github\.sha/);
  assert.match(step("Reject privileged pull_request_target callers"), /pull_request_target[\s\S]*run: exit 1/);
  assert.match(step("Verify exact source revision and locked manifests"), /git rev-parse HEAD[\s\S]*test -f composer.json[\s\S]*test -f composer.lock/);
  assert.equal(action.match(/uses: shivammathur\/setup-php@/g)?.length, 1);
  assert.match(action, /extensions: zip\n        coverage: none\n        tools: composer:v2/);
  assert.match(action, /node-version: '24.11.0'/);
  assert.match(step("Verify exact Node.js version"), /node --version.*v24.11.0/);
  assert.match(step("Validate Composer configuration"), /composer validate --strict --no-check-publish --no-check-all/);
  assert.equal(action.match(/composer install --no-interaction --prefer-dist --no-progress/g)?.length, 1);
});

test("baseline precedes Core checkout; host uses the same pinned action helper", () => {
  const baseline = step("Run independent baseline before Core exists");
  const host = step("Run candidate-host quality aggregate");
  assert.ok(action.indexOf(baseline) < action.indexOf(step("Check out candidate Booster host")));
  assert.ok(action.indexOf(step("Check out candidate Booster host")) < action.indexOf(host));
  assert.doesNotMatch(baseline, /RAN_BOOSTER_CORE_PATH/);
  for (const s of [baseline, host]) {
    assert.match(s, /RAN_RECIPE_PATH: \$\{\{ github.action_path \}\}/);
    assert.match(s, /working-directory: package/);
    assert.match(s, /RAN_CI_PHASE_STATE: \$\{\{ runner.temp \}\}\/booster-library-phase-/);
  }
  assert.match(baseline, /run: bash "\$RAN_RECIPE_PATH\/ci-quality-phase.sh" baseline/);
  assert.match(host, /run: bash "\$RAN_RECIPE_PATH\/ci-quality-phase.sh" host/);
  assert.match(host, /RAN_BOOSTER_HOST_SHA: \$\{\{ inputs.booster-sha \}\}/);
  assert.match(step("Check out candidate Booster host"), /repository: RocketsAreNostalgic\/ran-booster\n        ref: \$\{\{ inputs.booster-sha \}\}\n        persist-credentials: false\n        path: booster/);
});
