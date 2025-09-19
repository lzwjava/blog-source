import os
import subprocess
from datetime import datetime
import yaml


def get_last_content_change_date(file_path):
    """
    Retrieves the date of the last commit that changed the content of a file,
    ignoring changes to the front matter.
    """
    try:
        # Get the commit hashes that changed the file
        commits = (
            subprocess.check_output(
                ["git", "log", "--pretty=format:%H", "--", file_path],
                text=True,
                stderr=subprocess.DEVNULL,
            )
            .strip()
            .splitlines()
        )

        if not commits:
            return None

        for commit_hash in commits:
            # Get the diff for this commit
            diff_output = subprocess.check_output(
                [
                    "git",
                    "show",
                    "--pretty=format:",
                    "--unified=0",
                    commit_hash,
                    file_path,
                ],
                text=True,
                stderr=subprocess.DEVNULL,
            )

            # Split the diff into lines and check for content changes
            diff_lines = diff_output.splitlines()
            content_change = False
            in_content = False
            for line in diff_lines:
                if line.startswith("---"):
                    in_content = not in_content
                    continue
                if in_content and (line.startswith("+") or line.startswith("-")):
                    if not line.startswith("+++") and not line.startswith("---"):
                        content_change = True
                        break
            if content_change:
                # Get the commit date
                date_str = subprocess.check_output(
                    ["git", "show", "-s", "--format=%cd", "--date=iso", commit_hash],
                    text=True,
                    stderr=subprocess.DEVNULL,
                ).strip()
                return datetime.fromisoformat(date_str)

        return None

    except subprocess.CalledProcessError:
        return None


def update_frontmatter_date(file_path):
    """
    Updates the 'updated' field in the front matter of a markdown file
    with the last content change date.
    """
    try:
        with open(file_path, "r") as f:
            content = f.read()

        parts = content.split("---", 2)
        if len(parts) < 3:
            print(f"Skipped: {file_path} (no frontmatter)")
            return

        frontmatter_str = parts[1]
        body = parts[2]

        frontmatter = yaml.safe_load(frontmatter_str)
        if not frontmatter:
            print(f"Skipped: {file_path} (empty frontmatter)")
            return

        last_change_date = get_last_content_change_date(file_path)
        if last_change_date:
            frontmatter["updated"] = last_change_date.strftime("%Y-%m-%d")
            modified_frontmatter_str = yaml.dump(frontmatter, sort_keys=False)
            modified_content = f"---\n{modified_frontmatter_str}---{body}"

            with open(file_path, "w") as f:
                f.write(modified_content)
            print(
                f"Updated date in {file_path} to {last_change_date.strftime('%Y-%m-%d')}"
            )
        else:
            print(f"No content changes found for {file_path}")

    except yaml.YAMLError as e:
        print(f"Skipped: {file_path} (YAML error: {e})")
    except Exception as e:
        print(f"Skipped: {file_path} (Error processing file: {e})")


if __name__ == "__main__":
    target_dir = "original"
    for root, _, files in os.walk(target_dir):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                update_frontmatter_date(file_path)
