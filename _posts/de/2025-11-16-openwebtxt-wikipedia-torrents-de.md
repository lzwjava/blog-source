---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: OpenWebText- und Wikipedia-Dataset-Torrents
translated: true
type: note
---

### OpenWebText-Dataset-Torrents

OpenWebText ist eine Open-Source-Replikation von OpenAIs WebText-Dataset und besteht aus ~38 GB bereinigtem Text, der aus hoch bewerteten Reddit-Links extrahiert wurde (hauptsächlich Webseiten, die gescraped und nach Qualität gefiltert wurden). Es ist ein beliebiges großes Textkorpus für das Training von Sprachmodellen. Während der vollständige gescrapete Text nicht immer direkt als einzelner Torrent verfügbar ist, hier zuverlässige Optionen:

- **URLs-Liste (Gefiltert, ~480 MB)**: Eine vorgefilterte Liste von ~26 Millionen URLs, die für das Scraping von OpenWebText verwendet wurden. Sie können diese verwenden, um den Text selbst herunterzuladen und zu verarbeiten.
  - Torrent: [OpenWebText-urls-26M-filtered.xz](https://academictorrents.com/details/f5161721b322bca66ed74da32b963c1066e64312)
  - Quelle: Academic Torrents (von der Community geseedet).

- **URLs-Liste (Vollständig, ~1,75 GB)**: Die vollständige, deduplizierte URL-Liste aus Reddit-Beiträgen.
  - Torrent: [WebText dataset urls.txt.tar.gz](https://academictorrents.com/details/15f3494b2991e75194d3af72bf7afa5025a7abc3)
  - Quelle: Academic Torrents (von der Community geseedet).

- **Tokenisierte Version (~16 GB)**: GPT-2-tokenisierte Textdateien aus dem gescrapeten Korpus (395 Dateien, bereit für das Modelltraining).
  - Torrent: [OpenWebText (Gokaslan's distribution, 2019), GPT-2 Tokenized](https://academictorrents.com/details/36c39b25657ce1639ccec0a91cf242b42e1f01db)
  - Quelle: Academic Torrents (geseedet von OSUOSL und der Community).

Für das vollständige Rohtext-Korpus sollten Sie die offizielle Website für Direktdownloads (nicht Torrent-basiert) überprüfen oder die oben genannten URLs mit Scraping-Skripten aus dem [OpenWebText GitHub-Repo](https://github.com/eukaryote31/openwebtext) verwenden. Eine erweiterte Version, OpenWebText2 (~Multi-TB-Größe), ist über [EleutherAI's Repo](https://github.com/EleutherAI/openwebtext2) verfügbar, verwendet jedoch Streaming anstelle von Torrents.

### Wikipedia-Dump-Torrents

Wikipedia-Dumps sind monatliche XML-Exporte der gesamten Datenbank (Artikel, Versionen, Metadaten). Die englische Version ist riesig (~20-25 GB komprimiert für Abstracts, bis zu 100+ GB für den vollständigen Verlauf). Torrents werden von der Community gepflegt (inoffiziell, aber gegen offizielle Prüfsummen verifiziert) und werden von Wikimedia-Servern aus geseedet, um Zuverlässigkeit zu gewährleisten. Überprüfen Sie Downloads immer gegen die Hashes von [dumps.wikimedia.org](https://dumps.wikimedia.org/enwiki/latest/).

Die Hauptanlaufstelle für Torrents ist die [Meta-Wiki Data Dump Torrents page](https://meta.wikimedia.org/wiki/Data_dump_torrents#enwiki), die die neuesten englischen Wikipedia-Dumps auflistet (z.B. enwiki-20251101). Hier eine Zusammenfassung der letzten:

| Dump-Datum | Dateityp | Komprimierte Größe | Torrent-Link | Anmerkungen |
|-----------|-----------|-----------------|--------------|-------|
| 2025-11-01 | Pages-Articles (XML, nur Abstracts) | ~22 GB | [enwiki-20251101-pages-articles-multistream.xml.bz2](https://meta.wikimedia.org/wiki/Data_dump_torrents#enwiki) | Multistream-Format; am einfachsten für Textextraktion. |
| 2025-11-01 | Pages-Articles-History (XML, alle Versionen) | ~120 GB | [enwiki-20251101-pages-meta-history*.xml.bz2](https://meta.wikimedia.org/wiki/Data_dump_torrents#enwiki) | Beinhaltet alle Bearbeitungen; in Streams aufgeteilt für einfachere Handhabung. |
| 2025-10-01 | Pages-Articles (XML, nur Abstracts) | ~21 GB | [enwiki-20251001-pages-articles-multistream.xml.bz2](https://meta.wikimedia.org/wiki/Data_dump_torrents#enwiki) | Vorheriger Monatsdump; gut für historische Vergleiche. |

- **Vollständige Sammlung**: Durchsuchen Sie alle historischen englischen Wikipedia-Torrents in der [Academic Torrents Wikipedia Collection](https://academictorrents.com/collection/wikipedia) (beinhaltet ältere Dumps bis ca. 2010).
- **Kiwix ZIM Format**: Wenn Sie eine offline durchsuchbare Wikipedia (HTML, ~100 GB) möchten, probieren Sie [wikipedia_en_all_maxi_2024-01.zim.torrent](https://download.kiwix.org/zim/wikipedia/wikipedia_en_all_maxi_2024-01.zim.torrent) – von der Community geseedet, aber überprüfen Sie [Kiwix downloads](https://download.kiwix.org/zim/wikipedia/) auf Updates für 2025.

Um diese in Klartext zu verarbeiten, verwenden Sie Tools wie `wikiextractor` aus Python. Torrents reduzieren die Serverlast und setzen unterbrochene Downloads fort – verwenden Sie einen Client wie qBittorrent. Wenn Sie Dumps für andere Sprachen oder Teilmengen benötigen, hat die Meta-Wiki-Seite entsprechende Filter.