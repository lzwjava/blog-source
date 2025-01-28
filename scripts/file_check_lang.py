import os
import re
import yaml
from dotenv import load_dotenv

load_dotenv()

INPUT_DIR = "original"

def get_changed_files():
    changed_files = []
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".md"):
            input_file = os.path.join(INPUT_DIR, filename)
            try:
                languages = ['ja', 'es', 'hi', 'zh', 'en', 'fr', 'de', 'ar', 'hant']

                for lang in languages:
                    output_dir = f"_posts/{lang}"
                    output_filename = os.path.basename(input_file).replace("-en.md", f"-{lang}.md").replace("-zh.md", f"-{lang}.md")
                    output_file = os.path.join(output_dir, output_filename)
                    if not os.path.exists(output_file):
                        changed_files.append(input_file)
                        break
            except Exception as e:
                print(f"Error processing file {input_file}: {e}")
    return changed_files

files = get_changed_files()

for file in files:
    print(file)

