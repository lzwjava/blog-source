import os
import glob
import datetime


def add_date_to_filename(filename):
    """Adds the file's modified date to the filename if it's not already present."""
    try:
        # Extract the directory and filename
        directory, filename_only = os.path.split(filename)

        # Extract the filename without extension and the extension
        name, ext = os.path.splitext(filename_only)

        # Check if the filename already starts with a date in YYYY-MM-DD format
        try:
            datetime.datetime.strptime(name[:10], "%Y-%m-%d")
            return filename  # Filename already has a date
        except ValueError:
            pass  # Filename does not start with a date

        # Get the file's last modified timestamp
        timestamp = os.path.getmtime(filename)

        # Convert the timestamp to a datetime object
        date = datetime.datetime.fromtimestamp(timestamp)

        # Format the date as YYYY-MM-DD
        date_str = date.strftime("%Y-%m-%d")

        # Create the new filename with the date prefix
        new_filename = os.path.join(directory, f"{date_str}-{name}{ext}")

        # Rename the file
        os.rename(filename, new_filename)
        return new_filename
    except Exception as e:
        print(f"Error processing {filename}: {e}")
        return filename


# Process all markdown files in the 'notes' directory
for filename in glob.glob("notes/*.md"):
    add_date_to_filename(filename)
