import os
import sys
import xml.etree.ElementTree as ET

# Define the namespace used in Maven pom.xml files
NS = "{http://maven.apache.org/POM/4.0.0}"

# Cache for groupId to avoid redundant parsing
group_id_cache = {}

def get_group_id(pom_path, root_pom):
    """
    Extract the groupId from a pom.xml file, considering inheritance from parent.
    
    Args:
        pom_path (str): Path to the pom.xml file.
        root_pom (str): Path to the root pom.xml file.
    
    Returns:
        str: The groupId of the module.
    """
    if pom_path in group_id_cache:
        return group_id_cache[pom_path]
    
    tree = ET.parse(pom_path)
    root = tree.getroot()
    group_id_elem = root.find(NS + 'groupId')
    
    if group_id_elem is not None:
        group_id = group_id_elem.text.strip()
    else:
        parent_pom_path = get_parent_pom_path(pom_path, root_pom)
        if parent_pom_path is None:
            raise ValueError(f"Root pom.xml must specify groupId: {pom_path}")
        group_id = get_group_id(parent_pom_path, root_pom)
    
    group_id_cache[pom_path] = group_id
    return group_id

def get_parent_pom_path(pom_path, root_pom):
    """
    Determine the parent pom.xml path based on directory structure.
    
    Args:
        pom_path (str): Path to the current pom.xml file.
        root_pom (str): Path to the root pom.xml file.
    
    Returns:
        str or None: Path to the parent pom.xml, or None if it's the root.
    """
    if pom_path == root_pom:
        return None
    
    parent_dir = os.path.dirname(os.path.dirname(pom_path))
    parent_pom_path = os.path.join(parent_dir, 'pom.xml')
    
    if not os.path.exists(parent_pom_path):
        raise ValueError(f"Expected parent pom.xml at {parent_pom_path}")
    
    return parent_pom_path

def get_artifact_id(pom_path):
    """
    Extract the artifactId from a pom.xml file.
    
    Args:
        pom_path (str): Path to the pom.xml file.
    
    Returns:
        str: The artifactId of the module.
    """
    tree = ET.parse(pom_path)
    root = tree.getroot()
    artifact_id_elem = root.find(NS + 'artifactId')
    
    if artifact_id_elem is None:
        raise ValueError(f"pom.xml must specify artifactId: {pom_path}")
    
    return artifact_id_elem.text.strip()

def get_dependencies(pom_path):
    """
    Extract the list of dependencies from a pom.xml file.
    
    Args:
        pom_path (str): Path to the pom.xml file.
    
    Returns:
        list: List of tuples (groupId, artifactId) for each dependency.
    """
    tree = ET.parse(pom_path)
    root = tree.getroot()
    dependencies = []
    
    for dep in root.findall(NS + 'dependencies/' + NS + 'dependency'):
        dep_group_id_elem = dep.find(NS + 'groupId')
        dep_artifact_id_elem = dep.find(NS + 'artifactId')
        if dep_group_id_elem is not None and dep_artifact_id_elem is not None:
            dep_group_id = dep_group_id_elem.text.strip()
            dep_artifact_id = dep_artifact_id_elem.text.strip()
            dependencies.append((dep_group_id, dep_artifact_id))
    
    return dependencies

def get_package_group(relative_dir, level):
    """
    Determine the group of a module based on its relative directory path and level.
    
    Args:
        relative_dir (str): Relative path to the module's directory (e.g., "module1/submodule").
        level (int): Number of directory levels to include.
    
    Returns:
        str: The group name (e.g., "module1" for level=1, "module1.submodule" for level=2).
    """
    parts = relative_dir.split(os.sep)
    if len(parts) <= level:
        return '.'.join(parts)
    else:
        return '.'.join(parts[:level])

if __name__ == '__main__':
    # Check command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python script.py <root_directory> <level>")
        sys.exit(1)

    root_dir = sys.argv[1]
    try:
        level = int(sys.argv[2])
        if level < 1:
            raise ValueError
    except ValueError:
        print("Error: level must be a positive integer")
        sys.exit(1)

    # Verify root pom.xml exists
    root_pom = os.path.join(root_dir, 'pom.xml')
    if not os.path.exists(root_pom):
        print(f"Error: No pom.xml found in {root_dir}")
        sys.exit(1)

    # Find all pom.xml files
    pom_files = [os.path.join(root, file) for root, dirs, files in os.walk(root_dir)
                 for file in files if file == 'pom.xml']

    # Build modules dictionary: (groupId, artifactId) -> relative_dir
    modules = {}
    for pom_file in pom_files:
        if pom_file == root_pom:
            continue  # Skip root pom
        relative_dir = os.path.relpath(os.path.dirname(pom_file), root_dir)
        group_id = get_group_id(pom_file, root_pom)
        artifact_id = get_artifact_id(pom_file)
        modules[(group_id, artifact_id)] = relative_dir

    # Collect dependencies between groups
    group_dependencies = set()
    for pom_file in pom_files:
        if pom_file == root_pom:
            continue
        relative_dir = os.path.relpath(os.path.dirname(pom_file), root_dir)
        importer_group = get_package_group(relative_dir, level)
        dependencies = get_dependencies(pom_file)
        for dep_group_id, dep_artifact_id in dependencies:
            if (dep_group_id, dep_artifact_id) in modules:
                imported_relative_dir = modules[(dep_group_id, dep_artifact_id)]
                imported_group = get_package_group(imported_relative_dir, level)
                if importer_group != imported_group:
                    group_dependencies.add((importer_group, imported_group))

    # Output in DOT format
    print('digraph G {')
    for from_group, to_group in sorted(group_dependencies):
        print(f'  "{from_group}" -> "{to_group}";')
    print('}')