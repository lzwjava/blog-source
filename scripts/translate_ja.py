import os
import re
import time
import json
from dotenv import load_dotenv
from openai import OpenAI
import yaml

load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
MODEL_NAME = "deepseek-chat"
INPUT_DIR = "_posts/original"
OUTPUT_DIR = "_posts/ja"
PROGRESS_FILE = "progress_ja.json"

client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")


def translate_text(text):
    print(f"  Translating text: {text[:50]}...")
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are a professional translator. Translate the following text to Japanese."},
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
        front_matter_dict = yaml.safe_load(front_matter)
        if 'title' in front_matter_dict:
            translated_title = translate_text(front_matter_dict['title'])
            if translated_title:
                front_matter_dict['title'] = translated_title
        return "---\n" + yaml.dump(front_matter_dict, allow_unicode=True) + "---"
    except yaml.YAMLError as e:
        print(f"  Error parsing front matter: {e}")
        return front_matter


def translate_markdown_file(input_file, output_file, progress):
    print(f"  Processing file: {input_file}")
    with open(input_file, 'r', encoding='utf-8') as infile:
        content = infile.read()

    # Extract front matter
    front_matter_match = re.match(r'---\n(.*?)\n---', content, re.DOTALL)
    front_matter = front_matter_match.group(0) if front_matter_match else ""
    content_without_front_matter = content[len(front_matter):] if front_matter else content
    print(f"  Front matter: {front_matter[:50]}...")

    translated_front_matter = translate_front_matter(front_matter)


    # Split content into paragraphs
    paragraphs = content_without_front_matter.split('\n\n')
    translated_paragraphs = []

    start_paragraph = progress.get(input_file, 0)
    for i, paragraph in enumerate(paragraphs):
        if i < start_paragraph:
            translated_paragraphs.append(progress.get(f"{input_file}_para_{i}", ""))
            continue
        if paragraph.strip():
            print(f"  Translating paragraph {i+1}/{len(paragraphs)}...")
            translated_text = translate_text(paragraph)
            if translated_text:
                translated_paragraphs.append(translated_text)
                progress[f"{input_file}_para_{i}"] = translated_text
            else:
                translated_paragraphs.append(paragraph)
                progress[f"{input_file}_para_{i}"] = paragraph
            time.sleep(1) # Add a delay to avoid rate limiting
        else:
            translated_paragraphs.append("")
        progress[input_file] = i + 1
        save_progress(progress)

    translated_content = "\n\n".join(translated_paragraphs)
    translated_content = translated_front_matter + translated_content

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(translated_content)
    print(f"  Finished processing file: {output_file}")

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_progress(progress):
    with open(PROGRESS_FILE, 'w') as f:
        json.dump(progress, f, indent=4)

def main():
    if not DEEPSEEK_API_KEY:
        print("Error: DEEPSEEK_API_KEY is not set in .env file.")
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Created directory {OUTPUT_DIR}")

    progress = load_progress()

    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".md"):
            input_file = os.path.join(INPUT_DIR, filename)
            output_file = os.path.join(OUTPUT_DIR, filename)
            print(f"Translating {filename}...")
            translate_markdown_file(input_file, output_file, progress)
            print(f"Translated {filename} to {output_file}")

if __name__ == "__main__":
    main()
