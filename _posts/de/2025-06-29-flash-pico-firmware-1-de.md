---
audio: false
generated: true
lang: de
layout: post
title: Pico mit UF2-Datei flashen
translated: true
type: note
---

Um die Datei `RPI_PICO-20250415-v1.25.0.uf2` auf deinen Raspberry Pi Pico zu flashen, der unter `/media/lzw/RPI-RP2` eingehängt ist, verwende den folgenden Befehl:

```bash
cp ~/Downloads/RPI_PICO-20250415-v1.25.0.uf2 /media/lzw/RPI-RP2/
```

### Erklärung
- `cp`: Kopiert die Datei.
- `~/Downloads/RPI_PICO-20250415-v1.25.0.uf2`: Der Pfad zu deiner `.uf2`-Datei im Downloads-Verzeichnis.
- `/media/lzw/RPI-RP2/`: Der Einhängepunkt des `RPI-RP2`-Laufwerks des Pico, wie in deiner Ausgabe gezeigt.

### Nach Ausführung des Befehls
- Die `.uf2`-Datei wird auf den Pico kopiert und das Gerät flasht die Firmware automatisch.
- Das `RPI-RP2`-Laufwerk wird nach Abschluss des Flashens ausgehängt (verschwindet), was auf einen Erfolg hinweist.
- Wenn das Laufwerk wieder erscheint, ist der Flash-Vorgang möglicherweise fehlgeschlagen. Überprüfe, ob die `.uf2`-Datei gültig ist, oder versuche es mit einem anderen USB-Kabel/einem anderen USB-Port.

Wenn du auf Probleme stößt oder weitere Hilfe benötigst, lass es mich wissen!