import subprocess
import sys
import os
import subprocess
import re
from PIL import Image
from pdf2image import convert_from_path

A4_WIDTH_MM = 210
A4_HEIGHT_MM = 297
MARGIN_PERCENT = 0.005

def calculate_scale_factor(input_pdf):
    """
    Detects the dimensions of the first page of a PDF, analyzes whitespace,
    and calculates the scale factor based on the PDF content and target A4 dimensions with margins.
    Returns the scale factor or None if an error occurs.
    """
    print(f"Calculating scale factor for: {input_pdf}")
    try:
        images = convert_from_path(input_pdf, first_page=1, last_page=1)
        if not images:
            print("  Could not convert PDF to image.")
            return None
        
        image = images[0]
        width, height = image.size
        
        # Convert pixels to points (assuming 72 DPI, a common default)
        width_points = width * 72 / image.info.get('dpi', (72,72))[0]
        height_points = height * 72 / image.info.get('dpi', (72,72))[1]

        # Analyze whitespace (simplified - assumes white background)
        left_margin_px = width
        right_margin_px = 0
        top_margin_px = height
        bottom_margin_px = 0            
        
        found_content = False
        for x in range(width):
            for y in range(height):
                pixel = image.getpixel((x,y))
                if isinstance(pixel, tuple):
                    if pixel[0] < 250 or pixel[1] < 250 or pixel[2] < 250:
                        if not found_content:
                            left_margin_px = x
                            top_margin_px = y
                            found_content = True
                        
                        if x > right_margin_px:
                            right_margin_px = x
                        if y > bottom_margin_px:
                            bottom_margin_px = y
                elif pixel < 250:
                    if not found_content:
                        left_margin_px = x
                        top_margin_px = y
                        found_content = True
                    
                    if x > right_margin_px:
                        right_margin_px = x
                    if y > bottom_margin_px:
                        bottom_margin_px = y
        
        if found_content:
            content_width_px = right_margin_px - left_margin_px
            content_height_px = bottom_margin_px - top_margin_px
            
            right_margin_px = width - right_margin_px
            bottom_margin_px = height - bottom_margin_px

            # Convert whitespace to points
            left_margin_points = left_margin_px * 72 / image.info.get('dpi', (72,72))[0]
            right_margin_points = right_margin_px * 72 / image.info.get('dpi', (72,72))[0]
            top_margin_points = top_margin_px * 72 / image.info.get('dpi', (72,72))[1]
            bottom_margin_points = bottom_margin_px * 72 / image.info.get('dpi', (72,72))[1]

            print(f"  Content box: left={left_margin_px}, upper={top_margin_px}, right={right_margin_px}, lower={bottom_margin_px}")
            print(f"  Content dimensions (pixels): width={content_width_px}, height={content_height_px}")
            print(f"  Margins (points): left={left_margin_points}, right={right_margin_points}, top={top_margin_points}, bottom={bottom_margin_points}")
        else:
            print("  Could not determine content bounding box.")
            left_margin_points = 0
            right_margin_points = 0
            top_margin_points = 0
            bottom_margin_points = 0

        image.save("tmp-1.jpg")

        print(f"  Detected dimensions: width={width_points}, height={height_points}")
        
        content_width = width_points - left_margin_points - right_margin_points
        content_height = height_points - top_margin_points - bottom_margin_points
        print(f"  Content dimensions (points): width={content_width}, height={content_height}")

        if content_width <= 0 or content_height <= 0:
            print("Error: Could not determine content dimensions.")
            return None

        # Convert mm to points (1 mm = 2.83465 points)
        target_width = A4_WIDTH_MM * (1 - 2 * MARGIN_PERCENT) * 2.83465
        target_height = A4_HEIGHT_MM * (1 - 2 * MARGIN_PERCENT) * 2.83465
        print(f"  Target dimensions: width={target_width}, height={target_height}")


        width_scale = target_width / content_width
        height_scale = target_height / content_height
        print(f"  Calculated width scale: {width_scale}, height scale: {height_scale}")
        
        # Use the smaller scale factor to fit within both dimensions
        scale_factor = min(width_scale, height_scale)
        print(f"  Final scale factor: {scale_factor}")
        
        return scale_factor

    except Exception as e:
        print(f"Error getting PDF dimensions or calculating scale factor: {e}")
        return None


def scale_pdf(input_pdf, output_pdf, scale_factor):
    """Scales a PDF using pdfjam."""
    print(f"Scaling {input_pdf} to {output_pdf} with scale factor: {scale_factor}")
    try:
        subprocess.run(
            [
                "pdfjam",
                "--scale",
                str(scale_factor),
                input_pdf,
                "--outfile",
                output_pdf,
            ],
            check=True,
        )
        print(f"Successfully scaled {input_pdf} to {output_pdf}")
    except subprocess.CalledProcessError as e:
        print(f"Error scaling PDF: {e}")
    except FileNotFoundError:
        print("Error: pdfjam command not found. Please ensure it is installed and in your system's PATH.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python scale-pdf.py <input_pdf> <output_pdf>")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    print(f"Input PDF: {input_pdf}, Output PDF: {output_pdf}")
    
    if not os.path.exists(input_pdf):
        print(f"Error: Input PDF file not found: {input_pdf}")
        sys.exit(1)

    scale_factor = calculate_scale_factor(input_pdf)
    if scale_factor is None:
        sys.exit(1)

    scale_pdf(input_pdf, output_pdf, scale_factor)
