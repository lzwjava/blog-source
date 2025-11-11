---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Lecture et Écriture de Fichiers CSV
translated: true
type: note
---

### Introduction au module `csv` de Python

Le module `csv` fait partie de la bibliothèque standard de Python et est utilisé pour lire et écrire des fichiers CSV (Comma-Separated Values). Il gère efficacement l'analyse des lignes et des colonnes. Pour l'utiliser, importez d'abord le module : `import csv`. Vous travaillerez avec des objets fichier, généralement ouverts en mode lecture (`'r'`) ou écriture (`'w'`).

Composants clés :
- **Reader** : Analyse les données CSV d'un fichier (par exemple, `csv.reader()` pour un accès par ligne).
- **Writer** : Écrit des données dans un fichier CSV (par exemple, `csv.writer()`).
- Les fichiers CSV sont traités comme des séquences de lignes, où chaque ligne est une liste de chaînes de caractères (colonnes).

Pour des raisons de sécurité et de simplicité, manipulez toujours les fichiers avec des instructions `with` pour garantir une fermeture correcte.

### Lecture basique d'un fichier CSV

Pour lire un CSV :
```python
import csv

with open('file.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Chaque 'row' est une liste de colonnes
```
- Ceci lit le fichier ligne par ligne. Vous pouvez accéder à des colonnes spécifiques par index (par exemple, `row[0]` pour la première colonne).
- Pour les en-têtes, lisez la première ligne séparément : `headers = next(reader)`.

### Comparaison de deux fichiers CSV : Lignes et colonnes

Pour comparer deux CSV (par exemple, `file1.csv` et `file2.csv`), chargez-les dans des structures comme des listes de listes (lignes), puis comparez. Hypothèses : les deux CSV ont la même structure (même nombre de colonnes/lignes). Les comparaisons peuvent vérifier des correspondances exactes, des différences ou une logique spécifique (par exemple, la correspondance sur une colonne clé).

#### Exemple 1 : Comparaison de lignes (Lignes entières)
Utilisez des dictionnaires pour stocker les lignes (si elles ont une colonne ID unique) ou des listes pour une comparaison directe.

```python
import csv

def compare_rows(file1, file2, key_column=0):
    # Lire file1 dans un dict (en utilisant key_column comme clé, la ligne entière comme valeur)
    data1 = {}
    with open(file1, 'r') as f1:
        reader1 = csv.reader(f1)
        headers1 = next(reader1, None)  # Ignorer l'en-tête si présent
        for row in reader1:
            data1[row[key_column]] = row  # par exemple, clé sur la première colonne

    # Lire file2 de manière similaire
    data2 = {}
    with open(file2, 'r') as f2:
        reader2 = csv.reader(f2)
        headers2 = next(reader2, None)
        for row in reader2:
            data2[row[key_column]] = row

    # Comparer
    common_keys = set(data1.keys()) & set(data2.keys())
    differing_rows = []
    for key in common_keys:
        if data1[key] != data2[key]:
            differing_rows.append((key, data1[key], data2[key]))
    
    return differing_rows  # Liste de (clé, row_de_file1, row_de_file2)

# Utilisation
differences = compare_rows('file1.csv', 'file2.csv', key_column=0)  # Clé sur la colonne 0
print("Lignes différentes :", differences)
```

- **Fonctionnement** : Convertit les CSV en dictionnaires indexés par une colonne (par exemple, ID). Compare les lignes correspondantes directement. Ajustez `key_column` pour spécifier la colonne à utiliser comme clé.
- **Variations** : Pour une comparaison ligne par ligne sans clés, itérez les deux lecteurs simultanément (si même ordre/longueur).

#### Exemple 2 : Comparaison de colonnes
Comparez des colonnes spécifiques sur l'ensemble du fichier (par exemple, vérifiez si les valeurs de la colonne 1 sont identiques dans les deux fichiers).

```python
import csv

def compare_columns(file1, file2, col_index=0):
    # Extraire les données de la colonne sous forme de listes
    col1 = []
    with open(file1, 'r') as f1:
        reader1 = csv.reader(f1)
        next(reader1, None)  # Ignorer l'en-tête si nécessaire
        for row in reader1:
            if len(row) > col_index:
                col1.append(row[col_index])

    col2 = []
    with open(file2, 'r') as f2:
        reader2 = csv.reader(f2)
        next(reader2, None)
        for row in reader2:
            if len(row) > col_index:
                col2.append(row[col_index])

    # Comparer les colonnes
    are_equal = col1 == col2
    differences = []
    for i, (val1, val2) in enumerate(zip(col1, col2)):
        if val1 != val2:
            differences.append((i, val1, val2))
    
    return are_equal, differences  # Booléen pour la correspondance, liste de (row_index, val1, val2)

# Utilisation
equal, diffs = compare_columns('file1.csv', 'file2.csv', col_index=1)  # Comparer la colonne 1
print("Les colonnes sont-elles égales ?", equal)
print("Différences (ligne, val1, val2) :", diffs)
```

- **Fonctionnement** : Extrait la colonne spécifiée dans des listes, puis compare élément par élément. Suppose que les CSV ont le même nombre de lignes ; gérez les incohérences si nécessaire.
- **Variations** : Utilisez `pandas` pour des opérations sur les colonnes plus avancées (par exemple, `df1['column'] == df2['column']`), mais restez sur `csv` pour une solution utilisant uniquement la bibliothèque standard.

#### Conseils et cas particuliers
- **En-têtes** : Si les CSV ont des en-têtes, ignorez-les avec `next(reader)`.
- **Types de données** : CSV lit les données sous forme de chaînes de caractères ; convertissez en int/float si nécessaire (par exemple, `int(row[0])`).
- **Fichiers volumineux** : Pour les gros CSV, utilisez DictReader pour un accès par clé : `csv.DictReader(file)` renvoie les lignes sous forme de OrderedDicts.
- **Délimiteur** : Utilisez `delimiter=';'` dans reader/writer si le séparateur n'est pas une virgule.
- **Erreurs** : Encapsulez dans un try-except pour les problèmes de fichier ; validez les longueurs des colonnes pour éviter les erreurs d'index.
- **Alternatives** : Pour des comparaisons complexes, envisagez des bibliothèques comme `pandas` (`df1.equals(df2)` pour les dataframes).

Pour la documentation complète, consultez le [guide officiel du module csv de Python](https://docs.python.org/3/library/csv.html). Si vous avez des fichiers CSV spécifiques ou une logique de comparaison particulière, fournissez plus de détails pour un code adapté !