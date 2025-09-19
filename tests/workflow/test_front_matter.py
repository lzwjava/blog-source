import unittest
import re
import os

def scan_markdown_files_for_front_matter_issues():
    """Scan all markdown files for front matter that doesn't have a newline after closing ---."""
    issues = []
    
    # Define directories to scan
    directories_to_scan = ['_posts', 'original']
    
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
                    
                    # Only check first 15 lines
                    content = ''.join(lines[:15])
                    
                    # Check if file starts with front matter
                    if not content.startswith('---\n'):
                        continue
                    
                    # Find the closing --- and check what follows
                    # Pattern: --- with content (including title) followed immediately by non-newline character
                    pattern = r'^---\n(.*?title.*?)\n---([^\n])'
                    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
                    
                    if match:
                        following_char = match.group(2)
                        # Find line number of the issue
                        front_matter_end = match.end() - 1  # Position of the character after ---
                        line_number = content[:front_matter_end].count('\n') + 1
                        
                        issues.append({
                            'file': file_path,
                            'line': line_number,
                            'following_char': repr(following_char),
                            'context': content[match.start():match.end()][:100]
                        })
                        
                except (UnicodeDecodeError, IOError) as e:
                    # Skip files that can't be read
                    continue
    
    return issues

class TestFrontMatter(unittest.TestCase):
    def test_front_matter_newline(self):
        """Test that front matter closing --- is followed by a newline."""
        front_matter_issues = scan_markdown_files_for_front_matter_issues()
        
        if front_matter_issues:
            details = "\n".join([
                f"{issue['file']}:{issue['line']} - Front matter closing --- immediately followed by {issue['following_char']}"
                for issue in front_matter_issues
            ])
            self.fail(f"Found {len(front_matter_issues)} front matter formatting issues:\n{details}")

if __name__ == '__main__':
    unittest.main()