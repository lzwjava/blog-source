import os
import subprocess
import argparse
import glob
from datetime import datetime
import tempfile
import re
import yaml

OUTPUT_DIRECTORY = "assets/epub/"
INPUT_DIRECTORY = "_posts/en"

def convert_markdown_to_kindle(input_path, output_dir):
    """Converts a directory of markdown files to a single epub, ordered by date."""

    if not input_path:
        input_path = INPUT_DIRECTORY

    if not os.path.exists(input_path):
        print(f"Error: Input path '{input_path}' does not exist.")
        return

    if not os.path.isdir(input_path):
         print("Error: Input must be a directory containing markdown files.")
         return

    md_files = glob.glob(os.path.join(input_path, "*.md"))
    if not md_files:
        print(f"No markdown files found in {input_path}")
        return


    # Extract date from filename and sort by date desc
    def get_date_from_filename(filename):
        try:
            match = re.search(r'(\d{4}-\d{2}-\d{2})', os.path.basename(filename))
            if match:
                date_str = match.group(1)
                return datetime.strptime(date_str, '%Y-%m-%d')
            else:
                return datetime.min
        except (ValueError, IndexError):
            return datetime.min # if no date, put at the beginning

    md_files.sort(key=get_date_from_filename, reverse=True)


    _convert_multiple_files(md_files, output_dir)


def _convert_multiple_files(file_paths, output_dir):
    """Converts multiple markdown files to a single epub file."""
    if not output_dir:
        output_dir = OUTPUT_DIRECTORY
    
    os.makedirs(output_dir, exist_ok=True)
    
    output_epub_file = os.path.join(output_dir, "blog-en.epub")

    if os.path.exists(output_epub_file):
        print(f"Skipping: {output_epub_file} already exists.")
        return

    try:
        # Create a temporary file to store the combined markdown content
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as tmp_file:
            combined_content = f'# My Blog\n\n'
            title = "My Blog"
            for file_path in file_paths:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Remove YAML front matter
                    front_matter = ""
                    match = re.search(r'^---(.*?)---', content, re.DOTALL)
                    if match:
                        front_matter = match.group(1)
                        content = content[match.end():]
                    
                    file_title = os.path.splitext(os.path.basename(file_path))[0]
                    try:
                        if front_matter:
                            yaml_data = yaml.safe_load(front_matter)
                            if 'title' in yaml_data:
                                file_title = yaml_data['title']
                    except yaml.YAMLError as e:
                        print(f"Error parsing YAML in {file_path}: {e}")
                    
                    combined_content += f'## {file_title}\n'
                    combined_content += content
                    combined_content += '\n\n'  # Add a separator between files
            tmp_file.write(combined_content)
            temp_file_path = tmp_file.name

        # Convert the combined markdown file to epub using pandoc
        print(f"Converting {len(file_paths)} markdown files to {output_epub_file} using pandoc")
        pandoc_command = [
            "pandoc",
            temp_file_path,
            "-o",
            output_epub_file,
            "--toc",
            "--toc-depth=1",
            "--metadata",
            f"title={title}"
        ]
        pandoc_result = subprocess.run(pandoc_command, capture_output=True, text=True)
        if pandoc_result.returncode != 0:
            print(f"Error converting to {output_epub_file} using pandoc: {pandoc_result.stderr}")
        else:
            print(f"Successfully converted to {output_epub_file} using pandoc")
    except Exception as e:
        print(f"Error processing files: {e}")
    finally:
        if 'temp_file_path' in locals() and os.path.exists(temp_file_path):
            os.remove(temp_file_path)


def main():
    parser = argparse.ArgumentParser(description="Convert Markdown files to epub format.")
    parser.add_argument("input_path", nargs='?', help="Path to the directory containing markdown files.", default="")
    parser.add_argument("-o", "--output_dir", help="Output directory for the generated epub files.", default=OUTPUT_DIRECTORY)

    args = parser.parse_args()

    convert_markdown_to_kindle(args.input_path, args.output_dir)

if __name__ == "__main__":
    main()
