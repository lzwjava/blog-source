---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4.1-fast
title: FineWeb-Dataset-Parquet-Dateianzahl
translated: true
type: note
---

Der **FineWeb**-Datensatz (die englische Version mit 15T+ Token auf `HuggingFaceFW/fineweb`) enthält insgesamt **ungefähr 35.000 bis 50.000** `.parquet`-Dateien.

### Aufschlüsselung
- Er besteht aus **96** separaten Common Crawl Snapshots (Dumps, z.B. `CC-MAIN-2013-20`, `CC-MAIN-2024-10`, usw.).
- Jeder Dump wird in einem eigenen Unterverzeichnis unter `/data/` gespeichert und ist in viele geshardete `.parquet`-Dateien aufgeteilt, die Namen wie `000_00000.parquet`, `000_00001.parquet`, … haben (mit Nullen aufgefüllt, sequenziell).
- Die Anzahl der Parquet-Dateien variiert pro Dump, abhängig von seiner Größe:
  - Kleinere/ältere Dumps (wie das `CC-MAIN-2013-20`-Beispiel in Ihrem Skript) haben oft **~200–1.000** Dateien.
  - Größere, neuere Dumps können **mehrere tausend** Dateien jeweils haben.
- Es gibt keine einzige offiziell veröffentlichte Gesamtzahl, aber Community-Schätzungen und Berechnungen basierend auf den Dump-Größen/Token-Anzahlen kommen konsistent auf eine **Gesamtzahl von ungefähr 35.000–50.000** Parquet-Dateien über alle 96 Dumps hinweg (der vollständige Datensatz ist ~45–53 TB unkomprimiert).

Ihr Skript lädt die Shards 11 bis 20 (10 Dateien) vom sehr kleinen `CC-MAIN-2013-20`-Dump herunter, der weitaus mehr als das hat – allein für diesen Dump gibt es viele Hunderte von Shards insgesamt.

Wenn Sie die exakte Anzahl benötigen, können Sie sie programmgesteuert mit der Hugging Face Hub API berechnen (z.B. mit `huggingface_hub.list_repo_files`), aber die groben Zahlen oben sind das, was allgemein verwendet wird, wenn der vollständige Datensatz heruntergeladen oder verarbeitet wird.

[FineWeb Datensatzkarte](https://huggingface.co/datasets/HuggingFaceFW/fineweb)  
[FineWeb Datenbaum (Beispieldump)](https://huggingface.co/datasets/HuggingFaceFW/fineweb/tree/main/data)