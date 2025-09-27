import sys
import os
import random
import subprocess
import argparse
from datetime import datetime, timedelta
from typing import Optional
from gpa import gpa
from create_note_from_clipboard import create_note

# Ensure repository root is on sys.path for importing scripts.* packages
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from scripts.llm.openrouter_client import MODEL_MAPPING
from scripts.content.fix_mathjax import fix_mathjax_in_file

def git_pull_rebase() -> None:
    """Run 'git pull --rebase' at the repository root.

    This is helpful when creating notes from multiple machines to avoid conflicts.
    If not in a git repo or git is unavailable, fail gracefully.
    """
    try:
        toplevel = subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"], text=True
        ).strip()
        print(f"[info] Running 'git pull --rebase' in {toplevel}...")
        # Do not raise on non-zero; we only warn to avoid blocking note creation
        subprocess.run(["git", "-C", toplevel, "pull", "--rebase"], check=False)
    except Exception as e:
        print(f"[warn] Skipping git pull --rebase: {e}")


def _repo_root() -> str:
    """Return the repository root derived from this file's location."""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def open_note_in_browser(note_path: Optional[str]) -> None:
    """Open the GitHub page for the created note in the system default browser."""
    if not note_path:
        return

    abs_note_path = os.path.abspath(note_path)
    root = _repo_root()

    try:
        rel_path = os.path.relpath(abs_note_path, root)
    except ValueError as exc:
        print(f"[warn] Unable to compute relative path for {abs_note_path}: {exc}")
        return

    github_url = "https://github.com/lzwjava/blog-source/blob/main/" + rel_path.replace(os.sep, "/")

    if sys.platform.startswith("darwin"):
        command = ["open", github_url]
    elif sys.platform.startswith("linux"):
        command = ["xdg-open", github_url]
    else:
        try:
            import webbrowser

            if not webbrowser.open(github_url):
                print(f"[warn] webbrowser module could not launch {github_url}")
        except Exception as exc:  # pragma: no cover - defensive fallback
            print(f"[warn] Unable to launch browser for {github_url}: {exc}")
        return

    try:
        subprocess.run(command, check=False)
    except FileNotFoundError:
        print(f"[warn] Launch command not found when opening {github_url}")
    except Exception as exc:  # pragma: no cover - defensive fallback
        print(f"[warn] Failed to open browser for {github_url}: {exc}")

def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description="Create a note; first positional arg is the model key."
    )
    parser.add_argument(
        "model",
        choices=sorted(MODEL_MAPPING.keys()),
        help=(
            "Model key to annotate in frontmatter; choices shown above."
        ),
    )
    parser.add_argument(
        "--random",
        action="store_true",
        help="Use a random date within last 180 days",
    )
    parser.add_argument(
        "--math",
        action="store_true",
        help="Fix MathJax delimiters in the created file before git add",
    )
    parser.add_argument(
        "--only-create",
        action="store_true",
        help="Only create the note; skip calling gpa to submit",
    )
    return parser.parse_args()

def generate_random_date():
    """Generate a random date within the last 180 days"""
    end_date = datetime.now()
    start_date = end_date - timedelta(days=180)
    
    random_days = random.randint(0, 180)
    random_date = start_date + timedelta(days=random_days)
    
    return random_date.strftime('%Y-%m-%d')

if __name__ == "__main__":
    # Ensure we are up to date to avoid conflicts across machines
    git_pull_rebase()

    args = parse_args()
    random_date = generate_random_date() if args.random else None

    created_path = create_note(date=random_date, note_model_key=args.model)

    # Optionally fix MathJax before invoking GPT-assisted git add/commit
    if args.math and created_path and os.path.exists(created_path):
        try:
            fix_mathjax_in_file(created_path)
        except Exception as e:
            print(f"[warn] MathJax fix failed for {created_path}: {e}")

    # Call gpa function unless only creating the note was requested
    if not args.only_create:
        try:
            gpa()
            open_note_in_browser(created_path)
        except Exception as e:
            print(f"[warn] gpa failed: {e}, not opening browser")
