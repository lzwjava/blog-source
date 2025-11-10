---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Guide de Démarrage Rapide de PyGetWindow
translated: true
type: note
---

### Installation
PyGetWindow est une bibliothèque Python pour manipuler et interroger les fenêtres sur plusieurs plateformes (Windows, macOS et Linux). Installez-la via pip :

```bash
pip install pygetwindow
```

### Importation du module
Commencez par importer le module dans votre script Python :

```python
import pygetwindow as gw
```

### Obtention d'objets Window
PyGetWindow représente les fenêtres sous forme d'objets `Window`. Vous pouvez récupérer les fenêtres par titre, par processus ou par d'autres attributs.

- **Obtenir tous les objets Window** :  
  Utilisez `gw.getAllWindows()` pour renvoyer une liste de toutes les fenêtres ouvertes.

- **Obtenir les fenêtres par titre** :  
  Utilisez `gw.getWindowsWithTitle(title)` ou `gw.getFirstWindowWithTitle(title)` pour des correspondances partielles ou exactes.

- **Obtenir la fenêtre active** :  
  Utilisez `gw.getActiveWindow()` pour obtenir la fenêtre actuellement focalisée.

Exemple :
```python
windows = gw.getAllWindows()
active = gw.getActiveWindow()
notepad = gw.getWindowsWithTitle('Notepad')  # Liste des fenêtres avec 'Notepad' dans le titre
```

### Méthodes courantes sur les objets Window
Une fois que vous avez un objet `Window`, vous pouvez accéder à ses propriétés et méthodes comme :

- **Propriétés** : `title`, `left`, `top`, `width`, `height`, `isMinimized`, `isMaximized`, `isActive`.
- **Méthodes** : 
  - `activate()` : Amener la fenêtre au premier plan et la rendre active.
  - `maximize()` / `minimize()` / `restore()` / `close()` : Contrôler l'état de la fenêtre.
  - `resize() / move()` : Ajuster la taille et la position.

Exemple :
```python
if notepad:
    win = notepad[0]
    print(win.title)  # Sortie : par ex., 'Untitled - Notepad'
    win.activate()
    win.maximize()
    win.move(100, 100)  # Déplacer à la position (100, 100)
    win.resize(800, 600)  # Redimensionner à 800x600
```

### Gestion des plateformes multiples
- Sur Windows et macOS, il utilise des API natives.
- Sur Linux, il repose sur le support X11 ou Wayland ; assurez-vous qu'il est installé sur votre système (par ex., `x11-utils` sur Ubuntu).
- Si une méthode n'est pas supportée sur votre OS, elle peut lever une `NotImplementedError`.

### Exemples
Voici quelques extraits de code pratiques :

1. **Afficher tous les titres de fenêtre** :
   ```python
   for win in gw.getAllWindows():
       print(win.title)
   ```

2. **Fermer une fenêtre spécifique** :
   ```python
   firefox_wins = gw.getWindowsWithTitle('Mozilla Firefox')
   if firefox_wins:
       firefox_wins[0].close()
   ```

3. **Déplacer et redimensionner plusieurs fenêtres** :
   ```python
   windows = gw.getAllWindows()
   for i, win in enumerate(windows[:3]):  # Les 3 premières fenêtres
       win.move(50 * i, 50 * i)
       win.resize(400, 400)
   ```

Pour une utilisation avancée, reportez-vous à la [documentation officielle](https://pygetwindow.readthedocs.io/). Si vous rencontrez des problèmes spécifiques à une plateforme, vérifiez les permissions du système ou les dépendances comme `xdotool` sur Linux.