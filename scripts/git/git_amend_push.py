#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path


def run_command(
    command: list[str],
    check: bool = True,
    repo_path: Path | None = None,
) -> subprocess.CompletedProcess[str]:
    """Run a shell command inside the target repository and capture the output."""
    cwd = repo_path if repo_path is not None else Path.cwd()
    print(f"Running command: {' '.join(command)} (cwd={cwd})")
    result = subprocess.run(
        command,
        check=check,
        text=True,
        capture_output=True,
        cwd=str(cwd),
    )
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)
    return result


def stage_changes(repo_path: Path) -> None:
    """Stage all modified files."""
    run_command(["git", "add", "-A"], repo_path=repo_path)


def amend_commit(repo_path: Path) -> None:
    """Amend the last commit to include the new changes."""
    run_command(["git", "commit", "--amend", "--no-edit"], repo_path=repo_path)


def push_changes(repo_path: Path) -> None:
    """Push the amended commit to the remote repository."""
    run_command(["git", "push", "--force-with-lease"], repo_path=repo_path)


def main(argv: list[str] | None = None) -> None:
    """Automate staging, amending, and pushing changes for a given repository."""
    args = argv if argv is not None else sys.argv[1:]
    if args:
        repo_path = Path(args[0]).expanduser().resolve()
    else:
        repo_path = Path.cwd()

    if not repo_path.is_dir():
        print(f"Error: '{repo_path}' is not a valid directory.", file=sys.stderr)
        sys.exit(1)

    # Stage the changes
    stage_changes(repo_path)

    # Amend the last commit
    amend_commit(repo_path)

    # Push the changes to the remote repository
    push_changes(repo_path)


if __name__ == "__main__":
    main()
