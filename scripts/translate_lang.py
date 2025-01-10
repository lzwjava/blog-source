import os
import re
import time
import argparse
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
    elif target_language == 'fr':
        return "You are a professional translator. You are translating a markdown file for a Jekyll blog post. Translate the following text to French. Do not translate English names. Be careful about code blocks, if not sure, just do not change."
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


def translate_markdown_file(input_file, output_file, target_language):
    print(f"  Processing file: {input_file}")
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            content = infile.read()

        # Extract front matter
        front_matter_match = re.match(r'---\n(.*?)\n---', content, re.DOTALL)
        front_matter = front_matter_match.group(1) if front_matter_match else ""
        content_without_front_matter = content[len(front_matter_match.group(0)):] if front_matter_match else content
        print(f"  Front matter: {front_matter[:50]}...")

        translated_front_matter = translate_front_matter(front_matter, target_language)


        # Split content into paragraphs
        paragraphs = content_without_front_matter.split('\n\n')
        translated_paragraphs = []


        for i, paragraph in enumerate(paragraphs):
            if paragraph.strip():
                print(f"  Translating paragraph {i+1}/{len(paragraphs)}...")
                translated_text = translate_text(paragraph, target_language)
                if translated_text:
                    translated_paragraphs.append(translated_text)
                else:
                    translated_paragraphs.append(paragraph)
                time.sleep(1) # Add a delay to avoid rate limiting
            else:
                translated_paragraphs.append("")


        translated_content = "\n\n".join(translated_paragraphs)
        translated_content = translated_front_matter + translated_content

        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(translated_content)
        print(f"  Finished processing file: {output_file}")
    except Exception as e:
        print(f"  Error processing file {input_file}: {e}")


def main():
    if not DEEPSEEK_API_KEY:
        print("Error: DEEPSEEK_API_KEY is not set in .env file.")
        return

    parser = argparse.ArgumentParser(description="Translate markdown files to a specified language.")
    parser.add_argument("--n", type=int, default=None, help="Maximum number of files to translate.")
    parser.add_argument("--lang", type=str, default="ja", help="Target language for translation (e.g., ja, es).")
    args = parser.parse_args()
    max_files = args.n
    target_language = args.lang
    
    output_dir = f"_posts/{target_language}"
    if target_language == 'hi':
        output_dir = "_posts/hi"
    os.makedirs(output_dir, exist_ok=True)
    print(f"Created directory {output_dir}")

    
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        translated_count = 0
        futures = []
        for filename in os.listdir(INPUT_DIR):
            if max_files is not None and translated_count >= max_files:
                print(f"Reached max files limit: {max_files}. Stopping translation.")
                break
            if filename.endswith(".md"):
                input_file = os.path.join(INPUT_DIR, filename)
                output_filename = filename.replace(".md", f"-{target_language}.md")
                
                # Check if the original file is named with "-en.md" or "-zh.md"
                if filename.endswith("-en.md") or filename.endswith("-zh.md"):
                    output_filename = filename.replace("-en.md", f"-{target_language}.md").replace("-zh.md", f"-{target_language}.md")
                
                output_file = os.path.join(output_dir, output_filename)
                if not os.path.exists(output_file):
                    print(f"Submitting translation job for {filename}...")
                    future = executor.submit(translate_markdown_file, input_file, output_file, target_language)
                    futures.append(future)
                    translated_count += 1
                else:
                    print(f"Skipping {filename} because {output_file} already exists.")
        
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"A thread failed: {e}")


if __name__ == "__main__":
    main()
