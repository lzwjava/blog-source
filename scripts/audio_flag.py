import os
import re
import yaml
import traceback

def check_audio_file_exists(file_path):
    """Check if corresponding audio file exists in assets/audios"""
    # Extract base filename without extension
    file_name = os.path.basename(file_path).replace('.md', '')
    # Construct audio file path
    audio_file = os.path.join('assets', 'audios', f'{file_name}.mp3')
    return os.path.exists(audio_file)

def update_front_matter(file_path):
    print(f"Starting to process file: {file_path}")
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    print(f"Reading content from {file_path}")
    with open(file_path, "r", encoding="utf-8") as infile:
        content = infile.read()
        print(f"Successfully read {len(content)} characters from {file_path}")

    print(f"Extracting front matter from {file_path}")
    front_matter_match = re.match(r"\n*---(.*?)---", content, re.DOTALL)
    front_matter = front_matter_match.group(1) if front_matter_match else None
            
    if not front_matter:
        print(f"No front matter found in {file_path}")
        raise Exception('No front matter found in {file_path}')
        
    print(f"Front matter found in {file_path}")

    print(f"Loading front matter YAML for {file_path}")
    front_matter_dict = yaml.safe_load(front_matter) if front_matter else {}
    print(f"Current front matter content: {front_matter_dict}")

    # Check if audio file exists
    has_audio = check_audio_file_exists(file_path)
    print(f"Setting audio flag to {has_audio} for {file_path}")
    front_matter_dict["audio"] = has_audio

    print(f"Generating updated front matter for {file_path}")
    updated_front_matter = (
        "---\n" + yaml.dump(front_matter_dict, allow_unicode=True) + "---"
    )
    print(f"Updated front matter content: {updated_front_matter}")

    print(f"Creating updated content for {file_path}")
    updated_content = (
        updated_front_matter + content[len(front_matter_match.group(0)) :]
        if front_matter_match
        else updated_front_matter + content
    )

    print(f"Writing updated content to {file_path}")
    with open(file_path, "w", encoding="utf-8") as outfile:
        outfile.write(updated_content)
    print(f"Successfully updated front matter in {file_path}, audio set to {has_audio}")

def main():
    posts_dir = "_posts"
    languages = ["ja", "es", "hi", "zh", "en", "fr", "de", "ar", "hant"]
    original_dir = "original"

    if not os.path.exists(original_dir):
        print(f"Directory not found: {original_dir}")
        return

    # Process all language directories
    for lang_dir in languages:
        target_dir = os.path.join(posts_dir, lang_dir)
        if not os.path.exists(target_dir):
            print(f"Directory not found: {target_dir}")
            continue
        print(f"Processing files in {target_dir}")
        for filename in os.listdir(target_dir):
            if filename.endswith(".md"):
                file_path = os.path.join(target_dir, filename)
                print(f"  Updating audio flag for {file_path}")
                update_front_matter(file_path)


main()
