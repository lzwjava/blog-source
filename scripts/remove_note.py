import os
import re


def remove_note_from_title(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    title_pattern = re.compile(r'title:\s*"([^"]*?)\(Note:[^"]*?\)"')

    for i, line in enumerate(lines):
        match = title_pattern.search(line)
        if match:
            new_title = re.sub(r'\(Note:[^"]*?\)', '', match.group(1)).strip()
            lines[i] = f'title: "{new_title}"\n'
            print(f"Updated title in {file_path} to '{new_title}'")
            break

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)


def process_files_in_directory(directory):
    if not os.path.isdir(directory):
        raise FileNotFoundError(f"Directory '{directory}' does not exist.")

    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            file_path = os.path.join(directory, filename)
            remove_note_from_title(file_path)


# Get the absolute path to the _posts directory
current_directory = os.path.dirname(os.path.abspath(__file__))
posts_directory = os.path.join(current_directory, '../_posts')

process_files_in_directory(posts_directory)
