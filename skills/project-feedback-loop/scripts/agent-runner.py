# skills/project-feedback-loop/scripts/agent-runner.py
#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import shlex
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

HISTORY = Path(os.getenv("PROJECT_FEEDBACK_LOOP_HISTORY", "state/history.jsonl"))
FAILURE_FILE = Path(os.getenv("PROJECT_FEEDBACK_LOOP_FAILURE_FILE", ".project-feedback-loop/last-failure.txt"))
GENERATE_CMD = os.getenv("PROJECT_FEEDBACK_LOOP_GENERATE_CMD")
VERIFY_CMD = os.getenv("PROJECT_FEEDBACK_LOOP_VERIFY")
FIX_CMD = os.getenv("PROJECT_FEEDBACK_LOOP_FIX_CMD")
MAX_RETRIES = int(os.getenv("PROJECT_FEEDBACK_LOOP_MAX_RETRIES", "6"))

if not VERIFY_CMD:
    raise SystemExit("PROJECT_FEEDBACK_LOOP_VERIFY is required")


@dataclass
class Result:
    returncode: int
    stdout: str
    stderr: str

    @property
    def combined(self) -> str:
        return f"{self.stdout}\n{self.stderr}".strip()


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def run(cmd: str) -> Result:
    proc = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return Result(proc.returncode, proc.stdout, proc.stderr)


def categorize(text: str) -> str:
    lowered = text.lower()
    if re.search(r"prettier|format|black|ruff format|unformatted", lowered):
        return "format"
    if re.search(r"eslint|ruff check|lint|flake8|sonar", lowered):
        return "lint"
    if re.search(r"mypy|pyright|tsc|typecheck|typing", lowered):
        return "type"
    if re.search(r"pytest|vitest|assertionerror|test failed|failing test", lowered):
        return "unit"
    if re.search(r"playwright|e2e|integration", lowered):
        return "integration"
    if re.search(r"module not found|cannot find|importerror|environment|command not found", lowered):
        return "env"
    return "unknown"


def append_history(entry: dict) -> None:
    HISTORY.parent.mkdir(parents=True, exist_ok=True)
    with HISTORY.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def main() -> int:
    FAILURE_FILE.parent.mkdir(parents=True, exist_ok=True)

    if GENERATE_CMD:
        gen = run(GENERATE_CMD)
        if gen.returncode != 0:
            print(gen.combined, file=sys.stderr)
            return gen.returncode

    for attempt in range(1, MAX_RETRIES + 2):
        verification = run(VERIFY_CMD)
        if verification.returncode == 0:
            append_history(
                {
                    "ts": now(),
                    "attempt": attempt,
                    "status": "pass",
                    "verify": VERIFY_CMD,
                }
            )
            print("Verification passed.")
            return 0

        category = categorize(verification.combined)
        FAILURE_FILE.write_text(verification.combined, encoding="utf-8")
        append_history(
            {
                "ts": now(),
                "attempt": attempt,
                "status": "fail",
                "category": category,
                "verify": VERIFY_CMD,
                "failure_file": str(FAILURE_FILE),
            }
        )

        if attempt > MAX_RETRIES or not FIX_CMD:
            print(verification.combined, file=sys.stderr)
            print(f"Stopped after attempt {attempt}. Category: {category}", file=sys.stderr)
            return verification.returncode

        env = os.environ.copy()
        env["PFL_ATTEMPT"] = str(attempt)
        env["PFL_CATEGORY"] = category
        env["PFL_FAILURE_FILE"] = str(FAILURE_FILE)
        env["PFL_VERIFY_CMD"] = VERIFY_CMD

        fix = subprocess.run(FIX_CMD, shell=True, env=env)
        if fix.returncode != 0:
            print(f"Fix command failed on attempt {attempt}", file=sys.stderr)
            return fix.returncode

    return 1


if __name__ == "__main__":
    raise SystemExit(main())

