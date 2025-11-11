---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Guide des expressions régulières en Python
translated: true
type: note
---

### Importation du module `re`
Le module `re` (abréviation de *regular expressions*) fait partie de la bibliothèque standard de Python. Ce n'est pas un package "regex" séparé mais un module intégré. Importez-le en haut de votre script :

```python
import re
```

### Concepts de base
Les expressions régulières (regex) sont des motifs utilisés pour faire correspondre, rechercher et manipuler des chaînes de caractères. Elles utilisent des caractères spéciaux comme :
- `.` (n'importe quel caractère)
- `*` (zéro ou plusieurs occurrences)
- `+` (une ou plusieurs occurrences)
- `[]` (classes de caractères, par exemple `[a-z]` pour les lettres minuscules)
- `^` (début de chaîne), `$` (fin de chaîne)

Les exemples sont basés sur la documentation de `re` de Python. Compilez toujours les motifs complexes pour plus d'efficacité avec `re.compile()`.

### Fonctions principales et utilisation

#### 1. **Faire correspondre un motif au début**
   - `re.match(pattern, string)` : Vérifie si le motif correspond au début de la chaîne.
   - Retourne un objet match ou `None`.

   Exemple :
   ```python
   import re
   result = re.match(r"Hello", "Hello world")
   print(result.group())  # Sortie : Hello
   ```

#### 2. **Rechercher n'importe où dans la chaîne**
   - `re.search(pattern, string)` : Trouve la première occurrence du motif n'importe où.
   - Retourne un objet match ou `None`.

   Exemple :
   ```python
   result = re.search(r"world", "Hello world")
   print(result.group())  # Sortie : world
   ```

#### 3. **Trouver toutes les correspondances**
   - `re.findall(pattern, string)` : Retourne une liste de toutes les correspondances non chevauchantes.

   Exemple :
   ```python
   matches = re.findall(r"\d+", "I have 3 cats and 42 dogs")
   print(matches)  # Sortie : ['3', '42']
   ```

#### 4. **Diviser les chaînes de caractères**
   - `re.split(pattern, string)` : Divise la chaîne à chaque occurrence du motif.

   Exemple :
   ```python
   parts = re.split(r"\s+", "Hello    world   example")
   print(parts)  # Sortie : ['Hello', 'world', 'example']
   ```

#### 5. **Remplacer les correspondances**
   - `re.sub(pattern, replacement, string)` : Remplace les correspondances par la chaîne de remplacement.

   Exemple :
   ```python
   new_string = re.sub(r"bad", "good", "This is bad")
   print(new_string)  # Sortie : This is good
   ```

#### 6. **Compiler les motifs pour une réutilisation**
   - Pour une utilisation répétée, compilez l'expression régulière en un objet pattern pour de meilleures performances.

   Exemple :
   ```python
   pattern = re.compile(r"\d+")
   matches = pattern.findall("Room 101 and 102")
   print(matches)  # Sortie : ['101', '102']
   ```

### Bonnes pratiques
- Utilisez des chaînes brutes (`r""`) pour les motifs regex afin d'éviter les problèmes d'échappement des barres obliques inverses.
- Manipulez les objets match : utilisez `.group()` pour obtenir la correspondance, `.span()` pour les indices.
- Pour les tâches complexes, testez les motifs avec des outils en ligne ou le shell interactif de Python.
- Référez-vous à la documentation officielle de Python : https://docs.python.org/3/library/re.html pour plus d'exemples et de drapeaux (par exemple, `re.IGNORECASE`).

Si vous avez un cas d'utilisation spécifique ou une erreur, fournissez plus de détails !