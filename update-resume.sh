#!/bin/bash

# Set source and destination directories
SOURCE_DIR="awesome-cv"
DEST_DIR="assets/resume"

# Define file mappings
FILES_TO_COPY=(
    "$SOURCE_DIR/resume.pdf $DEST_DIR/Zhiwei.Li.Resume.pdf"
    "$SOURCE_DIR/resume-zh.pdf $DEST_DIR/Zhiwei.Li.Resume.ZH.pdf"
)

# Ensure destination directory exists
mkdir -p "$DEST_DIR"

# Loop through files and copy them
for file_pair in "${FILES_TO_COPY[@]}"; do
    src=$(echo "$file_pair" | cut -d' ' -f1)
    dest=$(echo "$file_pair" | cut -d' ' -f2)

    if [ -f "$src" ]; then
        cp "$src" "$dest"
        echo "Copied $src to $dest"
    else
        echo "Warning: $src does not exist and was not copied."
    fi
done

echo "File copy and rename completed."
