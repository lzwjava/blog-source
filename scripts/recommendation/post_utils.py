import os
from datetime import datetime, timedelta
import frontmatter


def get_recent_posts(posts_dir="_posts/en", years=1):
    """Filter posts from the last specified number of years."""
    post_files = [f for f in os.listdir(posts_dir) if f.endswith(".md")]
    print(f"Found {len(post_files)} post files in {posts_dir}")

    years_ago = datetime.now() - timedelta(days=365 * years)
    recent_post_files = []
    for file in post_files:
        try:
            date_str = file.split("-", 3)[:3]
            if len(date_str) == 3:
                file_date = datetime.strptime("-".join(date_str), "%Y-%m-%d")
                if file_date >= years_ago:
                    recent_post_files.append(file)
        except (ValueError, IndexError):
            print(f"Could not parse date from {file}, skipping")

    print(f"Found {len(recent_post_files)} posts from the last {years} year(s)")
    return recent_post_files


def extract_post_data(post_files, posts_dir="_posts/en"):
    """Extract title and link data from markdown files."""
    post_data = []
    for file in post_files:
        file_path = os.path.join(posts_dir, file)
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                post = frontmatter.load(f)
                title = post.get("title", file.replace(".md", ""))
            print(f"  Extracted title: {title} from {file}")
            base_name = file.split("-", 3)[-1].replace(".md", "")
            post_data.append({"title": title, "link": base_name})
        except Exception as e:
            print(f"Error processing {file}: {e}")
    post_data.sort(key=lambda x: x["title"])
    return post_data


if __name__ == "__main__":
    # Example usage
    posts = get_recent_posts(years=1)
    data = extract_post_data(posts)
    print(data)  # Output the extracted post data for verification
