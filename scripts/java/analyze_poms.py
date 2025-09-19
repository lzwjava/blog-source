import os
import sys
import xml.etree.ElementTree as ET

# Define the Maven POM namespace
NS = "{http://maven.apache.org/POM/4.0.0}"

# Cache for groupId to avoid redundant parsing
group_id_cache = {}


def get_group_id(pom_path, pom_map):
    """
    Extract the groupId from a pom.xml file, considering inheritance from parent.

    Args:
        pom_path (str): Path to the pom.xml file.
        pom_map (dict): Mapping of pom.xml paths to their parsed data.

    Returns:
        str: The groupId of the module.
    """
    if pom_path in group_id_cache:
        return group_id_cache[pom_path]

    tree = ET.parse(pom_path)
    root = tree.getroot()
    group_id_elem = root.find(NS + "groupId")

    if group_id_elem is not None:
        group_id = group_id_elem.text.strip()
    else:
        # Check for parent declaration
        parent = root.find(NS + "parent")
        if parent is not None:
            parent_group_id = parent.find(NS + "groupId").text.strip()
            parent_artifact_id = parent.find(NS + "artifactId").text.strip()
            parent_relative_path = parent.find(NS + "relativePath")
            if parent_relative_path is not None and parent_relative_path.text:
                parent_pom_path = os.path.normpath(
                    os.path.join(os.path.dirname(pom_path), parent_relative_path.text)
                )
            else:
                # Default to parent directory if relativePath is omitted
                parent_pom_path = os.path.join(
                    os.path.dirname(pom_path), "..", "pom.xml"
                )
                parent_pom_path = os.path.normpath(parent_pom_path)

            if parent_pom_path in pom_map:
                group_id = get_group_id(parent_pom_path, pom_map)
            else:
                raise ValueError(
                    f"Parent POM not found for {pom_path}: {parent_pom_path}"
                )
        else:
            raise ValueError(f"No groupId or parent specified in {pom_path}")

    group_id_cache[pom_path] = group_id
    return group_id


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
    artifact_id_elem = root.find(NS + "artifactId")

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

    for dep in root.findall(NS + "dependencies/" + NS + "dependency"):
        dep_group_id_elem = dep.find(NS + "groupId")
        dep_artifact_id_elem = dep.find(NS + "artifactId")
        if dep_group_id_elem is not None and dep_artifact_id_elem is not None:
            dep_group_id = dep_group_id_elem.text.strip()
            dep_artifact_id = dep_artifact_id_elem.text.strip()
            dependencies.append((dep_group_id, dep_artifact_id))

    return dependencies


if __name__ == "__main__":
    # Check command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python script.py <root_directory>")
        sys.exit(1)

    root_dir = sys.argv[1]
    if not os.path.isdir(root_dir):
        print(f"Error: {root_dir} is not a directory")
        sys.exit(1)

    # Step 1: Recursively find all pom.xml files
    pom_files = [
        os.path.join(root, file)
        for root, _, files in os.walk(root_dir)
        for file in files
        if file == "pom.xml"
    ]

    if not pom_files:
        print(f"No pom.xml files found in {root_dir}")
        sys.exit(1)

    # Step 2: Build a dictionary of all POMs for parent lookups
    pom_map = {pom_file: None for pom_file in pom_files}

    # Step 3: Extract module information
    modules = {}  # (groupId, artifactId) -> pom_path
    for pom_file in pom_files:
        try:
            group_id = get_group_id(pom_file, pom_map)
            artifact_id = get_artifact_id(pom_file)
            modules[(group_id, artifact_id)] = pom_file
        except ValueError as e:
            print(f"Warning: Skipping {pom_file} due to error: {e}")
            continue

    # Step 4: Analyze dependencies
    dependencies = set()
    for pom_file in pom_files:
        try:
            importer_group_id = get_group_id(pom_file, pom_map)
            importer_artifact_id = get_artifact_id(pom_file)
            importer_key = (importer_group_id, importer_artifact_id)
            deps = get_dependencies(pom_file)
            for dep_group_id, dep_artifact_id in deps:
                dep_key = (dep_group_id, dep_artifact_id)
                if dep_key in modules and dep_key != importer_key:
                    # Add dependency as (importer, imported) tuple using artifactId for simplicity
                    dependencies.add((importer_artifact_id, dep_artifact_id))
        except ValueError as e:
            print(f"Warning: Error processing dependencies in {pom_file}: {e}")
            continue

    # Step 5: Output in DOT format
    print("digraph G {")
    for from_module, to_module in sorted(dependencies):
        print(f'  "{from_module}" -> "{to_module}";')
    print("}")
