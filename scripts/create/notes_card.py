#!/usr/bin/env python3

import os
import sys
import subprocess
import argparse
import re
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import qrcode

def get_latest_notes(notes_dir, count=10):
    """Get the latest modified notes sorted by modification time"""
    notes_path = Path(notes_dir)
    if not notes_path.exists():
        print(f"Notes directory {notes_dir} does not exist")
        return []
    
    notes = []
    for note_file in notes_path.glob("*.md"):
        mtime = note_file.stat().st_mtime
        notes.append((mtime, note_file))
    
    notes.sort(key=lambda x: x[0], reverse=True)
    return [note[1] for note in notes[:count]]

def get_note_url(note_filename):
    """Generate the URL for a note based on its filename"""
    base_name = note_filename.stem
    return f"https://lzwjava.github.io/notes/{base_name}"

def get_note_title(note_path):
    """Extract title from the frontmatter of a markdown file"""
    try:
        with open(note_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Look for frontmatter between --- delimiters
        frontmatter_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
        if frontmatter_match:
            frontmatter = frontmatter_match.group(1)
            # Look for title field
            title_match = re.search(r'^title:\s*(.+)$', frontmatter, re.MULTILINE)
            if title_match:
                return title_match.group(1).strip()

        # Fallback to filename without extension if no title found
        return note_path.stem
    except Exception as e:
        print(f"Warning: Could not read title from {note_path.name}: {e}")
        return note_path.stem

def generate_share_card(notes, output_path):
    """Generate a share card image with note titles and QR code"""
    # Image dimensions
    WIDTH = 800
    HEIGHT = 600

    # Create new image with white background
    img = Image.new('RGB', (WIDTH, HEIGHT), color='white')
    draw = ImageDraw.Draw(img)

    try:
        # Try to use a nice font, fallback to default
        font_title = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 24)
        font_notes = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 16)
    except:
        # Fallback to default font
        font_title = ImageFont.load_default()
        font_notes = ImageFont.load_default()

    # Title
    title = "Latest Notes"
    draw.text((20, 20), title, fill='black', font=font_title)

    # List notes
    y_offset = 80
    for i, note in enumerate(notes[:8]):  # Limit to 8 notes for space
        title = get_note_title(note)
        draw.text((20, y_offset), f"• {title}", fill='black', font=font_notes)
        y_offset += 30

    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data("https://lzwjava.github.io/notes-en")
    qr.make(fit=True)

    # Create QR code image
    qr_img = qr.make_image(fill='black', back_color='white')

    # Resize QR code and place on right side
    qr_size = 150
    qr_img = qr_img.resize((qr_size, qr_size))

    # Paste QR code on the image
    qr_x = WIDTH - qr_size - 20
    qr_y = HEIGHT - qr_size - 20
    img.paste(qr_img, (qr_x, qr_y))

    # Add QR code label
    draw.text((qr_x, qr_y - 25), "Scan for more notes", fill='black', font=font_notes)

    # Save the image
    img.save(output_path)
    return output_path

def open_browser(url):
    """Open URL in default browser"""
    try:
        if sys.platform.startswith('darwin'):
            subprocess.run(['open', url])
        elif sys.platform.startswith('win'):
            subprocess.run(['start', url], shell=True)
        else:
            subprocess.run(['xdg-open', url])
    except Exception as e:
        print(f"Failed to open browser: {e}")

def main():
    parser = argparse.ArgumentParser(description='Generate share card for latest notes')
    parser.add_argument('--notes-dir', default='./notes',
                       help='Path to notes directory (default: ./notes)')
    parser.add_argument('-n', type=int, default=5,
                       help='Number of latest notes to include (default: 5)')

    args = parser.parse_args()

    notes_dir = Path(args.notes_dir).resolve()
    if not notes_dir.is_absolute():
        notes_dir = Path(__file__).parent / args.notes_dir

    # Get latest n notes
    latest_notes = get_latest_notes(notes_dir, args.n)

    if not latest_notes:
        print("No notes found")
        return

    # Generate share card
    output_path = "share_card.png"
    card_path = generate_share_card(latest_notes, output_path)

    print(f"Share card generated: {card_path}")
    print("Titles included:")
    for i, note in enumerate(latest_notes):
        title = get_note_title(note)
        print(f"• {title}")
    print(f"QR code links to: https://lzwjava.github.io/notes-en")

if __name__ == "__main__":
    main()