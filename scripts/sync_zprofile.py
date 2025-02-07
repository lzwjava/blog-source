import shutil
import os
import re

source_file = os.path.expanduser("~/.zprofile")
target_file = os.path.join(os.path.dirname(__file__), "config", ".zprofile")

with open(source_file, 'r') as f_source:
    content = f_source.read()

# Replace API keys with "xxx"
content = re.sub(r'export (\w+_API_KEY)=".*"', r'export \1="xxx"', content)
content = re.sub(r'export (TIGER_\w+)=".*"', r'export \1="xxx"', content)


with open(target_file, 'w') as f_target:
    f_target.write(content)

print(f"Copied and sanitized {source_file} to {target_file}")
