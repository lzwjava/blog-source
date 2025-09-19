import os
import subprocess
import argparse

OUTPUT_DIRECTORY = "assets/epub/"


def convert_markdown_to_kindle(input_path, output_dir):
    """Converts a markdown file or directory of markdown files to epub format using Pandoc."""

    if not os.path.exists(input_path):
        print(f"Error: Input path '{input_path}' does not exist.")
        return

    if os.path.isdir(input_path):
        for filename in os.listdir(input_path):
            if filename.endswith(".md"):
                file_path = os.path.join(input_path, filename)
                _convert_single_file(file_path, output_dir)
    elif input_path.endswith(".md"):
        _convert_single_file(input_path, output_dir)
    else:
        print(
            "Error: Input must be a markdown file or a directory containing markdown files."
        )


def _convert_single_file(file_path, output_dir):
    """Converts a single markdown file to epub format."""

    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}")
        return

    if not output_dir:
        output_dir = OUTPUT_DIRECTORY

    os.makedirs(output_dir, exist_ok=True)

    base_name = os.path.splitext(os.path.basename(file_path))[0]
    epub_file = os.path.join(output_dir, f"{base_name}.epub")

    if os.path.exists(epub_file):
        print(f"Skipping {file_path}: {epub_file} already exists.")
        return

    try:
        # Convert markdown to epub using pandoc
        print(f"Converting {file_path} to {epub_file} using pandoc")
        pandoc_command = ["pandoc", file_path, "-o", epub_file]
        pandoc_result = subprocess.run(pandoc_command, capture_output=True, text=True)
        if pandoc_result.returncode != 0:
            print(
                f"Error converting {file_path} to {epub_file} using pandoc: {pandoc_result.stderr}"
            )
            return
        else:
            print(f"Successfully converted {file_path} to {epub_file} using pandoc")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Convert Markdown files to epub format."
    )
    parser.add_argument(
        "input_path",
        help="Path to the markdown file or directory containing markdown files.",
    )
    parser.add_argument(
        "-o",
        "--output_dir",
        help="Output directory for the generated epub files.",
        default=OUTPUT_DIRECTORY,
    )

    args = parser.parse_args()

    convert_markdown_to_kindle(args.input_path, args.output_dir)


if __name__ == "__main__":
    main()
