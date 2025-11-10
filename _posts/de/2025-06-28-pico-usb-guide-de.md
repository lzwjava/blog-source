---
audio: false
generated: true
lang: de
layout: post
title: USB-Kabel-Anleitung für Raspberry Pi Pico unter Ubuntu
translated: true
type: note
---

Für deinen **Raspberry Pi Pico (mit Headern)** von der **Raspberry Pi Foundation** (angenommen, "duistou" ist ein Tippfehler oder eine Reseller-Marke), benötigst du das richtige USB-Kabel, um ihn mit Ubuntu einzurichten. Hier ist, was du brauchst:

### USB-Kabel-Anforderungen
1. **Typ**: USB-auf-Micro-USB-Kabel
   - Der Raspberry Pi Pico (Original, mit Headern) verwendet einen **Micro-USB**-Anschluss für Strom und Daten.
   - Stelle sicher, dass das Kabel **Datenübertragung** unterstützt und nicht nur das Laden. Einige billige Micro-USB-Kabel sind nur für die Stromversorgung ausgelegt und eignen sich nicht zum Programmieren oder für die Kommunikation.

2. **Kabelspezifikationen**:
   - **Stecker**: USB-A (oder USB-C, abhängig von den Anschlüssen deines Computers) auf Micro-USB.
   - **Qualität**: Verwende ein hochwertiges Kabel, um Verbindungsprobleme zu vermeiden. Ein Kabel einer renommierten Marke (z.B. Anker, Belkin oder das mit Geräten wie Handys oder Tablets mitgelieferte Kabel) funktioniert gut.
   - **Länge**: Ein 1-3 ft (30-100 cm) langes Kabel ist ideal, um Signalprobleme zu minimieren.

3. **Computer-Anschluss**:
   - Wenn dein Ubuntu-Computer **USB-A-Anschlüsse** hat, verwende ein USB-A-auf-Micro-USB-Kabel.
   - Wenn er nur **USB-C-Anschlüsse** hat, verwende ein USB-C-auf-Micro-USB-Kabel oder einen USB-C-Hub/Adapter mit einem USB-A-auf-Micro-USB-Kabel.

### Einrichtungsnotizen
- **Verbindung**: Stecke das Micro-USB-Ende in den Micro-USB-Anschluss des Pico und das andere Ende in deinen Ubuntu-Computer.
- **Modus**:
  - **Normaler Modus**: Stecke den Pico direkt ein, um eine Verbindung für die Programmierung herzustellen (z.B. MicroPython, C/C++).
  - **BOOTSEL-Modus**: Halte die **BOOTSEL**-Taste auf dem Pico gedrückt, während du ihn einsteckst, um in den Massenspeichermodus für Firmware-Updates zu gelangen (er erscheint als Laufwerk mit dem Namen `RPI-RP2`).
- **Überprüfung**: Verwende nach dem Verbinden die Schritte aus meiner vorherigen Antwort, um zu bestätigen, dass Ubuntu den Pico erkennt (z.B. `lsusb`, `ls /dev/tty*` oder `lsblk`).

### Fehlerbehebung bei Kabelproblemen
- Wenn der Pico nicht erkannt wird (kein `/dev/ttyACM0` oder `RPI-RP2`-Laufwerk), versuche ein anderes Kabel oder einen anderen USB-Anschluss.
- Vermeide die Verwendung von USB-Hubs, da diese manchmal zu Erkennungsproblemen führen können.
- Überprüfe das Kabel, indem du es mit einem anderen Gerät testest (z.B. einem Handy), um zu bestätigen, dass es die Datenübertragung unterstützt.

Wenn du unsicher wegen deines Kabels bist oder immer noch Probleme hast, beschreibe dein Setup (z.B. Computer-Anschlüsse, Kabeltyp, was du siehst, wenn du es einsteckst), und ich kann dir weiterhelfen!