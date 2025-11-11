---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Nutzungsanleitung für das Python-Modul tarfile
translated: true
type: note
---

### Importieren des tarfile-Moduls
Um die `tarfile`-Bibliothek in Python zu verwenden, importieren Sie sie zunächst:
```python
import tarfile
```
Dieses Modul ist Teil der Python-Standardbibliothek, daher ist keine Installation erforderlich. Es basiert auf dem POSIX-tar-Format und unterstützt das Lesen von und Schreiben in tar-Archive, komprimiert oder unkomprimiert.

### Öffnen und Erstellen von Tar-Archiven
- **Öffnen einer vorhandenen tar-Datei**: Verwenden Sie `tarfile.open()` mit einem Modus. Modi umfassen `'r'` (Lesen), `'w'` (Leeres Archiv schreiben), `'a'` (Anhängen) oder Varianten mit Komprimierung wie `'r:gz'` für gzip.
  ```python
  import tarfile
  
  # Zum Lesen öffnen (unkomprimiert)
  with tarfile.open('example.tar', 'r') as tar:
      # Hier mit tar arbeiten
      pass
  ```
- **Erstellen einer neuen tar-Datei**: Verwenden Sie den Modus `'w'`, um ein leeres Archiv zu erstellen. Fügen Sie Komprimierungspräfixe wie `'w:gz'` für gzip oder `'w:bz2'` für bzip2 hinzu.
  ```python
  # Eine komprimierte tar.gz-Datei erstellen
  with tarfile.open('archive.tar.gz', 'w:gz') as tar:
      pass
  ```

### Hinzufügen von Dateien zu einem Archiv
- **Eine einzelne Datei hinzufügen**: Rufen Sie `add()` auf dem tar-Dateiobjekt auf und übergeben Sie den Dateipfad. Sie können einen arcname für einen anderen Namen innerhalb des Archivs angeben.
  ```python
  with tarfile.open('archive.tar.gz', 'w:gz') as tar:
      tar.add('file.txt')  # Fügt file.txt unverändert hinzu
      tar.add('data.csv', arcname='renamed_data.csv')  # Innerhalb des Archivs umbenennen
  ```
- **Mehrere Dateien oder ein Verzeichnis hinzufügen**: Verwenden Sie `add()` in einer Schleife oder fügen Sie gesamte Verzeichnisse rekursiv hinzu.
  ```python
  import os
  
  with tarfile.open('backup.tar', 'w') as tar:
      for root, dirs, files in os.walk('my_folder'):
          for file in files:
              tar.add(os.path.join(root, file))
  ```

### Extrahieren von Dateien aus einem Archiv
- **Alle Dateien extrahieren**: Verwenden Sie `extractall()`, um in ein bestimmtes Verzeichnis zu extrahieren (Standard ist das aktuelle Verzeichnis).
  ```python
  with tarfile.open('archive.tar.gz', 'r:gz') as tar:
      tar.extractall(path='extracted_folder')  # Erstellt den Ordner falls nötig
  ```
- **Bestimmte Dateien extrahieren**: Listen Sie zunächst die Member mit `getmembers()` auf und verwenden Sie dann `extract()`.
  ```python
  with tarfile.open('example.tar', 'r') as tar:
      members = tar.getmembers()
      for member in members:
          if 'important' in member.name:  # Beispiel-Filter
              tar.extract(member, path='output_dir')
  ```
- Hinweis: Aus Sicherheitsgründen sollten Sie Pfade filtern (z.B. `..` vermeiden), um Path Traversal-Angriffe zu verhindern. `tarfile` führt einige Prüfungen durch, aber für nicht vertrauenswürdige Archive ist manuelles Filtern ratsam.

### Auflisten der Archivinhalte
- **Über Dateien iterieren**: Verwenden Sie `getmembers()` oder iterieren Sie direkt über das tar-Objekt, um TarInfo-Objekte zu erhalten.
  ```python
  with tarfile.open('example.tar', 'r') as tar:
      for member in tar.getmembers():
          print(f"{member.name}: {member.size} bytes")
  ```

### Wichtige Modi und Komprimierung
- `'r'`: Unkomprimiertes tar lesen.
- `'r:gz'`, `'r:bz2'`, `'r:xz'`: Komprimierte Varianten lesen.
- `'w'`: Neues unkomprimiertes tar schreiben (überschreibt).
- `'a'`: An vorhandenes tar anhängen.
- Komprimierung wird beim Lesen automatisch erkannt; muss beim Schreiben angegeben werden.

### Tipps und Best Practices
- Verwenden Sie immer Kontextmanager (`with`-Anweisungen), um sicherzustellen, dass Dateien ordnungsgemäß geschlossen werden.
- Bei großen Archiven sollten Sie das Filtern oder selektive Extrahieren in Betracht ziehen, um Speicher zu sparen.
- `tarfile` behandelt verschlüsselte Archive nicht direkt – verwenden Sie externe Tools oder kombinieren Sie sie bei Bedarf manuell mit `gzip`.
- Fehlerbehandlung: Fangen Sie `tarfile.TarError` für Archivprobleme ab.
- Vollständige Dokumentation: Konsultieren Sie die offizielle [tarfile-Dokumentation](https://docs.python.org/3/library/tarfile.html) von Python für erweiterte Funktionen wie benutzerdefinierte Filter.