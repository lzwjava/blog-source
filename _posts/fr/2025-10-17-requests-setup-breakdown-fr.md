---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Décomposition du Fichier Setup.py
translated: true
type: note
---

### Aperçu
Il s'agit d'un fichier `setup.py`, un script Python standard utilisé avec `setuptools` pour définir et construire un package Python. Plus précisément, celui-ci est pour la bibliothèque **Requests** — un client HTTP populaire pour Python. Il gère les métadonnées telles que le nom du package, la version, les dépendances et les classificateurs (pour la distribution sur PyPI). Lorsque vous exécutez `pip install requests`, ce script (ou ses artefacts construits) est ce qui est exécuté en arrière-plan pour installer le package.

Le script est structuré comme un seul appel de fonction `setup()`, mais il inclut quelques gardes-fous, aides et lectures dynamiques d'autres fichiers. Je vais le décomposer section par section.

### 1. Importations et Vérification de la Version de Python
```python
#!/usr/bin/env python
import os
import sys
from codecs import open

from setuptools import setup

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 9)

if CURRENT_PYTHON < REQUIRED_PYTHON:
    # Message d'erreur et sortie
    sys.exit(1)
```
- **Shebang (`#!/usr/bin/env python`)** : Rend le fichier exécutable sur les systèmes de type Unix, en l'exécutant avec l'interpréteur Python du système.
- **Importations** : Importe `os` et `sys` pour les interactions système, `codecs.open` pour la lecture de fichiers UTF-8 (pour gérer les non-ASCII en toute sécurité), et `setup` de `setuptools` pour construire le package.
- **Vérification de Version** : S'assure que l'utilisateur exécute Python 3.9 ou supérieur. Sinon, il affiche un message d'erreur utile suggérant une mise à niveau ou un épinglage à une ancienne version de Requests (<2.32.0), puis quitte avec le code 1 (échec). Cela impose la compatibilité, car Requests a abandonné la prise en charge des anciennes versions de Python.

### 2. Raccourci de Publication
```python
if sys.argv[-1] == "publish":
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    sys.exit()
```
- Une commodité pour les mainteneurs : Si vous exécutez `python setup.py publish`, cela :
  - Construit les archives de distribution source (`sdist`) et de roue (`bdist_wheel`) dans le dossier `dist/`.
  - Les télécharge sur PyPI en utilisant `twine` (un outil de téléchargement sécurisé).
- C'est un moyen rapide de publier une nouvelle version sans commandes manuelles. Il se termine après l'exécution.

### 3. Dépendances
```python
requires = [
    "charset_normalizer>=2,<4",
    "idna>=2.5,<4",
    "urllib3>=1.21.1,<3",
    "certifi>=2017.4.17",
]
test_requirements = [
    "pytest-httpbin==2.1.0",
    "pytest-cov",
    "pytest-mock",
    "pytest-xdist",
    "PySocks>=1.5.6, !=1.5.7",
    "pytest>=3",
]
```
- **`requires`** : Dépendances principales installées lorsque vous exécutez `pip install requests`. Celles-ci gèrent l'encodage (`charset_normalizer`), les noms de domaines internationalisés (`idna`), le transport HTTP (`urllib3`) et les certificats SSL (`certifi`).
- **`test_requirements`** : Installées uniquement si vous exécutez les tests (par exemple, via `pip install -e '.[tests]'`). Inclut des outils de test comme des variantes de `pytest` pour la simulation HTTP, la couverture et les tests parallèles. `PySocks` est pour la prise en charge des proxy SOCKS dans les tests.

### 4. Chargement Dynamique des Métadonnées
```python
about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "src", "requests", "__version__.py"), "r", "utf-8") as f:
    exec(f.read(), about)

with open("README.md", "r", "utf-8") as f:
    readme = f.read()
```
- **Dictionnaire `about`** : Lit les métadonnées depuis `src/requests/__version__.py` (par exemple, `__title__`, `__version__`, `__description__`, etc.) en utilisant `exec()`. Cela permet de centraliser les informations de version — mettez-les à jour une fois, et `setup.py` les récupère.
- **`readme`** : Charge l'intégralité du fichier `README.md` sous forme de chaîne pour la description longue du package sur PyPI.

### 5. L'Appel Principal `setup()`
C'est le cœur du fichier. Il configure le package pour la construction/l'installation :
```python
setup(
    name=about["__title__"],  # par ex., "requests"
    version=about["__version__"],  # par ex., "2.32.3"
    description=about["__description__"],  # Résumé court
    long_description=readme,  # README complet
    long_description_content_type="text/markdown",  # S'affiche en Markdown sur PyPI
    author=about["__author__"],  # par ex., "Kenneth Reitz"
    author_email=about["__author_email__"],
    url=about["__url__"],  # par ex., le dépôt GitHub
    packages=["requests"],  # Installe le package 'requests'
    package_data={"": ["LICENSE", "NOTICE"]},  # Inclut les fichiers non-Python
    package_dir={"": "src"},  # Le code source est dans 'src/'
    include_package_data=True,  # Récupère tous les fichiers de données
    python_requires=">=3.9",  # Reflète la vérification de version
    install_requires=requires,  # Défini plus tôt
    license=about["__license__"],  # par ex., "Apache 2.0"
    zip_safe=False,  # Permet la modification des fichiers installés (commun pour les bibliothèques)
    classifiers=[  # Catégories PyPI pour la découvrabilité
        "Development Status :: 5 - Production/Stable",
        # ... (liste complète inclut les versions Python, OS, sujets)
    ],
    tests_require=test_requirements,  # Pour `pip install -e '.[tests]'`
    extras_require={  # Dépendances optionnelles
        "security": [],  # Vide — peut-être pour un usage futur
        "socks": ["PySocks>=1.5.6, !=1.5.7"],  # Prise en charge des proxy SOCKS
        "use_chardet_on_py3": ["chardet>=3.0.2,<6"],  # Fallback d'encodage hérité
    },
    project_urls={  # Liens sur la page PyPI
        "Documentation": "https://requests.readthedocs.io",
        "Source": "https://github.com/psf/requests",
    },
)
```
- **Arguments Clés** :
  - **Nom/Version/Description** : Tirés de `__version__.py` pour une maintenance facile.
  - **Packages/Package Dir** : Indique à setuptools que le package se trouve sous `src/requests/` et de l'installer comme `import requests`.
  - **Classificateurs** : Une liste de chaînes qui catégorisent le package (par ex., stable, Python 3.9+, licence Apache, sujet web/HTTP). Cela aide les utilisateurs à le trouver sur PyPI.
  - **Extras Require** : Permet aux utilisateurs d'installer des fonctionnalités optionnelles, comme `pip install requests[socks]` pour la prise en charge des proxy.
  - **URLs du Projet** : Ajoute des liens cliquables vers la documentation et la source sur la page PyPI.

### Comment Cela Fonctionne en Pratique
- **Installation** : `pip install .` (depuis le dépôt) ou `pip install requests` (depuis PyPI) exécute ceci pour copier les fichiers, installer les dépendances et configurer le package.
- **Construction** : `python setup.py sdist` crée les archives distribuables.
- **Pourquoi Cette Structure ?** C'est une "disposition src" (code dans `src/`), qui est une pratique moderne recommandée pour éviter les importations accidentelles pendant le développement. Le fichier est autonome mais délègue les détails à d'autres fichiers comme `__version__.py`.

Ce setup.py provient du dépôt officiel de Requests et n'a pas beaucoup changé au fil des versions — il est éprouvé pour sa fiabilité.

### Références
- [Documentation de Requests](https://requests.readthedocs.io/en/latest/)
- [Dépôt GitHub de Requests](https://github.com/psf/requests)
- [Guide de l'utilisateur pour l'empaquetage Python](https://packaging.python.org/en/latest/tutorials/packaging-projects/)