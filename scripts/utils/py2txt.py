import os
import shutil


def convert_files_to_txt(source_dir, dest_dir):
    """
    Lists all files except this script in the source directory, copies them to the destination directory,
    and renames them with a txt extension, excluding directories
    """
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    script_name = os.path.basename(__file__)

    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)

        if os.path.isfile(source_path) and item != script_name:
            name, ext = os.path.splitext(item)
            dest_filename = name + ".txt"  # Change extension to txt
            dest_path = os.path.join(dest_dir, dest_filename)

            try:
                shutil.copy2(source_path, dest_path)  # Copy file with metadata
                print(f"Copied and renamed: {item} -> {dest_filename}")
            except Exception as e:
                print(f"Error processing {item}: {e}")


if __name__ == "__main__":
    source_directory = os.path.dirname(__file__)  # Current directory
    destination_directory = os.path.join(
        os.path.dirname(__file__), "txt"
    )  # Directory to store txt files, using absolute path

    convert_files_to_txt(source_directory, destination_directory)
