---
audio: false
generated: true
lang: de
layout: post
title: Überprüfung der Raspberry Pi Pico Erkennung unter Ubuntu
translated: true
type: note
---

Um zu überprüfen, ob dein Raspberry Pi Pico von Ubuntu erkannt wird, nachdem du ihn eingesteckt hast, folge diesen Schritten:

1. **Überprüfe USB-Geräte**:
   - Öffne ein Terminal und führe aus:
     ```bash
     lsusb
     ```
   - Suche nach einem Eintrag wie `Raspberry Pi Pico` oder einem Gerät mit der Vendor-ID `2E8A` (die Vendor-ID von Raspberry Pi). Zum Beispiel:
     ```
     Bus XXX Device XXX: ID 2e8a:0003 Raspberry Pi Pico
     ```

2. **Überprüfe serielle Anschlüsse**:
   - Wenn sich der Pico im BOOTSEL-Modus befindet (zum Flashen der Firmware) oder ein MicroPython/Arduino-Programm mit serieller Ausführung läuft, überprüfe auf einen seriellen Anschluss:
     ```bash
     ls /dev/tty*
     ```
   - Suche nach einem Gerät wie `/dev/ttyACM0` oder `/dev/ttyUSB0`. Der Pico erscheint typischerweise als `/dev/ttyACM0`, wenn MicroPython läuft.

3. **Überprüfe Laufwerksgeräte (BOOTSEL-Modus)**:
   - Wenn sich der Pico im BOOTSEL-Modus befindet (BOOTSEL-Taste gedrückt halten während des Einsteckens), sollte er als Massenspeichergerät erscheinen. Führe aus:
     ```bash
     lsblk
     ```
   - Suche nach einem Gerät wie `/dev/sdb` (oder ähnlich) mit einem Mount-Punkt, oft beschriftet mit `RPI-RP2`.

4. **Verwende `dmesg` für Kernel-Logs**:
   - Führe aus:
     ```bash
     dmesg | tail -n 20
     ```
   - Überprüfe die Meldungen, die auf eine Erkennung des Picos hinweisen, wie zum Beispiel:
     ```
     [1234.567890] usb 1-1: New USB device found, idVendor=2e8a, idProduct=0003
     [1234.567891] usb 1-1: Product: Pico
     [1234.567892] cdc_acm 1-1:1.0: ttyACM0: USB ACM device
     ```
   - Dies bestätigt, dass der Pico erkannt und ein Port zugewiesen wurde (z.B. `ttyACM0`).

5. **Teste mit MicroPython (falls installiert)**:
   - Wenn du MicroPython verwendest, installiere ein Tool wie `picocom` oder `minicom`:
     ```bash
     sudo apt install picocom
     ```
   - Verbinde dich mit dem seriellen Anschluss des Picos:
     ```bash
     picocom /dev/ttyACM0
     ```
   - Wenn erkannt, solltest du die MicroPython REPL-Eingabeaufforderung (>>>) sehen. Drücke `Strg+C`, um zu beenden.

**Hinweise**:
- Stelle sicher, dass der Pico ordnungsgemäß über ein gutes USB-Kabel verbunden ist (Daten, nicht nur Strom).
- Im BOOTSEL-Modus erscheint der Pico als Speichergerät, nicht als serielles Gerät.
- Wenn er nicht erkannt wird, versuche einen anderen USB-Port, ein anderes Kabel oder überprüfe, ob die Treiber (wie `cdc_acm` für serielle Verbindungen) geladen sind:
  ```bash
  lsmod | grep cdc_acm
  ```

Wenn du den Pico in keiner dieser Überprüfungen siehst, teile mir bitte mehr Details mit (z.B. Modus des Picos, was du versuchst zu tun), und ich kann bei der weiteren Fehlerbehebung helfen!