#!/usr/bin/env python3

import sys
import os
import argparse
import re
from dotenv import load_dotenv
import concurrent.futures

# Add the project root to the Python path to import from tests
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from tests.workflow.test_md_tables import scan_markdown_files_for_table_issues
from markdown_translate_client import translate_markdown_file

load_dotenv()

MAX_THREADS = 10


def get_original_file_for_post(post_file):
    """Find the original file for a given post file."""
    # Extract base name and language from post file
    # e.g., _posts/zh/2024-11-29-vision-tips-zh.md -> 2024-11-29-vision-tips, zh
    base_name = os.path.basename(post_file)
    if not base_name.endswith('.md'):
        return None
    
    # Remove .md extension
    base_name = base_name[:-3]
    
    # Extract language suffix
    lang_match = re.search(r'-([a-z]{2}|hant)$', base_name)
    if not lang_match:
        return None
    
    lang = lang_match.group(1)
    base_without_lang = base_name[:-len(lang)-1]  # Remove -lang suffix
    
    # Look for original file in preferred order
    preferred_orig_langs = ['en', 'zh', 'ja']
    for orig_lang in preferred_orig_langs:
        original_file = os.path.join('original', f"{base_without_lang}-{orig_lang}.md")
        if os.path.exists(original_file):
            return original_file, lang
    
    return None


def fix_table_issues(issues, target_languages=None, dry_run=False, model="deepseek-v3"):
    """Fix markdown table issues by retranslating affected files."""
    if not issues:
        print("No table formatting issues to fix.")
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
        print(f"\nProcessing {post_file} with {len(file_issues)} table issues:")
        for issue in file_issues:
            print(f"  Line {issue['line']}: Header '{issue['header']}' -> table")
        
        # Find the original file
        original_info = get_original_file_for_post(post_file)
        if not original_info:
            print(f"  Warning: Could not find original file for {post_file}")
            continue
        
        original_file, current_lang = original_info
        print(f"  Original file: {original_file}")
        print(f"  Current language: {current_lang}")
        
        # Add retranslation job
        if not target_languages or current_lang in target_languages:
            translation_jobs.append((original_file, current_lang))
            print(f"  Added retranslation job: {original_file} -> {current_lang}")
    
    if not translation_jobs:
        print("No translation jobs to execute.")
        return
    
    if dry_run:
        print(f"\nDry run mode: Would retranslate {len(translation_jobs)} files:")
        for original_file, lang in translation_jobs:
            print(f"  {original_file} -> {lang}")
        return
    
    print(f"\nStarting retranslation of {len(translation_jobs)} files...")
    
    # Execute translation jobs
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = []
        for original_file, lang in translation_jobs:
            # Determine output file
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
    """Main function to scan and fix markdown table formatting issues."""
    parser = argparse.ArgumentParser(
        description="Fix markdown table formatting issues by retranslating affected files."
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
        default="deepseek-v3",
        help="Model to use for translation (e.g., deepseek-v3, mistral-medium, gemini-flash).",
    )
    
    args = parser.parse_args()
    
    print("Scanning markdown files for table formatting issues...")
    issues = scan_markdown_files_for_table_issues()
    
    if issues:
        print(f"\nFound {len(issues)} markdown table formatting issues:")
        for issue in issues:
            print(f"{issue['file']}:{issue['line']} - Header '{issue['header']}' immediately followed by table")
        
        # Determine target languages
        target_languages = None
        if args.lang != "all":
            target_languages = [args.lang]
        
        # Fix the issues by retranslating
        fix_table_issues(issues, target_languages, args.dry_run, args.model)
    else:
        print("No table formatting issues found.")


if __name__ == '__main__':
    main()