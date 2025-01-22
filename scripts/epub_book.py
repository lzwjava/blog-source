import os
import subprocess
import argparse
import glob
from datetime import datetime

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
            date_str = os.path.basename(filename).split('-')[0]
            return datetime.strptime(date_str, '%Y-%m-%d')
        except (ValueError, IndexError):
            return datetime.min # if no date, put at the beginning

    md_files.sort(key=get_date_from_filename, reverse=True)


    _convert_multiple_files(md_files, output_dir)


def _convert_multiple_files(file_paths, output_dir):
    """Converts multiple markdown files to a single epub file."""
    if not output_dir:
        output_dir = OUTPUT_DIRECTORY
    
    os.makedirs(output_dir, exist_ok=True)
    
    output_epub_file = os.path.join(output_dir, "all_posts.epub")

    if os.path.exists(output_epub_file):
        print(f"Skipping: {output_epub_file} already exists.")
        return

    try:
        # Convert markdown to epub using pandoc
        print(f"Converting {len(file_paths)} markdown files to {output_epub_file} using pandoc")
        pandoc_command = [
            "pandoc",
            *file_paths,
            "-o",
            output_epub_file
        ]
        pandoc_result = subprocess.run(pandoc_command, capture_output=True, text=True)
        if pandoc_result.returncode != 0:
            print(f"Error converting to {output_epub_file} using pandoc: {pandoc_result.stderr}")
            return
        else:
            print(f"Successfully converted to {output_epub_file} using pandoc")
    except Exception as e:
        print(f"Error processing files: {e}")


def main():
    parser = argparse.ArgumentParser(description="Convert Markdown files to epub format.")
    parser.add_argument("input_path", nargs='?', help="Path to the directory containing markdown files.", default="")
    parser.add_argument("-o", "--output_dir", help="Output directory for the generated epub files.", default=OUTPUT_DIRECTORY)

    args = parser.parse_args()

    convert_markdown_to_kindle(args.input_path, args.output_dir)

if __name__ == "__main__":
    main()
