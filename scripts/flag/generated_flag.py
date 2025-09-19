import os
import re
import yaml
import datetime


def update_front_matter(file_path):
    try:
        # Extract date from filename
        filename = os.path.basename(file_path)
        date_match = re.match(r"(\d{4}-\d{2}-\d{2})", filename)
        if not date_match:
            print(f"Could not extract date from filename: {filename}")
            return
        file_date_str = date_match.group(1)
        file_date = datetime.datetime.strptime(file_date_str, "%Y-%m-%d").date()

        # Check if the file date is within the specified range
        start_date = datetime.date(2025, 1, 16)
        today = datetime.date.today()
        if not (start_date <= file_date <= today):
            return  # Skip files outside the date range

        with open(file_path, "r", encoding="utf-8") as infile:
            content = infile.read()

        front_matter_match = re.match(r"---\n(.*?)\n---", content, re.DOTALL)
        front_matter = front_matter_match.group(1) if front_matter_match else None

        if not front_matter:
            front_matter_dict = {}
        else:
            front_matter_dict = yaml.safe_load(front_matter) if front_matter else {}

        front_matter_dict["generated"] = True

        updated_front_matter = (
            "---\n" + yaml.dump(front_matter_dict, allow_unicode=True) + "---"
        )
        updated_content = (
            updated_front_matter + content[len(front_matter_match.group(0)) :]
            if front_matter_match
            else updated_front_matter + content
        )

        with open(file_path, "w", encoding="utf-8") as outfile:
            outfile.write(updated_content)
        print(f"Updated front matter in {file_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")


def main():
    original_dir = "original"
    posts_dir = "_posts"

    # Process files in original directory
    for filename in os.listdir(original_dir):
        if filename.endswith(".md"):
            file_path = os.path.join(original_dir, filename)
            update_front_matter(file_path)

    # Process files in _posts directories
    for lang_dir in os.listdir(posts_dir):
        lang_dir_path = os.path.join(posts_dir, lang_dir)
        if os.path.isdir(lang_dir_path):
            for filename in os.listdir(lang_dir_path):
                if filename.endswith(".md"):
                    file_path = os.path.join(lang_dir_path, filename)
                    update_front_matter(file_path)


if __name__ == "__main__":
    main()
