# Python template

This template is a strict Python scaffold for repositories that want a deterministic feedback loop.

## Included tooling

- Ruff and Black for linting and formatting
- mypy in strict mode
- pytest and Hypothesis for automated checks
- pre-commit hooks for local enforcement
- durable hook install and activation verification through Nox
- Nox as the canonical command runner
- GitHub Actions CI running the full verify contract

## Commands

- bootstrap nox: `pipx install nox`
- install: `python -m pip install -e ".[dev]"`
- format: `nox -s format`
- lint: `nox -s lint`
- typecheck: `nox -s typecheck`
- tests: `nox -s tests`
- full verify: `nox -s verify`
- install hooks: `nox -s install_hooks`
- verify hooks: `nox -s verify_hooks`
- watch: `nox -s watch`
- single test file: `pytest tests/test_core.py -q`
- single test case: `pytest tests/test_core.py::test_normalize_id_from_int -q`

## Contract

- canonical verify command: `nox -s verify`
- CI command: `nox -s verify`
- formatter command: `nox -s format`
- hook install command: `nox -s install_hooks`
- hook health command: `nox -s verify_hooks`

## Hook activation

`.pre-commit-config.yaml` is not enough by itself. Use the repo-owned Nox sessions to install and verify durable Git hook files.

- detect `core.hooksPath` before assuming hooks live in `.git/hooks`
- verify that real `pre-commit` and `pre-push` hook files exist at the active Git hook path
- use optional provisioning tools such as `mise` to bootstrap and discover commands if helpful, but let Nox own the durable install and verification workflow

## Style expectations

- Python 3.12+
- explicit annotations on public functions
- Black and Ruff width 100
- mypy strict mode
- validate boundary inputs explicitly
- prefer small, readable functions over broad helpers
