#!/usr/bin/env python3
import sys
import os
from pdf_base import text_to_pdf_from_markdown

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <markdown-file>")
        sys.exit(1)

    markdown_path = sys.argv[1]
    if not os.path.isfile(markdown_path):
        print(f"Error: File not found: {markdown_path}")
        sys.exit(1)

    # Replace .md extension with .pdf, keep same directory
    if markdown_path.lower().endswith('.md'):
        pdf_path = markdown_path[:-3] + '.pdf'
    else:
        pdf_path = markdown_path + '.pdf'

    success = text_to_pdf_from_markdown(markdown_path, pdf_path)
    if success:
        print(f"Successfully converted {markdown_path} to {pdf_path}")
        sys.exit(0)
    else:
        print(f"Failed to convert {markdown_path}")
        sys.exit(1)

if __name__ == '__main__':
    main()