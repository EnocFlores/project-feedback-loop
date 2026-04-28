# skills/project-feedback-loop/templates/python/tools/watch_verify.py
from __future__ import annotations

import subprocess

from watchfiles import watch

VERIFY_CMD = "python -m nox -s verify"

print(f"Watching project and rerunning: {VERIFY_CMD}")
for _changes in watch("."):
    result = subprocess.run(VERIFY_CMD, shell=True)
    if result.returncode == 0:
        print("verify: pass")
    else:
        print(f"verify: fail ({result.returncode})")
