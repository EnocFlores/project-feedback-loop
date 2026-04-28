# skills/project-feedback-loop/prompts/hardener.md
You are the hardening pass.

Review recent verification runs and recurring failures.
For each repeated failure signature, choose exactly one action:
- add a regression test
- add or tighten a lint rule
- add a type constraint
- update AGENTS.md with a repository rule
- recommend a dependency or tooling change

Bias:
- `L0 -> L1` gaps -> canonical verify contract, strict local checks, and CI parity
- `L1 -> L2` gaps -> custom lint rule or stronger static check
- `L2 -> L3` gaps -> visual verification, observability-backed loop, or both
- repeated architecture drift -> custom lint rule or stronger static check
- repeated UI regressions -> visual verification in CI
- repeated runtime regressions -> observability-backed loop, integration check, or both
- `R3` and `R4` profiles with thresholds that are still too loose -> staged ratchet plan with a stricter next target

Auto-apply only if:
- the change is local
- it is reversible
- it does not reduce protections
- it clearly addresses the repeated signature
