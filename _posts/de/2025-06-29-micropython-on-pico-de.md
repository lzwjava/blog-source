---
audio: false
generated: true
lang: de
layout: post
title: Hochladen von MicroPython auf den Pico
translated: true
type: note
---

Nach dem Flashen von MicroPython auf Ihren Raspberry Pi Pico (mithilfe der `.uf2`-Datei, wie beschrieben), können Sie ein einfaches MicroPython-Programm mit einem Tool wie Thonny IDE hochladen und ausführen. Thonny ist einsteigerfreundlich und wird häufig für die MicroPython-Entwicklung verwendet. Nachfolgend finden Sie die Schritte zum Einrichten von MicroPython und zum Hochladen eines einfachen Programms auf Ihren Pico.

---

### Voraussetzungen
1.  **MicroPython Geflasht**: Sie haben bereits `RPI_PICO-20250415-v1.25.0.uf2` auf das `RPI-RP2`-Laufwerk kopiert, und der Pico hat neu gestartet (das `RPI-RP2`-Laufwerk sollte nicht mehr erscheinen).
2.  **USB-Verbindung**: Der Pico ist über ein USB-Kabel, das Datenübertragung unterstützt, mit Ihrem Computer verbunden.
3.  **Thonny IDE**: Installieren Sie Thonny, falls noch nicht geschehen:
    - **Linux**: Installieren Sie Thonny mit Ihrem Paketmanager oder laden Sie es von [thonny.org](https://thonny.org) herunter.
      ```bash
      sudo apt update
      sudo apt install thonny
      ```
    - Alternativ können Sie `pip` verwenden:
      ```bash
      pip install thonny
      ```
    - Für Windows/macOS laden Sie die Software von [thonny.org](https://thonny.org) herunter und installieren sie.

---

### Schritt-für-Schritt-Anleitung zum Hochladen eines einfachen MicroPython-Programms

1.  **Pico verbinden und Thonny öffnen**:
    - Stecken Sie Ihren Pico in den USB-Port Ihres Computers.
    - Öffnen Sie Thonny IDE.

2.  **Thonny für MicroPython konfigurieren**:
    - Gehen Sie in Thonny zu **Tools > Options > Interpreter** (oder **Run > Select interpreter**).
    - Wählen Sie **MicroPython (Raspberry Pi Pico)** aus dem Interpreter-Dropdown-Menü.
    - Wenn der serielle Port des Picos (z.B. `/dev/ttyACM0` unter Linux) nicht automatisch erscheint:
      - Überprüfen Sie die verfügbaren Ports im Dropdown-Menü oder führen Sie `ls /dev/tty*` in einem Terminal aus, um den Port des Picos zu identifizieren (normalerweise `/dev/ttyACM0` oder ähnlich).
      - Wählen Sie den korrekten Port manuell aus.
    - Klicken Sie auf **OK**, um die Einstellungen zu speichern.

3.  **Überprüfen, ob MicroPython läuft**:
    - In Thonnys **Shell** (unterer Bereich) sollten Sie eine MicroPython REPL-Eingabeaufforderung sehen:
      ```
      >>>
      ```
    - Testen Sie sie, indem Sie einen einfachen Befehl eingeben, z.B.:
      ```python
      print("Hello, Pico!")
      ```
      Drücken Sie die Eingabetaste, und Sie sollten die Ausgabe in der Shell sehen.

4.  **Ein einfaches MicroPython-Programm schreiben**:
    - Erstellen Sie in Thonnys Haupt-Editor eine neue Datei und schreiben Sie ein einfaches Programm. Zum Beispiel ein Programm, um die onboard-LED des Picos blinken zu lassen (auf GPIO 25 für den Pico, oder "LED" für den Pico W):
      ```python
      from machine import Pin
      import time

      # Initialisiere die onboard-LED
      led = Pin(25, Pin.OUT)  # Verwende "LED" anstelle von 25 für Pico W

      # Lasse die LED blinken
      while True:
          led.on()           # LED einschalten
          time.sleep(0.5)    # 0.5 Sekunden warten
          led.off()          # LED ausschalten
          time.sleep(0.5)    # 0.5 Sekunden warten
      ```
    - Hinweis: Wenn Sie einen Pico W verwenden, ersetzen Sie `Pin(25, Pin.OUT)` mit `Pin("LED", Pin.OUT)`.

5.  **Das Programm auf dem Pico speichern**:
    - Klicken Sie auf **File > Save As**.
    - Wählen Sie im Dialogfeld **Raspberry Pi Pico** als Ziel (nicht Ihren Computer).
    - Nennen Sie die Datei `main.py` (MicroPython führt `main.py` automatisch beim Start aus) oder geben Sie einen anderen Namen wie `blink.py` ein.
    - Klicken Sie auf **OK**, um die Datei im Dateisystem des Picos zu speichern.

6.  **Das Programm ausführen**:
    - Klicken Sie auf den grünen **Run**-Button (oder drücken Sie **F5**) in Thonny, um das Programm auszuführen.
    - Alternativ, wenn Sie es als `main.py` gespeichert haben, setzen Sie den Pico zurück (ausstecken und wieder einstecken oder die RESET-Taste drücken, falls vorhanden), und das Programm wird automatisch ausgeführt.
    - Sie sollten sehen, wie die onboard-LED alle 0,5 Sekunden blinkt.

7.  **Das Programm anhalten** (falls nötig):
    - Um das Programm zu stoppen, drücken Sie **Strg+C** in Thonnys Shell, um das laufende Skript zu unterbrechen.
    - Um zu verhindern, dass `main.py` automatisch ausgeführt wird, löschen Sie es vom Pico:
      - Gehen Sie in Thonny zu **View > Files**, wählen Sie das Dateisystem des Picos aus, klicken Sie mit der rechten Maustaste auf `main.py` und wählen Sie **Delete**.

---

### Tests und Fehlerbehebung
-   **Keine REPL-Eingabeaufforderung**: Wenn Thonny die MicroPython REPL nicht anzeigt:
    - Stellen Sie sicher, dass der korrekte Port in den Interpreter-Einstellungen ausgewählt ist.
    - Überprüfen Sie, ob MicroPython korrekt geflasht wurde. Wenn nicht, flashen Sie die `.uf2`-Datei erneut, wie zuvor beschrieben.
    - Überprüfen Sie das USB-Kabel (muss Daten unterstützen) und versuchen Sie einen anderen Port.
-   **LED blinkt nicht**: Stellen Sie sicher, dass der korrekte GPIO-Pin verwendet wird (`25` für Pico, `"LED"` für Pico W). Wenn es immer noch nicht funktioniert, testen Sie die LED mit einem einfachen REPL-Befehl:
    ```python
    from machine import Pin
    led = Pin(25, Pin.OUT)
    led.on()
    ```
-   **Datei wird nicht gespeichert**: Stellen Sie sicher, dass Thonny mit dem Pico verbunden ist und der Interpreter auf MicroPython (Raspberry Pi Pico) eingestellt ist.

---

### Zusätzliche Tipps
-   **Verwendung anderer Tools**: Neben Thonny können Sie `rshell` oder `ampy` verwenden, um Dateien auf dem Pico zu verwalten:
    ```bash
    pip install rshell
    rshell --port /dev/ttyACM0
    cp blink.py /pyboard/main.py
    ```
-   **Weitere Beispielprogramme**:
    - Einen Tastendruck lesen (z.B. auf GPIO 14):
      ```python
      from machine import Pin
      button = Pin(14, Pin.IN, Pin.PULL_UP)
      while True:
          print(button.value())
      ```
    - Steuern Sie eine externe LED oder andere Peripheriegeräte, indem Sie die GPIO-Pinnummer anpassen.
-   **Automatischer Start**: Das Speichern einer Datei als `main.py` bewirkt, dass sie automatisch beim Start ausgeführt wird. Verwenden Sie `boot.py` für Setup-Code, der vor `main.py` ausgeführt wird.

Wenn Sie auf spezifische Probleme stoßen (z.B. Port-Erkennung, Fehler in Thonny oder Hardware-Probleme) oder ein anderes Programm ausprobieren möchten, lassen Sie es mich wissen, und ich werde Sie weiter unterstützen!