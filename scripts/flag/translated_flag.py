import os
import re
import yaml


def update_front_matter(original_file_path, translated_file_path):
    try:
        with open(original_file_path, "r", encoding="utf-8") as infile:
            original_content = infile.read()

        original_front_matter_match = re.match(
            r"---\n(.*?)\n---", original_content, re.DOTALL
        )
        original_front_matter = (
            original_front_matter_match.group(1)
            if original_front_matter_match
            else None
        )

        if not original_front_matter:
            print(f"No front matter found in {original_file_path}")
            return

        original_front_matter_dict = (
            yaml.safe_load(original_front_matter) if original_front_matter else {}
        )

        if not os.path.exists(translated_file_path):
            print(f"Translated file not found: {translated_file_path}")
            return

        with open(translated_file_path, "r", encoding="utf-8") as translated_infile:
            translated_content = translated_infile.read()

        translated_front_matter_match = re.match(
            r"---\n(.*?)\n---", translated_content, re.DOTALL
        )
        translated_front_matter = (
            translated_front_matter_match.group(1)
            if translated_front_matter_match
            else None
        )

        if not translated_front_matter:
            print(f"No front matter found in {translated_file_path}")
            return

        translated_front_matter_dict = (
            yaml.safe_load(translated_front_matter) if translated_front_matter else {}
        )

        if (
            "lang" in original_front_matter_dict
            and "lang" in translated_front_matter_dict
        ):
            if (
                original_front_matter_dict["lang"]
                != translated_front_matter_dict["lang"]
            ):
                translated_front_matter_dict["translated"] = True
            else:
                translated_front_matter_dict["translated"] = False
        else:
            translated_front_matter_dict["translated"] = False

        updated_front_matter = (
            "---\n"
            + yaml.dump(translated_front_matter_dict, allow_unicode=True)
            + "---"
        )
        updated_content = (
            updated_front_matter
            + translated_content[len(translated_front_matter_match.group(0)) :]
            if translated_front_matter_match
            else updated_front_matter + translated_content
        )

        with open(translated_file_path, "w", encoding="utf-8") as outfile:
            outfile.write(updated_content)
        print(f"Updated front matter in {translated_file_path}")

    except Exception as e:
        print(f"Error processing {translated_file_path}: {e}")


def main():
    original_dir = "original"
    posts_dir = "_posts"

    for filename in os.listdir(original_dir):
        if filename.endswith(".md"):
            original_file_path = os.path.join(original_dir, filename)

            base_name = filename.replace(".md", "")

            for lang_dir in os.listdir(posts_dir):
                if lang_dir in ["de"]:
                    translated_file_name = f"{base_name}-{lang_dir}.md"
                    translated_file_path = os.path.join(
                        posts_dir, lang_dir, translated_file_name
                    )
                    if os.path.exists(translated_file_path):
                        update_front_matter(original_file_path, translated_file_path)

                    # Handle the case where the original file is named with "-en.md" or "-zh.md"
                    if filename.endswith("-en.md") or filename.endswith("-zh.md"):
                        base_name_without_suffix = filename.replace(
                            "-en.md", ""
                        ).replace("-zh.md", "")
                        translated_file_name = (
                            f"{base_name_without_suffix}-{lang_dir}.md"
                        )
                        translated_file_path = os.path.join(
                            posts_dir, lang_dir, translated_file_name
                        )
                        if os.path.exists(translated_file_path):
                            update_front_matter(
                                original_file_path, translated_file_path
                            )


if __name__ == "__main__":
    main()
