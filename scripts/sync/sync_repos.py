import os
import subprocess


def sync_repos():
    # List of directories to sync
    dirs = ["/Users/lzwjava/projects/lzwjava.github.io", "/Users/lzwjava/projects/logs"]

    for dir_path in dirs:
        try:
            # Change to the directory
            os.chdir(dir_path)
            print(f"Syncing repository in {dir_path}")

            # Execute git pull --rebase
            result = subprocess.run(
                ["git", "pull", "--rebase"], capture_output=True, text=True
            )

            # Print the output
            print(result.stdout)
            if result.stderr:
                print("Error:", result.stderr)

        except Exception as e:
            print(f"Failed to sync {dir_path}: {str(e)}")


if __name__ == "__main__":
    sync_repos()
