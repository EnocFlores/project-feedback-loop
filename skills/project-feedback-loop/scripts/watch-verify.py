# skills/project-feedback-loop/scripts/watch-verify.py
#!/usr/bin/env python3
from __future__ import annotations

import os
import subprocess
from pathlib import Path
from watchfiles import watch

VERIFY_CMD = os.getenv("PROJECT_FEEDBACK_LOOP_VERIFY", "echo 'set PROJECT_FEEDBACK_LOOP_VERIFY'")
ROOT = Path(os.getenv("PROJECT_FEEDBACK_LOOP_WATCH_ROOT", "."))

print(f"Watching {ROOT.resolve()} and rerunning: {VERIFY_CMD}")

for _changes in watch(ROOT):
    result = subprocess.run(VERIFY_CMD, shell=True)
    if result.returncode == 0:
        print("verify: pass")
    else:
        print(f"verify: fail ({result.returncode})")

