---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: FineWeb-Daten Download und Vorbereitung
translated: true
type: note
---

### Herunterladen der Parquet-Datei

Die von Ihnen bereitgestellte URL verweist auf eine spezifische Parquet-Datei aus dem FineWeb-Datensatz (ein bereinigter Teil des CommonCrawl-Datensatzes). Diese Datei (`000_00000.parquet` aus dem Dump `CC-MAIN-2013-20`) enthält ~1 Million Zeilen englischen Web-Texts, wobei jede Zeile eine `text`-Spalte enthält, die bereits für das Training von Sprachmodellen vorverarbeitet ist (HTML entfernt, dedupliziert, qualitätsgefiltert mit Tools wie Trafilatura).

So laden Sie sie herunter:
- Verwenden Sie die Hugging Face CLI: `huggingface-cli download HuggingFaceFW/fineweb data/CC-MAIN-2013-20/000_00000.parquet --local-dir ./fineweb_data`
- Oder via Python mit `huggingface_hub`:
  ```python
  from huggingface_hub import hf_hub_download

  file_path = hf_hub_download(
      repo_id="HuggingFaceFW/fineweb",
      filename="data/CC-MAIN-2013-20/000_00000.parquet",
      local_dir="./fineweb_data"
  )
  print(f"Downloaded to: {file_path}")
  ```
Dies speichert die ~500 MB große Datei lokal (z.B. `./fineweb_data/data/CC-MAIN-2013-20/000_00000.parquet`).

Für den kompletten Dump (Hunderte von Dateien) verwenden Sie `snapshot_download`, wie in der Datensatzdokumentation gezeigt, aber beginnen Sie mit dieser einzelnen Datei zum Testen.

### Extrahieren des Texts

Die `text`-Spalte von FineWeb ist Klartext, der bereit für das Training ist – kein Parsen von HTML oder Rohtext nötig. Verwenden Sie `pandas` oder `pyarrow`, um ihn effizient zu laden. So geht's:

1. **Abhängigkeiten installieren** (falls nötig): `pip install pandas pyarrow datasets` (angenommen, Sie haben sie für das NanoGPT-Setup bereits).

2. **Die Parquet-Datei laden und Text extrahieren**:
   ```python
   import pandas as pd
   import os

   # Pfad zu Ihrer heruntergeladenen Datei
   parquet_path = "./fineweb_data/data/CC-MAIN-2013-20/000_00000.parquet"

   # Die Parquet-Datei laden (effizient für große Dateien)
   df = pd.read_parquet(parquet_path, columns=['text'])  # Nur die Text-Spalte laden, um Speicher zu sparen

   # Allen Text in eine Liste extrahieren (oder iterieren, wenn speicherbeschränkt)
   texts = df['text'].tolist()  # Liste von ~1M Zeichenketten

   # Optional: Grundlegende Bereinigung (FineWeb ist bereits sauber, aber Leerzeichen normalisieren)
   import re
   def clean_text(text):
       if pd.isna(text):  # Nullwerte überspringen (selten in FineWeb)
           return ''
       text = re.sub(r'\s+', ' ', text.strip())  # Leerzeichen zusammenfassen
       return text if len(text) > 10 else ''  # Sehr kurze Texte filtern

   cleaned_texts = [clean_text(t) for t in texts if t]  # Filter anwenden

   print(f"Extracted {len(cleaned_texts)} text samples")
   print("Sample:", cleaned_texts[0][:200] + "...")  # Vorschau des ersten Texts
   ```

   - **Speichertipp**: Diese Datei hat ~1M Zeilen, jeder Text ~1-5k Zeichen. Auf einer Maschine mit 16GB RAM lädt sie problemlos. Für größere Dumps verwenden Sie `pyarrow` für chunked Reading:
     ```python
     import pyarrow.parquet as pq

     table = pq.read_table(parquet_path, columns=['text'])
     texts = table['text'].to_pylist()
     ```

   - **Streaming-Alternative** (kein vollständiger Download nötig): Verwenden Sie die `datasets`-Bibliothek, um zu iterieren, ohne alles zu laden:
     ```python
     from datasets import load_dataset

     # Spezifischen Dump im Streaming-Modus laden
     dataset = load_dataset("HuggingFaceFW/fineweb", name="CC-MAIN-2013-20", split="train", streaming=True)

     texts = []
     for i, sample in enumerate(dataset):
         if i >= 100000:  # Begrenzung für Tests
             break
         texts.append(sample['text'])

     # Wie oben bereinigen
     ```

### Vorbereitung für das NanoGPT-Training

NanoGPT erwartet eine einzelne Textdatei (z.B. `input.txt`) mit verketteten Dokumenten, getrennt durch ein spezielles Token (wie `"<|endoftext|>"`). So formatieren Sie den extrahierten Text:

```python
# Nach dem Extrahieren von cleaned_texts von oben
with open('input.txt', 'w', encoding='utf-8') as f:
    for text in cleaned_texts:
        f.write(text + "\n<|endoftext|>\n")  # NanoGPT's Standard-Trenner

print("Saved to input.txt – ready for NanoGPT!")
```

- **Warum dieses Format?** Das `data.py`-Skript von NanoGPT liest `input.txt`, kodiert es mit Ihrem Tokenizer (z.B. GPT-2) und erzeugt Trainings-/Validierungsaufteilungen. Jedes Dokument endet mit `"<|endoftext|>"`, um Kontext-Vermischung zwischen Dokumenten zu vermeiden.
- **Anpassung**:
  - Nach Länge filtern: Fügen Sie `if 100 < len(text.split()) < 10000:` vor dem Schreiben hinzu, um mittelgroße Dokumente zu behalten.
  - Teilmenge für Tests: Verwenden Sie `cleaned_texts[:10000]` für einen schnellen Lauf mit 10k Beispielen.
  - Trainingsbefehl: Sobald `input.txt` bereit ist, führen Sie `python train.py` in NanoGPT aus (passen Sie `--dataset=input.txt` an, falls nötig).

Diese einzelne Datei liefert ~5-10B Token – hervorragend für das Fine-Tuning. Für mehr laden Sie zusätzliche Parquet-Dateien herunter und verketten sie. Wenn Sie auf Speicherprobleme stoßen oder Hilfe mit der NanoGPT-Konfiguration benötigen, teilen Sie die Details mit!

**Referenz**: [FineWeb Dataset Card](https://huggingface.co/datasets/HuggingFaceFW/fineweb)