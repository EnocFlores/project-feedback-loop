# Contributing

Thanks for helping improve `project-feedback-loop`.

This repository packages a single public skill. Good contributions usually strengthen determinism rather than weaken it.

## Before you change anything

- read `README.md` for the public product story
- read `skills/project-feedback-loop/SKILL.md` for the skill contract
- read `skills/project-feedback-loop/README.md` for package structure
- read `skills/project-feedback-loop/references/maturity-modes.md` for the classification model
- read `skills/project-feedback-loop/references/recommended-feedback-loops.md` for visual and observability guidance

If you are editing templates, also read the relevant local config files first.

## Contribution flow

1. Read the core docs for the public story, skill contract, and classification model.
2. Make a focused change that improves determinism, clarity, or reusable packaging.
3. Run the smallest relevant check while iterating, then the full verify command for the affected template.
4. Explain the behavior, packaging, and docs impact clearly in the PR.

## Repository structure

- `skills/project-feedback-loop/` contains the packaged skill
- `skills/project-feedback-loop/prompts/` contains planner, fixer, and hardener prompts
- `skills/project-feedback-loop/scripts/` contains repair-loop helpers
- `skills/project-feedback-loop/state/` contains learned patterns and decisions
- `skills/project-feedback-loop/templates/` contains shared, JS, and Python scaffolds

## Contribution principles

Prefer changes that:

- tighten validation or clarify constraints
- improve skill instructions without making them host-specific
- add regression coverage for real failure patterns
- make templates more deterministic and easier to verify
- improve public docs without overstating what the repo supports today

Good contributions include:

- docs clarifications that make the public story or skill contract easier to adopt
- stronger prompt and reference guidance grounded in real failure patterns
- conservative template improvements that increase determinism
- additional supported language templates with concrete verify, lint, test, and CI flows
- regression coverage for bugs or drift patterns the skill should help prevent

When adding a new language template, keep the quality bar aligned with the existing package:

- define one canonical verify command
- include template-specific docs and commands
- wire local validation and CI clearly
- prefer strict defaults where practical
- support staged adoption when the ecosystem or legacy baseline requires it

Avoid changes that:

- lower lint, type, or test strictness to get green
- delete tests or weaken assertions without strong justification
- add speculative abstractions that are not yet needed
- make public claims about publishing or installation flows that are not verified

## Validation workflow

Use the smallest relevant check while iterating, then run the full verify command for the affected template before asking for review.

### JavaScript template

Working directory: `skills/project-feedback-loop/templates/js`

- install: `npm install`
- lint: `npm run lint`
- typecheck: `npm run typecheck`
- test: `npm run test`
- full verify: `npm run verify`
- single test file: `npx vitest run tests/sum.test.ts`
- single test by name: `npx vitest run -t "adds two numbers"`

### Python template

Working directory: `skills/project-feedback-loop/templates/python`

- bootstrap nox: `pipx install nox`
- install: `python -m pip install -e ".[dev]"`
- format: `nox -s format`
- lint: `nox -s lint`
- typecheck: `nox -s typecheck`
- tests: `nox -s tests`
- full verify: `nox -s verify`
- single test file: `pytest tests/test_core.py -q`
- single test case: `pytest tests/test_core.py::test_normalize_id_from_int -q`

## Definition of done

- the affected template or docs surface is updated consistently
- the relevant verify command was run when a template changed
- no protections were weakened to get green
- public-facing docs do not overclaim what the package supports
- the `Loop Level` (`L0-L3`) and `Repo Profile` (`R1-R4`) model remains intact

## Docs changes

- keep `README.md` public, polished, and product-style
- keep `skills/project-feedback-loop/SKILL.md` focused on activation behavior, not installation
- keep install instructions at the root repo level unless a file is explicitly maintainer-facing
- present visual verification and observability-backed loops as optional, but highly recommended when project risk justifies them
