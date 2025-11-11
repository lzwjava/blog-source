---
audio: false
generated: true
lang: de
layout: post
title: Bereinigte Log-Meldungen
translated: true
type: note
---

```python
import sys
import argparse
from difflib import SequenceMatcher

def clean_log(input_path=None, output_path=None, similarity_threshold=1.0, lines_to_compare=1):
    """
    Liest eine Log-Datei, entfernt doppelte aufeinanderfolgende Standard-Log-Zeilen basierend auf Ähnlichkeit
    und schreibt die bereinigte Log-Datei in eine angegebene Datei, standardmäßig durch Überschreiben der Eingabedatei.

    Args:
        input_path (str, optional): Pfad zur Eingabe-Log-Datei. Wenn None, wird von stdin gelesen.
        output_path (str, optional): Pfad zur Ausgabe-Log-Datei. Wenn None, wird die Eingabedatei überschrieben.
        similarity_threshold (float, optional): Ähnlichkeitsverhältnis (0.0 bis 1.0), um Zeilen als Duplikate zu betrachten. Standardwert ist 1.0 (exakte Übereinstimmung).
        lines_to_compare (int, optional): Anzahl der aufeinanderfolgenden Zeilen zum Vergleichen. Standardwert ist 1.
    """

    if not isinstance(lines_to_compare, int) or lines_to_compare < 1:
        raise ValueError("lines_to_compare muss eine ganze Zahl größer oder gleich 1 sein.")

    # Bestimme die Eingabequelle
    if input_path:
        try:
            with open(input_path, 'r') as infile:
                lines = infile.readlines()
        except FileNotFoundError:
            print(f"Error: Datei nicht gefunden unter Pfad: {input_path}", file=sys.stderr)
            sys.exit(1)
    else:
        lines = sys.stdin.readlines()  # Alle Zeilen von stdin lesen

    # Bestimme das Ausgabeziel
    if output_path:
        try:
            outfile = open(output_path, 'w')
        except IOError:
            print(f"Error: Datei kann nicht zum Schreiben geöffnet werden: {output_path}", file=sys.stderr)
            sys.exit(1)
    elif input_path:
        try:
            outfile = open(input_path, 'w')  # Überschreibe die Eingabedatei
        except IOError:
            print(f"Error: Datei kann nicht zum Schreiben geöffnet werden: {input_path}", file=sys.stderr)
            sys.exit(1)
    else:
        outfile = sys.stdout  # Standardmäßig stdout, wenn kein input_path

    num_lines = len(lines)
    i = 0
    removed_lines = 0
    while i < num_lines:
        # Sammle 'lines_to_compare' Zeilen oder verbleibende Zeilen, wenn weniger als 'lines_to_compare'
        current_lines = lines[i:min(i + lines_to_compare, num_lines)]

        # Verarbeite nur, wenn wir genug Zeilen zum Vergleichen haben
        if len(current_lines) == lines_to_compare:
            # Extrahiere Standardinformationen aus dem ersten Satz von Zeilen
            current_standards = []
            all_standard = True
            for line in current_lines:
                parts = line.split(" | ", 3)
                if len(parts) == 4:
                    level, _, thread, message = parts
                    current_standards.append((thread, message))
                else:
                    print(f"Non-standard line: {line.strip()}")
                    print(line, end='', file=outfile)
                    all_standard = False
                    break  # Verarbeitung dieser Gruppe stoppen, wenn eine nicht-standard Zeile gefunden wird

            if all_standard:
                # Extrahiere Standardinformationen aus dem zweiten Satz von Zeilen (falls verfügbar)
                next_lines_start_index = i + lines_to_compare
                next_lines_end_index = min(next_lines_start_index + lines_to_compare, num_lines)
                next_lines = lines[next_lines_start_index:next_lines_end_index]

                if len(next_lines) == lines_to_compare:
                    next_standards = []
                    for line in next_lines:
                        parts = line.split(" | ", 3)
                        if len(parts) == 4:
                            level, _, thread, message = parts
                            next_standards.append((thread, message))
                        else:
                            # Behandle die nächsten Zeilen als nicht-standard, falls eine davon nicht-standard ist
                            next_standards = None
                            break

                    if next_standards:
                        similarity = SequenceMatcher(None, ' '.join([' '.join(x) for x in current_standards]), ' '.join([' '.join(x) for x in next_standards])).ratio()
                        print(f"Similarity: {similarity:.4f}, Threshold: {similarity_threshold:.4f}")

                        if similarity < similarity_threshold:
                            for line in current_lines:
                                print(line, end='', file=outfile)
                        else:
                            print(f"Skipping duplicate lines: { ''.join([line.strip() for line in current_lines])}")
                            removed_lines += len(current_lines)
                    else:
                        for line in current_lines:
                            print(line, end='', file=outfile)
                else:
                    for line in current_lines:
                        print(line, end='', file=outfile)
            i += lines_to_compare  # Zum nächsten Satz von Zeilen wechseln
        else:
            # Behandle die verbleibenden Zeilen (weniger als 'lines_to_compare')
            for line in current_lines:
                parts = line.split(" | ", 3)
                if len(parts) == 4:
                    print(line, end='', file=outfile)
                else:
                    print(f"Non-standard line: {line.strip()}")
                    print(line, end='', file=outfile)
            i += len(current_lines)

    if output_path or input_path:
        outfile.close()

    print(f"Removed {removed_lines} duplicate lines.")


def is_valid_similarity_threshold(value):
    """
    Prüft, ob der gegebene Wert ein gültiger Ähnlichkeitsschwellenwert ist.
    """
    try:
        value = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError("Ähnlichkeitsschwellenwert muss eine Gleitkommazahl sein.")
    if 0.0 <= value <= 1.0:
        return value
    else:
        raise argparse.ArgumentTypeError("Ähnlichkeitsschwellenwert muss zwischen 0.0 und 1.0 liegen.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Entferne doppelte Log-Zeilen aus einer Datei oder stdin und schreibe in eine Datei, standardmäßig durch Überschreiben der Eingabedatei.")
    parser.add_argument("input_path", nargs="?", type=str, help="Pfad zur Eingabe-Log-Datei (optional, Standardwert ist stdin)")
    parser.add_argument("-o", "--output_path", type=str, help="Pfad zur Ausgabe-Log-Datei (optional, Standardwert ist Überschreiben der Eingabedatei)")
    parser.add_argument("-s", "--similarity", type=is_valid_similarity_threshold, default=1.0, help="Ähnlichkeitsschwellenwert (0.0-1.0), um Zeilen als Duplikate zu betrachten (Standard: 1.0)")
    parser.add_argument("-l", "--lines", type=int, default=1, help="Anzahl der aufeinanderfolgenden Zeilen zum Vergleichen (Standard: 1)")

    args = parser.parse_args()

    clean_log(args.input_path, args.output_path, args.similarity, args.lines)
```

Dieses Python-Skript `clean_log.py` ist dafür konzipiert, doppelte Log-Zeilen aus einer Datei oder der Standardeingabe zu entfernen. Es verwendet einen Ähnlichkeitsschwellenwert, um zu bestimmen, ob aufeinanderfolgende Log-Zeilen ähnlich genug sind, um als Duplikate betrachtet zu werden.

Hier ist eine Aufschlüsselung des Codes:

**1. Imports:**

- `sys`: Wird für die Interaktion mit dem Python-Interpreter verwendet, z.B. zum Lesen von stdin und Schreiben nach stderr.
- `argparse`: Wird für die Erstellung einer Kommandozeilenschnittstelle verwendet.
- `difflib.SequenceMatcher`: Wird für den Vergleich der Ähnlichkeit zwischen Sequenzen von Strings verwendet.

**2. `clean_log` Funktion:**

- Nimmt `input_path`, `output_path`, `similarity_threshold` und `lines_to_compare` als Argumente.
- `input_path`: Gibt die Eingabe-Log-Datei an. Wenn `None`, wird von stdin gelesen.
- `output_path`: Gibt die Ausgabedatei an. Wenn `None` und `input_path` gegeben ist, wird die Eingabedatei überschrieben. Wenn beide `None` sind, wird nach stdout geschrieben.
- `similarity_threshold`: Ein Float zwischen 0.0 und 1.0, der das minimale Ähnlichkeitsverhältnis bestimmt, damit Zeilen als Duplikate betrachtet werden. Ein Wert von 1.0 bedeutet, dass nur identische Zeilen entfernt werden.
- `lines_to_compare`: Eine ganze Zahl, die die Anzahl der aufeinanderfolgenden Zeilen zum Vergleichen auf Ähnlichkeit angibt.

- **Eingabe-Behandlung:**
    - Liest Zeilen aus der Eingabedatei oder von stdin.
    - Behandelt `FileNotFoundError`, falls die Eingabedatei nicht existiert.

- **Ausgabe-Behandlung:**
    - Öffnet die Ausgabedatei zum Schreiben oder verwendet stdout.
    - Behandelt `IOError`, falls die Ausgabedatei nicht geöffnet werden kann.

- **Duplikat-Entfernungs-Logik:**
    - Iteriert durch die Zeilen der Log-Datei in Blöcken von `lines_to_compare`.
    - Für jeden Block:
        - Teilt jede Zeile anhand des " | " Trennzeichens in Teile auf, erwartet vier Teile: Level, Zeitstempel, Thread und Nachricht.
        - Wenn eine Zeile nicht vier Teile hat, wird sie als "nicht-standard" Zeile betrachtet und ohne Vergleich in die Ausgabe geschrieben.
        - Wenn alle Zeilen im aktuellen Block Standard sind, vergleicht sie sie mit den nächsten `lines_to_compare` Zeilen.
        - Verwendet `SequenceMatcher`, um das Ähnlichkeitsverhältnis zwischen den zusammengefügten Strings der Thread- und Nachrichtenteile des aktuellen und nächsten Blocks zu berechnen.
        - Wenn das Ähnlichkeitsverhältnis kleiner als der `similarity_threshold` ist, wird der aktuelle Block von Zeilen in die Ausgabe geschrieben.
        - Wenn das Ähnlichkeitsverhältnis größer oder gleich dem `similarity_threshold` ist, wird der aktuelle Block von Zeilen als Duplikat betrachtet und übersprungen.
    - Behandelt die verbleibenden Zeilen am Ende der Datei (weniger als `lines_to_compare` Zeilen).

- **Statistiken:**
    - Zählt die Anzahl der entfernten Zeilen.
    - Gibt die Anzahl der entfernten Zeilen auf der Konsole aus.

- **Datei-Schließen:**
    - Schließt die Ausgabedatei, falls sie geöffnet wurde.

**3. `is_valid_similarity_threshold` Funktion:**

- Eine Hilfsfunktion, die von `argparse` verwendet wird, um das Ähnlichkeitsschwellenwert-Argument zu validieren.
- Prüft, ob der Eingabewert ein Float zwischen 0.0 und 1.0 ist.

**4. `if __name__ == "__main__":` Block:**

- Dieser Block wird ausgeführt, wenn das Skript von der Kommandozeile ausgeführt wird.
- Verwendet `argparse`, um einen Kommandozeilen-Argument-Parser zu erstellen.
- Definiert die folgenden Argumente:
    - `input_path`: Der Pfad zur Eingabe-Log-Datei (optional).
    - `-o` oder `--output_path`: Der Pfad zur Ausgabe-Log-Datei (optional).
    - `-s` oder `--similarity`: Der Ähnlichkeitsschwellenwert (Standard: 1.0).
    - `-l` oder `--lines`: Die Anzahl der zu vergleichenden Zeilen (Standard: 1).
- Parst die Kommandozeilenargumente mit `parser.parse_args()`.
- Ruft die `clean_log` Funktion mit den geparsten Argumenten auf.

**Zusammenfassend bietet das Skript eine flexible Möglichkeit, Log-Dateien zu bereinigen, indem doppelte Zeilen basierend auf einem konfigurierbaren Ähnlichkeitsschwellenwert und der Anzahl der zu vergleichenden Zeilen entfernt werden. Es unterstützt das Lesen von stdin, Schreiben nach stdout und Überschreiben der Eingabedatei.**