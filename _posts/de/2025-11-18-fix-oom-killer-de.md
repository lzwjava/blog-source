---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Behebung des OOM-Killers im FineWeb-Skript
translated: true
type: note
---

Die "Killed"-Meldung ohne Python-Traceback bedeutet, dass der Linux OOM (Out-of-Memory) Killer den Prozess beendet hat. Dies passiert im `data/fineweb/prepare.py` Skript, weil es versucht, Ihre gesamte ~15 GB große zusammengeführte Textdatei (`train_fineweb.txt`) auf einmal mit etwas wie `open(...).read()` in den RAM zu laden, bevor die Tokenisierung erfolgt.

Obwohl FineWeb-Edu für Streaming konzipiert ist (der offizielle Downloader verwendet Hugging Face `datasets` und verarbeitet Shard-für-Shard in ~100M Token-Blöcken, ohne alles auf einmal in den Speicher zu laden), hat der nanoGPT fineweb-Ordner einen benutzerdefinierten Lokaldatei-Pfad, der für große Dateien nicht speichereffizient ist.

### Schnelle Lösungen (wählen Sie eine)

1. **Beste & Empfohlen: Verwenden Sie den offiziellen Streaming FineWeb-Edu Downloader anstelle Ihrer lokalen Dateien**  
   Verwenden Sie das nanoGPT `data/fineweb/prepare.py` Skript überhaupt nicht.  
   Verwenden Sie Karpathys neueres Skript, das genau für FineWeb-Edu 10B Tokens (oder größer) erstellt wurde:

   ```bash
   # Aus dem nanoGPT Root (oder einem beliebigen Ort)
   wget https://raw.githubusercontent.com/karpathy/build-nanogpt/master/fineweb.py
   python fineweb.py
   ```

   Dies lädt die FineWeb-Edu sample-10BT (10 Milliarden Tokens, ~15-20 GB Rohdaten) im Streaming-Verfahren herunter und tokenisiert sie unter Verwendung von `datasets.load_dataset(..., streaming=True)` und Multiprocessing. Es lädt niemals den vollständigen Datensatz in den RAM und erzeugt die exakt gleichen `.bin` Shards, die nanoGPT in einem Ordner wie `edu_fineweb10B/` erwartet.  
   Es läuft problemlos auf Maschinen mit 32-64 GB RAM (oder sogar weniger, wenn Sie `num_proc_load_dataset` und `num_proc` im Skript reduzieren).

   Für die vollständigen 100B oder 1T Versionen ändern Sie einfach `remote_name = "sample-10BT"` in `"100BT"` oder was immer Sie benötigen.

2. **Falls Sie unbedingt Ihre 10 lokalen Parquet → txt Dateien behalten wollen**  
   Modifizieren Sie `data/fineweb/prepare.py`, um den Text in Blöcken zu verarbeiten, anstatt alles auf einmal zu laden:

   Öffnen Sie das Skript und ersetzen Sie den großen `with open(local_file, 'r', encoding='utf-8') as f: data = f.read()` Block mit so etwas wie diesem:

   ```python
   from tqdm import tqdm
   import tiktoken
   enc = tiktoken.get_encoding("gpt2")

   chunk_size = 1_000_000  # Zeichen pro Block, bei Bedarf anpassen
   tokens = []
   with open(local_file, "r", encoding="utf-8") as f:
       while True:
           chunk = f.read(chunk_size)
           if not chunk:
               break
           tokens.extend(enc.encode_ordinary(chunk))  # oder enc.encode(chunk)
           print(f"Bisher tokenisiert: {len(tokens)/1e6:.1f}M Tokens")
   tokens = np.array(tokens, dtype=np.uint16)
   ```

   Dies hält den Spitzen-RAM-Verbrauch selbst für Ihre 15 GB Datei bei ~10-15 GB.

3. **Hardware Workarounds (temporär, nicht ideal)**  
   - Fügen Sie viel Swap-Speicher hinzu (z.B. 64-128 GB Swap-Datei). Es wird extrem langsam sein, sobald das Swapping beginnt, aber es könnte fertig werden.  
     ```bash
     sudo fallocate -l 64G /swapfile
     sudo chmod 600 /swapfile
     sudo mkswap /swapfile
     sudo swapon /swapfile
     ```
   - Führen Sie es auf einer Maschine/Instanz mit ≥64 GB RAM aus (z.B. AWS r6i.4xlarge oder größer).

### Zusammenfassung
Führen Sie einfach das offizielle `fineweb.py` von build-nanogpt aus – es ist die sauberste Lösung und das, was jetzt jeder für FineWeb verwendet. Ihre zusammengefügte 15 GB txt-Datei ist das Problem, nicht FineWeb selbst.

[Offizielles FineWeb-Edu Downloader-Skript](https://raw.githubusercontent.com/karpathy/build-nanogpt/master/fineweb.py)  
[FineWeb-Edu Datensatz-Seite](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu)