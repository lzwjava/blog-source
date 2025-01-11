import os
import re
import yaml

def update_front_matter(translated_file_path, is_translated):
    try:
        if not os.path.exists(translated_file_path):
            print(f"Translated file not found: {translated_file_path}")
            return
        
        with open(translated_file_path, 'r', encoding='utf-8') as translated_infile:
            translated_content = translated_infile.read()
        
        translated_front_matter_match = re.match(r'---\n(.*?)\n---', translated_content, re.DOTALL)
        translated_front_matter = translated_front_matter_match.group(1) if translated_front_matter_match else None
        
        if not translated_front_matter:
            print(f"No front matter found in {translated_file_path}")
            return
        
        translated_front_matter_dict = yaml.safe_load(translated_front_matter) if translated_front_matter else {}
        
        translated_front_matter_dict['translated'] = is_translated
        
        updated_front_matter = "---\n" + yaml.dump(translated_front_matter_dict, allow_unicode=True) + "---"
        updated_content = updated_front_matter + translated_content[len(translated_front_matter_match.group(0)):] if translated_front_matter_match else updated_front_matter + translated_content
        
        with open(translated_file_path, 'w', encoding='utf-8') as outfile:
            outfile.write(updated_content)
        print(f"Updated front matter in {translated_file_path}")

    except Exception as e:
        print(f"Error processing {translated_file_path}: {e}")

def main():
    original_dir = "original"
    posts_dir = "_posts"

    for filename in os.listdir(original_dir):
        if filename.endswith("-en.md"):
            target_file = os.path.join(posts_dir, "en", filename)
            update_front_matter(target_file, False)
        elif filename.endswith("-zh.md"):
            target_file = os.path.join(posts_dir, "zh", filename)
            update_front_matter(target_file, False)

if __name__ == "__main__":
    main()
