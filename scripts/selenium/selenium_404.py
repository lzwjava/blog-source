import argparse
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
import requests
import sys

parser = argparse.ArgumentParser(description="Crawl a website and find 404 links.")
parser.add_argument(
    "--max-check-links",
    type=int,
    default=None,
    help="Maximum number of links to check before exiting early.",
)
args = parser.parse_args()

service = Service(executable_path="/home/lzw/bin/geckodriver")
driver = webdriver.Firefox(service=service)

blog_url = "http://localhost:4000"
domain = urlparse(blog_url).netloc

visited_urls = set()
broken_links = []
checked_links = 0


def is_same_domain(url, base_domain):
    try:
        parsed_url = urlparse(url)
        return parsed_url.netloc == base_domain
    except:
        return False


def check_link_status(url):
    if url == "http://localhost:4000/error-en":
        return True
    try:
        response = requests.head(url, timeout=5, allow_redirects=True)
        if response.status_code == 404:
            return True
        return False
    except requests.RequestException:
        return False


def crawl(url):
    global checked_links
    if args.max_check_links is not None and checked_links >= args.max_check_links:
        print(f"Reached max checked links: {args.max_check_links}")
        sys.exit(0)
    if url in visited_urls:
        return
    visited_urls.add(url)
    checked_links += 1
    if check_link_status(url):
        broken_links.append(url)
        print(f"Broken link found: {url}")
        return
    try:
        driver.get(url)
        links = driver.find_elements(By.TAG_NAME, "a")
        hrefs = [
            link.get_attribute("href") for link in links if link.get_attribute("href")
        ]
        unique_hrefs = set(hrefs)
        for href in unique_hrefs:
            if href and is_same_domain(href, domain) and href not in visited_urls:
                crawl(href)
    except Exception as e:
        print(f"Error crawling {url}: {e}")


try:
    crawl(blog_url)
    if broken_links:
        print("\nSummary of 404 links:")
        for link in broken_links:
            print(link)
    else:
        print("No 404 links found.")
except SystemExit:
    if broken_links:
        print("\nSummary of 404 links:")
        for link in broken_links:
            print(link)
    else:
        print("No 404 links found.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()
