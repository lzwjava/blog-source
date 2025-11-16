---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Behebung von Python-3.13-Regex-Fehlern
translated: true
type: note
---

Der Fehler, den Sie sehen, wird dadurch verursacht, dass **Python 3.13** strenger bei der Syntax regulärer Ausdrücke ist als vorherige Versionen.

Konkret ist diese Zeile in `wikiextractor/extract.py` (ungefähr Zeile 378) in Python 3.13 nun ungültig:

```python
ExtLinkBracketedRegex = re.compile(
    '\\[(((?i)' + '|'.join(wgUrlProtocols) + ')' + EXT_LINK_URL_CLASS + r'+)\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\]',
    re.S | re.U)
```

Das Problem ist das eingebettete `(?i)` Flag, das mitten in der Zeichenkette nach der String-Verkettung platziert ist. Ab Python 3.12/3.13 sind **eingebettete Flags wie `(?i)` nur noch am Anfang des Regex-Musters erlaubt**.

### Schnelle Lösung (funktioniert mit Python 3.13)

Bearbeiten Sie die Datei:

```bash
~/.local/lib/python3.13/site-packages/wikiextractor/extract.py
```

Gehen Sie zu Zeile ~378 und ersetzen Sie den defekten Block mit dieser korrigierten Version:

```python
# Alte, defekte Version (scheitert bei Python 3.13)
# ExtLinkBracketedRegex = re.compile(
#     '\\[(((?i)' + '|'.join(wgUrlProtocols) + ')' + EXT_LINK_URL_CLASS + r'+)\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\]',
#     re.S | re.U)

# Korrigierte Version – verschiebt das Flag für Groß-/Kleinschreibung in die re.compile Flags
protocol_pattern = '|'.join(wgUrlProtocols)
ExtLinkBracketedRegex = re.compile(
    r'\\['
    r'(((' + protocol_pattern + r')' + EXT_LINK_URL_CLASS + r'+)'
    r'\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\])',
    re.IGNORECASE | re.DOTALL | re.UNICODE
)
```

Oder noch sauberer (empfohlen):

```python
ExtLinkBracketedRegex = re.compile(
    r'\\['
    r'(((' + '|'.join(wgUrlProtocols) + r')' + EXT_LINK_URL_CLASS + r'+)'
    r'\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\])',
    re.I | re.S | re.U
)
```

`re.I` ist dasselbe wie `re.IGNORECASE` und kann als Flag übergeben werden, anstatt `(?i)` in das Muster einzubetten.

### Alternative Lösungen

1. Verwenden Sie Python 3.11 oder 3.12 (am einfachsten, wenn Sie nicht patchen möchten)
   ```bash
   python3.11 -m pip install wikiextractor
   # dann ausführen mit python3.11 wikiextractor ...
   ```

2. Verwenden Sie den gewarteten Fork, der bereits die Python 3.13-Kompatibilität behebt:
   ```bash
   pip uninstall wikiextractor
   pip install git+https://github.com/attardi/wikiextractor.git
   ```

   Giuseppe Attardis Fork wurde für Python 3.12+ aktualisiert und funktioniert einwandfrei unter 3.13.

3. Verwenden Sie die sehr schnelle, moderne Alternative (sehr empfohlen für große Dumps):
   ```bash
   pip install wikiextractor-ng   # oder "wiki-dump-tools", "wikitextprocessor", etc.
   ```

Nachdem Sie den Patch angewendet oder zum korrigierten Fork gewechselt haben, funktioniert Ihr Befehl wieder:

```bash
wikiextractor *.bz2
```

Sagen Sie Bescheid, wenn Sie einen One-Liner-Patch oder den genauen `sed`-Befehl zur automatischen Korrektur wünschen.