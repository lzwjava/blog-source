---
audio: false
generated: true
image: false
lang: de
layout: post
model: google/gemini-2.5-flash
title: Extraktion der letzten zehn Audiominuten
translated: true
type: note
---

Um die letzten 10 Minuten der Audiodatei `lobby-zh.ogg` zu extrahieren, müssen Sie die folgenden Informationen verwenden:

1.  **Gesamtdauer:** Die Dauer der Eingabedatei beträgt `00:33:34.40`.
2.  **Gewünschte Segmentlänge:** 10 Minuten (oder 600 Sekunden).
3.  **Startzeit-Berechnung:** Sie müssen den Punkt berechnen, der 10 Minuten *vor* dem Ende der Datei liegt.

### Berechnung

*   Gesamtdauer in Sekunden:
    $$(33 \times 60) + 34.40 = 1980 + 34.40 = 2014.40 \text{ Sekunden}$$
*   Startzeit:
    $$2014.40 \text{ Sekunden} - 600 \text{ Sekunden} = 1414.40 \text{ Sekunden}$$

Im `HH:MM:SS.sss` Format:
$$1414.40 \text{ Sekunden} = 23 \text{ Minuten und } 34.40 \text{ Sekunden} \quad (1414.40 / 60 = 23.5733\dots)$$
$$\text{Startzeit} = 00:23:34.40$$

### FFmpeg-Befehl

Sie verwenden die `-ss` (Position anspringen) Eingabeoption in Kombination mit der `-t` (Dauer) Option.

1.  `-ss 00:23:34.40`: Setzt die Startposition für die Extraktion.
2.  `-t 00:10:00`: Setzt die Dauer des Ausgabesegments auf genau 10 Minuten.

```bash
ffmpeg -i lobby-zh.ogg -ss 00:23:34.40 -t 00:10:00 last_10_minutes.ogg
```

**Hinweis:** Wenn Sie die ursprünglichen Bitrate/Codec-Einstellungen der Ausgabedatei beibehalten möchten, können Sie `-c copy` für eine schnellere Verarbeitung hinzufügen:

```bash
ffmpeg -i lobby-zh.ogg -ss 00:23:34.40 -t 00:10:00 -c copy last_10_minutes_copy.ogg
```