import os


def make_modules(directory):
    """
    Make all directories under the given directory Python modules by adding an __init__.py file to them.
    """
    for dirpath, dirnames, filenames in os.walk(directory):
        # Create __init__.py if it doesn't exist
        init_file = os.path.join(dirpath, "__init__.py")
        if not os.path.exists(init_file):
            open(init_file, "a").close()  # creates an empty file
            print(f"Created {init_file}")


if __name__ == "__main__":
    # Get the parent directory of this script
    parent_dir = os.path.dirname(os.path.abspath(__file__))

    # Make all subdirectories modules
    make_modules(parent_dir)
    print("Done making modules.")
