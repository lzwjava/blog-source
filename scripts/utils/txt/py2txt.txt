import os
import shutil

def convert_files_to_txt(source_dir, dest_dir):
    """
    Lists all .py and .sh files in the source directory, copies them to the destination directory,
    and renames them with a .txt extension.
    """
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for filename in os.listdir(source_dir):
        if filename.endswith((".py", ".sh")):
            source_path = os.path.join(source_dir, filename)
            name, ext = os.path.splitext(filename)
            dest_filename = name + ".txt"  # Change extension to .txt
            dest_path = os.path.join(dest_dir, dest_filename)

            try:
                shutil.copy2(source_path, dest_path)  # Copy file with metadata
                print(f"Copied and renamed: {filename} -> {dest_filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    source_directory = "."  # Current directory
    destination_directory = "txt"  # Directory to store .txt files

    convert_files_to_txt(source_directory, destination_directory)
