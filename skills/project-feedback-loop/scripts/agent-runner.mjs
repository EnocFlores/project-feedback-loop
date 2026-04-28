// skills/project-feedback-loop/scripts/agent-runner.mjs
import { mkdirSync, appendFileSync, writeFileSync } from "node:fs";
import { dirname } from "node:path";
import { spawnSync } from "node:child_process";

const HISTORY = process.env.PROJECT_FEEDBACK_LOOP_HISTORY ?? "state/history.jsonl";
const FAILURE_FILE =
  process.env.PROJECT_FEEDBACK_LOOP_FAILURE_FILE ?? ".project-feedback-loop/last-failure.txt";
const GENERATE_CMD = process.env.PROJECT_FEEDBACK_LOOP_GENERATE_CMD;
const VERIFY_CMD = process.env.PROJECT_FEEDBACK_LOOP_VERIFY;
const FIX_CMD = process.env.PROJECT_FEEDBACK_LOOP_FIX_CMD;
const MAX_RETRIES = Number.parseInt(process.env.PROJECT_FEEDBACK_LOOP_MAX_RETRIES ?? "6", 10);

if (!VERIFY_CMD) {
  console.error("PROJECT_FEEDBACK_LOOP_VERIFY is required");
  process.exit(1);
}

function now() {
  return new Date().toISOString();
}

function run(cmd) {
  const result = spawnSync(cmd, { shell: true, encoding: "utf8" });
  return {
    code: result.status ?? 1,
    stdout: result.stdout ?? "",
    stderr: result.stderr ?? "",
    combined: `${result.stdout ?? ""}\n${result.stderr ?? ""}`.trim(),
  };
}

function categorize(text) {
  const lowered = text.toLowerCase();
  if (/(prettier|format|unformatted)/.test(lowered)) return "format";
  if (/(eslint|lint|sonarjs|oxlint)/.test(lowered)) return "lint";
  if (/(tsc|typecheck|typing)/.test(lowered)) return "type";
  if (/(vitest|jest|assert|test failed|failing test)/.test(lowered)) return "unit";
  if (/(playwright|integration|e2e)/.test(lowered)) return "integration";
  if (/(module not found|cannot find|environment|command not found)/.test(lowered)) return "env";
  return "unknown";
}

function appendHistory(entry) {
  mkdirSync(dirname(HISTORY), { recursive: true });
  appendFileSync(HISTORY, `${JSON.stringify(entry)}\n`, "utf8");
}

mkdirSync(dirname(FAILURE_FILE), { recursive: true });

if (GENERATE_CMD) {
  const generated = run(GENERATE_CMD);
  if (generated.code !== 0) {
    console.error(generated.combined);
    process.exit(generated.code);
  }
}

for (let attempt = 1; attempt <= MAX_RETRIES + 1; attempt += 1) {
  const verification = run(VERIFY_CMD);
  if (verification.code === 0) {
    appendHistory({ ts: now(), attempt, status: "pass", verify: VERIFY_CMD });
    console.log("Verification passed.");
    process.exit(0);
  }

  const category = categorize(verification.combined);
  writeFileSync(FAILURE_FILE, verification.combined, "utf8");
  appendHistory({
    ts: now(),
    attempt,
    status: "fail",
    category,
    verify: VERIFY_CMD,
    failure_file: FAILURE_FILE,
  });

  if (attempt > MAX_RETRIES || !FIX_CMD) {
    console.error(verification.combined);
    console.error(`Stopped after attempt ${attempt}. Category: ${category}`);
    process.exit(verification.code);
  }

  const fix = spawnSync(FIX_CMD, {
    shell: true,
    stdio: "inherit",
    env: {
      ...process.env,
      PFL_ATTEMPT: String(attempt),
      PFL_CATEGORY: category,
      PFL_FAILURE_FILE: FAILURE_FILE,
      PFL_VERIFY_CMD: VERIFY_CMD,
    },
  });

  if ((fix.status ?? 1) !== 0) {
    console.error(`Fix command failed on attempt ${attempt}`);
    process.exit(fix.status ?? 1);
  }
}

