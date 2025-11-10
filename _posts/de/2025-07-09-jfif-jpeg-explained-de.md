---
audio: false
generated: true
image: false
lang: de
layout: post
title: JFIF ist nur JPEG erklärt
translated: true
type: note
---

JFIF steht für **JPEG File Interchange Format**.

### Was JFIF ist

* Es ist kein anderes Bildformat als JPEG, sondern vielmehr eine **standardisierte Methode, Metadaten und Struktur in einer JPEG-Datei einzubetten**.
* Dateien mit der Endung `.jfif` sind immer noch **JPEG-Bilder** — sie deklarieren lediglich die JFIF-Spezifikation explizit in ihren Headern.
* Viele Tools (insbesondere ältere wie Windows Paint oder einige Kameras/Scanner) verwendeten `.jfif` als Standarderweiterung anstelle von `.jpg` oder `.jpeg`.

Wenn Sie also eine `.jfif`-Datei sehen, können Sie sie genauso behandeln wie ein `.jpg`-Bild.

---

### Wie man JFIF in Standard-Bildformate konvertiert

1. **Dateiendung umbenennen**

   * In den meisten Fällen benennen Sie einfach `bild.jfif` → `bild.jpg` um.
   * Da das zugrunde liegende Format JPEG ist, öffnen die meisten Programme die Datei ohne Probleme.

2. **Verwendung von Bildbearbeitungsprogrammen**

   * Öffnen Sie die `.jfif`-Datei in Photoshop, GIMP, Paint oder Preview (macOS).
   * Speichern/Exportieren Sie sie als `.jpg` oder `.png`.

3. **Verwendung von Python (Pillow)**

   ```python
   from PIL import Image

   img = Image.open("bild.jfif")
   img.save("bild.jpg")   # Als JPEG speichern
   img.save("bild.png")   # Oder in PNG konvertieren
   ```

4. **Verwendung der Kommandozeile (ImageMagick)**

   ```bash
   magick bild.jfif bild.jpg
   ```

   Oder mit FFmpeg (da es auch Bilder decodieren kann):

   ```bash
   ffmpeg -i bild.jfif bild.jpg
   ```

---

✅ Zusammenfassend: **JFIF ist nur ein JPEG**, also können Sie es wie jede `.jpg`-Datei öffnen. Falls Kompatibilitätsprobleme auftreten, benennen Sie es einfach um oder konvertieren Sie es mit Pillow/ImageMagick.

Möchten Sie, dass ich Ihnen ein kurzes **Python-Skript** gebe, das alle `.jfif`-Dateien in einem Ordner stapelweise in `.jpg` konvertieren kann?