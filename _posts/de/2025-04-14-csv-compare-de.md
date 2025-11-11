---
audio: false
generated: true
lang: de
layout: post
title: Vergleichen zweier einzeiliger CSV-Dateien
translated: true
type: note
---

Hier folgt ein Python-Skript, das zwei einzeilige CSV-Dateien, die Zeichenketten enthalten (z.B. "P0001"), vergleicht und identifiziert:
- Gemeinsame Elemente (in beiden Dateien vorhanden)
- Elemente, die nur in der ersten Datei vorkommen
- Elemente, die nur in der zweiten Datei vorkommen

Das Skript verwendet `argparse`, um zwei CSV-Dateipfade zu akzeptieren, liest die erste Zeile aus jeder Datei, führt einen mengenbasierten Vergleich durch und schreibt die Ergebnisse in `comparison.txt`.

```python
#!/usr/bin/env python3
import argparse
import csv
import os

def main():
    # Argumentparser einrichten
    parser = argparse.ArgumentParser(description='Compare two single-row CSV files for common and unique items')
    parser.add_argument('file1_path', help='Path to the first CSV file')
    parser.add_argument('file2_path', help='Path to the second CSV file')
    
    # Argumente parsen
    args = parser.parse_args()
    
    try:
        # Erste Zeile der ersten CSV-Datei lesen
        with open(args.file1_path, 'r') as file1:
            reader1 = csv.reader(file1)
            for row in reader1:
                values1 = row
                break
        
        # Erste Zeile der zweiten CSV-Datei lesen
        with open(args.file2_path, 'r') as file2:
            reader2 = csv.reader(file2)
            for row in reader2:
                values2 = row
                break
        
        # In Sets für Vergleich konvertieren
        set1 = set(values1)
        set2 = set(values2)
        
        # Gemeinsame und eindeutige Elemente finden
        common_items = set1.intersection(set2)
        unique_to_file1 = set1.difference(set2)
        unique_to_file2 = set2.difference(set1)
        
        # Ausgabeverzeichnis bestimmen (Verzeichnis der ersten Datei verwenden)
        output_dir = os.path.dirname(args.file1_path) or '.'
        output_file = os.path.join(output_dir, 'comparison.txt')
        
        # Ergebnisse in Ausgabedatei schreiben
        with open(output_file, 'w') as file:
            file.write("Comparison Results:\n\n")
            
            file.write("Common Items (in both files):\n")
            if common_items:
                for item in sorted(common_items):
                    file.write(f"{item}\n")
            else:
                file.write("None\n")
                
            file.write("\nItems only in first file:\n")
            if unique_to_file1:
                for item in sorted(unique_to_file1):
                    file.write(f"{item}\n")
            else:
                file.write("None\n")
                
            file.write("\nItems only in second file:\n")
            if unique_to_file2:
                for item in sorted(unique_to_file2):
                    file.write(f"{item}\n")
            else:
                file.write("None\n")
        
        print(f"Comparison complete. Results saved to {output_file}")
        
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

### Funktionsweise:
1. **Eingabe**: Akzeptiert zwei CSV-Dateipfade über Kommandozeilenargumente.
2. **Lesen**: Liest nur die erste Zeile aus jeder CSV-Datei.
3. **Vergleich**:
   - Konvertiert die Zeilen in Sets für effizienten Vergleich.
   - Findet:
     - **Gemeinsame Elemente**: Elemente, die in beiden Zeilen vorhanden sind (Schnittmenge).
     - **Eindeutig für erste Datei**: Elemente nur in der ersten Zeile (Differenzmenge: Datei1 - Datei2).
     - **Eindeutig für zweite Datei**: Elemente nur in der zweiten Zeile (Differenzmenge: Datei2 - Datei1).
4. **Ausgabe**: Schreibt Ergebnisse in `comparison.txt` im Verzeichnis der ersten Datei, listet auf:
   - Gemeinsame Elemente
   - Elemente nur in der ersten Datei
   - Elemente nur in der zweiten Datei
   - Jeder Abschnitt ist alphabetisch sortiert; "None" wird geschrieben, wenn ein Abschnitt leer ist.
5. **Fehlerbehandlung**: Fängt Datei-nicht-gefunden-Fehler und andere Ausnahmen ab.

### Beispielverwendung:
Speichern Sie das Skript als `compare_csv.py`. Erstellen Sie zwei CSV-Dateien, z.B.:
- `file1.csv`: `P0001,P0002,P0003`
- `file2.csv`: `P0001,P0004,P0003`

Führen Sie das Skript aus:
```
python compare_csv.py file1.csv file2.csv
```

**Ausgabe** (`comparison.txt`):
```
Comparison Results:

Common Items (in both files):
P0001
P0003

Items only in first file:
P0002

Items only in second file:
P0004
```

### Hinweise:
- Das Skript ignoriert die Position der Elemente und konzentriert sich nur auf Präsenz/Abwesenheit.
- Doppelte Elemente in einer Zeile werden automatisch behandelt (Sets entfernen Duplikate).
- Die Ausgabe wird in `comparison.txt` im Verzeichnis der ersten Eingabedatei geschrieben.
- Wenn eine Datei leer ist oder keine Zeile hat, behandelt das Skript sie als leere Menge.

Möchten Sie, dass ich das Skript ändere (z.B. das Ausgabeformat ändere oder mehr Details hinzufüge)?