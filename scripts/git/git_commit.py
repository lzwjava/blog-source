#!/usr/bin/env python3
"""Find the most recent commit relative to a date offset."""

from __future__ import annotations

import argparse
import datetime as dt
import subprocess
import sys
from typing import Optional


def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Find the latest commit on the current branch that is at least N days old."
        )
    )
    parser.add_argument(
        "--days",
        type=int,
        default=365,
        help="Number of days to look back (default: 365).",
    )
    parser.add_argument(
        "--ref",
        default="HEAD",
        help="Git ref to search backwards from (default: HEAD).",
    )
    return parser.parse_args(argv)


def format_before_date(days: int, now: Optional[dt.datetime] = None) -> str:
    if days < 0:
        raise ValueError("days must be non-negative")
    now_local = (now or dt.datetime.now()).astimezone()
    target = now_local - dt.timedelta(days=days)
    # Match git's default date parsing: YYYY-MM-DD HH:MM:SS +ZZZZ
    return target.strftime("%Y-%m-%d %H:%M:%S %z")


def find_commit(before: str, ref: str) -> str:
    try:
        completed = subprocess.run(
            ["git", "rev-list", "-1", f"--before={before}", ref],
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as exc:
        stderr = exc.stderr.strip()
        message = stderr or "git rev-list failed"
        raise RuntimeError(message) from exc
    commit = completed.stdout.strip()
    if not commit:
        raise RuntimeError("No commit found for the provided constraints")
    return commit


def main(argv: Optional[list[str]] = None) -> int:
    args = parse_args(argv)
    try:
        before = format_before_date(args.days)
        commit = find_commit(before, args.ref)
    except (ValueError, RuntimeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    print(commit)
    return 0


if __name__ == "__main__":
    sys.exit(main())
