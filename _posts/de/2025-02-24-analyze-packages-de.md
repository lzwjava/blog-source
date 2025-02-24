---
audio: false
lang: de
layout: post
title: Analyse von Java-Paketen in einem Projekt
translated: true
---

Basierend auf Ihrer Anfrage möchten Sie ein Skript, bei dem, wenn der `level`-Parameter 0 ist oder nicht angegeben wird, der gesamte Paketname (alle Teile davon) verwendet wird, was `level = 0` als "unendlich" oder "verwende alle Teile" behandelt, anstatt es auf eine bestimmte Anzahl von Teilen zu beschränken (wie nur den ersten Teil bei `level = 1`). Unten werde ich erklären, wie dies in einem Python-Skript implementiert werden kann, das Java-Dateien analysiert, um Paketnamen zu extrahieren, und ich werde eine vollständige Lösung bereitstellen, die auf Ihre Anfrage zugeschnitten ist.

### Verständnis der Anforderung
- **Wenn `level = 0` oder nicht angegeben**: Verwenden Sie den vollständigen Paketnamen, wie er aus Java-`import`-Anweisungen extrahiert wird (z. B. `java.util` oder `com.google.common.eventbus`), ohne ihn zu kürzen.
- **Wenn `level > 0`**: Kürzen Sie den Paketnamen auf die ersten `level`-Teile (z. B. für `com.google.common.eventbus`, `level = 2` würde `com.google` ergeben).
- Das Skript sollte weiterhin Java-Dateien verarbeiten, Paketnamen aus `import`-Anweisungen extrahieren und Randfälle angemessen behandeln.

### Lösungansatz
1. **Argumentparsing**:
   - Wenn nur das Stammverzeichnis angegeben ist (z. B. `python script.py /pfad/zum/verzeichnis`), setzen Sie `level = 0`, was bedeutet, dass der vollständige Paketname verwendet wird.
   - Wenn `level` angegeben ist (z. B. `python script.py /pfad/zum/verzeichnis 2`), verwenden Sie es, um den Paketnamen zu kürzen, und stellen Sie sicher, dass es eine nicht-negative ganze Zahl ist.
   - Beenden Sie mit einem Fehler, wenn die Argumente ungültig sind.

2. **Paketextraktion**:
   - Extrahieren Sie den Paketnamen aus `import`-Anweisungen (z. B. `import java.util.ArrayList;` ergibt `java.util`).
   - Verwenden Sie Java-Benennungskonventionen: Pakete sind in der Regel Kleinbuchstaben, und Klassenamen beginnen mit Großbuchstaben.

3. **Logik zur Paketkürzung**:
   - Wenn `level = 0`, fügen Sie den vollständigen Paketnamen der Ergebnismenge hinzu.
   - Wenn `level > 0`, teilen Sie den Paketnamen durch Punkte (`.`) und nehmen Sie die ersten `level`-Teile.

4. **Protokollierung und Ausgabe**:
   - Geben Sie klar an, ob vollständige Paketnamen oder gekürzte verwendet werden.
   - Listen Sie alle eindeutigen Pakete auf, die gefunden wurden.

### Implementierung
Hier ist das vollständige Python-Skript, das Ihren Anforderungen entspricht:

```python
import os
import sys

def find_java_files(root_dir):
    """
    Durchsucht rekursiv alle .java-Dateien im angegebenen Verzeichnis und seinen Unterverzeichnissen.

    Args:
        root_dir (str): Das Stammverzeichnis, von dem die Suche beginnen soll.

    Yields:
        str: Der vollständige Pfad zu jeder .java-Datei.
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        print(f"[INFO] Betreten des Verzeichnisses: {dirpath}")
        for filename in filenames:
            if filename.endswith('.java'):
                yield os.path.join(dirpath, filename)

def extract_package(import_statement):
    """
    Extrahiert den Paketnamen aus einer import-Anweisung.

    Geht davon aus, dass Paketnamen Kleinbuchstaben sind und bei Klassenamen (Großbuchstaben) oder Wildcards (*) aufhören.

    Args:
        import_statement (str): Die import-Anweisungszeile aus einer Java-Datei.

    Returns:
        str: Der Paketname oder eine leere Zeichenkette, wenn nicht bestimmt.
    """
    parts = import_statement.split()
    if parts[0] == 'import':
        parts = parts[1:]
    if parts[0] == 'static':
        parts = parts[1:]
    import_path = ' '.join(parts).strip(';').strip()
    identifiers = import_path.split('.')
    for i, ident in enumerate(identifiers):
        if ident == '*' or (ident and ident[0].isupper()):
            package_parts = identifiers[:i]
            break
    else:
        package_parts = []
    package = '.'.join(package_parts)
    return package

if __name__ == '__main__':
    # Parsen der Befehlszeilenargumente
    if len(sys.argv) == 2:
        root_dir = sys.argv[1]
        level = 0  # Kein Level angegeben, vollständige Paketnamen verwenden
    elif len(sys.argv) == 3:
        root_dir = sys.argv[1]
        try:
            level = int(sys.argv[2])
            if level < 0:
                raise ValueError
        except ValueError:
            print("[FEHLER] Level muss eine nicht-negative ganze Zahl sein.")
            sys.exit(1)
    else:
        print("Verwendung: python script.py <Stammverzeichnis> [level]")
        sys.exit(1)

    # Überprüfen, ob das Verzeichnis existiert
    if not os.path.isdir(root_dir):
        print(f"[FEHLER] Der angegebene Pfad ist kein Verzeichnis: {root_dir}")
        sys.exit(1)

    # Protokollieren des Beginns der Analyse
    if level == 0:
        print(f"[INFO] Beginn der Analyse des Verzeichnisses: {root_dir} mit vollständigen Paketnamen.")
    else:
        print(f"[INFO] Beginn der Analyse des Verzeichnisses: {root_dir} auf Ebene: {level}")

    # Initialisieren von Variablen
    packages = set()
    total_files = 0
    error_files = 0

    # Verarbeiten der Java-Dateien
    for java_file in find_java_files(root_dir):
        print(f"[INFO] Verarbeiten der Datei: {java_file}")
        try:
            with open(java_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('import'):
                        package = extract_package(line)
                        if package:
                            if level == 0:
                                # Verwenden des vollständigen Paketnamens
                                packages.add(package)
                            else:
                                # Kürzen auf die ersten 'level'-Teile
                                parts = package.split('.')
                                truncated_package = '.'.join(parts[:level])
                                packages.add(truncated_package)
            total_files += 1
        except Exception as e:
            print(f"[FEHLER] Datei {java_file} konnte nicht gelesen werden: {e}")
            error_files += 1
            continue

    # Drucken der Zusammenfassung
    print(f"[INFO] Gesamtzahl der versuchten Java-Dateien: {total_files + error_files}")
    print(f"[INFO] Erfolgreich verarbeitet: {total_files}")
    print(f"[INFO] Dateien mit Fehlern: {error_files}")
    if level == 0:
        print(f"[INFO] Gesamtzahl der eindeutigen vollständigen Pakete: {len(packages)}")
    else:
        print(f"[INFO] Gesamtzahl der eindeutigen Pakete auf Ebene {level}: {len(packages)}")

    # Drucken der Ergebnisse
    if packages:
        if level == 0:
            print("[INFO] Analyse abgeschlossen. Drucken der eindeutigen vollständigen Pakete:")
        else:
            print(f"[INFO] Analyse abgeschlossen. Drucken der eindeutigen Pakete auf Ebene {level}:")
        for package in sorted(packages):
            print(package)
    else:
        print("[INFO] Keine Pakete gefunden.")
```

### Funktionsweise
- **Ausführen des Skripts**:
  - `python script.py /pfad/zum/java/projekt`: Analysiert alle `.java`-Dateien im Verzeichnis und verwendet vollständige Paketnamen (`level = 0`).
  - `python script.py /pfad/zum/java/projekt 2`: Kürzt Paketnamen auf die ersten 2 Teile (z. B. `com.google.common.eventbus` wird zu `com.google`).

- **Beispielausgabe**:
  Angenommen, Sie haben eine Java-Datei mit:
  ```java
  import java.util.ArrayList;
  import com.google.common.eventbus.EventBus;
  ```
  - **Mit `level = 0` (oder kein Level angegeben)**:
    ```
    [INFO] Beginn der Analyse des Verzeichnisses: /pfad/zum/java/projekt mit vollständigen Paketnamen.
    [INFO] Betreten des Verzeichnisses: /pfad/zum/java/projekt
    [INFO] Verarbeiten der Datei: /pfad/zum/java/projekt/MyFile.java
    [INFO] Gesamtzahl der versuchten Java-Dateien: 1
    [INFO] Erfolgreich verarbeitet: 1
    [INFO] Dateien mit Fehlern: 0
    [INFO] Gesamtzahl der eindeutigen vollständigen Pakete: 2
    [INFO] Analyse abgeschlossen. Drucken der eindeutigen vollständigen Pakete:
    com.google.common.eventbus
    java.util
    ```
  - **Mit `level = 2`**:
    ```
    [INFO] Beginn der Analyse des Verzeichnisses: /pfad/zum/java/projekt auf Ebene: 2
    [INFO] Betreten des Verzeichnisses: /pfad/zum/java/projekt
    [INFO] Verarbeiten der Datei: /pfad/zum/java/projekt/MyFile.java
    [INFO] Gesamtzahl der versuchten Java-Dateien: 1
    [INFO] Erfolgreich verarbeitet: 1
    [INFO] Dateien mit Fehlern: 0
    [INFO] Gesamtzahl der eindeutigen Pakete auf Ebene 2: 2
    [INFO] Analyse abgeschlossen. Drucken der eindeutigen Pakete auf Ebene 2:
    com.google
    java.util
    ```

- **Wichtige Merkmale**:
  - **Vollständige Paketnamen**: Wenn `level = 0` oder nicht angegeben, wird der gesamte Paketname verwendet, wie er extrahiert wurde (z. B. `java.util`, `com.google.common.eventbus`).
  - **Kürzung**: Wenn `level > 0`, wird der erste `level`-Teil verwendet.
  - **Fehlerbehandlung**: Überprüft auf gültiges Verzeichnis und nicht-negative `level`.
  - **Einzigartigkeit**: Speichert Pakete in einem `set`, um Duplikate zu vermeiden.

### Randfälle, die behandelt werden
- **Fehlendes Level**: Standardmäßig `level = 0`, vollständige Paketnamen verwenden.
- **Ungültiges Level**: Beendet mit einem Fehler, wenn `level` negativ oder keine ganze Zahl ist.
- **Kurze Pakete**: Wenn ein Paket weniger Teile hat als `level` (z. B. `java` mit `level = 2`), wird das vollständige Paket (`java`) verwendet.
- **Leere Imports**: Überspringt Zeilen, bei denen kein Paket extrahiert wird.

Dieses Skript erfüllt vollständig Ihre Anforderung: Wenn `level = 0` oder nicht angegeben, verwendet es alle Teile des Paketnamens, was es effektiv als "unendlich" in Bezug auf die verwendeten Teile behandelt.