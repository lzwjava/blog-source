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
MAX_THREADS = 10

client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")

def create_x_post_prompt(target_language):
    if target_language == "zh":
        return f"""You are a professional social media content creator. You are creating a short post for X (formerly Twitter) based on a blog post written in English. The post should be no more than 140 characters. Translate Zhiwei Li to 李智维. Translate Meitai Technology Services to 美钛技术服务. Translate Neusiri to 思芮 instead of 纽思瑞. Translate Chongding Conference to 冲顶大会. Translate Fun Live to 趣直播. Translate MianbaoLive to 面包Live. Translate Beijing Dami Entertainment Co. to 北京大米互娱有限公司. Translate Guangzhou Yuyan Middle School to 广州玉岩中学. Be concise and engaging."""
    elif target_language == "hant":
        return f"You are a professional social media content creator. You are creating a short post for X (formerly Twitter) based on a blog post written in English. The post should be no more than 140 characters. Translate the following text to Traditional Chinese (Hong Kong). Be concise and engaging."
    elif target_language == 'ja':
        return "You are a professional social media content creator. You are creating a short post for X (formerly Twitter) based on a blog post written in English. The post should be no more than 140 characters. Translate the following text to Japanese. Be concise and engaging."
    elif target_language == 'es':
        return "You are a professional social media content creator. You are creating a short post for X (formerly Twitter) based on a blog post written in English. The post should be no more than 140 characters. Translate the following text to Spanish. Be concise and engaging."
    elif target_language == 'hi':
        return "You are a professional social media content creator. You are creating a short post for X (formerly Twitter) based on a blog post written in English. The post should be no more than 140 characters. Translate the following text to Hindi. Be concise and engaging."
    elif target_language == 'fr':
        return "You are a professional social media content creator. You are creating a short post for X (formerly Twitter) based on a blog post written in English. The post should be no more than 140 characters. Translate the following text to French. Be concise and engaging."
    elif target_language == 'de':
        return "You are a professional social media content creator. You are creating a short post for X (formerly Twitter) based on a blog post written in English. The post should be no more than 140 characters. Translate the following text to German. Be concise and engaging."
    elif target_language == 'ar':
        return "You are a professional social media content creator. You are creating a short post for X (formerly Twitter) based on a blog post written in English. The post should be no more than 140 characters. Translate the following text to Arabic. Be concise and engaging."
    else:
        return f"You are a professional social media content creator. You are creating a short post for X (formerly Twitter) based on a blog post written in English. The post should be no more than 140 characters. Generate a post in {target_language}. Be concise and engaging."


def generate_x_post(text, target_language):
    print(f"  Generating X post: {text[:50]}...")
    prompt = create_x_post_prompt(target_language)
    print(f"  Prompt: {prompt}")
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": text}
            ],
            stream=False
        )
        if response and response.choices:
            print(f"  X post generated successfully.")
            return response.choices[0].message.content
        else:
            print(f"  X post generation failed.")
            return None
    except Exception as e:
        print(f"  X post generation failed with error: {e}")
        if "This model's maximum context length is" in str(e):
            print(f"  Skipping X post generation due to context length error.")
            return None
        return None


def generate_x_post_from_markdown_file(input_file, output_file, target_language):
    print(f"  Processing file: {input_file}")
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            content = infile.read()

        # Extract front matter
        front_matter_match = re.match(r'---\n(.*?)\n---', content, re.DOTALL)
        content_without_front_matter = content[len(front_matter_match.group(0)):] if front_matter_match else content
        print(f"  Content: {content_without_front_matter[:50]}...")

        x_post_content = generate_x_post(content_without_front_matter, target_language)
        if x_post_content:
            with open(output_file, 'w', encoding='utf-8') as outfile:
                outfile.write(x_post_content)
            print(f"  Finished processing file: {output_file}")
        else:
            print(f"  X post generation failed for {input_file}")
    except Exception as e:
        print(f"  Error processing file {input_file}: {e}")


def main():
    if not DEEPSEEK_API_KEY:
        print("Error: DEEPSEEK_API_KEY is not set in .env file.")
        return

    parser = argparse.ArgumentParser(description="Generate X posts from markdown files.")
    parser.add_argument("--n", type=int, default=None, help="Maximum number of files to process.")
    parser.add_argument("--lang", type=str, default="ja", help="Target language for X post (e.g., ja, es).")
    args = parser.parse_args()
    max_files = args.n
    target_language = args.lang

    output_dir = f"x/{target_language}"
    if target_language == 'hi':
        output_dir = "x/hi"
    os.makedirs(output_dir, exist_ok=True)
    print(f"Created directory {output_dir}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        processed_count = 0
        futures = []
        for filename in os.listdir(INPUT_DIR):
            if max_files is not None and processed_count >= max_files:
                print(f"Reached max files limit: {max_files}. Stopping X post generation.")
                break
            if filename.endswith(".md"):
                input_file = os.path.join(INPUT_DIR, filename)
                output_filename = filename.replace(".md", f"-{target_language}.txt")

                # Check if the original file is named with "-en.md" or "-zh.md"
                if filename.endswith("-en.md") or filename.endswith("-zh.md"):
                    output_filename = filename.replace("-en.md", f"-{target_language}.txt").replace("-zh.md", f"-{target_language}.txt")

                output_file = os.path.join(output_dir, output_filename)
                if not os.path.exists(output_file):
                    print(f"Submitting X post generation job for {filename}...")
                    future = executor.submit(generate_x_post_from_markdown_file, input_file, output_file, target_language)
                    futures.append(future)
                    processed_count += 1
                else:
                    print(f"Skipping {filename} because {output_file} already exists.")

        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"A thread failed: {e}")

if __name__ == "__main__":
    main()
