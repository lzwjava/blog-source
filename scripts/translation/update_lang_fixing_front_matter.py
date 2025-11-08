#!/usr/bin/env python3

import sys
import os
import argparse
import re
from dotenv import load_dotenv
import concurrent.futures

# Add the project root to the Python path to import from tests
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from tests.workflow.test_front_matter import scan_markdown_files_for_front_matter_issues
from markdown_translate_client import translate_markdown_file
from update_lang_utils import get_original_file_for_post

load_dotenv()

MAX_THREADS = 10


def fix_front_matter_issues(issues, target_languages=None, dry_run=False, model="deepseek-v3.2"):
    """Fix front matter issues by retranslating affected files."""
    if not issues:
        print("No front matter formatting issues to fix.")
        return
    
    # Group issues by file
    files_with_issues = {}
    for issue in issues:
        file_path = issue['file']
        if file_path not in files_with_issues:
            files_with_issues[file_path] = []
        files_with_issues[file_path].append(issue)
    
    # Find original files and target languages for retranslation
    translation_jobs = []
    
    for post_file, file_issues in files_with_issues.items():
        print(f"\nProcessing {post_file} with {len(file_issues)} front matter issues:")
        for issue in file_issues:
            print(f"  Line {issue['line']}: Front matter closing --- immediately followed by {issue['following_char']}")

        # Find the original file
        original_info = get_original_file_for_post(post_file)
        if not original_info:
            print(f"  Warning: Could not find original file for {post_file}")
            continue

        original_file, current_lang = original_info
        print(f"  Original file: {original_file}")
        print(f"  Current language: {current_lang}")

        # Determine content type (post or note) by checking the original file's frontmatter
        try:
            with open(original_file, 'r', encoding='utf-8') as f:
                content = f.read()
            first_marker = content.find('---')
            second_marker = content.find('---', first_marker + 3)
            if first_marker != -1 and second_marker != -1:
                frontmatter = content[first_marker:second_marker + 3]
                content_type = 'note' if 'type: note' in frontmatter else 'post'
            else:
                content_type = 'post'  # Default to post if no frontmatter found
        except (UnicodeDecodeError, IOError) as e:
            print(f"  Warning: Could not read frontmatter from {original_file}: {e}")
            content_type = 'post'  # Default to post on error

        # Add retranslation job
        if not target_languages or current_lang in target_languages:
            translation_jobs.append((original_file, current_lang, content_type))
            print(f"  Added retranslation job: {original_file} -> {content_type}/{current_lang}")
    
    if not translation_jobs:
        print("No translation jobs to execute.")
        return
    
    if dry_run:
        print(f"\nDry run mode: Would retranslate {len(translation_jobs)} files:")
        for original_file, lang, content_type in translation_jobs:
            print(f"  {original_file} -> {content_type}/{lang}")
        return
    
    print(f"\nStarting retranslation of {len(translation_jobs)} files...")
    
    # Execute translation jobs
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = []
        for original_file, lang, content_type in translation_jobs:
            # Determine output directory based on content type
            if content_type == 'note':
                output_dir = f"_notes/{lang}"
            else:
                output_dir = f"_posts/{lang}"
            os.makedirs(output_dir, exist_ok=True)

            base_name = os.path.basename(original_file)
            # Replace original language suffix with target language
            for orig_suffix in ['-en.md', '-zh.md', '-ja.md']:
                if base_name.endswith(orig_suffix):
                    output_filename = base_name.replace(orig_suffix, f'-{lang}.md')
                    break
            else:
                print(f"Warning: Unexpected filename format: {base_name}")
                continue

            output_file = os.path.join(output_dir, output_filename)

            print(f"Submitting translation job: {original_file} -> {output_file}")
            future = executor.submit(
                translate_markdown_file, original_file, output_file, lang, model
            )
            futures.append(future)
        
        # Wait for all translations to complete
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
                print("Translation job completed successfully")
            except Exception as e:
                print(f"Translation job failed: {e}")


def main():
    """Main function to scan and fix front matter formatting issues."""
    parser = argparse.ArgumentParser(
        description="Fix front matter formatting issues by retranslating affected files."
    )
    parser.add_argument(
        "--lang",
        type=str,
        default="all",
        help="Target language to fix (e.g., zh, ja, all).",
    )
    parser.add_argument(
        "--dry_run",
        action="store_true",
        help="Perform a dry run without modifying files.",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="deepseek-v3.2",
        help="Model to use for translation (e.g., deepseek-v3, mistral-medium, gemini-flash).",
    )
    
    args = parser.parse_args()
    
    print("Scanning markdown files for front matter formatting issues...")
    issues = scan_markdown_files_for_front_matter_issues()
    
    if issues:
        print(f"\nFound {len(issues)} front matter formatting issues:")
        for issue in issues:
            print(f"{issue['file']}:{issue['line']} - Front matter closing --- immediately followed by {issue['following_char']}")
        
        # Determine target languages
        target_languages = None
        if args.lang != "all":
            target_languages = [args.lang]
        
        # Fix the issues by retranslating
        fix_front_matter_issues(issues, target_languages, args.dry_run, args.model)
    else:
        print("No front matter formatting issues found.")


if __name__ == '__main__':
    main()