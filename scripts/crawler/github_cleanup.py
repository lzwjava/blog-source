import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager


def main():
    # Parse the username from command-line arguments
    parser = argparse.ArgumentParser(description="GitHub repository cleanup script")
    parser.add_argument("username", help="GitHub username")
    args = parser.parse_args()
    username = args.username

    # Set up Selenium with headless Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run without opening a browser window
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    try:
        # Navigate to the user's public repositories page
        driver.get(f"https://github.com/{username}?tab=repositories")
        fork_repos = []

        # Scrape all fork repositories, handling pagination
        while True:
            # Wait for the repository list to load
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "user-repositories-list"))
            )
            # Find all repository entries
            repos = driver.find_elements(
                By.CSS_SELECTOR, "#user-repositories-list ul li"
            )
            for repo in repos:
                try:
                    # Check if the repository is a fork
                    forked_from = repo.find_element(By.CSS_SELECTOR, "p.mb-1")
                    if "Forked from" in forked_from.text:
                        # Extract the repository path (e.g., username/repo-name)
                        repo_link = repo.find_element(By.CSS_SELECTOR, "h3 a")
                        href = repo_link.get_attribute("href")
                        repo_path = href.replace("https://github.com/", "")
                        fork_repos.append(repo_path)
                except NoSuchElementException:
                    continue  # Skip if not a fork

            # Check for a 'Next' page button
            try:
                next_button = driver.find_element(
                    By.CSS_SELECTOR, ".paginate-container a[rel='next']"
                )
                next_button.click()
                # Wait for the page to refresh
                WebDriverWait(driver, 10).until(EC.staleness_of(repos[0]))
            except (NoSuchElementException, TimeoutException):
                break  # No more pages to scrape

        # Analyze each fork for user commits
        delete_repos = []
        for repo_path in fork_repos:
            # Visit the commits page filtered by the user's contributions
            commits_url = f"https://github.com/{repo_path}/commits?author={username}"
            driver.get(commits_url)
            try:
                # Wait for the content to load
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, ".repository-content")
                    )
                )
                # Check if there are no commits by the user
                no_commits = driver.find_element(By.CSS_SELECTOR, ".blankslate h3")
                if no_commits.text.strip() == "No commits found":
                    delete_repos.append(repo_path)
            except (NoSuchElementException, TimeoutException):
                pass  # Commits exist or page load failed, skip deletion suggestion

        # Display results
        print(f"Found {len(fork_repos)} fork repositories.")
        if delete_repos:
            print("Suggested for deletion:")
            for repo in delete_repos:
                print(f"- {repo}")
        else:
            print("No fork repositories found that can be deleted.")

    finally:
        # Clean up by closing the browser
        driver.quit()


if __name__ == "__main__":
    main()
