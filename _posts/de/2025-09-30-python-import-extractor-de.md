---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Python-Paket-Import-Extraktor
translated: true
type: note
---

### Python-Skript zum Extrahieren aller importierten Pakete

Dieses Skript durchläuft ein bestimmtes Verzeichnis und seine Unterverzeichnisse, findet alle Python-Dateien (`.py`), analysiert ihre Import-Anweisungen mit dem `ast`-Modul von Python (für sicheres, syntaxbewusstes Parsing) und sammelt alle eindeutigen Basis-Modulnamen (z.B. `os` von `import os` oder `collections` von `from collections import defaultdict`). Es ignoriert Built-ins und konzentriert sich auf externe Module.

Speichern Sie dies als eine `.py`-Datei (z.B. `extract_imports.py`) und führen Sie sie mit einem Verzeichnispfad als Argument aus, z.B. `python extract_imports.py /pfad/zum/verzeichnis`.

```python
import os
import ast
import sys

def extract_imports_from_file(file_path):
    """
    Parses a Python file and extracts imported module names.
    Handles 'import mod' and 'from mod import item' styles.
    """
    modules = set()
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read(), filename=file_path)
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    modules.add(alias.name.split('.')[0])  # Get base module (e.g., 'import os.path' -> 'os')
            elif isinstance(node, ast.ImportFrom) and node.module:
                modules.add(node.module.split('.')[0])  # Get base module from 'from mod.sub import ...'
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
    
    return modules

def get_all_imported_modules(directory):
    """
    Walks through the directory and subdirectories, collects all unique imported modules.
    """
    all_modules = set()
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                modules = extract_imports_from_file(file_path)
                all_modules.update(modules)
    
    # Exclude common builtins (optional, as they are rarely external packages)
    excluded = {'sys', 'os', 're', 'math', 'random', 'json', 'time', 'datetime', 'collections', 'itertools', 'functools'}
    all_modules -= excluded
    
    return sorted(all_modules)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_imports.py <directory_path>")
        sys.exit(1)
    
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        sys.exit(1)
    
    modules = get_all_imported_modules(directory)
    print("All unique imported packages:")
    for mod in modules:
        print(mod)
```

### So funktioniert es
- **Verzeichnis-Durchlauf**: Verwendet `os.walk`, um rekursiv alle Unterverzeichnisse und Dateien zu besuchen.
- **Dateifilterung**: Verarbeitet nur `.py`-Dateien.
- **Import-Analyse**: Verwendet `ast`, um Quellcode sicher zu parsen und `Import`- und `ImportFrom`-Knoten zu identifizieren. Teilt den Modulnamen bei `.`, um das Top-Level-Modul zu erfassen (z.B. `numpy` von `import numpy.linalg`).
- **Sammlung**: Sammelt Module in einem Set für Eindeutigkeit, sortiert sie und gibt sie aus.
- **Sonderfälle**: Überspringt Built-ins (die `excluded`-Liste kann angepasst werden), behandelt Syntaxfehler elegant und unterstützt Unicode-Dateien.
- **Ausgabe**: Eine sortierte Liste eindeutiger Paketnamen. Wenn es im eigenen Projektverzeichnis ausgeführt wird, listet es Pakete wie `requests`, `pandas` etc. auf, die installiert werden müssten.

Dieser Ansatz ist effizient für die Codebasis-Analyse und vermeidet die Ausführung von potenziell unsicherem Code. Wenn Sie Anpassungen benötigen (z.B. andere Behandlung von relativen Imports oder das Erstellen einer requirements.txt), geben Sie bitte weitere Details an!