---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Bildschirmfoto-Anleitung mit PIL ImageGrab
translated: true
type: note
---

### Voraussetzungen
Um `ImageGrab` aus der PIL (Pillow)-Bibliothek zu verwenden, stellen Sie sicher, dass Pillow installiert ist. Unter Windows installieren Sie es über pip:
```
pip install Pillow
```
Typischerweise ist unter Windows keine zusätzliche Einrichtung erforderlich, da `ImageGrab` native Windows-APIs verwendet.

### Grundlegende Verwendung
`ImageGrab.grab()` erfasst den gesamten Bildschirm (alle Monitore) als ein PIL Image-Objekt. Hier ein einfaches Beispiel, um einen Screenshot aufzunehmen und als PNG-Datei zu speichern:

```python
from PIL import ImageGrab

# Erfasst den gesamten Bildschirm
screenshot = ImageGrab.grab()

# Speichert das Bild in einer Datei
screenshot.save("screenshot.png")
```

Dies speichert eine Datei namens `screenshot.png` in Ihrem aktuellen Arbeitsverzeichnis.

### Zusätzliche Optionen
- **Einen bestimmten Bereich erfassen**: Geben Sie einen Begrenzungsrahmen (links, oben, rechts, unten) als Tupel von Pixelkoordinaten an.
  ```python
  # Erfasst einen 300x300 Pixel Bereich beginnend bei (100, 100)
  region = (100, 100, 400, 400)  # Koordinaten nach Bedarf anpassen
  screenshot = ImageGrab.grab(bbox=region)
  screenshot.save("region_screenshot.png")
  ```
- **Mauszeiger einbeziehen** (falls unterstützt; überprüfen Sie die Pillow-Dokumentation für Versionsdetails):
  ```python
  # Hinweis: Dies erfordert auf einigen Systemen möglicherweise include_layered_windows=True
  screenshot = ImageGrab.grab(include_layered_windows=True)
  ```
- **Bild anzeigen**: Verwenden Sie `screenshot.show()`, um es in Ihrem Standard-Bildbetrachter zu öffnen (zum Testen).

### Hinweise
- Koordinaten sind in Pixeln angegeben, wobei (0, 0) sich oben links am primären Monitor befindet.
- Bei Multi-Monitor-Setups erfasst `grab()` alle Bildschirme als ein zusammengesetztes Bild.
- Wenn Sie auf Probleme stoßen (z.B. Berechtigungsfehler unter neueren Windows-Versionen), stellen Sie sicher, dass Ihr Skript Bildschirmaufnahmeberechtigungen hat, oder versuchen Sie, es mit Administratorrechten auszuführen.
- Vollständige Dokumentation: [Pillow ImageGrab docs](https://pillow.readthedocs.io/en/stable/reference/ImageGrab.html). Für Windows-spezifische Eigenheiten, überprüfen Sie bei Bedarf GitHub-Issues.