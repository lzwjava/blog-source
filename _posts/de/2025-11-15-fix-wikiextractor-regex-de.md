---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Behebe den Wikiextractor-Python-3.13-Regex-Fehler
translated: true
type: note
---

Der Fehler, auf den Sie stoßen, liegt an einem Kompatibilitätsproblem im `wikiextractor`-Paket mit der strengeren Handhabung von regulären Ausdrücken in Python 3.13. Insbesondere wird das Flag `(?i)` im Regex-Muster als globales Flag interpretiert, es befindet sich jedoch nicht am Anfang des Ausdrucks, was zum `re.PatternError` führt.

Um dies zu beheben, bearbeiten Sie die Datei `/home/lzw/.local/lib/python3.13/site-packages/wikiextractor/extract.py` und ändern Sie Zeile 378 (oder die nahegelegene Definition von `ExtLinkBracketedRegex`) wie folgt:

- Original: `'\\[(((?i)' + '|'.join(wgUrlProtocols) + ')' + EXT_LINK_URL_CLASS + r'+)\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\]',`
- Geändert: `'\\[(((?i:' + '|'.join(wgUrlProtocols) + ')' + EXT_LINK_URL_CLASS + r'+)\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\]',`

Dies fügt ein `:` nach `(?i` hinzu, wodurch es zu einem lokalen Inline-Flag `(?i:...)` wird, das nur auf die Protokoll-Übereinstimmungsgruppe zutrifft. Dies behebt den Parsing-Fehler.

Zusätzlich stammen die `SyntaxWarning: invalid escape sequence '\\['`-Warnungen von Strings, die keine Raw-Strings sind und Escape-Sequenzen enthalten, die Python 3.13 strenger behandelt (obwohl sie nicht den Hauptfehler verursachen). Sie können diese vorerst ignorieren oder, falls sie Sie stören, diese Strings in derselben Datei in Raw-Strings ändern (z.B. `r'\\['`).

Nach der Bearbeitung führen Sie `wikiextractor *.bz2` erneut aus. Wenn das Paket veraltet ist, ziehen Sie in Betracht, nach Updates via `pip install --upgrade wikiextractor` zu suchen oder als Workaround eine virtuelle Umgebung mit einer älteren Python-Version (z.B. 3.10) zu verwenden.