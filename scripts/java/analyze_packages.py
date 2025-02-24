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
    
    Uses the convention that package names are lowercase, while class names
    start with uppercase letters. Handles wildcard imports (*).
    
    Args:
        import_statement (str): The import statement line from a Java file.
    
    Returns:
        str: The package name, or empty string if not determined.
    """
    parts = import_statement.split()
    if parts[0] == 'import':
        parts = parts[1:]
    if parts[0] == 'static':
        parts = parts[1:]
    import_path = ' '.join(parts).strip(';').strip()
    identifiers = import_path.split('.')
    for i, ident in enumerate(identifiers):
        if ident == '*' or (ident and ident[0].isupper()):
            package_parts = identifiers[:i]
            break
    else:
        package_parts = []
    package = '.'.join(package_parts)
    return package

if __name__ == '__main__':
    # Check if a directory and level are provided
    if len(sys.argv) < 3:
        print("Usage: python script.py <root_directory> <level>")
        sys.exit(1)
    
    root_dir = sys.argv[1]
    try:
        level = int(sys.argv[2])
        if level < 1:
            raise ValueError
    except ValueError:
        print("[ERROR] Level must be a positive integer.")
        sys.exit(1)
    
    # Verify the directory exists
    if not os.path.isdir(root_dir):
        print(f"[ERROR] The specified path is not a directory: {root_dir}")
        sys.exit(1)
    
    # Log the start of the analysis
    print(f"[INFO] Starting analysis of directory: {root_dir} at level: {level}")
    
    # Initialize variables
    packages = set()
    total_files = 0
    error_files = 0
    
    # Process Java files
    for java_file in find_java_files(root_dir):
        try:
            with open(java_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('import'):
                        package = extract_package(line)
                        if package:
                            # Split the package name into parts and truncate to the specified level
                            parts = package.split('.')
                            truncated_package = '.'.join(parts[:level])
                            packages.add(truncated_package)
            total_files += 1
        except Exception as e:
            print(f"[ERROR] Could not read file {java_file}: {e}")
            error_files += 1
            continue
    
    # Print summary
    print(f"[INFO] Total Java files attempted: {total_files + error_files}")
    print(f"[INFO] Successfully processed: {total_files}")
    print(f"[INFO] Files with errors: {error_files}")
    print(f"[INFO] Total unique packages at level {level}: {len(packages)}")
    
    # Print results
    if packages:
        print(f"[INFO] Analysis complete. Printing unique packages at level {level}:")
        for package in sorted(packages):
            print(package)
    else:
        print("[INFO] No packages found.")