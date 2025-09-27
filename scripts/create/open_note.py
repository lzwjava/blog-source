#!/usr/bin/env python3

import os
import sys
import subprocess
import argparse
from pathlib import Path

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
    parser = argparse.ArgumentParser(description='Open latest note in browser')
    parser.add_argument('position', nargs='?', type=int, default=1, 
                       help='Position of note to open (1=latest, 2=second latest, etc)')
    parser.add_argument('--notes-dir', default='./notes', 
                       help='Path to notes directory (default: ./notes)')
    
    args = parser.parse_args()
    
    notes_dir = Path(args.notes_dir).resolve()
    if not notes_dir.is_absolute():
        notes_dir = Path(__file__).parent / args.notes_dir
    
    latest_notes = get_latest_notes(notes_dir, args.position + 5)
    
    if not latest_notes:
        print("No notes found")
        return
    
    if args.position > len(latest_notes):
        print(f"Only {len(latest_notes)} notes available")
        return
    
    selected_note = latest_notes[args.position - 1]
    note_url = get_note_url(selected_note)
    
    print(f"Opening: {selected_note.name}")
    print(f"URL: {note_url}")
    
    open_browser(note_url)

if __name__ == "__main__":
    main()