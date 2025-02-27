import os
import datetime
import sys
import re
import glob

def create_md(name):
    """Create a draft Markdown file in the _drafts directory."""
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

def create_note(name):
    """Create a note Markdown file in the notes directory."""
    # Get today's date
    today = datetime.date.today()
    date_str = today.strftime('%Y-%m-%d')

    # Define file paths
    notes_dir = 'notes'
    if not os.path.exists(notes_dir):
        os.makedirs(notes_dir)

    note_file_path = os.path.join(notes_dir, f"{date_str}-{name}-en.md")

    # Note front matter (simplified version, adjust as needed)
    note_front_matter = f"""---
title: {name}
lang: en
layout: post
audio: false
translated: false
---"""

    # Create the note markdown file
    with open(note_file_path, 'w', encoding='utf-8') as note_file:
        note_file.write(note_front_matter)

    print(f"Created note: {note_file_path}")

def create_original(name):
    """Create an original Markdown file directly in the _posts/en directory."""
    # Get today's date
    today = datetime.date.today()
    date_str = today.strftime('%Y-%m-%d')

    # Define file paths
    posts_dir = os.path.join('_posts', 'en')
    if not os.path.exists(posts_dir):
        os.makedirs(posts_dir)

    file_path = os.path.join(posts_dir, f"{date_str}-{name}-en.md")

    # Front matter (same as create_md)
    front_matter = f"""---
audio: false
lang: en
layout: post
title: {name}
translated: false
---"""

    # Create the markdown file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(front_matter)

    print(f"Created original file: {file_path}")

def delete_md(name):
    """Delete Markdown files and associated assets for the given name across languages."""
    posts_dir = '_posts'
    pdfs_dir = 'assets/pdfs'
    audios_dir = 'assets/audios'
    
    langs = ["en", "zh", "es", "fr", "de", "ja", "hi", "ar", "hant"]

    for lang in langs:
        # Construct the file name pattern
        md_file_pattern = os.path.join(posts_dir, lang, f"{name}-{lang}.md")
        pdf_file_pattern = os.path.join(pdfs_dir, lang, f"{name}-{lang}.pdf")
        audio_file_pattern = os.path.join(audios_dir, f"{name}-{lang}.mp3")

        # Find and delete matching Markdown files
        for md_file_path in glob.glob(md_file_pattern):
            if os.path.exists(md_file_path):
                os.remove(md_file_path)
                print(f"Deleted file: {md_file_path}")
            else:
                print(f"File not found: {md_file_path}")
        
        # Check for original files in en and zh directories
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

        # Delete associated PDF files
        for pdf_file_path in glob.glob(pdf_file_pattern):
            if os.path.exists(pdf_file_path):
                os.remove(pdf_file_path)
                print(f"Deleted file: {pdf_file_path}")
            else:
                print(f"File not found: {pdf_file_path}")
        
        # Delete associated audio files
        if os.path.exists(audio_file_pattern):
            os.remove(audio_file_pattern)
            print(f"Deleted file: {audio_file_pattern}")
        else:
            print(f"File not found: {audio_file_pattern}")

if __name__ == "__main__":
    """Main entry point to handle command-line arguments."""
    if len(sys.argv) < 3:
        print("Usage: python scripts/file.py <create|create-note|create-original|delete> <name>")
    else:
        action = sys.argv[1]
        name = sys.argv[2]
        if action == "create":
            create_md(name)
        elif action == "create-note":
            create_note(name)
        elif action == "create-original":
            create_original(name)
        elif action == "delete":
            delete_md(name)
        else:
            print("Invalid action. Use 'create', 'create-note', 'create-original', or 'delete'.")