import os
import argparse
import frontmatter

def scan_markdown_files_for_front_matter_key_order():
    """Scan all markdown files for front matter where keys are not in alphabetical order."""
    issues = []

    # Define directories to scan
    directories_to_scan = ['_posts', 'original', 'notes', '_notes']

    for directory in directories_to_scan:
        if not os.path.exists(directory):
            continue

        # Walk through all subdirectories
        for root, dirs, files in os.walk(directory):
            for filename in files:
                if not filename.endswith('.md'):
                    continue

                file_path = os.path.join(root, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()

                    # Only check first 50 lines for front matter
                    content = ''.join(lines[:50])

                    # Check if file starts with front matter
                    if not content.startswith('---\n'):
                        continue

                    # Find the first front matter block only (between first --- and first closing ---)
                    front_matter_match = re.search(r'^---\n(.*?)\n---', content, re.MULTILINE | re.DOTALL)
                    if not front_matter_match:
                        continue

                    front_matter_content = front_matter_match.group(1)

                    # Extract key lines (lines that contain colons, ignoring comments)
                    key_lines = []
                    for line in front_matter_content.split('\n'):
                        line = line.strip()
                        if ':' in line and not line.startswith('#'):
                            # Extract key (everything before the first colon)
                            key = line.split(':', 1)[0].strip()
                            key_lines.append((key, line))

                    # Check if keys are in alphabetical order
                    sorted_keys = sorted([key for key, _ in key_lines])
                    actual_keys = [key for key, _ in key_lines]

                    if actual_keys != sorted_keys:
                        issues.append({
                            'file_path': file_path,
                            'actual_keys': actual_keys,
                            'key_lines': key_lines,
                            'front_matter_content': front_matter_content
                        })

                except (UnicodeDecodeError, IOError) as e:
                    # Skip files that can't be read
                    continue

    return issues

def fix_front_matter_key_order_for_file(file_path, actual_keys, key_lines, front_matter_content):
    """Fix the front matter key order for a single file."""
    try:
        # Read the entire file
        with open(file_path, 'r', encoding='utf-8') as f:
            full_content = f.read()

        # Get the content before front matter
        content_before_front_matter = full_content.split('---', 2)[0] + '---\n'

        # Get the content after front matter
        parts = full_content.split('\n---\n', 2)
        if len(parts) >= 3:
            content_after_front_matter = parts[2]
        else:
            # Fallback for files without closing ---
            parts = full_content.split('---\n', 2)
            if len(parts) >= 3:
                content_after_front_matter = '---\n' + parts[2]
            else:
                content_after_front_matter = ''

        # Create sorted front matter
        sorted_lines = []
        for key in sorted(actual_keys):
            # Find the corresponding line for this key
            for k, line in key_lines:
                if k == key:
                    sorted_lines.append(line)
                    break

        # Reconstruct front matter with sorted keys
        new_front_matter = '\n'.join(sorted_lines)
        new_content = content_before_front_matter + new_front_matter + '\n---\n' + content_after_front_matter

        # Write back the file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return True

    except (UnicodeDecodeError, IOError) as e:
        print(f"Error fixing {file_path}: {e}")
        return False

def fix_front_matter_key_order(max_files=None):
    """Fix front matter key order issues in all markdown files."""
    print("Scanning markdown files for front matter key order issues...")
    issues = scan_markdown_files_for_front_matter_key_order()

    if not issues:
        print("No front matter key order issues found.")
        return

    # Limit the number of files if specified
    if max_files:
        issues = issues[:max_files]
        print(f"Found {len(issues)} files with front matter key order issues (limited to {max_files}).")
    else:
        print(f"Found {len(issues)} files with front matter key order issues.")

    fixed_count = 0
    for issue in issues:
        print(f"Fixing {issue['file_path']}...")
        success = fix_front_matter_key_order_for_file(
            issue['file_path'],
            issue['post'],
            issue['actual_keys'],
            issue['sorted_keys']
        )
        if success:
            fixed_count += 1
        else:
            print(f"Failed to fix {issue['file_path']}")

    print(f"Successfully fixed {fixed_count} out of {len(issues)} files.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fix front matter key order in markdown files.')
    parser.add_argument('-n', '--number', type=int, help='Limit the number of files to process')
    args = parser.parse_args()

    fix_front_matter_key_order(max_files=args.number)