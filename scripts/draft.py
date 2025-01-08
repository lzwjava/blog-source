import os
import datetime

def create_md(name):
    # Get today's date
    today = datetime.date.today()
    date_str = today.strftime('%Y-%m-%d')

    # Define file paths
    drafts_dir = '_drafts'
    if not os.path.exists(drafts_dir):
        os.makedirs(drafts_dir)

    en_file_path = os.path.join(drafts_dir, f"{date_str}-{name}-en.md")
    zh_file_path = os.path.join(drafts_dir, f"{date_str}-{name}-zh.md")

    # English front matter
    en_front_matter = f"""---
audio: true
lang: en
layout: post
title: {name}
---"""

    # Chinese front matter
    zh_front_matter = f"""---
audio: true
lang: zh
layout: post
title: {name}
---"""

    # Create the English markdown file
    with open(en_file_path, 'w', encoding='utf-8') as en_file:
        en_file.write(en_front_matter)

    # Create the Chinese markdown file
    with open(zh_file_path, 'w', encoding='utf-8') as zh_file:
        zh_file.write(zh_front_matter)

    print(f"Created files: {en_file_path}, {zh_file_path}")

if __name__ == "__main__":
    # Input name from command line argument
    import sys
    if len(sys.argv) != 2:
        print("Usage: python scripts/draft.py <name>")
    else:
        create_md(sys.argv[1])
