---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Wikipedia-Download-Leitfaden
translated: true
type: note
---

Dies ist ein Verzeichnislisting von einem der offiziellen Wikimedia-Download-Mirrors (normalerweise https://dumps.wikimedia.org/enwiki/latest/).  
Es enthält alle verschiedenen Möglichkeiten, die aktuellen englischen Wikipedia-Artikel (Stand Anfang November 2025) herunterzuladen.

### Hauptformate und was sie tatsächlich enthalten

| Dateinamen-Muster | Was es ist | Ungefähre Größe (unkomprimiert) | Am besten für LLM-Training? | Anmerkungen |
| --- | --- | --- | --- | --- |
| `enwiki-latest-pages-articles.xml.bz2` | Eine einzige riesige Datei mit **allen** Artikeln + Diskussionsseiten, Vorlagen, Weiterleitungen etc. | ~85–90 GB unkomprimiert | Ja, sehr häufig verwendet | Am einfachsten, wenn Sie Platz und Bandbreite haben |
| `enwiki-latest-pages-articles1.xml-p1p41242.bz2`  … bis zu … `enwiki-latest-pages-articles27.xml-…` | Die gleichen Daten, aber in 27 kleinere Teile aufgeteilt (Multistream) | Jeweils ~200–600 MB komprimiert → gesamt immer noch ~85–90 GB unkomprimiert | Ja, beliebteste Wahl | Ermöglicht parallelen Download und einfaches Wiederaufnehmen |
| `enwiki-latest-pages-articles-multistreamX.xml.bz2` (z.B. multistream27) | Die eigentlichen großen komprimierten Datendateien, die zur oben genannten geteilten Version gehören | 300–600 MB pro Datei komprimiert | Dies sind die echten gewünschten Datendateien | Sie benötigen diese + die Indexdateien |
| `enwiki-latest-pages-articles-multistreamX.xml.bz2.md5` / `.meta` | Prüfsummen- und kleine Metadaten-Dateien | < 1 KB | Nicht für Text benötigt | Nur zur Überprüfung der Downloads |
| `enwiki-latest-pages-articles-multistream-indexX.xml.bz2` | Indexdateien, die angeben, welcher Artikel an welchem Byte-Offset in den großen Multistream-Dateien liegt | ~30–60 MB pro Datei komprimiert | Erforderlich bei Verwendung von Multistream | Benötigt für schnellen Direktzugriff; die meisten Verarbeitungsskripte erwarten sie |

### Empfehlung: Was fast alle im Jahr 2025 für das Training von Modellen verwenden

Der de-facto Standardweg (verwendet von LLaMA, Mistral, Qwen, DeepSeek, Gemma, Phi, etc.) ist:

Laden Sie die **27 Multistream-Dateien + ihre 27 Indexdateien** herunter  
(das ist alles, was mit `enwiki-latest-pages-articlesXX.xml-p…p….bz2` und den passenden `…-indexXX…bz2` beginnt)

Oder noch einfacher: Laden Sie einfach die **einzelne riesige Datei** herunter, wenn Ihre Verbindung und Festplatte damit umgehen können:

```
enwiki-latest-pages-articles.xml.bz2    ← 24,6 GB komprimiert, ~85–90 GB unkomprimiert
```

Beide enthalten exakt die gleichen rohen XML-Daten (alle Artikel im Haupt-Namensraum + viele zusätzliche Seiten).

### Warum nicht die kleinen Dateien (multistream3.xml-p…, multistream4.xml-p… etc.)?
Dies sind sehr alte Aufteilungen aus den Jahren 2010–2015, die nur einen winzigen Teil der Wikipedia enthalten (Artikel, die damals zufällig in diesen Seiten-ID-Bereich fielen). Sie werden nur aus historischen Gründen aufbewahrt und sind heute praktisch nutzlos.

### Schnellstart-Befehle (2025-Dump)

Paralleler Download der empfohlenen 27+27 Dateien (schnellste Methode):

```bash
# Liste der Dateien abrufen
wget -q https://dumps.wikimedia.org/enwiki/latest/ -O - | \
  grep -E 'enwiki-latest-pages-articles[0-9]+[02468]\.xml-p[0-9]+p[0-9]+\.bz2"' | \
  sed -e 's/.*href="//' -e 's/".*//' | \
  xargs -n1 -P10 wget https://dumps.wikimedia.org/enwiki/latest/

# Auch die passenden Indexdateien herunterladen
wget -q https://dumps.wikimedia.org/enwiki/latest/ -O - | \
  grep -E 'enwiki-latest-pages-articles-multistream-index' | \
  sed -e 's/.*href="//' -e 's/".*//' | \
  xargs -n1 -P10 wget https://dumps.wikimedia.org/enwiki/latest/
```

Oder nur die einzelne Datei (einfachste Methode):

```bash
wget https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2
```

Danach verarbeiten Sie sie normalerweise mit Tools wie:
- wikiextractor (Python) → bereinigt Text
- der Hugging Face `datasets` Wikipedia-Loader (erledigt bereits alles für Sie)
- DeepSeek's oder EleutherAI's Verarbeitungsskripte, etc.

Kurz gesagt:  
Laden Sie entweder die einzelne 24 GB große `enwiki-latest-pages-articles.xml.bz2` oder die 27 geteilten Dateien + Indexes herunter. Alles andere in dieser Liste sind entweder Prüfsummen, alter nutzloser Inhalt oder Metadaten, die Sie für das Training nicht benötigen.