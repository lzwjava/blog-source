#!/usr/bin/env python3
"""
Random Terminal Position Script
Opens a terminal at a random position on the screen for better multitasking
"""

import subprocess
import random
import os

def get_screen_resolution():
    """Get screen resolution using xrandr"""
    try:
        result = subprocess.run(['xrandr'], capture_output=True, text=True)
        for line in result.stdout.split('\n'):
            if '*' in line:
                # Parse resolution like "1920x1080 60.00*+"
                res_part = line.split()[0]
                width, height = map(int, res_part.split('x'))
                return width, height
    except Exception as e:
        print(f"Error getting screen resolution: {e}")
    return 1920, 1080  # Default fallback

def generate_random_position(screen_width, screen_height, term_width=80, term_height=24):
    """Generate random position for terminal window"""
    # Reserve some space for window borders/title bar (approx 30 pixels)
    effective_height = screen_height - 50
    effective_width = screen_width - 20

    # Terminal character dimensions (rough estimates)
    char_width_px = 8   # pixels per character
    char_height_px = 16 # pixels per line

    # Convert terminal dimensions to pixels
    term_width_px = term_width * char_width_px
    term_height_px = term_height * char_height_px

    # Ensure terminal fits within screen bounds
    max_x = max(0, effective_width - term_width_px)
    max_y = max(0, effective_height - term_height_px)

    # Generate random position
    x = random.randint(0, max_x)
    y = random.randint(0, max_y)

    return x, y

def open_terminal_at_position(x, y):
    """Open gnome-terminal at specified position"""
    try:
        # Use gnome-terminal with geometry (but note: geometry is in characters, not pixels)
        # We'll use the --geometry flag with character dimensions
        cmd = [
            'gnome-terminal',
            '--geometry', f'80x24+{x}+{y}',
            '--working-directory', os.getcwd()
        ]

        subprocess.Popen(cmd)
        print(f"Opened terminal at position ({x}, {y})")

    except subprocess.CalledProcessError as e:
        print(f"Error opening terminal: {e}")
        # Fallback to xterm if gnome-terminal not available
        try:
            cmd = [
                'xterm',
                '-geometry', f'80x24+{x}+{y}'
            ]
            subprocess.Popen(cmd)
            print(f"Opened xterm at position ({x}, {y})")
        except Exception as ex:
            print(f"Error opening xterm: {ex}")

def main():
    screen_width, screen_height = get_screen_resolution()
    x, y = generate_random_position(screen_width, screen_height)
    open_terminal_at_position(x, y)

if __name__ == "__main__":
    main()