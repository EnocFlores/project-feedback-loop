# Recommended feedback loops

Use these loops when the project shape justifies them. They are optional, but highly recommended when the risk is real.

## Structural guardrails

Recommend structural guardrails when:

- the repository has no complexity or size constraints on production code
- hotspot files keep triggering review pain or repair-loop churn
- architecture drift is visible, but still treated as a manual cleanup problem
- the ecosystem supports mature static checks for complexity, file size, depth, or cognitive complexity

Rollout guidance:

- call out missing structural guardrails explicitly during planning or audit
- classify them as `must add now`, `recommended next`, or `intentionally deferred`
- prefer repo-wide lower-strictness thresholds first, then ratchet down over time
- avoid hotspot carve-outs or path-based exemptions as the default strategy
- reserve narrow exemptions for clearly different surfaces such as tests or generated code

Examples:

- JS/TS: `complexity`, `max-depth`, `max-lines-per-function`, `max-params`, `max-statements`, and cognitive complexity rules
- Rust: `cargo clippy --workspace --all-targets --all-features -- -D warnings`, `cargo check --workspace --all-targets --all-features`, and `cargo deny check`
- other ecosystems: the strongest mainstream structural checks available for module size, branching complexity, or maintainability

## Hook health

Recommend explicit hook-health checks when:

- the repository relies on Git hooks for local enforcement
- `.pre-commit-config.yaml` or similar hook config exists, but activation is not verified
- `core.hooksPath` may differ from the default Git hook directory
- optional provisioners or task runners are introduced for setup convenience

Rollout guidance:

- detect `core.hooksPath` and the active hook directory
- verify that real hook files exist where Git will execute them
- treat optional provisioners such as `mise` as accelerators for setup, not proof of durable hook activation
- prefer a repo-owned install-and-verify flow after provisioning completes

## Visual verification

Recommend visual checks when:

- the repository ships a UI
- layout, styling, or interaction regressions are costly
- design-system drift is a known problem
- a page can look wrong while unit tests still pass

Examples:

- Playwright screenshots for critical pages and flows
- Storybook visual review tools such as Chromatic
- focused browser checks for modals, z-index, layout shifts, and clickability

## Observability-backed loops

Recommend runtime feedback when:

- the project is deployed or user-facing
- async jobs, queues, webhooks, or background processes exist
- failures appear only in staging or production conditions
- static checks cannot prove that wiring or behavior is actually correct

Examples:

- error and performance monitoring through tools such as Sentry or Datadog
- alerts or issue creation tied to recurring runtime failures
- integration checks that boot the system and verify real behavior

## Escalation guidance

- `L0 -> L1`: canonical verify command, strict local gate, and CI parity.
- `L1 -> L2`: custom lint rules, architecture checks, and stronger static enforcement.
- `L2 -> L3`: visual verification, observability-backed loops, or both when static checks miss important failures.
- Repeated architecture drift should bias toward custom lint rules or stronger static checks.
- Repeated UI regressions should bias toward visual verification in CI.
- Repeated runtime regressions should bias toward observability, integration checks, or both.
