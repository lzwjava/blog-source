---
audio: false
generated: true
lang: de
layout: post
title: 'Einführung in den Raspberry Pi Pico: Ein vielseitiger Mikrocontroller'
translated: true
type: note
---

Der **Raspberry Pi Pico** ist eine vielseitige, kostengünstige Mikrocontroller-Platine, die von der Raspberry Pi Foundation entwickelt wurde und für Embedded Systems, Prototyping und DIY-Elektronikprojekte konzipiert ist. Im Gegensatz zu den Einplatinencomputern (SBCs) wie dem Raspberry Pi 4 ist der Pico ein Mikrocontroller, was bedeutet, dass er für die Steuerung von Hardware, das Ausführen von schlanken Programmen und die Kommunikation mit Sensoren, Motoren und anderen Komponenten optimiert ist. Er wurde im Januar 2021 eingeführt und markierte den Einstieg der Foundation in den Mikrocontrollermarkt, indem er eine erschwingliche und dennoch leistungsstarke Plattform für Hobbyisten, Pädagogen und Profis bot.

Nachfolgend finden Sie eine umfassende Einführung in den Raspberry Pi Pico, die seine Merkmale, Spezifikationen, Programmiermöglichkeiten, Anwendungen und mehr abdeckt.

---

### **Überblick**
Der Raspberry Pi Pico basiert auf dem **RP2040**, einem speziell von der Raspberry Pi Foundation entwickelten Mikrocontroller-Chip. Zum Preis von etwa 4 US-Dollar konkurriert er mit Plattformen wie Arduino und ESP32, zeichnet sich jedoch durch seine hohe Leistung, niedrige Kosten und umfangreiche Community-Unterstützung aus. Der Pico ist kompakt (nur 51 mm x 21 mm) und wurde sowohl für Anfänger als auch für fortgeschrittene Benutzer entwickelt, die an Projekten arbeiten, die vom einfachen Blinken einer LED bis hin zu komplexen IoT- und Robotikanwendungen reichen.

---

### **Hauptmerkmale**
1.  **RP2040 Mikrocontroller**:
    *   Dual-Core-**Arm Cortex-M0+**-Prozessor mit bis zu **133 MHz** (übertaktbar).
    *   **264 KB SRAM** und **2 MB On-Board-QSPI-Flash-Speicher** für die Programmspeicherung.
    *   Geringer Stromverbrauch mit Schlaf- und Ruhemodi für batteriebetriebene Anwendungen.
    *   Flexible Taktkonfiguration zur Leistungsoptimierung.

2.  **GPIO-Pins**:
    *   26 multifunktionale **General Purpose Input/Output (GPIO)**-Pins.
    *   Unterstützt **I2C**, **SPI**, **UART** und **PWM**-Schnittstellen zum Anschluss von Peripheriegeräten.
    *   2x UART, 2x SPI-Controller, 2x I2C-Controller und 16x PWM-Kanäle.
    *   3x 12-Bit-Analog-Digital-Wandler (ADC) für analoge Sensoreingänge.
    *   8x programmierbare I/O (PIO)-Blöcke für benutzerdefinierte Protokolle (z. B. WS2812-LED-Steuerung, VGA-Ausgabe).

3.  **Stromversorgung und Konnektivität**:
    *   Stromversorgung über **USB Micro-B** (5V) oder externe Stromquelle (1,8–5,5 V).
    *   **3,3-V-Logikpegel** für die GPIO-Pins.
    *   Integrierter **Temperatursensor** auf dem RP2040.
    *   USB-1.1-Controller für Geräte- und Host-Modi (wird für Programmierung und Debugging verwendet).

4.  **Physikalische Bauform**:
    *   Kompakte Abmessungen: 51 mm x 21 mm.
    *   40-polige DIP-Bauweise mit **abgesetzten Kanten** (castellated edges), die das direkte Auflöten auf eine Leiterplatte oder die Verwendung mit einem Steckbrett ermöglicht.
    *   Einseitige Bauteilplatzierung für einfaches Löten.

5.  **Geringe Kosten**:
    *   Preis von etwa 4 US-Dollar, was ihn zu einem der erschwinglichsten Mikrocontroller auf dem Markt macht.

---

### **Varianten**
Seit seiner Einführung haben die Raspberry Pi Foundation und Partner Varianten des Pico veröffentlicht:
*   **Raspberry Pi Pico W** (2022): Fügt **Wi-Fi** (2,4 GHz 802.11n) und **Bluetooth 5.2** über einen Infineon CYW43439-Chip hinzu und ermöglicht so drahtlose IoT-Anwendungen. Preis bei etwa 6 US-Dollar.
*   **Raspberry Pi Pico H**: Beinhaltet einen vorverlöteten 40-poligen Header für einfacheres Prototyping.
*   **Raspberry Pi Pico WH**: Kombiniert die drahtlosen Fähigkeiten des Pico W mit vorverlöteten Headern.
*   **Pico 2** (2024): Enthält den **RP2350**-Mikrocontroller, eine verbesserte Version des RP2040 mit Dual-**Arm Cortex-M33**- oder **RISC-V Hazard3**-Kernen (benutzerwählbar), 520 KB SRAM, verbesserter Energieeffizienz und erweiterten Sicherheitsfunktionen (z. B. Arm TrustZone, SHA-256-Beschleunigung).

---

### **Programmierung des Raspberry Pi Pico**
Der Pico unterstützt mehrere Programmiersprachen und Umgebungen, was ihn für ein breites Benutzerspektrum zugänglich macht:

1.  **MicroPython**:
    *   Die beliebteste Wahl für Anfänger und Rapid Prototyping.
    *   Offizielle MicroPython-Firmware von der Raspberry Pi Foundation.
    *   Unterstützt Bibliotheken für GPIO, I2C, SPI, PWM, ADC und PIO.
    *   Interaktive REPL (Read-Eval-Print Loop) über USB für Echtzeit-Coding.

2.  **C/C++**:
    *   Bietet vollständige Kontrolle über die Funktionen des RP2040 mit dem offiziellen **Pico SDK** (Software Development Kit).
    *   Geeignet für leistungskritische Anwendungen und Low-Level-Hardware-Steuerung.
    *   Unterstützt erweiterte Funktionen wie PIO-Programmierung und Multi-Core-Verarbeitung.
    *   Werkzeuge wie CMake und GCC werden für die Kompilierung verwendet.

3.  **Andere Sprachen**:
    *   **CircuitPython**: Ein Fork von MicroPython von Adafruit, optimiert für Bildung und Benutzerfreundlichkeit.
    *   **Rust**: Community-gestützte Unterstützung für die Rust-Programmierung auf dem RP2040.
    *   **Arduino**: Der Pico kann mit der Arduino IDE unter Verwendung des offiziellen RP2040-Board-Pakets programmiert werden.
    *   Experimentelle Unterstützung für andere Sprachen wie JavaScript (über Espruino) und Lua.

4.  **Entwicklungswerkzeuge**:
    *   **Drag-and-Drop-Programmierung**: Laden Sie MicroPython- oder CircuitPython-.uf2-Firmware-Dateien per USB hoch, indem Sie die BOOTSEL-Taste gedrückt halten.
    *   **Debugging**: Unterstützt SWD (Serial Wire Debug) für erweitertes Debugging mit Werkzeugen wie einem Raspberry Pi Debug Probe.
    *   Integrierte Entwicklungsumgebungen wie **Thonny** (für Python) und **Visual Studio Code** (für C/C++) werden häufig verwendet.

---

### **Anwendungen**
Die Flexibilität des Raspberry Pi Pico macht ihn für eine Vielzahl von Projekten geeignet, darunter:
*   **Prototyping und Bildung**: Ideal zum Erlernen von Embedded Systems, Programmierung und Elektronik.
*   **IoT-Projekte**: Mit dem Pico W können Benutzer WLAN-fähige Geräte wie Smart-Home-Controller oder Wetterstationen erstellen.
*   **Robotik**: Steuerung von Motoren, Servos und Sensoren für robotische Anwendungen.
*   **Benutzerdefinierte Schnittstellen**: Verwenden Sie PIO, um Protokolle wie WS2812 (NeoPixel)-LED-Steuerung, VGA- oder DVI-Ausgabe zu implementieren.
*   **Datenprotokollierung**: Kommunikation mit Sensoren (z. B. Temperatur, Luftfeuchtigkeit, Licht) zur Umweltüberwachung.
*   **Wearables und Embedded Systems**: Kompakte Größe und geringer Stromverbrauch eignen sich für Wearable Technology und batteriebetriebene Geräte.

---

### **Ökosystem und Community**
Der Raspberry Pi Pico profitiert von einem robusten Ökosystem:
*   **Offizielle Dokumentation**: Die Raspberry Pi Foundation bietet detaillierte Anleitungen, einschließlich der *Pico Getting Started*-Anleitung, des RP2040-Datenblatts und Hardware-Design-Dateien.
*   **Community-Unterstützung**: Eine große Community auf Plattformen wie X, Reddit und in den Raspberry Pi-Foren teilt Projekte, Tutorials und Tipps zur Fehlerbehebung.
*   **Drittanbieter-Zubehör**: Zahlreiche Add-Ons sind erhältlich, wie Sensor-Breakout-Boards, Displays und Shields von Unternehmen wie Adafruit, SparkFun und Pimoroni.
*   **Open-Source-Hardware**: Das Design des RP2040 ist gut dokumentiert und fördert die Entwicklung benutzerdefinierter Boards.

---

### **Vergleich mit Alternativen**
*   **Arduino**: Der Pico ist schneller (Dual-Core, 133 MHz vs. 16 MHz des Arduino Uno) und günstiger, mit mehr GPIO und erweiterten Funktionen wie PIO. Allerdings hat Arduino ein größeres Ökosystem an Shields und Bibliotheken.
*   **ESP32**: Der ESP32 bietet integriertes Wi-Fi und Bluetooth, aber der Pico W bietet dies zu geringeren Kosten. Der PIO des Pico ist einzigartig für benutzerdefinierte Protokolle.
*   **STM32**: Der Pico ist für Anfänger einfacher zu programmieren (z. B. mit MicroPython) und erschwinglicher als viele STM32-Boards.

---

### **Einschränkungen**
*   **Kein integriertes Wireless (Basismodell)**: Dem ursprünglichen Pico fehlen Wi-Fi/Bluetooth, obwohl der Pico W dies adressiert.
*   **Begrenzter On-Board-Speicher**: 2 MB Flash sind für die meisten Projekte ausreichend, können aber komplexe Anwendungen einschränken.
*   **3,3-V-Logik**: Erfordert Pegelwandler für 5-V-Peripheriegeräte.
*   **Kein integrierter Reset-Knopf**: Eine kleine Unannehmlichkeit für einige Benutzer.

---

### **Erste Schritte**
So beginnen Sie mit dem Raspberry Pi Pico:
1.  **Hardware-Einrichtung**: Schließen Sie den Pico über USB an einen Computer an oder versorgen Sie ihn extern mit Strom.
2.  **Firmware installieren**: Laden Sie die MicroPython- oder CircuitPython-Firmware von der Raspberry- Pi-Website oder Adafruit herunter und übertragen Sie sie, indem Sie BOOTSEL gedrückt halten und den Pico anschließen.
3.  **Programmierung**: Verwenden Sie Thonny für Python oder richten Sie das Pico SDK für die C/C++-Entwicklung ein.
4.  **Projekte**: Beginnen Sie mit einfachen Projekten wie dem Blinken einer LED oder dem Auslesen eines Sensors und erkunden Sie dann erweiterte Anwendungen wie IoT oder Robotik.

---

### **Schlussfolgerung**
Der Raspberry Pi Pico ist ein leistungsstarker, erschwinglicher und anfängerfreundlicher Mikrocontroller, der die Entwicklung eingebetteter Systeme demokratisiert hat. Sein maßgeschneiderter RP2040-Chip, seine umfangreichen GPIO-Fähigkeiten und die Unterstützung mehrerer Programmiersprachen machen ihn zur ersten Wahl für Hobbyisten, Pädagogen und Profis. Mit Varianten wie dem Pico W und Pico 2 entwickelt er sich weiter und bietet drahtlose Konnektivität und verbesserte Leistung für moderne Anwendungen. Unterstützt durch die exzellente Dokumentation der Raspberry Pi Foundation und eine lebendige Community ist der Pico eine ideale Plattform zum Lernen, Prototyping und Umsetzen innovativer Projekte.

Wenn Sie spezielle Details zur Programmierung des Pico, Projektideen oder Vergleiche mit anderen Mikrocontrollern wünschen, lassen Sie es mich wissen!