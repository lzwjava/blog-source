#!/usr/bin/env python3
"""Run the Jekyll build with a fixed output destination."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DESTINATION = ROOT / "destination" / "_site"


def parse_args(argv: list[str]) -> tuple[str, list[str]]:
    """Return the destination path and any extra Jekyll CLI arguments."""
    parser = argparse.ArgumentParser(description="Run the Jekyll build command")
    parser.add_argument(
        "-d",
        "--destination",
        default=str(DEFAULT_DESTINATION),
        help="Destination directory for the generated site",
    )
    args, extra_args = parser.parse_known_args(argv)
    return args.destination, extra_args


def run_jekyll(destination: str, extra_args: list[str]) -> int:
    dest_path = Path(destination)
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    if dest_path.exists():
        shutil.rmtree(dest_path)

    command = [
        "jekyll",
        "build",
        "--destination",
        destination,
        *extra_args,
    ]
    completed = subprocess.run(command, check=False)
    return completed.returncode


def main(argv: list[str]) -> int:
    destination, extra_args = parse_args(argv)
    return run_jekyll(destination, extra_args)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
