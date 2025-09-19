import os


def find_translated_files():
    original_dir = "original"
    posts_dir = "_posts"

    if not os.path.exists(original_dir):
        print(f"Error: '{original_dir}' directory not found.")
        return

    for filename in os.listdir(original_dir):
        if filename.endswith(".md"):
            file_base = filename[:-3]  # Remove ".md"

            if filename.endswith("-en.md"):
                target_lang = "en"
            elif filename.endswith("-zh.md"):
                target_lang = "zh"
            else:
                print(f"Skipping {filename} as it does not end with -en.md or -zh.md")
                continue

            target_dir = os.path.join(posts_dir, target_lang)
            target_file = f"{file_base}.md"
            target_path = os.path.join(target_dir, target_file)

            if not os.path.exists(target_path):
                print(f"  {filename} does not exist in {target_lang}")


if __name__ == "__main__":
    find_translated_files()
