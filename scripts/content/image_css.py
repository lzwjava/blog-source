import os
import subprocess
import re


def is_image_responsive(image_path):
    """
    Checks if an image should be responsive based on its width and height.

    Args:
        image_path (str): The path to the image file.

    Returns:
        bool: True if the image's width is less than its height, False otherwise.
              Returns None if there is an error getting image dimensions.
    """
    try:
        command = [
            "ffprobe",
            "-v",
            "error",
            "-select_streams",
            "v:0",
            "-show_entries",
            "stream=width,height",
            "-of",
            "csv=s=,:p=0",
            image_path,
        ]
        result = subprocess.run(command, capture_output=True, text=True, check=True)

        output = result.stdout.strip()
        width, height = map(int, output.split(","))
        return width < height
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return None


def process_markdown_files(directory):
    """
    Processes markdown files in a directory to add or remove responsive image classes.

    Args:
        directory (str): The directory containing the markdown files.
    """
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            filepath = os.path.join(directory, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            updated_content = content
            image_pattern = re.compile(
                r"!\[.*?\]\((.*?)\)(?:\{: \.responsive \})?(?:\{: \.caption \})?"
            )

            for match in image_pattern.finditer(content):
                image_path = match.group(1)
                full_image_path = os.path.join(os.path.dirname(filepath), image_path)

                if os.path.exists(full_image_path):
                    is_responsive = is_image_responsive(full_image_path)
                    if is_responsive is None:
                        continue

                    if is_responsive:
                        if "{: .responsive }" not in match.group(0):
                            print(f"Add responsive class to {image_path} in {filename}")
                            updated_content = updated_content.replace(
                                match.group(0), f"{match.group(0)}{{: .responsive }}"
                            )
                    else:
                        if "{: .responsive }" in match.group(0):
                            print(
                                f"Remove responsive class from {image_path} in {filename}"
                            )
                            updated_content = updated_content.replace(
                                f"{match.group(0)}{{: .responsive }}", match.group(0)
                            )
                            updated_content = updated_content.replace(
                                f"{match.group(0)}{{: .responsive }}", match.group(0)
                            )

            if updated_content != content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(updated_content)
                print(f"Updated {filename}")


if __name__ == "__main__":
    original_dir = "original"
    process_markdown_files(original_dir)
