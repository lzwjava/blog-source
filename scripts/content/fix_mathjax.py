import os
import re
import markdown
import argparse


def fix_mathjax_in_file(filepath, gemini=False, reset=False):
    r"""
    Replaces instances of \( and \) with \\( and \\) respectively in a markdown file,
    skipping code blocks. If gemini is True, also replaces $ $ with \\( and \\).
    If reset is True, performs the reverse operation: \\( to \(, \\) to \), etc.

    Args:
        filepath (str): The path to the markdown file to process.
        gemini (bool, optional): Whether to also convert dollar sign notation to/from backslash notation.
        reset (bool, optional): Whether to reverse the replacements (\\( to \(, etc.).
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        if not reset and (
            re.search(r"\\\\\(", content) or re.search(r"\\\\\[", content)
        ):
            print(f"Skipping {filepath}: Already contains \\( or \\[")
            return False

        # Parse markdown to identify code blocks
        md = markdown.Markdown(extensions=["fenced_code"])
        html_content = md.convert(content)

        # Identify code blocks using regex
        code_blocks = list(
            re.finditer(r"<pre><code.*?>.*?</code></pre>", html_content, re.DOTALL)
        )

        # Extract code block content and their positions
        code_block_data = []
        for match in code_blocks:
            code_block_data.append(
                {"start": match.start(), "end": match.end(), "content": match.group(0)}
            )

        # Function to replace MathJax delimiters outside code blocks
        def replace_mathjax(text, gemini=False, reset=False):
            temp_text = text
            for cb in code_block_data:
                temp_text = temp_text.replace(cb["content"], "CODE_BLOCK_PLACEHOLDER")

            if reset:
                # Reverse replacements: \\( to \(, \\) to \), etc.
                temp_text = re.sub(r"\\\\\(", r"\(", temp_text)
                temp_text = re.sub(r"\\\\\)", r"\)", temp_text)
                temp_text = re.sub(r"\\\\\[", r"\[", temp_text)
                temp_text = re.sub(r"\\\\\]", r"\]", temp_text)
                if gemini:
                    # Reverse $...$ to \\(...\\)
                    temp_text = re.sub(r"\\\\\((.*?)\\\\\)", r"$\1$", temp_text)
            else:
                # Forward replacements: \( to \\(, \) to \\), etc.
                temp_text = re.sub(r"\\\(", r"\\\\(", temp_text)
                temp_text = re.sub(r"\\\)", r"\\\\)", temp_text)
                temp_text = re.sub(r"\\\[", r"\\\\[", temp_text)
                temp_text = re.sub(r"\\\]", r"\\\\]", temp_text)
                if gemini:
                    # Replace $...$ with \\(...\\)
                    temp_text = re.sub(r"\$(.*?)\$", r"\\\\(\1\\\\)", temp_text)

            for cb in code_block_data:
                temp_text = temp_text.replace("CODE_BLOCK_PLACEHOLDER", cb["content"])
            return temp_text

        updated_content = replace_mathjax(content, gemini, reset)

        # Check if any replacements were made
        replacements_made = content != updated_content

        # Write updated content only if replacements were made
        if replacements_made:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(updated_content)
            action = "Reversed" if reset else "Fixed"
            print(f"{action} MathJax delimiters in {filepath}: Replacements made")
        else:
            print(f"Processed {filepath}: No replacements needed")

        return replacements_made

    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False


def fix_mathjax_in_markdown(directory, max_files=None, gemini=False, reset=False):
    r"""
    Finds all markdown files in a directory and replaces instances of
    \( and \) with \\( and \\) respectively, skipping code blocks.
    If gemini is True, also replaces $ $ with \\( and \\).
    If reset is True, performs the reverse operation.

    Args:
        directory (str): The directory to search for markdown files.
        max_files (int, optional): Maximum number of files to process. Defaults to None (unlimited).
        gemini (bool, optional): Whether to also convert dollar sign notation to/from backslash notation.
        reset (bool, optional): Whether to reverse the replacements.
    """
    files_processed = 0
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".md"):
                filepath = os.path.join(root, filename)
                success = fix_mathjax_in_file(filepath, gemini, reset)
                if success:
                    files_processed += 1

                if max_files and files_processed >= max_files:
                    print(f"Maximum files processed ({max_files}). Exiting directory.")
                    return


def main():
    """
    Main function to process either a single file or directories.
    """
    parser = argparse.ArgumentParser(
        description="Fix or reverse MathJax delimiters in Markdown files."
    )
    parser.add_argument(
        "--maxfiles", type=int, help="Maximum number of files to process."
    )
    parser.add_argument(
        "--file", type=str, help="Path to a specific markdown file to process."
    )
    parser.add_argument(
        "--gemini",
        action="store_true",
        help="Convert dollar sign notation ($...$) to/from backslash notation (\\\\(...\\\\)).",
    )
    parser.add_argument(
        "--reset",
        action="store_true",
        help="Reverse the MathJax delimiter changes (\\\\( to \\(, etc.).",
    )
    args = parser.parse_args()

    if args.file:
        # Process a single file
        if os.path.exists(args.file) and args.file.endswith(".md"):
            fix_mathjax_in_file(args.file, args.gemini, args.reset)
        else:
            print(f"Invalid file path or not a markdown file: {args.file}")
    else:
        # Process directories
        directories = ["notes"]
        for directory in directories:
            if os.path.exists(directory):
                fix_mathjax_in_markdown(
                    directory,
                    max_files=args.maxfiles,
                    gemini=args.gemini,
                    reset=args.reset,
                )
            else:
                print(f"Directory not found: {directory}")


if __name__ == "__main__":
    main()
