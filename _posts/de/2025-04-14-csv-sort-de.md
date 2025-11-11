---
audio: false
generated: true
lang: de
layout: post
title: CSV-Sortierskript
translated: true
type: note
---

Ich werde ein Python-Skript erstellen, das argparse verwendet, um einen CSV-Dateipfad zu parsen, eine einzelne Zeile mit kommagetrennten Werten alphabetisch sortiert und das Ergebnis in einer Datei namens "name_sorted.csv" ausgibt.

```python
#!/usr/bin/env python3
import argparse
import csv
import os

def main():
    # Argumentparser einrichten
    parser = argparse.ArgumentParser(description='Sortiere eine einzeilige CSV-Datei alphabetisch')
    parser.add_argument('file_path', help='Pfad zur Eingabe-CSV-Datei')
    
    # Argumente parsen
    args = parser.parse_args()
    
    try:
        # Verzeichnis und Dateinamen ermitteln
        file_dir = os.path.dirname(args.file_path)
        file_name = os.path.basename(args.file_path)
        
        # Ausgabedateinamen erstellen
        base_name, ext = os.path.splitext(file_name)
        output_file = os.path.join(file_dir, f"{base_name}_sorted{ext}")
        
        # Die Eingabe-CSV-Datei lesen
        with open(args.file_path, 'r') as file:
            reader = csv.reader(file)
            # Nur die erste Zeile lesen
            for row in reader:
                values = row
                break
        
        # Werte alphabetisch sortieren
        sorted_values = sorted(values)
        
        # In Ausgabedatei schreiben
        with open(output_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(sorted_values)
        
        print(f"Werte erfolgreich sortiert und gespeichert in {output_file}")
        
    except FileNotFoundError:
        print(f"Fehler: Datei '{args.file_path}' nicht gefunden")
    except Exception as e:
        print(f"Fehler: {e}")

if __name__ == "__main__":
    main()
```

Dieses Skript:
1. Verwendet argparse, um den Eingabedateipfad zu erhalten
2. Öffnet die CSV-Datei und liest nur die erste Zeile
3. Sortiert die Werte alphabetisch
4. Schreibt die sortierten Werte in "name_sorted.csv"

Um das Skript auszuführen, speichern Sie es in einer Datei (z.B. "sort_csv.py"), machen Sie es bei Bedarf ausführbar und führen Sie es mit dem Pfad zu Ihrer CSV-Datei aus:

```
python sort_csv.py pfad/zu/ihrer/datei.csv
```

Möchten Sie, dass ich einen bestimmten Teil des Codes genauer erkläre?