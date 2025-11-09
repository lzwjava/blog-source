---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Kompaktes WLAN-Modul für IoT
translated: true
type: note
---

Das ESP-01S ist ein kompaktes WiFi-Modul, das auf dem ESP8266-Mikrocontroller-Chip von Espressif Systems basiert. Es ist eine verbesserte Version des ursprünglichen ESP-01 und wurde in erster Linie für IoT-Anwendungen entwickelt, bei denen Sie drahtlose Konnektivität zu anderen Mikrocontrollern wie Arduino oder Raspberry Pi hinzufügen müssen.

### Wichtige Merkmale:
- **WiFi-Fähigkeiten**: Unterstützt 802.11 b/g/n-Standards und kann als eigenständiger WiFi-Zugangspunkt, Station oder beides fungieren. Es enthält einen integrierten TCP/IP-Protokollstack für eine einfache Netzwerkintegration.
- **Prozessor und Speicher**: Läuft auf einem Tensilica L106 32-Bit RISC CPU mit 80 MHz (übertaktbar auf 160 MHz). Verfügt über 1 MB (oder manchmal 4 MB in Varianten) SPI-Flash-Speicher für Code und Datenspeicherung.
- **I/O-Pins**: 8-Pin-Layout (VCC, GND, CH_PD, RST, TX, RX, GPIO0, GPIO2) für serielle Kommunikation (UART) und grundlegende GPIO-Steuerung, z. B. zum Schalten von LEDs oder Relais.
- **Stromversorgung und Größe**: Arbeitet mit 3,3 V (nicht 5 V-tolerant), zieht wenig Strom (ca. 80 mA während der Übertragung) und misst etwa 24,75 x 14,5 mm – was es ideal für kleine Projekte macht.
- **Verbesserungen gegenüber ESP-01**: Besseres PCB-Layout für verbesserte WiFi-Signalstärke, mehr Flash-Speicher (1 MB vs. 512 KB) und eine blaue Status-LED auf GPIO2 anstelle von TX.

### Häufige Anwendungen:
- Verbinden von Sensoren oder Geräten mit dem Internet zur Fernüberwachung/-steuerung.
- Programmierung über die Arduino IDE (mit ESP8266-Board-Unterstützung) oder AT-Befehle über die serielle Schnittstelle.
- Prototyping von Smart-Home-Geräten, wie WiFi-fähigen Schaltern oder Wetterstationen.

Für den Einstieg benötigen Sie einen USB-zu-Serial-Adapter (wie FTDI) zum Flashen der Firmware, da es keinen integrierten USB-Port hat. Es ist preiswert (unter 5 $) und weit verbreitet, sollte aber vorsichtig behandelt werden, um eine Beschädigung der Pins zu vermeiden.

[How to use an ESP-01S module](https://www.taydaelectronics.com/datasheets/files/ESP-01S.pdf)  
[Getting Started With the ESP8266 ESP-01](https://www.instructables.com/Getting-Started-With-the-ESP8266-ESP-01/)  
[ESP-01S Introduction](https://lonelybinary.com/en-us/blogs/learn/what-is-esp-01s)  
[ESP-01S / ESP01S ESP8266 Module](https://hobbycomponents.com/esp8266/1176-esp-01s-esp01s-esp8266-module)