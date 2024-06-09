import os
import boto3
import json


def create_prompt(text, target_language):
    if target_language == 'en':
        return f'<s>[INST]Translate the following Chinese text to English, and provide only the English translation without any Chinese characters or punctuation: {text}[/INST]</s>'
    else:
        return f'<s>[INST]Translate the following English text to Chinese, and provide only the Chinese translation without any English characters or punctuation: {text}[/INST]</s>'


def translate_text(text, target_language):
    session = boto3.Session(region_name='us-east-1')
    bedrock_runtime = session.client('bedrock-runtime')

    prompt = create_prompt(text, target_language)

    body = {
        'prompt': prompt,
        'max_tokens': 4096,
        'top_k': 50,
        'top_p': 0.7,
        'temperature': 0.7
    }

    response = bedrock_runtime.invoke_model(
        modelId='mistral.mistral-7b-instruct-v0:2',
        body=json.dumps(body),
        contentType='application/json'
    )

    response_body = response['body'].read().decode('utf-8')
    output = json.loads(response_body)

    extracted_text = output['outputs'][0]['text']
    return extracted_text


def read_and_translate(input_file, output_file, target_language):
    with open(input_file, 'r') as infile, open(output_file, 'a') as outfile:
        lines = []
        for line in infile:
            lines.append(line)
            if len(lines) == 10:
                text_to_translate = "".join(lines)
                translated_chunk = translate_text(
                    text_to_translate, target_language)
                outfile.write(translated_chunk)
                lines = []

        if lines:
            text_to_translate = "\n".join(lines)
            translated_chunk = translate_text(
                text_to_translate, target_language)
            outfile.write(translated_chunk)

        if target_language == 'en':
            footer = "\n*This blog post was written with the assistance of mistral*\n\n---\n"
        else:
            footer = "\n*本文由mistral翻译原文所得。*\n\n---\n"

        outfile.write(footer)


def translate_files_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            input_file = os.path.join(directory, filename)
            with open(input_file, 'r') as file:
                lines = file.readlines()
                title_line = next(
                    (line for line in lines if line.startswith('title:')), '').strip()
                title = title_line.replace('title:', '').strip().strip('"')

            if filename.endswith('-cn.md'):
                translated_filename = filename.replace('-cn.md', '-en.md')
                output_file = os.path.join(directory, translated_filename)
                if not os.path.exists(output_file):
                    print(
                        f"Begin translating {input_file} to {output_file} (CN to EN)")
                    with open(output_file, 'w') as outfile:
                        outfile.write(
                            f"---\nlayout: post\ntitle: \"{title}\"\n---\n")
                    read_and_translate(input_file, output_file, 'en')
                    print(
                        f"Translated {input_file} to {output_file} (CN to EN)")
            elif filename.endswith('-en.md'):
                translated_filename = filename.replace('-en.md', '-cn.md')
                output_file = os.path.join(directory, translated_filename)
                if not os.path.exists(output_file):
                    print(
                        f"Begin translating {input_file} to {output_file} (EN to CN)")
                    with open(output_file, 'w') as outfile:
                        outfile.write(
                            f"---\nlayout: post\ntitle: \"{title}\"\n---\n")
                    read_and_translate(input_file, output_file, 'cn')
                    print(
                        f"Translated {input_file} to {output_file} (EN to CN)")


directory = '_posts'

translate_files_in_directory(directory)
