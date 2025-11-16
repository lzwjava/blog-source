---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Herunterladen spezifischer FineWeb-Parquet-Dateien
translated: true
type: note
---

Du möchtest einfach nur ein paar Parquet-Dateien aus einem Common Crawl-Dump (wie CC-MAIN-2013-20) herunterladen und verwenden, anstatt das gesamte 15T-Token-FineWeb-Monster — völlig verständlich! Hier sind die einfachsten Methoden, um das 2025 zu tun.

### Methode 1: Direkter Download mit huggingface_hub (Empfohlen, Schnellste)
Dies lädt nur die gewünschten Parquet-Dateien mit voller Geschwindigkeit herunter (~GB/s, wenn du hf-transfer aktivierst).

```bash
# 1. Installieren/Aktualisieren
pip install -U "huggingface_hub[hf_transfer]"

# 2. Schnellen Download aktivieren (sehr wichtig!)
export HF_HUB_ENABLE_HF_TRANSFER=1   # Linux/macOS
# oder in Windows PowerShell:
# $env:HF_HUB_ENABLE_HF_TRANSFER = "1"

# 3. Nur die gewünschten Parquet-Dateien herunterladen
huggingface-cli download HuggingFaceFW/fineweb \
    data/CC-MAIN-2013-20/000_00000.parquet \
    data/CC-MAIN-2013-20/000_00001.parquet \
    data/CC-MAIN-2013-20/000_00002.parquet \
    --repo-type dataset --local-dir fineweb-2013-20
```

Das war's — du hast jetzt drei ~2,15 GB große Parquet-Dateien im Ordner `fineweb-2013-20/`.

### Methode 2: Einzeiliges Python-Skript zum Herunterladen spezifischer Dateien
```python
from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="HuggingFaceFW/fineweb",
    repo_type="dataset",
    allow_patterns=[
        "data/CC-MAIN-2013-20/000_00000.parquet",
        "data/CC-MAIN-2013-20/000_00001.parquet",
        # füge bei Bedarf mehr hinzu
    ],
    local_dir="fineweb-2013-20"
)
```

### Wie man die Parquet-Dateien lokal liest
```python
import pandas as pd
# oder pyarrow für Geschwindigkeit + geringeren Speicherverbrauch verwenden
import pyarrow.parquet as pq
import pyarrow.dataset as ds

# Schnellste Methode (streamt, ohne alles im RAM zu laden)
dataset = ds.dataset("fineweb-2013-20/data/CC-MAIN-2013-20/", format="parquet")

for batch in dataset.to_batches(batch_size=1024):
    df = batch.to_pandas()
    for text in df["text"]:
        # mach, was du willst: tokenisieren, filtern, in jsonl schreiben, etc.
        print(text[:200])  # Beispiel
```

Oder einfach mit pandas (in Ordnung für ein paar Dateien):
```python
df = pd.read_parquet("fineweb-2013-20/data/CC-MAIN-2013-20/000_00000.parquet")
print(df.columns)  # ['text', 'id', 'dump', 'url', 'date', 'file_path', 'language', 'language_score', 'token_count']
print(df.iloc[0]["text"])
```

### Schnelle Statistiken für CC-MAIN-2013-20
- ~207 Parquet-Dateien × ~2,15 GB ≈ 422 GB gesamt
- ~44 Milliarden Tokens (gute Größe für kleine bis mittlere Experimente)
- Bereits von Hugging Face bereinigt, dedupliziert und gefiltert

Das ist alles, was du brauchst. Wähle einfach aus, wie viele `_0000XX.parquet`-Dateien du möchtest (sie sind durchgemischt), lade nur diese herunter und starte sofort mit dem Training oder Filtern.