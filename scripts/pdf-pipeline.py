import os
import json
import argparse
from datetime import datetime
import subprocess
import platform


OUTPUT_DIRECTORY = "assets/pdfs"
INPUT_DIRECTORY = "_posts"
LANGUAGES = ["en", "zh", "ja", "es", "hi", "fr", "de", "ar", "hant"]


def get_last_n_files(input_dir, n=10):
    try:
        md_files = []
        for lang in LANGUAGES:
            lang_dir = os.path.join(input_dir, lang)
            if os.path.exists(lang_dir):
                md_files.extend([os.path.join(lang_dir, f) for f in os.listdir(lang_dir) if f.endswith('.md')])
        md_files_sorted = sorted(md_files, key=lambda x: os.path.basename(x), reverse=True)
        last_n_files = md_files_sorted[:n]
        return last_n_files
    except Exception as e:
        print(f"Error retrieving files from {input_dir}: {e}")
        return []


def text_to_pdf_from_markdown(input_markdown_path, output_pdf_path, dry_run=False):
    if dry_run:
        print(f"Dry run: Would generate PDF from: {input_markdown_path}")
        return

    print(f"Generating PDF from: {input_markdown_path}")

    CJK_FONT = "Heiti SC"
    GEOMETRY = "margin=1in"

    if not os.path.exists(input_markdown_path):
        raise Exception(f"Input file does not exist: {input_markdown_path}")
    
    lang = os.path.basename(input_markdown_path).split('-')[-1].split('.')[0]
    
    if platform.system() == "Darwin":
        if lang == "hi":
            CJK_FONT = "Kohinoor Devanagari"
        elif lang == "ar":
            CJK_FONT = "Geeza Pro"
        elif lang in ["en", "fr", "de", "es"]:
            CJK_FONT = "Helvetica"
        elif lang == "zh":
            CJK_FONT = "PingFang SC"
        elif lang == "hant":
            CJK_FONT = "PingFang TC"
        elif lang == "ja":
            CJK_FONT = "Hiragino Sans"
        else:
            CJK_FONT = "Arial Unicode MS"
    else:
        if lang == "hi":
            CJK_FONT = "Noto Sans Devanagari"
        elif lang == "ar":
            CJK_FONT = "Noto Naskh Arabic"
        elif lang in ["en", "fr", "de", "es"]:
            CJK_FONT = "DejaVu Sans"
        elif lang == "zh":
            CJK_FONT = "Noto Sans CJK SC"
        elif lang == "hant":
            CJK_FONT = "Noto Sans CJK TC"
        elif lang == "ja":
            CJK_FONT = "Noto Sans CJK JP"
        else:
            CJK_FONT = "Noto Sans"
    command = [
        'pandoc',
        input_markdown_path,
        '-o', output_pdf_path,
        '-f', 'markdown',
        '--pdf-engine', 'xelatex',
        '-V', f'romanfont={CJK_FONT}',
        '-V', f'mainfont={CJK_FONT}',
        '-V', f'CJKmainfont={CJK_FONT}',
        '-V', f'CJKsansfont={CJK_FONT}',
        '-V', f'CJKmonofont={CJK_FONT}',
        '-V', f'geometry:{GEOMETRY}',
        '-V', 'classoption=16pt',
        '-V', 'CJKoptions=Scale=1.1',
        '-V', 'linestretch=1.5'
    ]

    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Pandoc error for {output_pdf_path}: {result.stderr}")
        raise Exception(f"Pandoc failed for {input_markdown_path}")

    print(f"PDF content written to {output_pdf_path}")

    scale_factor = "1.0"
    tmp_pdf_path = output_pdf_path.replace(".pdf", "-tmp.pdf")

    os.rename(output_pdf_path, tmp_pdf_path)

    pdfjam_command = [
        'pdfjam',
        '--scale', scale_factor,
        tmp_pdf_path,
        '-o', output_pdf_path
    ]

    pdfjam_result = subprocess.run(pdfjam_command, capture_output=True, text=True)
    if pdfjam_result.returncode != 0:
        print(f"pdfjam error for {output_pdf_path}: {pdfjam_result.stderr}")
        os.rename(tmp_pdf_path, output_pdf_path)
        raise Exception(f"pdfjam failed for {output_pdf_path}")

    os.remove(tmp_pdf_path)
    print(f"Scaled PDF written to {output_pdf_path}")

def process_markdown_files(input_dir, output_dir, n=10, max_files=10000, dry_run=False):
    
    md_files_to_process = get_last_n_files(input_dir, n)
    total_files = len(md_files_to_process)
    
    print(f"Total Markdown files to process: {total_files}")

    if total_files == 0:
        print(f"No Markdown files found in '{input_dir}' directory.")
        return

    files_processed = 0
    for idx, md_file_path in enumerate(md_files_to_process, start=1):
        filename = os.path.basename(md_file_path)
        lang = filename.split('-')[-1].split('.')[0]
        pdf_filename = f"{os.path.splitext(filename)[0]}.pdf"
        output_lang_dir = os.path.join(output_dir, lang)
        os.makedirs(output_lang_dir, exist_ok=True)
        output_filename = os.path.join(output_lang_dir, pdf_filename)


        if os.path.exists(output_filename):
            print(f"Skipping {filename}: {output_filename} already exists.")
            continue

        print(f"\nProcessing {files_processed + 1}/{total_files}: {filename}")
        try:
            with open(md_file_path, 'r', encoding='utf-8') as file:
                markdown_content = file.read()

            title_line = None

            if markdown_content.startswith('---'):
                lines = markdown_content.split('\n')
                try:
                    second_delim_index = lines[1:].index('---') + 1
                    front_matter_lines = lines[1:second_delim_index]
                    cleaned_lines = lines[second_delim_index+1:]

                    for fm_line in front_matter_lines:
                        fm_line_stripped = fm_line.strip()
                        if fm_line_stripped.lower().startswith('title:'):
                            title_value = fm_line_stripped.split(':', 1)[1].strip()
                            if (title_value.startswith('"') and title_value.endswith('"')) or (title_value.startswith("'") and title_value.endswith("'")):
                                title_value = title_value[1:-1].strip()
                            if title_value:
                                title_line = f"# {title_value}"
                            break

                    markdown_content = '\n'.join(cleaned_lines)
                except ValueError:
                    markdown_content = ''

                if not markdown_content.strip():
                    print(f"Skipping {filename}: No content to convert after cleaning front matter.")
                    continue

                if title_line:
                    markdown_content = title_line + "\n\n" + markdown_content

                cleaned_md_path = md_file_path + ".cleaned"
                with open(cleaned_md_path, 'w', encoding='utf-8') as temp:
                    temp.write(markdown_content)

                try:
                    text_to_pdf_from_markdown(
                        input_markdown_path=cleaned_md_path,
                        output_pdf_path=output_filename,
                        dry_run=dry_run
                    )
                except Exception as e:
                    print(f"Error processing {filename}: {e}")
                    continue
                finally:
                    if os.path.exists(cleaned_md_path):
                        os.remove(cleaned_md_path)
                    tmp_pdf_path = output_filename.replace(".pdf", "-tmp.pdf")
                    if os.path.exists(tmp_pdf_path):
                        os.remove(tmp_pdf_path)

                files_processed += 1
                if files_processed >= max_files:
                    print(f"Processed {max_files} files. Stopping.")
                    break

        except Exception as e:
            print(f"Error processing {filename}: {e}")
            continue

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Markdown files to PDFs.")
    parser.add_argument('--n', type=int, default=10, help="Number of files to process for 'posts' task (default: 10).")
    parser.add_argument('--max_files', type=int, default=10000, help="Maximum number of files to process (default: 10000).")
    parser.add_argument('--dry_run', action='store_true', help="Simulate the conversion without actual file generation.")
    args = parser.parse_args()

    process_markdown_files(INPUT_DIRECTORY, OUTPUT_DIRECTORY, n=args.n, max_files=args.max_files, dry_run=args.dry_run)
