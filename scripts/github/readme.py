import requests
import os
import re  # Import the re module for regular expressions


def get_realtime_commit_count(username, project_name, github_token=None):
    """
    Fetches the total commit count for a specific repository from the GitHub API.

    Args:
        username (str): The GitHub username (owner of the repository).
        project_name (str): The name of the repository.
        github_token (str, optional): Your GitHub Personal Access Token.
                                      Recommended for higher rate limits.

    Returns:
        int: The number of commits, or 0 if there's an error or no commits found.
    """
    base_url = "https://api.github.com"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "X-GitHub-Api-Version": "2022-11-28",  # Recommended API version header
    }
    if github_token:
        headers["Authorization"] = (
            f"token {github_token}"  # Use "Bearer" for fine-grained PATs or "token" for classic PATs
        )

    # This endpoint gets the list of commits, we only ask for one to get the 'link' header
    # which contains pagination info including the total number of pages.
    # The 'last' link in the header gives the total count if multiplied by per_page.
    commits_url = f"{base_url}/repos/{username}/{project_name}/commits?per_page=1"

    try:
        response = requests.get(commits_url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

        total_commits = 0
        if "link" in response.headers:
            link_header = response.headers["link"]
            # Regex to find the 'last' page link and extract the page number
            last_page_match = re.search(r'page=(\d+)>; rel="last"', link_header)
            if last_page_match:
                last_page_number = int(last_page_match.group(1))
                total_commits = (
                    last_page_number  # If per_page is 1, page number is the total count
                )
        elif response.json():
            # If there's no 'link' header (meaning only one page of commits),
            # and the response is not empty, it means there's at least 1 commit.
            total_commits = 1

        return total_commits

    except requests.exceptions.HTTPError as e:
        print(
            f"HTTP Error fetching commits for {project_name}: {e.response.status_code} - {e.response.json().get('message', 'Unknown error')}"
        )
        return 0
    except requests.exceptions.RequestException as e:
        print(f"Network error or other issue fetching commits for {project_name}: {e}")
        return 0
    except Exception as e:
        print(f"An unexpected error occurred for {project_name}: {e}")
        return 0


def format_projects_to_markdown(project_data, github_username, github_token=None):
    """
    Formats a list of project dictionaries into a GitHub-flavored Markdown table,
    updating the commit counts from the GitHub API.

    Args:
        project_data (list): A list of dictionaries, where each dictionary
                             contains 'project', 'url', 'language'.
                             The 'commits' field will be updated.
        github_username (str): The GitHub username (owner of these repositories).
        github_token (str, optional): Your GitHub Personal Access Token.

    Returns:
        str: A string containing the Markdown table.
    """
    if not project_data:
        return "No project data provided to format."

    headers = ["project", "language", "commits"]
    markdown_table = "| " + " | ".join(headers) + " |\n"
    markdown_table += "| " + "--- | --- | ---" + " |\n"

    for item in project_data:
        print(f"Fetching real-time commit count for {item['project']}...")
        updated_commits = get_realtime_commit_count(
            github_username, item["project"], github_token
        )

        project_link = f"[{item['project']}]({item['url']})"
        row = [
            project_link,
            str(item.get("language", "N/A")),
            str(updated_commits),  # Use updated commit count
        ]
        markdown_table += "| " + " | ".join(row) + " |\n"

    return markdown_table


# --- Your Project Data ---
# Note: The 'commits' field in this initial data will be overwritten by real-time data.
all_projects = [
    {
        "project": "algorithm-solutions",
        "url": "https://github.com/lzwjava/algorithm-solutions",
        "language": "Java",
    },
    {
        "project": "leanchat-android",
        "url": "https://github.com/lzwjava/leanchat-android",
        "language": "Java",
    },
    {
        "project": "LZAlbum",
        "url": "https://github.com/lzwjava/LZAlbum",
        "language": "Objective-C",
    },
    {
        "project": "leanchat-ios",
        "url": "https://github.com/lzwjava/leanchat-ios",
        "language": "Objective-C",
    },
    {
        "project": "lzwjava.github.io",
        "url": "https://github.com/lzwjava/lzwjava.github.io",
        "language": "Chinese & English",
    },
    {
        "project": "live-server",
        "url": "https://github.com/lzwjava/live-server",
        "language": "PHP",
    },
    {
        "project": "live-mobile-web",
        "url": "https://github.com/lzwjava/live-mobile-web",
        "language": "JavaScript & HTML",
    },
    {
        "project": "live-web",
        "url": "https://github.com/lzwjava/live-web",
        "language": "JavaScript & HTML",
    },
    {
        "project": "live-wxapp",
        "url": "https://github.com/lzwjava/live-wxapp",
        "language": "JavaScript",
    },
    {
        "project": "flower-recognition",
        "url": "https://github.com/lzwjava/flower-recognition",
        "language": "Java",
    },
    {
        "project": "code-review-server",
        "url": "https://github.com/lzwjava/code-review-server",
        "language": "PHP",
    },
    {
        "project": "code-review-web",
        "url": "https://github.com/lzwjava/code-review-web",
        "language": "JavaScript & HTML",
    },
    {
        "project": "curiosity-courses",
        "url": "https://github.com/lzwjava/curiosity-courses",
        "language": "Chinese",
    },
    {
        "project": "lvchensign",
        "url": "https://github.com/lzwjava/lvchensign",
        "language": "JavaScript",
    },
    {
        "project": "feynman-lectures-mobi",
        "url": "https://github.com/lzwjava/feynman-lectures-mobi",
        "language": "Python",
    },
    {
        "project": "Creak",
        "url": "https://github.com/lzwjava/Creak",
        "language": "Swift",
    },
    {
        "project": "Reveal-In-GitHub",
        "url": "https://github.com/lzwjava/Reveal-In-GitHub",
        "language": "Objective-C",
    },
    {
        "project": "Keynotes",
        "url": "https://github.com/lzwjava/Keynotes",
        "language": "Chinese",
    },
    {
        "project": "weimg-server",
        "url": "https://github.com/lzwjava/weimg-server",
        "language": "PHP",
    },
    {
        "project": "weimg-ios",
        "url": "https://github.com/lzwjava/weimg-ios",
        "language": "Objective-C",
    },
]

if __name__ == "__main__":
    github_username = (
        "lzwjava"  # This must be the GitHub username that owns these repos.
    )
    github_token = os.getenv("GITHUB_TOKEN")  # Get token from environment variable

    print("--- Starting to fetch real-time commit data ---")
    markdown_output = format_projects_to_markdown(
        all_projects, github_username, github_token
    )
    print("\n--- Generated Real-time GitHub Project Table ---\n")
    print(markdown_output)
