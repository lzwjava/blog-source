---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Pillow Bildverarbeitungsleitfaden
translated: true
type: note
---

### Was ist PIL/Pillow?
PIL stand ursprünglich für Python Imaging Library, wird aber jetzt als Pillow-Paket (ein moderner Fork) weiterentwickelt. Man importiert es im Code als `PIL`, muss aber Pillow über pip installieren. Es wird zum Öffnen, Bearbeiten und Speichern von Bilddateien in Python verwendet. Unterstützt Formate wie JPEG, PNG, GIF, BMP und mehr.

### Installation
Um PIL zu verwenden, installiere Pillow:
```bash
pip install pillow
```

### Grundlegender Import und Verwendung
Nach der Installation importierst du es wie folgt in deinem Python-Skript:
```python
from PIL import Image
```
`import PIL.Image` ist nicht nötig – dies importiert das Image-Modul direkt.

### Häufige Bildoperationen
So führst du grundlegende Aufgaben aus. Gehe davon aus, dass du eine Bilddatei namens `example.jpg` in deinem Verzeichnis hast.

#### 1. Ein Bild öffnen
```python
image = Image.open('example.jpg')  # Öffnet die Bilddatei
image.show()  # Zeigt es an (funktioniert auf Systemen mit einem Bildbetrachter)
```

#### 2. Bildinformationen abrufen
```python
print(image.format)  # z.B. 'JPEG'
print(image.size)    # Tupel: (Breite, Höhe)
print(image.mode)    # z.B. 'RGB' für Farbbilder
```

#### 3. Bildgröße ändern
```python
resized = image.resize((800, 600))  # Auf 800x600 Pixel verkleinern/vergrößern
resized.save('resized_example.jpg')  # Das angepasste Bild speichern
```

#### 4. Formate konvertieren
```python
image.convert('L').save('grayscale_example.png')  # In Graustufen konvertieren und als PNG speichern
```

#### 5. Ein Bild drehen
```python
rotated = image.rotate(90)  # Um 90 Grad im Uhrzeigersinn drehen
rotated.save('rotated_example.jpg')
```

#### 6. Ein Bild zuschneiden
```python
left, top, right, bottom = 100, 100, 300, 300  # Zuschneidebereich definieren (x1, y1, x2, y2)
cropped = image.crop((left, top, right, bottom))
cropped.save('cropped_example.jpg')
```

#### 7. Filter anwenden (erfordert zusätzliche Imports)
Für Filter importiere `ImageFilter`:
```python
from PIL import ImageFilter
blurred = image.filter(ImageFilter.BLUR)  # Weichzeichnungsfilter anwenden
blurred.save('blurred_example.jpg')
```

### Erweitertes Beispiel: Stapelverarbeitung mehrerer Bilder
```python
import os
from PIL import Image

# Alle JPEG-Bilder in einem Ordner auf 200x200 skalieren
input_folder = 'images/'
output_folder = 'resized_images/'
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith('.jpg'):
        image = Image.open(os.path.join(input_folder, filename))
        resized = image.resize((200, 200))
        resized.save(os.path.join(output_folder, filename))
```

### Tipps und Hinweise
- **Fehlerbehandlung**: Verwende try-except für ungültige Dateien, z.B. `try: image = Image.open('file.jpg')`.
- **Speichereffizienz**: Bei großen Bildern verwende `image.close()` nach den Operationen, um Speicher freizugeben.
- **Dokumentation**: Siehe die vollständige Dokumentation von Pillow unter [pillow.readthedocs.io](https://pillow.readthedocs.io/en/stable/) für weitere Funktionen wie Zeichnen, Text hinzufügen oder EXIF-Daten auslesen.
- **Abhängigkeiten**: Pillow benötigt möglicherweise Systembibliotheken (z.B. libjpeg) auf einigen Systemen; siehe den Installationsleitfaden, falls Probleme auftreten.

Wenn du eine konkrete Aufgabe oder einen Fehler hast, teile mehr Details mit, um maßgeschneiderte Hilfe zu erhalten!