import os
import sys
import pyperclip
import argparse


def append_clipboard_to_note(note_path):
    # Get clipboard content
    content = pyperclip.paste()
    if not content.strip():
        print("Clipboard is empty. Nothing to append.")
        sys.exit(1)

    # Ensure the note file exists
    if not os.path.isfile(note_path):
        print(f"File not found: {note_path}")
        sys.exit(1)

    # Append clipboard content to the note
    with open(note_path, "a", encoding="utf-8") as file:
        file.write("\n---\n" + content.strip())
    print(f"Appended clipboard content to: {note_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Append clipboard content to a note file."
    )
    parser.add_argument(
        "note_path", help="Path to the note file (e.g., ./notes/xxx.md)"
    )
    args = parser.parse_args()
    append_clipboard_to_note(args.note_path)


if __name__ == "__main__":
    main()
