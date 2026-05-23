# Project Feedback Loop

An installable Agent Skills package for turning software repositories into deterministic feedback systems.

`project-feedback-loop` helps an agent inspect a codebase, define a canonical verification contract, apply the smallest safe repair, and harden the repository over time instead of relying on repeated reminders.

The approach is inspired by [The Feedback Loop Is All You Need](https://zernie.com/blog/feedback-loop-is-all-you-need/): instructions help agents get things right faster, but durable quality comes from fast, repeatable, automated feedback.

## Install

Primary install method:

```bash
npx skills add EnocFlores/project-feedback-loop
```

This uses the standard `skills` installer for Agent Skills-compatible clients.

## Quick start

After installing, use the skill in a repository you want to harden. For example:

```text
Audit this repo and set up a strict feedback loop.
Classify it, define the canonical verify command, and recommend the next smallest high-signal guardrails.
```

## Manual local install

If you need a fallback path, copy or symlink `skills/project-feedback-loop/` into a supported local skills directory such as:

- `.agents/skills/project-feedback-loop/`
- `~/.agents/skills/project-feedback-loop/`
- a client-specific skills directory supported by your agent host

The skill directory must contain `SKILL.md` at its root.

## Why this exists

Modern coding agents can move quickly, but speed without constraints creates drift.

A repository stays healthy when the loop is tight:

- define one objective verify command
- run deterministic checks early and often
- classify failures instead of hand-waving them away
- apply the smallest safe repair
- convert recurring failures into stronger rules, tests, or docs

This repository packages that workflow as a reusable skill.

## Classification model

The skill now classifies repositories on two independent axes before recommending changes:

- `Loop Level`: `L0 - Vibes`, `L1 - Guardrails`, `L2 - Architecture as Code`, `L3 - Organism`
- `Repo Profile`: `R1 - Greenfield`, `R2 - Established, Tighten-able`, `R3 - Legacy, High-Complexity`, `R4 - Mixed/Platform-Scale`

Use the pair together, for example `L1 / R3`, to choose the next smallest high-signal upgrade.

- `L0 / R1` usually means start strict immediately.
- `L1 / R3` usually means stabilize the loop first, then ratchet guardrails upward in stages.

## What the skill does

The skill is designed to help agents and maintainers:

- scaffold or upgrade guardrails in a repository
- define a single canonical verification command
- run a repair loop until verification passes or the retry budget is exhausted
- record recurring failure signatures for future hardening
- prefer deterministic enforcement over purely advisory instructions

It is intentionally strict for new repositories, but flexible for established and legacy repositories that need staged tightening instead of one disruptive rewrite.

- new repositories should start strict and keep the contract narrow, explicit, and automated
- established repositories should tighten in planned iterations
- legacy or platform-scale repositories should adopt the loop safely at the current threshold, then ratchet complexity and drift down over time

Best fit:

- new repositories that want strict defaults from the start
- established repositories that need gradual tightening without stalling delivery
- legacy or platform-scale repositories that need safe adoption first, then iterative hardening

It is a good fit when you want an agent to do useful work without silently drifting away from team conventions, architectural boundaries, or quality expectations.

## What is included

The packaged skill lives at `skills/project-feedback-loop/` and helps an agent:

- detect project shape before making assumptions
- choose conservative, ecosystem-standard guardrails
- create or update repository instructions such as `AGENTS.md`
- define exactly one canonical verify command per target project
- run a narrow-fix-verify cycle instead of broad speculative rewrites
- record recurring failure families so they can become stronger guardrails

Supported project shapes currently include:

- TS-first JavaScript repositories
- Python repositories
- Rust crates and workspaces
- mixed repositories, when a root verification contract is defined

## How the loop works

At a high level, the skill follows this sequence:

1. Inspect the repository structure and existing tooling.
2. Determine the appropriate verification contract.
3. Run the current checks and classify failures.
4. Apply the smallest safe fix.
5. Re-run the narrowest relevant validation.
6. Re-run full verification.
7. Record repeated failure signatures for future hardening.

The goal is not just to make the current run pass. The goal is to make the next failure less likely.

When the project shape justifies it, the skill also highly recommends:

- visual verification loops for UI-heavy repositories
- observability-backed loops for deployed or user-facing systems
- custom lint and architecture checks for repeated design or migration drift

## For maintainers

This repository is organized as a single-skill package.

```text
.
├── README.md
├── CONTRIBUTING.md
└── skills/
    └── project-feedback-loop/
        ├── SKILL.md
        ├── README.md
        ├── prompts/
        ├── references/
        ├── scripts/
        ├── state/
        └── templates/
```

Key paths:

- `skills/project-feedback-loop/SKILL.md` - primary skill contract and execution rules
- `skills/project-feedback-loop/README.md` - skill-local usage and package notes
- `skills/project-feedback-loop/prompts/` - planner, fixer, and hardener prompts
- `skills/project-feedback-loop/references/maturity-modes.md` - loop level and repo profile classification guidance
- `skills/project-feedback-loop/references/recommended-feedback-loops.md` - visual and observability loop guidance
- `skills/project-feedback-loop/scripts/` - optional repair-loop wrappers
- `skills/project-feedback-loop/state/` - learned patterns, decisions, and run history
- `skills/project-feedback-loop/templates/` - shared, JS, Python, and Rust scaffolds

## Templates

The skill ships with reference templates for common project types.

### JavaScript / TypeScript template

Located in `skills/project-feedback-loop/templates/js`.

Highlights:

- ESLint with complexity limits and strict TypeScript rules
- Prettier for deterministic formatting
- Vitest for test execution and coverage
- Husky pre-commit verification
- GitHub Actions CI running the full verify contract

Representative commands:

```bash
npm run lint
npm run typecheck
npm run test:ci
npm run verify
```

### Python template

Located in `skills/project-feedback-loop/templates/python`.

Highlights:

- Ruff and Black for linting and formatting
- mypy in strict mode
- pytest and Hypothesis for test coverage and property checks
- Nox as the canonical command runner
- GitHub Actions CI running `nox -s verify`

Representative commands:

```bash
nox -s lint
nox -s typecheck
nox -s tests
nox -s verify
```

### Rust template

Located in `skills/project-feedback-loop/templates/rust`.

Highlights:

- rustfmt for deterministic formatting
- Clippy with warnings denied
- `cargo check` for compiler and build validation
- `cargo nextest` for fast test execution plus separate doctests
- `cargo-deny` for dependency policy checks
- GitHub Actions CI running `./scripts/verify.sh`
- repo-owned `.githooks/pre-commit` hook support

Representative commands:

```bash
./scripts/verify.sh
cargo clippy --workspace --all-targets --all-features -- -D warnings
cargo nextest run --workspace --all-features
cargo test --doc --workspace --all-features
cargo deny check
```

## Helper runners

The repository also includes optional wrapper scripts for repair-loop orchestration:

- `skills/project-feedback-loop/scripts/agent-runner.py`
- `skills/project-feedback-loop/scripts/agent-runner.mjs`
- `skills/project-feedback-loop/scripts/watch-verify.py`

These wrappers are driven by environment variables so a repository can define its own verify command, fix command, retry budget, and failure logging path.

## Usage ideas

Use the installed skill when you want an agent to:

- bootstrap a repo with linting, formatting, typing, tests, hooks, and CI
- harden an existing repo around a stricter verify loop
- keep a repo green while larger edits are in progress
- turn recurring failure patterns into tests, rules, or clearer documentation

## Philosophy

This project treats feedback as infrastructure.

- instructions explain intent and speed up first-pass quality
- linters and type systems prevent common mistakes from recurring
- tests catch behavioral regressions
- CI provides an objective gate
- failure history informs the next hardening step

If a failure pattern repeats, the right answer is usually not another reminder. It is a stronger constraint.

## Contributing

Good contributions usually strengthen determinism rather than weaken it.

Examples:

- tighter, better-justified validation rules
- clearer prompts and references
- stronger templates with conservative defaults
- improved failure classification and history recording
- docs that make the workflow easier to adopt without lowering standards

See `CONTRIBUTING.md` for contribution flow and template-specific verification commands.

## License

MIT.
