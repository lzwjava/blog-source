---
audio: false
generated: true
lang: de
layout: post
title: 'MicroPython: Python für Mikrocontroller'
translated: true
type: note
---

MicroPython ist eine schlanke und effiziente Implementierung der Programmiersprache Python 3, die für Mikrocontroller, eingebettete Systeme und ressourcenbeschränkte Umgebungen optimiert ist. Es bringt die Einfachheit und Vielseitigkeit von Python in die Hardware-Programmierung und ermöglicht Entwicklern das Schreiben von Code für kleine Geräte mit begrenztem Speicher und Rechenleistung. Nachfolgend finden Sie eine umfassende Einführung in MicroPython, die seine Entstehung, Funktionen, Anwendungen und mehr abdeckt.

### 1. **Was ist MicroPython?**
MicroPython ist eine leichtgewichtige, Open-Source-Version von Python 3, die für die Ausführung auf Mikrocontrollern und eingebetteten Geräten entwickelt wurde. Es behält die meiste Syntax und Kernfunktionalität von Python bei, ist jedoch für Umgebungen mit nur 16 KB RAM und 256 KB Speicher angepasst. MicroPython wurde 2013 von Damien George entwickelt, um die eingebettete Programmierung zugänglicher zu machen und dabei auf die lesbare Syntax von Python statt auf Low-Level-Sprachen wie C oder Assembler zurückzugreifen.

Im Gegensatz zu Standard-Python, das auf Allzweckcomputern mit reichlich Ressourcen läuft, ist MicroPython hochoptimiert, um innerhalb der Einschränkungen von Mikrocontrollern zu arbeiten, wie sie in IoT-Geräten, Sensoren, Robotik und anderen eingebetteten Systemen zu finden sind. Es enthält einen kompakten Interpreter, einen Teil der Python-Standardbibliothek und hardware-spezifische Module für die Interaktion mit Peripheriegeräten wie GPIO-Pins, I2C, SPI, UART und PWM.

### 2. **Hauptmerkmale von MicroPython**
MicroPython kombiniert die Benutzerfreundlichkeit von Python mit Funktionen für eingebettete Systeme:
- **Python 3 Syntax**: Unterstützt die meiste Python 3-Syntax, einschließlich Funktionen, Klassen, Listen, Dictionaries und Ausnahmebehandlung, was es Python-Entwicklern vertraut macht.
- **Kleiner Footprint**: Optimiert für die Ausführung auf Geräten mit minimalem RAM (bis zu 16 KB) und Speicher (bis zu 256 KB).
- **Interaktive REPL**: Bietet eine Read-Eval-Print Loop (REPL) für Echtzeit-Coding und Debugging direkt auf der Hardware über eine serielle Verbindung oder USB.
- **Hardware-spezifische Module**: Enthält Bibliotheken wie `machine` und `micropython` zur Steuerung von Hardware-Komponenten (z.B. GPIO, ADC, Timer und Kommunikationsprotokolle).
- **Dateisystem-Unterstützung**: Viele MicroPython-Ports enthalten ein kleines Dateisystem zum Speichern von Skripten und Daten auf Flash-Speicher oder SD-Karten.
- **Cross-Platform**: Verfügbar für eine Vielzahl von Mikrocontrollern, einschließlich ESP8266, ESP32, STM32, Raspberry Pi Pico und anderen.
- **Erweiterbar**: Unterstützt benutzerdefinierte Module und ermöglicht die Integration mit C/C++ für leistungskritische Aufgaben.
- **Niedriger Energieverbrauch**: Optimiert für Energieeffizienz, geeignet für batteriebetriebene IoT-Geräte.
- **Open Source**: Lizenziert unter der MIT-Lizenz, ist MicroPython frei zu verwenden, zu modifizieren und zu verteilen.

### 3. **Geschichte und Entwicklung**
MicroPython wurde vom australischen Physiker und Programmierer Damien George durch eine erfolgreiche Kickstarter-Kampagne im Jahr 2013 ins Leben gerufen. Das Ziel war es, die Einfachheit von Python auf Mikrocontroller zu bringen und die eingebettete Programmierung für Hobbyisten, Pädagogen und Profis zugänglicher zu machen. Das erste stabile Release erschien 2014 und zielte auf die PyBoard, einen Mikrocontroller-Board, der speziell für MicroPython entwickelt wurde.

Seitdem ist die MicroPython-Community gewachsen, mit Beiträgen von Entwicklern weltweit. Es unterstützt nun zahlreiche Mikrocontroller-Plattformen, und sein Ökosystem umfasst Tools, Bibliotheken und Dokumentation. Das Projekt wird aktiv gepflegt, mit regelmäßigen Updates zur Verbesserung der Leistung, Hinzufügung von Funktionen und Unterstützung neuer Hardware.

### 4. **Wie MicroPython funktioniert**
MicroPython besteht aus zwei Hauptkomponenten:
- **Interpreter**: Ein kompakter Python 3-Interpreter, der Python-Code auf dem Mikrocontroller ausführt. Er kompiliert Python-Skripte in Bytecode, der dann auf einer schlanken virtuellen Maschine ausgeführt wird.
- **Laufzeitumgebung und Bibliotheken**: Die Laufzeitumgebung bietet Kernfunktionalität von Python und enthält hardware-spezifische Module für die Interaktion mit der Peripherie des Mikrocontrollers.

Wenn ein MicroPython-Skript läuft, kann es:
- Hardware direkt steuern (z.B. eine LED einschalten, einen Sensor auslesen).
- Über Protokolle wie I2C, SPI oder MQTT kommunizieren.
- Skripte aus dem Dateisystem des Geräts speichern und ausführen.
- Mit der REPL für Live-Debugging oder Befehlsausführung interagieren.

MicroPython-Firmware ist auf spezifische Mikrocontroller-Architekturen zugeschnitten (z.B. ARM Cortex-M, ESP32). Benutzer flashen die Firmware auf das Gerät und laden dann Python-Skripte über Tools wie `ampy`, `rshell` oder integrierte Entwicklungsumgebungen (IDEs) wie Thonny oder Mu hoch.

### 5. **Unterstützte Hardware**
MicroPython läuft auf einer Vielzahl von Mikrocontroller-Plattformen, darunter:
- **ESP8266 und ESP32**: Beliebt für IoT- und Wi-Fi-fähige Projekte aufgrund ihrer geringen Kosten und Netzwerkfähigkeiten.
- **Raspberry Pi Pico (RP2040)**: Ein vielseitiges, kostengünstiges Board mit Dual-Core ARM Cortex-M0+.
- **STM32 Serie**: Verwendet in industriellen und leistungsstarken eingebetteten Anwendungen.
- **PyBoard**: Das ursprüngliche MicroPython-Board, entwickelt für Entwicklung und Prototyping.
- **Andere**: Enthält Boards wie BBC micro:bit, Arduino und verschiedene ARM-basierte Mikrocontroller.

Jede Plattform hat einen spezifischen Firmware-Build, optimiert für ihre Hardware-Features. Zum Beispiel enthält ESP32-Firmware Wi-Fi- und Bluetooth-Unterstützung, während STM32-Firmware erweiterte Peripherie wie CAN-Bus unterstützt.

### 6. **Anwendungen von MicroPython**
Die Vielseitigkeit von MicroPython macht es für ein breites Anwendungsspektrum geeignet:
- **Internet of Things (IoT)**: Bau intelligenter Geräte, die über Wi-Fi oder Bluetooth mit dem Internet verbunden sind (z.B. Hausautomation, Wetterstationen).
- **Robotik**: Steuerung von Motoren, Sensoren und Aktuatoren in Robotersystemen.
- **Bildung**: Unterricht in Programmierung und Elektronik aufgrund seiner Einfachheit und Interaktivität.
- **Prototyping**: Schnelle Entwicklung eingebetteter Systeme für Proof-of-Concept-Projekte.
- **Wearables**: Betrieb kleiner, batteriebetriebener Geräte wie Smartwatches oder Fitness-Tracker.
- **Sensornetzwerke**: Sammeln und Verarbeiten von Daten von Umgebungssensoren.
- **Hausautomation**: Steuerung von Lichtern, Geräten oder Sicherheitssystemen.

### 7. **Vorteile von MicroPython**
- **Einfache Bedienung**: Die lesbare Syntax von Python senkt die Einstiegshürde für die eingebettete Programmierung im Vergleich zu C/C++.
- **Schnelle Entwicklung**: Die REPL und High-Level-Abstraktionen beschleunigen Prototyping und Debugging.
- **Community und Ökosystem**: Eine wachsende Community bietet Bibliotheken, Tutorials und Support.
- **Portabilität**: Code, der für eine MicroPython-Plattform geschrieben wurde, kann oft mit minimalen Änderungen auf anderen wiederverwendet werden.
- **Flexibilität**: Geeignet für sowohl Anfänger als auch fortgeschrittene Entwickler.

### 8. **Einschränkungen von MicroPython**
- **Ressourcenbeschränkungen**: Begrenzter Speicher und Rechenleistung schränken die Komplexität von Anwendungen im Vergleich zu Standard-Python ein.
- **Leistung**: Langsamer als C/C++ für zeitkritische Aufgaben aufgrund der interpretierten Natur von Python.
- **Teilmenge von Python**: Nicht alle Python-Bibliotheken (z.B. NumPy, Pandas) sind aufgrund von Ressourcenbeschränkungen verfügbar.
- **Firmware-Management**: Erfordert das Flashen spezifischer Firmware für jeden Mikrocontroller, was für Anfänger komplex sein kann.

### 9. **MicroPython vs. Andere Eingebettete Programmierung**
- **MicroPython vs. C/C++ (Arduino)**: MicroPython ist einfacher zu lernen und schneller zu prototypisieren, aber weniger leistungsstark für Low-Level-, Hochgeschwindigkeitsaufgaben.
- **MicroPython vs. CircuitPython**: CircuitPython, ein Fork von MicroPython von Adafruit, ist anfängerfreundlicher und auf USB-Konnektivität fokussiert, hat aber ein kleineres Hardware-Ökosystem.
- **MicroPython vs. Lua (NodeMCU)**: MicroPython bietet eine vertrautere Programmiersprache für Python-Entwickler und breitere Bibliotheksunterstützung.

### 10. **Erste Schritte mit MicroPython**
Um mit MicroPython zu beginnen:
1. **Wählen Sie ein kompatibles Board**: Beliebte Optionen sind ESP32, Raspberry Pi Pico oder PyBoard.
2. **Firmware herunterladen**: Holen Sie sich die MicroPython-Firmware für Ihr Board von der offiziellen MicroPython-Website (micropython.org).
3. **Firmware flashen**: Verwenden Sie Tools wie `esptool.py` oder das Flashing-Utility des Boards, um MicroPython zu installieren.
4. **Code schreiben und hochladen**: Verwenden Sie eine IDE wie Thonny oder ein Tool wie `ampy`, um Python-Skripte auf das Gerät zu übertragen.
5. **Mit der REPL experimentieren**: Verbinden Sie sich mit dem Board über ein serielles Terminal (z.B. PuTTY, screen), um mit der REPL zu interagieren.
6. **Bibliotheken erkunden**: Verwenden Sie Module wie `machine`, `network` und `utime`, um Hardware zu steuern und Funktionalität zu implementieren.

### 11. **Ökosystem und Community**
MicroPython hat eine lebendige Community mit Ressourcen wie:
- **Offizielle Dokumentation**: Umfassende Anleitungen und API-Referenzen unter docs.micropython.org.
- **Foren und Gruppen**: Aktive Diskussionen im MicroPython-Forum, Reddit und X (suche nach #MicroPython).
- **Tutorials und Projekte**: Zahlreiche Tutorials auf Plattformen wie YouTube, Hackster.io und Community-Blogs.
- **Bibliotheken**: Community-beigetragene Bibliotheken für Sensoren, Displays und Kommunikationsprotokolle.

### 12. **Zukunft von MicroPython**
MicroPython entwickelt sich weiter mit:
- Unterstützung für neue Mikrocontroller und Features (z.B. Bluetooth Low Energy, erweiterte Netzwerke).
- Integration mit IoT-Frameworks wie MQTT und Home Assistant.
- Verbesserungen in Leistung und Speicheroptimierung.
- Wachsender Akzeptanz in Bildung und Industrie für schnelles Prototyping und IoT-Entwicklung.

### 13. **Beispielcode**
Hier ist ein einfaches MicroPython-Skript, um eine LED auf einem Raspberry Pi Pico blinken zu lassen:
```python
from machine import Pin
import utime

led = Pin(25, Pin.OUT)  # Onboard LED on Pico
while True:
    led.toggle()
    utime.sleep(0.5)  # Blink every 0.5 seconds
```

### 14. **Schlussfolgerung**
MicroPython ist ein leistungsstarkes und zugängliches Werkzeug für die eingebettete Programmierung, das die Lücke zwischen High-Level-Python-Entwicklung und Low-Level-Hardware-Steuerung schließt. Sein leichtgewichtiges Design, die Python-Syntax und die umfangreiche Hardware-Unterstützung machen es ideal für IoT, Robotik, Bildung und Prototyping. Obwohl es im Vergleich zu Standard-Python oder C Einschränkungen in Leistung und Bibliotheksunterstützung hat, machen seine Benutzerfreundlichkeit und schnellen Entwicklungsmöglichkeiten es zu einer ersten Wahl für Hobbyisten und Profis gleichermaßen.

Für weitere Informationen besuchen Sie die offizielle MicroPython-Website (micropython.org) oder erkunden Sie Community-Ressourcen auf X und GitHub. Wenn Sie spezifische Fragen zu MicroPython haben oder Hilfe bei einem Projekt benötigen, lassen Sie es mich wissen!