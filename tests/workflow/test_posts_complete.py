import unittest

import os
from collections import defaultdict

SUPPORTED_LANGUAGES = ['en', 'zh', 'ja', 'es', 'hi', 'fr', 'de', 'ar', 'hant']

def extract_post_base_name(filename):
    base_name = filename.replace('.md', '')
    for lang in SUPPORTED_LANGUAGES:
        suffix = f'-{lang}'
        if base_name.endswith(suffix):
            return base_name[:-len(suffix)]
    return base_name

def extract_language_from_filename(filename):
    base_name = filename.replace('.md', '')
    for lang in SUPPORTED_LANGUAGES:
        if base_name.endswith(f'-{lang}'):
            return lang
    return None

def scan_translated_posts():
    posts_by_base_name = defaultdict(set)
    for language in SUPPORTED_LANGUAGES:
        posts_directory = f"_posts/{language}"
        if not os.path.exists(posts_directory):
            continue
        for filename in os.listdir(posts_directory):
            if not filename.endswith('.md'):
                continue
            base_name = extract_post_base_name(filename)
            detected_language = extract_language_from_filename(filename)
            if detected_language == language:
                posts_by_base_name[base_name].add(language)
    return posts_by_base_name

def scan_original_posts():
    original_post_names = set()
    original_directory = "original"
    if not os.path.exists(original_directory):
        return original_post_names
    for filename in os.listdir(original_directory):
        if not filename.endswith('.md'):
            continue
        base_name = extract_post_base_name(filename)
        original_post_names.add(base_name)
    return original_post_names

def analyze_post_completeness():
    all_supported_languages = set(SUPPORTED_LANGUAGES)
    translated_posts = scan_translated_posts()
    original_posts = scan_original_posts()
    orphaned_posts = []
    complete_posts = []
    for base_name, available_languages in translated_posts.items():
        missing_languages = all_supported_languages - available_languages
        post_info = {
            'base_name': base_name,
            'available_languages': sorted(available_languages),
            'missing_languages': sorted(missing_languages),
            'has_original_source': base_name in original_posts
        }
        if missing_languages:
            orphaned_posts.append(post_info)
        else:
            complete_posts.append(post_info)
    for base_name in original_posts:
        if base_name not in translated_posts:
            orphaned_posts.append({
                'base_name': base_name,
                'available_languages': [],
                'missing_languages': sorted(all_supported_languages),
                'has_original_source': True
            })
    return orphaned_posts, complete_posts

class TestPostsComplete(unittest.TestCase):
    def test_no_orphaned_posts(self):
        orphaned_posts, complete_posts = analyze_post_completeness()
        details = "\n".join([f"{post['base_name']}: Available: {', '.join(post['available_languages'])}, Missing: {', '.join(post['missing_languages'])}, Has original: {post['has_original_source']}" for post in orphaned_posts])
        self.assertEqual(len(orphaned_posts), 0, f"There are {len(orphaned_posts)} orphaned posts:\n{details}")

if __name__ == '__main__':
    unittest.main()