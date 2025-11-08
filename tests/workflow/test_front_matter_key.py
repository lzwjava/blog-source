import unittest
import re
import os

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

                    # Find the front matter block
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
                        # Find line number of the front matter start
                        front_matter_start = content.find('---\n') + 4  # After opening ---
                        line_number = content[:front_matter_start].count('\n') + 1

                        # Find first out-of-order key
                        first_out_of_order_index = None
                        for i in range(len(actual_keys) - 1):
                            if actual_keys[i] > actual_keys[i + 1]:
                                first_out_of_order_index = i
                                break

                        issues.append({
                            'file': file_path,
                            'line': line_number,
                            'expected_order': sorted_keys,
                            'actual_order': actual_keys,
                            'first_misplaced_key': actual_keys[first_out_of_order_index] if first_out_of_order_index is not None else None
                        })

                except (UnicodeDecodeError, IOError) as e:
                    # Skip files that can't be read
                    continue

    return issues

class TestFrontMatterKey(unittest.TestCase):
    def test_front_matter_key_order(self):
        """Test that front matter keys are in alphabetical order."""
        key_order_issues = scan_markdown_files_for_front_matter_key_order()

        if key_order_issues:
            details = "\n".join([
                f"{issue['file']}:{issue['line']} - Front matter keys not in alphabetical order. "
                f"First misplaced key: {issue['first_misplaced_key']}. "
                f"Expected: {issue['expected_order']}, Actual: {issue['actual_order']}"
                for issue in key_order_issues
            ])
            self.fail(f"Found {len(key_order_issues)} front matter key ordering issues:\n{details}")

if __name__ == '__main__':
    unittest.main()