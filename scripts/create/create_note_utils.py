import os
import sys
import re
import datetime
import pyperclip

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from scripts.llm.openrouter_client import call_openrouter_api, MODEL_MAPPING


def get_first_n_words(text, n=500):
    words = text.split()
    return " ".join(words[:n])


def process_title_for_filename(title):
    title = title.strip()
    title = re.sub(r"\s+", "-", title)
    title = re.sub(r"[^a-zA-Z0-9-]", "", title)  # Remove special characters
    title = title.lower()
    return title


def clean_grok_tags(content):
    if "<grok:render" in content:
        prompt = f"""Remove all <grok:render> tags and their contents from the following text, and format the text cleanly by removing extra spaces and ensuring proper sentence spacing. Respond with only the cleaned text:

{content}"""
        cleaned_content = call_openrouter_api(prompt)
        if not cleaned_content:
            print("Failed to clean grok tags. Using original content.")
            return content
        return cleaned_content.strip()
    return content


def get_clipboard_content():
    content = pyperclip.paste()
    if len(content.strip()) < 100:
        print("Clipboard content is less than 100 characters. Aborting.")
        sys.exit(1)
    if not content.strip():
        print("Clipboard is empty. Nothing to create.")
        sys.exit(1)
    return content


def generate_title(content, max_words, format_prompt):
    prompt_content = get_first_n_words(content)
    prompt = format_prompt(prompt_content)
    title = call_openrouter_api(prompt)
    if not title:
        print(f"Failed to generate title with max {max_words} words. Exit.")
        sys.exit(1)
    title = re.sub(r"\*", " ", title).strip()
    return title

def generate_short_title(prompt):
    title = call_openrouter_api(prompt)
    if not title:
        print(f"Failed to generate short title. Exit.")
        sys.exit(1)
    return title

def create_filename(short_title, notes_dir="notes"):
    today = datetime.date.today()
    date_str = today.strftime("%Y-%m-%d")
    if not os.path.exists(notes_dir):
        os.makedirs(notes_dir)
    base_file_name = f"{date_str}-{short_title}-en.md"
    file_path = os.path.join(notes_dir, base_file_name)
    counter = 1
    while os.path.exists(file_path):
        file_path = os.path.join(notes_dir, f"{date_str}-{short_title}-{counter}-en.md")
        counter += 1
    return file_path


def format_front_matter(full_title, note_model_key: str, date=None):
    if ":" in full_title and '"' not in full_title:
        full_title = f'"{full_title}"'
    if date is None:
        date = datetime.date.today().strftime("%Y-%m-%d")
    # Map simple key to provider/model form for annotation in frontmatter
    if note_model_key not in MODEL_MAPPING:
        raise ValueError(f"Unknown model key '{note_model_key}'. Valid keys: {', '.join(sorted(MODEL_MAPPING.keys()))}")
    model_full = MODEL_MAPPING[note_model_key]
    return f"""---
title: {full_title}
lang: en
layout: post
audio: false
translated: false
generated: true
image: false
model: {model_full}
---"""


def clean_content(content):
    lines = content.splitlines()
    if lines and lines[0].startswith("# "):
        content = "\n".join(lines[1:])
    return content.strip()


def write_note(file_path, front_matter, content):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(front_matter + "\n\n" + content)
    print(f"Created note: {file_path}")
