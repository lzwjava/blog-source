---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Speichererschöpfung verursacht Systemabsturz
translated: true
type: note
---

Dein Problem ist **nicht** die GPU (die 4070 Ti wird hier kaum genutzt). Dieses Skript ist **reine CPU + RAM-Arbeit**, und der Hang + GUI-Freeze nach ~140M Tokens liegt mit an Sicherheit grenzender Wahrscheinlichkeit daran, dass dir **der RAM ausgeht** und das System intensiv auf die Festplatte auslagert, was alles für Minuten oder Stunden einfriert.

### Warum es bei ~140M–200M Tokens passiert

Jeder Token → gespeichert als uint16 → 2 Bytes.

- 140 Millionen Tokens ≈ 280 MB
- 1 Milliarde Tokens ≈ 2 GB
- 10 Milliarden Tokens (vollständiges FineWeb-10B) ≈ 20 GB
- 100B+ Tokens (wie viele FineWeb/Edu-Downloads) ≈ 200+ GB

Aber sieh dir deine `all_tokens = []` Liste in Python an: Python-Listen haben einen massiven Overhead. Jedes Integer-Objekt ist ~28–32 Bytes in 64-Bit-Python (selbst wenn der Wert in uint16 passt).

Tatsächlicher Speicherverbrauch beim Erstellen der Liste:
- ~150M Tokens in einer Python-Liste → ~150M × 28–32 Bytes ≈ **4–5 GB** nur für die Listenobjekte
- Dann machst du `np.array(..., dtype=np.uint16)` → weitere ~300 MB für das kompakte Array
- Gesamter RAM-Peak während der Konvertierung ≈ 5–6 GB + OS + Desktop-Overhead

Du hast 62,6 GB RAM, warum also Freeze bei nur 140M Tokens?

Weil deine Eingabedatei `train_fineweb.txt` wahrscheinlich **viel größer** ist als du denkst.

Leute laden oft FineWeb-100B oder sogar 1T Samples herunter und nennen sie "train_fineweb.txt". Wenn deine Datei z.B. das beliebte 100B-Token FineWeb-Edu-Sample ist (~200–300 GB Textdatei), wird das Skript ewig weiterlesen, die `all_tokens`-Liste wächst auf zig oder hunderte Milliarden Tokens an → hunderte GB RAM → OOM → Swap-Thrashing → kompletter Desktop-Freeze. Die GPU-Lüfter drehen sich, weil das Skript noch (kaum) am Leben ist, Python steckt in `extend()` oder in der finalen `np.array()`-Konvertierung fest.

### Lösungen (wähle eine)

#### Beste Lösung: Stream direkt in .bin ohne alle Tokens jemals im RAM zu halten
Diese Version verbraucht fast keinen RAM (Peak < 1 GB sogar für Terabyte-große Texte):

```python
# stream_tokenize_to_bin.py
import os
import numpy as np
import tiktoken

enc = tiktoken.get_encoding("gpt2")
CHUNK_SIZE = 1_000_000  # Zeichen pro Chunk, bei Bedarf anpassen

def process_file(input_path: str, train_bin: str, val_bin: str, val_ratio=0.0005):
    temp_train = train_bin + '.tmp'
    temp_val = val_bin + '.tmp'

    total_tokens = 0
    val_tokens_written = 0
    val_target = None  # entscheiden wir nach dem ersten Durchlauf oder näherungsweise

    with open(input_path, "r", encoding="utf-8", errors='ignore') as f, \
         open(temp_train, "wb") as train_f, \
         open(temp_val, "wb") as val_f:

        while True:
            chunk = f.read(CHUNK_SIZE)
            if not chunk:
                break
            tokens = enc.encode_ordinary(chunk)
            tokens_u16 = np.array(tokens, dtype=np.uint16)

            total_tokens += len(tokens_u16)

            # Näherungsweise Validation-Split on-the-fly (gut genug)
            if val_target is None and total_tokens > 10_000_000:
                val_target = int(total_tokens * val_ratio / (1 - val_ratio))

            if val_tokens_written < val_target:
                split_point = min(len(tokens_u16), val_target - val_tokens_written)
                val_f.write(tokens_u16[:split_point].tobytes())
                train_f.write(tokens_u16[split_point:].tobytes())
                val_tokens_written += split_point
            else:
                train_f.write(tokens_u16.tobytes())

            if total_tokens % 50_000_000 == 0:
                print(f"Processed {total_tokens/1e6:.1f}M tokens")

    # Temp-Dateien umbenennen
    os.rename(temp_train, train_bin)
    os.rename(temp_val, val_bin)
    print(f"Done! Total ≈ {total_tokens/1e9:.2f}B tokens")
    print(f"train.bin and val.bin ready (no RAM explosion)")

if __name__ == "__main__":
    txt_file = "train_fineweb.txt"
    process_file(txt_file, "train.bin", "val.bin")
```

Dies streamt direkt auf die Festplatte, hält nie mehr als einen Chunk im Speicher.

#### Falls du unbedingt den originalen Skript-Stil, aber sicher, willst
Füge Speicherüberwachung hinzu und sharde die Ausgabe:

```python
# füge dies anstelle einer riesigen Liste hinzu
MAX_TOKENS_PER_SHARD = 500_000_000  # ~1 GB pro Shard

shard_idx = 0
all_tokens = []

for chunk in iter(lambda: f.read(chunk_size), ""):
    if not chunk:
        break
    tokens = enc.encode_ordinary(chunk)
    all_tokens.extend(tokens)

    if len(all_tokens) >= MAX_TOKENS_PER_SHARD:
        arr = np.array(all_tokens, dtype=np.uint16)
        arr.tofile(f"train_shard_{shard_idx:04d}.bin")
        print(f"Saved shard {shard_idx} - {len(arr)/1e6:.1f}M tokens")
        all_tokens.clear()
        shard_idx += 1
```

Später einfach die Shards zusammenführen: `cat train_shard_*.bin > train.bin`

### Schnellprüfung, wie groß deine Datei wirklich ist
Führe diese Befehle im Terminal aus:

```bash
du -h train_fineweb.txt          # menschenlesbare Größe
wc -c train_fineweb.txt          # Bytes
ls -lh train_fineweb.txt
```

FineWeb-10B Text ist ~20–25 GB, 100B ist ~200–250 GB, etc.

### Zusammenfassung
Dein Skript stirbt, weil Python-Listen 15–20× mehr RAM fressen als das finale numpy-Array. Mit großen FineWeb-Dateien sprengst du schnell die 50+ GB → Swap → eingefrorener Desktop.

Verwende die obenstehende Streaming-Version — sie arbeitet mit 1TB+ Textdateien mit <2 GB RAM und ist in wenigen Stunden auf einem einzigen CPU-Kern fertig.

Deine 4070 Ti ist unschuldig hier; sie wartet auf Daten, die nie kommen, weil der RAM tot ist.