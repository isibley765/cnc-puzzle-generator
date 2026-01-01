from pathlib import Path
import os

# Repo root (two levels up from this file: repo/src/settings.py -> repo)
REPO_ROOT = Path(__file__).resolve().parents[1]

def get_repo_root() -> Path:
    """Return the repository root as a Path."""
    return REPO_ROOT

def set_cwd_root() -> None:
    """Set the current process CWD to the repository root.

    Use this in small runner scripts (like `scratchpad.py`) when you want
    relative file paths to resolve from the project root.
    """
    os.chdir(str(REPO_ROOT))

def set_cwd(path) -> None:
    """Set CWD to an explicit path (str or Path)."""
    os.chdir(str(Path(path)))
