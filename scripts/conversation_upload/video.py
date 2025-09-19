#!/usr/bin/env python3

import sys
import os
from PIL import Image, ImageDraw, ImageFont
import subprocess
import json
import re
import select


def get_mp3_duration(mp3_file):
    """Get the duration of the MP3 file in seconds using ffprobe."""
    try:
        cmd = [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "json",
            mp3_file,
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        data = json.loads(result.stdout)
        return float(data["format"]["duration"])
    except (
        subprocess.CalledProcessError,
        KeyError,
        ValueError,
        FileNotFoundError,
    ) as e:
        print(
            f"Warning: Could not get duration of {mp3_file}. Progress percentage won't be shown. Error: {e}"
        )
        return None


def run_ffmpeg_with_progress(ffmpeg_cmd, mp3_file):
    """Run FFmpeg and show progress based on -progress output."""
    print("Starting FFmpeg video creation...")
    duration = get_mp3_duration(mp3_file)

    # Add progress and logging options, ensure overwrite with -y
    cmd = (
        ["ffmpeg", "-y"]
        + ffmpeg_cmd
        + ["-progress", "pipe:1", "-nostats", "-loglevel", "info"]
    )

    # Run FFmpeg with line-buffered output
    try:
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,  # Line buffering
            universal_newlines=True,
        )
    except FileNotFoundError:
        print(
            "Error: FFmpeg not found. Please ensure FFmpeg is installed and in your PATH."
        )
        sys.exit(1)

    # Regular expression to parse progress output
    time_re = re.compile(r"out_time_ms=(\d+)")

    # Use select to read stdout and stderr non-blocking
    outputs = [process.stdout, process.stderr]
    while process.poll() is None:
        readable, _, _ = select.select(outputs, [], [], 1.0)
        for stream in readable:
            line = stream.readline().strip()
            if not line:
                continue
            if stream == process.stderr:
                print(f"[FFmpeg Log] {line}")
            else:
                # Parse progress from stdout
                match = time_re.search(line)
                if match:
                    time_ms = int(match.group(1)) / 1_000_000  # Convert to seconds
                    if duration:
                        percentage = (time_ms / duration) * 100
                        print(
                            f"Progress: {time_ms:.1f}s / {duration:.1f}s ({percentage:.1f}%)"
                        )
                    else:
                        print(f"Progress: {time_ms:.1f}s")

    # Capture any remaining output
    stdout, stderr = process.communicate()
    for line in stdout.splitlines():
        line = line.strip()
        if line:
            match = time_re.search(line)
            if match:
                time_ms = int(match.group(1)) / 1_000_000
                if duration:
                    percentage = (time_ms / duration) * 100
                    print(
                        f"Progress: {time_ms:.1f}s / {duration:.1f}s ({percentage:.1f}%)"
                    )
                else:
                    print(f"Progress: {time_ms:.1f}s")
    for line in stderr.splitlines():
        line = line.strip()
        if line:
            print(f"[FFmpeg Log] {line}")

    # Check if FFmpeg completed successfully
    if process.returncode != 0:
        print(f"Error: FFmpeg failed with return code {process.returncode}.")
        sys.exit(1)

    print("FFmpeg video creation completed.")


# Get filename from command-line argument
if len(sys.argv) != 2:
    print("Error: Please provide a filename or path to an MP3 file.")
    print("Usage: python make_video.py <path_to_mp3>")
    sys.exit(1)

input_path = sys.argv[1]

# Handle the input path
if not os.path.isfile(input_path):
    print(f"Error: {input_path} not found.")
    sys.exit(1)

# Extract directory, filename, and base name
input_dir = os.path.dirname(input_path) or "."
filename_with_ext = os.path.basename(input_path)
base_filename = os.path.splitext(filename_with_ext)[0]  # Remove .mp3 if present
mp3_file = input_path  # Use the full input path for the MP3

# Step 1: Create cover image
print("Creating cover image...")
image_width, image_height = 1280, 720
image = Image.new("RGB", (image_width, image_height), "black")
draw = ImageDraw.Draw(image)

# Load a font (try Arial, then Helvetica, then default)
font = None
for font_path in ["/Library/Fonts/Arial.ttf", "/Library/Fonts/Helvetica.ttf"]:
    try:
        font = ImageFont.truetype(font_path, 72)  # 72pt font size
        print(f"Using font: {font_path}")
        break
    except IOError:
        continue
if font is None:
    font = ImageFont.load_default()
    print(
        "Warning: Neither Arial nor Helvetica font found, using default font. Note: Default font may not scale well to 72pt."
    )

# Get text size and position to center it
text = base_filename
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]
text_x = (image_width - text_width) / 2
text_y = (image_height - text_height) / 2

# Draw text (white color)
draw.text((text_x, text_y), text, fill="white", font=font)

# Save image in ~/Downloads/
jpg_file = os.path.expanduser(f"~/Downloads/{base_filename}.jpg")
image.save(jpg_file)
print(f"Cover image created: {jpg_file}")

# Step 2: Create video with FFmpeg
output_video = os.path.expanduser(f"~/Downloads/{base_filename}.mp4")
ffmpeg_cmd = [
    "-loop",
    "1",
    "-i",
    jpg_file,
    "-i",
    mp3_file,
    "-c:v",
    "libx264",
    "-tune",
    "stillimage",
    "-c:a",
    "aac",
    "-b:a",
    "192k",
    "-shortest",
    output_video,
]

run_ffmpeg_with_progress(ffmpeg_cmd, mp3_file)

print(f"Video created: {output_video}")
