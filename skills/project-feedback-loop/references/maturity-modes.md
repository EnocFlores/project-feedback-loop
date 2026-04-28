# Classification model

Use two axes so the plan reflects both current enforcement and repository scale.

## Loop Level

### L0 - Vibes

- No reliable automated enforcement exists.
- Humans catch most drift in review.
- First target: one canonical verify command plus CI parity.

### L1 - Guardrails

- Standard lint, type, test, and CI checks exist.
- Architectural drift still gets through.
- Next target: move repeated review comments into enforceable rules.

### L2 - Architecture as Code

- Custom rules encode team conventions, migration boundaries, or design constraints.
- The repository can block known drift deterministically.
- Next target: add visual or runtime loops where static checks are not enough.

### L3 - Organism

- Rules, CI, visual or runtime feedback, and task intake reinforce each other.
- The loop learns from repeated failures.
- Focus on keeping signals trustworthy and high-signal.

## Repo Profile

### R1 - Greenfield

- Prefer strict defaults immediately.
- Add one canonical verify command before feature work grows.
- Keep complexity caps low enough that decomposition is required early.
- Add hooks and CI at the same time as lint, type, and test tooling.

### R2 - Established, Tighten-able

- Preserve the current delivery path while introducing an objective verify contract.
- Tighten the highest-value gaps first: formatting, linting, type safety, and core tests.
- Convert recurring review comments into automated checks as soon as the pattern is clear.
- Raise new protections in staged iterations instead of one broad cleanup.

### R3 - Legacy, High-Complexity

- Start from the safest threshold that the repository can actually adopt.
- Document which limits are temporarily higher and why.
- Require a ratchet-down plan for complexity, drift, and missing coverage.
- Each iteration should remove one source of tolerated inconsistency.

### R4 - Mixed/Platform-Scale

- Coordinate one canonical contract per surface and one clear root entry point.
- Keep ownership and dependency boundaries explicit.
- Tighten shared standards without breaking valid per-surface differences.
- Prefer staged rollouts for cross-language or cross-team guardrails.

## Ratchet rules

- Never lower protections to get green.
- Temporary exceptions must have an exit path.
- When a stricter threshold is not yet feasible, keep the canonical verify contract stable and narrow the gap in later passes.

## Pairing guidance

- `L0 / R1`: start strict immediately.
- `L0 / R3`: establish the verify contract first, then raise standards in stages.
- `L1 / R2`: add custom rules for repeated drift.
- `L2 / R3`: preserve delivery, then add the next targeted guardrail and lower one threshold.
- `L2 / R4`: prefer coordinated boundary checks and shared feedback contracts.
- `L3 / any`: keep loops trustworthy; remove flakes fast.
