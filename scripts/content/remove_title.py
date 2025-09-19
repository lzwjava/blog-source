import os
import re
import frontmatter


def process_markdown_content(file_path):
    # Load file with frontmatter
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            post = frontmatter.load(file)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return

    # Check if frontmatter exists
    if not post.metadata:
        # No frontmatter, skip
        return

    # Get the body content
    body = post.content

    # Get the first 5 lines of the body
    body_lines = body.splitlines()[:5]
    first_five_lines = "\n".join(body_lines)

    # Count level 1 headers in the first 5 lines
    header_pattern = re.compile(r"^#\s+.*$", re.MULTILINE)
    headers = header_pattern.findall(first_five_lines)
    if len(headers) != 1:
        # Skip if not exactly one level 1 header in the first 5 lines
        return

    # Remove the single level 1 header along with preceding newline(s) from the entire body
    header_with_newline_pattern = re.compile(r"\n+#\s+.*$", re.MULTILINE)
    new_body = header_with_newline_pattern.sub("", body, count=1)

    # Update the content
    post.content = new_body

    # Write back to file using dumps to get string representation
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(frontmatter.dumps(post))


def process_files_in_directory(directory):
    if not os.path.isdir(directory):
        raise FileNotFoundError(f"Directory '{directory}' does not exist.")

    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            file_path = os.path.join(directory, filename)
            process_markdown_content(file_path)


# Get the path to the notes directory
notes_directory = os.path.join("./notes")

process_files_in_directory(notes_directory)
