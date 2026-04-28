# skills/project-feedback-loop/templates/python/src/example_pkg/core.py
from __future__ import annotations

def normalize_id(value: int | str) -> str:
    if isinstance(value, int):
        if value < 0:
            raise ValueError("value must be non-negative")
        return f"user-{value}"

    cleaned = value.strip().lower()
    if not cleaned:
        raise ValueError("value cannot be empty")
    return cleaned

