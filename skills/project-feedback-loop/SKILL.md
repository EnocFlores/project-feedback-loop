---
name: project-feedback-loop
description: Scaffold or upgrade a software project with a strict automated feedback loop. Use for JS, TS, Python, or mixed repositories when the user wants guardrails, tests, hooks, CI, repair loops, or continuous hardening.
metadata:
  author: EnocFlores
  workflow: scaffold-verify-harden
  version: "1.0.0"
---

# Project Feedback Loop

## What this skill does

This skill turns a repository into a system with deterministic guardrails.

It will:
- inspect project state
- choose a language-appropriate conservative stack
- scaffold missing config, hooks, CI, and AGENTS.md
- define one canonical verification command
- run a repair loop until verification passes or the retry budget is exhausted
- record recurring failure signatures and hardening actions

## Execution rules

1. Detect the project shape first.
   - JS or TS: look for package.json, tsconfig.json, eslint and test config
   - Python: look for pyproject.toml, requirements files, noxfile.py, pytest config
   - Mixed: detect both and define a root-level verify contract

2. Prefer conservative defaults.
   - JS or TS: ESLint + Prettier + strict TypeScript + Vitest + Husky
   - Python: Ruff + Black + mypy + pytest + pre-commit + watchfiles + Nox

3. Always create or update AGENTS.md.
   Include:
   - install command
   - canonical verify command
   - focused repair order
   - any architectural constraints discovered during setup

4. Define exactly one canonical verification contract.
   - JS or TS default: `npm run verify`
   - Python default: `nox -s verify`
   - Mixed repos: a root command that dispatches to both

5. Repair loop policy.
   - run verify
   - classify failures: format, lint, type, unit, integration, env, dependency, architecture drift
   - apply the smallest safe fix
   - rerun the narrowest relevant checks
   - rerun full verify

6. Continuous hardening.
    - if the same failure family appears twice, add a regression test, stronger lint rule, type constraint, or AGENTS.md rule
    - log significant repetitions in `state/patterns.yml`
    - append runs to `state/history.jsonl`

## NEVER

- **NEVER rely on instructions alone when a deterministic check can enforce the rule**
  **Instead:** encode the rule in linting, typing, tests, hooks, or CI.
  **Why:** prompts and AGENTS.md improve first-pass behavior, but only automated checks keep the repo aligned under repeated agent edits.

- **NEVER weaken lint, type, test, or CI requirements just to get green**
  **Instead:** make the smallest safe fix, or stop and report the blocker when the retry budget is exhausted.
  **Why:** a green build with weaker protections breaks the feedback loop and lets the same defect family return.

- **NEVER keep repeating the same manual repair for the same failure family**
  **Instead:** convert repeated failures into one stronger guardrail: a regression test, stricter type, lint rule, or AGENTS.md rule.
  **Why:** the loop should tighten over time; repeated fixes without hardening create review toil instead of system learning.

- **NEVER define multiple competing verify commands for the same repository**
  **Instead:** publish one canonical verify command and make local fast checks subordinate to it.
  **Why:** agents need one objective contract; multiple sources of truth create drift and false confidence.

## Safe auto-apply rules

Safe by default:
- formatter rewrites
- linter safe fixes
- import sorting
- adding or tightening regression tests
- updating AGENTS.md with verified commands

Require explicit approval:
- removing tests
- lowering strictness
- broad dependency upgrades
- snapshot updates with unclear intent
- deleting files outside obvious scaffolding cleanup
- commits, pushes, or destructive Git operations

## Retry budget

- total verify retries: 6
- repeated retries for the same signature: 2
- max files changed in one repair step: 10

If the budget is exhausted:
- stop making speculative edits
- summarize blockers
- recommend the next hardening action
- do not silently weaken checks

## Supporting files

MANDATORY READ:
- Read `references/primary-sources.md` before introducing or changing verification tooling, hooks, CI, AGENTS.md conventions, or language-specific stack defaults.

Use these prompts when planning or repairing work:
- `prompts/planner.md`
- `prompts/fixer.md`
- `prompts/hardener.md`

Use these templates when scaffolding:
- `templates/common/*`
- `templates/js/*`
- `templates/python/*`

Use these helper scripts when a wrapper loop is useful:
- `scripts/agent-runner.py`
- `scripts/agent-runner.mjs`
- `scripts/watch-verify.py`
