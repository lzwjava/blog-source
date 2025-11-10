---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Correction de l'erreur du backend d'imagerie PIL
translated: true
type: note
---

Cette erreur signifie que votre installation de PIL soit n'a pas son backend binaire (`_imaging`), soit que vous utilisez accidentellement l'ancien package « PIL » au lieu du moderne « Pillow ». Voici comment la résoudre :

1. **Assurez-vous d'utiliser Python 3**
   Si `python` pointe vers Python 2, passez à Python 3 :

   ```bash
   python3 --version
   python3 scripts/content/avatar.py
   ```

2. **Désinstallez tout ancien package PIL**

   ```bash
   # Ceci supprime l'ancien PIL s'il est installé via pip
   python3 -m pip uninstall -y PIL
   ```

3. **(Ré)installez Pillow**

   ```bash
   python3 -m pip install --upgrade --force-reinstall pillow
   ```

4. **Installez les bibliothèques système requises**
   Sur Ubuntu, vous aurez besoin des en-têtes d'imagerie pour que Pillow puisse construire son extension `_imaging` :

   ```bash
   sudo apt update
   sudo apt install -y libjpeg-dev zlib1g-dev
   # puis réinstallez Pillow pour qu'il se recompile avec ces bibliothèques
   python3 -m pip install --upgrade --force-reinstall pillow
   ```

5. **Utilisez un environnement virtuel (optionnel mais recommandé)**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install pillow
   python scripts/content/avatar.py
   ```

Après cela, `from PIL import Image` devrait fonctionner sans l'erreur d'import `_imaging`.