---
audio: false
generated: true
lang: fr
layout: post
title: Analyser les POM Maven
translated: true
type: note
---

Pour répondre à votre question, je vais fournir une solution pour générer un graphe de dépendances au format DOT en trouvant récursivement tous les fichiers `pom.xml` dans un répertoire et en analysant leurs dépendances, sans supposer une structure de projet multi-module Maven fixe comme celle de l'exemple (`project/module1/pom.xml`, etc.). Le script se concentrera d'abord sur la collecte de tous les fichiers `pom.xml`, puis les analysera pour déterminer les dépendances entre modules et produire le graphe.

---

## Aperçu de la Solution

Voici ce que le script fera :
1. **Collecter Récursivement les Fichiers `pom.xml`** : Parcourir le répertoire racine spécifié pour trouver tous les fichiers `pom.xml`, indépendamment de leur emplacement ou structure.
2. **Analyser les Informations des Modules** : Extraire `groupId`, `artifactId` et les dépendances de chaque `pom.xml`.
3. **Gérer l'Héritage de `groupId`** : Si un `pom.xml` ne spécifie pas de `groupId`, l'hériter d'une déclaration `<parent>`, si présente.
4. **Identifier les Dépendances Intra-Projet** : Faire correspondre les dépendances aux modules du projet en fonction de `groupId` et `artifactId`.
5. **Générer la Sortie DOT** : Créer un graphe orienté des dépendances entre modules.

Cette approche ne repose pas sur une hiérarchie de répertoires prédéfinie ni ne suppose que les fichiers `pom.xml` parents se trouvent dans des répertoires parents.

---

## Script Python

Voici le script Python adapté à vos besoins :

```python
import os
import sys
import xml.etree.ElementTree as ET

# Définir l'espace de noms POM Maven
NS = "{http://maven.apache.org/POM/4.0.0}"

# Cache pour groupId afin d'éviter les analyses redondantes
group_id_cache = {}

def get_group_id(pom_path, pom_map):
    """
    Extraire le groupId d'un fichier pom.xml, en considérant l'héritage depuis un parent.

    Args:
        pom_path (str): Chemin vers le fichier pom.xml.
        pom_map (dict): Mapping des chemins de pom.xml vers leurs données analysées.

    Returns:
        str: Le groupId du module.
    """
    if pom_path in group_id_cache:
        return group_id_cache[pom_path]

    tree = ET.parse(pom_path)
    root = tree.getroot()
    group_id_elem = root.find(NS + 'groupId')

    if group_id_elem is not None:
        group_id = group_id_elem.text.strip()
    else:
        # Vérifier la déclaration parent
        parent = root.find(NS + 'parent')
        if parent is not None:
            parent_group_id = parent.find(NS + 'groupId').text.strip()
            parent_artifact_id = parent.find(NS + 'artifactId').text.strip()
            parent_relative_path = parent.find(NS + 'relativePath')
            if parent_relative_path is not None and parent_relative_path.text:
                parent_pom_path = os.path.normpath(
                    os.path.join(os.path.dirname(pom_path), parent_relative_path.text)
                )
            else:
                # Par défaut, répertoire parent si relativePath est omis
                parent_pom_path = os.path.join(os.path.dirname(pom_path), '..', 'pom.xml')
                parent_pom_path = os.path.normpath(parent_pom_path)

            if parent_pom_path in pom_map:
                group_id = get_group_id(parent_pom_path, pom_map)
            else:
                raise ValueError(f"POM parent non trouvé pour {pom_path}: {parent_pom_path}")
        else:
            raise ValueError(f"Aucun groupId ou parent spécifié dans {pom_path}")

    group_id_cache[pom_path] = group_id
    return group_id

def get_artifact_id(pom_path):
    """
    Extraire l'artifactId d'un fichier pom.xml.

    Args:
        pom_path (str): Chemin vers le fichier pom.xml.

    Returns:
        str: L'artifactId du module.
    """
    tree = ET.parse(pom_path)
    root = tree.getroot()
    artifact_id_elem = root.find(NS + 'artifactId')

    if artifact_id_elem is None:
        raise ValueError(f"pom.xml doit spécifier un artifactId: {pom_path}")

    return artifact_id_elem.text.strip()

def get_dependencies(pom_path):
    """
    Extraire la liste des dépendances d'un fichier pom.xml.

    Args:
        pom_path (str): Chemin vers le fichier pom.xml.

    Returns:
        list: Liste de tuples (groupId, artifactId) pour chaque dépendance.
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

if __name__ == '__main__':
    # Vérifier les arguments de ligne de commande
    if len(sys.argv) != 2:
        print("Usage: python script.py <root_directory>")
        sys.exit(1)

    root_dir = sys.argv[1]
    if not os.path.isdir(root_dir):
        print(f"Erreur: {root_dir} n'est pas un répertoire")
        sys.exit(1)

    # Étape 1 : Trouver récursivement tous les fichiers pom.xml
    pom_files = [
        os.path.join(root, file)
        for root, _, files in os.walk(root_dir)
        for file in files if file == 'pom.xml'
    ]

    if not pom_files:
        print(f"Aucun fichier pom.xml trouvé dans {root_dir}")
        sys.exit(1)

    # Étape 2 : Construire un dictionnaire de tous les POMs pour les recherches de parent
    pom_map = {pom_file: None for pom_file in pom_files}

    # Étape 3 : Extraire les informations des modules
    modules = {}  # (groupId, artifactId) -> pom_path
    for pom_file in pom_files:
        try:
            group_id = get_group_id(pom_file, pom_map)
            artifact_id = get_artifact_id(pom_file)
            modules[(group_id, artifact_id)] = pom_file
        except ValueError as e:
            print(f"Avertissement: Ignorer {pom_file} en raison de l'erreur: {e}")
            continue

    # Étape 4 : Analyser les dépendances
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
                    # Ajouter la dépendance comme un tuple (importateur, importé) en utilisant artifactId pour la simplicité
                    dependencies.add((importer_artifact_id, dep_artifact_id))
        except ValueError as e:
            print(f"Avertissement: Erreur lors du traitement des dépendances dans {pom_file}: {e}")
            continue

    # Étape 5 : Sortie au format DOT
    print('digraph G {')
    for from_module, to_module in sorted(dependencies):
        print(f'  "{from_module}" -> "{to_module}";')
    print('}')
```

---

## Fonctionnement

### 1. **Entrée en Ligne de Commande**
- Prend un seul argument : `<root_directory>`, le point de départ de la recherche récursive.
- Vérifie qu'il s'agit bien d'un répertoire.

### 2. **Recherche des Fichiers `pom.xml`**
- Utilise `os.walk` pour parcourir récursivement l'arborescence des répertoires et collecter tous les fichiers `pom.xml` dans une liste.

### 3. **Analyse des Informations des Modules**
- **Group ID (`groupId`)** :
  - Extrait de chaque `pom.xml`.
  - S'il n'est pas présent, cherche une section `<parent>` et résout le `groupId` depuis le POM parent référencé en utilisant le `relativePath` (ou par défaut le répertoire parent si omis).
  - Met en cache les résultats pour éviter de ré-analyser.
- **Artifact ID (`artifactId`)** : Doit être présent dans chaque `pom.xml`.
- **Dépendances** : Extrait les paires `(groupId, artifactId)` de la section `<dependencies>`.

### 4. **Analyse des Dépendances**
- Construit une map de `(groupId, artifactId)` vers `pom_path` pour tous les modules.
- Pour chaque `pom.xml`, vérifie ses dépendances par rapport à la map des modules pour trouver les dépendances intra-projet.
- Exclut les auto-dépendances (où un module dépend de lui-même).
- Enregistre les dépendances comme des paires `(importer_artifactId, imported_artifactId)`.

### 5. **Sortie DOT**
- Produit un graphe orienté au format DOT, en utilisant `artifactId` comme étiquettes de nœuds pour plus de simplicité.

---

## Exemple d'Utilisation

Supposons que votre structure de répertoires soit irrégulière :

```
myproject/
├── app/pom.xml (groupId="com.myapp", artifactId="app", dépend de "core")
├── libs/core/pom.xml (groupId="com.myapp", artifactId="core")
├── tools/util/pom.xml (groupId="com.myapp", artifactId="util", dépend de "core")
```

Exécutez le script :

```bash
python script.py myproject
```

**Sortie :**

```
digraph G {
  "app" -> "core";
  "util" -> "core";
}
```

Cela montre que `app` et `util` dépendent tous deux de `core`.

---

## Notes et Limitations

- **Aucun Regroupement par Répertoire** : Contrairement au script original dans la trace de réflexion, cette version ne regroupe pas les modules par structure de répertoire puisque vous ne l'avez pas demandé. Elle utilise `artifactId` directement dans le graphe.
- **Résolution du Parent** : S'appuie sur `relativePath` dans la section `<parent>` ou suppose que le POM parent est dans le répertoire parent s'il est omis. Si le POM parent n'est pas dans l'ensemble collecté, une erreur est levée.
- **Correspondance Simple** : Fait correspondre les dépendances uniquement par `groupId` et `artifactId`, en ignorant les versions.
- **Aucune Substitution de Propriété** : Ne gère pas les propriétés Maven comme `${project.groupId}`.
- **Gestion des Erreurs** : Ignore les fichiers `pom.xml` problématiques avec un avertissement au lieu d'échouer complètement.

Ce script répond à votre exigence de "parcourir récursivement, obtenir tous les POMs d'abord, puis analyser" sans supposer une structure de fichier fixe. Faites-moi savoir si vous avez besoin d'ajustements !