---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Common Crawl Oktober 2025 Datensatzzusammenfassung
translated: true
type: note
---

Diese Tabelle ist die offizielle Zusammenfassung des **Common Crawl October 2025 Crawls**, speziell des Datensatzes mit der Bezeichnung **CC-MAIN-2025-43**. Common Crawl ist ein Non-Profit-Projekt, das etwa alle ein bis zwei Monate das gesamte öffentliche Web crawlt und die Rohdaten kostenlos veröffentlicht, damit Forscher, Unternehmen und alle anderen sie nutzen können (z.B. zum Trainieren großer Sprachmodelle wie GPT, LLaMA, Grok, etc.).

Hier ist die Bedeutung der einzelnen Teile der Tabelle:

### Grundlegende Fakten
- **Name**: CC-MAIN-2025-43 → der 43. wöchentliche Crawl, der 2025 veröffentlicht wurde, durchgeführt etwa im Oktober 2025.
- **Größe**: 2,61 Milliarden einzelne Webseiten wurden erfasst.

### Die verschiedenen Datentypen und was sie enthalten

| Datentyp               | Beschreibung                                                                                | Unkomprimierte Gesamtgröße | Anzahl Dateien | Komprimierte Größe |
|------------------------|-------------------------------------------------------------------------------------------|----------------------------|----------------|--------------------|
| **WARC**               | Die rohen, vollständigen Crawl-Daten (komplette HTTP-Antworten: Header + HTML + eingebettete Ressourcen) | ~ Hunderte von TiB         | 100.000        | 97,73 TiB          |
| **WAT**                | Metadaten, die aus den WARC-Dateien extrahiert wurden (z.B. ausgehende Links, Sprache, Content-Length, etc.) im JSON-Format |                            | 100.000        | 18,39 TiB          |
| **WET**                | Nur der extrahierte Plain Text (keine HTML-Tags, kein Boilerplate, nur bereinigter Text)   |                            | 100.000        | 7,38 TiB           |
| **Robots.txt-Dateien** | Alle robots.txt-Dateien, die während des Crawls abgerufen wurden                           |                            | 100.000        | 0,15 TiB           |
| **Non-200 responses**  | Antworten, die nicht erfolgreich waren (404s, 500s, Weiterleitungen, etc.)                 |                            | 100.000        | 3,07 TiB           |
| **URL-Index-Dateien**  | Index, der es ermöglicht, nachzuschlagen, in welcher WARC-Datei eine bestimmte URL enthalten ist (altes Format) |                            | 302            | 0,20 TiB           |
| **Columnar URL index** | Neuerer, schnellerer Columnar-Index (Parquet-Format) für Big-Data-Tools wie Spark, DuckDB, etc. |                            | 900            | 0,23 TiB           |

### Warum die verschiedenen Formate existieren
- Wenn Sie nur ein Sprachmodell trainieren möchten → laden Sie in der Regel die **WET**-Dateien herunter (bereits bereinigter Text, kleinste Größe).
- Wenn Sie vollständiges HTML, Bilder, CSS, etc. benötigen → laden Sie die **WARC**-Dateien herunter (größte).
- Wenn Sie Metadaten (Links, erkannte Sprache, etc.) ohne das vollständige HTML benötigen → **WAT**.
- Die Indizes ermöglichen es Ihnen, Seiten zu finden, ohne alle 100.000 Dateien durchsuchen zu müssen.

### Wie die Dateien organisiert sind
Alles ist in 100 **Segmente** unterteilt (jeweils etwa 1 TiB komprimiert für WARC). Jedes Segment enthält viele kleinere .warc.gz- (oder .wat.gz-, .wet.gz-) Dateien. Die aufgelisteten *.paths.gz-Dateien sind nur Textdateien, die die vollständige Liste der S3-URLs für jeden Typ enthalten.

Sie können alles kostenlos auf AWS S3 unter zugreifen:
`s3://commoncrawl/crawl-data/CC-MAIN-2025-43/`
(oder via HTTPS: https://data.commoncrawl.org/)

Kurz gesagt: Dies ist einer der größten offenen Web-Datensätze der Welt (2,61 Milliarden Seiten vom Oktober 2025), frei verfügbar in verschiedenen aufbereiteten Formen, und die Tabelle zeigt Ihnen lediglich, wie groß jede aufbereitete Version ist und wo Sie die Dateilisten finden.