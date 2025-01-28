---
audio: true
lang: de
layout: post
title: DeepSeek-API-Nutzung
translated: true
---

## DeepSeek

In einem Monat kosteten mich 15 Millionen Tokens etwa 23,5 CNY.

Das war mein Verbrauch an einem Tag:

| Typ              | Tokens    |
|-------------------|-----------|
| Eingabe (Cache-Treffer)  | 946,816   |
| Eingabe (Cache-Fehler) | 2,753,752 |
| Ausgabe            | 3,100,977 |

Die Berechnung lautet wie folgt:

0,94 * 0,1 + 2,75 * 1 + 3,10 * 2 = 11,83

Daher hängt der Tokenverbrauch je nach Aufgabe stark von der Eingabe (Cache-Fehler) und der Ausgabe ab.

Dieses Ergebnis stimmt mit den erwarteten Kosten überein.

[DeepSeek API Pricing](https://api-docs.deepseek.com/quick_start/pricing/)

{: .centered }
![](assets/images/deepseek/d.jpg)
*Quelle: Eigener Screenshot*{: .caption }

## Mistral

Modell: `mistral-large-2411`

An einem Tag verbrauchte mein Mistral-Konto folgende Tokens:

| Typ   | Tokens  | Kosten (USD) |
|--------|---------|------------|
| Gesamt  | 772,284 | 3,44       |
| Ausgabe | 474,855 | 2,85       |
| Eingabe | 297,429 | 0,59       |

Die Preisgestaltung für Mistral Large ist wie folgt:

*   Eingabe: 2 USD pro Million Tokens
*   Ausgabe: 6 USD pro Million Tokens