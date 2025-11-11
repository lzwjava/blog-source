---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Lire des fichiers Excel avec Pandas
translated: true
type: note
---

### Prérequis
Pour lire des fichiers Excel en Python, vous avez besoin de la bibliothèque `pandas` et d'un moteur Excel. Installez pandas s'il n'est pas déjà installé :
```
pip install pandas
```
Pour les formats Excel modernes (.xlsx), installez `openpyxl` :
```
pip install openpyxl
```
Pour les fichiers .xls, utilisez `xlrd` :
```
pip install xlrd
```

### Utilisation de base
Pandas fournit la fonction `pd.read_excel()` pour charger les données Excel dans un DataFrame.

1. Importez pandas :
   ```python
   import pandas as pd
   ```

2. Lisez le fichier Excel (spécifiez le chemin du fichier) :
   ```python
   df = pd.read_excel('chemin/vers/votre/fichier.xlsx')
   ```
   - Cela charge la première feuille par défaut.
   - Le résultat est un DataFrame contenant les données Excel.

3. Inspectez les données :
   ```python
   print(df.head())  # Affiche les 5 premières lignes
   print(df.info())  # Résumé des colonnes et des types de données
   ```

### Options avancées
- **Spécifier une feuille** : Utilisez le paramètre `sheet_name` (la valeur par défaut est 0 pour la première feuille) :
  ```python
  df = pd.read_excel('fichier.xlsx', sheet_name='Feuille2')  # Par nom
  df = pd.read_excel('fichier.xlsx', sheet_name=1)           # Par index (base 0)
  ```
- **Lire plusieurs feuilles** : Passez une liste ou `None` pour charger toutes les feuilles dans un dictionnaire :
  ```python
  toutes_les_feuilles = pd.read_excel('fichier.xlsx', sheet_name=None)  # Dict de DataFrames clé par nom de feuille
  ```
- **Spécifier une plage de données** : Utilisez `usecols` pour les colonnes (ex: `'A:C'` pour les colonnes A à C) et `skiprows` pour ignorer les lignes initiales :
  ```python
  df = pd.read_excel('fichier.xlsx', usecols='A,C,E', skiprows=2)
  ```
- **Gérer les en-têtes** : Si l'en-tête n'est pas à la ligne 0, spécifiez-la avec `header` :
  ```python
  df = pd.read_excel('fichier.xlsx', header=1)  # En-tête à la ligne 1 (index base 0)
  ```
- **Définir l'index** : Utilisez `index_col` pour définir une colonne comme index :
  ```python
  df = pd.read_excel('fichier.xlsx', index_col='Nom de la Colonne')
  ```

### Exemple
Supposons que vous ayez un fichier Excel `ventes.xlsx` avec une feuille nommée "Data" contenant des données de vente.

```python
import pandas as pd

# Lire la feuille spécifique
df = pd.read_excel('ventes.xlsx', sheet_name='Data')

# Afficher le DataFrame
print(df)

# Sauvegarder en CSV si nécessaire
df.to_csv('ventes.csv', index=False)
```

Pour plus de détails, consultez la [documentation pandas sur read_excel](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html). Si vous rencontrez des erreurs, vérifiez le format du fichier Excel et assurez-vous que les paquets requis sont installés.