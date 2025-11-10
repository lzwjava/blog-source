---
audio: false
generated: true
lang: de
layout: post
title: Einrichten des Raspberry Pi Pico auf Ubuntu
translated: true
type: note
---

Um einen **Raspberry Pi Pico** auf **Ubuntu** zu verwenden, müssen Sie die Entwicklungsumgebung einrichten, die notwendige Software installieren und Tools konfigurieren, um den Pico zu programmieren. Der Pico unterstützt die Programmierung in **MicroPython**, **C/C++** oder **CircuitPython**. Im Folgenden skizziere ich die Schritte und die erforderliche Software für jeden Ansatz, wobei der Schwerpunkt auf den gängigsten Setups liegt.

### Allgemeine Voraussetzungen
- **Raspberry Pi Pico** (oder Pico W) mit einem USB-Kabel (Micro-USB für Pico, USB-C für Pico 2).
- **Ubuntu**-System (z.B. Ubuntu 20.04, 22.04 oder später; diese Anweisungen gehen von einer aktuellen Version wie 24.04 aus).
- Grundlegende Vertrautheit mit dem Terminal.

### Option 1: Programmierung mit MicroPython
MicroPython ist die einsteigerfreundlichste Methode, um den Pico zu programmieren. Es ist eine schlanke Python-Implementierung, die für Mikrocontroller entwickelt wurde.

#### Zu installierende Software
1. **MicroPython-Firmware**
   - Laden Sie die neueste MicroPython UF2-Firmware-Datei für den Raspberry Pi Pico von der [offiziellen MicroPython-Website](https://micropython.org/download/rp2-pico/) oder von der [Raspberry Pi Pico-Seite](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html) herunter.
   - Für Pico W oder Pico 2 stellen Sie sicher, dass Sie die entsprechende Firmware auswählen (z.B. `rp2-pico-w` für Pico W).

2. **Python 3**
   - Ubuntu enthält typischerweise standardmäßig Python 3. Überprüfen Sie dies mit:
     ```bash
     python3 --version
     ```
   - Falls nicht installiert, installieren Sie es:
     ```bash
     sudo apt update
     sudo apt install python3 python3-pip
     ```

3. **Thonny IDE** (Empfohlen für Anfänger)
   - Thonny ist eine einfache IDE zum Programmieren des Pico mit MicroPython.
   - Installieren Sie Thonny:
     ```bash
     sudo apt install thonny
     ```
   - Alternativ können Sie `pip` für die neueste Version verwenden:
     ```bash
     pip3 install thonny
     ```

4. **Optional: `picotool` (für erweitertes Management)**
   - Nützlich zum Verwalten der MicroPython-Firmware oder zum Inspizieren des Pico.
   - Installieren Sie `picotool`:
     ```bash
     sudo apt install picotool
     ```

#### Einrichtungsschritte
1. **MicroPython-Firmware installieren**
   - Verbinden Sie den Pico über USB mit Ihrem Ubuntu-Rechner, während Sie die **BOOTSEL**-Taste gedrückt halten (dies versetzt den Pico in den Bootloader-Modus).
   - Der Pico erscheint als USB-Speichergerät (z.B. `RPI-RP2`).
   - Ziehen Sie die heruntergeladene MicroPython `.uf2`-Datei per Drag & Drop auf den Speicher des Pico. Der Pico startet automatisch neu und hat MicroPython installiert.

2. **Thonny konfigurieren**
   - Öffnen Sie Thonny: `thonny` im Terminal oder über das Anwendungsmenü.
   - Gehen Sie zu **Tools > Options > Interpreter**.
   - Wählen Sie **MicroPython (Raspberry Pi Pico)** als Interpreter.
   - Wählen Sie den korrekten Port (z.B. `/dev/ttyACM0`). Führen Sie `ls /dev/tty*` im Terminal aus, um den Port bei Bedarf zu identifizieren.
   - Thonny sollte nun eine Verbindung zum Pico herstellen, sodass Sie Python-Skripte schreiben und ausführen können.

3. **Ein Programm testen**
   - Schreiben Sie in Thonny ein einfaches Skript, z.B.:
     ```python
     from machine import Pin
     led = Pin(25, Pin.OUT)  # Onboard-LED (GP25 für Pico)
     led.toggle()  # LED ein-/ausschalten
     ```
   - Klicken Sie auf die **Run**-Schaltfläche, um den Code auf dem Pico auszuführen.

4. **Optional: `picotool` verwenden**
   - Überprüfen Sie den Status des Pico:
     ```bash
     picotool info
     ```
   - Stellen Sie sicher, dass der Pico verbunden und bei Bedarf im Bootloader-Modus ist.

### Option 2: Programmierung mit C/C++
Für fortgeschrittene Benutzer kann der Pico in C/C++ mit dem offiziellen **Pico SDK** programmiert werden.

#### Zu installierende Software
1. **Pico SDK und Toolchain**
   - Installieren Sie die erforderlichen Tools zum Erstellen von C/C++-Programmen:
     ```bash
     sudo apt update
     sudo apt install cmake gcc-arm-none-eabi libnewlib-arm-none-eabi build-essential git
     ```

2. **Pico SDK**
   - Klonen Sie das Pico SDK-Repository:
     ```bash
     git clone -b master https://github.com/raspberrypi/pico-sdk.git
     cd pico-sdk
     git submodule update --init
     ```
   - Setzen Sie die `PICO_SDK_PATH`-Umgebungsvariable:
     ```bash
     export PICO_SDK_PATH=~/pico-sdk
     echo 'export PICO_SDK_PATH=~/pico-sdk' >> ~/.bashrc
     ```

3. **Optional: Pico Examples**
   - Klonen Sie die Pico-Beispiele zur Referenz:
     ```bash
     git clone -b master https://github.com/raspberrypi/pico-examples.git
     ```

4. **Visual Studio Code (Optional)**
   - Für eine bessere Entwicklungserfahrung installieren Sie VS Code:
     ```bash
     sudo snap install code --classic
     ```
   - Installieren Sie die **CMake Tools** und **C/C++**-Erweiterungen in VS Code.

#### Einrichtungsschritte
1. **Ein Projekt einrichten**
   - Erstellen Sie ein neues Verzeichnis für Ihr Projekt, z.B. `my-pico-project`.
   - Kopieren Sie eine Beispiel-`CMakeLists.txt` aus `pico-examples` oder erstellen Sie eine:
     ```cmake
     cmake_minimum_required(VERSION 3.13)
     include($ENV{PICO_SDK_PATH}/pico_sdk_init.cmake)
     project(my_project C CXX ASM)
     pico_sdk_init()
     add_executable(my_project main.c)
     pico_add_extra_outputs(my_project)
     target_link_libraries(my_project pico_stdlib)
     ```
   - Schreiben Sie ein einfaches C-Programm (z.B. `main.c`):
     ```c
     #include "pico/stdlib.h"
     int main() {
         const uint LED_PIN = 25;
         gpio_init(LED_PIN);
         gpio_set_dir(LED_PIN, GPIO_OUT);
         while (true) {
             gpio_put(LED_PIN, 1);
             sleep_ms(500);
             gpio_put(LED_PIN, 0);
             sleep_ms(500);
         }
     }
     ```

2. **Bauen und Flashen**
   - Wechseln Sie in Ihr Projektverzeichnis:
     ```bash
     cd my-pico-project
     mkdir build && cd build
     cmake ..
     make
     ```
   - Dies generiert eine `.uf2`-Datei (z.B. `my_project.uf2`).
   - Halten Sie die **BOOTSEL**-Taste auf dem Pico gedrückt, verbinden Sie ihn via USB und kopieren Sie die `.uf2`-Datei auf den Speicher des Pico:
     ```bash
     cp my_project.uf2 /media/$USER/RPI-RP2/
     ```

3. **Debugging (Optional)**
   - Installieren Sie `openocd` für das Debugging:
     ```bash
     sudo apt install openocd
     ```
   - Verwenden Sie einen Debugger (z.B. einen anderen Pico als Debug-Probe) und führen Sie aus:
     ```bash
     openocd -f interface/raspberrypi-swd.cfg -f target/rp2040.cfg
     ```

### Option 3: Programmierung mit CircuitPython
CircuitPython ist eine weitere Python-basierte Option, ähnlich wie MicroPython, jedoch mit Fokus auf Adafruits Ecosystem.

#### Zu installierende Software
1. **CircuitPython-Firmware**
   - Laden Sie die CircuitPython UF2-Datei für den Pico von der [Adafruit CircuitPython-Website](https://circuitpython.org/board/raspberry_pi_pico/) herunter.
   - Für Pico W oder Pico 2 wählen Sie die entsprechende Firmware.

2. **Python 3 und Tools**
   - Gleich wie für MicroPython (Python 3, Thonny, etc.).

#### Einrichtungsschritte
1. **CircuitPython-Firmware installieren**
   - Ähnlich wie bei MicroPython: Halten Sie **BOOTSEL** gedrückt, verbinden Sie den Pico und kopieren Sie die CircuitPython `.uf2`-Datei auf den Speicher des Pico.
   - Der Pico startet neu als USB-Laufwerk mit dem Namen `CIRCUITPY`.

2. **Programmieren mit Thonny oder einem Texteditor**
   - Verwenden Sie Thonny wie im MicroPython-Abschnitt beschrieben und wählen Sie **CircuitPython** als Interpreter.
   - Alternativ können Sie `code.py` direkt auf dem `CIRCUITPY`-Laufwerk mit einem beliebigen Texteditor bearbeiten.
   - Beispiel `code.py`:
     ```python
     import board
     import digitalio
     import time
     led = digitalio.DigitalInOut(board.LED)
     led.direction = digitalio.Direction.OUTPUT
     while True:
         led.value = True
         time.sleep(0.5)
         led.value = False
         time.sleep(0.5)
     ```

### Zusätzliche Hinweise
- **Berechtigungen**: Wenn der Port des Pico (z.B. `/dev/ttyACM0`) nicht zugänglich ist, fügen Sie Ihren Benutzer zur `dialout`-Gruppe hinzu:
  ```bash
  sudo usermod -a -G dialout $USER
  ```
  Melden Sie sich ab und wieder an, um die Änderung zu übernehmen.

- **Pico W Überlegungen**: Für den Pico W stellen Sie sicher, dass Sie eine spezifische Firmware dafür verwenden (z.B. MicroPython mit Wi-Fi-Unterstützung). Die Wi-Fi-Programmierung erfordert zusätzliche Bibliotheken, wie `network` für MicroPython.

- **Pico 2**: Der neuere Raspberry Pi Pico 2 (mit RP2350) erfordert möglicherweise aktualisierte Firmware- oder SDK-Versionen. Überprüfen Sie die offizielle Raspberry Pi-Dokumentation auf Kompatibilität.

- **Fehlerbehebung**:
  - Wenn der Pico nicht im Bootloader-Modus erscheint, überprüfen Sie das USB-Kabel (es muss Daten unterstützen, nicht nur Strom).
  - Führen Sie `lsusb` oder `dmesg` aus, um zu bestätigen, dass der Pico von Ubuntu erkannt wird.
  - Stellen Sie bei C/C++-Builds sicher, dass der Pico SDK-Pfad korrekt gesetzt ist.

### Empfohlener Ansatz
- Für **Anfänger**: Verwenden Sie **MicroPython mit Thonny** wegen der Einfachheit und des schnellen Setups.
- Für **fortgeschrittene Benutzer**: Verwenden Sie **C/C++ mit dem Pico SDK** für Leistung und Low-Level-Kontrolle.
- Für **Benutzer des Adafruit-Ecosystems**: Verwenden Sie **CircuitPython**, wenn Sie Adafruit-Bibliotheken oder -Hardware verwenden möchten.

Wenn Sie ein bestimmtes Projekt oder eine Programmierpräferenz haben, lassen Sie es mich wissen, und ich kann die Anweisungen weiter anpassen!