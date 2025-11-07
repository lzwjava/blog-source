import os
import argparse
import frontmatter

def scan_markdown_files_for_front_matter_key_order(verbose=False):
    """Scan all markdown files for front matter where keys are not in alphabetical order."""
    issues = []
    total_files_scanned = 0
    directories_with_files = set()

    # Define directories to scan
    directories_to_scan = ['_posts', 'original', 'notes', '_notes']

    if verbose:
        print(f"Scanning directories: {', '.join(directories_to_scan)}")

    for directory in directories_to_scan:
        if not os.path.exists(directory):
            if verbose:
                print(f"Directory '{directory}' does not exist, skipping.")
            continue

        if verbose:
            print(f"Scanning directory: {directory}")

        # Walk through all subdirectories (recursive)
        for root, dirs, files in os.walk(directory):
            # Track directories that contain markdown files
            md_files_in_dir = [f for f in files if f.endswith('.md')]
            if md_files_in_dir and root != directory:
                directories_with_files.add(root)

            for filename in files:
                if not filename.endswith('.md'):
                    continue

                file_path = os.path.join(root, filename)
                total_files_scanned += 1

                if verbose and total_files_scanned % 100 == 0:
                    print(f"Scanned {total_files_scanned} files so far...")

                try:
                    # Use frontmatter to parse the file
                    post = frontmatter.load(file_path)

                    # Check if the file has front matter
                    if not post.metadata:
                        if verbose:
                            print(f"Skipping {file_path}: no front matter")
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
                        if verbose:
                            print(f"Found issue in {file_path}: keys out of order")

                except Exception as e:
                    # Skip files that can't be parsed (not valid markdown, no front matter, etc.)
                    if verbose:
                        print(f"Error parsing {file_path}: {e}")
                    continue

    if verbose:
        print(f"Total files scanned: {total_files_scanned}")
        if directories_with_files:
            print("Subdirectories containing markdown files:")
            for subdir in sorted(directories_with_files):
                print(f"  {subdir}")

    return issues, total_files_scanned

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

def fix_front_matter_key_order(max_files=None, verbose=False):
    """Fix front matter key order issues in all markdown files."""
    print("Scanning markdown files for front matter key order issues...")
    issues, total_scanned = scan_markdown_files_for_front_matter_key_order(verbose=verbose)

    if not issues:
        print("No front matter key order issues found.")
        if verbose:
            print(f"Total files scanned: {total_scanned}")
        return

    # Limit the number of files if specified
    if max_files:
        issues = issues[:max_files]
        print(f"Found {len(issues)} files with front matter key order issues (limited to {max_files}).")
    else:
        print(f"Found {len(issues)} files with front matter key order issues.")

    if verbose:
        print(f"Total files scanned: {total_scanned}")

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
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output showing directories and files being processed')
    args = parser.parse_args()

    fix_front_matter_key_order(max_files=args.number, verbose=args.verbose)