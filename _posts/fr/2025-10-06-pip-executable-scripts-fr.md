---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Ajout de scripts exécutables aux paquets Pip
translated: true
type: note
---

### Création de scripts exécutables dans un package Python Pip

Pour inclure des scripts exécutables (c'est-à-dire des outils en ligne de commande) dans un package Python qui peut être installé via `pip`, vous définissez des **points d'entrée** dans le fichier de configuration de votre package. Cela permet aux utilisateurs d'exécuter vos scripts directement après l'installation (par exemple, `my-script` depuis le terminal).

Nous utiliserons un exemple simple : un package appelé `mytools` avec un script `greet` qui affiche une salutation.

#### Étape 1 : Configurer la structure de votre package
Créez une structure de répertoire comme ceci :

```
mytools/
├── pyproject.toml          # Fichier de configuration moderne (recommandé à la place de setup.py)
├── README.md
└── src/
    └── mytools/
        ├── __init__.py     # Le transforme en package
        └── greet.py        # La logique de votre script
```

Dans `src/mytools/__init__.py` (peut être vide ou contenir des informations de version) :
```python
__version__ = "0.1.0"
```

Dans `src/mytools/greet.py` (la fonction que votre script appellera) :
```python
import sys

def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "World"
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()
```

#### Étape 2 : Configurer les points d'entrée dans `pyproject.toml`
Utilisez la section `[project.scripts]` pour définir les scripts console. Cela indique à pip de créer des enveloppes exécutables.

```toml
[build-system]
requires = ["hatchling"]  # Ou "setuptools", "flit", etc.
build-backend = "hatchling.build"

[project]
name = "mytools"
version = "0.1.0"
description = "Un package d'outils simple"
readme = "README.md"
requires-python = ">=3.8"
dependencies = []  # Ajoutez vos dépendances ici, par ex. "requests"

[project.scripts]
greet = "mytools.greet:main"  # Format : nom_du_script = package.module:fonction
```

- `greet` est la commande que les utilisateurs exécuteront (par exemple, `greet Alice`).
- `mytools.greet:main` pointe vers la fonction `main()` dans `greet.py`.

Si vous préférez l'ancien `setup.py` (fonctionne toujours mais moins recommandé) :
```python
from setuptools import setup, find_packages

setup(
    name="mytools",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "greet = mytools.greet:main"
        ]
    },
    # ... autres champs comme description, install_requires
)
```

#### Étape 3 : Construire et installer le package
1. Installez les outils de construction : `pip install build twine` (ou `hatchling` si vous utilisez ce backend).

2. Construisez le package :
   ```
   python -m build
   ```
   Cela crée un dossier `dist/` avec les fichiers `.tar.gz` et `.whl`.

3. Installez localement pour tester :
   ```
   pip install -e .  # Mode éditable (les changements se reflètent immédiatement)
   ```
   Ou pour une installation propre : `pip install dist/mytools-0.1.0-py3-none-any.whl`.

4. Testez : Exécutez `greet Alice` dans votre terminal. Cela devrait afficher "Hello, Alice!".

#### Étape 4 : Distribuer (Optionnel)
- Téléversez sur PyPI : `twine upload dist/*` (nécessite un compte PyPI).
- Les utilisateurs peuvent alors exécuter `pip install mytools` et lancer `greet`.

#### Conseils
- **Scripts multiples** : Ajoutez plus de lignes dans `[project.scripts]`, par exemple, `another-script = mytools.other:main`.
- **Arguments** : Utilisez `argparse` dans votre fonction `main()` pour une meilleure gestion de la ligne de commande.
- **Dépendances** : Listez-les dans `[project.dependencies]` (par exemple, `click` pour les frameworks CLI).
- **Environnement virtuel** : Utilisez-en toujours un (`python -m venv env; source env/bin/activate`) pour éviter les conflits.
- **Des erreurs ?** Vérifiez `pip install --verbose` pour les détails. Assurez-vous que votre fonction ne prend aucun argument (ou qu'elle gère `sys.argv`).

Pour des configurations plus avancées (par exemple, avec Poetry ou Flit), consultez la documentation officielle.

#### Références
- [Python Packaging User Guide: Entry Points](https://packaging.python.org/en/latest/guides/writing-entry-points/)
- [PyPI: Building and Publishing](https://packaging.python.org/en/latest/tutorials/packaging-projects/)