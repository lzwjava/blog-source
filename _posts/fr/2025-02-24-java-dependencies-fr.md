---
audio: true
lang: fr
layout: post
title: Analyser les dépendances Java
translated: true
---

Voici un script Python qui parcourt tous les fichiers `.java` d'un projet, analyse leurs dépendances en fonction des déclarations d'importation et produit un graphe de dépendances au format DOT sous forme de "texte de dépendance." Ce script se concentre sur les dépendances internes entre les classes au sein du projet, fournissant une représentation claire qui peut être visualisée à l'aide d'outils comme Graphviz.

### Vue d'ensemble du script
Le script :
1. **Parcourt le répertoire du projet** de manière récursive pour trouver tous les fichiers `.java`.
2. **Analyse les dépendances** en extrayant les déclarations de package et les déclarations d'importation de chaque fichier `.java`.
3. **Produit un texte de dépendance** au format DOT, montrant des arêtes dirigées entre les classes où une classe importe une autre au sein du projet.

Voici le script complet :

```python
import os
import sys
import re
from collections import defaultdict

def get_package(file_path):
    """
    Extrait le nom du package d'un fichier .java.

    Args:
        file_path (str): Chemin vers le fichier .java.

    Returns:
        str: Le nom du package, ou None s'il n'est pas trouvé.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.search(r'^\s*package\s+([\w.]+);', line)
                if match:
                    return match.group(1)
    except Exception as e:
        print(f"Attention : Impossible de lire {file_path} : {e}")
    return None

def get_specific_imports(file_path):
    """
    Extrait les importations de classes spécifiques d'un fichier .java, en excluant les importations génériques.

    Args:
        file_path (str): Chemin vers le fichier .java.

    Returns:
        list: Liste des noms de classes importées qualifiés.
    """
    imports = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.search(r'^\s*import\s+([\w.]+);', line)
                if match:
                    imp = match.group(1)
                    # Exclure les importations génériques (par exemple, import java.util.*;)
                    if not imp.endswith('.*'):
                        imports.append(imp)
    except Exception as e:
        print(f"Attention : Impossible de lire {file_path} : {e}")
    return imports

if __name__ == '__main__':
    # Vérifier l'argument de la ligne de commande
    if len(sys.argv) != 2:
        print("Utilisation : python script.py <répertoire_racine>")
        sys.exit(1)

    root_dir = sys.argv[1]
    all_classes = set()

    # Première passe : Collecter tous les noms de classes qualifiés dans le projet
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                package = get_package(file_path)
                if package:
                    class_name = file.replace('.java', '')
                    full_class_name = f"{package}.{class_name}"
                    all_classes.add(full_class_name)

    # Stocker les dépendances : classe -> ensemble des classes dont elle dépend
    dependencies = defaultdict(set)

    # Deuxième passe : Analyser les dépendances en fonction des importations spécifiques
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
                        # Inclure uniquement les dépendances sur les classes au sein du projet
                        # Exclure les dépendances sur soi-même
                        if imp in all_classes and imp != full_class_name:
                            dependencies[full_class_name].add(imp)

    # Produire le graphe de dépendances au format DOT
    print('digraph G {')
    for class_name in sorted(dependencies):
        for dep in sorted(dependencies[class_name]):
            print(f'  "{class_name}" -> "{dep}";')
    print('}')
```

### Fonctionnement
#### 1. **Entrée en ligne de commande**
- Le script attend un seul argument : le répertoire racine du projet Java.
- Exemple d'utilisation : `python script.py /chemin/vers/projet`
- Si aucun argument n'est fourni, il affiche les instructions d'utilisation et se termine.

#### 2. **Recherche des fichiers `.java`**
- Utilise `os.walk()` pour parcourir récursivement le répertoire spécifié et identifier tous les fichiers se terminant par `.java`.

#### 3. **Extraction des informations de classe**
- **Extraction du package** : La fonction `get_package` lit chaque fichier `.java` et utilise une expression régulière (`^\s*package\s+([\w.]+);`) pour trouver la déclaration de package (par exemple, `package com.mycompany.myproject;`).
  - Retourne `None` si aucun package n'est trouvé ou si le fichier ne peut pas être lu.
- **Nom de la classe** : Suppose que le nom de la classe correspond au nom du fichier (par exemple, `MyClass.java` définit `MyClass`).
- **Nom qualifié complet** : Combine le package et le nom de la classe (par exemple, `com.mycompany.myproject.MyClass`).

#### 4. **Collecte de toutes les classes**
- Lors de la première passe, construit un ensemble de tous les noms de classes qualifiés dans le projet pour une recherche rapide ultérieure.

#### 5. **Analyse des dépendances**
- **Extraction des importations** : La fonction `get_specific_imports` extrait les déclarations d'importation en utilisant une expression régulière (`^\s*import\s+([\w.]+);`), en excluant les importations génériques (par exemple, `import java.util.*;`).
  - Exemple : À partir de `import com.mycompany.myproject.utils.Helper;`, elle extrait `com.mycompany.myproject.utils.Helper`.
- **Mappage des dépendances** : Pour chaque fichier `.java` :
  - Obtient son nom de classe qualifié complet.
  - Vérifie ses importations spécifiques.
  - Si une classe importée est dans l'ensemble des classes du projet et n'est pas la classe elle-même, ajoute une dépendance.

#### 6. **Production du texte de dépendance**
- Produit un graphe dirigé au format DOT :
  - Commence par `digraph G {`.
  - Pour chaque classe avec des dépendances, imprime des arêtes comme `"ClassA" -> "ClassB";`.
  - Se termine par `}`.
- Les classes et dépendances sont triées pour une sortie cohérente.
- Exemple de sortie :
  ```
  digraph G {
    "com.mycompany.myproject.ClassA" -> "com.mycompany.myproject.utils.Helper";
    "com.mycompany.myproject.ClassB" -> "com.mycompany.myproject.ClassA";
  }
  ```

### Exemple d'utilisation
1. Enregistrez le script sous le nom `analyze_deps.py`.
2. Exécutez-le :
   ```bash
   python analyze_deps.py /chemin/vers/projet/java
   ```
3. Redirigez la sortie vers un fichier :
   ```bash
   python analyze_deps.py /chemin/vers/projet/java > dependances.dot
   ```
4. Visualisez avec Graphviz :
   ```bash
   dot -Tpng dependances.dot -o dependances.png
   ```
   Cela génère une image PNG montrant le graphe de dépendances.

### Hypothèses et limitations
- **Une classe publique par fichier** : Suppose que chaque fichier `.java` contient une seule classe publique nommée d'après le fichier, selon la convention Java.
- **Dépendances basées sur les importations** : Ne considère que les dépendances indiquées par les déclarations d'importation spécifiques (par exemple, `import com.example.SomeClass;`), ignorant les importations génériques (`import com.example.*;`) et les références au même package (qui ne nécessitent pas d'importations).
- **Focus interne** : Ne suit que les dépendances entre les classes au sein du projet, ignorant les bibliothèques externes.
- **Analyse de base** : Utilise des expressions régulières pour la simplicité, ce qui peut manquer des cas particuliers (par exemple, des importations dans des commentaires). Un analyseur Java complet serait plus robuste mais complexe.

### Personnalisation
- **Format de sortie** : Modifiez les instructions d'impression pour changer le format du texte de dépendance (par exemple, une liste simple au lieu de DOT).
- **Gestion des erreurs** : Améliorée avec des blocs try-except pour ignorer les fichiers illisibles de manière élégante.
- **Portée** : Pourrait être étendu pour inclure des dépendances externes ou des dépendances au même package avec une analyse de code plus approfondie.

Ce script fournit un point de départ pratique pour l'analyse des dépendances, adapté pour comprendre la structure d'un projet Java à travers ses relations internes de classes.