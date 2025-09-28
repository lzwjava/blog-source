#!/usr/bin/env python3

import os
import sys
import subprocess
import argparse
import re
from pathlib import Path
from datetime import datetime
from notes_card_utils import generate_share_card

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
    parser.add_argument('-invite', metavar='NAME',
                       help='Name for invitation message (generates: "NAME invite you to read my latest ai notes")')

    args = parser.parse_args()

    notes_dir = Path(args.notes_dir).resolve()
    if not notes_dir.is_absolute():
        notes_dir = Path(__file__).parent / args.notes_dir

    # Get latest n notes
    latest_notes = get_latest_notes(notes_dir, args.n)

    if not latest_notes:
        print("No notes found")
        return

    # Extract titles
    titles = [get_note_title(note) for note in latest_notes]

    # Generate invitation text if provided
    invitation = None
    if args.invite:
        invitation = f"{args.invite}, invites you to read my latest AI notes"

    # Generate share card with timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    output_path = f"tmp/share_card_{timestamp}.png"
    card_path = generate_share_card(titles, output_path, invitation)

    print(f"Share card generated: {card_path}")
    if invitation:
        print(f"Invitation: {invitation}")
    print("Titles included:")
    for title in titles:
        print(f"• {title}")
    print(f"QR code links to: https://lzwjava.github.io/notes-en")

if __name__ == "__main__":
    main()