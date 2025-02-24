import os
import sys

def find_java_files(root_dir):
    """
    Recursively find all .java files in the given directory and its subdirectories.
    
    Args:
        root_dir (str): The root directory to start the search from.
    
    Yields:
        str: The full path to each .java file.
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.java'):
                yield os.path.join(dirpath, filename)

def extract_package(import_statement):
    """
    Extract the package name from an import statement.
    
    Uses the convention that package names are typically lowercase, while class names
    start with uppercase letters. For wildcard imports (*), the package is the part before '*'.
    
    Args:
        import_statement (str): The import statement line from a Java file.
    
    Returns:
        str: The package name, or empty string if not determined.
    """
    # Remove 'import' and 'static' if present
    parts = import_statement.split()
    if parts[0] == 'import':
        parts = parts[1:]
    if parts[0] == 'static':
        parts = parts[1:]
    
    # Join remaining parts and remove trailing ';'
    import_path = ' '.join(parts).strip(';').strip()
    
    # Split the import path by '.'
    identifiers = import_path.split('.')
    
    # Find the index where the first identifier starts with uppercase or is '*'
    for i, ident in enumerate(identifiers):
        if ident == '*' or (ident and ident[0].isupper()):
            package_parts = identifiers[:i]
            break
    else:
        package_parts = []
    
    package = '.'.join(package_parts)
    return package

if __name__ == '__main__':
    # Check command-line argument for root directory
    if len(sys.argv) < 2:
        print("Usage: python script.py <root_directory>")
        sys.exit(1)
    
    root_dir = sys.argv[1]
    packages = set()
    
    # Traverse all .java files in the directory and subdirectories
    for java_file in find_java_files(root_dir):
        try:
            with open(java_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('import'):
                        package = extract_package(line)
                        if package:  # Only add non-empty package names
                            packages.add(package)
        except Exception as e:
            print(f"Warning: Could not read file {java_file}: {e}")
            continue
    
    # Print the sorted list of unique packages
    for package in sorted(packages):
        print(package)