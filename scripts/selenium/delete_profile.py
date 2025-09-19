import os
import datetime
import argparse
from pathlib import Path

# Set up argument parser for dry run option
parser = argparse.ArgumentParser(
    description="Delete files in a directory created within a specific time range."
)
parser.add_argument(
    "--dry-run", action="store_true", help="Perform a dry run without deleting files"
)
args = parser.parse_args()

# Define the directory path
directory = "/home/lzw/Downloads"

# Define the time range for file creation (June 21, 2025, 00:51:00 to 00:52:59)
start_time = datetime.datetime(2025, 6, 21, 0, 51, 0)
end_time = datetime.datetime(2025, 6, 21, 0, 52, 59)


# Function to check if file was created within the specified time range
def is_file_in_time_range(file_path, start, end):
    try:
        ctime = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
        return start <= ctime <= end
    except OSError:
        return False


# Iterate through files in the directory
for item in Path(directory).iterdir():
    if item.is_file():  # Check if it's a file (not a directory)
        if is_file_in_time_range(item, start_time, end_time):
            if args.dry_run:
                print(f"Would delete: {item}")
            else:
                try:
                    item.unlink()  # Delete the file
                    print(f"Deleted: {item}")
                except OSError as e:
                    print(f"Error deleting {item}: {e}")
