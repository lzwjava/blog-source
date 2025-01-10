import os
import re

def remove_link_from_frontmatter(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    # Regex to find lines starting with 'link:' or 'link: '
    pattern = re.compile(r'^link:\s*.*$', re.MULTILINE)
    
    modified_content = pattern.sub('', content)

    with open(file_path, 'w') as f:
        f.write(modified_content)

if __name__ == "__main__":
    target_dir = "original"
    for root, _, files in os.walk(target_dir):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                remove_link_from_frontmatter(file_path)
                print(f"Processed: {file_path}")
