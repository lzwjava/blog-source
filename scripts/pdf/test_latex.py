import os
import subprocess

# Configuration
import platform

GEOMETRY = "margin=1in"
input_markdown_base = "_posts"  # Base path for input Markdown file
output_pdf_base = "test/test"  # Base path for output PDF file
languages = ["en", "zh", "ja", "es", "hi", "fr", "de", "ar", "hant"]
post_name = "2025-01-13-gitmessageai"


def generate_pdfs():
    for lang in languages:
        input_markdown_path = f"{input_markdown_base}/{lang}/{post_name}-{lang}.md"
        output_pdf_path = f"{output_pdf_base}-{lang}.pdf"

        # Ensure the output directory exists
        output_dir = os.path.dirname(output_pdf_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Check if input file exists
        if not os.path.exists(input_markdown_path):
            print(f"Input file does not exist: {input_markdown_path}")
            continue
        # Construct the Pandoc command
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
            "pandoc",
            input_markdown_path,
            "-o",
            output_pdf_path,
            "-f",
            "markdown",
            "--pdf-engine",
            "xelatex",
            "-V",
            f"romanfont={CJK_FONT}",
            "-V",
            f"mainfont={CJK_FONT}",
            "-V",
            f"CJKmainfont={CJK_FONT}",
            "-V",
            f"CJKsansfont={CJK_FONT}",
            "-V",
            f"CJKmonofont={CJK_FONT}",
            "-V",
            f"geometry:{GEOMETRY}",
            "-V",
            "classoption=16pt",
            "-V",
            "CJKoptions=Scale=1.1",
            "-V",
            "linestretch=1.5",
        ]

        print(command)

        # Run the Pandoc command
        try:
            subprocess.run(command, check=True)
            print(f"PDF successfully generated: {output_pdf_path}")
        except subprocess.CalledProcessError as e:
            print(f"Error generating PDF: {e}")


if __name__ == "__main__":
    generate_pdfs()
