---
audio: false
lang: de
layout: post
title: Analyse von Java-Paketen in einem Projekt
translated: true
---

Hier ist ein Python-Skript, das ein Verzeichnis rekursiv analysiert, alle in `.java`-Dateien verwendeten Java-Pakete findet, Duplikate entfernt und alle eindeutigen Pakete auflistet, die im Projekt verwendet werden. Das Skript konzentriert sich ausschließlich auf `.java`-Dateien und behandelt Projekte, die möglicherweise Module haben, indem es alle Unterverzeichnisse durchläuft.

### Python-Skript:

```python
import os
import sys

def find_java_files(root_dir):
    """
    Findet rekursiv alle .java-Dateien im angegebenen Verzeichnis und dessen Unterverzeichnissen.

    Args:
        root_dir (str): Das Stammverzeichnis, von dem die Suche beginnen soll.

    Yields:
        str: Der vollständige Pfad zu jeder .java-Datei.
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.java'):
                yield os.path.join(dirpath, filename)

def extract_package(import_statement):
    """
    Extrahiert den Paketnamen aus einer Import-Anweisung.

    Verwendet die Konvention, dass Paketnamen typischerweise Kleinbuchstaben sind, während Klassennamen mit Großbuchstaben beginnen. Bei Wildcard-Imports (*) ist das Paket der Teil vor '*'.

    Args:
        import_statement (str): Die Import-Anweisungszeile aus einer Java-Datei.

    Returns:
        str: Der Paketname oder eine leere Zeichenkette, wenn nicht bestimmt.
    """
    # Entferne 'import' und 'static', falls vorhanden
    parts = import_statement.split()
    if parts[0] == 'import':
        parts = parts[1:]
    if parts[0] == 'static':
        parts = parts[1:]

    # Verbinde die verbleibenden Teile und entferne das abschließende ';'
    import_path = ' '.join(parts).strip(';').strip()

    # Teile den Importpfad durch '.'
    identifiers = import_path.split('.')

    # Finde den Index, an dem der erste Bezeichner mit Großbuchstaben beginnt oder '*' ist
    for i, ident in enumerate(identifiers):
        if ident == '*' or (ident and ident[0].isupper()):
            package_parts = identifiers[:i]
            break
    else:
        package_parts = []

    package = '.'.join(package_parts)
    return package

if __name__ == '__main__':
    # Überprüfe das Kommandozeilenargument für das Stammverzeichnis
    if len(sys.argv) < 2:
        print("Verwendung: python script.py <root_directory>")
        sys.exit(1)

    root_dir = sys.argv[1]
    packages = set()

    # Durchsuche alle .java-Dateien im Verzeichnis und Unterverzeichnissen
    for java_file in find_java_files(root_dir):
        try:
            with open(java_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('import'):
                        package = extract_package(line)
                        if package:  # Nur nicht-leere Paketnamen hinzufügen
                            packages.add(package)
        except Exception as e:
            print(f"Warnung: Datei {java_file} konnte nicht gelesen werden: {e}")
            continue

    # Gib die sortierte Liste der eindeutigen Pakete aus
    for package in sorted(packages):
        print(package)
```

### So verwenden Sie das Skript:

1. Speichern Sie das Skript in einer Datei, z.B. `analyze_java_packages.py`.
2. Führen Sie das Skript von der Kommandozeile aus, indem Sie den Pfad zum Stammverzeichnis des Java-Projekts angeben:
   ```
   python analyze_java_packages.py /pfad/zu/ihrem/java/projekt
   ```
3. Das Skript gibt eine sortierte Liste der eindeutigen Paketnamen aus, die in den `.java`-Dateien importiert werden.

### Was das Skript macht:

- **Findet `.java`-Dateien:**
  - Verwendet `os.walk()`, um das Verzeichnis und dessen Unterverzeichnisse rekursiv zu durchsuchen.
  - Identifiziert alle Dateien, die mit `.java` enden.

- **Extrahiert Paketnamen:**
  - Analysiert jede `.java`-Datei Zeile für Zeile.
  - Identifiziert Zeilen, die mit `import` beginnen.
  - Extrahiert Paketnamen aus Import-Anweisungen, einschließlich:
    - Reguläre Importe (z.B. `import java.util.List;`)
    - Wildcard-Importe (z.B. `import java.util.*;`)
    - Statische Importe (z.B. `import static java.util.Collections.sort;`)
  - Verwendet eine Heuristik basierend auf Java-Benennungskonventionen:
    - Paketnamen sind typischerweise Kleinbuchstaben (z.B. `java.util`).
    - Klassennamen beginnen typischerweise mit Großbuchstaben (z.B. `List`, `Collections`).
    - Wildcard-Importe enden mit `*`.

- **Entfernt Duplikate:**
  - Sammelt alle Paketnamen in einem `set`, um Duplikate automatisch zu entfernen.

- **Gibt Ergebnisse aus:**
  - Konvertiert das Set in eine sortierte Liste und gibt jeden Paketnamen in einer neuen Zeile aus.

### Annahmen und Einschränkungen:

- **Import-Anweisungen:**
  - Geht davon aus, dass Import-Anweisungen auf eigenen Zeilen stehen und nicht in Kommentaren oder Zeichenketten eingebettet sind.
  - Behandelt sowohl reguläre als auch statische Importe, einschließlich Wildcard-Importen.

- **Benennungskonventionen:**
  - Stützt sich auf die Konvention, dass Paketnamen Kleinbuchstaben sind und Klassennamen mit Großbuchstaben beginnen.
  - Kann möglicherweise nicht korrekt mit nicht-standardmäßigen Benennungen umgehen (z.B. Paketnamen in Großbuchstaben), dies ist jedoch in der Praxis selten.

- **Dateikodierung:**
  - Geht davon aus, dass `.java`-Dateien in UTF-8 kodiert sind. Passen Sie den `encoding`-Parameter bei Bedarf an.

- **Fehlerbehandlung:**
  - Enthält grundlegende Fehlerbehandlung für nicht lesbare Dateien, gibt eine Warnung aus und setzt fort.

### Beispiel:

Wenn Ihr Java-Projekt die folgenden `.java`-Dateien hat:

- **File1.java:**
  ```java
  import java.util.List;
  import java.util.*;
  import java.lang.String;
  ```

- **File2.java:**
  ```java
  import java.util.Collections;
  import static java.util.Collections.sort;
  import com.example.myapp.*;
  ```

Führen Sie das Skript aus, um Folgendes auszugeben:
```
com.example.myapp
java.lang
java.util
```

Dies listet alle eindeutigen Pakete auf, die im Projekt importiert werden, alphabetisch sortiert.

### Hinweise:

- Das Skript konzentriert sich auf Pakete, die über `import`-Anweisungen importiert werden, die die externen und internen Pakete darstellen, die das Projekt verwendet.
- Es enthält nicht die Paketdeklarationen der `.java`-Dateien selbst (z.B. `package com.mycompany.myapp;`), da diese die Pakete definieren, zu denen die Dateien gehören, nicht die Pakete, die sie verwenden.
- Da das Projekt möglicherweise Module hat, analysiert das Skript rekursiv alle Unterverzeichnisse, um sicherzustellen, dass alle `.java`-Dateien verarbeitet werden.