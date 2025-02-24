---
audio: true
lang: de
layout: post
title: Analyse Java-Abhängigkeiten
translated: true
---

Hier ist ein Python-Skript, das alle `.java`-Dateien in einem Projekt scannt, deren Abhängigkeiten basierend auf Importanweisungen analysiert und eine Abhängigkeitsgrafik im DOT-Format als "Abhängigkeitstext" ausgibt. Dieses Skript konzentriert sich auf interne Abhängigkeiten zwischen Klassen innerhalb des Projekts und bietet eine klare Darstellung, die mit Tools wie Graphviz visualisiert werden kann.

### Skriptübersicht
Das Skript:
1. **Scannt das Projektverzeichnis** rekursiv, um alle `.java`-Dateien zu finden.
2. **Analysiert Abhängigkeiten**, indem es Paketdeklarationen und Importanweisungen aus jeder `.java`-Datei extrahiert.
3. **Gibt einen Abhängigkeitstext** im DOT-Format aus, der gerichtete Kanten zwischen Klassen zeigt, wobei eine Klasse eine andere innerhalb des Projekts importiert.

Hier ist das vollständige Skript:

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
        str: Der Paketname oder None, wenn nicht gefunden.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.search(r'^\s*package\s+([\w.]+);', line)
                if match:
                    return match.group(1)
    except Exception as e:
        print(f"Warnung: {file_path} konnte nicht gelesen werden: {e}")
    return None

def get_specific_imports(file_path):
    """
    Extrahiert spezifische Klassenimports aus einer .java-Datei, wobei Wildcard-Imports ausgeschlossen werden.

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
                    # Ausschließen von Wildcard-Imports (z.B., import java.util.*;)
                    if not imp.endswith('.*'):
                        imports.append(imp)
    except Exception as e:
        print(f"Warnung: {file_path} konnte nicht gelesen werden: {e}")
    return imports

if __name__ == '__main__':
    # Überprüfen auf Befehlszeilenargument
    if len(sys.argv) != 2:
        print("Verwendung: python script.py <Stammverzeichnis>")
        sys.exit(1)

    root_dir = sys.argv[1]
    all_classes = set()

    # Erster Durchlauf: Sammeln aller vollständig qualifizierten Klassennamen im Projekt
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                package = get_package(file_path)
                if package:
                    class_name = file.replace('.java', '')
                    full_class_name = f"{package}.{class_name}"
                    all_classes.add(full_class_name)

    # Speichern von Abhängigkeiten: Klasse -> Menge der Klassen, von denen sie abhängt
    dependencies = defaultdict(set)

    # Zweiter Durchlauf: Analysieren von Abhängigkeiten basierend auf spezifischen Imports
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                package = get_package(file_path)
                if package:
                    class_name = file.replace('.java', '')
                    full_class_name = f"{package}.{class_name}"
                    imports = get_specific_imports(file_path)
                    for imp in imports:
                        # Nur Abhängigkeiten von Klassen innerhalb des Projekts einschließen
                        # Selbstabhängigkeiten ausschließen
                        if imp in all_classes and imp != full_class_name:
                            dependencies[full_class_name].add(imp)

    # Ausgabe des Abhängigkeitsgrafen im DOT-Format
    print('digraph G {')
    for class_name in sorted(dependencies):
        for dep in sorted(dependencies[class_name]):
            print(f'  "{class_name}" -> "{dep}";')
    print('}')
```

### Funktionsweise
#### 1. **Befehlszeilen-Eingabe**
- Das Skript erwartet ein einziges Argument: das Stammverzeichnis des Java-Projekts.
- Beispielverwendung: `python script.py /pfad/zum/projekt`
- Wenn kein Argument angegeben ist, gibt es Anweisungen zur Verwendung aus und beendet sich.

#### 2. **Finden von `.java`-Dateien**
- Verwendet `os.walk()`, um das angegebene Verzeichnis rekursiv zu durchsuchen und alle Dateien zu identifizieren, die mit `.java` enden.

#### 3. **Extrahieren von Klasseninformationen**
- **Paketextraktion**: Die Funktion `get_package` liest jede `.java`-Datei und verwendet einen regulären Ausdruck (`^\s*package\s+([\w.]+);`), um die Paketdeklaration zu finden (z.B., `package com.mycompany.myproject;`).
  - Gibt `None` zurück, wenn kein Paket gefunden wird oder die Datei nicht gelesen werden kann.
- **Klassenname**: Geht davon aus, dass der Klassenname mit dem Dateinamen übereinstimmt (z.B., `MyClass.java` definiert `MyClass`).
- **Vollständig qualifizierter Name**: Kombiniert Paket- und Klassennamen (z.B., `com.mycompany.myproject.MyClass`).

#### 4. **Sammeln aller Klassen**
- Im ersten Durchlauf wird eine Menge aller vollständig qualifizierten Klassennamen im Projekt erstellt, um sie später schnell nachzuschlagen.

#### 5. **Analysieren von Abhängigkeiten**
- **Importextraktion**: Die Funktion `get_specific_imports` extrahiert Importanweisungen mit einem regulären Ausdruck (`^\s*import\s+([\w.]+);`), wobei Wildcard-Imports (z.B., `import java.util.*;`) ausgeschlossen werden.
  - Beispiel: Aus `import com.mycompany.myproject.utils.Helper;` wird `com.mycompany.myproject.utils.Helper` extrahiert.
- **Abhängigkeitszuordnung**: Für jede `.java`-Datei:
  - Holt sich den vollständig qualifizierten Klassennamen.
  - Überprüft die spezifischen Imports.
  - Wenn eine importierte Klasse im Klassensatz des Projekts ist und nicht die Klasse selbst, wird eine Abhängigkeit hinzugefügt.

#### 6. **Ausgeben des Abhängigkeitstextes**
- Gibt einen gerichteten Graphen im DOT-Format aus:
  - Beginnt mit `digraph G {`.
  - Für jede Klasse mit Abhängigkeiten gibt es Kanten wie `"ClassA" -> "ClassB";` aus.
  - Endet mit `}`.
- Klassen und Abhängigkeiten werden für eine konsistente Ausgabe sortiert.
- Beispielausgabe:
  ```
  digraph G {
    "com.mycompany.myproject.ClassA" -> "com.mycompany.myproject.utils.Helper";
    "com.mycompany.myproject.ClassB" -> "com.mycompany.myproject.ClassA";
  }
  ```

### Beispielverwendung
1. Speichern Sie das Skript als `analyze_deps.py`.
2. Führen Sie es aus:
   ```bash
   python analyze_deps.py /pfad/zum/java/projekt
   ```
3. Leiten Sie die Ausgabe in eine Datei um:
   ```bash
   python analyze_deps.py /pfad/zum/java/projekt > abhaengigkeiten.dot
   ```
4. Visualisieren Sie mit Graphviz:
   ```bash
   dot -Tpng abhaengigkeiten.dot -o abhaengigkeiten.png
   ```
   Dies erzeugt eine PNG-Datei, die den Abhängigkeitsgraphen zeigt.

### Annahmen und Einschränkungen
- **Eine öffentliche Klasse pro Datei**: Geht davon aus, dass jede `.java`-Datei eine öffentliche Klasse enthält, die nach der Datei benannt ist, gemäß Java-Konvention.
- **Importbasierte Abhängigkeiten**: Berücksichtigt nur Abhängigkeiten, die durch spezifische Importanweisungen angegeben werden (z.B., `import com.example.SomeClass;`), ignoriert Wildcard-Imports (`import com.example.*;`) und Verweise innerhalb desselben Pakets (die keine Imports erfordern).
- **Interner Fokus**: Verfolgt nur Abhängigkeiten zwischen Klassen innerhalb des Projekts und ignoriert externe Bibliotheken.
- **Grundlegendes Parsen**: Verwendet reguläre Ausdrücke für Einfachheit, was möglicherweise Randfälle verpasst (z.B. Imports innerhalb von Kommentaren). Ein vollständiger Java-Parser wäre robuster, aber komplexer.

### Anpassung
- **Ausgabeformat**: Ändern Sie die `print`-Anweisungen, um das Abhängigkeitstextformat zu ändern (z.B. eine einfache Liste anstelle von DOT).
- **Fehlerbehandlung**: Verbessert mit `try-except`-Blöcken, um unlesbare Dateien anmutig zu überspringen.
- **Umfang**: Könnte erweitert werden, um externe Abhängigkeiten oder Abhängigkeiten innerhalb desselben Pakets mit tieferer Codeanalyse zu enthalten.

Dieses Skript bietet einen praktischen Ausgangspunkt für die Abhängigkeitsanalyse, geeignet zur Verständnis der Struktur eines Java-Projekts durch seine internen Klassenbeziehungen.