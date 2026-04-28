# skills/project-feedback-loop/state/decisions.md

## Initial defaults

- Use native agent orchestration and standard skill-install flows before adding custom wrappers.
- Prefer one canonical verify command per repository.
- Prefer conservative, ecosystem-standard stacks by default.

## Hardening notes

- Repeated production logging violations should become lint rules.
- Repeated boundary-condition bugs should become property or regression tests.
- Never auto-reduce strictness to get green.
