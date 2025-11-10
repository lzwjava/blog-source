---
audio: false
generated: true
image: false
lang: de
layout: post
title: MacOS Python Fensteraufnahme Methoden
translated: true
type: note
---

Gute Frage 👍 — `pygetwindow` ist ein leichtgewichtiger Wrapper, aber es gibt mehrere andere Python-Bibliotheken, die du auf macOS verwenden kannst, um die Geometrie des aktiven Fensters für Screenshots zu erhalten:

---

## 1. **PyObjC + Quartz (native macOS-API)**

Dies ist der direkteste und zuverlässigste Weg auf macOS, da `Quartz` dir Fensterinformationen auf Systemebene liefert. Beispiel:

```bash
python3 -m pip install pyobjc
```

```python
import Quartz
from PIL import ImageGrab

# Begrenzungen des aktiven Fensters abrufen
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

Dies vermeidet die Abhängigkeit von `pygetwindow` und kommuniziert direkt mit CoreGraphics.

---

## 2. **AppKit (über PyObjC)**

Ebenfalls aus PyObjC, aber über AppKit:

```python
from AppKit import NSWorkspace

ws = NSWorkspace.sharedWorkspace()
active_app = ws.frontmostApplication()
print("Active App:", active_app.localizedName())
```

Du würdest immer noch `Quartz` für die Koordinaten benötigen, aber AppKit liefert dir den Vordergrundprozess sauberer.

---

## 3. **PyWinCtl**

Plattformübergreifender Ersatz für `pygetwindow` (Windows, macOS, Linux):

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

Dies ist wahrscheinlich die ähnlichste "Drop-in"-Alternative zu pygetwindow, aber mit besserer macOS-Unterstützung.

---

## 4. **PyAutoGUI**

Während PyAutoGUI selbst keine Fenster-Handles bereitstellt, kannst du den gesamten Bildschirm aufnehmen oder eine Region manuell definieren, sobald du die Koordinaten kennst (von Quartz/AppKit).

---

✅ Wenn du einen **rein plattformübergreifenden Ersatz** für `pygetwindow` möchtest: verwende **`pywinctl`**.
✅ Wenn du **native macOS-Präzision und mehr Kontrolle** möchtest: verwende **PyObjC + Quartz**.

Soll ich dir ein gebrauchsfertiges Skript zeigen, das **nur von PyObjC (Quartz) abhängt** (keine Third-Party-Wrapper), damit du `pygetwindow` komplett ersetzen kannst?