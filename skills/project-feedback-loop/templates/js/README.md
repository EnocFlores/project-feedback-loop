# JavaScript template

This template is a strict TS-first JavaScript scaffold for repositories that want a deterministic feedback loop.

## Included tooling

- ESLint with strict TypeScript and complexity rules
- Prettier for formatting
- Vitest for tests and coverage
- Husky for fast pre-commit verification
- GitHub Actions CI running the full verify contract

## Commands

- install: `npm install`
- lint: `npm run lint`
- lint fix: `npm run lint:fix`
- format: `npm run format`
- format check: `npm run format:check`
- typecheck: `npm run typecheck`
- test: `npm run test`
- CI test: `npm run test:ci`
- fast verify: `npm run verify:fast`
- full verify: `npm run verify`
- watch tests: `npm run watch:test`
- watch types: `npm run watch:typecheck`
- single test file: `npx vitest run tests/sum.test.ts`
- single test by name: `npx vitest run -t "adds two numbers"`

## Contract

- canonical verify command: `npm run verify`
- fast local verify command: `npm run verify:fast`
- CI command: `npm run verify`

## Style expectations

- strict TypeScript with `noEmit`
- semicolons, double quotes, no trailing commas, width 100
- no `console`
- no `any`
- prefer type-only imports when applicable
- decompose functions instead of fighting complexity limits
