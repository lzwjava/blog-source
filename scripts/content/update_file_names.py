import os
import argparse


def update_file_names(old_name, new_name):
    directories = ["_posts", "assets/pdfs", "assets/audios"]

    for directory in directories:
        full_directory_path = os.path.join(os.getcwd(), directory)
        if not os.path.exists(full_directory_path):
            print(f"Directory {full_directory_path} does not exist. Skipping.")
            continue

        for filename in os.listdir(full_directory_path):
            if old_name in filename:
                old_file_path = os.path.join(full_directory_path, filename)
                base_name, extension = os.path.splitext(filename)
                new_base_name = base_name.replace(old_name, new_name)
                new_file_name = new_base_name + extension
                new_file_path = os.path.join(full_directory_path, new_file_name)

                try:
                    os.rename(old_file_path, new_file_path)
                    print(f"Renamed: {old_file_path} to {new_file_path}")
                except Exception as e:
                    print(f"Error renaming {old_file_path} to {new_file_path}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Update file names in specified directories."
    )
    parser.add_argument("old_name", type=str, help="The old file name to be replaced.")
    parser.add_argument(
        "new_name", type=str, help="The new file name to replace the old one."
    )
    args = parser.parse_args()

    update_file_names(args.old_name, args.new_name)
