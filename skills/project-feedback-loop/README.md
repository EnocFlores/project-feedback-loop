# project-feedback-loop skill

This directory contains the packaged skill that is installed from the root repository.

Use this skill when you want an agent to bootstrap or harden a repository around a strict automated feedback loop.

## Core outcomes

- scaffold or upgrade guardrails
- define one canonical verify command
- run a repair loop until green or until the retry budget is exhausted
- convert recurring failures into stronger checks

## Package contents

- `SKILL.md` defines the activation contract and execution rules
- `prompts/` contains planner, fixer, and hardener prompts
- `references/` contains background material used to shape the skill
- `scripts/` contains optional repair-loop helpers
- `state/` stores learned patterns, decisions, and run history
- `templates/` contains shared, JS, and Python scaffolds

## Supported templates

- `templates/js/` for TS-first JavaScript projects
- `templates/python/` for Python projects
- `templates/common/` for shared `AGENTS.md` scaffolding

See `templates/js/README.md` and `templates/python/README.md` for template-specific commands and conventions.

## State

- `state/history.jsonl` stores verification attempts and outcomes
- `state/patterns.yml` stores recurring failure signatures and recommended hardening actions
- `state/decisions.md` stores small human-readable design notes

## Helper runners

- `scripts/agent-runner.py`
- `scripts/agent-runner.mjs`
- `scripts/watch-verify.py`

These are optional wrappers around:

1. an objective verification command
2. a fix command that can repair or continue the workflow
3. a retry budget and failure-log path
