# Recommended feedback loops

Use these loops when the project shape justifies them. They are optional, but highly recommended when the risk is real.

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
