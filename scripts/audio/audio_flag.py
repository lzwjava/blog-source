import os
import re
import yaml


def check_audio_file_exists(file_path):
    """Check if corresponding audio file exists in assets/audios"""
    file_name = os.path.basename(file_path).replace(".md", "")
    audio_file = os.path.join("assets", "audios", f"{file_name}.mp3")
    return os.path.exists(audio_file)


def update_front_matter(file_path):
    if not os.path.exists(file_path):
        return

    with open(file_path, "r", encoding="utf-8") as infile:
        content = infile.read()

    front_matter_match = re.match(r"\n*---(.*?)---", content, re.DOTALL)
    front_matter = front_matter_match.group(1) if front_matter_match else None

    if not front_matter:
        raise Exception(f"No front matter found in {file_path}")

    front_matter_dict = yaml.safe_load(front_matter) if front_matter else {}

    has_audio = check_audio_file_exists(file_path)
    front_matter_dict["audio"] = has_audio

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


def main():
    posts_dir = "_posts"
    languages = ["ja", "es", "hi", "zh", "en", "fr", "de", "ar", "hant"]
    original_dir = "original"

    if not os.path.exists(original_dir):
        return

    for lang_dir in languages:
        target_dir = os.path.join(posts_dir, lang_dir)
        if not os.path.exists(target_dir):
            continue
        for filename in os.listdir(target_dir):
            if filename.endswith(".md"):
                file_path = os.path.join(target_dir, filename)
                update_front_matter(file_path)


main()
