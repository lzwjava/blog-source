#!/usr/bin/env python3
import subprocess
import sys


def run_command(command: list[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    """Run a shell command and capture the output."""
    print(f"Running command: {' '.join(command)}")
    result = subprocess.run(command, check=check, text=True, capture_output=True)
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)
    return result


def stage_changes() -> None:
    """Stage all modified files."""
    run_command(["git", "add", "-A"])


def amend_commit() -> None:
    """Amend the last commit to include the new changes."""
    run_command(["git", "commit", "--amend", "--no-edit"])


def push_changes() -> None:
    """Push the amended commit to the remote repository."""
    run_command(["git", "push", "--force-with-lease"])


def main() -> None:
    """Main function to automate the process of staging, amending, and pushing changes."""
    # Stage the changes
    stage_changes()

    # Amend the last commit
    amend_commit()

    # Push the changes to the remote repository
    push_changes()


if __name__ == "__main__":
    main()
