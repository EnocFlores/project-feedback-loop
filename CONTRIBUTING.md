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
- `skills/project-feedback-loop/templates/` contains shared, JS, Python, and Rust scaffolds

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
- real-world usage reports that identify transferable guardrails, template gaps, or prompt improvements

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

## Share skill feedback from real usage

If you used this skill on a real repository, the most useful feedback is concrete: what the skill detected, what it missed, what it recommended, what you had to correct, and what should become a reusable rule, prompt, template, or reference.

You can paste one of these prompts into your coding agent after using the skill.

### Short feedback prompt

```text
We just used the project-feedback-loop skill on this repository.

Please extract concrete feedback for the skill maintainers.

Return an issue-ready report with:
- repository shape: language, framework, package manager, test stack, CI, hook setup
- detected classification: Loop Level (L0-L3) and Repo Profile (R1-R4), if known
- what the skill did well
- what the skill missed or under-emphasized
- any recommendation that was wrong, risky, too generic, or not actionable
- any tool, command, threshold, or config that should be added to a template
- any repeated failure pattern that should become a rule, prompt, test, or reference
- exact commands or files involved, when safe to share
- a concise proposed improvement to the skill

Do not include secrets, private URLs, credentials, customer data, or proprietary code.
```

### Deep knowledge-extraction prompt

```text
We used the project-feedback-loop skill on this repository and want to improve the public skill.

Analyze the full interaction and extract transferable knowledge.

Focus on:
- where the skill helped create a tighter feedback loop
- where the agent needed human correction or extra prompting
- guardrails that should have been detected earlier
- checks that existed but were not verified as active
- missing template commands, CI steps, hook checks, dependency checks, visual checks, observability loops, or language-specific defaults
- places where the skill was too strict, too loose, or not specific enough for this repo profile
- whether the final approach should apply to greenfield, established, legacy, or platform-scale repos
- whether the improvement belongs in SKILL.md, a prompt, a reference doc, a language template, README docs, or AGENTS guidance

Format the result as a GitHub issue with:
- title
- summary
- repo context
- classification
- observed gap
- expected behavior
- actual behavior
- suggested skill change
- suggested template or doc files to update
- acceptance criteria

Do not include secrets, private URLs, credentials, customer data, or proprietary code.
```

### Issue report template

```md
## Summary

<!-- What should the skill learn from this usage? -->

## Repository context

- Language/framework:
- Package manager/toolchain:
- Test stack:
- CI provider:
- Hook setup:
- Runtime/deployment context, if relevant:

## Classification

- Loop Level: `L? - ...`
- Repo Profile: `R? - ...`

## What worked well

-

## What the skill missed

-

## Expected behavior

-

## Actual behavior

-

## Suggested improvement

-

## Suggested files to update

-

## Acceptance criteria

-

## Safety notes

- [ ] No secrets included
- [ ] No private URLs included
- [ ] No credentials included
- [ ] No customer or proprietary data included
```

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

### Rust template

Working directory: `skills/project-feedback-loop/templates/rust`

- install tooling: `rustup component add rustfmt clippy && cargo install cargo-nextest --locked && cargo install cargo-deny --locked`
- format: `cargo fmt`
- format check: `cargo fmt --check`
- compiler check: `cargo check --workspace --all-targets --all-features`
- lint: `cargo clippy --workspace --all-targets --all-features -- -D warnings`
- test: `cargo nextest run --workspace --all-features`
- doctests: `cargo test --doc --workspace --all-features`
- dependency checks: `cargo deny check`
- full verify: `./scripts/verify.sh`
- install hooks: `./scripts/install-hooks.sh`
- verify hooks: `./scripts/verify-hooks.sh`

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
