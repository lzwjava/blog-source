import os
import subprocess
import argparse


def code_to_pdf(input_dir, output_file):
    """
    Converts all code files in a directory to a single PDF.

    Args:
        input_dir (str): The directory containing the code files.
        output_file (str): The path to the output PDF file.
    """
    text_content = ""

    if not os.path.isdir(input_dir):
        print(f"Error: Input directory '{input_dir}' does not exist.")
        return

    for filename in os.listdir(input_dir):
        if filename.endswith(
            (".py", ".js", ".java", ".c", ".cpp", ".go", ".sh", ".html", ".css")
        ):
            filepath = os.path.join(input_dir, filename)
            text_content += f"{filename}\n\n"
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    code_content = f.read()
                    text_content += f"{code_content}\n\n"
            except Exception as e:
                print(f"Error reading file {filename}: {e}")
                continue

    if not text_content:
        print("No code files found in the specified directory.")
        return

    temp_text_file = "temp_code.txt"
    with open(temp_text_file, "w", encoding="utf-8") as f:
        f.write(text_content)

    try:
        subprocess.run(
            [
                "pandoc",
                temp_text_file,
                "-o",
                output_file,
                "--from",
                "txt",
                "--pdf-engine=xelatex",
            ],
            check=True,
        )
        print(f"Successfully generated PDF: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error generating PDF: {e}")
    finally:
        os.remove(temp_text_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert code files to PDF.")
    parser.add_argument(
        "--input_dir", required=True, help="The directory containing the code files."
    )
    parser.add_argument(
        "--output_file", required=True, help="The path to the output PDF file."
    )
    args = parser.parse_args()

    code_to_pdf(args.input_dir, args.output_file)
