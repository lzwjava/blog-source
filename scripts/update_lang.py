import os
import re
import time
import argparse
import subprocess
from dotenv import load_dotenv
from openai import OpenAI
import yaml
import concurrent.futures

load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
MODEL_NAME = "deepseek-chat"
INPUT_DIR = "original"
MAX_THREADS = 20

client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")


def create_translation_prompt(target_language):
    if target_language == 'ja':
        return "You are a professional translator. You are translating a markdown file for a Jekyll blog post. Translate the following text to Japanese. Do not translate English names. Be careful about code blocks, if not sure, just do not change."
    elif target_language == 'es':
        return "You are a professional translator. You are translating a markdown file for a Jekyll blog post. Translate the following text to Spanish. Do not translate English names. Be careful about code blocks, if not sure, just do not change."
    elif target_language == 'hi':
        return "You are a professional translator. You are translating a markdown file for a Jekyll blog post. Translate the following text to Hindi. Do not translate English names. Be careful about code blocks, if not sure, just do not change."
    else:
        return f"You are a professional translator. You are translating a markdown file for a Jekyll blog post. Translate the following text to {target_language}. Do not translate English names. Be careful about code blocks, if not sure, just do not change."


def translate_text(text, target_language):
    print(f"  Translating text: {text[:50]}...")
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": create_translation_prompt(target_language)},
                {"role": "user", "content": text}
            ],
            stream=False
        )
        if response and response.choices:
            print(f"  Translation successful.")
            return response.choices[0].message.content
        else:
            print(f"  Translation failed.")
            return None
    except Exception as e:
        print(f"  Translation failed with error: {e}")
        return None

def translate_front_matter(front_matter, target_language):
    if not front_matter:
        return ""
    try:
        front_matter_dict = {}
        if front_matter:
            front_matter_dict = yaml.safe_load(front_matter)
        if 'title' in front_matter_dict:
            translated_title = translate_text(front_matter_dict['title'], target_language)
            if translated_title:
                front_matter_dict['title'] = translated_title
        # Always set lang to target_language
        front_matter_dict['lang'] = target_language
        return "---\n" + yaml.dump(front_matter_dict, allow_unicode=True) + "---"
    except yaml.YAMLError as e:
        print(f"  Error parsing front matter: {e}")
        return front_matter


def translate_markdown_file(input_file, output_file, target_language, changed_paragraphs=None, dry_run=False):
    print(f"  Processing file: {input_file}")
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            content = infile.read()

        # Extract front matter
        front_matter_match = re.match(r'---\n(.*?)\n---', content, re.DOTALL)
        front_matter = front_matter_match.group(1) if front_matter_match else ""
        content_without_front_matter = content[len(front_matter_match.group(0)):] if front_matter_match else content
        
        if not dry_run:
            translated_front_matter = translate_front_matter(front_matter, target_language)
            
            
            translated_content = translate_text(content_without_front_matter, target_language)
            if translated_content:
                translated_content = translated_front_matter + "\n\n" + translated_content
            else:
                translated_content = content
            
            if os.path.exists(output_file):
                os.remove(output_file)
                
            with open(output_file, 'w', encoding='utf-8') as outfile:
                outfile.write(translated_content)
        else:
            translated_content = content
        print(f"  Finished processing file: {output_file}")
    except Exception as e:
        print(f"  Error processing file {input_file}: {e}")


def get_changed_files():
    try:
        # Get the list of files changed in the last commit
        result = subprocess.run(['git', 'diff', '--name-only', 'HEAD~1', 'HEAD'], capture_output=True, text=True, check=True)
        changed_files = result.stdout.strip().split('\n')
        return [f for f in changed_files if f.startswith(f'{INPUT_DIR}/') and f.endswith('.md')]
    except subprocess.CalledProcessError as e:
        print(f"Error getting changed files: {e}")
        return []

def get_changed_paragraphs(input_file, output_file):
    try:
        result = subprocess.run(['git', 'diff', 'HEAD~1', 'HEAD', '--', input_file], capture_output=True, text=True, check=True)
        diff_output = result.stdout
        changed_lines = set()
        
        for line in diff_output.splitlines():
            if line.startswith('@@'):
                match = re.search(r'\+(\d+)', line)
                if match:
                    start_line = int(match.group(1))
                    changed_lines.add(start_line)
        
        if not changed_lines:
            return None
        
        with open(input_file, 'r', encoding='utf-8') as infile:
            content = infile.read()
        
        front_matter_match = re.match(r'---\n(.*?)\n---', content, re.DOTALL)
        content_without_front_matter = content[len(front_matter_match.group(0)):] if front_matter_match else content
        paragraphs = content_without_front_matter.split('\n\n')
        
        changed_paragraphs = set()
        current_line = 1
        for i, paragraph in enumerate(paragraphs):
            if current_line in changed_lines:
                changed_paragraphs.add(str(i))
            current_line += paragraph.count('\n') + 1
        
        return changed_paragraphs
    except subprocess.CalledProcessError as e:
        print(f"Error getting diff: {e}")
        return None
    except FileNotFoundError:
        print(f"File not found: {input_file}")
        return None


def main():
    if not DEEPSEEK_API_KEY:
        print("Error: DEEPSEEK_API_KEY is not set in .env file.")
        return

    parser = argparse.ArgumentParser(description="Translate markdown files to a specified language.")
    parser.add_argument("--lang", type=str, default="all", help="Target language for translation (e.g., ja, es, all).")
    parser.add_argument("--dry_run", action="store_true", help="Perform a dry run without modifying files.")
    args = parser.parse_args()
    target_language = args.lang
    dry_run = args.dry_run
    
    languages = ['ja', 'es', 'hi', 'zh'] if target_language == 'all' else [target_language]

    total_files_to_process = 0
    for lang in languages:
        output_dir = f"_posts/{lang}"
        if lang == 'hi':
            output_dir = "_posts/hi"
        os.makedirs(output_dir, exist_ok=True)
        print(f"Created directory {output_dir}")

        changed_files = get_changed_files()
        total_files_to_process += len(changed_files)
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
            futures = []
            for filename in changed_files:
                input_file = filename
                output_filename = os.path.basename(filename).replace(".md", f"-{lang}.md")
                
                # Check if the original file is named with "-en.md" or "-zh.md"
                if filename.endswith("-en.md") or filename.endswith("-zh.md"):
                    output_filename = os.path.basename(filename).replace("-en.md", f"-{lang}.md").replace("-zh.md", f"-{lang}.md")
                
                output_file = os.path.join(output_dir, output_filename)
                
                changed_paragraphs = get_changed_paragraphs(input_file, output_file)
                
                print(f"Submitting translation job for {filename} to {lang}...")
                future = executor.submit(translate_markdown_file, input_file, output_file, lang, changed_paragraphs, dry_run)
                futures.append(future)
            
            for future in concurrent.futures.as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    print(f"A thread failed: {e}")
    print(f"Total Markdown files to process: {total_files_to_process}")


if __name__ == "__main__":
    main()
