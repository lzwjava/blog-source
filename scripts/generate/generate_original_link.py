import os
import frontmatter  # You need to install the 'python-frontmatter' package
from datetime import datetime

# Path to the original directory
original_dir = "original"

# List all .md files in the original directory
original_files = [f for f in os.listdir(original_dir) if f.endswith(".md")]

# Initialize a list to store links with date
links_with_date = []

# Parse each markdown file to extract the title and generate the links
for file in original_files:
    # Load the markdown file content and front matter
    with open(os.path.join(original_dir, file), "r", encoding="utf-8") as f:
        post = frontmatter.load(f)
        title = post.get(
            "title", file.replace(".md", "")
        )  # Default to filename if no title is found

    # Generate the markdown link with the title and add an asterisk (*) in front
    link = f"* [{title}](/original/{file.replace('.md', '')})"

    # Extract date from filename
    try:
        date_str = file.split("-")[0:3]
        date_obj = datetime.strptime("-".join(date_str), "%Y-%m-%d")
    except (ValueError, IndexError):
        raise Exception(f"Could not parse date from filename: {file}")

    links_with_date.append((date_obj, title, link))

# Sort links by date desc
links_with_date.sort(key=lambda item: item[0], reverse=True)
sorted_links = [link for _, _, link in links_with_date]


file_path = os.path.join("original", "2025-01-11-original-en.md")
content = f"""---
audio: false
lang: en
layout: post
title: Original Posts
translated: false
---

These are my original blog posts.

{chr(10).join(sorted_links)}
"""

# Update the markdown file with the generated content
with open(file_path, "w", encoding="utf-8") as md_file:
    md_file.write(content)

print(f"Updated {file_path}")
