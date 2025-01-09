import os
import shutil
import frontmatter
from datetime import datetime

source_en_dir = "_posts/en"
source_zh_dir = "_posts/zh"
target_dir = "_posts"

date_threshold = datetime(2022, 9, 29)

def copy_file(source_file, target_file):
    shutil.copy2(source_file, target_file)
    print(f"Copied {source_file} to {target_file}")

def process_posts(source_dir, target_dir, date_threshold, is_en):
    print(f"Processing posts in {source_dir}")
    for filename in os.listdir(source_dir):
        if filename.endswith(".md"):
            filepath = os.path.join(source_dir, filename)
            print(f"  Processing {filepath}")
            try:
                parts = filename.split('-')
                if len(parts) < 4:
                    print(f"    Skipped {filepath} due to invalid filename format.")
                    continue
                date_str = '-'.join(parts[:3])
                post_date = datetime.strptime(date_str, '%Y-%m-%d')
                print(f"    Post date: {post_date}")

                if is_en and post_date > date_threshold:
                    target_file = os.path.join(target_dir, "original", filename)
                    copy_file(filepath, target_file)
                    print(f"    Moved {filepath} to original folder because it is an english post after {date_threshold}")
                elif not is_en and post_date < date_threshold:
                    target_file = os.path.join(target_dir, "original", filename)
                    copy_file(filepath, target_file)
                    print(f"    Moved {filepath} to original folder because it is a chinese post before {date_threshold}")
                else:
                    print(f"    Skipped {filepath} due to date condition.")

            except Exception as e:
                print(f"    Error processing {filepath}: {e}")

os.makedirs(os.path.join(target_dir, "original"), exist_ok=True)
print(f"Created directory {os.path.join(target_dir, 'original')}")
process_posts(source_en_dir, target_dir, date_threshold, True)
process_posts(source_zh_dir, target_dir, date_threshold, False)
