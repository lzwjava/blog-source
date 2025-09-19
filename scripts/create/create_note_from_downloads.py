import os
import scripts.create.create_note_from_clipboard as cn
import pyperclip


def get_most_recent_file(dirpath):
    files = [
        os.path.join(dirpath, f)
        for f in os.listdir(dirpath)
        if os.path.isfile(os.path.join(dirpath, f))
    ]
    if not files:
        return None
    most_recent_file = max(files, key=os.path.getmtime)
    return most_recent_file


def copy_file_to_clipboard(filepath):
    try:
        with open(filepath, "r") as f:
            content = f.read()
        pyperclip.copy(content)
        print(f"Copied content of {filepath} to clipboard using pyperclip.")
        return True
    except Exception as e:
        print(f"Error copying {filepath} to clipboard: {e}")
        return False


def create_note():
    try:
        cn.create_note()
    except ImportError:
        print(
            "create_note module not found.  Make sure it's installed or in the PYTHONPATH."
        )
    except AttributeError:
        print("create_note function not found in create_note module.")
    except Exception as e:
        print(f"An error occurred while calling create_note: {e}")


def main():
    downloads_dir = os.path.expanduser("~/Downloads")
    most_recent_file = get_most_recent_file(downloads_dir)

    if most_recent_file:
        if most_recent_file.lower().endswith((".md", ".markdown")):
            if copy_file_to_clipboard(most_recent_file):
                create_note()
        else:
            print("Most recent file is not a markdown file.")
    else:
        print("No files found in Downloads directory.")


if __name__ == "__main__":
    main()
