#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
import qrcode
import os

def generate_share_card(titles, output_path):
    """Generate a share card image with note titles and QR code"""
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Image dimensions - iPhone 14 Pro Max aspect ratio (2.16:1)
    WIDTH = 1080
    HEIGHT = 1600

    # Create new image with white background
    img = Image.new('RGB', (WIDTH, HEIGHT), color='white')
    draw = ImageDraw.Draw(img)

    try:
        # Try to use a nice font, fallback to default
        font_title = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 72)
        font_notes = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 36)
    except:
        # Fallback to default font
        font_title = ImageFont.load_default()
        font_notes = ImageFont.load_default()

    # Title
    title = "Latest Notes"
    draw.text((20, 20), title, fill='black', font=font_title)

    # List notes
    y_offset = 120
    for title in titles:
        draw.text((20, y_offset), f"• {title}", fill='black', font=font_notes)
        y_offset += 50

    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=15, border=5)
    qr.add_data("https://lzwjava.github.io/notes-en")
    qr.make(fit=True)

    # Create QR code image
    qr_img = qr.make_image(fill='black', back_color='white')

    # Resize QR code and place on right side - larger for mobile viewing
    qr_size = 300
    qr_img = qr_img.resize((qr_size, qr_size))

    # Paste QR code on the image - centered at bottom
    qr_x = (WIDTH - qr_size) // 2
    qr_y = HEIGHT - qr_size - 100
    img.paste(qr_img, (qr_x, qr_y))

    # Add QR code label
    label_height = draw.textbbox((0, 0), "Scan for more notes", font=font_notes)[3]
    label_y = qr_y - 40
    label_x = (WIDTH - draw.textbbox((0, 0), "Scan for more notes", font=font_notes)[2]) // 2
    draw.text((label_x, label_y), "Scan for more notes", fill='black', font=font_notes)

    # Save the image
    img.save(output_path)
    return output_path