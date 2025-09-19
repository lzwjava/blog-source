import sys
import os
from PIL import Image

DPI = 72


def get_image_dimensions(image_path):
    """Gets image dimensions in pixels and points."""
    try:
        image = Image.open(image_path)
        width, height = image.size
        dpi = image.info.get("dpi", (DPI, DPI))
        print(f"  Image dimensions: width={width}, height={height}, dpi={dpi}")
        return width, height, dpi
    except Exception as e:
        print(f"Error opening or processing image: {e}")
        sys.exit(1)


file_path = sys.argv[1]
print(f"Processing image: {file_path}.jpg")

# Check if the file exists
if not os.path.exists(f"{file_path}.jpg"):
    print(f"Error: File {file_path}.jpg not found.")
    sys.exit(1)

# Get image dimensions using PIL
width, height, dpi = get_image_dimensions(f"{file_path}.jpg")

# Calculate scale factor based on desired height of 480, maintaining aspect ratio
scale_factor = 480 / height
print(f"  Calculated scale factor: {scale_factor}")

# Calculate new width based on scale factor
new_width = int(width * scale_factor)
print(f"  New width: {new_width}")

try:
    # Open the image
    image = Image.open(f"{file_path}.jpg")
    print("  Image opened successfully.")

    # Resize the image
    resized_image = image.resize((new_width, 480), Image.Resampling.LANCZOS)
    print("  Image resized successfully.")

    # Calculate the cropping box
    left = (resized_image.width - 854) / 2
    top = 0
    right = (resized_image.width + 854) / 2
    bottom = 480
    print(f"  Cropping box: left={left}, top={top}, right={right}, bottom={bottom}")

    # Crop the image
    cropped_image = resized_image.crop((left, top, right, bottom))
    print("  Image cropped successfully.")

    # Save the processed image, overwriting the original
    cropped_image.save(f"{file_path}.jpg")
    print(f"  Image saved to {file_path}.jpg")


except Exception as e:
    print(f"Error processing image: {e}")
    sys.exit(1)
