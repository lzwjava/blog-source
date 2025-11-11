---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Guide de Correspondance de Fichiers avec le Module Glob de Python
translated: true
type: note
---

### Importation de Glob
Pour utiliser glob en Python, importez le module de la bibliothèque standard :
```python
import glob
```

### Fonctionnalités de base
La fonction `glob.glob()` prend une chaîne de motif et renvoie une liste de chemins de fichiers ou de répertoires correspondants. Elle utilise des caractères génériques de style shell Unix :

- `*` : Correspond à n'importe quelle séquence de caractères (sauf les séparateurs de chemin).
- `?` : Correspond à n'importe quel caractère unique.
- `[seq]` : Correspond à n'importe quel caractère dans seq (par exemple, `[0-9]` pour les chiffres).
- `**` : Correspond récursivement aux répertoires (nécessite `recursive=True`).

Les motifs sont relatifs au répertoire courant, sauf si un chemin absolu est spécifié.

### Exemples d'utilisation

#### 1. Trouver tous les fichiers .txt dans le répertoire courant
```python
import glob

files = glob.glob("*.txt")
print(files)  # Sortie : ['file1.txt', 'file2.txt', ...]
```

#### 2. Trouver des fichiers avec des extensions spécifiques dans un sous-répertoire
```python
files = glob.glob("documents/*.pdf")
print(files)  # Sortie : ['documents/doc1.pdf', ...]
```

#### 3. Correspondre à des motifs spécifiques (par exemple, fichiers commençant par 'log' et se terminant par des chiffres)
```python
files = glob.glob("log[0-9].txt")
print(files)  # Sortie : ['log1.txt', 'log2.txt', ...] si de tels fichiers existent
```

#### 4. Recherche récursive dans les sous-répertoires
Utilisez `**` avec `recursive=True` pour rechercher dans les répertoires et sous-répertoires :
```python
files = glob.glob("**/*.py", recursive=True)
print(files)  # Sortie : ['script1.py', 'subdir/script2.py', ...]
```

### Notes importantes
- Les résultats ne sont pas triés par défaut ; utilisez `sorted()` si vous avez besoin d'un ordre : `sorted(glob.glob("*.txt"))`.
- Pour une correspondance insensible à la casse sur les systèmes de fichiers sensibles à la casse, envisagez de combiner avec `fnmatch` ou de gérer cela dans le code, car glob est sensible à la casse.
- Glob ne suit pas les liens symboliques sauf s'ils sont explicitement gérés ; utilisez `os.walk()` pour des parcours plus complexes.
- Pour une correspondance à la fois, utilisez `glob.iglob()` qui renvoie un itérateur pour économiser la mémoire sur les grands résultats : `for file in glob.iglob("*.txt"): print(file)`.

Ceci couvre l'essentiel ; reportez-vous à la [documentation Python](https://docs.python.org/3/library/glob.html) pour plus de détails.