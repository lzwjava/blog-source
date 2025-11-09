---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Gestion des Dépendances Python avec Poetry
translated: true
type: note
---

### Qu'est-ce que Poetry ?

Poetry est un outil de gestion des dépendances et d'empaquetage en Python. Il vous permet de déclarer les bibliothèques dont votre projet dépend, et il gère leur installation, leur mise à jour et leur résolution automatiquement tout en garantissant des environnements reproductibles.

### Objectif principal
Poetry simplifie les flux de travail des projets Python en gérant les dépendances via un seul fichier de configuration (`pyproject.toml`), en créant un fichier de verrouillage pour des installations cohérentes sur différentes machines, et en prenant en charge la construction de projets pour la distribution (par exemple, vers PyPI). Il est conçu pour remplacer des outils fragmentés comme `pip`, `pipenv` et `setuptools` par une approche unifiée et conviviale.

### Fonctionnalités clés
- **Résolution des dépendances** : Installe et met à jour automatiquement les dépendances en résolvant intelligemment les conflits.
- **Fichier de verrouillage** : Génère `poetry.lock` pour figer les versions exactes et assurer des builds reproductibles.
- **Environnements virtuels** : Crée des environnements isolés par projet pour éviter la pollution globale.
- **Empaquetage** : Construit des wheels ou des sdists pour une distribution facile.
- **Support multi-plateforme** : Fonctionne sur Linux, macOS et Windows.
- **Intégration au shell** : Complétion par tabulation pour Bash, Fish et Zsh.
- **Compatible Python 3.9+** : Requiert des versions modernes de Python.

### Installation
Installez Poetry dans un environnement isolé en utilisant `pipx` (recommandé pour un accès global sans conflits) :

1. Installez `pipx` si nécessaire (via le gestionnaire de paquets de votre OS ou `python -m pip install --user pipx`).
2. Exécutez : `pipx install poetry`.

Pour les mises à jour : `pipx upgrade poetry`.  
Pour la désinstallation : `pipx uninstall poetry`.

Activez les complétions du shell (par exemple, pour Bash : `poetry completions bash >> ~/.bash_completion`).

### Utilisation de base
Initialiser un nouveau projet : `poetry init`.  
Ajouter une dépendance : `poetry add requests`.  
Installer à partir du fichier de verrouillage : `poetry install`.  
Exécuter des scripts : `poetry run python script.py`.  
Construire le package : `poetry build`.

Pour la liste complète des commandes, consultez la documentation.

[Documentation de Poetry](https://python-poetry.org/docs/)