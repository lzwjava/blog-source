import subprocess
import os
from dotenv import load_dotenv
import argparse

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update language files.")
    parser.add_argument('--dry_run', dest='dry_run', action='store_true', help='Only print the files to be processed.')
    parser.add_argument("--max_files", type=int, default=None, help="Maximum number of files to process.")

    args = parser.parse_args()

    files = get_changed_files()
    
    if args.max_files and len(files) > args.max_files:
        files = files[:args.max_files]
    
    total_files_to_process = len(files)

    if args.dry_run:
        print(f"Total Markdown files to process: {total_files_to_process}")
    else:
        for file in files:
            subprocess.run(["python", "scripts/update_lang.py", "--file", file, "--model", "mistral"], check=True)
        print(f"Total Markdown files to process: {total_files_to_process}")
