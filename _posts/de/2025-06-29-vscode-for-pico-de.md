---
audio: false
generated: true
lang: de
layout: post
title: VSCode für Raspberry Pi Pico MicroPython
translated: true
type: note
---

Ja, du kannst Visual Studio Code (VSCode) verwenden, um MicroPython-Programme für dein Raspberry Pi Pico zu schreiben, hochzuladen und auszuführen, ähnlich wie mit Thonny. VSCode ist ein leistungsstarker Editor, und mit den richtigen Erweiterungen und Tools kann es MicroPython-Entwicklung effektiv handhaben. Nachfolgend findest du eine Schritt-für-Schritt-Anleitung zur Einrichtung von VSCode für das Hochladen eines einfachen MicroPython-Programms auf deinen Pico, vorausgesetzt, MicroPython ist bereits geflasht (wie du es mit der `.uf2`-Datei getan hast).

---

### Voraussetzungen
1.  **MicroPython geflasht**: Dein Pico hat MicroPython installiert (z. B. von der `RPI_PICO-20250415-v1.25.0.uf2`-Datei).
2.  **VSCode installiert**: Lade VSCode von [code.visualstudio.com](https://code.visualstudio.com) herunter und installiere es, falls noch nicht geschehen.
3.  **Python installiert**: Installiere Python (erforderlich für MicroPython-Tools) über:
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip
    ```
4.  **USB-Verbindung**: Der Pico ist über ein datenfähiges USB-Kabel mit deinem Computer verbunden.

---

### Schritt-für-Schritt-Anleitung zur Verwendung von VSCode für MicroPython auf Raspberry Pi Pico

1.  **Erforderliche VSCode-Erweiterungen installieren**:
    - Öffne VSCode.
    - Gehe zur Erweiterungsansicht (`Strg+Umschalt+X` oder `Cmd+Umschalt+X` auf macOS).
    - Installiere die folgenden Erweiterungen:
      - **Python** (von Microsoft): Für Python- und MicroPython-Syntaxhervorhebung und IntelliSense.
      - **Pico-W-Go** (optional, aber empfohlen): Eine dedizierte Erweiterung für die Raspberry Pi Pico-Entwicklung mit MicroPython. Suche nach "Pico-W-Go" und installiere sie.
        - Hinweis: Pico-W-Go vereinfacht Dateiübertragungen und REPL-Zugriff, erfordert aber eine zusätzliche Einrichtung (siehe unten).
      - Alternativ kannst du allgemeine Erweiterungen wie **Remote-SSH** oder **Serial Monitor** verwenden, wenn du manuelle Kontrolle bevorzugst.

2.  **Pico-W-Go einrichten (Empfohlen)**:
    - **Abhängigkeiten installieren**: Pico-W-Go benötigt `pyserial` und `esptool`. Installiere sie via pip:
      ```bash
      pip3 install pyserial esptool
      ```
    - **Pico-W-Go konfigurieren**:
      - Öffne die Befehlspalette von VSCode (`Strg+Umschalt+P` oder `Cmd+Umschalt+P`).
      - Tippe **Pico-W-Go > Configure Project** ein und wähle es aus.
      - Folge den Anweisungen, um dein Projekt einzurichten:
        - Wähle den seriellen Port des Picos (z. B. `/dev/ttyACM0`). Führe `ls /dev/tty*` in einem Terminal aus, um ihn zu finden.
        - Wähle MicroPython als Interpreter.
        - Erstelle einen neuen Projektordner oder verwende einen bestehenden.
      - Pico-W-Go erstellt einen Arbeitsbereich mit einer `.picowgo`-Konfigurationsdatei.

3.  **Ein einfaches MicroPython-Programm schreiben**:
    - Erstelle in VSCode eine neue Datei (z. B. `main.py`) in deinem Projektordner.
    - Schreibe ein einfaches Programm, wie das Blinken der onboard-LED:
      ```python
      from machine import Pin
      import time

      led = Pin(25, Pin.OUT)  # Verwende "LED" für Pico W
      while True:
          led.on()
          time.sleep(0.5)
          led.off()
          time.sleep(0.5)
      ```
    - Speichere die Datei (`Strg+S` oder `Cmd+S`).

4.  **Das Programm auf den Pico hochladen**:
    - **Mit Pico-W-Go**:
      - Stelle sicher, dass der Pico verbunden ist und der korrekte Port ausgewählt ist (prüfe dies ggf. in `Pico-W-Go > Configure Project`).
      - Öffne die Befehlspalette (`Strg+Umschalt+P`).
      - Wähle **Pico-W-Go > Upload Project to Pico** aus.
      - Dies lädt alle Dateien in deinem Projektordner (z. B. `main.py`) in das Dateisystem des Picos hoch.
      - Wenn du die Datei `main.py` genannt hast, wird sie automatisch beim Booten ausgeführt.
    - **Manueller Upload mit `rshell`** (falls Pico-W-Go nicht verwendet wird):
      - Installiere `rshell`:
        ```bash
        pip3 install rshell
        ```
      - Verbinde dich mit dem Pico:
        ```bash
        rshell --port /dev/ttyACM0
        ```
      - Kopiere die Datei auf den Pico:
        ```bash
        cp main.py /pyboard/main.py
        ```
      - Verlasse `rshell` mit `exit`.

5.  **Das Programm ausführen und testen**:
    - **Mit Pico-W-Go**:
      - Öffne die Befehlspalette und wähle **Pico-W-Go > Run** aus.
      - Dies führt die aktuelle Datei aus oder öffnet den REPL für manuelle Befehle.
      - Du solltest die LED blinken sehen, wenn du das obige Beispiel verwendest.
    - **Mit VSCode-Terminal oder REPL**:
      - Öffne den REPL mit Pico-W-Go (`Pico-W-Go > Open REPL`) oder verwende `rshell`:
        ```bash
        rshell --port /dev/ttyACM0 repl
        ```
      - Teste Befehle direkt, z. B.:
        ```python
        from machine import Pin
        led = Pin(25, Pin.OUT)
        led.on()
        ```
      - Drücke `Strg+C`, um ein laufendes Programm im REPL zu stoppen.
    - Wenn die Datei `main.py` heißt, setze den Pico zurück (ausstecken und wieder einstecken oder die RESET-Taste drücken), um sie automatisch auszuführen.

6.  **Debuggen und Dateien verwalten**:
    - **Pico-W-Go**: Verwende **Pico-W-Go > Download Project from Pico**, um Dateien vom Pico abzurufen, oder **Pico-W-Go > Delete All Files**, um das Dateisystem zu löschen.
    - **rshell**: Liste Dateien mit:
      ```bash
      rshell ls /pyboard
      ```
      Lösche Dateien mit:
      ```bash
      rshell rm /pyboard/main.py
      ```
    - Überprüfe die Programmausgabe im VSCode-Terminal oder REPL.

---

### Alternative: Manueller Workflow ohne Pico-W-Go
Wenn du Pico-W-Go nicht verwenden möchtest, kannst du die MicroPython-Entwicklung manuell verwalten:
1.  Schreibe deinen Code in VSCode und speichere ihn als `main.py`.
2.  Verwende `ampy` (ein weiteres MicroPython-Tool) zum Hochladen:
    ```bash
    pip3 install adafruit-ampy
    ampy --port /dev/ttyACM0 put main.py
    ```
3.  Greife auf den REPL mit einem Terminal-Tool wie `minicom` oder `screen` zu:
    ```bash
    screen /dev/ttyACM0 115200
    ```
    Drücke `Strg+C`, um ein laufendes Programm zu stoppen und in den REPL zu gelangen.

---

### Fehlerbehebung
-   **Port nicht gefunden**: Führe `ls /dev/tty*` aus, um den Port des Picos zu überprüfen (z. B. `/dev/ttyACM0`). Stelle sicher, dass der Pico verbunden ist und MicroPython geflasht ist.
-   **Pico-W-Go-Fehler**: Überprüfe, ob `pyserial` und `esptool` installiert sind und der korrekte Port ausgewählt ist. Starte VSCode bei Bedarf neu.
-   **Programm läuft nicht**: Stelle sicher, dass die Datei als `main.py` gespeichert ist für die automatische Ausführung, oder führe sie manuell über den REPL oder `ampy run main.py` aus.
-   **LED blinkt nicht**: Überprüfe den GPIO-Pin (`25` für Pico, `"LED"` für Pico W). Teste im REPL:
    ```python
    from machine import Pin
    led = Pin(25, Pin.OUT)
    led.on()
    ```

---

### Vorteile von VSCode gegenüber Thonny
-   Bessere Code-Editing-Funktionen (z. B. IntelliSense, Git-Integration, anpassbare Workflows).
-   Unterstützt größere Projekte mit mehreren Dateien.
-   Pico-W-Go bietet eine Thonny-ähnliche Erfahrung, aber mit der Leistungsfähigkeit von VSCode.

### Einschränkungen
-   Die Einrichtung ist etwas komplexer als bei Thonny.
-   Die REPL-Integration kann sich weniger nahtlos anfühlen im Vergleich zu Thonnys All-in-One-Oberfläche.

Wenn du Hilfe mit spezifischen VSCode-Einstellungen, der Installation von Tools oder dem Schreiben komplexerer MicroPython-Programme benötigst, lass es mich wissen!