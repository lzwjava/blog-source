import unittest

import os
from collections import defaultdict

SUPPORTED_LANGUAGES = ['en', 'zh', 'ja', 'es', 'hi', 'fr', 'de', 'ar', 'hant']

def extract_note_base_name(filename):
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

def scan_translated_notes():
    notes_by_base_name = defaultdict(set)
    for language in SUPPORTED_LANGUAGES:
        notes_directory = f"_posts/{language}"
        if not os.path.exists(notes_directory):
            continue
        for filename in os.listdir(notes_directory):
            if not filename.endswith('.md'):
                continue
            filepath = os.path.join(notes_directory, filename)
            if not is_note_type(filepath):
                continue
            base_name = extract_note_base_name(filename)
            detected_language = extract_language_from_filename(filename)
            if detected_language == language:
                notes_by_base_name[base_name].add(language)
    return notes_by_base_name

def is_note_type(filepath):
    """Check if a file has type: note in its frontmatter"""
    if not os.path.exists(filepath):
        return False
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        first_marker = content.find('---')
        second_marker = content.find('---', first_marker + 3)
        if first_marker == -1 or second_marker == -1:
            return False  # Not proper frontmatter
        frontmatter = content[first_marker:second_marker + 3]
        return 'type: note' in frontmatter
    except:
        return False

def scan_en_notes_as_reference():
    """Scan _posts/en as the reference for what notes should exist across all languages"""
    reference_note_names = set()
    reference_directory = "_posts/en"
    if not os.path.exists(reference_directory):
        return reference_note_names
    for filename in os.listdir(reference_directory):
        if not filename.endswith('.md'):
            continue
        filepath = os.path.join(reference_directory, filename)
        if not is_note_type(filepath):
            continue
        base_name = extract_note_base_name(filename)
        # Verify this is indeed an English note
        if filename.endswith('-en.md'):
            reference_note_names.add(base_name)
    return reference_note_names

def analyze_notes_completeness():
    all_supported_languages = set(SUPPORTED_LANGUAGES)
    translated_notes = scan_translated_notes()
    reference_notes = scan_en_notes_as_reference()
    orphaned_notes = []
    complete_notes = []

    # Check each reference note for completeness across all languages
    for base_name in reference_notes:
        available_languages = translated_notes.get(base_name, set())
        missing_languages = all_supported_languages - available_languages
        note_info = {
            'base_name': base_name,
            'available_languages': sorted(available_languages),
            'missing_languages': sorted(missing_languages),
            'has_original_source': True  # Reference notes are in en
        }
        if missing_languages:
            orphaned_notes.append(note_info)
        else:
            complete_notes.append(note_info)
    return orphaned_notes, complete_notes

class TestNotesComplete(unittest.TestCase):
    def test_no_orphaned_notes(self):
        orphaned_notes, complete_notes = analyze_notes_completeness()
        details = "\n".join([f"{note['base_name']}: Available: {', '.join(note['available_languages'])}, Missing: {', '.join(note['missing_languages'])}, Has original: {note['has_original_source']}" for note in orphaned_notes])
        self.assertEqual(len(orphaned_notes), 0, f"There are {len(orphaned_notes)} orphaned notes:\n{details}")

if __name__ == '__main__':
    unittest.main()