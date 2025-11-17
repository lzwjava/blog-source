---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Training an einem Einzigen Verketteten Textstrom
translated: true
type: note
---

In nanoGPT (und im Wesentlichen in jedem GPT-artigen Training, einschließlich des ursprünglichen GPT-2/GPT-3 Trainings), **muss man auf einem einzigen gigantischen, verketteten Textstrom trainieren**, und nicht auf einzelnen Artikeln/Dokumenten, die nacheinander als separate Sequenzen gefüttert werden.

Hier ist der Grund und die genaue praktische Umsetzung mit FineWeb (und in Andrejs nanoGPT-Code):

### Was Sie tun sollten (korrekte Methode)
1. Fügen Sie **alle** einzelnen Artikel zu **einer riesigen .txt-Datei** (oder mehreren großen Shard-Dateien) zusammen, getrennt nur durch ein spezielles Textende-Token `<|endoftext|>` (oder einen beliebigen anderen von Ihnen gewählten Separator).
2. Während des Trainings wird nanoGPT:
   - Den gesamten verketteten Text in ein riesiges Token-Array laden.
   - Es in Blöcke fester Länge aufteilen (z.B. block_size = 1024 Tokens).
   - Diese Blöcke überschreiten sehr häufig Dokumentgrenzen – das ist nicht nur in Ordnung, sondern sogar erwünscht.

Genau so hat OpenAI GPT-2 und GPT-3 trainiert, und so macht es Andrej auch mit Shakespeare, OpenWebText, FineWeb-Edu, etc.

### Was das Skript `extract_fineweb.py` tut
Das von Ihnen ausgeführte Skript macht bereits das Richtige:

```bash
$ python ./scripts/train/extract_fineweb.py
```

Es liest alle Parquet-Dateien, extrahiert nur die `text`-Spalte jeder Zeile (d.h. jeder Webseite/jedes Artikels), schreibt den Rohtext nacheinander in `fineweb_extracted.txt` und fügt (in den neuesten Versionen) automatisch den `<|endoftext|>`-Separator zwischen den Dokumenten ein.

Die resultierende Datei sieht also so aus:

```
<Artikel-1-Text> <|endoftext|> <Artikel-2-Text> <|endoftext|> <Artikel-3-Text> <|endoftext|> ...
```

Das ist perfekt. Sie sollten auf dieser einzelnen riesigen Datei trainieren (oder auf den shardeten Bin-Dateien, die `train.py` daraus erstellen wird).

### Was Sie NICHT tun sollten
- Füttern Sie **nicht** jeden Artikel als separates Beispiel/separate Sequenz an das Modell und setzen Sie die Attention für jeden Artikel zurück.
- Kürzen oder padden Sie **nicht** jeden Artikel auf exakt block_size und trainieren Sie nur innerhalb eines Dokuments.
- Verwenden Sie **kein** Document-level Batching, bei dem jede Sequenz im Batch ein vollständiges Dokument ist.

Das würde die Fähigkeit des Modells zerstören, langreichweitige Abhängigkeiten zu lernen, die sich über mehrere Dokumente erstrecken, und würde die Leistung drastisch verschlechtern.

### Zusammenfassung
Ja → Trainieren Sie auf **einer einzigen massiven, verketteten Textdatei** (genau das, was `extract_fineweb.py` erzeugt).  
Nein → Trainieren Sie **nicht** artikelweise als separate Sequenzen.

So wurden GPTs schon immer trainiert, und das ist der Grund, warum nanoGPTs `train.py` die Daten einfach als einen langen Tokenstrom behandelt.

Fahren Sie also einfach mit dem normalen nanoGPT-Workflow fort:

```bash
python scripts/train/extract_fineweb.py   # Das haben Sie bereits getan
python train.py --dataset=your_extracted_file_or_fineweb10B etc.
```

Sie sind auf dem richtigen Weg!