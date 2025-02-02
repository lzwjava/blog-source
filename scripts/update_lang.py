import os
import re
import time
import argparse
import subprocess
import json
import requests
from dotenv import load_dotenv
import yaml
import concurrent.futures
import traceback
import copy

load_dotenv()


GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
MODEL_NAME = "deepseek-chat"
INPUT_DIR = "original"
MAX_THREADS = 10
DEEPSEEK_API_URL = "https://api.deepseek.com/chat/completions"
MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"


def create_translation_prompt(target_language, type="content", special=False):
    if type == "title":
        base_prompt = "Translate the following title to {target_language}. Provide only the translated title, without any additional notes or explanations. Do not repeat or mention the input text.\n"
    else:
        base_prompt = "Translate the following markdown text to {target_language}. Provide only the translated output, without any additional notes or explanations.\n"
    if target_language == 'ja':
        return base_prompt.format(target_language="Japanese")
    elif target_language == 'es':
        return base_prompt.format(target_language="Spanish")
    elif target_language == 'hi':
        return base_prompt.format(target_language="Hindi")
    elif target_language == 'fr':
        return base_prompt.format(target_language="French")
    elif target_language == "zh":
        return base_prompt.format(target_language="Simplified Chinese")
    elif target_language == 'hant':
        return base_prompt.format(target_language="Traditional Chinese (Hong Kong)")
    elif target_language == 'en':
        return base_prompt.format(target_language="English")
    elif target_language == 'de':
        return base_prompt.format(target_language="German")
    elif target_language == 'ar':
        return base_prompt.format(target_language="Arabic")
    else:
        return base_prompt.format(target_language=target_language)

def call_mistral_api(prompt):
    api_key = MISTRAL_API_KEY
    if not api_key:
        print("Error: MISTRAL_API_KEY environment variable not set.")
        return None
    
    url = MISTRAL_API_URL
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "mistral-small-latest",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    try:
        # print(f"Mistral API Request: {data}")
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        # print(f"Mistral API Response: {response_json}")

        if response_json and response_json['choices']:
            content = response_json['choices'][0]['message']['content']
            return content
        else:
            print(f"Mistral API Error: Invalid response format: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Mistral API Error: {e}")
        if e.response:
            print(f"Response status code: {e.response.status_code}")
            print(f"Response content: {e.response.text}")
        return None

def call_gemini_api(prompt):
    api_key = GEMINI_API_KEY
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        return None
    
    url = f"{GEMINI_API_URL}?key={api_key}"
    headers = {'Content-Type': 'application/json'}
    data = {
      "contents": [{
        "parts":[{"text": prompt}]
        }]
       }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raise an exception for bad status codes
        
        json_response = response.json()
        
        if 'candidates' in json_response and json_response['candidates']:
            first_candidate = json_response['candidates'][0]
            if 'content' in first_candidate and 'parts' in first_candidate['content']:
                first_part = first_candidate['content']['parts'][0]
                if 'text' in first_part:
                    return first_part['text']
                else:
                    print("No text found in the response")
                    return None
            else:
                print("Unexpected response format: content or parts missing")
                return None
        else:
            print("No candidates found in the response")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error during Gemini API request: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        return None


def translate_text(text, target_language, type="content", special=False, model="deepseek"):
    if not text or not text.strip():
        return ""
    if target_language == 'en':
        print(f"  Skipping translation for English: {text[:50]}...")
        return text.strip()
    print(f"  Translating text: {text[:50]}...")
    
    if model == "deepseek":
        try:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
            }
            data = {
                "model": MODEL_NAME,
                "messages": [
                    {"role": "system", "content": create_translation_prompt(target_language, type, special)},
                    {"role": "user", "content": text}
                ],
                "stream": False
            }
            response = requests.post(DEEPSEEK_API_URL, headers=headers, json=data)        
            response.raise_for_status()
            response_json = response.json()
            if not response_json or not response_json.get('choices') or not response_json['choices'][0]['message']['content']:
                print(f"  Error: Translation response is empty or invalid:")
                print(response.content)
                return None
            
            if response_json['choices'][0].get('finish_reason') != "stop":
                print(f"  Error: Translation did not finish with 'stop' reason:")
                print(response.content)
                return None
            
            translated_text = response_json['choices'][0]['message']['content']
            return translated_text
        except requests.exceptions.RequestException as e:
            print(f"  Translation failed with error: {e}")
            traceback.print_exc()
            if response and response.content:
                print(f"  Response content: {response.content}")
            else:
                print("  Response content is empty.")
            return None
    elif model == "mistral":
        prompt = create_translation_prompt(target_language, type, special) + "\n\n" + text
        translated_text = call_mistral_api(prompt)
        return translated_text
    elif model == "gemini":
        prompt = create_translation_prompt(target_language, type, special) + "\n\n" + text
        translated_text = call_gemini_api(prompt)
        return translated_text
    else:
        print(f"  Error: Invalid model specified: {model}")
        return None


def translate_front_matter(front_matter, target_language, input_file, model="deepseek"):
    print(f"  Translating front matter for: {input_file}")
    if not front_matter:
        print(f"  No front matter found for: {input_file}")
        return ""
    try:
        front_matter_dict = {}
        if front_matter:
            front_matter_dict = yaml.safe_load(front_matter)
            print(f"  Front matter after safe_load: {front_matter_dict}")
        
        front_matter_dict_copy = copy.deepcopy(front_matter_dict)
        
        if 'title' in front_matter_dict_copy:
            print(f"  Translating title: {front_matter_dict_copy['title']}")
            translated_title = translate_text(front_matter_dict_copy['title'], target_language, type="title", model=model)
            if translated_title:
                translated_title = translated_title.strip()
                
                front_matter_dict_copy['title'] = translated_title
                print(f"  Translated title to: {translated_title}")
            else:
                print(f"  Title translation failed for: {input_file}")
        else:
            print(f"  Skipping title translation for {input_file} to {target_language}")
        # Always set lang to target_language
 
        front_matter_dict_copy['lang'] = target_language        
        front_matter_dict_copy['translated'] = target_language != 'en'
        
        audio_file = os.path.join("assets/audios/", os.path.basename(input_file).replace("-en", f"-{target_language}").replace("-zh", f"-{target_language}").replace(".md", ".mp3"))
        if os.path.exists(audio_file):
            front_matter_dict_copy['audio'] = True
        else:
            front_matter_dict_copy['audio'] = False

        result = "---\n" + yaml.dump(front_matter_dict_copy, allow_unicode=True) + "---"
        print(f"  Front matter translation complete for: {input_file}")
        return result
    except yaml.YAMLError as e:
        print(f"  Error parsing front matter: {e}")
        return front_matter

def translate_markdown_file(input_file, output_file, target_language, model="deepseek"):
    print(f"  Processing file: {input_file}")
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            content = infile.read()

        # Extract front matter
        front_matter_match = re.match(r'---\n(.*?)\n---', content, re.DOTALL)
        if front_matter_match:
            front_matter = front_matter_match.group(1)
        else:
            raise Exception("No front matter found in markdown file")
        content_without_front_matter = content[len(front_matter_match.group(0)):] if front_matter_match else content

        print(f"front_matter_match: {front_matter_match}")
        print(f"front_matter: {front_matter}")
        
        translated_front_matter = translate_front_matter(front_matter, target_language, input_file, model=model)            
        
        special = target_language == "zh" and (
            "resume" in input_file.lower() or 
            "introduction" in input_file.lower() or 
            "Zhiwei" in content_without_front_matter
        )
        translated_content = translate_text(content_without_front_matter, target_language, special=special, model=model)
        # print(f"  Translated content: {translated_content}")
        if translated_content:
            translated_content = translated_front_matter + "\n\n" + translated_content
        else:
            raise Exception(f"Translation failed for: {input_file}")
        
        if os.path.exists(output_file):
            os.remove(output_file)
            
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(translated_content)
        print(f"  Finished processing file: {output_file}")
    except Exception as e:
        print(f"  Error processing file {input_file}: {e}")

def get_changed_files():
    changed_files = set()
    languages = ['ja', 'es', 'hi', 'zh', 'en', 'fr', 'de', 'ar', 'hant']

    # First pass: Check for missing translations
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".md"):
            input_file = os.path.join(INPUT_DIR, filename)
            for target_lang in languages:         
                output_dir = f"_posts/{target_lang}"
                if filename.endswith("-en.md"):
                    output_filename = filename.replace("-en.md", f"-{target_lang}.md")
                elif filename.endswith("-zh.md"):
                    output_filename = filename.replace("-zh.md", f"-{target_lang}.md")
                else:
                    raise Exception(f"Unexpected filename format: {filename}")
                output_file = os.path.join(output_dir, output_filename)
                if not os.path.exists(output_file):
                    changed_files.add((input_file, target_lang))
                    print(f"  File {input_file} is missing translation for {target_lang}")

    # Second pass: Check for content changes
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".md"):
            input_file = os.path.join(INPUT_DIR, filename)
            try:
                with open(input_file, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                front_matter_match = re.match(r'---(.*?)---', content, re.DOTALL)
                if not front_matter_match:
                    raise Exception(f"No front matter found in markdown file: {input_file}")
                front_matter = front_matter_match.group(1)
                content_without_front_matter = content[len(front_matter_match.group(0)):] if front_matter_match else content
                front_matter_dict = yaml.safe_load(front_matter) if front_matter else {}
                original_title = front_matter_dict.get('title', '')
                original_lang = front_matter_dict.get('lang', 'en')
                
                output_dir = f"_posts/{original_lang}"
                output_filename = filename
                output_file = os.path.join(output_dir, output_filename)

                if not os.path.exists(output_file):
                    for target_lang in languages:           
                        output_dir = f"_posts/{target_lang}"
                        if filename.endswith("-en.md"):
                            output_filename = filename.replace("-en.md", f"-{target_lang}.md")
                        elif filename.endswith("-zh.md"):
                            output_filename = filename.replace("-zh.md", f"-{target_lang}.md")
                        else:
                            raise Exception(f"Unexpected filename format: {filename}")
                        output_file = os.path.join(output_dir, output_filename)
                        if not os.path.exists(output_file):
                            changed_files.add((input_file, target_lang))
                            print(f"  File {input_file} is missing translation for {target_lang}")
                else:                
                    with open(output_file, 'r', encoding='utf-8') as translated_infile:
                        translated_content = translated_infile.read()
                    
                    target_front_matter_match = re.match(r'---\n(.*?)\n---', translated_content, re.DOTALL)
                    translated_front_matter = target_front_matter_match.group(1) if target_front_matter_match else ""
                    translated_content_without_front_matter = translated_content[len(target_front_matter_match.group(0)):] if target_front_matter_match else translated_content
                    translated_front_matter_dict = yaml.safe_load(translated_front_matter) if translated_front_matter else {}
                    translated_title = translated_front_matter_dict.get('title', '')
                    
                    if translated_title != original_title or translated_content_without_front_matter.strip() != content_without_front_matter.strip():                        
                        for target_lang in languages:
                            changed_files.add((input_file, target_lang))
                            print(f"  File {input_file} needs update for {target_lang} due to content change")
                        try:
                            diff_command = ["diff", input_file, output_file]
                            process = subprocess.Popen(diff_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                            stdout, stderr = process.communicate()

                            if process.returncode == 1 and len(stdout) > 0:
                                print(f"  Diff:\n{stdout}")
                            else:
                                print(f"  Diff:\n{stdout}")                                
                                print(f"  Diff command failed with error: {stderr}")
                                print(f"  No diff available for {input_file} and {output_file}")
                        except FileNotFoundError:
                            print(f"  Diff command not found.")
                        except Exception as e:
                            print(f"  Error generating diff for {input_file}: {e}")
            except Exception as e:
                print(f"Error processing file {input_file}: {e}")
    return changed_files


def main():
    if not DEEPSEEK_API_KEY and not MISTRAL_API_KEY and not GEMINI_API_KEY:
        print("Error: DEEPSEEK_API_KEY, MISTRAL_API_KEY or GEMINI_API_KEY is not set in .env file.")
        return

    parser = argparse.ArgumentParser(description="Translate markdown files to a specified language.")
    parser.add_argument("--lang", type=str, default="all", help="Target language for translation (e.g., ja, es, all).")
    parser.add_argument("--dry_run", action="store_true", help="Perform a dry run without modifying files.")
    parser.add_argument("--file", type=str, default=None, help="Specific file to translate.")
    parser.add_argument("--max_files", type=int, default=None, help="Maximum number of files to process.")
    parser.add_argument("--model", type=str, default="deepseek", help="Model to use for translation (deepseek or mistral).")
    args = parser.parse_args()
    target_language = args.lang
    dry_run = args.dry_run
    input_file = args.file
    max_files = args.max_files
    model = args.model
    
    if target_language == "all":
        languages = ['ja', 'es', 'hi', 'zh', 'en', 'fr', 'de', 'ar', 'hant']
    else:
        languages = [target_language]
    
    if input_file:
        changed_files = {(input_file, lang) for lang in languages}
        total_files_to_process = len(changed_files)
    else:
        changed_files = get_changed_files()
        if max_files and len(changed_files) > max_files:
            changed_files = set(list(changed_files)[:max_files])
        total_files_to_process = len(changed_files)
    
    if dry_run:
        print(f"Total Markdown files to process: {total_files_to_process}")
        return
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = []
        for filename, lang in changed_files:
            input_file = filename
            
            output_dir = f"_posts/{lang}"
            os.makedirs(output_dir, exist_ok=True)

            output_filename = os.path.basename(filename).replace("-en.md", f"-{lang}.md").replace("-zh.md", f"-{lang}.md")
    
            output_file = os.path.join(output_dir, output_filename)
                            
            print(f"Submitting translation job for {filename} to {lang}...")
            future = executor.submit(translate_markdown_file, input_file, output_file, lang, model)
            futures.append(future)
            
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"A thread failed: {e}")
    print(f"Total Markdown files to process: {total_files_to_process}")

if __name__ == "__main__":
    main()
