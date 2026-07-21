# AGENTS.md

This repository uses a strict automated feedback loop.

## Canonical commands

- Install: {{INSTALL_COMMAND}}
- Verify: {{VERIFY_COMMAND}}
- Fast verify: {{FAST_VERIFY_COMMAND}}
- Watch: {{WATCH_COMMAND}}

Use `Not configured` for commands that are intentionally unavailable in the target stack.

## Verification policy

1. Run the narrowest relevant check after a small fix.
2. Re-run full verify before considering the task done.
3. Never weaken lint, type checking, tests, or CI to get green.
4. If the same failure family repeats twice, add a regression test, stronger rule, or a clearer project instruction.

## Safe automatic changes

Allowed:
- formatter rewrites
- linter safe fixes
- import sorting
- new regression tests
- AGENTS.md clarifications

Not allowed without approval:
- lowering strictness
- deleting tests
- updating snapshots without clear intent
- broad dependency upgrades
- destructive Git operations

## Architecture notes

- Keep functions small and decomposed.
- Prefer explicit boundaries over implicit conventions.
- Treat CI as the final source of truth, not local success alone.
