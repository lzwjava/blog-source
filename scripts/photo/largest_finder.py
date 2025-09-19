import os
import subprocess
from pathlib import Path


def find_largest_videos(directory, top_n=10):
    video_extensions = {".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv", ".m4v"}
    video_files = []

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = Path(root) / file
            if file_path.suffix.lower() in video_extensions:
                size = file_path.stat().st_size
                video_files.append((file_path, size))
                print(
                    f"Found: {file_path} - {size / (1024 * 1024):.2f} MB"
                )  # Log all detected videos

    video_files.sort(key=lambda x: x[1], reverse=True)
    print("\nTop Largest Videos:")
    for i, (path, size) in enumerate(video_files[:top_n], 1):
        print(f"{i}. {path} - {size / (1024 * 1024):.2f} MB")
        get_video_metadata(path, i)


def get_video_metadata(video_path, rank):
    """Get metadata including creation_time for each video using ffmpeg"""
    try:
        # Run ffmpeg command to get metadata
        cmd = ["ffmpeg", "-i", str(video_path)]
        result = subprocess.run(cmd, stderr=subprocess.PIPE, text=True)

        # Search for creation_time in the output but only print the first occurrence
        print(f"Metadata for video #{rank}: {video_path}")
        creation_time_found = False
        for line in result.stderr.split("\n"):
            if "creation_time" in line and not creation_time_found:
                print(line.strip())
                creation_time_found = True
                break

        if not creation_time_found:
            print("No creation_time found in metadata")
        print("-" * 50)
    except Exception as e:
        print(f"Error getting metadata: {e}")


if __name__ == "__main__":
    photos_library_path = "/Users/lzwjava/Pictures/Photos Library.photoslibrary/"
    find_largest_videos(photos_library_path)
