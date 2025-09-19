#!/usr/bin/env python3

import os
import shutil
from pathlib import Path


def main():
    # Get home directory and source config path
    home = str(Path.home())
    source = os.path.join(home, ".ssh", "config")

    # Get script directory for destination
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dest = os.path.join(script_dir, "config", "config")

    # Copy the file
    if os.path.exists(source):
        shutil.copy2(source, dest)
        print(f"SSH config copied from {source} to {dest}")
    else:
        print(f"Source SSH config not found at {source}")


if __name__ == "__main__":
    main()
