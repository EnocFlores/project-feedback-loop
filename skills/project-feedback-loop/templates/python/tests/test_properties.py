# skills/project-feedback-loop/templates/python/tests/test_properties.py
from hypothesis import given
from hypothesis import strategies as st

from example_pkg.core import normalize_id


@given(st.integers(min_value=0, max_value=1_000_000))
def test_non_negative_ints_always_produce_user_prefix(value: int) -> None:
    assert normalize_id(value).startswith("user-")


@given(st.text(min_size=1).filter(lambda value: value.strip() != ""))
def test_non_empty_strings_never_return_empty(value: str) -> None:
    assert normalize_id(value) != ""
