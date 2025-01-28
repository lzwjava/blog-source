import shutil
import os
import re

source_file = os.path.expanduser("~/.zprofile")
target_file = os.path.join(os.path.dirname(__file__), ".zprofile")

with open(source_file, 'r') as f_source:
    content = f_source.read()

# Replace API keys with "xxx"
content = re.sub(r'export DEEPSEEK_API_KEY=".*"', 'export DEEPSEEK_API_KEY="xxx"', content)
content = re.sub(r'export MISTRAL_API_KEY=".*"', 'export MISTRAL_API_KEY="xxx"', content)
content = re.sub(r'export DO_API_KEY=".*"', 'export DO_API_KEY="xxx"', content)
content = re.sub(r'export GEMINI_API_KEY=".*"', 'export GEMINI_API_KEY="xxx"', content)



with open(target_file, 'w') as f_target:
    f_target.write(content)

print(f"Copied and sanitized {source_file} to {target_file}")
