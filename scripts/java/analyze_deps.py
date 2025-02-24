import os
import sys
import re
from collections import defaultdict

def get_package(file_path):
    """
    Extract the package name from a .java file.

    Args:
        file_path (str): Path to the .java file.

    Returns:
        str: The package name, or None if not found.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.search(r'^\s*package\s+([\w.]+);', line)
                if match:
                    return match.group(1)
    except Exception as e:
        print(f"Warning: Could not read {file_path}: {e}")
    return None

def get_specific_imports(file_path):
    """
    Extract specific class imports from a .java file, excluding wildcard imports.

    Args:
        file_path (str): Path to the .java file.

    Returns:
        list: List of fully qualified imported class names.
    """
    imports = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.search(r'^\s*import\s+([\w.]+);', line)
                if match:
                    imp = match.group(1)
                    # Exclude wildcard imports (e.g., import java.util.*;)
                    if not imp.endswith('.*'):
                        imports.append(imp)
    except Exception as e:
        print(f"Warning: Could not read {file_path}: {e}")
    return imports

if __name__ == '__main__':
    # Check for command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <root_directory>")
        sys.exit(1)

    root_dir = sys.argv[1]
    all_classes = set()

    # First pass: Collect all fully qualified class names in the project
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                package = get_package(file_path)
                if package:
                    class_name = file.replace('.java', '')
                    full_class_name = f"{package}.{class_name}"
                    all_classes.add(full_class_name)

    # Store dependencies: class -> set of classes it depends on
    dependencies = defaultdict(set)

    # Second pass: Analyze dependencies based on specific imports
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                package = get_package(file_path)
                if package:
                    class_name = file.replace('.java', '')
                    full_class_name = f"{package}.{class_name}"
                    imports = get_specific_imports(file_path)
                    for imp in imports:
                        # Only include dependencies on classes within the project
                        # Exclude self-dependencies
                        if imp in all_classes and imp != full_class_name:
                            dependencies[full_class_name].add(imp)

    # Output the dependency graph in DOT format
    print('digraph G {')
    for class_name in sorted(dependencies):
        for dep in sorted(dependencies[class_name]):
            print(f'  "{class_name}" -> "{dep}";')
    print('}')