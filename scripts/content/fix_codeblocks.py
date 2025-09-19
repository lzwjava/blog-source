import os
import argparse


def fix_code_blocks_in_file(filepath):
    """
    Adds newlines before specific code blocks (Java and XML) in a markdown file,
    preserving any leading whitespace.

    Args:
        filepath (str): The path to the markdown file to process.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.readlines()

        updated_content = []
        for line in content:
            stripped_line = line.strip()
            if stripped_line.startswith("```java") or stripped_line.startswith(
                "```xml"
            ):
                # Add a newline before the code block if it's not already there
                if updated_content and not updated_content[-1].strip() == "":
                    updated_content.append("\n")
                # Preserve the original leading whitespace
                updated_content.append(line)
            else:
                updated_content.append(line)

        # Check if any replacements were made
        replacements_made = content != updated_content

        # Write updated content only if replacements were made
        if replacements_made:
            with open(filepath, "w", encoding="utf-8") as f:
                f.writelines(updated_content)
            print(f"Added newlines to Java and XML code blocks in {filepath}")
        else:
            print(f"Processed {filepath}: No replacements needed")

        return replacements_made

    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False


def process_markdown_files(directory, max_files=None):
    """
    Processes all markdown files in a directory to add newlines before specific code blocks.

    Args:
        directory (str): The directory to search for markdown files.
        max_files (int, optional): Maximum number of files to process.
    """
    files_processed = 0
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".md"):
                filepath = os.path.join(root, filename)
                success = fix_code_blocks_in_file(filepath)
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
        description="Add newlines before specific code blocks in Markdown files."
    )
    parser.add_argument(
        "--maxfiles", type=int, help="Maximum number of files to process."
    )
    parser.add_argument(
        "--file", type=str, help="Path to a specific markdown file to process."
    )
    args = parser.parse_args()

    if args.file:
        # Process a single file
        if os.path.exists(args.file) and args.file.endswith(".md"):
            fix_code_blocks_in_file(args.file)
        else:
            print(f"Invalid file path or not a markdown file: {args.file}")
    else:
        # Process directories
        directories = ["."]  # Default to current directory
        for directory in directories:
            if os.path.exists(directory):
                process_markdown_files(directory, max_files=args.maxfiles)
            else:
                print(f"Directory not found: {directory}")


if __name__ == "__main__":
    main()
