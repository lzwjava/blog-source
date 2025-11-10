---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Überwachen der Ausgabe von Unterprozessen mit Zeitlimit
translated: true
type: note
---

```python
import subprocess
import threading
import queue
import time
import sys

def read_output(proc, output_queue):
    """Thread-Funktion zum Lesen von stdout und stderr, schreibt in Queue."""
    try:
        for line in iter(proc.stdout.readline, b''):
            if not line:
                break
            output_queue.put(line.decode('utf-8', errors='ignore').rstrip())
        # Auch stderr prüfen falls benötigt
        for line in iter(proc.stderr.readline, b''):
            if not line:
                break
            output_queue.put(line.decode('utf-8', errors='ignore').rstrip())
    except Exception as e:
        output_queue.put(f"Fehler beim Lesen der Ausgabe: {e}")

def main():
    # Befehl zum Ausführen (z.B. 'mvn clean compile' unter Windows)
    cmd = ['mvn', 'clean', 'compile']  # Anpassen nach Bedarf, z.B. ['cmd', '/c', 'mvn build']
    timeout_seconds = 10

    # Subprozess starten
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        bufsize=1,  # Zeilengepuffert
        universal_newlines=False,  # Bytes behandeln
        cwd=None  # Arbeitsverzeichnis setzen falls benötigt
    )

    # Queue für Ausgabe
    output_queue = queue.Queue()

    # Thread zum Lesen der Ausgabe starten
    output_thread = threading.Thread(target=read_output, args=(proc, output_queue))
    output_thread.daemon = True
    output_thread.start()

    print("Befehl gestartet. Überwache Ausgabe alle 10 Sekunden...")

    while proc.poll() is None:
        try:
            # Auf Ausgabe mit Timeout warten
            output = output_queue.get(timeout=timeout_seconds)
            print(f"Ausgabe: {output}")  # Optional: Ausgabe drucken oder verarbeiten
        except queue.Empty:
            print(f"Keine Ausgabe für {timeout_seconds} Sekunden. Beende Befehl und beende.")
            proc.terminate()  # oder proc.kill() für erzwungenes Beenden
            try:
                proc.wait(timeout=5)  # Kurz auf ordnungsgemäßes Herunterfahren warten
            except subprocess.TimeoutExpired:
                proc.kill()
            sys.exit(1)

    # Prozess wurde normal beendet
    print("Befehl abgeschlossen.")
    output_thread.join()  # Auf Beendigung des Ausgabe-Threads warten

if __name__ == "__main__":
    main()
```

### Erklärung
- **Subprozess**: Verwendet `subprocess.Popen` um `mvn clean compile` auszuführen (Befehl nach Bedarf anpassen; für einfaches `mvn build` könnte es `['mvn', 'build']` sein oder in `cmd /c` eingewickelt falls benötigt). Läuft asynchron mit Pipes für stdout und stderr.
- **Queue Threading**: Ein separater Thread liest zeilenweise von stdout und stderr (um nicht die gesamte Ausgabe auf einmal zu lesen), decodiert sie und schreibt Zeilen in eine `queue.Queue`. Ermöglicht nicht-blockierende Lesevorgänge.
- **Timeout-Überwachung**: Im Hauptthread wird die Queue auf neue Ausgabe mit `get(timeout=10)` geprüft. Wenn 10 Sekunden lang keine Ausgabe erscheint, wird der Subprozess beendet und das Programm beendet.
- **Windows-Kompatibilität**: `subprocess` funktioniert unter Windows. Falls der Befehl eine Shell benötigt (z.B. für `mvn` wenn nicht im PATH), könnte `shell=True` gesetzt und der Befehl als String übergeben werden: `proc = subprocess.Popen("mvn clean compile", shell=True, ...)`.
- **Randfälle**: Wenn der Prozess normal beendet wird während gewartet wird, stoppt die Schleife und wir joinen den Thread. Der Thread ist daemonic um Hängen beim Beenden zu vermeiden.
- **Anpassung**: Kann modifiziert werden um Ausgaben anders zu verarbeiten (z.B. in Datei loggen statt drucken). Für stderr wird es in dieselbe Queue kombiniert; könnte bei Bedarf getrennt werden. Falls Ausgaben binär sind, Decodierung anpassen.