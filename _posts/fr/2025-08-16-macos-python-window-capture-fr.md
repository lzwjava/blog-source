---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Méthodes de Capture de Fenêtre Python sous macOS
translated: true
type: note
---

Bonne question 👍 — `pygetwindow` est un wrapper léger, mais il existe plusieurs autres bibliothèques Python que vous pouvez utiliser sur macOS pour obtenir la géométrie de la fenêtre active pour les captures d'écran :

---

## 1. **PyObjC + Quartz (API macOS native)**

C'est la méthode la plus directe et la plus fiable sur macOS, car `Quartz` vous donne les informations sur les fenêtres au niveau du système. Exemple :

```bash
python3 -m pip install pyobjc
```

```python
import Quartz
from PIL import ImageGrab

# Obtenir les limites de la fenêtre active
window_info = Quartz.CGWindowListCopyWindowInfo(
    Quartz.kCGWindowListOptionOnScreenOnly, Quartz.kCGNullWindowID
)

active_app = Quartz.CGWindowListCopyWindowInfo(
    Quartz.kCGWindowListOptionOnScreenOnly | Quartz.kCGWindowListOptionOnScreenAbove,
    Quartz.kCGNullWindowID,
)

if active_app:
    bounds = active_app[0]['kCGWindowBounds']
    x, y = int(bounds['X']), int(bounds['Y'])
    w, h = int(bounds['Width']), int(bounds['Height'])
    img = ImageGrab.grab(bbox=(x, y, x + w, y + h))
    img.save("active-window.png")
    print(f"Saved active-window.png size={img.size}")
```

Cela évite de dépendre de `pygetwindow` et communique directement avec CoreGraphics.

---

## 2. **AppKit (via PyObjC)**

Également via PyObjC, mais à travers AppKit :

```python
from AppKit import NSWorkspace

ws = NSWorkspace.sharedWorkspace()
active_app = ws.frontmostApplication()
print("Active App:", active_app.localizedName())
```

Vous auriez toujours besoin de `Quartz` pour les coordonnées, mais AppKit vous donne le processus au premier plan plus proprement.

---

## 3. **PyWinCtl**

Remplaçant multiplateforme pour `pygetwindow` (Windows, macOS, Linux) :

```bash
python3 -m pip install pywinctl
```

```python
import pywinctl
from PIL import ImageGrab

active = pywinctl.getActiveWindow()
if active:
    x, y, w, h = active.left, active.top, active.width, active.height
    img = ImageGrab.grab(bbox=(x, y, x + w, y + h))
    img.save("active-window.png")
    print("Saved active-window.png")
```

C'est probablement l'alternative la plus proche de "remplacement direct" à pygetwindow, mais avec un support macOS plus cohérent.

---

## 4. **PyAutoGUI**

Bien que PyAutoGUI lui-même ne fournisse pas de gestionnaires de fenêtres, vous pouvez capturer l'écran entier ou définir une région manuellement une fois que vous connaissez les coordonnées (depuis Quartz/AppKit).

---

✅ Si vous voulez un **remplacement purement multiplateforme** pour `pygetwindow` : utilisez **`pywinctl`**.
✅ Si vous voulez **une précision native macOS et plus de contrôle** : utilisez **PyObjC + Quartz**.

Voulez-vous que je vous montre un script prêt à l'emploi qui **dépend uniquement de PyObjC (Quartz)** (sans wrappers tiers), afin que vous puissiez abandonner complètement `pygetwindow` ?