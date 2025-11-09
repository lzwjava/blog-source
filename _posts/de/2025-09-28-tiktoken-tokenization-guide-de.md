---
audio: false
generated: true
image: false
lang: de
layout: post
model: anthropic/claude-sonnet-4
title: TikToken Tokenisierungsleitfaden und Beispiele
translated: true
type: note
---

Dieser Code demonstriert, wie die **TikToken**-Bibliothek verwendet wird, OpenAIs Tokenizer zum Zählen und Verarbeiten von Tokens in Text, der an Sprachmodelle wie GPT-3.5, GPT-4 usw. gesendet wird.

## Was TikToken macht

TikToken wandelt Text in **Tokens** um – die grundlegenden Einheiten, die Sprachmodelle verarbeiten. Jeder Token entspricht grob einem Wort oder einem Teil eines Wortes. Das Verständnis von Tokenisierung ist entscheidend, weil:

- Die API-Kosten auf der Token-Anzahl basieren
- Modelle haben Token-Limits für Eingabe/Ausgabe
- Die Token-Anzahl beeinflusst die Verarbeitungsgeschwindigkeit

## Code-Überblick

### 1. Grundlegendes Kodieren (`basic_encoding()`)
```python
enc = tiktoken.encoding_for_model("gpt-3.5-turbo")
tokens = enc.encode("Hello, how are you doing today?```
- Erstellt einen Tokenizer für GPT-3.5-turbo
- Wandelt Text in eine Liste von Token-IDs um: `[9906, 11, 1268, 527, 499, 3815, 3432, 30]`
- Zeigt, dass "Hello, how are you doing today?" = 8 Tokens entspricht
- Kann Tokens zurück in den ursprünglichen Text dekodieren

### 2. Modellvergleich (`different_models()`)
Vergleicht, wie verschiedene Modelle denselben Text tokenisieren:
- **GPT-4**: 10 Tokens für "The quick brown fox jumps over the lazy dog."
- **GPT-3.5-turbo**: 10 Tokens (dieselbe Kodierung)
- **text-davinci-003**: 10 Tokens (dieselbe Kodierung)

Verschiedene Modelle können unterschiedliche Tokenizer verwenden, daher kann die Token-Anzahl variieren.

### 3. Stapelverarbeitung (`batch_processing()`)
Zeigt, wie mehrere Texte effizient verarbeitet werden:
- Verarbeitet 3 Nachrichten unterschiedlicher Länge
- Berechnet die gesamten Tokens über alle Nachrichten (15 insgesamt)
- Nützlich zur Kostenschätzung beim Senden mehrerer Nachrichten

### 4. Spezielle Tokens (`special_tokens()`)
Behandelt spezielle Steuer-Tokens wie `<|endoftext|>`:
- Zeigt verfügbare spezielle Tokens für das Modell
- Demonstriert die Kodierung von Text, der spezielle Tokens enthält
- Verwendet `allowed_special="all"`, um spezielle Tokens zu verarbeiten

### 5. Effizientes Zählen (`count_tokens_efficiently()`)
Zwei Methoden zum Zählen von Tokens:
- **Methode 1**: Tokens speichern und dann zählen (`len(enc.encode(text))`)
- **Methode 2**: Direktes Zählen (speichereffizienter für große Texte)
- Berechnet das Token-pro-Wort-Verhältnis (1.29 in diesem Beispiel)

## Praktische Anwendungen

1. **Kostenschätzung**: API-Kosten vor Anfragen berechnen
2. **Eingabevalidierung**: Sicherstellen, dass Text innerhalb der Token-Limits des Modells liegt
3. **Batch-Optimierung**: Nachrichten effizient für API-Aufrufe gruppieren
4. **Leistungsüberwachung**: Token-Verbrauch in Anwendungen verfolgen

## Wichtige Erkenntnisse aus der Ausgabe

- Einfache Phrasen verwenden weniger Tokens als erwartet
- Die Token-Anzahl entspricht nicht immer der Wortanzahl
- Verschiedene Modelle können unterschiedlich tokenisieren
- Spezielle Tokens erfordern sorgfältige Handhabung

Diese Bibliothek ist unerlässlich für alle, die Anwendungen mit OpenAIs APIs erstellen, da sie eine präzise Token-Zählung bietet, die mit dem übereinstimmt, wofür die API tatsächlich Gebühren berechnet.