import os


def find_translated_files():
    original_dir = "original"
    posts_dir = "_posts"

    if not os.path.exists(original_dir):
        print(f"Error: '{original_dir}' directory not found.")
        return

    original_files = set()
    for filename in os.listdir(original_dir):
        if filename.endswith(".md"):
            original_files.add(filename)
            file_base = filename[:-5]  # Remove ".md"

            if filename.endswith("-en.md"):
                target_lang = "en"
            elif filename.endswith("-zh.md"):
                target_lang = "en"
            else:
                print(f"Skipping {filename} as it does not end with -en.md or -zh.md")
                continue
            target_dir = os.path.join(posts_dir, target_lang)
            target_file = f"{file_base}{target_lang}.md"
            target_path = os.path.join(target_dir, target_file)
            # print(f"{filename}  Checking: target_dir={target_dir}, target_file={target_file}, target_path={target_path}")

            if not os.path.exists(target_path):
                print(f"  {filename} does not exist in {target_dir}/{target_path}")
        else:
            print(filename)


if __name__ == "__main__":
    find_translated_files()
