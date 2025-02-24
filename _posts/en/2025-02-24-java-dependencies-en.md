---
audio: false
lang: en
layout: post
title: Analyze Java Dependencies
translated: false
---

Below is a Python script that scans all `.java` files in a project, analyzes their dependencies based on import statements, and outputs a dependency graph in DOT format as a "dependency text." This script focuses on internal dependencies between classes within the project, providing a clear representation that can be visualized using tools like Graphviz.

### Script Overview
The script:
1. **Scans the project directory** recursively to find all `.java` files.
2. **Analyzes dependencies** by extracting package declarations and import statements from each `.java` file.
3. **Outputs a dependency text** in DOT format, showing directed edges between classes where one class imports another within the project.

Here's the complete script:

```python
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
```

### How It Works
#### 1. **Command-Line Input**
- The script expects a single argument: the root directory of the Java project.
- Example usage: `python script.py /path/to/project`
- If no argument is provided, it prints usage instructions and exits.

#### 2. **Finding `.java` Files**
- Uses `os.walk()` to recursively traverse the specified directory and identify all files ending with `.java`.

#### 3. **Extracting Class Information**
- **Package Extraction**: The `get_package` function reads each `.java` file and uses a regular expression (`^\s*package\s+([\w.]+);`) to find the package declaration (e.g., `package com.mycompany.myproject;`).
  - Returns `None` if no package is found or if the file can't be read.
- **Class Name**: Assumes the class name matches the file name (e.g., `MyClass.java` defines `MyClass`).
- **Fully Qualified Name**: Combines package and class name (e.g., `com.mycompany.myproject.MyClass`).

#### 4. **Collecting All Classes**
- In the first pass, builds a set of all fully qualified class names in the project for quick lookup later.

#### 5. **Analyzing Dependencies**
- **Import Extraction**: The `get_specific_imports` function extracts import statements using a regex (`^\s*import\s+([\w.]+);`), excluding wildcard imports (e.g., `import java.util.*;`).
  - Example: From `import com.mycompany.myproject.utils.Helper;`, it extracts `com.mycompany.myproject.utils.Helper`.
- **Dependency Mapping**: For each `.java` file:
  - Gets its fully qualified class name.
  - Checks its specific imports.
  - If an imported class is in the project’s class set and not the class itself, adds a dependency.

#### 6. **Outputting Dependency Text**
- Outputs a directed graph in DOT format:
  - Starts with `digraph G {`.
  - For each class with dependencies, prints edges like `"ClassA" -> "ClassB";`.
  - Ends with `}`.
- Classes and dependencies are sorted for consistent output.
- Example output:
  ```
  digraph G {
    "com.mycompany.myproject.ClassA" -> "com.mycompany.myproject.utils.Helper";
    "com.mycompany.myproject.ClassB" -> "com.mycompany.myproject.ClassA";
  }
  ```

### Usage Example
1. Save the script as `analyze_deps.py`.
2. Run it:
   ```bash
   python analyze_deps.py /path/to/java/project
   ```
3. Redirect output to a file:
   ```bash
   python analyze_deps.py /path/to/java/project > dependencies.dot
   ```
4. Visualize with Graphviz:
   ```bash
   dot -Tpng dependencies.dot -o dependencies.png
   ```
   This generates a PNG image showing the dependency graph.

### Assumptions and Limitations
- **One Public Class per File**: Assumes each `.java` file contains one public class named after the file, per Java convention.
- **Import-Based Dependencies**: Only considers dependencies indicated by specific import statements (e.g., `import com.example.SomeClass;`), ignoring wildcard imports (`import com.example.*;`) and same-package references (which don’t require imports).
- **Internal Focus**: Only tracks dependencies between classes within the project, ignoring external libraries.
- **Basic Parsing**: Uses regex for simplicity, which may miss edge cases (e.g., imports within comments). A full Java parser would be more robust but complex.

### Customization
- **Output Format**: Modify the print statements to change the dependency text format (e.g., a plain list instead of DOT).
- **Error Handling**: Enhanced with try-except blocks to skip unreadable files gracefully.
- **Scope**: Could be extended to include external dependencies or same-package dependencies with deeper code analysis.

This script provides a practical starting point for dependency analysis, suitable for understanding the structure of a Java project through its internal class relationships.