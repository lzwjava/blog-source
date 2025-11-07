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
                    # Use frontmatter to parse the file
                    post = frontmatter.load(file_path)

                    # Check if the file has front matter
                    if not post.metadata:
                        continue

                    # Get the keys from the metadata
                    actual_keys = list(post.metadata.keys())
                    sorted_keys = sorted(actual_keys)

                    # Check if keys are in alphabetical order
                    if actual_keys != sorted_keys:
                        issues.append({
                            'file_path': file_path,
                            'post': post,
                            'actual_keys': actual_keys,
                            'sorted_keys': sorted_keys
                        })

                except Exception as e:
                    # Skip files that can't be parsed (not valid markdown, no front matter, etc.)
                    continue

    return issues

def fix_front_matter_key_order_for_file(file_path, post, actual_keys, sorted_keys):
    """Fix the front matter key order for a single file using frontmatter library."""
    try:
        # Create new metadata with sorted keys
        sorted_metadata = {}
        for key in sorted_keys:
            if key in post.metadata:
                sorted_metadata[key] = post.metadata[key]

        # Update the post with sorted metadata
        post.metadata = sorted_metadata

        # Write the file back with sorted front matter
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(frontmatter.dumps(post))

        return True

    except Exception as e:
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