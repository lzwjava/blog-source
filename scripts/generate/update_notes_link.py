import subprocess
from generate_notes_link import generate_notes_links


def get_changed_files():
    try:
        # Get the list of files changed in the last commit
        result = subprocess.run(['git', 'diff', '--name-only', 'HEAD~1', 'HEAD'], capture_output=True, text=True, check=True)
        changed_files = result.stdout.strip().split('\n')
        return [f for f in changed_files if f.startswith('notes/') and f.endswith('.md')]
    except subprocess.CalledProcessError as e:
        print(f"Error getting changed files: {e}")
        return []

def main():
    changed_files = get_changed_files()
    if changed_files:
        print("Notes files changed, regenerating notes links.")
        generate_notes_links()
    else:
        print("No notes files changed, skipping notes link regeneration.")

if __name__ == "__main__":
    main()
