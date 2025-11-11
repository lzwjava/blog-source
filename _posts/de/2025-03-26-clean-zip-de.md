---
audio: false
generated: true
lang: de
layout: post
title: Saubere Zip-Datei
translated: true
type: note
---

1. **Liest eine ZIP-Datei** mit `zipfile.ZipFile` und erhält eine Liste aller enthaltenen Dateien.
2. **Filtert Dateien ohne Erweiterungen heraus**, behält jedoch Verzeichnisse (Einträge, die mit `/` enden).
3. **Protokolliert die entfernten Dateien**, um den Benutzer darüber zu informieren, welche ausgeschlossen wurden.
4. **Erstellt eine neue ZIP-Datei** nur mit gültigen Dateien (solchen mit Erweiterungen oder Verzeichnissen).
5. **Verwendet `argparse`**, um einen ZIP-Dateipfad als Kommandozeilenargument zu akzeptieren.

Dies stellt sicher, dass nur ordnungsgemäße Dateien erhalten bleiben, während die Verzeichnisstrukturen beibehalten werden. 🚀

```python
import zipfile
import os
import argparse

def clean_zip(zip_path):
    output_path = os.path.splitext(zip_path)[0] + "_output.zip"
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        file_names = zip_ref.namelist()
        
        # Separate valid files and files without extensions (excluding directories)
        valid_files = [f for f in file_names if os.path.splitext(os.path.basename(f))[1] or f.endswith('/')]
        removed_files = [f for f in file_names if not os.path.splitext(os.path.basename(f))[1] and not f.endswith('/')]
        
        if not valid_files:
            print("No valid files with extensions found. Exiting.")
            return
        
        # Log removed files
        if removed_files:
            print("Removing the following files (no extensions detected):")
            for f in removed_files:
                print(f" - {f}")
        
        # Create a new zip file excluding invalid files
        with zipfile.ZipFile(output_path, 'w') as clean_zip:
            for file in valid_files:
                with zip_ref.open(file) as source:
                    clean_zip.writestr(file, source.read())

    print(f"Cleaned ZIP file created: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean a ZIP file by removing files without extensions.")
    parser.add_argument("zip_path", help="Path to the input ZIP file")
    args = parser.parse_args()
    clean_zip(args.zip_path)

```