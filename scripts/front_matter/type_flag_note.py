import os
import re
import frontmatter
import datetime
import argparse
from .type_flag_util import update_front_matter

def main():
    parser = argparse.ArgumentParser(description='Update front matter in blog notes files')
    parser.add_argument('-n', type=int, help='Maximum number of files to update')
    parser.add_argument('--type', default='note', help='Type value to set in front matter (default: note)')
    args = parser.parse_args()

    notes_dir = "notes"
    notes_output_dir = "_notes"
    count = 0

    # Process files in notes directory
    if not args.n or count < args.n:
        for filename in os.listdir(notes_dir):
            if filename.endswith(".md") and (not args.n or count < args.n):
                file_path = os.path.join(notes_dir, filename)
                update_front_matter(file_path, args.type)
                count += 1

    # Process files in _notes directories
    if not args.n or count < args.n:
        for lang_dir in os.listdir(notes_output_dir):
            lang_dir_path = os.path.join(notes_output_dir, lang_dir)
            if os.path.isdir(lang_dir_path):
                for filename in os.listdir(lang_dir_path):
                    if filename.endswith(".md") and (not args.n or count < args.n):
                        file_path = os.path.join(lang_dir_path, filename)
                        update_front_matter(file_path, args.type)
                        count += 1


if __name__ == "__main__":
    main()
