---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Python Regex Guide
translated: true
type: note
---

### Importieren des `re`-Moduls
Das `re`-Modul (kurz für Regular Expressions) ist Teil der Python-Standardbibliothek. Es ist kein separates "Regex-Paket", sondern ein eingebautes Modul. Importieren Sie es am Anfang Ihres Skripts:

```python
import re
```

### Grundkonzepte
Reguläre Ausdrücke (Regex) sind Muster, die verwendet werden, um Zeichenketten zu vergleichen, zu durchsuchen und zu manipulieren. Sie verwenden Sonderzeichen wie:
- `.` (beliebiges Zeichen)
- `*` (null oder mehr Vorkommen)
- `+` (ein oder mehr Vorkommen)
- `[]` (Zeichenklassen, z.B. `[a-z]` für Kleinbuchstaben)
- `^` (Anfang der Zeichenkette), `$` (Ende der Zeichenkette)

Die Beispiele basieren auf der `re`-Dokumentation von Python. Komplexe Muster sollten zur Effizienzsteigerung mit `re.compile()` kompiliert werden.

### Wichtige Funktionen und Verwendung

#### 1. **Übereinstimmung am Anfang prüfen**
   - `re.match(pattern, string)`: Prüft, ob das Muster vom Anfang der Zeichenkette an passt.
   - Gibt ein Match-Objekt oder `None` zurück.

   Beispiel:
   ```python
   import re
   result = re.match(r"Hello", "Hello world")
   print(result.group())  # Ausgabe: Hello
   ```

#### 2. **Überall in der Zeichenkette suchen**
   - `re.search(pattern, string)`: Findet das erste Vorkommen des Musters an einer beliebigen Stelle.
   - Gibt ein Match-Objekt oder `None` zurück.

   Beispiel:
   ```python
   result = re.search(r"world", "Hello world")
   print(result.group())  # Ausgabe: world
   ```

#### 3. **Alle Übereinstimmungen finden**
   - `re.findall(pattern, string)`: Gibt eine Liste aller nicht überlappenden Übereinstimmungen zurück.

   Beispiel:
   ```python
   matches = re.findall(r"\d+", "I have 3 cats and 42 dogs")
   print(matches)  # Ausgabe: ['3', '42']
   ```

#### 4. **Zeichenketten aufteilen**
   - `re.split(pattern, string)`: Teilt die Zeichenkette an den Stellen, an denen das Muster vorkommt.

   Beispiel:
   ```python
   parts = re.split(r"\s+", "Hello    world   example")
   print(parts)  # Ausgabe: ['Hello', 'world', 'example']
   ```

#### 5. **Übereinstimmungen ersetzen**
   - `re.sub(pattern, replacement, string)`: Ersetzt Übereinstimmungen durch die Ersatzzeichenkette.

   Beispiel:
   ```python
   new_string = re.sub(r"bad", "good", "This is bad")
   print(new_string)  # Ausgabe: This is good
   ```

#### 6. **Muster zur Wiederverwendung kompilieren**
   - Für wiederholte Verwendung sollte der Regex zur Leistungssteigerung in ein Pattern-Objekt kompiliert werden.

   Beispiel:
   ```python
   pattern = re.compile(r"\d+")
   matches = pattern.findall("Room 101 and 102")
   print(matches)  # Ausgabe: ['101', '102']
   ```

### Best Practices
- Verwenden Sie Raw Strings (`r""`) für Regex-Muster, um Probleme mit Backslash-Escapes zu vermeiden.
- Arbeiten Sie mit Match-Objekten: Verwenden Sie `.group()`, um die Übereinstimmung zu erhalten, und `.span()` für die Indizes.
- Testen Sie komplexe Muster mit Online-Tools oder der interaktiven Python-Shell.
- Konsultieren Sie die offizielle Python-Dokumentation: https://docs.python.org/3/library/re.html für weitere Beispiele und Flags (z.B. `re.IGNORECASE`).

Wenn Sie einen spezifischen Anwendungsfall oder einen Fehler haben, geben Sie bitte weitere Details an!