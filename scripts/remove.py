import os


def remove_last_two_hyphens(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Remove any "---" in the last two lines if present
    if lines[-1].strip() == "---":
        lines.pop()
    if len(lines) > 0 and lines[-1].strip() == "---":
        lines.pop()

    # Write the updated content back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)
    print(f"Removed trailing hyphens in {file_path}")


def process_files_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            file_path = os.path.join(directory, filename)
            remove_last_two_hyphens(file_path)


directory = '_posts'
process_files_in_directory(directory)
