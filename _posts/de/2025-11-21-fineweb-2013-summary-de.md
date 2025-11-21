---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4.1-fast
title: FineWeb 2013 Datensatz-Zusammenfassung
translated: true
type: note
---

**CC-MAIN-2013-20** (Summer 2013 Dump) im FineWeb-Datensatz:

- **Anzahl der .parquet-Dateien**: Ungefähr **460–500**  
  (Dateien sind in unterschiedlich großen Shards aufgeteilt: viele ~1 GB, einige größer bis zu ~2 GB. Das Verzeichnis hat eine Gesamtgröße von **422 GB**, also 422 ÷ ~0,9 GB Durchschnitt ≈ 460–480 Shards. Die Namensgebung ist sequenziell von `000_00000.parquet` bis ungefähr `000_004xx.parquet`.)

- **Gesamtgröße aller Parquet-Dateien**: **422 GB**

- **Tokens, wenn mit einem GPT-artigen Tokenizer kodiert** (cl100k_base, verwendet für GPT-4, oder der ältere GPT-2-Tokenizer, der in den FineWeb-Berichten verwendet wurde):  
  **144,5 Milliarden Tokens** (nach der FineWeb-Bereinigung, Filterung und Deduplizierung)

Hinweis: Der ursprüngliche, rohe Common Crawl Dump war viel größer (~393 Milliarden Tokens vor der Filterung), aber FineWeb behält nur den hochwertigen englischsprachigen Text, weshalb dieser alte Dump von 2013 so dramatisch schrumpft.

Wenn Sie das gesamte Verzeichnis herunterladen (z.B. via `huggingface-cli download` oder einem Skript, das über alle Shards iteriert), erhalten Sie ~422 GB Parquet-Dateien, die 144,5 Mrd. Tokens enthalten und bereit für das Training sind.

[FineWeb-Datensatzkarte (enthält Tabelle mit Tokens pro Dump)](https://huggingface.co/datasets/HuggingFaceFW/fineweb)  
[CC-MAIN-2013-20 Verzeichnis auf HF (zeigt die Gesamtgröße)](https://huggingface.co/datasets/HuggingFaceFW/fineweb/tree/main/data/CC-MAIN-2013-20)