---
audio: false
lang: de
layout: post
title: DeepSeek API Nutzung
translated: true
---

## DeepSeek

In einem Monat kosteten mich 15 Millionen Tokens etwa 23,5 CNY.

Das war mein Verbrauch an einem Tag:

| Type               | Tokens    |
|--------------------|-----------|
| Input (Cache Hit)  | 946,816   |
| Input (Cache Miss) | 2,753,752 |
| Output            | 3,100,977 |

Die Berechnung erfolgt wie folgt:

0.94 * 0.1 + 2.75 * 1 + 3.10 * 2 = 11.83

Daher hängt der Tokenverbrauch je nach Aufgabe hauptsächlich von der Eingabe (Cache Miss) und der Ausgabe ab.

Dieses Ergebnis stimmt mit den erwarteten Kosten überein.

[DeepSeek API Pricing](https://api-docs.deepseek.com/quick_start/pricing/)

{: .centered }
![](assets/images/deepseek/d.jpg)
*Quelle: Self-Screenshot*{: .caption }

## Mistral

Der Verbrauch meines Mistral-Kontos an einem Tag war wie folgt (Modell: `mistral-large-2411`):

| Type   | Tokens  | Kosten (USD) |
|--------|---------|--------------|
| Total  | 772,284 | 3.44         |
| Output | 474,855 | 2.85         |
| Input  | 297,429 | 0.59         |

Die Preisgestaltung für Mistral-Modelle ist wie folgt:

| Model                | Input (USD pro Million Tokens) |  Output (USD pro Million Tokens) |
|----------------------|------------------------------|---------------------------------|
| `mistral-large-2411` | 2                            | 6                               |
| `mistral-small-latest`| 0.2                          | 0.6                             |