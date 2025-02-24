---
audio: false
lang: fr
layout: post
title: Analyser les Packages Java dans un Projet
translated: true
---

Sur la base de votre requête, vous souhaitez un script où, si le paramètre `level` est 0 ou non fourni, il utilise le nom complet du package (toutes ses parties), en traitant `level = 0` comme "infini" ou "utiliser toutes les parties", au lieu de le limiter à un nombre spécifique de parties (comme seulement la première partie lorsque `level = 1`). Ci-dessous, je vais expliquer comment cela peut être mis en œuvre dans un script Python qui analyse les fichiers Java pour extraire les noms de packages, et je vais fournir une solution complète adaptée à votre demande.

### Compréhension de la Requête
- **Lorsque `level = 0` ou non fourni** : Utiliser le nom de package complet tel qu'extrait des instructions `import` Java (par exemple, `java.util` ou `com.google.common.eventbus`), sans le tronquer.
- **Lorsque `level > 0`** : Tronquer le nom du package aux premières `level` parties (par exemple, pour `com.google.common.eventbus`, `level = 2` donnerait `com.google`).
- Le script doit toujours traiter les fichiers Java, extraire les noms de packages des instructions `import` et gérer les cas limites de manière appropriée.

### Approche de la Solution
1. **Analyse des Arguments** :
   - Si seul le répertoire racine est fourni (par exemple, `python script.py /path/to/dir`), définir `level = 0`, ce qui signifie utiliser le nom de package complet.
   - Si `level` est fourni (par exemple, `python script.py /path/to/dir 2`), l'utiliser pour tronquer le nom du package, en s'assurant qu'il s'agit d'un entier non négatif.
   - Quitter avec une erreur si les arguments sont invalides.

2. **Extraction du Package** :
   - Extraire le nom du package des instructions `import` (par exemple, `import java.util.ArrayList;` donne `java.util`).
   - Utiliser les conventions de nommage Java : les packages sont généralement en minuscules, et les noms de classes commencent par une majuscule.

3. **Logique de Troncature du Package** :
   - Si `level = 0`, ajouter le nom de package complet à l'ensemble des résultats.
   - Si `level > 0`, diviser le nom du package par des points (`.`) et prendre les premières `level` parties.

4. **Journalisation et Sortie** :
   - Indiquer clairement si les noms de packages complets ou tronqués sont utilisés.
   - Lister tous les packages uniques trouvés.

### Mise en Œuvre
Voici le script Python complet qui répond à vos exigences :

```python
import os
import sys

def find_java_files(root_dir):
    """
    Rechercher de manière récursive tous les fichiers .java dans le répertoire donné et ses sous-répertoires.

    Args:
        root_dir (str): Le répertoire racine à partir duquel commencer la recherche.

    Yields:
        str: Le chemin complet de chaque fichier .java.
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        print(f"[INFO] Entrer dans le répertoire : {dirpath}")
        for filename in filenames:
            if filename.endswith('.java'):
                yield os.path.join(dirpath, filename)

def extract_package(import_statement):
    """
    Extraire le nom du package d'une instruction import.

    Supposons que les noms de packages sont en minuscules et s'arrêtent aux noms de classes (majuscules) ou aux jokers (*).

    Args:
        import_statement (str): La ligne d'instruction import d'un fichier Java.

    Returns:
        str: Le nom du package, ou une chaîne vide si non déterminé.
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
    # Analyser les arguments de la ligne de commande
    if len(sys.argv) == 2:
        root_dir = sys.argv[1]
        level = 0  # Aucun niveau fourni, utiliser les noms de packages complets
    elif len(sys.argv) == 3:
        root_dir = sys.argv[1]
        try:
            level = int(sys.argv[2])
            if level < 0:
                raise ValueError
        except ValueError:
            print("[ERREUR] Le niveau doit être un entier non négatif.")
            sys.exit(1)
    else:
        print("Utilisation : python script.py <répertoire_racine> [niveau]")
        sys.exit(1)

    # Vérifier que le répertoire existe
    if not os.path.isdir(root_dir):
        print(f"[ERREUR] Le chemin spécifié n'est pas un répertoire : {root_dir}")
        sys.exit(1)

    # Journaliser le début de l'analyse
    if level == 0:
        print(f"[INFO] Démarrage de l'analyse du répertoire : {root_dir} avec les noms de packages complets.")
    else:
        print(f"[INFO] Démarrage de l'analyse du répertoire : {root_dir} au niveau : {level}")

    # Initialiser les variables
    packages = set()
    total_files = 0
    error_files = 0

    # Traiter les fichiers Java
    for java_file in find_java_files(root_dir):
        print(f"[INFO] Traitement du fichier : {java_file}")
        try:
            with open(java_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('import'):
                        package = extract_package(line)
                        if package:
                            if level == 0:
                                # Utiliser le nom de package complet
                                packages.add(package)
                            else:
                                # Tronquer aux premières 'level' parties
                                parts = package.split('.')
                                truncated_package = '.'.join(parts[:level])
                                packages.add(truncated_package)
            total_files += 1
        except Exception as e:
            print(f"[ERREUR] Impossible de lire le fichier {java_file} : {e}")
            error_files += 1
            continue

    # Afficher le résumé
    print(f"[INFO] Total des fichiers Java tentés : {total_files + error_files}")
    print(f"[INFO] Traités avec succès : {total_files}")
    print(f"[INFO] Fichiers avec erreurs : {error_files}")
    if level == 0:
        print(f"[INFO] Total des packages complets uniques : {len(packages)}")
    else:
        print(f"[INFO] Total des packages uniques au niveau {level} : {len(packages)}")

    # Afficher les résultats
    if packages:
        if level == 0:
            print("[INFO] Analyse terminée. Affichage des packages complets uniques :")
        else:
            print(f"[INFO] Analyse terminée. Affichage des packages uniques au niveau {level} :")
        for package in sorted(packages):
            print(package)
    else:
        print("[INFO] Aucun package trouvé.")
```

### Fonctionnement
- **Exécution du Script** :
  - `python script.py /path/to/java/project` : Analyse tous les fichiers `.java` dans le répertoire et utilise les noms de packages complets (`level = 0`).
  - `python script.py /path/to/java/project 2` : Tronque les noms de packages aux deux premières parties (par exemple, `com.google.common.eventbus` devient `com.google`).

- **Exemple de Sortie** :
  Supposons que vous avez un fichier Java avec :
  ```java
  import java.util.ArrayList;
  import com.google.common.eventbus.EventBus;
  ```
  - **Avec `level = 0` (ou aucun niveau fourni)** :
    ```
    [INFO] Démarrage de l'analyse du répertoire : /path/to/java/project avec les noms de packages complets.
    [INFO] Entrer dans le répertoire : /path/to/java/project
    [INFO] Traitement du fichier : /path/to/java/project/MyFile.java
    [INFO] Total des fichiers Java tentés : 1
    [INFO] Traités avec succès : 1
    [INFO] Fichiers avec erreurs : 0
    [INFO] Total des packages complets uniques : 2
    [INFO] Analyse terminée. Affichage des packages complets uniques :
    com.google.common.eventbus
    java.util
    ```
  - **Avec `level = 2`** :
    ```
    [INFO] Démarrage de l'analyse du répertoire : /path/to/java/project au niveau : 2
    [INFO] Entrer dans le répertoire : /path/to/java/project
    [INFO] Traitement du fichier : /path/to/java/project/MyFile.java
    [INFO] Total des fichiers Java tentés : 1
    [INFO] Traités avec succès : 1
    [INFO] Fichiers avec erreurs : 0
    [INFO] Total des packages uniques au niveau 2 : 2
    [INFO] Analyse terminée. Affichage des packages uniques au niveau 2 :
    com.google
    java.util
    ```

- **Caractéristiques Clés** :
  - **Noms de Packages Complets** : Lorsque `level = 0` ou non passé, il utilise le nom de package complet tel qu'extrait (par exemple, `java.util`, `com.google.common.eventbus`).
  - **Troncature** : Lorsque `level > 0`, il prend les premières `level` parties.
  - **Gestion des Erreurs** : Vérifie la validité du répertoire et du `level` non négatif.
  - **Uniqueness** : Stocke les packages dans un `set` pour éviter les doublons.

### Cas Limites Gérés
- **Niveau Manquant** : Par défaut, `level = 0`, utilise les noms de packages complets.
- **Niveau Invalide** : Quitte avec une erreur si `level` est négatif ou non entier.
- **Packages Courts** : Si un package a moins de parties que `level` (par exemple, `java` avec `level = 2`), il utilise le package complet (`java`).
- **Imports Vides** : Ignore les lignes où aucun package n'est extrait.