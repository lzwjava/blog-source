import os


def update_footer_text(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    old_footer = "*This blog post was written with the assistance of mistral*"
    new_footer = "*This blog post was translated by Mistral*"

    updated_lines = [line.replace(old_footer, new_footer) for line in lines]

    # Write the updated content back to the file
    with open(file_path, 'w') as file:
        file.writelines(updated_lines)
    print(f"Updated footer text in {file_path}")


def process_files_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            file_path = os.path.join(directory, filename)
            update_footer_text(file_path)


directory = '_posts'
process_files_in_directory(directory)
