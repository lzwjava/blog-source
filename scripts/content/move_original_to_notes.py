import sys
import subprocess
from pathlib import Path

#!/usr/bin/env python3


def move_original_to_notes(filename):
    """
    Delete file from _posts/ using delete script and move from original/ to notes/
    Also updates the front matter to set generated: true
    """
    # Define paths
    original_dir = Path("original")
    notes_dir = Path("notes")

    # Extract just the filename from the path
    file_path = Path(filename)
    base_filename = file_path.name

    # Ensure filename has .md extension for file operations
    if not base_filename.endswith(".md"):
        md_filename = base_filename + ".md"
    else:
        md_filename = base_filename

    # Use the original filename (without .md) for the delete script
    delete_filename = (
        base_filename.replace(".md", "")
        if base_filename.endswith(".md")
        else base_filename
    )
    # Remove '-en' suffix if present
    delete_filename = delete_filename.replace("-en", "")

    # Define file paths
    original_file = original_dir / md_filename
    notes_file = notes_dir / md_filename

    print(delete_filename)

    # Delete from _posts using the delete script
    try:
        result = subprocess.run(
            [
                "/opt/homebrew/bin/python3",
                "scripts/create/file.py",
                "delete",
                delete_filename,
            ],
            capture_output=True,
            text=True,
        )

        if result.returncode == 0:
            print(f"Deleted from _posts: {delete_filename}")
        else:
            print(f"Delete script output: {result.stdout}")
            if result.stderr:
                print(f"Delete script error: {result.stderr}")
    except Exception as e:
        print(f"Error running delete script: {e}")

    # Move from original to notes and update front matter
    if original_file.exists():
        # Create notes directory if it doesn't exist
        notes_dir.mkdir(exist_ok=True)

        # Read the file content
        with open(original_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Check if front matter exists
        if not content.lstrip().startswith("---"):
            raise Exception(f"No front matter found in markdown file: {original_file}")

        # Parse front matter manually
        parts = content.split("---", 2)
        if len(parts) < 3:
            raise Exception(f"Invalid front matter format in: {original_file}")

        front_matter_content = parts[1].strip()
        content_without_front_matter = parts[2]

        # Remove any existing 'generated' field
        front_matter_lines = front_matter_content.split("\n")
        front_matter_lines = [
            line for line in front_matter_lines if not line.startswith("generated:")
        ]
        front_matter_content = "\n".join(front_matter_lines)

        # Add generated: true to front matter
        if front_matter_content:
            front_matter_content += "\ngenerated: true"
        else:
            front_matter_content = "generated: true"

        # Reconstruct the file content
        new_content = f"---\n{front_matter_content}\n---{content_without_front_matter}"

        # Write to the new location
        with open(notes_file, "w", encoding="utf-8") as f:
            f.write(new_content)

        # Remove the original file
        original_file.unlink()

        print(f"Moved and updated: {original_file} -> {notes_file}")
    else:
        print(f"File not found in original: {original_file}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python move_original_to_notes.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    move_original_to_notes(filename)
