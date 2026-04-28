# Python template

This template is a strict Python scaffold for repositories that want a deterministic feedback loop.

## Included tooling

- Ruff and Black for linting and formatting
- mypy in strict mode
- pytest and Hypothesis for automated checks
- pre-commit hooks for local enforcement
- Nox as the canonical command runner
- GitHub Actions CI running the full verify contract

## Commands

- install: `python -m pip install -e ".[dev]"`
- lint: `nox -s lint`
- typecheck: `nox -s typecheck`
- tests: `nox -s tests`
- full verify: `nox -s verify`
- watch: `nox -s watch`
- single test file: `pytest tests/test_core.py -q`
- single test case: `pytest tests/test_core.py::test_normalize_id_from_int -q`

## Contract

- canonical verify command: `nox -s verify`
- CI command: `nox -s verify`

## Style expectations

- Python 3.12+
- explicit annotations on public functions
- Black and Ruff width 100
- mypy strict mode
- validate boundary inputs explicitly
- prefer small, readable functions over broad helpers
