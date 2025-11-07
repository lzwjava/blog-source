#!/usr/bin/env python3

import argparse
import os
import yaml
import re
from pathlib import Path
from datetime import datetime
from glob import glob

def get_post_types():
    """Get all available post types (directories under _posts)."""
    posts_dir = Path("_posts")
    if not posts_dir.exists():
        return []
    return [d.name for d in posts_dir.iterdir() if d.is_dir()]

def list_posts(post_type=None, detailed=False):
    """List posts, optionally filtered by type."""
    posts_dir = Path("_posts")
    posts = []

    if not posts_dir.exists():
        print(f"Error: _posts directory not found in {os.getcwd()}")
        return []

    pattern = f"**/*.md" if post_type is None else f"{post_type}/**/*.md"
    post_files = glob(str(posts_dir / pattern), recursive=True)

    for post_file in post_files:
        try:
            post_path = Path(post_file)
            posts.append(extract_post_info(post_path, detailed))
        except Exception as e:
            print(f"Warning: Could not process {post_file}: {e}")
            continue

    # Sort by date descending (most recent first)
    posts.sort(key=lambda x: x.get('date', datetime.min), reverse=True)
    return posts

def extract_post_info(post_path, detailed=False):
    """Extract information from a post file."""
    info = {
        'path': str(post_path),
        'type': post_path.parent.name,
        'filename': post_path.name,
        'date': None,
        'title': None,
        'lang': None,
        'generated': False,
        'audio': False,
        'image': False,
        'translated': False
    }

    # Parse date from filename (assuming format like 1995-06-30-childhood.md)
    match = re.match(r'(\d{4}-\d{2}-\d{2})-', post_path.name)
    if match:
        try:
            info['date'] = datetime.strptime(match.group(1), '%Y-%m-%d')
        except ValueError:
            pass

    # Read frontmatter for detailed info
    try:
        with open(post_path, 'r', encoding='utf-8') as f:
            content = f.read(1000)  # Read first part to find frontmatter
            frontmatter_match = re.search(r'^---\s*(.*?\n?)^---', content, re.DOTALL | re.MULTILINE)
            if frontmatter_match:
                frontmatter = frontmatter_match.group(1)
                try:
                    data = yaml.safe_load(frontmatter)
                    if data:
                        for key, value in data.items():
                            if key == 'title':
                                info['title'] = value
                            elif key in ['lang', 'generated', 'audio', 'image', 'translated']:
                                info[key] = value
                except yaml.YAMLError:
                    pass
    except Exception:
        pass

    return info

def display_posts(posts, detailed=False):
    """Display the list of posts."""
    if not posts:
        print("No posts found.")
        return

    for post in posts:
        if detailed:
            date_str = post['date'].strftime('%Y-%m-%d') if post['date'] else 'Unknown'
            print(f"[{date_str}] {post['type']}: {post.get('title', 'Untitled')}")
            print(f"  File: {post['path']}")
            if post.get('lang'):
                print(f"  Language: {post['lang']}")
            if post.get('translated'):
                print(f"  Translated: {'Yes' if post['translated'] else 'No'}")
            if post.get('generated'):
                print(f"  Generated: {'Yes' if post['generated'] else 'No'}")
            print()
        else:
            post_path = Path(post['path'])
            print(f"{post['type']}/{post_path.name}")

def main():
    parser = argparse.ArgumentParser(description='List blog posts by type or show all posts')
    parser.add_argument('--type', '-t', help='Specify post type (e.g., ar, en, zh). If not specified, shows all types.')
    parser.add_argument('--detailed', '-d', action='store_true', help='Show detailed information including titles and metadata')
    parser.add_argument('--types', action='store_true', help='List all available post types')
    parser.add_argument('--reverse', '-r', action='store_true', help='Sort in reverse chronological order (oldest first)')

    args = parser.parse_args()

    if args.types:
        types = get_post_types()
        if types:
            print("Available post types:")
            for post_type in sorted(types):
                print(f"  {post_type}")
        else:
            print("No post types found.")
        return

    posts = list_posts(args.type, args.detailed)

    if not args.reverse:
        # Already sorted descending by default
        pass
    else:
        # Reverse to oldest first
        posts.sort(key=lambda x: x.get('date', datetime.max), reverse=False)

    display_posts(posts, args.detailed)

if __name__ == "__main__":
    main()