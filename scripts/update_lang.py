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
MAX_THREADS = 10

client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")

def create_translation_prompt(target_language, special=False):
    if target_language == 'ja':
        return "You are a professional translator. You are translating a markdown file for a Jekyll blog post. Translate the following text to Japanese. Do not translate English names. Be careful about code blocks."
    elif target_language == 'es':
        return "You are a professional translator. You are translating a markdown file for a Jekyll blog post. Translate the following text to Spanish. Do not translate English names. Be careful about code blocks."
    elif target_language == 'hi':
        return "You are a professional translator. You are translating a markdown file for a Jekyll blog post. Translate the following text to Hindi. Do not translate English names. Be careful about code blocks."
    elif target_language == 'fr':
        return "You are a professional translator. You are translating a markdown file for a Jekyll blog post. Translate the following text to French. Do not translate English names. Be careful about code blocks."
    elif target_language == "zh":
        if special:
            return f"""You are a professional translator. You are translating a markdown file for a Jekyll blog post from English to Chinese. Translate the following text to Chinese. Translate Zhiwei Li to 李智维. Translate Meitai Technology Services to 美钛技术服务. Translate Neusiri to 思芮 instead of 纽思瑞. Translate Chongding Conference to 冲顶大会. Translate Fun Live to 趣直播. Translate MianbaoLive to 面包Live. Translate Beijing Dami Entertainment Co. to 北京大米互娱有限公司. Translate Guangzhou Yuyan Middle School to 广州玉岩中学. Do not translate English names or code blocks. Be careful about code blocks."""
        else:
            return f"""You are a professional translator. You are translating a markdown file for a Jekyll blog post from English to Chinese. Translate the following text to Chinese. Do not translate English names or code blocks. Be careful about code blocks."""
    elif target_language == 'hant':
        return "You are a professional translator. You are translating a markdown file for a Jekyll blog post. Translate the following text to Traditional Chinese (Hong Kong). "
    elif target_language == 'en':
        return "You are a professional translator. You are translating a markdown file for a Jekyll blog post. Translate the following text to English. Do not translate English names. Be careful about code blocks."
    elif target_language == 'de':
        return "You are a professional translator. You are translating a markdown file for a Jekyll blog post. Translate the following text to German. Do not translate English names. Be careful about code blocks."
    elif target_language == 'ar':
        return "You are a professional translator. You are translating a markdown file for a Jekyll blog post. Translate the following text to Arabic. Do not translate English names. Be careful about code blocks."
    else:
        return f"You are a professional translator. You are translating a markdown file for a Jekyll blog post. Translate the following text to {target_language}. Do not translate English names. Be careful about code blocks."

def translate_text(text, target_language, special=False):
    if not text or not text.strip():
        return ""
    print(f"  Translating text: {text[:50]}...")
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": create_translation_prompt(target_language, special)},
                {"role": "user", "content": text}
            ],
            stream=False
        )
        if response and response.choices:
            translated_text = response.choices[0].message.content
            return translated_text
        else:
            print(f"  Translation failed.")
            return None
    except Exception as e:
        print(f"  Translation failed with error: {e}")
        return None

def translate_front_matter(front_matter, target_language, input_file):
    print(f"  Translating front matter for: {input_file}")
    if not front_matter:
        print(f"  No front matter found for: {input_file}")
        return ""
    try:
        front_matter_dict = {}
        if front_matter:
            front_matter_dict = yaml.safe_load(front_matter)
            print(f"  Front matter after safe_load: {front_matter_dict}")
        if 'title' in front_matter_dict:
            print(f"  Translating title: {front_matter_dict['title']}")
            if not (input_file == 'original/2025-01-11-resume-en.md' and target_language in ['zh', 'fr']):
                if isinstance(front_matter_dict['title'], str):
                    translated_title = translate_text(front_matter_dict['title'], target_language)
                    if translated_title:
                        translated_title = translated_title.strip()
                        if len(translated_title) > 300:
                            translated_title = translated_title.split('\n')[0]
                        front_matter_dict['title'] = translated_title
                        print(f"  Translated title to: {translated_title}")
                    else:
                        print(f"  Title translation failed for: {input_file}")
                else:
                    print(f"  Title is not a string, skipping translation for: {input_file}")
            else:
                print(f"  Skipping title translation for {input_file} to {target_language}")
        # Always set lang to target_language
        
        # Determine if the file is a translation
        original_lang = 'en' # Default to english
        if 'lang' in front_matter_dict:
            original_lang = front_matter_dict['lang']
        
        if target_language != original_lang:
            front_matter_dict['lang'] = target_language
            front_matter_dict['translated'] = True
            print(f"  Marked as translated to {target_language} for: {input_file}")
        else:
            front_matter_dict['translated'] = False
            print(f"  Not marked as translated for: {input_file}")
        
        
        result = "---\n" + yaml.dump(front_matter_dict, allow_unicode=True) + "---"
        print(f"  Front matter translation complete for: {input_file}")
        return result
    except yaml.YAMLError as e:
        print(f"  Error parsing front matter: {e}")
        return front_matter

def translate_markdown_file(input_file, output_file, target_language, dry_run=False):
    print(f"  Processing file: {input_file}")
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            content = infile.read()

        # Extract front matter
        front_matter_match = re.match(r'---\n(.*?)\n---', content, re.DOTALL)
        front_matter = front_matter_match.group(1) if front_matter_match else ""
        content_without_front_matter = content[len(front_matter_match.group(0)):] if front_matter_match else content
        
        if not dry_run:
            translated_front_matter = translate_front_matter(front_matter, target_language, input_file)            
            
            special = target_language == "zh" and (
                "resume" in input_file.lower() or 
                "introduction" in input_file.lower() or 
                "Zhiwei" in content_without_front_matter
            )
            translated_content = translate_text(content_without_front_matter, target_language, special=special)
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
    
    languages = ['ja', 'es', 'hi', 'zh', 'en', 'fr', 'de', 'ar', 'hant']

    total_files_to_process = 0
    
    if dry_run:
        changed_files = get_changed_files()
        total_files_to_process = len(changed_files)
        print(f"Total Markdown files to process: {total_files_to_process}")
        return
    
    changed_files = get_changed_files()
    total_files_to_process = len(changed_files)
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = []
        for filename in changed_files:
            input_file = filename
            
            # Check if the file was deleted
            diff_result = subprocess.run(['git', 'diff', 'HEAD~1', 'HEAD', '--', input_file], capture_output=True, text=True)
            if not diff_result.stdout.strip() and "deleted file" in diff_result.stderr:
                print(f"File {input_file} was deleted. Removing translated files.")
                for lang in languages:
                    output_dir = f"_posts/{lang}"
                    output_filename = os.path.basename(filename).replace(".md", f"-{lang}.md")
                    if filename.endswith("-en.md") or filename.endswith("-zh.md"):
                        output_filename = os.path.basename(filename).replace("-en.md", f"-{lang}.md").replace("-zh.md", f"-{lang}.md")
                    output_file = os.path.join(output_dir, output_filename)
                    if os.path.exists(output_file):
                        os.remove(output_file)
                        print(f"  Removed {output_file}")
                continue
            
            with open(input_file, 'r', encoding='utf-8') as infile:
                content = infile.read()
            front_matter_match = re.match(r'---\n(.*?)\n---', content, re.DOTALL)
            front_matter = front_matter_match.group(1) if front_matter_match else ""
            front_matter_dict = {}
            if front_matter:
                front_matter_dict = yaml.safe_load(front_matter)
            original_lang = 'en'
            if 'lang' in front_matter_dict:
                original_lang = front_matter_dict['lang']
            
            
            for lang in languages:
                output_dir = f"_posts/{lang}"
                os.makedirs(output_dir, exist_ok=True)
                
                output_filename = os.path.basename(filename).replace(".md", f"-{lang}.md")
                
                # Check if the original file is named with "-en.md" or "-zh.md"
                if filename.endswith("-en.md") or filename.endswith("-zh.md") or filename.endswith("-hant.md"):
                    output_filename = os.path.basename(filename).replace("-en.md", f"-{lang}.md").replace("-zh.md", f"-{lang}.md").replace("-hant.md", f"-{lang}.md")
                
                output_file = os.path.join(output_dir, output_filename)
                
                if lang == original_lang:
                    # Copy the file and set translated to false
                    with open(input_file, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                    
                    # Modify front matter to set translated: false
                    front_matter_match = re.match(r'---\n(.*?)\n---', content, re.DOTALL)
                    if front_matter_match:
                        front_matter = front_matter_match.group(1)
                        front_matter_dict = yaml.safe_load(front_matter)
                        front_matter_dict['translated'] = False
                        updated_front_matter = yaml.dump(front_matter_dict, sort_keys=False)
                        content = f"---\n{updated_front_matter}---\n{content[front_matter_match.end():]}"
                    else:
                        content = f"---\ntranslated: false\n---\n{content}"

                    with open(output_file, 'w', encoding='utf-8') as outfile:
                        outfile.write(content)
                    print(f"Copied {filename} to {output_file} and set translated: false because target language is the same as original language.")
                    continue
                
                
                print(f"Submitting translation job for {filename} to {lang}...")
                future = executor.submit(translate_markdown_file, input_file, output_file, lang, dry_run)
                futures.append(future)
            
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"A thread failed: {e}")
    print(f"Total Markdown files to process: {total_files_to_process}")

if __name__ == "__main__":
    main()
