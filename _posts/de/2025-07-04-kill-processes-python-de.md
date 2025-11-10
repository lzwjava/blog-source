---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Prozesse mit Python beenden
translated: true
type: note
---

### Prozesse unter Windows mit Python beenden

Um Prozesse unter Windows programmatisch zu beenden, verwenden Sie hauptsächlich das Modul `subprocess`, um Systembefehle wie `taskkill` aufzurufen. Das Modul `signal` ist auf Unix-Systeme ausgerichtet und eignet sich nicht zuverlässig zum Beenden von Prozessen unter Windows (Signale wie SIGKILL werden nicht nativ unterstützt; `os.kill()` kann begrenzte Signale senden, ist aber nicht ideal für eine vollständige Prozessbeendigung). Das Modul `platform` kann helfen, zu bestätigen, dass Sie sich auf Windows befinden, um betriebssystemspezifisches Verhalten zu gewährleisten.

#### Schritt 1: Module installieren und importieren
- `subprocess`, `signal` und `platform` sind Teil der Python Standard Library, daher ist keine Installation erforderlich.
- Beispiel-Imports:

```python
import subprocess
import platform
import os  # Für PID-Zugriff, falls benötigt
```

#### Schritt 2: Windows-Betriebssystem erkennen (mit `platform`)
- Bestätigen Sie die Umgebung, um plattformübergreifende Probleme zu vermeiden:

```python
if platform.system() == 'Windows':
    print("Läuft unter Windows - verwende kompatible Beendigungsmethoden.")
```

#### Schritt 3: Einen Prozess beenden
- Um einen bestehenden Prozess anhand seiner Prozess-ID (PID) oder seines Namens zu beenden, verwenden Sie `taskkill` über `subprocess`. Dies ist die zuverlässige, Windows-native Methode, da `subprocess.terminate()` oder `.kill()` nur für Prozesse funktioniert, die Sie selbst mit `subprocess.Popen` gestartet haben.
- Beispiel: Beenden Sie einen Prozess anhand der PID (erzwingend mit dem `/F`-Flag). Ersetzen Sie `1234` durch die tatsächliche PID.

```python
def kill_process_by_pid(pid):
    try:
        subprocess.call(['taskkill', '/PID', str(pid), '/F'])
        print(f"Prozess {pid} beendet.")
    except subprocess.CalledProcessError as e:
        print(f"Prozess {pid} konnte nicht beendet werden: {e}")

# Verwendung
kill_process_by_pid(1234)
```

- Beenden anhand des Prozessnamens (z.B. 'notepad.exe'), wodurch alle übereinstimmenden Prozesse beendet werden:

```python
def kill_process_by_name(name):
    try:
        subprocess.call(['taskkill', '/IM', name, '/F'])
        print(f"Prozesse, die auf '{name}' zutreffen, wurden beendet.")
    except subprocess.CalledProcessError as e:
        print(f"Prozesse '{name}' konnten nicht beendet werden: {e}")

# Verwendung
kill_process_by_name('notepad.exe')
```

#### Einschränkungen und Hinweise
- `subprocess` ruft externe Befehle auf, stellen Sie also sicher, dass Ihr Skript über die entsprechenden Berechtigungen verfügt (z.B. Ausführung als Administrator für Systemprozesse).
- Für einen Prozess, der via `subprocess.Popen` gestartet wurde, verwenden Sie `.terminate()` (ordentliches Herunterfahren) oder `.kill()` (erzwungen) direkt:

```python
proc = subprocess.Popen(['notepad.exe'])  # Starten
proc.kill()  # Beenden
```

- `signal`-Modul: Die Verwendung von `os.kill(pid, signal.SIGTERM)` könnte für einige Signale unter Windows funktionieren (Python 3.2+), ist aber weniger robust und beendet möglicherweise nicht alle Prozesse. Zum Beispiel:

```python
import signal
os.kill(pid, signal.SIGTERM)  # Schließt eventuell sanft; nicht garantiert
```

Verlassen Sie sich nicht auf `signal` zum Beenden unter Windows – verwenden Sie für die besten Ergebnisse `subprocess` mit `taskkill`.

Wenn Sie PIDs auflisten müssen (z.B. via `tasklist`-Befehl), können Sie diese zuerst abfragen, um dynamisch zu beenden. Für erweiterte Prozessverwaltung ziehen Sie Drittanbieter-Bibliotheken wie `psutil` in Betracht, aber die oben genannten Methoden verwenden nur Standardmodule.