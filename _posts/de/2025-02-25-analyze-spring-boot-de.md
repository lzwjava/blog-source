---
audio: false
generated: true
lang: de
layout: post
title: Analyse von Spring Boot Projekten
translated: true
type: note
---

Um ein Spring Boot-Projekt (das aus mehreren Modulen bestehen kann) zu analysieren und alle mit `@GetMapping` oder `@PostMapping` Annotationen definierten APIs zu extrahieren, müssen wir das Projektverzeichnis durchlaufen, Controller-Klassen identifizieren, die API-Pfade extrahieren und sie in einem bestimmten Format ausgeben. Nachfolgend finden Sie ein vollständiges Python-Skript, das diese Aufgabe erfüllt, inspiriert von der Struktur des bereitgestellten Codes, aber an die neuen Anforderungen angepasst. Die Ausgabe listet jeden Controller mit seinen zugehörigen GET- und POST-Pfaden im Format "XXController: get pfad post pfad" auf.

### Vorgehensweise

1.  **Verzeichnis durchlaufen**: Rekursiv alle `.java`-Dateien im Projektverzeichnis und seinen Unterverzeichnissen finden.
2.  **Controller identifizieren**: Jede Java-Datei auf `@Controller` oder `@RestController` Annotationen überprüfen, um zu bestätigen, dass es sich um eine Controller-Klasse handelt.
3.  **Klassenebene Pfade extrahieren**: Nach `@RequestMapping` Annotationen auf Klassenebene suchen, um Basis-Pfade zu bestimmen.
4.  **Methodenebene APIs extrahieren**: Methoden finden, die mit `@GetMapping` oder `@PostMapping` annotiert sind, deren Pfade extrahieren und sie ggf. mit Basis-Pfaden kombinieren.
5.  **Organisieren und Ausgeben**: GET- und POST-Pfade pro Controller sammeln und im angegebenen Format ausgeben.

### Python-Skript

```python
import os
import sys
import re
from collections import defaultdict

def find_java_files(root_dir):
    """
    Rekursiv alle .java-Dateien im angegebenen Verzeichnis und seinen Unterverzeichnissen finden.
    
    Args:
        root_dir (str): Das Stammverzeichnis, von dem aus die Suche beginnen soll.
    
    Yields:
        str: Der vollständige Pfad zu jeder .java-Datei.
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.java'):
                yield os.path.join(dirpath, filename)

def extract_paths(line, annotation_type):
    """
    Extrahiert Pfadwerte aus einer Spring-Annotation (@GetMapping, @PostMapping oder @RequestMapping).
    
    Args:
        line (str): Die Zeile, die die Annotation enthält.
        annotation_type (str): Der Typ der Annotation ('GetMapping', 'PostMapping' oder 'RequestMapping').
    
    Returns:
        list: Eine Liste von Pfad-Strings, die aus der Annotation extrahiert wurden.
    """
    if annotation_type in ['GetMapping', 'PostMapping']:
        match = re.search(rf'@{annotation_type}\\((.*)\\)', line)
        if match:
            content = match.group(1)
            # Extrahiere alle String-Literale innerhalb von Anführungszeichen
            paths = re.findall(r'"([^"]*)"', content)
            return paths
        return []
    elif annotation_type == 'RequestMapping':
        match = re.search(r'@RequestMapping\\((.*)\\)', line)
        if match:
            content = match.group(1)
            # Suche nach 'value' oder 'path' Attribut
            value_match = re.search(r'(value|path)\s*=\s*({[^}]*}|"[^"]*")', content)
            if value_match:
                value = value_match.group(2)
                if value.startswith('{'):
                    paths = re.findall(r'"([^"]*)"', value)
                else:
                    paths = [value.strip('"')]
                return paths
            # Falls kein 'value' oder 'path', gehe von direkter Pfadangabe aus
            paths = re.findall(r'"([^"]*)"', content)
            return paths
        return []

if __name__ == '__main__':
    # Kommandozeilenargumente parsen
    if len(sys.argv) != 2:
        print("Usage: python script.py <root_directory>")
        sys.exit(1)
    
    root_dir = sys.argv[1]
    if not os.path.isdir(root_dir):
        print(f"[ERROR] Der angegebene Pfad ist kein Verzeichnis: {root_dir}")
        sys.exit(1)
    
    print(f"[INFO] Beginne Analyse des Verzeichnisses: {root_dir}")
    
    # Initialisiere ein Dictionary, um Controller-Zuordnungen zu speichern
    controllers = defaultdict(lambda: {'GET': [], 'POST': []})
    total_files = 0
    error_files = 0
    
    # Verarbeite alle Java-Dateien
    for java_file in find_java_files(root_dir):
        try:
            with open(java_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # Prüfe, ob die Datei ein Controller ist
            if any('@Controller' in line or '@RestController' in line for line in lines):
                controller_name = os.path.basename(java_file).replace('.java', '')
                
                # Finde die Klassendeklarationszeile, um klassen- und methodenebene Annotationen zu trennen
                class_line_index = None
                for i, line in enumerate(lines):
                    if re.search(r'public\s+(class|abstract\s+class|interface)\s+\w+', line):
                        class_line_index = i
                        break
                if class_line_index is None:
                    continue
                
                # Extrahiere klassenebene @RequestMapping als Basis-Pfade
                base_paths = []
                for line in lines[:class_line_index]:
                    if re.search(r'\s*@RequestMapping', line):
                        base_paths = extract_paths(line, 'RequestMapping')
                        break
                if not base_paths:
                    base_paths = ['']
                
                # Extrahiere methodenebene @GetMapping und @PostMapping
                get_paths = []
                post_paths = []
                for line in lines[class_line_index:]:
                    if re.search(r'\s*@GetMapping', line):
                        paths = extract_paths(line, 'GetMapping')
                        for base in base_paths:
                            for path in paths:
                                full_path = base + path
                                get_paths.append(full_path)
                    elif re.search(r'\s*@PostMapping', line):
                        paths = extract_paths(line, 'PostMapping')
                        for base in base_paths:
                            for path in paths:
                                full_path = base + path
                                post_paths.append(full_path)
                
                # Speichere eindeutige Pfade
                get_paths = sorted(list(set(get_paths)))
                post_paths = sorted(list(set(post_paths)))
                
                if get_paths or post_paths:
                    controllers[controller_name]['GET'] = get_paths
                    controllers[controller_name]['POST'] = post_paths
            
            total_files += 1
        except Exception as e:
            print(f"[ERROR] Konnte Datei {java_file} nicht lesen: {e}")
            error_files += 1
    
    # Drucke Zusammenfassung
    print(f"[INFO] Gesamte Java-Dateien versucht: {total_files + error_files}")
    print(f"[INFO] Erfolgreich verarbeitet: {total_files}")
    print(f"[INFO] Dateien mit Fehlern: {error_files}")
    print(f"[INFO] Gesamte Controller gefunden: {len(controllers)}")
    
    # Drucke Ergebnisse im angegebenen Format
    for controller, mappings in sorted(controllers.items()):
        print(f"{controller}:")
        for path in mappings['GET']:
            print(f"get {path}")
        for path in mappings['POST']:
            print(f"post {path}")
```

### Erklärung

-   **Imports**: Wir verwenden `os` für die Verzeichnisdurchquerung, `sys` für Kommandozeilenargumente, `re` für reguläre Ausdrücke und `defaultdict` zur Organisation der Controller-Daten.
-   **`find_java_files`**: Diese Funktion liefert rekursiv alle `.java`-Dateien im Projektverzeichnis und behandelt mehrere Module natürlich über `os.walk`.
-   **`extract_paths`**: Diese Funktion parst `@GetMapping`, `@PostMapping` oder `@RequestMapping` Annotationen, um Pfadwerte zu extrahieren. Sie behandelt:
    -   Einzelne Pfade (z.B. `@GetMapping("/pfad")`).
    -   Mehrere Pfade (z.B. `@GetMapping({"/pfad1", "/pfad2"})`).
    -   Benannte Attribute (z.B. `@RequestMapping(value = "/pfad")`).
-   **Hauptlogik**:
    -   **Kommandozeilenbehandlung**: Nimmt ein Stammverzeichnis als Eingabe, ähnlich dem bereitgestellten Skript.
    -   **Controller-Erkennung**: Prüft auf `@Controller` oder `@RestController` im Dateiinhalt.
    -   **Basis-Pfade**: Extrahiert klassenebene `@RequestMapping`-Pfade vor der Klassendeklaration.
    -   **API-Extraktion**: Verarbeitet Zeilen nach der Klassendeklaration auf `@GetMapping` und `@PostMapping`, kombiniert Pfade mit Basis-Pfaden.
    -   **Ausgabe**: Gibt jeden Controller mit seinen GET- und POST-Pfaden aus, einen pro Zeile, mit "get" oder "post" vorangestellt.
-   **Fehlerbehandlung**: Fängt Ausnahmen während des Dateilesens ab und meldet sie, ähnlich der Robustheit des bereitgestellten Codes.

### Beispielausgabe

Für ein Spring Boot-Projekt mit einer Datei `UserController.java`:

```java
@RestController
@RequestMapping("/users")
public class UserController {
    @GetMapping("/all")
    public ResponseEntity<?> getAllUsers() { ... }

    @PostMapping("/create")
    public ResponseEntity<?> createUser() { ... }
}
```

Die Ausführung von `python script.py /pfad/zu/projekt` könnte ergeben:

```
[INFO] Beginne Analyse des Verzeichnisses: /pfad/zu/projekt
[INFO] Gesamte Java-Dateien versucht: 10
[INFO] Erfolgreich verarbeitet: 10
[INFO] Dateien mit Fehlern: 0
[INFO] Gesamte Controller gefunden: 1
UserController:
get /users/all
post /users/create
```

### Anmerkungen

-   **Vereinfachungen**: Das Skript geht davon aus, dass Annotationen in einzelnen Zeilen stehen und Pfade String-Literale ohne komplexe Ausdrücke sind. Für den Produktiveinsatz könnte ein Java-Parser robuster sein.
-   **Nur GET und POST**: Wie gewünscht konzentriert es sich auf `@GetMapping` und `@PostMapping` und ignoriert andere Methoden wie PUT oder DELETE (obwohl der Denkprozess `@RequestMapping` mit Methoden in Betracht zog).
-   **Pfadverkettung**: Kombiniert klassen- und methodenebene Pfade direkt (z.B. `/users` + `/all` = `/users/all`). Spring normalisiert mehrere Schrägstriche, daher ist dies für Anzeigezwecke ausreichend.

Dieses Skript erfüllt die Anforderungen der Abfrage und behält dabei eine Struktur bei, die dem bereitgestellten Code ähnelt, um Vertrautheit und Zuverlässigkeit zu gewährleisten.