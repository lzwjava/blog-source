import os
import re
import yaml


def update_front_matter(file_path):
    try:
        with open(file_path, "r+", encoding="utf-8") as infile:
            content = infile.read()

        front_matter_match = re.match(r"---\n(.*?)\n---", content, re.DOTALL)
        if front_matter_match:
            front_matter = front_matter_match.group(1)
            front_matter_dict = yaml.safe_load(front_matter) if front_matter else {}
        else:
            front_matter_dict = {}

        # Check if content contains image path
        has_image = "assets/images/" in content
        front_matter_dict["image"] = has_image

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
        print(f"Updated front matter in {file_path} with image={has_image}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")


def process_all_files():
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


def main():
    process_all_files()


if __name__ == "__main__":
    main()
