---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Python ZipFile-Paket Leitfaden
translated: true
type: note
---

### Übersicht des ZipFile-Pakets

Das `zipfile`-Modul von Python ermöglicht das Lesen von und Schreiben in ZIP-Archivdateien ohne externe Tools. Es ist Teil der Standardbibliothek, daher ist keine Installation erforderlich (ab Python 2.3+). Verwenden Sie es, um ZIP-Dateien programmgesteuert zu komprimieren, zu dekomprimieren oder zu manipulieren. Es unterstützt verschiedene Komprimierungsmethoden wie DEFLATE.

Importieren mit: `import zipfile`

### ZIP-Dateien lesen

Um vorhandene ZIP-Dateien zu extrahieren oder zu inspizieren:

1. **Eine ZIP-Datei zum Lesen öffnen**:
   ```python
   with zipfile.ZipFile('example.zip', 'r') as zip_ref:
       # 'r' steht für Lesemodus
   ```

2. **Inhalt auflisten**:
   ```python
   with zipfile.ZipFile('example.zip', 'r') as zip_ref:
       file_list = zip_ref.namelist()  # Gibt eine Liste der Dateinamen zurück
       print(file_list)
   ```

3. **Dateien extrahieren**:
   - Alle extrahieren: `zip_ref.extractall('ziel_ordner')`
   - Eine extrahieren: `zip_ref.extract('datei_im_zip.zip', 'pfad')`

4. **Dateiinhalt lesen ohne Extraktion**:
   ```python
   with zipfile.ZipFile('example.zip', 'r') as zip_ref:
       with zip_ref.open('datei_im_zip.zip') as file:
           content = file.read()
           print(content.decode())  # Falls es Text ist
   ```

Hinweis: Verwenden Sie immer `with` für automatisches Schließen. Für passwortgeschützte ZIPs fügen Sie `pwd=b'passwort'` zu `ZipFile()` hinzu.

### ZIP-Dateien schreiben

Um neue oder vorhandene ZIP-Dateien zu erstellen oder zu erweitern:

1. **Eine neue ZIP-Datei erstellen**:
   ```python
   with zipfile.ZipFile('new_archive.zip', 'w') as zip_ref:
       # 'w' steht für Schreibmodus (überschreibt, falls vorhanden)
   ```

2. **Dateien hinzufügen**:
   - Eine hinzufügen: `zip_ref.write('quelldatei.txt', 'zielname.txt')` (optionaler arcname benennt sie intern um)
   - Mehrere hinzufügen: Über eine Liste von Dateien iterieren und `write()` aufrufen.

3. **Beim Schreiben komprimieren** (Standard ist DEFLATE):
   ```python
   with zipfile.ZipFile('archive.zip', 'w', zipfile.ZIP_DEFLATED) as zip_ref:
       zip_ref.write('large_file.txt')
   ```
   Optionen: `ZIP_STORED` (keine Komprimierung), `ZIP_DEFLATED`, `ZIP_BZIP2`, etc.

4. **An vorhandene ZIP-Datei anhängen** (verwenden Sie Modus 'a' anstelle von 'w').

### Häufige Operationen und Tipps

- **Prüfen, ob eine Datei eine gültige ZIP-Datei ist**: Verwenden Sie `zipfile.is_zipfile('datei.zip')`.
- **Dateiinformationen abrufen**: `zip_ref.getinfo('datei.txt')` gibt ein ZipInfo-Objekt mit Details wie Größe, Datum zurück.
- **Umgang mit großen Dateien**: Das Lesen/Extrahieren großer Dateien kann viel Speicher verbrauchen; verwenden Sie die `open()`-Methode für Streaming.
- **Fehlerbehandlung**: Fangen Sie `BadZipFile`- oder `LargeZipFile`-Exceptions ab.
- **Plattformübergreifend**: Funktioniert unter Windows, macOS, Linux, aber achten Sie auf Pfadtrennzeichen (verwenden Sie `/`).
- **Verschlüsselung**: Grundlegender Passwortschutz wird unterstützt, ist aber schwach – verwenden Sie für Sicherheit stärkere Tools.
- **Höhere Ebene**: Für mehr Funktionen (z.B. shutil-Integration) kombinieren Sie mit `shutil.make_archive()` zum Erstellen von ZIPs.

Beispielskript zum Zippen eines Ordners:
```python
import zipfile
import os

def zip_folder(source_dir, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                zipf.write(os.path.join(root, file),
                           os.path.relpath(os.path.join(root, file), os.path.join(source_dir, '..')))

zip_folder('my_folder', 'output.zip')
```

Die vollständige Dokumentation finden Sie in den [offiziellen Python-Docs](https://docs.python.org/3/library/zipfile.html). Wenn Sie eine bestimmte Aufgabe haben (z.B. "wie man in den Speicher extrahiert"), geben Sie mehr Details an!