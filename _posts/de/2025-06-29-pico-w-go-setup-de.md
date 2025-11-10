---
audio: false
generated: true
lang: de
layout: post
title: VSCode Pico-W-Go für MicroPython
translated: true
type: note
---

Die Verwendung der **Raspberry Pi Pico**-Erweiterung in Visual Studio Code (VSCode) ist eine ausgezeichnete Wahl für die MicroPython-Entwicklung auf Ihrem Raspberry Pi Pico, da sie einen optimierten Workflow bietet, ähnlich wie Thonny, jedoch in der leistungsstarken Editierungsumgebung von VSCode. Die Erweiterung, auf die Sie sich wahrscheinlich beziehen, ist **Pico-W-Go** (oder eine ähnliche Erweiterung wie **Pico-Go**), die speziell für die Entwicklung mit Raspberry Pi Pico und Pico W mit MicroPython entwickelt wurde. Im Folgenden werde ich Sie durch die Einrichtung und Verwendung der **Pico-W-Go**-Erweiterung (der beliebtesten und gepflegten Option) führen, um ein einfaches MicroPython-Programm auf Ihren Pico hochzuladen, unter der Annahme, dass MicroPython bereits geflasht ist (von der von Ihnen verwendeten `RPI_PICO-20250415-v1.25.0.uf2`-Datei).

---

### Voraussetzungen
1.  **MicroPython geflasht**: Ihr Pico hat MicroPython installiert, wie Sie bereits geflasht haben.
2.  **VSCode installiert**: Stellen Sie sicher, dass VSCode installiert ist ([code.visualstudio.com](https://code.visualstudio.com)).
3.  **Python installiert**: Erforderlich für Pico-W-Go-Abhängigkeiten:
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip
    ```
4.  **USB-Verbindung**: Der Pico ist über ein datenfähiges USB-Kabel verbunden.

---

### Schritt-für-Schritt-Anleitung zur Verwendung der Raspberry Pi Pico (Pico-W-Go) Erweiterung in VSCode

1.  **Installieren Sie die Pico-W-Go Erweiterung**:
    - Öffnen Sie VSCode.
    - Gehen Sie zur Erweiterungsansicht (`Strg+Umschalt+X` oder `Cmd+Umschalt+X` auf macOS).
    - Suchen Sie nach **Pico-W-Go** und installieren Sie sie (entwickelt von Paul Obermeier und anderen).
    - Hinweis: Falls Sie eine andere Erweiterung (z.B. Pico-Go) gemeint haben, lassen Sie es mich wissen, aber Pico-W-Go ist die am häufigsten verwendete für die Pico MicroPython-Entwicklung.

2.  **Installieren Sie Pico-W-Go Abhängigkeiten**:
    - Pico-W-Go benötigt `pyserial` und `esptool` für die serielle Kommunikation und das Flashen:
      ```bash
      pip3 install pyserial esptool
      ```
    - Stellen Sie sicher, dass diese in Ihrer Python-Umgebung installiert sind (verwenden Sie `pip3 list` zur Überprüfung).

3.  **Konfigurieren Sie Pico-W-Go**:
    - Öffnen Sie die Befehlspalette in VSCode (`Strg+Umschalt+P` oder `Cmd+Umschalt+P`).
    - Tippen Sie **Pico-W-Go > Configure Project** ein und wählen Sie es aus.
    - Folgen Sie den Anweisungen:
      - **Serial Port**: Wählen Sie den Port des Picos (z.B. `/dev/ttyACM0`). Finden Sie ihn durch Ausführen von:
        ```bash
        ls /dev/tty*
        ```
        Suchen Sie nach `/dev/ttyACM0` oder ähnlich, der erscheint, wenn der Pico verbunden ist.
      - **Interpreter**: Wählen Sie MicroPython (Raspberry Pi Pico).
      - **Project Folder**: Wählen Sie einen Ordner für Ihr Projekt aus oder erstellen Sie ihn (z.B. `~/PicoProjects/MeinProjekt`).
    - Pico-W-Go erstellt eine `.picowgo` Konfigurationsdatei in Ihrem Projektordner, um die Einstellungen zu speichern.

4.  **Schreiben Sie ein einfaches MicroPython-Programm**:
    - Öffnen Sie in VSCode Ihren Projektordner (Datei > Ordner öffnen).
    - Erstellen Sie eine neue Datei namens `main.py` (MicroPython führt `main.py` automatisch beim Booten aus).
    - Fügen Sie ein einfaches Programm hinzu, z.B. zum Blinken der onboard-LED:
      ```python
      from machine import Pin
      import time

      led = Pin(25, Pin.OUT)  # Verwenden Sie "LED" für Pico W
      while True:
          led.on()
          time.sleep(0.5)
          led.off()
          time.sleep(0.5)
      ```
    - Speichern Sie die Datei (`Strg+S`).

5.  **Laden Sie das Programm auf den Pico hoch**:
    - Stellen Sie sicher, dass der Pico verbunden ist und der korrekte Port ausgewählt ist (führen Sie bei Bedarf **Pico-W-Go > Configure Project** erneut aus).
    - Öffnen Sie die Befehlspalette (`Strg+Umschalt+P`).
    - Wählen Sie **Pico-W-Go > Upload Project to Pico** aus.
      - Dies lädt alle Dateien in Ihrem Projektordner (z.B. `main.py`) in das Dateisystem des Picos hoch.
    - Alternativ, um eine einzelne Datei hochzuladen:
      - Klicken Sie mit der rechten Maustaste auf `main.py` im VSCode-Datei-Explorer.
      - Wählen Sie **Pico-W-Go > Upload File to Pico** aus.
    - Die Datei wird auf den Pico übertragen, und wenn es `main.py` ist, wird sie automatisch beim Booten ausgeführt.

6.  **Führen Sie das Programm aus und testen Sie es**:
    - **Automatische Ausführung**: Wenn Sie `main.py` hochgeladen haben, setzen Sie den Pico zurück (ausstecken und wieder einstecken oder die RESET-Taste drücken, falls vorhanden). Die LED sollte anfangen zu blinken.
    - **Manuelle Ausführung**:
      - Öffnen Sie die Befehlspalette und wählen Sie **Pico-W-Go > Run** aus.
      - Dies führt die aktuelle Datei auf dem Pico aus.
    - **Verwenden Sie den REPL**:
      - Öffnen Sie die Befehlspalette und wählen Sie **Pico-W-Go > Open REPL** aus.
      - Der REPL erscheint im Terminal von VSCode, wo Sie Befehle testen können:
        ```python
        from machine import Pin
        led = Pin(25, Pin.OUT)
        led.on()
        ```
      - Drücken Sie `Strg+C`, um ein laufendes Programm im REPL zu stoppen.

7.  **Verwalten Sie Dateien auf dem Pico**:
    - **Dateien auflisten**: Verwenden Sie **Pico-W-Go > Download Project from Pico**, um Dateien vom Dateisystem des Picos anzuzeigen oder abzurufen.
    - **Dateien löschen**: Öffnen Sie die Befehlspalette und wählen Sie **Pico-W-Go > Delete All Files** aus, um das Dateisystem des Picos zu leeren, oder verwenden Sie den REPL:
      ```python
      import os
      os.remove('main.py')
      ```
    - **Ausgabe überprüfen**: Die Programmausgabe (z.B. `print`-Anweisungen) erscheint im REPL oder im Terminal von VSCode, falls konfiguriert.

---

### Fehlerbehebung
-   **Port nicht erkannt**:
    - Führen Sie `ls /dev/tty*` aus, um den Port des Picos zu bestätigen (z.B. `/dev/ttyACM0`).
    - Stellen Sie sicher, dass das USB-Kabel die Datenübertragung unterstützt, und versuchen Sie einen anderen Port.
    - Konfigurieren Sie den Port in **Pico-W-Go > Configure Project** neu.
-   **Upload fehlgeschlagen**:
    - Überprüfen Sie, ob `pyserial` und `esptool` installiert sind (`pip3 list`).
    - Prüfen Sie, ob MicroPython läuft (REPL sollte zugänglich sein).
    - Flashen Sie MicroPython bei Bedarf neu, indem Sie den BOOTSEL-Modus erneut aufrufen und die `.uf2`-Datei kopieren.
-   **LED blinkt nicht**:
    - Bestätigen Sie den korrekten GPIO-Pin (`25` für Pico, `"LED"` für Pico W).
    - Testen Sie im REPL:
      ```python
      from machine import Pin
      led = Pin(25, Pin.OUT)
      led.on()
      ```
-   **Pico-W-Go Befehle fehlen**: Stellen Sie sicher, dass die Erweiterung installiert und aktiviert ist. Starten Sie VSCode bei Bedarf neu.

---

### Vorteile von Pico-W-Go in VSCode
-   **Integrierter Workflow**: Kombiniert Code-Editierung, Dateiverwaltung und REPL-Zugriff in VSCode.
-   **Erweiterte Funktionen**: Nutzt die Git-Integration, Erweiterungen und Anpassungsmöglichkeiten von VSCode.
-   **Plattformübergreifend**: Funktioniert unter Linux, Windows und macOS.

### Einschränkungen im Vergleich zu Thonny
-   Der Setup-Aufwand ist etwas höher (z.B. Installation von `pyserial`, Konfiguration des Ports).
-   Die REPL-Integration kann sich weniger nahtlos anfühlen als Thonnys All-in-One-Oberfläche.
-   Weniger einsteigerfreundlich für erstmalige MicroPython-Benutzer.

---

### Alternative Erweiterungen
Falls Sie eine andere Erweiterung (z.B. **Pico-Go**) gemeint haben, beachten Sie, dass Pico-Go eine ältere Alternative zu Pico-W-Go ist und möglicherweise weniger Funktionen oder Updates hat. Die Einrichtung ist ähnlich, aber Pico-W-Go wird aufgrund seiner aktiven Entwicklung und Unterstützung für sowohl Pico als auch Pico W empfohlen. Falls Sie eine andere spezifische Erweiterung verwenden, klären Sie dies bitte, und ich kann die Anweisungen entsprechend anpassen.

---

### Beispielhafter Workflow
1.  Installieren Sie Pico-W-Go und die Abhängigkeiten.
2.  Konfigurieren Sie das Projekt mit dem korrekten seriellen Port (`/dev/ttyACM0`).
3.  Schreiben und speichern Sie `main.py` mit dem LED-Blinkcode.
4.  Verwenden Sie **Pico-W-Go > Upload Project to Pico** zum Hochladen.
5.  Setzen Sie den Pico zurück oder verwenden Sie **Pico-W-Go > Run**, um das Blinken der LED zu sehen.
6.  Verwenden Sie den REPL, um interaktiv zu testen oder zu debuggen.

Wenn Sie Hilfe mit spezifischen Pico-W-Go-Befehlen, einem anderen Programmierbeispiel oder zur Fehlerbehebung (z.B. Port-Probleme, Erweiterungsfehler) benötigen, lassen Sie es mich wissen!