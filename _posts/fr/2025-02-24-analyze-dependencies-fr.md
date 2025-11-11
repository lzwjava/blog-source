---
audio: false
generated: true
lang: fr
layout: post
title: Analyser les Dépendances Java
translated: true
type: note
---

Pour répondre à votre question, je vais modifier le script Python fourni pour générer un graphe de dépendances pour les classes Java, où les dépendances sont regroupées par un "niveau" spécifié de la hiérarchie des packages. Par exemple, si `level=1`, les packages sont regroupés au niveau supérieur (par exemple, "org"), et si `level=2`, ils sont regroupés au deuxième niveau (par exemple, "org.springframework"). Cela signifie qu'avant d'analyser les dépendances, nous accumulons les classes en groupes basés sur les premières parties `level` de leurs noms de package, et le graphe montrera les dépendances entre ces groupes plutôt qu'entre les classes individuelles.

Voici le script modifié, suivi d'une explication des changements et de la manière dont il répond à vos exigences.

### Script Modifié

```python
import os
import sys
import re
from collections import defaultdict

def get_package(file_path):
    """
    Extraire le nom du package d'un fichier .java.

    Args:
        file_path (str): Chemin vers le fichier .java.

    Returns:
        str: Le nom du package, ou None si non trouvé.
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
    Extraire les imports de classes spécifiques d'un fichier .java, en excluant les imports wildcard.

    Args:
        file_path (str): Chemin vers le fichier .java.

    Returns:
        list: Liste des noms de classes importés entièrement qualifiés.
    """
    imports = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.search(r'^\s*import\s+([\w.]+);', line)
                if match:
                    imp = match.group(1)
                    # Exclure les imports wildcard (par exemple, import java.util.*;)
                    if not imp.endswith('.*'):
                        imports.append(imp)
    except Exception as e:
        print(f"Warning: Could not read {file_path}: {e}")
    return imports

def get_package_group(full_class_name, level):
    """
    Obtenir le groupe de package basé sur les premières parties 'level' du nom du package.

    Args:
        full_class_name (str): Nom de classe entièrement qualifié (par exemple, "org.springframework.boot.App").
        level (int): Nombre de niveaux de package à inclure (par exemple, 1 pour "org", 2 pour "org.springframework").

    Returns:
        str: Le groupe de package (par exemple, "org" ou "org.springframework").
    """
    package = '.'.join(full_class_name.split('.')[:-1])  # Extraire le package, en excluant le nom de la classe
    parts = package.split('.')
    if len(parts) <= level:
        return package  # Utiliser le package complet s'il a moins ou autant de parties que level
    else:
        return '.'.join(parts[:level])  # Utiliser les premières parties 'level'

if __name__ == '__main__':
    # Vérifier les arguments de ligne de commande : root_directory et level
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

    all_classes = set()

    # Premier passage : Collecter tous les noms de classes entièrement qualifiés dans le projet
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                package = get_package(file_path)
                if package:
                    class_name = file.replace('.java', '')
                    full_class_name = f"{package}.{class_name}"
                    all_classes.add(full_class_name)

    # Stocker les dépendances entre les groupes de packages
    group_dependencies = set()

    # Deuxième passage : Analyser les dépendances basées sur les groupes de packages
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                package = get_package(file_path)
                if package:
                    class_name = file.replace('.java', '')
                    full_class_name = f"{package}.{class_name}"
                    importer_group = get_package_group(full_class_name, level)
                    imports = get_specific_imports(file_path)
                    for imp in imports:
                        # Inclure uniquement les dépendances sur les classes du projet
                        # Exclure les auto-dépendances
                        if imp in all_classes and imp != full_class_name:
                            imported_group = get_package_group(imp, level)
                            if imported_group != importer_group:
                                group_dependencies.add((importer_group, imported_group))

    # Sortir le graphe de dépendances au format DOT
    print('digraph G {')
    for from_group, to_group in sorted(group_dependencies):
        print(f'  "{from_group}" -> "{to_group}";')
    print('}')
```

### Explication des Changements

1. **Arguments de Ligne de Commande** :
   - **Original** : `python script.py <root_directory>`
   - **Modifié** : `python script.py <root_directory> <level>`
   - Ajout de la prise en charge d'un deuxième argument, `level`, qui spécifie le niveau de la hiérarchie des packages. Le script vérifie qu'exactement deux arguments sont fournis et que `level` est un entier positif.

2. **Nouvelle Fonction : `get_package_group`** :
   - Ajout d'une fonction pour calculer le groupe de package pour une classe basé sur le `level` spécifié.
   - Pour un nom de classe entièrement qualifié (par exemple, "org.springframework.boot.App"), elle extrait le package ("org.springframework.boot"), le divise en parties ("org", "springframework", "boot"), et prend les premières parties `level` :
     - Si `level=1` : Retourne "org".
     - Si `level=2` : Retourne "org.springframework".
     - Si le package a moins de parties que `level` (par exemple, "com.example" avec `level=3`), il retourne le package complet ("com.example").

3. **Regroupement des Dépendances** :
   - **Original** : Utilisait `defaultdict(set)` pour stocker les dépendances entre les classes individuelles.
   - **Modifié** : Utilise un `set` (`group_dependencies`) pour stocker les arêtes dirigées entre les groupes de packages sous forme de tuples `(from_group, to_group)`.
   - Pour chaque classe :
     - Calcule son groupe de package (`importer_group`) en utilisant `get_package_group`.
     - Pour chaque import spécifique qui est dans le projet (`imp in all_classes`) et qui n'est pas la classe elle-même (`imp != full_class_name`) :
       - Calcule le groupe de package de la classe importée (`imported_group`).
       - Si les groupes diffèrent (`imported_group != importer_group`), ajoute une arête à `group_dependencies`.
   - Le `set` garantit l'unicité, donc plusieurs dépendances entre les mêmes groupes résultent en une seule arête.

4. **Sortie DOT** :
   - **Original** : Imprimait les arêtes entre les classes individuelles (par exemple, "org.springframework.boot.App" -> "org.apache.commons.IOUtils").
   - **Modifié** : Imprime les arêtes entre les groupes de packages (par exemple, "org.springframework" -> "org.apache" pour `level=2`).
   - Les arêtes sont triées pour une sortie cohérente.

### Comment il Répond à Vos Exigences

- **Prise en charge des Niveaux** : Le script accepte maintenant un paramètre `level` pour regrouper les packages avant d'analyser les dépendances.
- **Niveau = 1** : Regroupe toutes les classes par leur package de niveau supérieur (par exemple, "org"). Par exemple, "org.springframework.boot.App" et "org.apache.commons.IOUtils" appartiennent tous deux au groupe "org", donc les imports entre eux au sein de "org" ne sont pas affichés comme des arêtes.
- **Niveau = 2** : Regroupe les classes par les deux premiers niveaux de packages (par exemple, "org.springframework"). Par exemple, un import de "org.springframework.boot.App" vers "org.apache.commons.IOUtils" crée une arête de "org.springframework" vers "org.apache".
- **Accumuler les Packages Avant l'Analyse des Dépendances** : Le script détermine le groupe de package de chaque classe basé sur `level` avant d'analyser ses imports, garantissant que les dépendances sont entre les groupes, et non les classes individuelles.
- **Conformité à l'Exemple** : Pour votre exemple d'arête :
  - Original : `"org.springframework.boot.web.servlet.server.Session" -> "org.springframework.boot.convert.DurationUnit"`
  - Avec `level=2` : Les deux classes sont dans "org.springframework", donc aucune arête n'est ajoutée (même groupe).
  - Avec `level=3` : "org.springframework.boot.web" -> "org.springframework.boot.convert", ajoutant une arête entre ces groupes distincts.

### Exemples d'Utilisation

- **Commande** : `python script.py /path/to/project 1`
  - Groupes : "org", "com", etc.
  - La sortie peut inclure : `"org" -> "com"` si une classe dans un package "org" importe une classe dans un package "com".

- **Commande** : `python script.py /path/to/project 2`
  - Groupes : "org.springframework", "org.apache", etc.
  - La sortie peut inclure : `"org.springframework" -> "org.apache"`.

### Notes

- Le script maintient le comportement original de n'inclure que les dépendances intra-projet (imports dans `all_classes`) et d'exclure les imports wildcard et les auto-dépendances.
- Les classes sans déclaration de package sont ignorées, conformément au script original.
- La sortie est un graphe dirigé au format DOT, visualisable avec des outils comme Graphviz.

Ce script modifié devrait satisfaire pleinement votre demande de regrouper les dépendances par niveau de hiérarchie des packages.