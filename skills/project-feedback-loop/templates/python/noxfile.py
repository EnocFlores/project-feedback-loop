import subprocess
from pathlib import Path

import nox

HOOK_TYPES = ("pre-commit", "pre-push")


def _run_git(*args: str) -> str:
    completed = subprocess.run(
        ["git", *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout.strip()


def _get_repo_root() -> Path:
    return Path(_run_git("rev-parse", "--show-toplevel"))


def _get_git_dir(repo_root: Path) -> Path:
    git_dir = Path(_run_git("rev-parse", "--git-dir"))
    if git_dir.is_absolute():
        return git_dir
    return repo_root / git_dir


def _get_active_hooks_path(repo_root: Path, git_dir: Path) -> tuple[Path, str | None]:
    core_hooks_path = subprocess.run(
        ["git", "config", "--get", "core.hooksPath"],
        check=False,
        capture_output=True,
        text=True,
    ).stdout.strip()

    if not core_hooks_path:
        return git_dir / "hooks", None

    configured_path = Path(core_hooks_path)
    if configured_path.is_absolute():
        return configured_path, core_hooks_path
    return repo_root / configured_path, core_hooks_path


def _verify_hooks_active() -> tuple[Path, str | None]:
    repo_root = _get_repo_root()
    git_dir = _get_git_dir(repo_root)
    hooks_path, core_hooks_path = _get_active_hooks_path(repo_root, git_dir)

    missing_hooks = [
        hook_name for hook_name in HOOK_TYPES if not (hooks_path / hook_name).is_file()
    ]
    if missing_hooks:
        missing_names = ", ".join(missing_hooks)
        configured = core_hooks_path or ".git/hooks"
        raise RuntimeError(
            "Git hooks are not fully active. "
            f"Missing: {missing_names}. "
            f"Active hooks path: {hooks_path}. "
            f"Configured core.hooksPath: {configured}. "
            "Run `nox -s install_hooks` to install durable hook files."
        )

    return hooks_path, core_hooks_path


@nox.session(reuse_venv=True)
def lint(session: nox.Session) -> None:
    session.install(".[dev]")
    session.run("ruff", "check", ".")
    session.run("black", "--check", ".")


@nox.session(reuse_venv=True)
def format(session: nox.Session) -> None:
    session.install(".[dev]")
    session.run("ruff", "check", ".", "--fix")
    session.run("black", ".")


@nox.session(reuse_venv=True)
def typecheck(session: nox.Session) -> None:
    session.install(".[dev]")
    session.run("mypy", ".")


@nox.session(reuse_venv=True)
def tests(session: nox.Session) -> None:
    session.install(".[dev]")
    session.run("pytest", "-q")


@nox.session(reuse_venv=True)
def verify(session: nox.Session) -> None:
    session.notify("lint")
    session.notify("typecheck")
    session.notify("tests")


@nox.session(reuse_venv=True)
def install_hooks(session: nox.Session) -> None:
    session.install(".[dev]")
    session.run("pre-commit", "install")
    session.run("pre-commit", "install", "--hook-type", "pre-push")
    session.notify("verify_hooks")


@nox.session(reuse_venv=True)
def verify_hooks(session: nox.Session) -> None:
    hooks_path, core_hooks_path = _verify_hooks_active()
    configured = core_hooks_path or ".git/hooks"
    session.log(f"Git hooks active at {hooks_path} (core.hooksPath={configured})")


@nox.session(reuse_venv=True)
def watch(session: nox.Session) -> None:
    session.install(".[dev]")
    session.run("python", "tools/watch_verify.py")
