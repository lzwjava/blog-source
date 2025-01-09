import os
import re
import time
import argparse
from dotenv import load_dotenv
from openai import OpenAI
import yaml

load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
MODEL_NAME = "deepseek-chat"
INPUT_DIR = "original"
OUTPUT_DIR = "_posts/ja"

client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")


def translate_text(text):
    print(f"  Translating text: {text[:50]}...")
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are a professional translator. You are translating a markdown file for a Jekyll blog post. Translate the following text to Japanese. Do not translate English names. Be careful about code blocks, if not sure, just do not change."},
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

def translate_front_matter(front_matter):
    if not front_matter:
        return ""
    try:
        front_matter_dict = {}
        if front_matter:
            front_matter_dict = yaml.safe_load(front_matter)
        if 'title' in front_matter_dict:
            translated_title = translate_text(front_matter_dict['title'])
            if translated_title:
                front_matter_dict['title'] = translated_title
        # Always set lang to ja
        front_matter_dict['lang'] = 'ja'
        return "---\n" + yaml.dump(front_matter_dict, allow_unicode=True) + "---"
    except yaml.YAMLError as e:
        print(f"  Error parsing front matter: {e}")
        return front_matter


def translate_markdown_file(input_file, output_file):
    print(f"  Processing file: {input_file}")
    with open(input_file, 'r', encoding='utf-8') as infile:
        content = infile.read()

    # Extract front matter
    front_matter_match = re.match(r'---\n(.*?)\n---', content, re.DOTALL)
    front_matter = front_matter_match.group(1) if front_matter_match else ""
    content_without_front_matter = content[len(front_matter_match.group(0)):] if front_matter_match else content
    print(f"  Front matter: {front_matter[:50]}...")

    translated_front_matter = translate_front_matter(front_matter)


    # Split content into paragraphs
    paragraphs = content_without_front_matter.split('\n\n')
    translated_paragraphs = []


    for i, paragraph in enumerate(paragraphs):
        if paragraph.strip():
            print(f"  Translating paragraph {i+1}/{len(paragraphs)}...")
            translated_text = translate_text(paragraph)
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


def main():
    if not DEEPSEEK_API_KEY:
        print("Error: DEEPSEEK_API_KEY is not set in .env file.")
        return

    parser = argparse.ArgumentParser(description="Translate markdown files to Japanese.")
    parser.add_argument("--n", type=int, default=None, help="Maximum number of files to translate.")
    args = parser.parse_args()
    max_files = args.n


    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Created directory {OUTPUT_DIR}")

    translated_count = 0
    for filename in os.listdir(INPUT_DIR):
        if max_files is not None and translated_count >= max_files:
            print(f"Reached max files limit: {max_files}. Stopping translation.")
            break
        if filename.endswith(".md"):
            input_file = os.path.join(INPUT_DIR, filename)
            output_filename = filename.replace(".md", "-ja.md")
            
            # Check if the original file is named with "-en.md" or "-zh.md"
            if filename.endswith("-en.md") or filename.endswith("-zh.md"):
                output_filename = filename.replace("-en.md", "-ja.md").replace("-zh.md", "-ja.md")
            
            output_file = os.path.join(OUTPUT_DIR, output_filename)
            if not os.path.exists(output_file):
                print(f"Translating {filename}...")
                translate_markdown_file(input_file, output_file)
                print(f"Translated {filename} to {output_file}")
                translated_count += 1
            else:
                print(f"Skipping {filename} because {output_file} already exists.")

if __name__ == "__main__":
    main()
