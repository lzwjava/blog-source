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

def generate_random_dimensions(screen_width, screen_height):
    """Generate random terminal dimensions with full height"""
    # Estimate maximum characters based on screen size
    # Assuming 8px character width and accounting for borders
    max_chars_width = (screen_width - 40) // 8

    # Generate random width between 40% and 80% of max width
    min_width = max(40, max_chars_width // 5 * 2)  # 40% of max
    max_width = max_chars_width // 5 * 4  # 80% of max

    # Ensure minimum reasonable width
    min_width = max(min_width, 60)
    max_width = max(max_width, min_width + 20)

    # Generate random width
    term_width = random.randint(min_width, max_width)

    # Use full height (estimate lines based on screen height, minus borders)
    char_height_px = 16  # pixels per line
    effective_height = screen_height - 60  # account for window decorations
    term_height = max(20, effective_height // char_height_px)

    return term_width, term_height

def generate_random_position(screen_width, screen_height, term_width_px, term_height_px):
    """Generate random position for terminal window"""
    # Reserve some space for window borders/title bar (approx 30 pixels)
    effective_height = screen_height - 50
    effective_width = screen_width - 20

    # Ensure terminal fits within screen bounds
    max_x = max(0, effective_width - term_width_px)
    max_y = max(0, effective_height - term_height_px)

    # Generate random position
    x = random.randint(0, max_x)
    y = random.randint(0, max_y)

    return x, y

def open_terminal_at_position(x, y, term_width=80, term_height=24):
    """Open gnome-terminal at specified position with given dimensions"""
    try:
        # Use gnome-terminal with geometry (geometry is in characters, not pixels)
        cmd = [
            'gnome-terminal',
            '--geometry', f'{term_width}x{term_height}+{x}+{y}',
            '--working-directory', os.getcwd()
        ]

        subprocess.Popen(cmd)
        print(f"Opened terminal at position ({x}, {y}) with dimensions {term_width}x{term_height}")

    except subprocess.CalledProcessError as e:
        print(f"Error opening terminal: {e}")
        # Fallback to xterm if gnome-terminal not available
        try:
            cmd = [
                'xterm',
                '-geometry', f'{term_width}x{term_height}+{x}+{y}'
            ]
            subprocess.Popen(cmd)
            print(f"Opened xterm at position ({x}, {y}) with dimensions {term_width}x{term_height}")
        except Exception as ex:
            print(f"Error opening xterm: {ex}")

def main():
    screen_width, screen_height = get_screen_resolution()
    term_width, term_height = generate_random_dimensions(screen_width, screen_height)
    x, y = generate_random_position(screen_width, screen_height,
                                   term_width * 8, term_height * 16)
    open_terminal_at_position(x, y, term_width, term_height)

if __name__ == "__main__":
    main()