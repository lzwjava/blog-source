---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Textextraktion aus Wikipedia-Dumps
translated: true
type: note
---

Hier sind die gängigsten und effektivsten Methoden, um Klartext aus Wikipedia `.bz2`-Dump-Dateien wie Ihrer (`enwiki-latest-pages-articles1.xml-p1p41242.bz2`) zu extrahieren.

### Empfohlene Tools & Methoden (vom einfachsten bis zum effizientesten)

#### 1. Verwende wikiextractor (am besten für die meisten Benutzer – schnell und sauber)
Dies ist das Standard-Tool, das von fast jedem im Bereich NLP/ML für Wikipedia-Dumps verwendet wird.

```bash
# Installation (einmalig)
pip install wikiextractor

# Text extrahieren (entfernt Vorlagen, Tabellen etc., liefert sauberen Text pro Artikel)
wikiextractor enwiki-latest-pages-articles1.xml-p1p41242.bz2 --output wiki_text
```

- Ausgabe: Erstellt einen Ordner `wiki_text/` mit Unterordnern AA, AB, … die `.bz2`-Dateien mit sauberem JSON/Text enthalten.
- Um Klartext zu erhalten (ein Artikel pro Zeile):
```bash
wikiextractor enwiki-latest-pages-articles1.xml-p1p41242.bz2 --processes 8 -o wiki_text --json
# Dann JSON bei Bedarf in Klartext umwandeln
find wiki_text -name '*' -exec cat {} \; | grep '"text":' | sed 's/.*"text": "//;s/"$//' > all_text.txt
```

#### 2. Verwende gensims WikiCorpus (ideal, wenn Sie NLP in Python durchführen)

```python
from gensim.corpora import WikiCorpus

# Dies verarbeitet automatisch .bz2 und extrahiert Text + tokenisiert
wiki = WikiCorpus("enwiki-latest-pages-articles1.xml-p1p41242.bz2", dictionary=False)

# Über Artikel iterieren
with open("output.txt", "w", encoding="utf-8") as f:
    for i, text in enumerate(wiki.get_texts()):
        f.write(" ".join(text) + "\n")
        if i % 10000 == 0:
            print(f"Processed {i} articles")
```

#### 3. Einfaches bzip2 + grep/awk (schnell & schmutzig, keine Bereinigung)

```bash
# Einfach dekomprimieren und rohes XML ansehen
bzip2 -dc enwiki-latest-pages-articles1.xml-p1p41242.bz2 | less

# Nur den <text>-Inhalt extrahieren (sehr grob, behält Wiki-Markup bei)
bzip2 -dc enwiki-latest-pages-articles1.xml-p1p41242.bz2 | \
  sed -n '/<text /,/<\/text>/p' | \
  sed 's/<text[^>]*>//g;s/<\/text>//g' > raw_text_with_markup.txt
```

#### 4. Wenn Sie den kompletten Dump haben und alles schnell möchten (parallel)
Ihre Datei ist nur der erste Teil (p1p41242), aber wenn Sie später alle ~30+ Teile haben:

```bash
# Alle parallel extrahieren
ls *.bz2 | xargs -P 8 -I {} wikiextractor {} --output wiki_extracted
```

### Zusammenfassung – Was ich Ihnen jetzt empfehle:

```bash
pip install wikiextractor
wikiextractor enwiki-latest-pages-articles1.xml-p1p41242.bz2 -o extracted_wiki --bytes 1M --json
```

Dies liefert Ihnen in wenigen Minuten saubere, lesbare Artikel (Ihre Datei ist nur ~2-3 GB komprimiert, also sehr handhabbar).

Lassen Sie mich wissen, wenn Sie möchten:
- Nur den Haupt-Namensraum (echte Artikel, keine Diskussionsseiten)
- Klartext anstelle von JSON
- Tokenisierte Ausgabe
- Chinesische Wikipedia stattdessen (zhwiki) – der Prozess ist identisch

Viel Erfolg beim Extrahieren! 🚀