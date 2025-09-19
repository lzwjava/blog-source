import os

# Directories to search for files
directories = ["_posts", "pages"]

# Loop through the specified directories
for directory in directories:
    # Check if the directory exists
    if os.path.exists(directory):
        # Loop through all the files in the directory
        for filename in os.listdir(directory):
            # Check if the file ends with '-cn.md'
            if filename.endswith("-cn.md"):
                # Create the new filename by replacing '-cn.md' with '-zh.md'
                new_filename = filename.replace("-cn.md", "-zh.md")

                # Get the full path for the old and new filenames
                old_file = os.path.join(directory, filename)
                new_file = os.path.join(directory, new_filename)

                # Rename the file
                os.rename(old_file, new_file)

                # Print the renaming result
                print(f"Renamed: {filename} -> {new_filename}")
    else:
        print(f"Directory {directory} does not exist.")
