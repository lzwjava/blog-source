import os
import re
import boto3
import json
import mistune


class TranslateRenderer(mistune.Renderer):
    def __init__(self, translator):
        super().__init__()
        self.translator = translator

    def translate_text(self, text):
        if contains_chinese(text):
            translated_text = self.translator.translate_text(text)
            # Log a snippet of the text being translated
            print(f"Translating text: {text[:60]}...")
            return translated_text
        return text

    def text(self, text):
        return self.translate_text(text)

    def paragraph(self, text):
        return self.translate_text(text) + "\n"

    def block_code(self, code, lang=None):
        lang_str = f"{lang}" if lang else ""
        return f"```{lang_str}\n{code}\n```\n"

    def block_html(self, html):
        return html

    def block_quote(self, text):
        return f"> {self.translate_text(text)}\n"

    def header(self, text, level, raw=None):
        return f"{'#' * level} {self.translate_text(text)}\n"

    def list(self, body, ordered=True):
        return body

    def list_item(self, text, ordered=True):
        return f"{self.translate_text(text)}"

    def emphasis(self, text):
        return f"*{self.translate_text(text)}*"

    def strong(self, text):
        return f"**{self.translate_text(text)}**"

    def codespan(self, text):
        return f"`{text}`"

    def linebreak(self):
        return "\n"

    def thematic_break(self):
        return "\n---\n"

    def link(self, link, title, text):
        return f"[{self.translate_text(text)}]({link})"

    def image(self, src, title, text):
        return f"![{self.translate_text(text)}]({src})"


class Translator:
    def __init__(self):
        self.session = boto3.Session(region_name='us-east-1')
        self.bedrock_runtime = self.session.client('bedrock-runtime')
        self.model_id = 'meta.llama3-70b-instruct-v1:0'

    def translate_text(self, text):
        body = {
            'prompt': f'<s>[INST]Translate the following Chinese text to English. Provide only the English translation without any additional text or introduction: {text}[/INST]</s>'
        }

        response = self.bedrock_runtime.invoke_model(
            modelId=self.model_id,
            body=json.dumps(body),
            contentType='application/json'
        )

        # Read the content from the StreamingBody
        response_body = response['body'].read().decode('utf-8')
        output = json.loads(response_body)
        print(response_body)

        # Extract the text from the response
        extracted_text = output.get('generation', 'Translation Error')
        # Log a snippet of the translation
        print(f"Received translation: {extracted_text[:60]}...")
        return extracted_text


def contains_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff]', text))


def translate_markdown_file(input_file, output_file, translator):
    print(f"Translating file: {input_file}")
    with open(input_file, 'r', encoding='utf-8') as infile:
        content = infile.read()

    renderer = TranslateRenderer(translator)
    markdown = mistune.Markdown(renderer=renderer)
    translated_content = markdown(content)

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(translated_content)
    print(f"Saved translated markdown to {output_file}")


def translate_files_in_directory(directory):
    translator = Translator()
    filenames = sorted(os.listdir(directory))  # Sort filenames
    for filename in filenames:
        if filename.endswith('-en.md'):
            en_file_path = os.path.join(directory, filename)
            with open(en_file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                if "*This blog post was translated by Mistral*" in content:
                    cn_file_path = en_file_path.replace('-en.md', '-cn.md')
                    if os.path.exists(cn_file_path):
                        print(f"Found matching -cn.md file: {cn_file_path}")
                        translate_markdown_file(
                            cn_file_path, en_file_path, translator)
                    else:
                        print(
                            f"Matching -cn.md file not found for: {en_file_path}")
                else:
                    print(f"Skipping file (no Mistral text): {en_file_path}")


# Define the directory containing the markdown posts
base_directory = "/Users/lzwjava/projects/lzwjava.github.io"
posts_directory = os.path.join(base_directory, '_posts')

# Run the function to translate files
translate_files_in_directory(posts_directory)
