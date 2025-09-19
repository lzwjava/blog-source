import os
import shutil

source_dir = "_posts"
target_dirs = {"-zh": "zh", "-en": "en"}

for filename in os.listdir(source_dir):
    if filename.endswith(".md"):
        for suffix, target_dir in target_dirs.items():
            if suffix in filename:
                target_path = os.path.join(source_dir, target_dir)
                if not os.path.exists(target_path):
                    os.makedirs(target_path)
                source_file = os.path.join(source_dir, filename)
                target_file = os.path.join(target_path, filename)
                shutil.move(source_file, target_file)
                print(f"Moved {filename} to {target_dir}")
                break
