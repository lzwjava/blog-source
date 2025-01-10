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
INPUT_DIR = "."
MAX_THREADS = 3

client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")


def create_translation_prompt(target_language):
    if target_language == 'ja':
        return "You are a professional translator. You are translating a LaTeX file. Translate the following text to Japanese. Do not translate English names or LaTeX commands. Be careful about code blocks, if not sure, just do not change."
    elif target_language == 'es':
        return "You are a professional translator. You are translating a LaTeX file. Translate the following text to Spanish. Do not translate English names or LaTeX commands. Be careful about code blocks, if not sure, just do not change."
    elif target_language == 'hi':
        return "You are a professional translator. You are translating a LaTeX file. Translate the following text to Hindi. Do not translate English names or LaTeX commands. Be careful about code blocks, if not sure, just do not change."
    elif target_language == 'fr':
         return "You are a professional translator. You are translating a LaTeX file. Translate the following text to French. Do not translate English names or LaTeX commands. Be careful about code blocks, if not sure, just do not change."
    else:
        return f"You are a professional translator. You are translating a LaTeX file. Translate the following text to {target_language}. Do not translate English names or LaTeX commands. Be careful about code blocks, if not sure, just do not change."


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


def translate_latex_file(input_file, output_file, target_language):
    print(f"  Processing file: {input_file}")
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            content = infile.read()

        translated_content = translate_text(content, target_language)

        if translated_content:
            with open(output_file, 'w', encoding='utf-8') as outfile:
                outfile.write(translated_content)
            print(f"  Finished processing file: {output_file}")
        else:
            print(f"  Translation failed for {input_file}")
    except Exception as e:
        print(f"  Error processing file {input_file}: {e}")


def main():
    if not DEEPSEEK_API_KEY:
        print("Error: DEEPSEEK_API_KEY is not set in .env file.")
        return

    parser = argparse.ArgumentParser(description="Translate LaTeX files to a specified language.")
    parser.add_argument("--lang", type=str, default="ja", help="Target language for translation (e.g., ja, es).")
    parser.add_argument("--input_dir", type=str, default=".", help="Input directory containing LaTeX files.")
    args = parser.parse_args()
    target_language = args.lang
    input_dir = args.input_dir
            
    files_to_translate = []
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".tex"):
                files_to_translate.append(os.path.join(root, file))
    
    if not files_to_translate:
        print(f"No .tex files found in {input_dir}")
        return
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = []
        for filename in files_to_translate:
            if os.path.exists(filename):
                output_dir = os.path.dirname(filename)
                output_filename = os.path.basename(filename).replace(".tex", f"-{target_language}.tex")
                
                base_name = os.path.basename(filename).replace('.tex', '')
                output_dir = os.path.join(output_dir, f"{base_name}-{target_language}")
                os.makedirs(output_dir, exist_ok=True)
                output_file = os.path.join(output_dir, output_filename)
                
                print(f"Submitting translation job for {filename}...")
                future = executor.submit(translate_latex_file, filename, output_file, target_language)
                futures.append(future)
            else:
                print(f"Skipping {filename} because it does not exist.")
        
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"A thread failed: {e}")


if __name__ == "__main__":
    main()
