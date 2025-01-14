import os
import subprocess

# Configuration
CJK_FONT = "simsun"
GEOMETRY = "margin=1in"
input_markdown_path = "_posts/en/2025-01-13-gitmessageai-en.md"  # Replace with your input Markdown file
output_pdf_path = "test.pdf"    # Replace with your desired output PDF file

# Check if input file exists
if not os.path.exists(input_markdown_path):
    raise Exception(f"Input file does not exist: {input_markdown_path}")

# Construct the Pandoc command
command = [
    'pandoc',
    input_markdown_path,
    '-o', output_pdf_path,
    '-f', 'markdown',
    '--pdf-engine', 'xelatex',
    '-V', f'CJKmainfont={CJK_FONT}',
    '-V', f'CJKsansfont={CJK_FONT}',
    '-V', f'CJKmonofont={CJK_FONT}',
    '-V', f'geometry:{GEOMETRY}',
    '-V', 'classoption=16pt',
    '-V', 'CJKoptions=Scale=1.1',
    '-V', 'linestretch=1.5'
]

# Run the Pandoc command
try:
    subprocess.run(command, check=True)
    print(f"PDF successfully generated: {output_pdf_path}")
except subprocess.CalledProcessError as e:
    print(f"Error generating PDF: {e}")