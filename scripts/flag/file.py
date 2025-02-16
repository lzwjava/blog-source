import os
import datetime
import sys
import re
import glob

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
audio: false
lang: en
layout: post
title: {name}
translated: false
---"""


    # Create the English markdown file
    with open(en_file_path, 'w', encoding='utf-8') as en_file:
        en_file.write(en_front_matter)


    print(f"Created file: {en_file_path}")

def delete_md(name):
    posts_dir = '_posts'
    pdfs_dir = 'assets/pdfs'
    audios_dir = 'assets/audios'
    
    langs = ["en", "zh", "es", "fr", "de", "ja", "hi", "ar", "hant"]

    for lang in langs:
        # Construct the file name pattern, allowing for a date at the beginning
        md_file_pattern = os.path.join(posts_dir, lang, f"{name}-{lang}.md")
        pdf_file_pattern = os.path.join(pdfs_dir, lang, f"{name}-{lang}.pdf")
        audio_file_pattern = os.path.join(audios_dir, f"{name}-{lang}.mp3")

        # Find matching files
        for md_file_path in glob.glob(md_file_pattern):
            if os.path.exists(md_file_path):
                os.remove(md_file_path)
                print(f"Deleted file: {md_file_path}")
            else:
                print(f"File not found: {md_file_path}")
        
        # Check for original files without language code
        original_md_file_pattern_en = os.path.join(posts_dir, "en", f"{name}-en.md")
        original_md_file_pattern_zh = os.path.join(posts_dir, "zh", f"{name}-zh.md")
        
        for original_md_file_path in glob.glob(original_md_file_pattern_en):
            if os.path.exists(original_md_file_path):
                os.remove(original_md_file_path)
                print(f"Deleted file: {original_md_file_path}")
            else:
                print(f"File not found: {original_md_file_path}")
        for original_md_file_path in glob.glob(original_md_file_pattern_zh):
            if os.path.exists(original_md_file_path):
                os.remove(original_md_file_path)
                print(f"Deleted file: {original_md_file_path}")
            else:
                print(f"File not found: {original_md_file_path}")


        for pdf_file_path in glob.glob(pdf_file_pattern):
            if os.path.exists(pdf_file_path):
                os.remove(pdf_file_path)
                print(f"Deleted file: {pdf_file_path}")
            else:
                print(f"File not found: {pdf_file_path}")
        if os.path.exists(audio_file_pattern):
            os.remove(audio_file_pattern)
            print(f"Deleted file: {audio_file_pattern}")
        else:
            print(f"File not found: {audio_file_pattern}")


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
