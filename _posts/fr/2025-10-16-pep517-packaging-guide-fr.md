---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Guide d'Emballage Python PEP 517
translated: true
type: note
---

La PEP 517, acceptée en 2016, définit une interface standardisée pour construire des paquets Python qui découple le backend de construction (la logique pour créer des distributions) du frontend (des outils comme pip qui orchestrent le processus). Cela permet aux développeurs d'utiliser des outils de construction modernes sans être enfermés dans des systèmes hérités comme le `setup.py` de setuptools. Combinée avec la PEP 518 (qui spécifie les dépendances de construction), elle permet des builds fiables et isolés à partir d'arbres sources ou de distributions de sources (sdists). En 2025, la PEP 517 est le fondement de l'empaquetage Python moderne, supportée par pip (depuis la version 10 pour la PEP 518 et la 19 pour la PEP 517 complète) et des outils comme Poetry, Flit et PDM.

Ce guide couvre la motivation, les concepts clés, la spécification, les workflows, l'implémentation et les bonnes pratiques.

## Motivation et Contexte

L'empaquetage Python a évolué de `distutils` (introduit dans Python 1.6, 2000) vers `setuptools` (2004), qui a ajouté la gestion des dépendances mais a introduit des problèmes :
- **Impératif et Fragile** : Les builds reposaient sur l'exécution de `python setup.py`, un script arbitraire qui pouvait échouer à cause d'hypothèses sur l'environnement (par exemple, l'absence de Cython pour les extensions).
- **Aucune Dépendance de Build** : Les outils nécessaires à la construction (par exemple, les compilateurs, Cython) n'étaient pas déclarés, conduisant à des installations manuelles et des conflits de versions.
- **Couplage Fort** : Pip invoquait en dur `setup.py`, bloquant les systèmes de construction alternatifs comme Flit ou Bento.
- **Pollution de l'Environnement Hôte** : Les builds utilisaient l'environnement Python global de l'utilisateur, risquant des effets de bord.

Ces problèmes ont étouffé l'innovation et causé des erreurs lors des installations depuis les sources (par exemple, depuis Git). La PEP 517 résout cela en standardisant une interface minimale : les frontends appellent des hooks backend dans des environnements isolés. Les wheels (binaires pré-construits, introduits en 2014) simplifient la distribution—les backends doivent juste produire des wheels/sdists conformes. La PEP 518 complète en déclarant les exigences de build dans `pyproject.toml`, permettant l'isolation.

Le résultat : Un écosystème déclaratif et extensible où `setup.py` est optionnel, et où des outils comme pip peuvent construire n'importe quel projet conforme sans recours aux méthodes héritées.

## Concepts Clés

### Arbres Sources et Distributions
- **Arbre Source (Source Tree)** : Un répertoire (par exemple, un checkout VCS) contenant le code du paquet et `pyproject.toml`. Des outils comme `pip install .` construisent à partir de lui.
- **Distribution Source (Sdist)** : Une archive tarball compressée (`.tar.gz`) comme `package-1.0.tar.gz`, se décompressant en un répertoire `{nom}-{version}` avec `pyproject.toml` et des métadonnées (PKG-INFO). Utilisée pour les releases et l'empaquetage en aval (par exemple, Debian).
- **Wheel** : Une distribution binaire `.whl`—pré-construite, spécifique à une plateforme, et installable sans compilation. La PEP 517 impose les wheels pour la reproductibilité.

Les sdists hérités (pré-PEP 517) se décompressent en arbres exécutables mais doivent maintenant inclure `pyproject.toml` pour être conformes.

### pyproject.toml
Ce fichier TOML centralise la configuration. La section `[build-system]` (issue des PEP 518/517) spécifie :
- `requires` : Liste des dépendances PEP 508 pour la construction (par exemple, `["setuptools>=40.8.0", "wheel"]`).
- `build-backend` : Point d'entrée vers le backend (par exemple, `"setuptools.build_meta"` ou `"poetry.masonry.api"`).
- `backend-path` (optionnel) : Chemins in-tree ajoutés à `sys.path` pour les backends auto-hébergés (par exemple, `["src/backend"]`).

Exemple de configuration minimale :
```
[build-system]
requires = ["setuptools>=40.8.0", "wheel"]
build-backend = "setuptools.build_meta"
```

Les exigences forment un DAG (pas de cycles ; les frontends détectent et échouent). D'autres sections comme `[project]` (PEP 621) ou `[tool.poetry]` contiennent les métadonnées/dépendances.

### Backends et Frontends de Build
- **Backend** : Implémente la logique de construction via des hooks (fonctions appelables). S'exécute dans un sous-processus pour l'isolation.
- **Frontend** : Orchestre (par exemple, pip). Configure l'isolation, installe les exigences, appelle les hooks.
- **Découplage** : Les frontends invoquent des hooks standardisés, et non `setup.py`. Cela supporte des backends divers sans modifications de pip.

Les hooks utilisent `config_settings` (dict pour les flags, par exemple, `{"--debug": true}`) et peuvent écrire sur stdout/stderr (UTF-8).

## La Spécification

### Détails de [build-system]
- `requires` : Chaînes PEP 508 (par exemple, `">=1.0; sys_platform == 'win32'"`).
- `build-backend` : `module:objet` (par exemple, `flit_core.buildapi` importe `flit_core; backend = flit_core.buildapi`).
- Aucune pollution de sys.path—les backends importent via l'isolation.

### Hooks
Les backends exposent ceux-ci en tant qu'attributs :

**Obligatoires :**
- `build_wheel(wheel_directory, config_settings=None, metadata_directory=None) -> str` : Construit une wheel dans `wheel_directory`, retourne le nom de base (par exemple, `"myproj-1.0-py3-none-any.whl"`). Utilise les métadonnées précédentes si fournies. Gère les sources en lecture seule via des temporaires.
- `build_sdist(sdist_directory, config_settings=None) -> str` : Construit une sdist dans `sdist_directory` (format pax, UTF-8). Lève `UnsupportedOperation` si impossible (par exemple, pas de VCS).

**Optionnels (par défaut `[]` ou solutions de repli) :**
- `get_requires_for_build_wheel(config_settings=None) -> list[str]` : Dépendances wheel supplémentaires (par exemple, `["cython"]`).
- `prepare_metadata_for_build_wheel(metadata_directory, config_settings=None) -> str` : Écrit les métadonnées `{pkg}-{ver}.dist-info` (selon la spécification wheel, pas de RECORD). Retourne le nom de base ; les frontends extraient depuis la wheel si manquant.
- `get_requires_for_build_sdist(config_settings=None) -> list[str]` : Dépendances sdist supplémentaires.

Les hooks lèvent des exceptions pour les erreurs. Les frontends appellent dans des environnements isolés (par exemple, venv avec seulement stdlib + exigences).

### Environnement de Build
- Venv isolé : Bootstrap pour `get_requires_*`, complet pour les builds.
- Outils CLI (par exemple, `flit`) dans le PATH.
- Pas de stdin ; sous-processus par hook.

## Comment Fonctionne le Processus de Build

### Workflow Étape par Étape
Pour `pip install .` (arbre source) ou l'installation depuis une sdist :

1. **Découverte** : Le frontend lit `pyproject.toml`.
2. **Configuration de l'Isolation** : Crée un venv ; installe `requires`.
3. **Requête des Exigences** : Appelle `get_requires_for_build_wheel` (installe les extras).
4. **Préparation des Métadonnées** : Appelle `prepare_metadata_for_build_wheel` (ou construit une wheel et extrait).
5. **Construction de la Wheel** : Appelle `build_wheel` dans l'environnement isolé ; installe la wheel résultante.
6. **Solutions de Repli** : Si sdist non supportée, construit une wheel ; si pas de hooks, utilise `setup.py` hérité.

Pour les sdists : Décompresse, traite comme un arbre source. Workflow développeur (par exemple, `pip wheel .`) :
1. Environnement isolé.
2. Appelle les hooks backend pour wheel/sdist.

### Isolation du Build (PEP 518)
Crée un venv temporaire pour les builds, évitant la pollution de l'hôte. L'option `--no-build-isolation` de pip désactive (à utiliser avec prudence). Les outils comme tox utilisent l'isolation par défaut.

Ancien vs. Nouveau :
- **Ancien** : `python setup.py install` dans l'environnement hôte—risque de conflits.
- **Nouveau** : Hooks isolés—reproductible, sécurisé.

## Implémenter un Backend de Build

Pour en créer un :
1. Définir un module avec des hooks (par exemple, `mybackend.py`).
2. Pointer `build-backend` vers lui.

Exemple minimal (paquet Python pur) :
```python
# mybackend.py
from zipfile import ZipFile
import os
from pathlib import Path

def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    # Copie la source dans le répertoire wheel, zip en .whl
    dist = Path(wheel_directory) / "myproj-1.0-py3-none-any.whl"
    with ZipFile(dist, 'w') as z:
        for src in Path('.').rglob('*'):
            z.write(src, src.relative_to('.'))
    return str(dist.relative_to(wheel_directory))

# Hooks optionnels
def get_requires_for_build_wheel(config_settings=None):
    return []

def prepare_metadata_for_build_wheel(metadata_directory, config_settings=None):
    # Écrit METADATA, etc.
    return "myproj-1.0.dist-info"
```

Dans `pyproject.toml` :
```
[build-system]
requires = []
build-backend = "mybackend:build_wheel"  # Pointe en fait vers l'objet module
```

Utiliser des bibliothèques comme `pyproject-hooks` pour le code boilerplate. Pour les extensions, intégrer les compilateurs C via `config_settings`.

## Utiliser la PEP 517 avec les Outils

- **pip** : Détecte automatiquement `pyproject.toml` ; utiliser `--use-pep517` (défaut depuis 19.1). Pour l'installations éditables : `pip install -e .` appelle les hooks.
- **Poetry** : Outil déclaratif. Génère :
  ```
  [build-system]
  requires = ["poetry-core>=1.0.0"]
  build-backend = "poetry.core.masonry.api"
  ```
  Installe via `poetry build` ; compatible pip.
- **Flit** : Simple pour le Python pur. Utilise :
  ```
  [build-system]
  requires = ["flit_core >=3.2,<4"]
  build-backend = "flit_core.buildapi"
  ```
  `flit publish` construit et publie.
- **Setuptools** : Pont vers l'héritage :
  ```
  [build-system]
  requires = ["setuptools>=40.8.0", "wheel"]
  build-backend = "setuptools.build_meta"
  ```
  Supporte `setup.cfg` pour les métadonnées déclaratives.

Migrer l'héritage : Ajouter `[build-system]` ; supprimer les appels à `setup.py`.

## Gestion des Erreurs et Bonnes Pratiques

- **Erreurs** : Les hooks lèvent des exceptions (par exemple, `ValueError` pour une configuration invalide). Cycles : Le frontend échoue avec un message. Sdist non supportée : Repli sur la wheel.
- **Bonnes Pratiques** :
  - Préférer le déclaratif (`setup.cfg` ou `[project]`).
  - Déclarer des dépendances de build exactes (par exemple, `cython==0.29`).
  - Tester l'isolation : `pip wheel . --no-build-isolation` pour le débogage.
  - Pour les backends in-tree : Utiliser `backend-path` ; éviter les cycles.
  - Sécurité : Hooks dans des sous-processus ; pas de code arbitraire.
  - Compatibilité : Inclure `setup.py` pour les anciens outils.

En 2025, setuptools domine (selon les enquêtes), mais l'adoption de Poetry/Flit croît pour leur simplicité.

## Références
- [PEP 517 – A build-system independent format for source trees](https://peps.python.org/pep-0517/)
- [PEP 517 and 518 in Plain English](https://chadsmith-software.medium.com/pep-517-and-518-in-plain-english-47208ca8b7a6)
- [Python packaging - Past, Present, Future](https://bernat.tech/posts/pep-517-518/)
- [What is PEP 517/518 compatibility?](https://pydevtools.com/handbook/explanation/what-is-pep-517/)
- [Modern pip build process (–use-pep517)](https://fromkk.com/posts/modern-pip-build-process-use-pep517/)
- [What is a build backend?](https://pydevtools.com/handbook/explanation/what-is-a-build-backend/)