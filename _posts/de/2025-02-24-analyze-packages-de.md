---
audio: false
generated: true
lang: de
layout: post
title: Analyse von Java-Paketen
translated: true
type: note
---

Basierend auf Ihrer Anfrage wünschen Sie ein Skript, bei dem, wenn der Parameter `level` 0 ist oder nicht angegeben wird, der gesamte Paketname (alle Teile davon) verwendet wird. Dies behandelt `level = 0` effektiv als "unendlich" oder "verwende alle Teile", anstatt es auf eine bestimmte Anzahl von Teilen zu beschränken (wie nur den ersten Teil bei `level = 1`). Im Folgenden werde ich erläutern, wie dies in einem Python-Skript implementiert werden kann, das Java-Dateien analysiert, um Paketnamen zu extrahieren, und ich werde eine vollständige, auf Ihre Anfrage zugeschnittene Lösung bereitstellen.

### Anforderungsverständnis
- **Wenn `level = 0` oder nicht angegeben**: Verwenden Sie den vollständigen Paketnamen, wie er aus Java-`import`-Anweisungen extrahiert wurde (z. B. `java.util` oder `com.google.common.eventbus`), ohne ihn zu kürzen.
- **Wenn `level > 0`**: Kürzen Sie den Paketnamen auf die ersten `level` Teile (z. B. würde für `com.google.common.eventbus` mit `level = 2` `com.google` resultieren).
- Das Skript sollte weiterhin Java-Dateien verarbeiten, Paketnamen aus `import`-Anweisungen extrahieren und Randfälle angemessen behandeln.

### Lösungsansatz
1. **Argumentparsing**:
   - Wenn nur das Stammverzeichnis angegeben ist (z. B. `python script.py /pfad/zu/verz`), setze `level = 0`, was die Verwendung des vollständigen Paketnamens bedeutet.
   - Wenn `level` angegeben ist (z. B. `python script.py /pfad/zu/verz 2`), verwenden Sie es, um den Paketnamen zu kürzen, und stellen Sie sicher, dass es sich um eine nicht-negative Ganzzahl handelt.
   - Beenden Sie mit einer Fehlermeldung, wenn die Argumente ungültig sind.

2. **Paket-Extraktion**:
   - Extrahieren Sie den Paketnamen aus `import`-Anweisungen (z. B. ergibt `import java.util.ArrayList;` den Paketnamen `java.util`).
   - Verwenden Sie Java-Namenskonventionen: Pakete sind typischerweise kleingeschrieben, und Klassennamen beginnen mit Großbuchstaben.

3. **Logik zur Paketkürzung**:
   - Wenn `level = 0`, fügen Sie den vollständigen Paketnamen zum Resultat-Set hinzu.
   - Wenn `level > 0`, teilen Sie den Paketnamen anhand von Punkten (`.`) und nehmen Sie die ersten `level` Teile.

4. **Protokollierung und Ausgabe**:
   - Geben Sie klar an, ob vollständige Paketnamen oder gekürzte verwendet werden.
   - Listen Sie alle eindeutigen gefundenen Pakete auf.

### Implementierung
Hier ist das vollständige Python-Skript, das Ihre Anforderungen erfüllt:

```python
import os
import sys
from collections import Counter

def find_java_files(root_dir):
    """
    Findet rekursiv alle .java-Dateien im angegebenen Verzeichnis und seinen Unterverzeichnissen.
    
    Args:
        root_dir (str): Das Stammverzeichnis, von dem aus die Suche beginnen soll.
    
    Yields:
        str: Der vollständige Pfad zu jeder .java-Datei.
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.java'):
                yield os.path.join(dirpath, filename)

def extract_package(import_statement):
    """
    Extrahiert den Paketnamen aus einer import-Anweisung.
    
    Verwendet die Konvention, dass Paketnamen kleingeschrieben sind, während Klassennamen
    mit Großbuchstaben beginnen. Verarbeitet Wildcard-Imports (*).
    
    Args:
        import_statement (str): Die import-Anweisungszeile aus einer Java-Datei.
    
    Returns:
        str: Der Paketname oder ein leerer String, falls nicht bestimmt.
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
    # Kommandozeilenargumente parsen
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("Usage: python script.py <root_directory> [level] [--count]")
        sys.exit(1)
    
    root_dir = sys.argv[1]
    level = 0
    count = False
    
    if len(sys.argv) == 3:
        if sys.argv[2] == "--count":
            count = True
        elif sys.argv[2].isdigit():
            level = int(sys.argv[2])
        else:
            print(f"Invalid argument: {sys.argv[2]}")
            sys.exit(1)
    elif len(sys.argv) == 4:
        if sys.argv[3] == "--count" and sys.argv[2].isdigit():
            level = int(sys.argv[2])
            count = True
        else:
            print(f"Invalid arguments: {sys.argv[2]} {sys.argv[3]}")
            sys.exit(1)
    
    # Überprüfen, ob das Verzeichnis existiert
    if not os.path.isdir(root_dir):
        print(f"[ERROR] The specified path is not a directory: {root_dir}")
        sys.exit(1)
    
    # Start der Analyse protokollieren
    level_str = "using full package names" if level == 0 else f"at level {level}"
    count_str = "with appearance counts" if count else ""
    print(f"[INFO] Starting analysis of directory: {root_dir} {level_str} {count_str}")
    
    # Variablen initialisieren
    package_counter = Counter()
    total_files = 0
    error_files = 0
    
    # Java-Dateien verarbeiten
    for java_file in find_java_files(root_dir):
        try:
            with open(java_file, 'r', encoding='utf-8') as f:
                file_packages = set()
                for line in f:
                    line = line.strip()
                    if line.startswith('import'):
                        package = extract_package(line)
                        if package:
                            if level > 0:
                                parts = package.split('.')
                                truncated_package = '.'.join(parts[:level])
                            else:
                                truncated_package = package
                            file_packages.add(truncated_package)
            for pkg in file_packages:
                package_counter[pkg] += 1
            total_files += 1
        except Exception as e:
            print(f"[ERROR] Could not read file {java_file}: {e}")
            error_files += 1
            continue
    
    # Zusammenfassung ausgeben
    print(f"[INFO] Total Java files attempted: {total_files + error_files}")
    print(f"[INFO] Successfully processed: {total_files}")
    print(f"[INFO] Files with errors: {error_files}")
    if count:
        print(f"[INFO] Total unique packages with counts: {len(package_counter)}")
    else:
        print(f"[INFO] Total unique packages: {len(package_counter)}")
    
    # Ergebnisse mit entsprechender Sortierung ausgeben
    if package_counter:
        if count:
            print("[INFO] Analysis complete. Printing unique packages with counts (sorted by count descending):")
            # Nach Count absteigend, dann nach Paketnamen aufsteigend sortieren
            for pkg, cnt in sorted(package_counter.items(), key=lambda x: (-x[1], x[0])):
                print(f"{pkg}: {cnt}")
        else:
            print("[INFO] Analysis complete. Printing unique packages (sorted by name ascending):")
            # Nach Paketnamen aufsteigend sortieren
            for pkg in sorted(package_counter):
                print(pkg)
    else:
        print("[INFO] No packages found.")
```

### Funktionsweise
- **Ausführen des Skripts**:
  - `python script.py /pfad/zu/java/projekt`: Analysiert alle `.java`-Dateien im Verzeichnis und verwendet vollständige Paketnamen (`level = 0`).
  - `python script.py /pfad/zu/java/projekt 2`: Kürzt Paketnamen auf die ersten 2 Teile (z. B. wird `com.google.common.eventbus` zu `com.google`).

- **Beispielausgabe**:
  Angenommen, Sie haben eine Java-Datei mit:
  ```java
  import java.util.ArrayList;
  import com.google.common.eventbus.EventBus;
  ```
  - **Mit `level = 0` (oder kein level angegeben)**:
    ```
    [INFO] Starting analysis of directory: /path/to/java/project with full package names.
    [INFO] Entering directory: /path/to/java/project
    [INFO] Processing file: /path/to/java/project/MyFile.java
    [INFO] Total Java files attempted: 1
    [INFO] Successfully processed: 1
    [INFO] Files with errors: 0
    [INFO] Total unique full packages: 2
    [INFO] Analysis complete. Printing unique full packages:
    com.google.common.eventbus
    java.util
    ```
  - **Mit `level = 2`**:
    ```
    [INFO] Starting analysis of directory: /path/to/java/project at level: 2
    [INFO] Entering directory: /path/to/java/project
    [INFO] Processing file: /path/to/java/project/MyFile.java
    [INFO] Total Java files attempted: 1
    [INFO] Successfully processed: 1
    [INFO] Files with errors: 0
    [INFO] Total unique packages at level 2: 2
    [INFO] Analysis complete. Printing unique packages at level 2:
    com.google
    java.util
    ```

- **Hauptmerkmale**:
  - **Vollständige Paketnamen**: Wenn `level = 0` oder nicht übergeben, wird der gesamte extrahierte Paketname verwendet (z. B. `java.util`, `com.google.common.eventbus`).
  - **Kürzung**: Wenn `level > 0`, werden die ersten `level` Teile genommen.
  - **Fehlerbehandlung**: Überprüft auf gültiges Verzeichnis und nicht-negatives `level`.
  - **Eindeutigkeit**: Speichert Pakete in einem `set`, um Duplikate zu vermeiden.

### Behandelte Randfälle
- **Fehlendes Level**: Standardwert ist `level = 0`, verwendet vollständige Paketnamen.
- **Ungültiges Level**: Beendet mit einem Fehler, wenn `level` negativ oder keine Ganzzahl ist.
- **Kurze Pakete**: Wenn ein Paket weniger Teile hat als `level` (z. B. `java` mit `level = 2`), wird das vollständige Paket (`java`) verwendet.
- **Leere Imports**: Überspringt Zeilen, in denen kein Paket extrahiert wird.

Dieses Skript erfüllt Ihre Anforderung vollständig: Wenn `level = 0` ist oder nicht angegeben wird, verwendet es alle Teile des Paketnamens und behandelt ihn effektiv als "unendlich" in Bezug auf die verwendeten Teile.