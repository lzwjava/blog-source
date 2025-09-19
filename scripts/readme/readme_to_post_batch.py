import os
import subprocess
from datetime import datetime
import argparse
import re


def get_first_commit_date(repo_path):
    try:
        result = subprocess.run(
            ["git", "log", "--reverse"],
            cwd=repo_path,
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            print(
                f"Git command failed with return code {result.returncode} for {repo_path}"
            )
            return None
        date_str = result.stdout.strip()
        match = re.search(
            r"Date:\s*(\w{3}\s+\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}\s+\d{4}\s+[\+\-]\d{4})",
            date_str,
        )
        if match:
            date_str = match.group(1)
            date_obj = datetime.strptime(date_str, "%a %b %d %H:%M:%S %Y %z")
            return date_obj.strftime("%Y-%m-%d")
        else:
            print(f"Could not parse date from git output: {date_str} for {repo_path}")
            return None
    except Exception as e:
        print(f"Error getting commit date for {repo_path}: {e}")
        return None


projects = [
    ("algorithm-solutions", "algorithm-solutions-en.md"),
    ("LZAlbum", "lzalbum-en.md"),
    ("lzwjava.github.io", "blog-en.md"),
    ("live-mobile-web", "live-mobile-web-en.md"),
    ("live-web", "live-web-en.md"),
    ("live-wxapp", "live-wxapp-en.md"),
    ("flower-recognition", "flower-recognition-en.md"),
    ("code-review-server", "code-review-server-en.md"),
    ("code-review-web", "code-review-web-en.md"),
    ("curiosity-courses", "curiosity-courses-en.md"),
    ("lvchensign", "lvchensign-en.md"),
    ("feynman-lectures-mobi", "feynman-lectures-mobi-en.md"),
    ("Creak", "creak-en.md"),
    ("Reveal-In-GitHub", "reveal-in-github-en.md"),
    ("Keynotes", "keynotes-en.md"),
    ("weimg-server", "weimg-server-en.md"),
    ("weimg-ios", "weimg-ios-en.md"),
    ("leachat-android", "leachat-android-en.md"),
    ("leanchat-ios", "leanchat-ios-en.md"),
    ("live-server", "live-server-en.md"),
    ("LearnJapanese", "learn-japanese-en.md"),
    ("TabsKiller", "tabskiller-en.md"),
]


def main():
    parser = argparse.ArgumentParser(description="Create posts from README files.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Perform a dry run without creating posts.",
    )
    args = parser.parse_args()

    for project, target_post_suffix in projects:
        project_path = os.path.expanduser(f"~/projects/{project}")
        if os.path.exists(project_path):
            first_commit_date = get_first_commit_date(project_path)
            if first_commit_date:
                target_post = f"{first_commit_date}-{target_post_suffix}"
                command = [
                    "python3",
                    "scripts/readme_to_post.py",
                    project_path,
                    target_post,
                ]
                if args.dry_run:
                    print(f"[Dry Run] Would run: {' '.join(command)}")
                else:
                    subprocess.run(command, check=False)
            else:
                print(f"Could not get first commit date for {project}")
        else:
            print(f"Project {project} not found in ~/projects")


if __name__ == "__main__":
    main()
