---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Unterschiede in der Struktur von Wikipedia-Dump-Dateien
translated: true
type: note
---

Der entscheidende Unterschied liegt darin, wie der vollständige Wikipedia-Artikeltext über mehrere Dateien aufgeteilt wird – insbesondere, ob eine `.xml.bz2`-Datei nur einen Revisionsstrom enthält (Non-Multistream) oder viele komprimierte Ströme, die zusammengebündelt sind (Multistream).

### 1. Non-Multistream-Dumps (älterer Stil oder die standardmäßigen "pages-articles"-Dateien)
Beispiel-Dateiname:  
`enwiki-20251101-pages-articles1.xml-p1p41242.bz2`

- Jede `.xml.bz2`-Datei enthält einen Teil der Seiten (z.B. Seiten 1–41242) in Page-ID-Reihenfolge.
- Innerhalb der Datei gibt es genau eine kontinuierliche `<page>` … `<page>` … Sequenz.
- Alle Revisionen einer einzelnen Seite sind zusammen innerhalb dieses einen Page-Tags (die neueste Revision + ältere, falls "aktuell + Verlauf" angefordert wurde).
- Um einen einzelnen Artikel zu extrahieren, dekomprimiert und parst man einfach die große XML-Datei normal mit jedem XML/BZ2-Tool.
- `wget -c` funktioniert auf einfache Weise perfekt: Es setzt genau dort fort, wo es aufgehört hat, da die Datei ein einzelner Bzip2-Stream ist.

### 2. Multistream-Dumps (Dateien, die "multistream" im Namen enthalten)
Beispiel-Dateiname (der von Ihnen verlinkte):  
`enwiki-20251101-pages-articles-multistream1.xml-p1p41242.bz2`

- Derselbe Seitenbereich (p1p41242) wird abgedeckt, aber der Volltext jeder Revision wird nicht mehr in der Haupt-XML-Datei gespeichert.
- Stattdessen:
  - Die Haupt-XML-Datei enthält nur Metadaten (Titel, ID, Einschränkungen, Zeitstempel der letzten Revision usw.) und einen Zeiger (Byte-Offset + Länge) darauf, wo sich der eigentliche Revisionstext befindet.
  - Die eigentlichen Revisionstexte werden separat in vielen kleinen komprimierten Strömen innerhalb derselben `.bz2`-Datei gespeichert (daher "Multistream").
- Es gibt usually eine Begleitdatei `...-multistream-index1.txt.bz2`, die die genauen Byte-Offsets für jede Seite/Revision enthält, damit Tools direkt zum richtigen komprimierten Stream springen und nur diesen Text extrahieren können, ohne die gesamte 10–30 GB große Datei dekomprimieren zu müssen.

### Warum ist das für `wget -c` relevant?

In der Praxis verhalten sich beide Befehle:

```bash
wget -c https://.../enwiki-20251101-pages-articles1.xml-p1p41242.bz2
wget -c https://.../enwiki-20251101-pages-articles-multistream1.xml-p1p41242.bz2
```

aus Sicht von wget genau gleich: Beide sind normale einzelne Bzip2-Dateien, sodass der wiederaufnehmbare Download mit `-c` in beiden Fällen perfekt funktioniert.

Der Unterschied zeigt sich erst, wenn man beginnt, die heruntergeladene Datei zu verarbeiten.

### Zusammenfassungstabelle

| Merkmal                              | Non-Multistream (regulär)                      | Multistream                                      |
|--------------------------------------|-------------------------------------------------|--------------------------------------------------|
| Dateiname enthält                   | `-pages-articlesN.xml-...bz2`                  | `-pages-articles-multistreamN.xml-...bz2`        |
| Speicherort des Artikeltextes       | Innerhalb der XML `<page><revision><text>...</text></revision></page>` | Außerhalb der XML, in separaten komprimierten Strömen |
| Dateigröße (für denselben Seitenbereich) | Viel größer (oft 2–3×)                        | Viel kleiner                                    |
| Direktzugriff / Einzelseitenextraktion | Sehr langsam (ganze Datei muss dekomprimiert werden) | Sehr schnell (mit der Indexdatei)                  |
| Tools, die es direkt verstehen      | Jeder XML-Parser (SAX, xmltodict, etc.)           | wikimedia’s dump-generator tools, pywiki, mwxml, etc. |
| Begleit-Indexdatei erforderlich?    | Nein                                            | Ja (`-multistream-index....txt.bz2`)            |
| `wget -c`-Wiederaufnahmefähigkeit   | Perfekt                                         | Perfekt (immer noch eine Bzip2-Datei)                   |

### Welche sollten Sie also herunterladen?

- Wenn Sie nur einen vollständigen sequenziellen Durchlauf einmal durchführen möchten (z.B. um ein Sprachmodell zu trainieren), sind die Non-Multistream-Dateien einfacher.
- Wenn Sie jemals einzelne Seiten schnell nachschlagen möchten oder Ihnen Speicherplatz und Extraktionsgeschwindigkeit wichtig sind, sollten Sie immer dem Multistream + Index-Paar den Vorzug geben. Fast alle ernsthaften Wikimedia-Verarbeitungstools (WikiExtractor, gensim’s WikiCorpus, jawiki scripts, etc.) erwarten oder empfehlen heutzutage die Multistream-Version.

Beide Dateien können Sie ohne Probleme mit `wget -c` wiederaufnehmen; der "Multistream"-Teil ändert nur, was sich *innerhalb* der Datei befindet, nicht wie HTTP/wget sie sieht.