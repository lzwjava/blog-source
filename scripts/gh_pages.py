#!/usr/bin/env python3
"""Local reproduction of the GitHub Pages workflow."""

from __future__ import annotations

import argparse
import os
import re
import shlex
import shutil
import subprocess
import sys
from glob import glob
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parents[1]
NOTES_SENTINEL = "Updated original/2025-01-11-notes-en.md"

if sys.platform == "darwin":
    python_path = Path("/opt/homebrew/bin/python3")
    PYTHON = str(python_path if python_path.exists() else Path(sys.executable))
else:
    discovered = shutil.which("python") or shutil.which("python3")
    PYTHON = discovered or sys.executable


def run_command(
    command: Sequence[str], *, capture_output: bool = False, check: bool = True
) -> subprocess.CompletedProcess[str]:
    """Run a command from the repository root and stream the output."""
    cmd_display = " ".join(shlex.quote(str(part)) for part in command)
    print(f"$ {cmd_display}")
    result = subprocess.run(
        list(command),
        cwd=ROOT,
        check=check,
        text=True,
        capture_output=capture_output,
    )
    if capture_output:
        if result.stdout:
            print(result.stdout, end="")
        if result.stderr:
            print(result.stderr, end="", file=sys.stderr)
    return result


def ensure_git_identity() -> None:
    """Configure git user identity to mirror the CI workflow."""
    run_command(["git", "config", "user.name", "github-actions[bot]"])
    run_command(
        ["git", "config", "user.email", "github-actions[bot]@users.noreply.github.com"]
    )


def update_notes_links() -> bool:
    """Update cross-language note links and report whether changes were made."""
    result = run_command(
        [PYTHON, "scripts/generate/update_notes_link.py"],
        capture_output=True,
    )
    output = result.stdout or ""
    updated = NOTES_SENTINEL in output
    if updated:
        print("Detected notes link updates.")
    else:
        print("No notes link changes detected.")
    return updated


def stage_paths(patterns: Sequence[str]) -> None:
    """Add matching files to the git index."""
    staged: list[str] = []
    for pattern in patterns:
        matches = glob(str(ROOT / pattern), recursive=True)
        if not matches:
            candidate = ROOT / pattern
            if candidate.exists():
                matches = [str(candidate)]
            else:
                continue
        for match in matches:
            rel_path = os.path.relpath(match, ROOT)
            if rel_path not in staged:
                staged.append(rel_path)
    if staged:
        run_command(["git", "add", *staged])


def commit_changes(message: str) -> bool:
    """Commit staged changes when present."""
    diff_result = run_command(["git", "diff", "--cached", "--quiet"], check=False)
    if diff_result.returncode == 0:
        return False
    run_command(["git", "commit", "-m", message])
    return True


def push_with_rebase() -> None:
    """Push changes, rebasing if the first attempt fails."""
    try:
        run_command(["git", "push"])
    except subprocess.CalledProcessError:
        print("git push failed, attempting rebase before retry.")
        run_command(["git", "pull", "--rebase"])
        run_command(["git", "push"])


def commit_notes_link_changes(auto_commit: bool, push: bool) -> None:
    """Stage and optionally commit note link changes."""
    if not auto_commit:
        print("Auto commit disabled; skipping notes link commit.")
        return
    ensure_git_identity()
    stage_paths([
        "original/2025-01-11-notes-en.md",
        "_posts/en/*.md",
    ])
    if not commit_changes("chore(notes): Update notes links"):
        print("No staged notes link changes; nothing to commit.")
        return
    if push:
        push_with_rebase()


def parse_total_posts(output: str) -> int | None:
    """Extract the number of posts reported by the dry-run command."""
    match = re.search(r"Total Markdown files to process:\s*(\d+)", output)
    return int(match.group(1)) if match else None


def update_language_files(auto_commit: bool, push: bool) -> None:
    """Run the translation updater with batching logic from CI."""
    dry_run = run_command(
        [PYTHON, "scripts/translation/update_lang.py", "--commits", "1000", "--dry_run"],
        capture_output=True,
    )
    total_posts = parse_total_posts(dry_run.stdout or "")
    if total_posts is None:
        print("Unable to determine total posts from translation dry run.", file=sys.stderr)
        return
    if total_posts == 0:
        print("No language files to update.")
        return

    batches = 2 + total_posts // 9 + (1 if total_posts % 9 else 0)
    print(f"Processing language files in {batches} batch(es).")

    if auto_commit:
        ensure_git_identity()

    for batch in range(1, batches + 1):
        print(f"Running language update batch {batch}/{batches}.")
        run_command(
            [
                PYTHON,
                "scripts/translation/update_lang.py",
                "--max_files",
                "9",
                "--model",
                "gemini-flash",
                "--commits",
                "1000",
            ]
        )
        if not auto_commit:
            print("Auto commit disabled; review language updates manually.")
            continue
        stage_paths(["_posts/**/*.md"])
        if not commit_changes("chore(lang): Update language files"):
            print("No staged language file changes; nothing to commit.")
            continue
        if push:
            push_with_rebase()


def run_unit_tests() -> None:
    """Execute the workflow-specific unit tests."""
    run_command([PYTHON, "-m", "unittest", "discover", "-s", "tests/workflow"])


def update_release_hash() -> None:
    """Update the release hash metadata."""
    run_command([PYTHON, "scripts/release/update_release.py"])


def build_site() -> None:
    """Build the Jekyll site locally."""
    run_command(["bundle", "exec", "jekyll", "build"])


def send_telegram_message() -> None:
    """Trigger the Telegram notification job."""
    run_command([PYTHON, "scripts/bot/telegram_bot.py", "--job", "send_message"])


def parse_args() -> argparse.Namespace:
    """Collect CLI options for the local pipeline."""
    parser = argparse.ArgumentParser(
        description="Run the GitHub Pages workflow locally.",
    )
    parser.add_argument(
        "--auto-commit",
        action="store_true",
        help="Allow the script to create commits like the CI workflow.",
    )
    parser.add_argument(
        "--push",
        action="store_true",
        help="Push commits to the remote when auto-commit is enabled.",
    )
    parser.add_argument(
        "--skip-tests",
        action="store_true",
        help="Skip running the workflow unit test suite.",
    )
    parser.add_argument(
        "--skip-release",
        action="store_true",
        help="Skip updating the release hash metadata.",
    )
    parser.add_argument(
        "--skip-build",
        action="store_true",
        help="Skip the Jekyll build step.",
    )
    parser.add_argument(
        "--send-telegram",
        action="store_true",
        help="Send the Telegram notification at the end of the pipeline.",
    )
    args = parser.parse_args()
    if args.push and not args.auto_commit:
        parser.error("--push requires --auto-commit")
    return args


def main() -> None:
    args = parse_args()

    notes_updated = update_notes_links()
    if notes_updated:
        commit_notes_link_changes(args.auto_commit, args.push)

    update_language_files(args.auto_commit, args.push)

    if args.skip_tests:
        print("Skipping unit tests as requested.")
    else:
        run_unit_tests()

    if args.skip_release:
        print("Skipping release hash update as requested.")
    else:
        update_release_hash()

    if args.skip_build:
        print("Skipping Jekyll build as requested.")
    else:
        build_site()

    if args.send_telegram:
        send_telegram_message()
    else:
        print("Skipping Telegram notification.")


if __name__ == "__main__":
    main()
