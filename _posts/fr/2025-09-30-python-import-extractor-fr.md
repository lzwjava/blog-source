---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Extracteur d'Import de Paquets Python
translated: true
type: note
---

### Script Python pour Extraire Tous les Packages Importés

Ce script parcourt un répertoire spécifié et ses sous-répertoires, trouve tous les fichiers Python (`.py`), analyse leurs instructions d'importation en utilisant le module `ast` de Python (pour une analyse syntaxique sûre), et accumule tous les noms de modules de base uniques (par exemple, `os` de `import os`, ou `collections` de `from collections import defaultdict`). Il ignore les modules intégrés et se concentre sur les modules externes.

Enregistrez ceci sous forme de fichier `.py` (par exemple, `extract_imports.py`) et exécutez-le avec un chemin de répertoire comme argument, comme `python extract_imports.py /chemin/vers/repertoire`.

```python
import os
import ast
import sys

def extract_imports_from_file(file_path):
    """
    Analyse un fichier Python et extrait les noms des modules importés.
    Gère les styles 'import mod' et 'from mod import item'.
    """
    modules = set()
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read(), filename=file_path)
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    modules.add(alias.name.split('.')[0])  # Obtenir le module de base (ex: 'import os.path' -> 'os')
            elif isinstance(node, ast.ImportFrom) and node.module:
                modules.add(node.module.split('.')[0])  # Obtenir le module de base de 'from mod.sub import ...'
    except Exception as e:
        print(f"Erreur lors de l'analyse de {file_path}: {e}")
    
    return modules

def get_all_imported_modules(directory):
    """
    Parcourt le répertoire et les sous-répertoires, collecte tous les modules importés uniques.
    """
    all_modules = set()
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                modules = extract_imports_from_file(file_path)
                all_modules.update(modules)
    
    # Exclure les modules intégrés courants (optionnel, car ce sont rarement des packages externes)
    excluded = {'sys', 'os', 're', 'math', 'random', 'json', 'time', 'datetime', 'collections', 'itertools', 'functools'}
    all_modules -= excluded
    
    return sorted(all_modules)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Utilisation: python extract_imports.py <chemin_du_répertoire>")
        sys.exit(1)
    
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Erreur: {directory} n'est pas un répertoire valide.")
        sys.exit(1)
    
    modules = get_all_imported_modules(directory)
    print("Tous les packages importés uniques:")
    for mod in modules:
        print(mod)
```

### Fonctionnement
- **Parcours de Répertoire** : Utilise `os.walk` pour visiter récursivement tous les sous-répertoires et fichiers.
- **Filtrage des Fichiers** : Ne traite que les fichiers `.py`.
- **Analyse des Imports** : Utilise `ast` pour analyser en toute sécurité le code source et identifier les nœuds `Import` et `ImportFrom`. Sépare sur `.` pour capturer le module de premier niveau (par exemple, `numpy` de `import numpy.linalg`).
- **Accumulation** : Collecte les modules dans un ensemble pour l'unicité, puis les trie et les affiche.
- **Cas Particuliers** : Ignore les modules intégrés (vous pouvez personnaliser l'ensemble `excluded`), gère les erreurs de syntaxe avec élégance et prend en charge les fichiers Unicode.
- **Sortie** : Une liste triée de noms de packages uniques. S'il est exécuté sur le répertoire de votre propre projet, il listera des packages comme `requests`, `pandas`, etc., que vous devrez installer.

Cette approche est efficace pour l'analyse d'une base de code et évite d'exécuter du code potentiellement non sécurisé. Si vous avez besoin de modifications (par exemple, gérer différemment les imports relatifs ou générer un requirements.txt), fournissez plus de détails !