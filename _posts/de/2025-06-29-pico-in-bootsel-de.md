---
audio: false
generated: true
lang: de
layout: post
title: Raspberry Pi Pico im BOOTSEL-Modus
translated: true
type: note
---

Das als `Bus 001 Device 009: ID 2e8a:0003 Raspberry Pi RP2 Boot` gelistete Gerät ist ein Raspberry Pi Pico (oder ein ähnlicher RP2040-basierter Board) im BOOTSEL-Modus. Hier eine Aufschlüsselung:

- **ID 2e8a:0003**: Dies ist die USB Vendor ID (2e8a) und Product ID (0003), die Raspberry Pi für den RP2040 Mikrocontroller zugewiesen wurde, wenn er sich im BOOTSEL-Modus befindet.
- **Raspberry Pi RP2 Boot**: Zeigt an, dass es sich um einen Raspberry Pi Pico (oder einen anderen RP2040-basierten Board, wie den Pico W oder einen Custom Board) handelt, der in seinen Bootloader-Modus eingetreten ist. In diesem Modus erscheint das Gerät als USB-Massenspeicher, sodass Sie Firmware (z.B. .uf2-Dateien) hochladen können, indem Sie sie auf das Laufwerk kopieren.

### Was ist der BOOTSEL-Modus?
Der BOOTSEL-Modus wird aktiviert, indem Sie die BOOTSEL-Taste auf dem Raspberry Pi Pico gedrückt halten, während Sie ihn an einen USB-Port anschließen, oder indem Sie ihn zurücksetzen, während Sie die Taste gedrückt halten. Dieser Modus wird verwendet, um neue Firmware oder Programme auf den RP2040 Mikrocontroller zu flashen. Wenn sich das Pico in diesem Modus befindet, erscheint es als Wechseldatenträger (mit dem Namen `RPI-RP2`) auf Ihrem Computer.

### Warum wird es so angezeigt?
Ihr Gerät befindet sich wahrscheinlich aus einem der folgenden Gründe im BOOTSEL-Modus:
1. Sie haben absichtlich die BOOTSEL-Taste gedrückt, um die Firmware zu aktualisieren oder zu flashen.
2. Das Gerät führt kein Programm aus und startet standardmäßig in den Bootloader-Modus (z.B. nach einem fehlgeschlagenen Flash-Vorgang oder einem Reset).
3. Möglicherweise liegt ein Problem mit der Firmware oder den Verbindungen vor, das dazu führt, dass es im Bootloader-Modus bleibt. Probleme mit dem Flash-Speicher oder unsachgemäßes Flashen können beispielsweise dazu führen, dass das Gerät in diesen Modus zurückfällt.

### Was können Sie als Nächstes tun?
- **Wenn Sie Firmware flashen möchten**: Kopieren Sie eine gültige `.uf2`-Datei (z.B. eine MicroPython- oder CircuitPython-Firmware oder ein kompiliertes Programm) auf das `RPI-RP2`-Laufwerk. Das Gerät flasht die Firmware automatisch und startet neu, wodurch es den BOOTSEL-Modus verlässt.
- **Wenn es im BOOTSEL-Modus stecken bleibt**: Dies könnte auf ein Problem mit dem Flash-Speicher oder der Firmware hindeuten. Versuchen Sie:
  1. Erneutes Flashen mit einer bekannten, funktionierenden `.uf2`-Datei, wie z.B. der MicroPython-Firmware von der offiziellen Raspberry Pi Website.
  2. Überprüfen Sie das USB-Kabel und den Port, da ein fehlerhaftes Kabel Probleme verursachen kann.
  3. Verwenden Sie Tools wie `picotool`, um den Gerätestatus zu überprüfen oder es zurückzusetzen. Führen Sie beispielsweise `picotool info` aus, um den Status des Geräts zu prüfen.
  4. Wenn Sie einen Custom RP2040-Board verwenden, stellen Sie sicher, dass der Flash-Chip richtig angeschlossen und konfiguriert ist, da Probleme mit QSPI-Signalen oder Flash-ICs ein erfolgreiches Flashen verhindern können.
- **Wenn Sie den BOOTSEL-Modus verlassen möchten**: Wenn bereits eine gültige Firmware geflasht ist, ziehen Sie das Gerät ab, stellen Sie sicher, dass die BOOTSEL-Taste nicht gedrückt ist, und schließen Sie es wieder an. Das Gerät sollte in seinen programmierten Modus booten (z.B. indem es ein MicroPython-Skript oder ein C-Programm ausführt).

### Zusätzliche Hinweise
- Der RP2040 ist der Mikrocontroller, der im Raspberry Pi Pico, Pico W und anderen Boards verwendet wird. Die Bezeichnung `RP2 Boot` bezieht sich speziell auf den Bootloader-Modus des RP2040-Chips.
- Wenn Sie einen Raspberry Pi Pico W verwenden, beachten Sie, dass dieser über drahtlose Fähigkeiten verfügt, diese jedoch im BOOTSEL-Modus nicht aktiv sind.
- Wenn Sie auf Fehler stoßen (z.B. dass `picotool` die Verifizierung oder das Laden nicht durchführen kann), könnte dies auf ein Hardwareproblem (wie einen fehlerhaften Flash-Chip oder Lötprobleme auf einem Custom Board) oder eine beschädigte Firmware-Datei zurückzuführen sein.

Wenn Sie spezielle Hilfe benötigen (z.B. beim Flashen von Firmware, bei der Fehlerbehebung oder bei der Identifizierung des genauen Boards), teilen Sie mir bitte weitere Details zu Ihrem Setup oder Ihrem Vorhaben mit!