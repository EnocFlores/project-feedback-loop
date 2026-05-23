# Rust template

This template is a strict Rust scaffold for crates and workspaces that want a deterministic feedback loop.

## Included tooling

- rustfmt for formatting
- Clippy with warnings denied
- `cargo check` for compiler and build validation
- `cargo-nextest` for test execution
- separate doctests through `cargo test --doc`
- `cargo-deny` for dependency advisories, license checks, bans, and source restrictions
- GitHub Actions CI running the full verify contract
- repo-owned `.githooks/pre-commit` for local enforcement

## Commands

- install tooling: `rustup component add rustfmt clippy && cargo install cargo-nextest --locked && cargo install cargo-deny --locked`
- verify: `./scripts/verify.sh`
- format: `cargo fmt`
- format check: `cargo fmt --check`
- compiler check: `cargo check --workspace --all-targets --all-features`
- lint: `cargo clippy --workspace --all-targets --all-features -- -D warnings`
- test: `cargo nextest run --workspace --all-features`
- focused test: `cargo nextest run --workspace --all-features -- <test-name>`
- doctests: `cargo test --doc --workspace --all-features`
- dependency checks: `cargo deny check`
- install hooks: `./scripts/install-hooks.sh`
- verify hooks: `./scripts/verify-hooks.sh`

## Contract

- canonical verify command: `./scripts/verify.sh`
- CI command: `./scripts/verify.sh`
- fast verify command: `Not configured`
- watch command: `Not configured`
- hook install command: `./scripts/install-hooks.sh`
- hook health command: `./scripts/verify-hooks.sh`

## Suggested AGENTS.md commands

- Install: `rustup component add rustfmt clippy && cargo install cargo-nextest --locked && cargo install cargo-deny --locked`
- Verify: `./scripts/verify.sh`
- Fast verify: `Not configured`
- Watch: `Not configured`
- Format: `cargo fmt`
- Format check: `cargo fmt --check`
- Lint: `cargo clippy --workspace --all-targets --all-features -- -D warnings`
- Type/build check: `cargo check --workspace --all-targets --all-features`
- Test: `cargo nextest run --workspace --all-features`
- Focused test: `cargo nextest run --workspace --all-features -- <test-name>`
- Doctests: `cargo test --doc --workspace --all-features`
- Dependency checks: `cargo deny check`

## Hook activation

Use the repo-owned scripts to install and verify durable hook enforcement.

- `./scripts/install-hooks.sh` configures `core.hooksPath` to `.githooks`
- `./scripts/verify-hooks.sh` confirms that Git will execute the real `.githooks/pre-commit` file
- do not treat config files or wrapper commands as proof that hooks are active

## Style expectations

- stable toolchain with `rustfmt` and `clippy`
- keep warnings denied in Clippy-backed CI and local verification
- prefer small, explicit modules over clever abstractions
- keep doctests explicit in the verify loop when `cargo-nextest` is used
