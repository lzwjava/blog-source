import os
import glob


def count_md_files_in_original(quiet=False):
    # Look for an 'original' directory
    original_dir = "original"

    if not os.path.exists(original_dir):
        if not quiet:
            print(f"Directory '{original_dir}' not found")
        return 0

    # Count .md files in the original directory
    md_files = glob.glob(os.path.join(original_dir, "*.md"))
    count = len(md_files)

    if not quiet:
        print(f"Found {count} markdown files in '{original_dir}' directory")
    return count


if __name__ == "__main__":
    count_md_files_in_original()
