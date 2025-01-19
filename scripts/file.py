import os
import datetime
import sys

def create_md(name):
    # Get today's date
    today = datetime.date.today()
    date_str = today.strftime('%Y-%m-%d')

    # Define file paths
    drafts_dir = '_drafts'
    if not os.path.exists(drafts_dir):
        os.makedirs(drafts_dir)

    en_file_path = os.path.join(drafts_dir, f"{date_str}-{name}-en.md")

    # English front matter
    en_front_matter = f"""---
audio: true
lang: en
layout: post
title: {name}
---"""


    # Create the English markdown file
    with open(en_file_path, 'w', encoding='utf-8') as en_file:
        en_file.write(en_front_matter)


    print(f"Created file: {en_file_path}")

def delete_md(name):
    posts_dir = '_posts'
    
    today = datetime.date.today()
    date_str = today.strftime('%Y-%m-%d')

    langs = ["en", "zh", "es", "fr", "de", "ja", "hi", "ar", "hant"]
    for lang in langs:
        file_path = os.path.join(posts_dir, lang, f"{date_str}-{name}-{lang}.md")
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted file: {file_path}")
        else:
            print(f"File not found: {file_path}")


if __name__ == "__main__":
    # Input name from command line argument
    if len(sys.argv) < 3:
        print("Usage: python scripts/file.py <create|delete> <name>")
    else:
        action = sys.argv[1]
        name = sys.argv[2]
        if action == "create":
            create_md(name)
        elif action == "delete":
            delete_md(name)
        else:
            print("Invalid action. Use 'create' or 'delete'.")
