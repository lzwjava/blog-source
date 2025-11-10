---
audio: false
generated: true
lang: de
layout: post
title: Behebung des HEIC-Unterstützungsfehlers bei Kissen
translated: true
type: note
---

Der Fehler `cannot identify image file` zeigt an, dass Pillow die HEIC-Dateien nicht lesen kann, wahrscheinlich aus einem der folgenden Gründe:
1. **Fehlende `libheif`-Bibliothek**: Pillow benötigt `libheif` für die Verarbeitung von HEIC-Dateien, und diese ist möglicherweise nicht auf Ihrem System installiert oder korrekt konfiguriert.
2. **Beschädigte oder inkompatible HEIC-Dateien**: Die HEIC-Dateien könnten beschädigt sein oder ein Format haben, das Pillow nicht verarbeiten kann.
3. **Pillow-Versionsproblem**: Obwohl Pillow 9.0.0+ HEIC unterstützt, könnte ein Konfigurationsproblem oder eine veraltete Version vorliegen.

Da Sie macOS verwenden (basierend auf Ihrer vorherigen Ausgabe), werde ich ein korrigiertes Python-Skript bereitstellen, das zusätzliche Fehlerbehandlung und Protokollierung enthält, um das Problem zu diagnostizieren. Ich werde Sie auch durch die Installation von `libheif` und die Überprüfung der HEIC-Unterstützung von Pillow führen. Falls Pillow weiterhin fehlschlägt, enthält das Skript einen Fallback auf `ImageMagick` (falls installiert) für die HEIC-Konvertierung.

### Schritte zur Fehlerbehebung

#### 1. Installieren Sie `libheif`
Pillow benötigt `libheif` für die HEIC-Unterstützung. Installieren Sie es mit Homebrew:
```bash
brew install libheif
```
Installieren Sie Pillow danach neu, um sicherzustellen, dass es mit `libheif` verknüpft wird:
```bash
pip uninstall pillow
pip install pillow
```

#### 2. Überprüfen Sie die Pillow HEIC-Unterstützung
Prüfen Sie, ob Pillow HEIC-Dateien verarbeiten kann:
```bash
python -c "from PIL import features; print(features.check_feature('heic'))"
```
- Wenn es `True` ausgibt, hat Pillow HEIC-Unterstützung.
- Wenn es `False` oder einen Fehler ausgibt, ist `libheif` nicht korrekt konfiguriert oder Pillow wurde ohne HEIC-Unterstützung erstellt.

#### 3. Überprüfen Sie die Dateiintegrität
Stellen Sie sicher, dass die HEIC-Dateien nicht beschädigt sind. Versuchen Sie, eine der Dateien (z.B. `IMG_5988.HEIC`) in einem Viewer wie Vorschau auf macOS zu öffnen. Wenn sie sich nicht öffnen lässt, sind die Dateien möglicherweise beschädigt, und Sie müssen sie neu exportieren oder neue Kopien beschaffen.

#### 4. Aktualisiertes Python-Skript
Das aktualisierte Skript:
- Verwendet Pillow für die HEIC-Konvertierung mit verbesserter Fehlerbehandlung.
- Fällt auf `ImageMagick` zurück (falls installiert), wenn Pillow eine HEIC-Datei nicht lesen kann.
- Protokolliert detaillierte Fehler in einer Datei (`conversion_errors.log`) zur Fehlersuche.
- Unterstützt sowohl `.heic` als auch `.heif` Erweiterungen.
- Komprimiert Ausgabe-JPGs auf ~500KB.

```python
import os
import argparse
import subprocess
import logging
from PIL import Image
from datetime import datetime

# Set up logging
logging.basicConfig(
    filename="conversion_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Convert HEIC images to JPG and compress to ~500KB.")
parser.add_argument("input_dir", help="Directory containing HEIC files")
args = parser.parse_args()

# Define input and output directories
input_dir = args.input_dir.rstrip(os.sep)
output_dir = input_dir + "_compressed"
target_size_kb = 500  # Target file size in KB

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def get_file_size(file_path):
    """Return file size in KB."""
    return os.path.getsize(file_path) / 1024

def convert_with_imagemagick(heic_path, jpg_path):
    """Fallback to ImageMagick for HEIC to JPG conversion."""
    try:
        subprocess.run(
            ["magick", heic_path, "-quality", "85", jpg_path],
            check=True, capture_output=True, text=True
        )
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"ImageMagick failed for {heic_path}: {e.stderr}")
        return False
    except FileNotFoundError:
        logging.error("ImageMagick not installed. Install it with 'brew install imagemagick'.")
        return False

def convert_heic_to_jpg(heic_path, jpg_path, quality=85):
    """Convert HEIC to JPG and compress to approximate target size."""
    try:
        # Try Pillow first
        image = Image.open(heic_path)
        if image.mode != "RGB":
            image = image.convert("RGB")
        
        # Save as JPG with initial quality
        image.save(jpg_path, "JPEG", quality=quality)
        
        # Adjust quality to approach target size
        current_size = get_file_size(jpg_path)
        low, high = 10, 100
        while low <= high and abs(current_size - target_size_kb) > 10:
            quality = (low + high) // 2
            image.save(jpg_path, "JPEG", quality=quality)
            current_size = get_file_size(jpg_path)
            if current_size > target_size_kb:
                high = quality - 1
            else:
                low = quality + 1
        return True
    except Exception as e:
        logging.error(f"Pillow failed for {heic_path}: {e}")
        # Fallback to ImageMagick
        return convert_with_imagemagick(heic_path, jpg_path)

# Process all HEIC files in the input directory
for filename in os.listdir(input_dir):
    if filename.lower().endswith((".heic", ".heif")):
        heic_path = os.path.join(input_dir, filename)
        jpg_filename = os.path.splitext(filename)[0] + ".jpg"
        jpg_path = os.path.join(output_dir, jpg_filename)

        try:
            if convert_heic_to_jpg(heic_path, jpg_path):
                print(f"Converted {filename} to {jpg_filename}, size: {get_file_size(jpg_path):.2f} KB")
            else:
                print(f"Error processing {filename}: Conversion failed (check conversion_errors.log)")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
            logging.error(f"General error for {heic_path}: {e}")

print("Batch conversion complete! Check conversion_errors.log for any issues.")
```

### Verwendung
1. **Speichern Sie das Skript**:
   Speichern Sie den Code als `photo_compress.py` in Ihrem `scripts/media/` Verzeichnis.

2. **Installieren Sie die Abhängigkeiten**:
   - Stellen Sie sicher, dass Pillow installiert ist:
     ```bash
     pip install --upgrade pillow
     ```
   - Installieren Sie `libheif`:
     ```bash
     brew install libheif
     ```
   - Optional: Installieren Sie ImageMagick für den Fallback:
     ```bash
     brew install imagemagick
     ```

3. **Führen Sie das Skript aus**:
   ```bash
   python scripts/media/photo_compress.py ./assets/images/yuebei
   ```
   - Dies verarbeitet alle `.heic` und `.heif` Dateien in `assets/images/yuebei`.
   - Ausgabe-JPGs werden in `assets/images/yuebei_compressed` gespeichert.
   - Fehler werden in `conversion_errors.log` im aktuellen Verzeichnis protokolliert.

4. **Überprüfen Sie das Protokoll**:
   Wenn Dateien nicht konvertiert werden konnten, überprüfen Sie `conversion_errors.log` auf detaillierte Fehlermeldungen.

### Zusätzliche Fehlerbehebung
- **Falls Pillow weiterhin fehlschlägt**:
  - Verifizieren Sie, dass `libheif` korrekt installiert und verknüpft ist:
    ```bash
    pkg-config --modversion libheif
    ```
    Wenn dies fehlschlägt, installieren Sie `libheif` und Pillow neu.
  - Testen Sie eine einzelne Datei manuell:
    ```python
    from PIL import Image
    img = Image.open("./assets/images/yuebei/IMG_5988.HEIC")
    print("Image opened successfully")
    ```
    Wenn dies fehlschlägt, ist die Datei möglicherweise beschädigt oder liegt in einer nicht unterstützten HEIC-Variante vor.

- **Beschädigte Dateien**:
  - Versuchen Sie, eine Datei manuell mit ImageMagick zu konvertieren:
    ```bash
    magick ./assets/images/yuebei/IMG_5988.HEIC test.jpg
    ```
    Wenn dies fehlschlägt, ist die Datei wahrscheinlich beschädigt.

- **ImageMagick Fallback**:
  - Falls Pillow konsistent fehlschlägt, versucht das Skript, ImageMagick zu verwenden (falls installiert).
  - Installieren Sie `jpegoptim` für eine bessere Komprimierungskontrolle:
    ```bash
    brew install jpegoptim
    ```
    Komprimieren Sie danach die Ausgabe:
    ```bash
    for i in ./assets/images/yuebei_compressed/*.jpg; do jpegoptim --size=500k "$i"; done
    ```

### Referenzen
- [Pillow Documentation](https://pillow.readthedocs.io/en/stable/)
- [ImageMagick](https://imagemagick.org/)
- [libheif](https://github.com/strukturag/libheif)
- [jpegoptim](https://github.com/tjko/jpegoptim)

Wenn Sie weiterhin Probleme haben, teilen Sie den Inhalt von `conversion_errors.log` oder neue Fehlermeldungen mit, und ich kann weitere Unterstützung bieten!