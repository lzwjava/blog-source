---
audio: false
generated: true
lang: de
layout: post
title: Api-Verwendung von DeepSeek und Mistral
translated: true
---

## DeepSeek

In einem Monat kosteten mich 15 Millionen Tokens etwa 23,5 CNY.

Dies war meine Nutzung an einem Tag:

| Typ                | Tokens    |
|--------------------|-----------|
| Eingabe (Cache Treffer) | 946,816  |
| Eingabe (Cache Fehlschlag) | 2,753,752 |
| Ausgabe             | 3,100,977 |

Die Berechnung lautet:

0.94 * 0.1 + 2.75 * 1 + 3.10 * 2 = 11.83

Abhängig von der Aufgabe hängt der Tokenverbrauch in großem Maße von der Eingabe (Cache Fehlschlag) und Ausgabe ab.

Dieses Ergebnis stimmt mit den erwarteten Kosten überein.

[DeepSeek API Preise](https://api-docs.deepseek.com/quick_start/pricing/)

{: .centered }
![](assets/images/deepseek/d.jpg)
*Quelle: Selbst-Screenshot*{: .caption }

## Mistral

Die Preisgestaltung für die Mistral-Modelle lautet:

| Modell                 | Eingabe (USD pro Million Tokens) | Ausgabe (USD pro Million Tokens) |
|------------------------|-------------------------------|--------------------------------|
| `mistral-large-2411`   | 2                             | 6                               |
| `mistral-small-latest` | 0.2                           | 0.6                             |

Meine Mistral-Konto-Nutzung an einem Tag (Modell: `mistral-large-2411`):

| Typ    | Tokens  | Kosten (USD) |
|--------|---------|--------------|
| Gesamt | 772,284 | 3.44         |
| Ausgabe | 474,855 | 2.85         |
| Eingabe | 297,429 | 0.59         |

Für das Modell `mistral-small-2409` betrug die gesamte Nutzung 1,022,407 Tokens.

Angenommen, ein Drittel davon waren Eingabetokens und zwei Drittel Ausgabetokens:

Es gab 340,802 Eingabetokens und 681,605 Ausgabetokens.

Die Gesamtkosten werden daher berechnet als 340,802 * 0.2 / 1,000,000 + 681,605 * 0.6 / 1,000,000 = 0.07 + 0.41 = 0.48 USD.

Die Mistral-Konsole meldet eine Gesamtnutzungskosten von 0.43 USD, was in etwa unserer Berechnung entspricht.

## Grok

| Modell         | Eingabe (USD pro Million Tokens) | Ausgabe (USD pro Million Tokens) |
|----------------|-------------------------------|--------------------------------|
| `grok-2-latest` | 2                             | 10                              |