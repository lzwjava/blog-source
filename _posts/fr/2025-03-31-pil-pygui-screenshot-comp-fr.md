---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Comparaison de Captures d'Écran PIL vs PyAutoGUI
translated: true
type: note
---

À la fois **`ImageGrab` de PIL** et **les outils de capture d'écran de PyAutoGUI** vous permettent de capturer l'écran, mais ils diffèrent par leur utilisation, leurs fonctionnalités et leur support multiplateforme.

---

## 1. PIL (Pillow) – `ImageGrab`

`ImageGrab` fait partie de **Pillow (la version moderne de PIL)**. Il vous permet de capturer l'écran ou une partie de celui-ci.

### Comment ça fonctionne

* Sur **Windows et macOS**, il utilise des API natives (GDI sur Windows, Quartz sur macOS) pour capturer les pixels.
* Sur **Linux**, il n'est pas supporté par défaut (nécessite des bibliothèques supplémentaires comme `xwd`).

### Exemple d'utilisation

```python
from PIL import ImageGrab

# Capture d'écran complète
screenshot = ImageGrab.grab()
screenshot.save("screenshot.png")

# Capture d'une région (gauche, haut, droite, bas)
region = (100, 100, 500, 500)
cropped_screenshot = ImageGrab.grab(bbox=region)
cropped_screenshot.show()
```

### Avantages

* Simple, fait partie de Pillow (pas de dépendance supplémentaire).
* Pratique si vous utilisez déjà Pillow pour le traitement d'image.

### Inconvénients

* Pas de support Linux par défaut.
* Moins de flexibilité (pas de prise en charge multi-écran).

---

## 2. PyAutoGUI – `screenshot()`

PyAutoGUI est plus polyvalent et destiné à l'automatisation (souris/clavier + capture d'écran).

### Comment ça fonctionne

* Utilise **Pillow en interne**.
* Utilise les API du système d'exploitation (multiplateforme : Windows, macOS, Linux).
* Peut retourner directement une `Image` Pillow ou l'enregistrer dans un fichier.

### Exemple d'utilisation

```python
import pyautogui

# Capture d'écran complète
screenshot = pyautogui.screenshot()
screenshot.save("screenshot.png")

# Capture d'une région (gauche, haut, largeur, hauteur)
region_screenshot = pyautogui.screenshot(region=(100, 100, 400, 400))
region_screenshot.show()
```

### Avantages

* Multiplateforme (Windows, macOS, Linux).
* Facile à intégrer dans des scripts d'automatisation (contrôle souris/clavier).
* Peut capturer des régions spécifiques directement.

### Inconvénients

* Légèrement plus lent que `ImageGrab` car il ajoute une couche d'abstraction.
* Dépendance supplémentaire (`pip install pyautogui`).

---

## Lequel devriez-vous utiliser ?

* **Si vous n'avez besoin que de captures d'écran et que vous êtes sur Windows/macOS** → `ImageGrab` est léger et rapide.
* **Si vous avez aussi besoin d'automatisation ou d'un support Linux** → `pyautogui` est meilleur.

---

👉 Souhaitez-vous que je vous montre également **comment comparer les performances** entre `ImageGrab` et `pyautogui.screenshot()` avec du code Python ?