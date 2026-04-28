import nox

@nox.session(reuse_venv=True)
def lint(session: nox.Session) -> None:
    session.install(".[dev]")
    session.run("ruff", "check", ".", "--fix")
    session.run("black", "--check", ".")

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
def watch(session: nox.Session) -> None:
    session.install(".[dev]")
    session.run("python", "tools/watch_verify.py")

