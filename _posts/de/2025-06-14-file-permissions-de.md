---
audio: false
generated: true
lang: de
layout: post
title: Dateiberechtigungen
translated: true
type: note
---

Das `crw-rw----` in der Ausgabe von `ls -alrt /dev/ttyUSB0` repräsentiert den **Dateityp und die Berechtigungen** für die Gerätedatei `/dev/ttyUSB0`. Hier ist die Aufschlüsselung:

- **c**: Das erste Zeichen gibt den Dateityp an. `c` bedeutet, dass es sich um ein **Character Device** handelt (im Gegensatz zu `b` für Block Device, `d` für Verzeichnis oder `-` für eine reguläre Datei). `/dev/ttyUSB0` ist ein serielles Schnittstellengerät, das typischerweise für USB-zu-Seriell-Adapter verwendet wird.

- **rw-rw----**: Die nächsten neun Zeichen repräsentieren die **Berechtigungen** für die Datei, aufgeteilt in drei Gruppen:
  - **rw-** (Positionen 2-4): Berechtigungen für den **Besitzer** (root). Der Besitzer kann **lesen** (`r`) und **schreiben** (`w`), aber nicht ausführen (`-`).
  - **rw-** (Positionen 5-7): Berechtigungen für die **Gruppe** (dialout). Mitglieder der `dialout`-Gruppe können ebenfalls **lesen** und **schreiben**, aber nicht ausführen.
  - **---** (Positionen 8-10): Berechtigungen für **andere** (Benutzer, die nicht Besitzer oder in der Gruppe sind). Andere haben **keine Berechtigungen** (kein Lesen, Schreiben oder Ausführen).

### Zusammenfassung
- `/dev/ttyUSB0` ist eine Character-Device-Datei.
- Der Besitzer (`root`) und die Gruppe (`dialout`) können von dem Gerät lesen und darauf schreiben.
- Andere Benutzer haben keinen Zugriff.
- Um mit diesem Gerät zu interagieren (z.B. für serielle Kommunikation), muss Ihr Benutzerkonto typischerweise der `dialout`-Gruppe angehören. Sie können dies mit `groups` überprüfen und sich selbst mit `sudo usermod -a -G dialout <Benutzername>` hinzufügen, falls nötig (danach aus- und wieder einloggen).