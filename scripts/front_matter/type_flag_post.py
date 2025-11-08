import os
import re
import frontmatter
import datetime
import argparse


def update_front_matter(file_path):
    try:
        # Extract date from filename
        filename = os.path.basename(file_path)
        date_match = re.match(r"(\d{4}-\d{2}-\d{2})", filename)
        if not date_match:
            print(f"Could not extract date from filename: {filename}")
            return
        file_date_str = date_match.group(1)

        # Load the post using frontmatter library
        post = frontmatter.load(file_path)

        # Update the type field
        post.metadata["type"] = "post"

        # Write the updated post back to file
        frontmatter.dump(post, file_path)

        print(f"Updated front matter in {file_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")


def main():
    parser = argparse.ArgumentParser(description='Update front matter in blog post files')
    parser.add_argument('-n', type=int, help='Maximum number of files to update')
    args = parser.parse_args()

    original_dir = "original"
    posts_dir = "_posts"
    count = 0

    # Process files in original directory
    if not args.n or count < args.n:
        for filename in os.listdir(original_dir):
            if filename.endswith(".md") and (not args.n or count < args.n):
                file_path = os.path.join(original_dir, filename)
                update_front_matter(file_path)
                count += 1

    # Process files in _posts directories
    if not args.n or count < args.n:
        for lang_dir in os.listdir(posts_dir):
            lang_dir_path = os.path.join(posts_dir, lang_dir)
            if os.path.isdir(lang_dir_path):
                for filename in os.listdir(lang_dir_path):
                    if filename.endswith(".md") and (not args.n or count < args.n):
                        file_path = os.path.join(lang_dir_path, filename)
                        update_front_matter(file_path)
                        count += 1


if __name__ == "__main__":
    main()
