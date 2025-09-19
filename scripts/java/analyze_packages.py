import os
import sys
from collections import Counter


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
            if filename.endswith(".java"):
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
    if parts[0] == "import":
        parts = parts[1:]
    if parts[0] == "static":
        parts = parts[1:]
    import_path = " ".join(parts).strip(";").strip()
    identifiers = import_path.split(".")
    for i, ident in enumerate(identifiers):
        if ident == "*" or (ident and ident[0].isupper()):
            package_parts = identifiers[:i]
            break
    else:
        package_parts = []
    package = ".".join(package_parts)
    return package


if __name__ == "__main__":
    # Parse command-line arguments
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("Usage: python script.py <root_directory> [level] [--count]")
        sys.exit(1)

    root_dir = sys.argv[1]
    level = 0
    count = False

    if len(sys.argv) == 3:
        if sys.argv[2] == "--count":
            count = True
        elif sys.argv[2].isdigit():
            level = int(sys.argv[2])
        else:
            print(f"Invalid argument: {sys.argv[2]}")
            sys.exit(1)
    elif len(sys.argv) == 4:
        if sys.argv[3] == "--count" and sys.argv[2].isdigit():
            level = int(sys.argv[2])
            count = True
        else:
            print(f"Invalid arguments: {sys.argv[2]} {sys.argv[3]}")
            sys.exit(1)

    # Verify the directory exists
    if not os.path.isdir(root_dir):
        print(f"[ERROR] The specified path is not a directory: {root_dir}")
        sys.exit(1)

    # Log the start of the analysis
    level_str = "using full package names" if level == 0 else f"at level {level}"
    count_str = "with appearance counts" if count else ""
    print(f"[INFO] Starting analysis of directory: {root_dir} {level_str} {count_str}")

    # Initialize variables
    package_counter = Counter()
    total_files = 0
    error_files = 0

    # Process Java files
    for java_file in find_java_files(root_dir):
        try:
            with open(java_file, "r", encoding="utf-8") as f:
                file_packages = set()
                for line in f:
                    line = line.strip()
                    if line.startswith("import"):
                        package = extract_package(line)
                        if package:
                            if level > 0:
                                parts = package.split(".")
                                truncated_package = ".".join(parts[:level])
                            else:
                                truncated_package = package
                            file_packages.add(truncated_package)
            for pkg in file_packages:
                package_counter[pkg] += 1
            total_files += 1
        except Exception as e:
            print(f"[ERROR] Could not read file {java_file}: {e}")
            error_files += 1
            continue

    # Print summary
    print(f"[INFO] Total Java files attempted: {total_files + error_files}")
    print(f"[INFO] Successfully processed: {total_files}")
    print(f"[INFO] Files with errors: {error_files}")
    if count:
        print(f"[INFO] Total unique packages with counts: {len(package_counter)}")
    else:
        print(f"[INFO] Total unique packages: {len(package_counter)}")

    # Print results with appropriate sorting
    if package_counter:
        if count:
            print(
                "[INFO] Analysis complete. Printing unique packages with counts (sorted by count descending):"
            )
            # Sort by count descending, then by package name ascending
            for pkg, cnt in sorted(
                package_counter.items(), key=lambda x: (-x[1], x[0])
            ):
                print(f"{pkg}: {cnt}")
        else:
            print(
                "[INFO] Analysis complete. Printing unique packages (sorted by name ascending):"
            )
            # Sort by package name ascending
            for pkg in sorted(package_counter):
                print(pkg)
    else:
        print("[INFO] No packages found.")
