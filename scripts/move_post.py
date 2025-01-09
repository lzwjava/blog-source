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

for filename in os.listdir(source_en_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(source_en_dir, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            post = frontmatter.loads(content)
            post_date = post.get('date')
            if post_date:
                if isinstance(post_date, str):
                    post_date = datetime.strptime(post_date.split(' ')[0], '%Y-%m-%d')
                if post_date > date_threshold:
                    target_file = os.path.join(target_dir, filename)
                    copy_file(filepath, target_file)
        except Exception as e:
            print(f"Error processing {filepath}: {e}")

for filename in os.listdir(source_zh_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(source_zh_dir, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            post = frontmatter.loads(content)
            post_date = post.get('date')
            if post_date:
                if isinstance(post_date, str):
                    post_date = datetime.strptime(post_date.split(' ')[0], '%Y-%m-%d')
                if post_date < date_threshold:
                    target_file = os.path.join(target_dir, filename)
                    copy_file(filepath, target_file)
        except Exception as e:
            print(f"Error processing {filepath}: {e}")
