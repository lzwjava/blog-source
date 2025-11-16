---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: OpenWebText-Datensatz Vorverarbeitungsskript
translated: true
type: note
---

### Übersicht
Dieses Python-Skript verarbeitet eine große Textdatei, die den OpenWebText-Datensatz enthält (ein Korpus von Web-Texten, ähnlich dem, was zum Trainieren von Modellen wie GPT-2 verwendet wird). Das Ziel ist:
- Den Rohtext in handliche "Dokumente" (Textblöcke) aufzuteilen.
- Ein Hugging Face `Dataset`-Objekt zur einfachen Handhabung zu erstellen.
- Den Text mit dem GPT-2 Byte Pair Encoding (BPE) Tokenizer von TikToken zu tokenisieren (unter Ignorieren spezieller Tokens und Anhängen eines End-of-Text-Markers).
- Den Datensatz in Trainings- (99,95 %) und Validierungs- (0,05 %) Daten aufzuteilen.
- Die tokenisierten Daten als kompakte Binärdateien (`train.bin` und `val.bin`) unter Verwendung von NumPys speichergemappten Arrays zu speichern. Diese Dateien speichern Sequenzen von Token-IDs (als 16-Bit-Ganzzahlen) für effizientes Laden während des Machine-Learning-Trainings.

Das Skript ist für Effizienz auf Mehrkernsystemen ausgelegt und verwendet Multiprocessing für die Tokenisierung. Es ist inspiriert von einem Datenlademodul aus dem Flash-Attention-Repository (im Code verlinkt), das ähnliche Vorverarbeitung für Sprachmodelltrainings handhabt. Hinweis: OpenWebText ist massiv (~40 GB unkomprimiert), aber dieses Skript geht von einer bereits heruntergeladenen, lokalen `openwebtext.txt`-Datei aus. Die Ausgabedateien sind viel kleiner: `train.bin` ~17 GB (9B Tokens) und `val.bin` ~8,5 MB (4M Tokens).

Das Skript gibt zu Beginn Proxy-Einstellungen aus (wahrscheinlich zum Debuggen von Netzwerkproblemen während impliziter Downloads, obwohl hier keine explizit vorhanden sind). Es verwendet standardmäßig 8 Worker-Prozesse für die Tokenisierung.

### Schritt-für-Schritt-Aufschlüsselung

#### 1. Imports und Ersteinrichtung
```python
import os
import tarfile
from tqdm import tqdm
import numpy as np
import tiktoken
from huggingface_hub import hf_hub_download
from datasets import load_dataset # huggingface datasets
import datasets

print("HTTP_PROXY:", os.getenv("HTTP_PROXY"))
print("HTTPS_PROXY:", os.getenv("HTTPS_PROXY"))

# number of workers in .map() call
# good number to use is ~order number of cpu cores // 2
num_proc = 8

# number of workers in load_dataset() call
# best number might be different from num_proc above as it also depends on NW speed.
# it is better than 1 usually though
num_proc_load_dataset = num_proc

enc = tiktoken.get_encoding("gpt2")

datasets.logging.set_verbosity_info()
```
- **Zweck**: Importiert Bibliotheken für Dateihandhabung (`os`, `tarfile`), Fortschrittsbalken (`tqdm`), numerische Operationen (`numpy`), Tokenisierung (`tiktoken`) und Hugging Face Utilities (`huggingface_hub`, `datasets`).
- **Proxy-Ausgaben**: Protokolliert Umgebungsvariablen für HTTP/HTTPS-Proxys, nützlich, wenn das Skript auf Netzwerkeinschränkungen stößt (z.B. für das Herunterladen von Tokenizer-Modellen, obwohl TikToken dies intern handhabt).
- **Worker**: Setzt `num_proc=8` für parallele Verarbeitung bei der Tokenisierung (etwa die Hälfte der CPU-Kerne für Balance). `num_proc_load_dataset` stimmt damit überein, wird hier aber nicht verwendet (Überbleibsel aus dem Inspirationscode, der von Hugging Face lädt).
- **Encoder**: Lädt den GPT-2 BPE Tokenizer (`enc`). Dieser wandelt Text in ganzzahlige Token-IDs um (Bereich 0–50.256).
- **Logging**: Setzt das Hugging Face Datasets Logging auf "Info"-Level für ausführliche Ausgaben während der Verarbeitung.

Die `if __name__ == '__main__':`-Bedingung stellt sicher, dass die Hauptlogik nur ausgeführt wird, wenn das Skript direkt ausgeführt wird (nicht importiert).

#### 2. Lesen und Aufteilen der Textdatei
```python
if __name__ == '__main__':
    # Read the local openwebtext.txt file
    txt_file = os.path.join(os.path.dirname(__file__), 'openwebtext.txt')
    print(f"Reading from local file: {txt_file}")

    # Read the text content
    texts = []
    with open(txt_file, 'r', encoding='utf-8', errors='ignore') as f:
        # Read the entire file
        full_text = f.read().strip()

        # Try to split into documents by double newlines first
        documents = full_text.split('\n\n')

        # If we only got one document, split by single newlines
        if len(documents) <= 1:
            documents = full_text.split('\n')

        # If we still only have one document, split by period followed by space
        if len(documents) <= 1:
            # Split on period followed by space, then join back sentences
            sentences = full_text.split('. ')
            # Group sentences into chunks of ~100 sentences per document
            chunk_size = 100
            for i in range(0, len(sentences), chunk_size):
                chunk = '. '.join(sentences[i:i+chunk_size])
                if chunk.strip():
                    texts.append(chunk.strip() + '.')
        else:
            # Process documents from double/single newline splits
            for doc in documents:
                doc = doc.strip()
                if doc:  # Only add non-empty documents
                    texts.append(doc)

        print(f"Created {len(texts)} documents from the text file")
```
- **Dateilesen**: Öffnet `openwebtext.txt` (angenommen im selben Verzeichnis wie das Skript) im UTF-8-Modus, ignoriert Kodierungsfehler. Liest den gesamten Inhalt in `full_text` und entfernt Leerzeichen.
- **Aufteilungslogik**: Versucht, den Text in "Dokumente" (logische Blöcke wie Absätze oder Artikel) aufzuteilen:
  - **Primär**: Aufteilung durch doppelte Zeilenumbrüche (`\n\n`), üblich zum Trennen von Dokumenten in Korpora.
  - **Fallback 1**: Falls dies ≤1 Block ergibt (z.B. keine doppelten Zeilenumbrüche), Aufteilung durch einfache Zeilenumbrüche (`\n`) für zeilenbasierten Text.
  - **Fallback 2**: Falls immer noch ≤1 Block (z.B. ein einzelner Textblock), Aufteilung in Sätze durch `. ` (Punkt + Leerzeichen), dann Gruppierung von jeweils 100 Sätzen in einen "Dokumenten"-Block. Dies verhindert übermäßig lange einzelne Einträge. Fügt zur Vollständigkeit einen Punkt am Ende jedes Blocks hinzu.
- **Ausgabe**: Speichert nicht-leere, bereinigte Dokumente in der Liste `texts`. Gibt die Gesamtzahl der erstellten Dokumente aus (z.B. 10k Beispiele für einen Teilbereich).
- **Warum so?** OpenWebText ist eine Aneinanderreihung von Webseiten, daher erzeugt das Aufteilen Trainingsbeispiele, die keine reinen Rohtext-Ausschnitte sind. Dies ahmt die Verarbeitung von Datensätzen wie BookCorpus nach.

#### 3. Erstellen und Aufteilen des Datensatzes
```python
    # Create dataset from texts
    dataset = datasets.Dataset.from_dict({'text': texts})

    # create train/val split from the 10k examples
    split_dataset = dataset.train_test_split(test_size=0.0005, seed=2357, shuffle=True)
    split_dataset['val'] = split_dataset.pop('test') # rename the test split to val
```
- **Datensatzerstellung**: Verpackt die `texts`-Liste in ein Hugging Face `Dataset` mit einer einzigen Spalte `'text'`. Dies ermöglicht effiziente parallele Operationen wie Mapping.
- **Aufteilung**: Verwendet `train_test_split`, um in Trainings- (99,95 %) und Test- (0,05 %) Daten aufzuteilen. Die kleine Validierungsgröße ist bei großen Datensätzen beabsichtigt – genug für die Evaluation, ohne Rechenleistung zu verschwenden.
  - `test_size=0.0005`: 0,05 % für Val (z.B. ~50 Beispiele von 100k).
  - `seed=2357`: Fester Zufallsseed für Reproduzierbarkeit.
  - `shuffle=True`: Zufällige Mischung vor der Aufteilung.
- **Umbenennung**: Entfernt `'test'` und benennt es in `'val'` um. Jetzt ist `split_dataset` ein Dict mit den Schlüsseln `'train'` und `'val'`, jeweils ein `Dataset`-Objekt.

#### 4. Tokenisierungsfunktion
```python
    # we now want to tokenize the dataset. first define the encoding function (gpt2 bpe)
    def process(example):
        ids = enc.encode_ordinary(example['text']) # encode_ordinary ignores any special tokens
        ids.append(enc.eot_token) # add the end of text token, e.g. 50256 for gpt2 bpe
        # note: I think eot should be prepended not appended... hmm. it's called "eot" though...
        out = {'ids': ids, 'len': len(ids)}
        return out
```
- **Zweck**: Wandelt Text in Token-IDs für die Modelleingabe um.
- **`encode_ordinary`**: Tokenisiert den Textstring in eine Liste von Ganzzahlen (GPT-2 Vokabular). Ignoriert alle nicht-standardisierten Tokens im Text.
- **EOT anhängen**: Fügt den End-of-Text-Token (ID 50256 für GPT-2) am Ende hinzu. Dies signalisiert die Sequenzgrenze während des Trainings. (Der Kommentar erwähnt eine mögliche Debatte zwischen Voranstellen vs. Anhängen, aber Anhängen ist bei kausalen LM-Setups wie GPT üblich.)
- **Ausgabe**: Gibt ein Dict mit `'ids'` (Liste der Token-IDs) und `'len'` (Sequenzlänge, für späteres Summieren) zurück.

#### 5. Anwenden der Tokenisierung
```python
    # tokenize the dataset
    tokenized = split_dataset.map(
        process,
        remove_columns=['text'],
        desc="tokenizing the splits",
        num_proc=num_proc,
    )
```
- **Mapping**: Wendet `process` auf jedes Beispiel in den Trainings-/Validierungs-Datensätzen unter Verwendung paralleler Worker (`num_proc=8`) an.
- **`remove_columns=['text']`**: Entfernt den Originaltext, um Speicher zu sparen (wir benötigen jetzt nur noch Tokens).
- **Fortschritt**: Zeigt einen Fortschrittsbalken via `desc`. Dieser Schritt kann bei großen Datensätzen aufgrund der Kodierung viel Zeit in Anspruch nehmen.

#### 6. Speichern der tokenisierten Daten in Binärdateien
```python
    # concatenate all the ids in each dataset into one large file we can use for training
    for split, dset in tokenized.items():
        arr_len = np.sum(dset['len'], dtype=np.uint64)
        filename = os.path.join(os.path.dirname(__file__), f'{split}.bin')
        dtype = np.uint16 # (can do since enc.max_token_value == 50256 is < 2**16)
        arr = np.memmap(filename, dtype=dtype, mode='w+', shape=(arr_len,))

        # Use adaptive batch size based on dataset size
        total_batches = min(1024, len(dset))
        if total_batches < 1024:
            print(f"Using {total_batches} batches for {split} dataset (size: {len(dset)})")

        idx = 0
        for batch_idx in tqdm(range(total_batches), desc=f'writing {filename}'):
            # Only process if this batch index is valid for the dataset size
            if batch_idx < len(dset):
                # Batch together samples for faster write
                batch = dset.shard(num_shards=total_batches, index=batch_idx, contiguous=True).with_format('numpy')
                arr_batch = np.concatenate(batch['ids'])
                # Write into mmap
                arr[idx : idx + len(arr_batch)] = arr_batch
                idx += len(arr_batch)
        arr.flush()
```
- **Schleife über Splits**: Für `'train'` und `'val'`, berechne die Gesamttokenanzahl (`arr_len`) durch Summieren der `'len'`-Felder.
- **Speichergemapptes Array**: Erstellt eine NumPy-Memmap-Datei (`train.bin` oder `val.bin`) als ein beschreibbares Array von uint16-Ganzzahlen (passt zum maximalen Tokenwert von GPT-2 50.256; spart ~50 % Platz gegenüber int32). Die Form ist 1D: `(total_tokens,)`.
- **Batching für Effizienz**: Teilt den Datensatz in bis zu 1024 Shards (`total_batches`) auf, um zu vermeiden, dass alles auf einmal in den RAM geladen wird. Für kleine Datensätze (<1024 Beispiele) wird die exakte Anzahl verwendet.
  - **`shard`**: Teilt den Datensatz in zusammenhängende Batches auf (hier kein Mischen).
  - **`with_format('numpy')`**: Konvertiert den Batch für schnelles Verketten in NumPy-Arrays.
- **Schreiben**: Verkettet Token-IDs aus jedem Batch und kopiert sie sequenziell, beginnend bei `idx`, in das Memmap-Array. Verfolgt den Fortschritt mit `tqdm`.
- **`flush()`**: Stellt sicher, dass alle Daten auf die Festplatte geschrieben werden.
- **Warum Binär/Memmap?** Diese Dateien sind riesig, aber streamfähig. Während des Trainings können sie mit `np.memmap('train.bin', dtype=np.uint16, mode='r')` geladen werden, ohne alles in den Speicher zu laden.

#### 7. Kommentare zur Ausgabe und Verwendung
```python
    # train.bin is ~17GB, val.bin ~8.5MB
    # train has ~9B tokens (9,035,582,198)
    # val has ~4M tokens (4,434,897)

    # to read the bin files later, e.g. with numpy:
    # m = np.memmap('train.bin', dtype=np.uint16, mode='r')
```
- Dies sind Beispielgrößen für das vollständige OpenWebText (Ihre lokale Datei kann abweichen).
- **Lesetipp**: Verwenden Sie Memmap für schreibgeschützten Zugriff. In Trainingsschleifen können Sie zufällige Startindizes abtasten und festlange Sequenzen (z.B. 1024 Tokens) aus dem flachen Array lesen.

### Mögliche Probleme und Hinweise
- **Speichernutzung**: Das Lesen der gesamten `openwebtext.txt` in den RAM könnte bei sehr großen Dateien (40 GB+) fehlschlagen. Erwägen Sie gegebenenfalls Streaming-Lesen.
- **EOT-Platzierung**: Der Kommentar hinterfragt das Anhängen vs. Voranstellen von EOT; in der Praxis funktioniert das Anhängen für autoregressive Modelle (es markiert das Ende nach dem Inhalt).
- **Anpassung**: Geht von einer lokalen Datei aus; der Inspirationscode lädt von Hugging Face herunter, aber diese Version liest lokal (schneller, keine Authentifizierung erforderlich).
- **Abhängigkeiten**: Erfordert `tiktoken`, `datasets`, `numpy`, `tqdm`. Bei Fehlern per pip installieren.
- **Skalierbarkeit**: Für das echte OpenWebText, auf einem Rechner mit 64 GB+ RAM und schnellem Speicher (SSD) ausführen. Die 10k-Beispiel-Aufteilung deutet darauf hin, dass dies möglicherweise für einen Teilbereich gedacht ist.

Dieses Skript wandelt Rohtext in ein trainierfertiges Format um, optimiert für Sprachmodelle wie GPT. Wenn Sie Fragen zur Modifikation haben (z.B. anderer Tokenizer oder Blockgröße), lassen Sie es mich wissen!