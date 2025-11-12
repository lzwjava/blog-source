---
audio: false
generated: true
lang: de
layout: post
title: Analyse von Java-Abhängigkeiten
translated: true
type: note
---

Um Ihre Anfrage zu beantworten, werde ich das bereitgestellte Python-Skript so ändern, dass es einen Abhängigkeitsgraphen für Java-Klassen erzeugt, wobei die Abhängigkeiten nach einer bestimmten "Ebene" der Pakethierarchie gruppiert werden. Zum Beispiel: Bei `level=1` werden Pakete auf der obersten Ebene gruppiert (z.B. "org"), und bei `level=2` werden sie auf der zweiten Ebene gruppiert (z.B. "org.springframework"). Das bedeutet, dass wir vor der Analyse der Abhängigkeiten Klassen in Gruppen basierend auf den ersten `level` Teilen ihrer Paketnamen zusammenfassen, und der Graph zeigt dann Abhängigkeiten zwischen diesen Gruppen anstelle einzelner Klassen.

Nachfolgend finden Sie das modifizierte Skript, gefolgt von einer Erläuterung der Änderungen und wie es Ihre Anforderungen erfüllt.

### Modifiziertes Skript

```python
import os
import sys
import re
from collections import defaultdict

def get_package(file_path):
    """
    Extrahiert den Paketnamen aus einer .java-Datei.

    Args:
        file_path (str): Pfad zur .java-Datei.

    Returns:
        str: Der Paketname oder None, falls nicht gefunden.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.search(r'^\s*package\s+([\w.]+);', line)
                if match:
                    return match.group(1)
    except Exception as e:
        print(f"Warnung: Konnte {file_path} nicht lesen: {e}")
    return None

def get_specific_imports(file_path):
    """
    Extrahiert spezifische Klassen-Imports aus einer .java-Datei, ausgenommen Wildcard-Imports.

    Args:
        file_path (str): Pfad zur .java-Datei.

    Returns:
        list: Liste der vollständig qualifizierten importierten Klassennamen.
    """
    imports = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.search(r'^\s*import\s+([\w.]+);', line)
                if match:
                    imp = match.group(1)
                    # Schließe Wildcard-Imports aus (z.B. import java.util.*;)
                    if not imp.endswith('.*'):
                        imports.append(imp)
    except Exception as e:
        print(f"Warnung: Konnte {file_path} nicht lesen: {e}")
    return imports

def get_package_group(full_class_name, level):
    """
    Ermittelt die Paketgruppe basierend auf den ersten 'level' Teilen des Paketnamens.

    Args:
        full_class_name (str): Vollständig qualifizierter Klassenname (z.B. "org.springframework.boot.App").
        level (int): Anzahl der einzubeziehenden Paketebenen (z.B. 1 für "org", 2 für "org.springframework").

    Returns:
        str: Die Paketgruppe (z.B. "org" oder "org.springframework").
    """
    package = '.'.join(full_class_name.split('.')[:-1])  # Extrahiere Paket, ausgenommen Klassenname
    parts = package.split('.')
    if len(parts) <= level:
        return package  # Verwende vollständiges Paket, wenn es weniger oder gleich viele Teile wie level hat
    else:
        return '.'.join(parts[:level])  # Verwende die ersten 'level' Teile

if __name__ == '__main__':
    # Prüfe Kommandozeilenargumente: root_directory und level
    if len(sys.argv) != 3:
        print("Verwendung: python script.py <root_directory> <level>")
        sys.exit(1)

    root_dir = sys.argv[1]
    try:
        level = int(sys.argv[2])
        if level < 1:
            raise ValueError
    except ValueError:
        print("Fehler: level muss eine positive Ganzzahl sein")
        sys.exit(1)

    all_classes = set()

    # Erster Durchlauf: Sammle alle vollständig qualifizierten Klassennamen im Projekt
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                package = get_package(file_path)
                if package:
                    class_name = file.replace('.java', '')
                    full_class_name = f"{package}.{class_name}"
                    all_classes.add(full_class_name)

    # Speichere Abhängigkeiten zwischen Paketgruppen
    group_dependencies = set()

    # Zweiter Durchlauf: Analysiere Abhängigkeiten basierend auf Paketgruppen
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                package = get_package(file_path)
                if package:
                    class_name = file.replace('.java', '')
                    full_class_name = f"{package}.{class_name}"
                    importer_group = get_package_group(full_class_name, level)
                    imports = get_specific_imports(file_path)
                    for imp in imports:
                        # Berücksichtige nur Abhängigkeiten von Klassen innerhalb des Projekts
                        # Schließe Selbstabhängigkeiten aus
                        if imp in all_classes and imp != full_class_name:
                            imported_group = get_package_group(imp, level)
                            if imported_group != importer_group:
                                group_dependencies.add((importer_group, imported_group))

    # Gib den Abhängigkeitsgraphen im DOT-Format aus
    print('digraph G {')
    for from_group, to_group in sorted(group_dependencies):
        print(f'  "{from_group}" -> "{to_group}";')
    print('}')
```

### Erklärung der Änderungen

1. **Kommandozeilenargumente**:
   - **Original**: `python script.py <root_directory>`
   - **Modifiziert**: `python script.py <root_directory> <level>`
   - Unterstützung für ein zweites Argument, `level`, wurde hinzugefügt, das die Pakethierarchie-Ebene spezifiziert. Das Skript prüft, dass genau zwei Argumente bereitgestellt werden und dass `level` eine positive Ganzzahl ist.

2. **Neue Funktion: `get_package_group`**:
   - Eine Funktion wurde hinzugefügt, um die Paketgruppe für eine Klasse basierend auf dem angegebenen `level` zu berechnen.
   - Für einen vollständig qualifizierten Klassennamen (z.B. "org.springframework.boot.App") extrahiert sie das Paket ("org.springframework.boot"), teilt es in Teile ("org", "springframework", "boot") und nimmt die ersten `level` Teile:
     - Wenn `level=1`: Gibt "org" zurück.
     - Wenn `level=2`: Gibt "org.springframework" zurück.
     - Wenn das Paket weniger Teile als `level` hat (z.B. "com.example" mit `level=3`), gibt es das vollständige Paket zurück ("com.example").

3. **Abhängigkeitsgruppierung**:
   - **Original**: Verwendete `defaultdict(set)`, um Abhängigkeiten zwischen einzelnen Klassen zu speichern.
   - **Modifiziert**: Verwendet ein `set` (`group_dependencies`), um gerichtete Kanten zwischen Paketgruppen als Tupel `(from_group, to_group)` zu speichern.
   - Für jede Klasse:
     - Berechnet ihre Paketgruppe (`importer_group`) unter Verwendung von `get_package_group`.
     - Für jeden spezifischen Import, der innerhalb des Projekts liegt (`imp in all_classes`) und nicht die Klasse selbst ist (`imp != full_class_name`):
       - Berechnet die Paketgruppe der importierten Klasse (`imported_group`).
       - Wenn sich die Gruppen unterscheiden (`imported_group != importer_group`), wird eine Kante zu `group_dependencies` hinzugefügt.
   - Das `set` stellt Eindeutigkeit sicher, sodass mehrere Abhängigkeiten zwischen denselben Gruppen in einer einzelnen Kante resultieren.

4. **DOT-Ausgabe**:
   - **Original**: Gab Kanten zwischen einzelnen Klassen aus (z.B. "org.springframework.boot.App" -> "org.apache.commons.IOUtils").
   - **Modifiziert**: Gibt Kanten zwischen Paketgruppen aus (z.B. "org.springframework" -> "org.apache" für `level=2`).
   - Kanten werden für eine konsistente Ausgabe sortiert.

### Wie es Ihre Anforderungen erfüllt

- **Unterstützung für Ebenen**: Das Skript akzeptiert nun einen `level`-Parameter, um Pakete vor der Analyse der Abhängigkeiten zu gruppieren.
- **Ebene = 1**: Gruppiert alle Klassen nach ihrem Top-Level-Paket (z.B. "org"). Zum Beispiel gehören "org.springframework.boot.App" und "org.apache.commons.IOUtils" beide zur Gruppe "org", daher werden Imports zwischen ihnen innerhalb von "org" nicht als Kanten angezeigt.
- **Ebene = 2**: Gruppiert Klassen nach den ersten beiden Paketebenen (z.B. "org.springframework"). Zum Beispiel erzeugt ein Import von "org.springframework.boot.App" zu "org.apache.commons.IOUtils" eine Kante von "org.springframework" zu "org.apache".
- **Pakete vor Abhängigkeitsanalyse sammeln**: Das Skript bestimmt die Paketgruppe jeder Klasse basierend auf `level`, bevor es ihre Imports analysiert, und stellt so sicher, dass Abhängigkeiten zwischen Gruppen und nicht einzelnen Klassen bestehen.
- **Beispielkonformität**: Für Ihre Beispiel-Kante:
  - Original: `"org.springframework.boot.web.servlet.server.Session" -> "org.springframework.boot.convert.DurationUnit"`
  - Mit `level=2`: Beide Klassen sind in "org.springframework", daher wird keine Kante hinzugefügt (gleiche Gruppe).
  - Mit `level=3`: "org.springframework.boot.web" -> "org.springframework.boot.convert", fügt eine Kante zwischen diesen verschiedenen Gruppen hinzu.

### Verwendungsbeispiele

- **Befehl**: `python script.py /pfad/zu/projekt 1`
  - Gruppen: "org", "com", etc.
  - Ausgabe könnte beinhalten: `"org" -> "com"`, wenn eine Klasse in einem "org"-Paket eine Klasse in einem "com"-Paket importiert.

- **Befehl**: `python script.py /pfad/zu/projekt 2`
  - Gruppen: "org.springframework", "org.apache", etc.
  - Ausgabe könnte beinhalten: `"org.springframework" -> "org.apache"`.

### Hinweise

- Das Skript behält das ursprüngliche Verhalten bei, nur projektinterne Abhängigkeiten (Imports innerhalb von `all_classes`) einzubeziehen und Wildcard-Imports sowie Selbstabhängigkeiten auszuschließen.
- Klassen ohne Paketdeklaration werden, konsistent mit dem ursprünglichen Skript, übersprungen.
- Die Ausgabe ist ein gerichteter Graph im DOT-Format, der mit Tools wie Graphviz betrachtet werden kann.

Dieses modifizierte Skript sollte Ihre Anfrage zur Gruppierung von Abhängigkeiten nach Paketebenen-Hierarchie vollständig erfüllen.