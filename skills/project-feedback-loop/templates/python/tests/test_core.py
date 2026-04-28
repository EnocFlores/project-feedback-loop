# skills/project-feedback-loop/templates/python/tests/test_core.py
from example_pkg.core import normalize_id

def test_normalize_id_from_int() -> None:
    assert normalize_id(7) == "user-7"

def test_normalize_id_from_str() -> None:
    assert normalize_id(" Alice ") == "alice"

