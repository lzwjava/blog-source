import os


def move_footer_to_top(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    english_footer = "*This blog post was written with the assistance of mistral*"
    chinese_footer = "*本文由mistral翻译原文所得。*"
    footer_index = None
    footer = None

    # Check if the English footer exists in the file
    for i, line in enumerate(lines):
        if english_footer in line:
            footer_index = i
            footer = english_footer
            break

    # Check if the Chinese footer exists in the file
    if footer_index is None:
        for i, line in enumerate(lines):
            if chinese_footer in line:
                footer_index = i
                footer = chinese_footer
                break

    if footer_index is not None:
        # Remove the footer from its current position
        while footer_index < len(lines) and lines[footer_index].strip() != "---":
            del lines[footer_index]

        # Find the end of the YAML front matter
        yaml_end_index = None
        for i, line in enumerate(lines):
            if line.strip() == "---":
                if yaml_end_index is not None:
                    yaml_end_index = i
                    break
                else:
                    yaml_end_index = i

        # Insert the footer below the YAML front matter
        if yaml_end_index is not None:
            footer_text = f"\n{footer}\n\n---\n"
            lines = lines[:yaml_end_index + 1] + \
                [footer_text] + lines[yaml_end_index + 1:]

        # Write the updated content back to the file
        with open(file_path, 'w') as file:
            file.writelines(lines)
        print(f"Moved footer to top in {file_path}")


def process_files_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            file_path = os.path.join(directory, filename)
            move_footer_to_top(file_path)


directory = '_posts'
process_files_in_directory(directory)
