---
audio: false
generated: true
lang: fr
layout: post
title: Résoudre l'erreur ModuleNotFoundError de Python distutils
translated: true
type: note
---

L'erreur se produit car le module `distutils`, faisant partie de la bibliothèque standard de Python, est manquant dans votre environnement. Ceci est courant dans les installations Python minimales. Voici comment la résoudre :

### Solution :
1. **Installer les outils de développement Python** (inclut `distutils`) :
   ```bash
   sudo apt update && sudo apt install python3-distutils python3-dev
   ```

2. **Réinstaller `setuptools`** (pour garantir un fonctionnement correct) :
   ```bash
   pip install --upgrade --force-reinstall setuptools
   ```

3. **Réessayer l'installation de vos requirements** :
   ```bash
   pip install -r requirements.local.txt
   ```

### Pourquoi cela fonctionne :
- `python3-distutils` fournit le module manquant `distutils`.
- `python3-dev` inclut les en-têtes et outils de compilation nécessaires.
- La réinstallation de `setuptools` résout tout problème de configuration persistant.

Si vous êtes dans un environnement virtuel, recréez-le après avoir installé les paquets système pour vous assurer que l'environnement a accès aux modules requis.