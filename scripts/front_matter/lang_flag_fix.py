import os
import re
import yaml
import json

updated_files = []


def update_front_matter(file_path, correct_lang):
    global updated_files
    try:
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            return

        with open(file_path, "r", encoding="utf-8") as infile:
            content = infile.read()

        front_matter_match = re.match(r"---\n(.*?)\n---", content, re.DOTALL)
        front_matter = front_matter_match.group(1) if front_matter_match else None

        if not front_matter:
            print(f"No front matter found in {file_path}")
            return

        front_matter_dict = yaml.safe_load(front_matter) if front_matter else {}

        if "lang" in front_matter_dict:
            if front_matter_dict["lang"] != correct_lang:
                print(
                    f"  Correcting language from {front_matter_dict['lang']} to {correct_lang} in {file_path}"
                )
                front_matter_dict["lang"] = correct_lang
                updated_files.append(file_path)
        else:
            print(f"  Adding language {correct_lang} in {file_path}")
            front_matter_dict["lang"] = correct_lang
            updated_files.append(file_path)

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
        print(f"Updated front matter in {file_path}, language set to {correct_lang}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")


def main():
    posts_dir = "_posts"
    languages = ["ja", "es", "hi", "zh", "en", "fr", "de", "ar", "hant"]
    original_dir = "original"

    if not os.path.exists(original_dir):
        print(f"Directory not found: {original_dir}")
        return

    for lang_dir in languages:
        target_dir = os.path.join(posts_dir, lang_dir)
        if not os.path.exists(target_dir):
            print(f"Directory not found: {target_dir}")
            continue
        print(f"Processing files in {target_dir}")
        for filename in os.listdir(target_dir):
            if filename.endswith(".md"):
                translated_file_path = os.path.join(target_dir, filename)
                update_front_matter(translated_file_path, lang_dir)

    with open("lang_flag_fix.json", "w") as outfile:
        json.dump(updated_files, outfile, indent=4)


if __name__ == "__main__":
    main()
