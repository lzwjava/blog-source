---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Beheben des Tiktoken-Multiprocessing-Pickle-Fehlers
translated: true
type: note
---

Dein Fehler tritt häufig auf, wenn du `datasets.map(..., num_proc>1)` mit einem benutzerdefinierten Tokenizer (wie dem Tiktoken-Encoder, der im nanoGPT FineWeb-Skript verwendet wird) verwendest – der Tokenizer lädt die BPE-Datei (`cl100k_base.tiktoken` oder ähnlich) und dieses Datei-Handle **kann nicht gepickelt werden**, wenn es an Subprozesse unter Linux (fork-basiertes Multiprocessing) gesendet wird.

Die Kindprozesse stürzen sofort ab → "One of the subprocesses has abruptly died".

### Schnelle Lösung (funktioniert in 99% der Fälle)

Editiere `data/fineweb/prepare.py` und erzwinge, dass die Tokenisierung **nur im Hauptprozess** läuft:

```python
# Um Zeile 80-85, finde den .map()-Aufruf und ändere num_proc=8 → num_proc=1

tokenized = raw_datasets.map(
    tokenize,
    num_proc=1,               # ← ändere diese Zeile (oder lösche das Argument einfach)
    desc="tokenizing the splits",
)
```

Es wird langsamer sein (Single-Core), aber es funktioniert zuverlässig. Bei FineWeb-10B dauert dies je nach CPU/Festplatte ~30-60 Minuten.

### Bessere Lösung (behalte Multiprocessing, bleibt schnell)

Sorge dafür, dass der Tokenizer träge innerhalb des Worker-Prozesses geladen wird, anstatt im globalen Scope.

Ersetze die aktuelle Tokenizer-Erstellung (um Zeile 40-50) mit diesem Muster:

```python
import tiktoken

# Entferne den globalen encoder = tiktoken.get_encoding("cl100k_base")

def get_encoder():
    """Lade Tokenizer träge in jedem Subprozess"""
    return tiktoken.get_encoding("cl100k_base")

def tokenize(example):
    enc = get_encoder()                                   # ← wird pro Prozess geladen
    ids = enc.encode_ordinary(example["text"])
    ids.append(enc.eot_token)  # oder was auch immer das Skript tut
    return {"ids": ids, "len": len(ids)}
```

Dann behalte `num_proc=8` (oder eine beliebige Zahl). Auf diese Weise lädt jeder Worker seine eigene Kopie der .tiktoken-Datei nach dem Forking → keine Pickling-Probleme.

### Noch schnellere Alternative (empfohlen für wiederholte Läufe)

Lade die 10B/100B FineWeb-Edu-Shards vorab von Hugging Face herunter und verwende Karpathys aktualisiertes Skript, das direkt auf den Parquet/Arrow-Dateien arbeitet, anstatt der riesigen .txt-Datei:

```bash
# Viel schneller und umgeht diesen Bug komplett
python data/fineweb/prepare_fineweb.py --version 10B
# oder 100B
```

Das neue Skript (hinzugefügt ~2024) verwendet den offiziellen HF-Datensatz und ist multiprocessing-sicher.

### Zusammenfassung

| Lösung                            | Geschwindigkeit | Komplexität | Empfehlung       |
|-----------------------------------|-----------------|-------------|------------------|
| `num_proc=1`                      | Langsam         | 1 Zeile     | Schnelle Lösung  |
| Träger Encoder in tokenize()      | Schnell         | kleine Änderung | Beste für .txt |
| Neues prepare_fineweb.py Skript verwenden | Am schnellsten | neuer Befehl | Empfohlen        |

Wähle einen Ansatz und du wirst diesen Fehler sofort umgehen. Lass mich wissen, welchen Weg du nimmst, und ich gebe dir bei Bedarf den genauen Patch!