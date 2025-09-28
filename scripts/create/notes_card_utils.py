#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
import qrcode
import os

def center_crop_to_fit(img, target_width, target_height):
    """Center crop an image to fit target dimensions while preserving aspect ratio"""
    img_width, img_height = img.size
    target_ratio = target_width / target_height
    img_ratio = img_width / img_height

    if img_ratio > target_ratio:
        # Image is wider than target ratio, crop width
        new_width = int(img_height * target_ratio)
        offset = (img_width - new_width) // 2
        cropped_img = img.crop((offset, 0, offset + new_width, img_height))
    elif img_ratio < target_ratio:
        # Image is taller than target ratio, crop height
        new_height = int(img_width / target_ratio)
        offset = (img_height - new_height) // 2
        cropped_img = img.crop((0, offset, img_width, offset + new_height))
    else:
        # Same aspect ratio, no cropping needed
        cropped_img = img

    # Resize to exact target dimensions
    resized_img = cropped_img.resize((target_width, target_height), Image.Resampling.LANCZOS)
    return resized_img

def generate_share_card(titles, output_path, invitation=None, background_image_path=None):
    """Generate a share card image with note titles and QR code"""
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Image dimensions - iPhone 14 Pro Max aspect ratio (2.16:1)
    WIDTH = 1080
    HEIGHT = 1600

    # Split layout: Top half for generated image, bottom half for solid color background
    HALF_HEIGHT = HEIGHT // 2

    # Create split background image
    if background_image_path and os.path.exists(background_image_path):
        # Load background image and center crop to match aspect ratio
        bg_img = Image.open(background_image_path)
        img = Image.new('RGBA', (WIDTH, HEIGHT), color=(64, 0, 64, 255))  # Deep purple background

        # Crop AI image for top half
        bg_img = center_crop_to_fit(bg_img, WIDTH, HALF_HEIGHT)
        bg_img = bg_img.convert('RGBA')

        # Paste AI image on top half
        img.paste(bg_img, (0, 0))
    else:
        # Create image with solid purple background if no background image
        img = Image.new('RGBA', (WIDTH, HEIGHT), color=(64, 0, 64, 255))  # Deep purple

    draw = ImageDraw.Draw(img)

    try:
        # Try to use a nice font, fallback to default
        font_title = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 72)
        font_invitation = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 48)
        font_notes = ImageFont.truetype("/System/Library/Fonts/Arial Bold.ttf", 36)
    except:
        # Fallback to default font
        font_title = ImageFont.load_default()
        font_invitation = ImageFont.load_default()
        font_notes = ImageFont.load_default()

    # All text content is now in the bottom half (bottom area starts at HALF_HEIGHT)
    # Title
    if invitation:
        title = invitation
        title_font = font_invitation
    else:
        title = "Latest Notes"
        title_font = font_title

    base_y_offset = HALF_HEIGHT + 20  # Start text in bottom half
    draw.text((20, base_y_offset), title, fill='white', font=title_font)

    # List notes - adjust offset based on title height
    title_bbox = draw.textbbox((20, base_y_offset), title, font=title_font)
    y_offset = title_bbox[3] + 40  # Add some padding after title
    for title in titles:
        # Calculate text dimensions
        text = f"• {title}"
        text_bbox = draw.textbbox((0, 0), text, font=font_notes)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        # Create semi-transparent gray background rectangle
        padding = 8
        rect_x1 = 20 - padding
        rect_y1 = y_offset - padding
        rect_x2 = 20 + text_width + padding
        rect_y2 = y_offset + text_height + padding

        # Draw gray semi-transparent background
        draw.rectangle([rect_x1, rect_y1, rect_x2, rect_y2],
                      fill=(128, 128, 128, 180))  # Semi-transparent gray

        draw.text((20, y_offset), text, fill='white', font=font_notes)
        y_offset += 50

    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=15, border=5)
    qr.add_data("https://lzwjava.github.io/notes-en")
    qr.make(fit=True)

    # Create QR code image
    qr_img = qr.make_image(fill='black', back_color='white')

    # Resize QR code and place in bottom half - centered
    qr_size = 300
    qr_img = qr_img.resize((qr_size, qr_size))

    # Paste QR code on the image - centered in bottom half
    qr_x = (WIDTH - qr_size) // 2
    qr_y = HALF_HEIGHT + (HALF_HEIGHT - qr_size) // 2  # Center in bottom half
    img.paste(qr_img, (qr_x, qr_y))

    # Add QR code label
    label_height = draw.textbbox((0, 0), "Scan for more notes", font=font_notes)[3]
    label_y = qr_y - 40
    label_x = (WIDTH - draw.textbbox((0, 0), "Scan for more notes", font=font_notes)[2]) // 2
    draw.text((label_x, label_y), "Scan for more notes", fill='white', font=font_notes)

    # Save the image - convert back to RGB for compatibility
    if img.mode == 'RGBA':
        # Create a new RGB image
        rgb_img = Image.new('RGB', img.size, 'white')
        rgb_img.paste(img, mask=img.split()[-1])  # Use alpha channel as mask
        rgb_img.save(output_path)
    else:
        img.save(output_path)
    return output_path