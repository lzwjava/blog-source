import os
from datetime import datetime

# Change to the directory where your files are
directory = './_posts'
os.chdir(directory)

# Define the date threshold
threshold_date = datetime(2022, 1, 1)

# Loop through each file
for filename in os.listdir('.'):
    if filename.endswith('.md'):
        # Extract the date from the filename
        date_str = '-'.join(filename.split('-')[0:3])

        # Parse the date
        try:
            file_date = datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            print(f"Skipping {filename}, date format error.")
            continue

        # Check if the file does not have "-cn" or "-en"
        if not filename.endswith('-cn.md') and not filename.endswith('-en.md'):
            # Extract the base name without the extension
            base_name = filename[:-3]

            # Determine the new suffix based on the date
            if file_date < threshold_date:
                new_suffix = '-cn'
            else:
                new_suffix = '-en'

            # Add the new suffix and rename the file
            new_filename = f"{base_name}{new_suffix}.md"
            os.rename(filename, new_filename)
            print(f"Renamed '{filename}' to '{new_filename}'")
        else:
            print(f"Skipped '{filename}', already has language suffix.")

print("Renaming completed.")
