---
audio: false
generated: true
lang: de
layout: post
title: Flash Pico-Firmware per UF2
translated: true
type: note
---

Um Firmware auf Ihren Raspberry Pi Pico (oder ein RP2040-basiertes Board) im BOOTSEL-Modus zu flashen, indem Sie eine `.uf2`-Datei auf das `RPI-RP2`-Laufwerk kopieren, befolgen Sie diese Schritte:

### Schritt-für-Schritt-Anleitung
1. **Bestätigen Sie, dass sich das Gerät im BOOTSEL-Modus befindet**:
   - Ihr Gerät sollte als USB-Laufwerk mit dem Namen `RPI-RP2` erscheinen, wenn es mit Ihrem Computer verbunden ist. Dies bestätigt, dass es sich im BOOTSEL-Modus befindet (angezeigt durch `Bus 001 Device 009: ID 2e8a:0003 Raspberry Pi RP2 Boot`).
   - Wenn es sich nicht im BOOTSEL-Modus befindet, ziehen Sie das Gerät ab, halten Sie die BOOTSEL-Taste auf dem Pico gedrückt und stecken Sie es in den USB-Port Ihres Computers, während Sie die Taste gedrückt halten. Lassen Sie die Taste nach ein paar Sekunden los.

2. **Beschaffen Sie eine gültige `.uf2`-Datei**:
   - **MicroPython**: Laden Sie die neueste MicroPython-Firmware für den Raspberry Pi Pico von der [offiziellen MicroPython-Website](https://micropython.org/download/rp2-pico/) herunter. Wählen Sie die `.uf2`-Datei für den Pico oder Pico W (z.B. `rp2-pico-latest.uf2`).
   - **CircuitPython**: Laden Sie die CircuitPython-Firmware von der [CircuitPython-Website](https://circuitpython.org/board/raspberry_pi_pico/) für den Pico oder Pico W herunter.
   - **Benutzerdefiniertes Programm**: Wenn Sie ein Programm geschrieben haben (z.B. in C/C++ mit dem Pico SDK), kompilieren Sie es, um eine `.uf2`-Datei zu generieren. Verwenden Sie zum Beispiel das Pico SDK oder die Arduino IDE, um Ihr Projekt zu bauen.
   - Speichern Sie die `.uf2`-Datei an einem leicht zugänglichen Ort auf Ihrem Computer (z.B. Desktop oder Downloads-Ordner).

3. **Suchen Sie das RPI-RP2-Laufwerk**:
   - Öffnen Sie auf Ihrem Computer den Datei-Explorer:
     - **Windows**: Suchen Sie nach `RPI-RP2` unter "Dieser PC" als Wechseldatenträger.
     - **macOS**: Das Laufwerk sollte auf dem Desktop oder im Finder unter "Geräte" erscheinen.
     - **Linux**: Prüfen Sie unter `/media` oder `/mnt`, oder verwenden Sie `lsblk`, um verbundene Laufwerke aufzulisten.
   - Wenn das Laufwerk nicht erscheint, stellen Sie sicher, dass das USB-Kabel datenfähig ist (nicht nur zur Stromversorgung) und versuchen Sie einen anderen USB-Port oder ein anderes Kabel.

4. **Kopieren Sie die `.uf2`-Datei auf das RPI-RP2-Laufwerk**:
   - Ziehen Sie die `.uf2`-Datei per Drag & Drop auf das `RPI-RP2`-Laufwerk, oder kopieren und fügen Sie sie mit Ihrem Datei-Explorer ein.
   - Alternativ können Sie einen Terminal-Befehl verwenden (unter Linux/macOS):
     ```bash
     cp /pfad/zu/ihrer/datei.uf2 /media/ihr_benutzername/RPI-RP2/
     ```
     Ersetzen Sie `/pfad/zu/ihrer/datei.uf2` durch den Pfad zu Ihrer `.uf2`-Datei und passen Sie den Mount-Punkt bei Bedarf an.

5. **Warten Sie auf den Flash-Vorgang**:
   - Sobald die `.uf2`-Datei kopiert wurde, flasht der Raspberry Pi Pico die Firmware automatisch. Das `RPI-RP2`-Laufwerk wird verschwinden (wird ausgehängt), wenn das Gerät neu startet, was anzeigt, dass der Vorgang abgeschlossen ist.
   - Dies dauert typischerweise ein paar Sekunden. Ziehen Sie das Gerät während dieser Zeit nicht ab.

6. **Überprüfen Sie das Gerät**:
   - Nach dem Flashen sollte der Pico den BOOTSEL-Modus verlassen und die neue Firmware ausführen.
   - Für MicroPython oder CircuitPython, verbinden Sie sich mit dem Gerät über ein Terminal (z.B. PuTTY, screen oder Thonny IDE) über den USB-Serial-Port (z.B. `COM3` unter Windows oder `/dev/ttyACM0` unter Linux/macOS). Sie sollten eine Python-REPL-Eingabeaufforderung sehen.
   - Für benutzerdefinierte Programme, prüfen Sie das erwartete Verhalten (z.B. blinkende LED, Serial-Ausgabe, etc.).
   - Wenn das `RPI-RP2`-Laufwerk wieder erscheint, ist der Flash-Vorgang möglicherweise fehlgeschlagen. Versuchen Sie eine andere `.uf2`-Datei oder prüfen Sie auf Hardware-Probleme (z.B. USB-Kabel, Flash-Chip).

### Fehlerbehebung
- **Laufwerk wird nicht angezeigt**: Stellen Sie sicher, dass sich der Pico im BOOTSEL-Modus befindet und das USB-Kabel Datenübertragung unterstützt. Versuchen Sie, BOOTSEL zu drücken, dann kurz die RESET-Taste (falls vorhanden) zu drücken, während er verbunden ist.
- **Kopieren schlägt fehl oder Laufwerk erscheint wieder**: Die `.uf2`-Datei könnte beschädigt sein oder der Flash-Speicher könnte fehlerhaft sein. Laden Sie eine neue `.uf2`-Datei herunter oder testen Sie mit einer minimalen Datei, wie der von MicroPython. Wenn das Problem bestehen bleibt, verwenden Sie `picotool` zur Diagnose:
  ```bash
  picotool info
  ```
  Installieren Sie `picotool` aus dem [Raspberry Pi Pico SDK](https://github.com/raspberrypi/picotool).
- **Keine Reaktion nach dem Flashen**: Wenn Sie MicroPython/CircuitPython verwenden, stellen Sie sicher, dass Ihre IDE (z.B. Thonny) auf den korrekten Serial-Port eingestellt ist. Für benutzerdefinierte Programme, verifizieren Sie, dass der Code korrekt kompiliert wurde.

### Beispiel: MicroPython flashen
1. Laden Sie die MicroPython `.uf2`-Datei von [micropython.org](https://micropython.org/download/rp2-pico/) herunter.
2. Halten Sie BOOTSEL gedrückt, stecken Sie den Pico ein und lassen Sie BOOTSEL los.
3. Öffnen Sie Ihren Datei-Explorer, finden Sie das `RPI-RP2`-Laufwerk und kopieren Sie die `.uf2`-Datei darauf.
4. Warten Sie, bis das Laufwerk verschwindet.
5. Öffnen Sie die Thonny IDE, wählen Sie den Serial-Port des Pico aus und beginnen Sie, in MicroPython zu programmieren.

Wenn Sie Hilfe mit einer bestimmten `.uf2`-Datei, einem Tool oder einem Setup benötigen (z.B. Installation von `picotool` oder Verwendung von Thonny), lassen Sie es mich wissen!