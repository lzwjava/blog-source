import os
import re
import frontmatter
import datetime
import argparse


def update_front_matter(file_path, post_type="post"):
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
        post.metadata["type"] = post_type

        # Write the updated post back to file
        frontmatter.dump(post, file_path)

        print(f"Updated front matter in {file_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")


def main():
    parser = argparse.ArgumentParser(description='Update front matter in blog notes files')
    parser.add_argument('-n', type=int, help='Maximum number of files to update')
    parser.add_argument('--type', default='note', help='Type value to set in front matter (default: note)')
    args = parser.parse_args()

    notes_dir = "notes"
    notes_output_dir = "_notes"
    count = 0

    # Process files in notes directory
    if not args.n or count < args.n:
        for filename in os.listdir(notes_dir):
            if filename.endswith(".md") and (not args.n or count < args.n):
                file_path = os.path.join(notes_dir, filename)
                update_front_matter(file_path, args.type)
                count += 1

    # Process files in _notes directories
    if not args.n or count < args.n:
        for lang_dir in os.listdir(notes_output_dir):
            lang_dir_path = os.path.join(notes_output_dir, lang_dir)
            if os.path.isdir(lang_dir_path):
                for filename in os.listdir(lang_dir_path):
                    if filename.endswith(".md") and (not args.n or count < args.n):
                        file_path = os.path.join(lang_dir_path, filename)
                        update_front_matter(file_path, args.type)
                        count += 1


if __name__ == "__main__":
    main()
