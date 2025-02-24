---
audio: false
lang: fr
layout: post
title: Analyser les Packages Java
translated: true
---

Sur la base de votre requête, vous souhaitez un script où, si le paramètre `level` est 0 ou non fourni, il utilise le nom du package complet (toutes ses parties), traitant ainsi `level = 0` comme "infini" ou "utiliser toutes les parties", au lieu de le limiter à un nombre spécifique de parties (comme seulement la première partie lorsque `level = 1`). Ci-dessous, je vais expliquer comment cela peut être mis en œuvre dans un script Python qui analyse les fichiers Java pour extraire les noms de packages, et je vais fournir une solution complète adaptée à votre demande.

### Compréhension de la Requête
- **Lorsque `level = 0` ou non fourni** : Utiliser le nom de package complet tel qu'extrait des instructions `import` Java (par exemple, `java.util` ou `com.google.common.eventbus`), sans le tronquer.
- **Lorsque `level > 0`** : Tronquer le nom du package aux premières `level` parties (par exemple, pour `com.google.common.eventbus`, `level = 2` donnerait `com.google`).
- Le script doit toujours traiter les fichiers Java, extraire les noms de packages des instructions `import` et gérer les cas limites de manière appropriée.

### Approche de la Solution
1. **Analyse des Arguments** :
   - Si seul le répertoire racine est fourni (par exemple, `python script.py /chemin/vers/rep`), définir `level = 0`, ce qui signifie utiliser le nom de package complet.
   - Si `level` est fourni (par exemple, `python script.py /chemin/vers/rep 2`), l'utiliser pour tronquer le nom du package, en s'assurant qu'il s'agit d'un entier non négatif.
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
from collections import Counter

def find_java_files(root_dir):
    """
    Rechercher récursivement tous les fichiers .java dans le répertoire donné et ses sous-répertoires.

    Args:
        root_dir (str): Le répertoire racine à partir duquel commencer la recherche.

    Yields:
        str: Le chemin complet de chaque fichier .java.
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.java'):
                yield os.path.join(dirpath, filename)

def extract_package(import_statement):
    """
    Extraire le nom du package d'une instruction d'importation.

    Utilise la convention que les noms de packages sont en minuscules, tandis que les noms de classes
    commencent par des lettres majuscules. Gère les importations sauvages (*).

    Args:
        import_statement (str): La ligne d'instruction d'importation d'un fichier Java.

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
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("Usage: python script.py <répertoire_racine> [level] [--count]")
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
            print(f"Argument invalide : {sys.argv[2]}")
            sys.exit(1)
    elif len(sys.argv) == 4:
        if sys.argv[3] == "--count" and sys.argv[2].isdigit():
            level = int(sys.argv[2])
            count = True
        else:
            print(f"Arguments invalides : {sys.argv[2]} {sys.argv[3]}")
            sys.exit(1)

    # Vérifier que le répertoire existe
    if not os.path.isdir(root_dir):
        print(f"[ERREUR] Le chemin spécifié n'est pas un répertoire : {root_dir}")
        sys.exit(1)

    # Journaliser le début de l'analyse
    level_str = "utilisation des noms de packages complets" if level == 0 else f"au niveau {level}"
    count_str = "avec des comptes d'apparitions" if count else ""
    print(f"[INFO] Début de l'analyse du répertoire : {root_dir} {level_str} {count_str}")

    # Initialiser les variables
    package_counter = Counter()
    total_files = 0
    error_files = 0

    # Traiter les fichiers Java
    for java_file in find_java_files(root_dir):
        try:
            with open(java_file, 'r', encoding='utf-8') as f:
                file_packages = set()
                for line in f:
                    line = line.strip()
                    if line.startswith('import'):
                        package = extract_package(line)
                        if package:
                            if level > 0:
                                parts = package.split('.')
                                truncated_package = '.'.join(parts[:level])
                            else:
                                truncated_package = package
                            file_packages.add(truncated_package)
            for pkg in file_packages:
                package_counter[pkg] += 1
            total_files += 1
        except Exception as e:
            print(f"[ERREUR] Impossible de lire le fichier {java_file} : {e}")
            error_files += 1
            continue

    # Afficher le résumé
    print(f"[INFO] Total des fichiers Java tentés : {total_files + error_files}")
    print(f"[INFO] Traités avec succès : {total_files}")
    print(f"[INFO] Fichiers avec erreurs : {error_files}")
    if count:
        print(f"[INFO] Total des packages uniques avec des comptes : {len(package_counter)}")
    else:
        print(f"[INFO] Total des packages uniques : {len(package_counter)}")

    # Afficher les résultats avec un tri approprié
    if package_counter:
        if count:
            print("[INFO] Analyse terminée. Affichage des packages uniques avec des comptes (triés par compte décroissant) :")
            # Trier par compte décroissant, puis par nom de package croissant
            for pkg, cnt in sorted(package_counter.items(), key=lambda x: (-x[1], x[0])):
                print(f"{pkg}: {cnt}")
        else:
            print("[INFO] Analyse terminée. Affichage des packages uniques (triés par nom croissant) :")
            # Trier par nom de package croissant
            for pkg in sorted(package_counter):
                print(pkg)
    else:
        print("[INFO] Aucun package trouvé.")
```

### Fonctionnement
- **Exécution du Script** :
  - `python script.py /chemin/vers/projet/java` : Analyse tous les fichiers `.java` dans le répertoire et utilise les noms de packages complets (`level = 0`).
  - `python script.py /chemin/vers/projet/java 2` : Tronque les noms de packages aux deux premières parties (par exemple, `com.google.common.eventbus` devient `com.google`).

- **Exemple de Sortie** :
  Supposons que vous avez un fichier Java avec :
  ```java
  import java.util.ArrayList;
  import com.google.common.eventbus.EventBus;
  ```
  - **Avec `level = 0` (ou aucun niveau fourni)** :
    ```
    [INFO] Début de l'analyse du répertoire : /chemin/vers/projet/java avec des noms de packages complets.
    [INFO] Entrée dans le répertoire : /chemin/vers/projet/java
    [INFO] Traitement du fichier : /chemin/vers/projet/java/MyFile.java
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
    [INFO] Début de l'analyse du répertoire : /chemin/vers/projet/java au niveau : 2
    [INFO] Entrée dans le répertoire : /chemin/vers/projet/java
    [INFO] Traitement du fichier : /chemin/vers/projet/java/MyFile.java
    [INFO] Total des fichiers Java tentés : 1
    [INFO] Traités avec succès : 1
    [INFO] Fichiers avec erreurs : 0
    [INFO] Total des packages uniques au niveau 2 : 2
    [INFO] Analyse terminée. Affichage des packages uniques au niveau 2 :
    com.google
    java.util
    ```

- **Fonctionnalités Clés** :
  - **Noms de Packages Complets** : Lorsque `level = 0` ou non passé, il utilise le nom de package complet tel qu'extrait (par exemple, `java.util`, `com.google.common.eventbus`).
  - **Troncature** : Lorsque `level > 0`, il prend les premières `level` parties.
  - **Gestion des Erreurs** : Vérifie la validité du répertoire et du niveau non négatif.
  - **Uniqueness** : Stocke les packages dans un `set` pour éviter les doublons.

### Cas Limites Gérés
- **Niveau Manquant** : Par défaut, `level = 0`, utilisant les noms de packages complets.
- **Niveau Invalide** : Quitte avec une erreur si `level` est négatif ou non entier.
- **Packages Courts** : Si un package a moins de parties que `level` (par exemple, `java` avec `level = 2`), il utilise le package complet (`java`).
- **Imports Vides** : Ignore les lignes où aucun package n'est extrait.

Ce script répond pleinement à votre exigence : lorsque `level = 0` ou non fourni, il utilise toutes les parties du nom de package, le traitant ainsi comme "infini" en termes de parties utilisées.