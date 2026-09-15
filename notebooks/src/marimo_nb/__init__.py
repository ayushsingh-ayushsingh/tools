"""marimo-nb: launcher for the bundled marimo notebooks."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

__version__ = "0.1.0"
__all__ = ["main", "__version__", "find_notebook", "discover_notebooks", "NOTEBOOKS"]


def _project_root() -> Path:
    """Project root: parent of the ``src/`` directory holding this package."""
    return Path(__file__).resolve().parent.parent.parent


def _notebooks_dir() -> Path:
    """Directory holding notebook sources (``notebooks/src/*.py``)."""
    return _project_root() / "src"


def discover_notebooks() -> tuple[str, ...]:
    """Find all notebook sources, sorted by file name.

    Files starting with an underscore are ignored so helpers and
    partials are never treated as standalone notebooks.
    """
    directory = _notebooks_dir()
    if not directory.is_dir():
        return ()
    return tuple(
        sorted(
            entry.name
            for entry in directory.iterdir()
            if entry.is_file()
            and entry.suffix == ".py"
            and not entry.name.startswith("_")
        )
    )


NOTEBOOKS: tuple[str, ...] = discover_notebooks()


def _default_notebook() -> str | None:
    return NOTEBOOKS[0] if NOTEBOOKS else None


def find_notebook(name: str | None = None) -> Path | None:
    """Locate a bundled notebook, checking dev layout, cwd, and package data."""
    resolved = name or _default_notebook()
    if resolved is None:
        return None
    candidate = Path(resolved)
    if candidate.is_file():
        return candidate.resolve()
    for base in (Path.cwd(), _project_root() / "src", Path(__file__).resolve().parent):
        hit = base / Path(resolved).name
        if hit.is_file():
            return hit.resolve()
    return None


def _marimo_cmd() -> list[str]:
    exe = shutil.which("marimo")
    if exe:
        return [exe]
    return [sys.executable, "-m", "marimo"]


def _usage() -> str:
    return (
        "Usage: marimo-nb [notebook] [--edit] [--port PORT] [--host HOST] [--list] [--help]\n"
        "\n"
        "Launch a bundled marimo notebook (default: first file in notebooks/src/).\n"
        "Runs `marimo run` (app mode); pass --edit for `marimo edit`.\n"
        "Unknown arguments are forwarded to the marimo CLI."
    )


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)

    if "--help" in args or "-h" in args:
        print(_usage())
        return 0
    if "--list" in args:
        for notebook in NOTEBOOKS:
            found = find_notebook(notebook)
            print(f"{notebook} {'-> ' + str(found) if found else '(not found)'}")
        return 0

    edit = False
    if "--edit" in args:
        edit = True
        args.remove("--edit")

    name = _default_notebook()
    forwarded: list[str] = []
    for arg in args:
        if not arg.startswith("-") and Path(arg).suffix == ".py" and name == _default_notebook():
            name = arg
        else:
            forwarded.append(arg)

    notebook = find_notebook(name)
    if notebook is None:
        print(f"error: notebook not found: {name}", file=sys.stderr)
        return 1

    env = os.environ.copy()
    cmd = _marimo_cmd() + (["edit"] if edit else ["run"]) + [str(notebook)] + forwarded
    try:
        completed = subprocess.run(cmd, env=env)
    except FileNotFoundError:
        print("error: marimo executable not found", file=sys.stderr)
        return 1
    return completed.returncode
