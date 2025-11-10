---
audio: false
generated: true
lang: fr
layout: post
title: Accès au Presse-papiers de Python sur Ubuntu
translated: true
type: note
---

Pour lire le contenu du presse-papiers (clipboard) dans Ubuntu en utilisant Python, vous pouvez utiliser des bibliothèques comme `pyperclip` ou interagir avec les utilitaires système comme `xclip` ou `xsel`. Voici deux approches courantes :

### Approche 1 : Utilisation de `pyperclip`
`pyperclip` est une bibliothèque Python multiplateforme pour accéder au presse-papiers.

1. **Installer pyperclip** :
   ```bash
   pip install pyperclip
   ```

2. **Code Python pour lire le presse-papiers** :
   ```python
   import pyperclip

   # Lire le contenu du presse-papiers
   clipboard_content = pyperclip.paste()
   print(clipboard_content)
   ```

3. **Notes** :
   - Assurez-vous que `xclip` ou `xsel` est installé sur Ubuntu, car `pyperclip` en dépend :
     ```bash
     sudo apt update
     sudo apt install xclip xsel
     ```
   - Cette méthode est simple et fonctionne sur plusieurs plateformes.

### Approche 2 : Utilisation directe de `xclip`
Si vous préférez interagir directement avec le presse-papiers système, vous pouvez utiliser `xclip`.

1. **Installer xclip** :
   ```bash
   sudo apt update
   sudo apt install xclip
   ```

2. **Code Python pour lire le presse-papiers en utilisant `xclip`** :
   ```python
   import subprocess

   # Lire le contenu du presse-papiers
   process = subprocess.run(['xclip', '-selection', 'clipboard', '-o'], capture_output=True, text=True)
   clipboard_content = process.stdout
   print(clipboard_content)
   ```

3. **Notes** :
   - Cette approche appelle directement l'outil en ligne de commande `xclip`.
   - Utilisez `-selection clipboard` pour le presse-papiers moderne (Ctrl+C/Ctrl+V) ou `-selection primary` pour le presse-papiers de sélection à la souris.
   - Assurez-vous que `xclip` est installé.

### Recommandations
- **Utilisez `pyperclip`** pour sa simplicité et sa portabilité, sauf si vous avez des raisons spécifiques d'utiliser `xclip` ou `xsel`.
- Les deux méthodes nécessitent l'installation de `xclip` ou `xsel` pour accéder au presse-papiers sur Ubuntu.
- Si le contenu du presse-papiers n'est pas du texte (par exemple, une image), ces méthodes peuvent ne pas fonctionner comme prévu, et vous auriez besoin d'une bibliothèque comme `pyclip` ou d'une gestion supplémentaire pour les données non textuelles.

Testé sur Ubuntu 22.04 avec Python 3.10. Si vous rencontrez des problèmes, assurez-vous que les outils requis (`xclip` ou `xsel`) sont installés et que le presse-papiers contient des données textuelles.