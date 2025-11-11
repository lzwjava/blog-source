---
audio: false
generated: true
lang: fr
layout: post
title: Fonctionnement des modules en Python
translated: true
type: note
---

En Python, un **module** est un fichier contenant du code Python — comme des fonctions, des classes et des variables — que vous pouvez importer et utiliser dans d'autres scripts Python. Les modules sont une fonctionnalité fondamentale de Python qui vous aide à organiser votre code, à favoriser la réutilisation et à éviter la répétition. Explorons leur fonctionnement et comment utiliser d'autres fichiers ou modules Python dans vos projets.

---

#### Qu'est-ce qu'un module ?
Un module est simplement un fichier `.py` contenant du code Python. Lorsque vous importez un module dans un autre script, Python exécute le code de ce fichier et rend son contenu (fonctions, classes, variables, etc.) disponible pour votre utilisation. Python est livré avec une riche bibliothèque standard de modules intégrés (par exemple, `math`, `os`, `sys`), et vous pouvez également créer vos propres modules personnalisés.

Par exemple, si vous avez un fichier nommé `greetings.py` avec le code suivant :
```python
def say_hello(name):
    print(f"Hello, {name}!")
```
Ce fichier est un module nommé `greetings`. Vous pouvez l'importer dans un autre script pour utiliser la fonction `say_hello`.

---

#### Comment utiliser d'autres fichiers ou modules Python
Pour utiliser le code d'un autre fichier Python (module), vous utilisez l'instruction `import`. Voici comment cela fonctionne étape par étape :

1. **Import de base**
   - Si le module se trouve dans le même répertoire que votre script, vous pouvez l'importer par son nom (sans l'extension `.py`).
   - Exemple : Dans un fichier nommé `main.py`, vous pouvez écrire :
     ```python
     import greetings
     greetings.say_hello("Alice")
     ```
   - L'exécution de `main.py` affichera : `Hello, Alice!`
   - Utilisez la notation pointée (`nom_du_module.nom_de_l_element`) pour accéder au contenu du module.

2. **Import d'éléments spécifiques**
   - Si vous n'avez besoin que de fonctions ou de variables spécifiques d'un module, utilisez la syntaxe `from ... import ...`.
   - Exemple :
     ```python
     from greetings import say_hello
     say_hello("Bob")
     ```
   - Cela affiche : `Hello, Bob!`
   - Vous pouvez maintenant utiliser `say_hello` directement sans le préfixer par le nom du module.

3. **Import avec alias**
   - Vous pouvez donner à un module un nom plus court (alias) en utilisant `as` pour plus de commodité.
   - Exemple :
     ```python
     import greetings as g
     g.say_hello("Charlie")
     ```
   - Sortie : `Hello, Charlie!`

4. **Tout importer**
   - Vous pouvez importer tout le contenu d'un module en utilisant `from nom_du_module import *`, mais cette pratique est généralement déconseillée car elle peut encombrer votre espace de noms et provoquer des conflits de noms.
   - Exemple :
     ```python
     from greetings import *
     say_hello("Dana")
     ```
   - Sortie : `Hello, Dana!`

---

#### Où Python cherche-t-il les modules ?
Python recherche les modules dans une liste de répertoires définie dans `sys.path`. Cela inclut :
- Le répertoire du script que vous exécutez (répertoire courant).
- Les répertoires listés dans la variable d'environnement `PYTHONPATH` (si elle est définie).
- Les emplacements par défaut où la bibliothèque standard de Python est installée.

Si votre module se trouve dans un répertoire différent, vous pouvez :
- Le déplacer dans le même répertoire que votre script.
- Ajouter son répertoire à `sys.path` programmatiquement :
  ```python
  import sys
  sys.path.append('/chemin/vers/repertoire')
  import mon_module
  ```

---

#### Modules intégrés
La bibliothèque standard de Python fournit de nombreux modules utiles que vous pouvez importer sans avoir à les créer vous-même. Par exemple :
- `import math` vous permet d'utiliser `math.sqrt(16)` (renvoie `4.0`) ou `math.pi` (renvoie `3.14159...`).
- `import os` fournit des fonctions pour interagir avec le système d'exploitation.

---

#### Packages
Un **package** est un répertoire contenant plusieurs modules et un fichier spécial `__init__.py` (qui peut être vide). Par exemple, si vous avez :
```
monpackage/
    __init__.py
    greetings.py
```
Vous pouvez importer le module `greetings` comme ceci :
```python
import monpackage.greetings
monpackage.greetings.say_hello("Eve")
```
Ou :
```python
from monpackage.greetings import say_hello
say_hello("Eve")
```

---

#### Comment les modules sont-ils exécutés ?
Lorsque vous importez un module, Python exécute une fois tout le code de ce module et le met en cache. Les imports suivants réutilisent la version mise en cache. Si un module contient du code de haut niveau (par exemple, une instruction `print`), celui-ci s'exécutera lors de l'import. Par exemple :
```python
# monmodule.py
print("Le module est en cours d'importation !")
def ma_fonction():
    print("Fonction appelée !")
```
```python
# main.py
import monmodule
```
L'exécution de `main.py` affiche : `Le module est en cours d'importation !`

Pour inclure du code qui ne s'exécute que lorsque le module est exécuté directement (et non importé), utilisez :
```python
if __name__ == "__main__":
    print("Ceci ne s'exécute que si le module est exécuté directement !")
```
Ceci est utile pour les tests ou pour définir un point d'entrée principal pour le module.

---

#### Exemple
Voici un exemple complet :
1. Créez `math_utils.py` :
   ```python
   def add(a, b):
       return a + b
   ```
2. Créez `main.py` dans le même répertoire :
   ```python
   import math_utils
   result = math_utils.add(3, 4)
   print(result)  # Affiche : 7
   ```
3. Alternative :
   ```python
   from math_utils import add
   print(add(3, 4))  # Affiche : 7
   ```

---

#### Points clés à retenir
- Les modules sont des fichiers Python que vous pouvez importer pour réutiliser du code.
- Utilisez `import nom_du_module` pour accéder au contenu avec la notation pointée, ou `from nom_du_module import element` pour un accès direct.
- Les modules peuvent être des fichiers personnalisés, des modules de la bibliothèque intégrée ou faire partie de packages.
- Python trouve les modules en utilisant `sys.path`, et vous pouvez organiser des projets plus importants avec des packages.

Ceci couvre les bases du fonctionnement des modules en Python et de l'utilisation d'autres fichiers ou modules Python dans vos scripts !