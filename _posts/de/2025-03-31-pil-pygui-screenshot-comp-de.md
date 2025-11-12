---
audio: false
generated: true
image: false
lang: de
layout: post
title: PIL vs PyAutoGUI Screenshot-Vergleich
translated: true
type: note
---

Sowohl **PILs `ImageGrab`** als auch **die Screenshot-Tools von PyAutoGUI** ermöglichen es Ihnen, den Bildschirm zu erfassen, aber sie unterscheiden sich in der Verwendung, den Funktionen und der plattformübergreifenden Unterstützung.

---

## 1. PIL (Pillow) – `ImageGrab`

`ImageGrab` ist Teil von **Pillow (dem modernen PIL Fork)**. Es ermöglicht Ihnen, den gesamten Bildschirm oder einen Teil davon zu erfassen.

### So funktioniert es

* Unter **Windows und macOS** verwendet es native APIs (GDI unter Windows, Quartz unter macOS), um Pixel zu erfassen.
* Unter **Linux** wird es standardmäßig nicht unterstützt (benötigt zusätzliche Bibliotheken wie `xwd`).

### Beispiel zur Verwendung

```python
from PIL import ImageGrab

# Vollbild aufnehmen
screenshot = ImageGrab.grab()
screenshot.save("screenshot.png")

# Einen Bereich aufnehmen (links, oben, rechts, unten)
region = (100, 100, 500, 500)
cropped_screenshot = ImageGrab.grab(bbox=region)
cropped_screenshot.show()
```

### Vorteile

* Einfach, Teil von Pillow (keine zusätzliche Abhängigkeit).
* Gut, wenn Sie bereits mit Pillow für die Bildverarbeitung arbeiten.

### Nachteile

* Standardmäßig keine Linux-Unterstützung.
* Weniger Flexibilität (keine Multi-Monitor-Unterstützung).

---

## 2. PyAutoGUI – `screenshot()`

PyAutoGUI ist allgemeiner für Automatisierung (Maus/Tastatur + Bildschirmaufnahme).

### So funktioniert es

* Verwendet intern **Pillow**.
* Nutzt Betriebssystem-APIs (plattformübergreifend: Windows, macOS, Linux).
* Kann ein Pillow-`Image` direkt zurückgeben oder in einer Datei speichern.

### Beispiel zur Verwendung

```python
import pyautogui

# Vollbild aufnehmen
screenshot = pyautogui.screenshot()
screenshot.save("screenshot.png")

# Einen Bereich aufnehmen (links, oben, Breite, Höhe)
region_screenshot = pyautogui.screenshot(region=(100, 100, 400, 400))
region_screenshot.show()
```

### Vorteile

* Plattformübergreifend (Windows, macOS, Linux).
* Einfach in Automatisierungsskripte zu integrieren (Maus-/Tastatursteuerung).
* Kann bestimmte Bereiche direkt erfassen.

### Nachteile

* Etwas langsamer als `ImageGrab`, da es mehr abstrahiert.
* Zusätzliche Abhängigkeit (`pip install pyautogui`).

---

## Was sollten Sie verwenden?

* **Wenn Sie nur Screenshots benötigen und unter Windows/macOS arbeiten** → `ImageGrab` ist leichtgewichtig und schnell.
* **Wenn Sie auch Automatisierung oder Linux-Unterstützung benötigen** → `pyautogui` ist besser.

---

👉 Möchten Sie, dass ich Ihnen auch zeige, **wie man den Leistungsunterschied** zwischen `ImageGrab` und `pyautogui.screenshot()` mit Python-Code **benchmarked**?