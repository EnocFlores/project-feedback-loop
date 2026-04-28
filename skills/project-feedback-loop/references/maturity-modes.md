# Maturity modes

Use these modes to choose a safe starting posture without giving up long-term tightening.

## Greenfield

- Prefer strict defaults immediately.
- Add one canonical verify command before feature work grows.
- Keep complexity caps low enough that decomposition is required early.
- Add hooks and CI at the same time as lint, type, and test tooling.

## Established but tighten-able

- Preserve the current delivery path while introducing an objective verify contract.
- Tighten the highest-value gaps first: formatting, linting, type safety, and core tests.
- Convert recurring review comments into automated checks as soon as the pattern is clear.
- Raise new protections in staged iterations instead of one broad cleanup.

## Legacy high-complexity

- Start from the safest threshold that the repository can actually adopt.
- Document which limits are temporarily higher and why.
- Require a ratchet-down plan for complexity, drift, and missing coverage.
- Each iteration should remove one source of tolerated inconsistency.

## Ratchet rules

- Never lower protections to get green.
- Temporary exceptions must have an exit path.
- When a stricter threshold is not yet feasible, keep the canonical verify contract stable and narrow the gap in later passes.
