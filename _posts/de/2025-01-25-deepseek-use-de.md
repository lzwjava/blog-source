---
audio: true
lang: de
layout: post
title: Deepseek- und Mistral-API-Nutzung
translated: true
---

## DeepSeek

In einem Monat kosteten mich 15 Millionen Tokens etwa 23,5 CNY.

Das war mein Tagesverbrauch:

| Art              | Tokens    |
|-------------------|-----------|
| Eingabe (Cache-Treffer)  | 946,816   |
| Eingabe (Cache-Fehler) | 2,753,752 |
| Ausgabe            | 3,100,977 |

Die Berechnung erfolgt wie folgt:

0,94 * 0,1 + 2,75 * 1 + 3,10 * 2 = 11,83

Daher hängt der Token-Verbrauch je nach Aufgabe hauptsächlich von der Eingabe (Cache-Fehler) und der Ausgabe ab.

Dieses Ergebnis stimmt mit den erwarteten Kosten überein.

[DeepSeek API-Preise](https://api-docs.deepseek.com/quick_start/pricing/)

{: .centered }
![](assets/images/deepseek/d.jpg)
*Quelle: Eigener Screenshot*{: .caption }

## Mistral

Die Preisgestaltung für Mistral-Modelle ist wie folgt:

| Modell                | Eingabe (USD pro Million Tokens) | Ausgabe (USD pro Million Tokens) |
|-----------------------|----------------------------------|----------------------------------|
| `mistral-large-2411`  | 2                               | 6                                |
| `mistral-small-latest`| 0,2                             | 0,6                              |

Mein Tagesverbrauch im Mistral-Konto war wie folgt (Modell: `mistral-large-2411`):

| Art   | Tokens  | Kosten (USD) |
|--------|---------|--------------|
| Gesamt  | 772,284 | 3,44         |
| Ausgabe | 474,855 | 2,85         |
| Eingabe | 297,429 | 0,59         |

Für das Modell `mistral-small-2409` betrug der Gesamtverbrauch 1.022.407 Tokens.

Wenn davon 1/3 Eingabetokens und 2/3 Ausgabetokens waren:

Es gab 340.802 Eingabetokens und 681.605 Ausgabetokens.

Daher beträgt die Gesamtkostenberechnung 340.802 * 0,2 / 1.000.000 + 681.605 * 0,6 / 1.000.000 = 0,07 + 0,41 = 0,48 USD.

Die Mistral-Konsole meldet Gesamtkosten von 0,43 USD, was unserer Berechnung ungefähr entspricht.