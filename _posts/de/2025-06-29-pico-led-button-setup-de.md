---
audio: false
generated: true
lang: de
layout: post
title: Raspberry Pi Pico LED-Taster-Konfiguration
translated: true
type: note
---

Um einen Raspberry Pi Pico so einzurichten, dass er den bereitgestellten MicroPython-Code ausführt, welcher eine LED basierend auf einem Tastendruck steuert, folgen Sie diesen Schritten:

### Hardware-Anforderungen
- **Raspberry Pi Pico** (oder Pico W)
- **LED** (mit einem passenden Vorwiderstand, z.B. 220–330 Ohm)
- **Taster**
- **Steckbrücken**
- **Steckbrett** (optional, für einfachere Verbindungen)
- **USB-Kabel** (um den Pico mit Ihrem Computer zu verbinden)

### Hardware-Einrichtung
1. **Schließen Sie die LED an**:
   - Verbinden Sie die Anode (längeres Beinchen) der LED mit **GPIO 25** (physischer Pin 30) am Pico.
   - Verbinden Sie die Kathode (kürzeres Beinchen) der LED über einen 220–330 Ohm Widerstand mit einem **Masse (GND)**-Pin (z.B. physischer Pin 3), um den Strom zu begrenzen.

2. **Schließen Sie den Taster an**:
   - Verbinden Sie eine Seite des Tasters mit **GPIO 14** (physischer Pin 19).
   - Verbinden Sie die andere Seite des Tasters mit einem **3.3V**-Pin (z.B. physischer Pin 36, 3V3(OUT)).
   - Der Code verwendet einen internen Pull-Down-Widerstand (`Pin.PULL_DOWN`), daher ist kein externer Pull-Down-Widerstand erforderlich. Wenn der Taster gedrückt wird, liest GPIO 14 HIGH (1); wenn nicht gedrückt, liest es LOW (0).

3. **Überprüfen Sie die Verbindungen**:
   - Stellen Sie sicher, dass alle Verbindungen sicher sind. Verwenden Sie ein Steckbrett oder direkte Verkabelung und überprüfen Sie doppelt, ob die LED-Polarität korrekt ist und der Widerstand richtig platziert ist.
   - Konsultieren Sie das Pico-Pinout-Diagramm (online oder im Pico-Datenblatt verfügbar), um die Pin-Belegungen zu bestätigen.

### Software-Einrichtung
1. **Installieren Sie MicroPython auf dem Pico**:
   - Laden Sie die neueste MicroPython UF2-Firmware für den Raspberry Pi Pico von der [offiziellen MicroPython-Website](https://micropython.org/download/rp2-pico/) herunter.
   - Verbinden Sie den Pico über ein USB-Kabel mit Ihrem Computer, während Sie die **BOOTSEL**-Taste gedrückt halten.
   - Der Pico erscheint als USB-Laufwerk (RPI-RP2). Ziehen Sie die heruntergeladene `.uf2`-Datei auf dieses Laufwerk.
   - Der Pico startet automatisch neu und hat MicroPython installiert.

2. **Richten Sie eine Entwicklungsumgebung ein**:
   - Installieren Sie eine MicroPython-kompatible IDE, wie z.B. **Thonny** (für Anfänger empfohlen):
     - Laden Sie Thonny von [thonny.org](https://thonny.org) herunter und installieren Sie es.
     - Gehen Sie in Thonny zu **Werkzeuge > Optionen > Interpreter**, wählen Sie **MicroPython (Raspberry Pi Pico)** und wählen Sie den entsprechenden Port (z.B. `COMx` unter Windows oder `/dev/ttyACM0` unter Linux/macOS).
   - Alternativ können Sie Tools wie `rshell`, `ampy` oder Visual Studio Code mit der MicroPython-Erweiterung verwenden.

3. **Laden Sie den Code hoch und führen Sie ihn aus**:
   - Kopieren Sie den bereitgestellten Code in eine Datei namens `main.py`:
     ```python
     from machine import Pin
     import time

     led = Pin(25, Pin.OUT)
     button = Pin(14, Pin.IN, Pin.PULL_DOWN)

     while True:
         if button.value():
             led.on()
         else:
             led.off()
         time.sleep(0.05)
     ```
   - In Thonny:
     - Öffnen Sie eine neue Datei, fügen Sie den Code ein und speichern Sie ihn auf dem Pico als `main.py` (MicroPython führt `main.py` automatisch beim Start aus).
     - Klicken Sie auf die **Ausführen**-Schaltfläche oder drücken Sie **F5**, um den Code hochzuladen und auszuführen.
   - Alternativ verwenden Sie `ampy` zum Hochladen der Datei:
     ```bash
     ampy --port /dev/ttyACM0 put main.py
     ```
     Ersetzen Sie `/dev/ttyACM0` durch den Port Ihres Picos.

4. **Testen Sie das Programm**:
   - Sobald der Code hochgeladen ist, sollte die LED aufleuchten, wenn der Taster gedrückt wird, und erlöschen, wenn er losgelassen wird. Das `time.sleep(0.05)` fügt eine Verzögerung von 50ms hinzu, um den Taster zu entprellen und die CPU-Last zu reduzieren.

### Fehlerbehebung
- **LED leuchtet nicht**:
  - Überprüfen Sie die LED-Polarität (Anode zu GPIO 25, Kathode zu GND über Widerstand).
  - Vergewissern Sie sich, dass der GPIO-Pin (25) mit dem Code und der physischen Verbindung übereinstimmt.
  - Stellen Sie sicher, dass die LED und der Widerstand funktionsfähig sind (testen Sie mit einem Multimeter oder einer anderen Schaltung).
- **Taster funktioniert nicht**:
  - Bestätigen Sie, dass GPIO 14 korrekt angeschlossen ist und der Taster bei Druck mit 3.3V verbindet.
  - Prüfen Sie, ob `Pin.PULL_DOWN` angemessen ist; wenn der Taster anders verdrahtet ist (z.B. an GND), passen Sie den Code an, um `Pin.PULL_UP` zu verwenden, und kehren Sie die Logik um (`if not button.value()`).
- **Code wird nicht ausgeführt**:
  - Stellen Sie sicher, dass MicroPython korrekt installiert ist.
  - Vergewissern Sie sich, dass die Datei als `main.py` auf dem Pico gespeichert ist.
  - Überprüfen Sie die USB-Verbindung und die Port-Einstellungen in Ihrer IDE.

### Hinweise
- Der Code geht davon aus, dass der Taster beim Drücken GPIO 14 mit 3.3V verbindet. Wenn Ihr Taster stattdessen mit GND verbunden ist, modifizieren Sie den Code, um `Pin.PULL_UP` zu verwenden und kehren Sie die Logik um:
  ```python
  button = Pin(14, Pin.IN, Pin.PULL_UP)
  while True:
      if not button.value():  # Taster gedrückt = LOW
          led.on()
      else:
          led.off()
      time.sleep(0.05)
  ```
- Wenn Sie Tasterprellen bemerken (flackernde LED), erhöhen Sie den `time.sleep`-Wert oder implementieren Sie eine Software-Entprellung.
- Für einen Pico W ist der Aufbau identisch, aber stellen Sie sicher, dass Sie die korrekten GPIO-Pins verwenden, da das Pinout gleich ist.

Wenn Sie weitere Erklärungen oder Hilfe mit spezifischen Problemen benötigen, lassen Sie es mich wissen!