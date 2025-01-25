---
audio: true
lang: de
layout: post
title: DeepSeek API Verwendung
translated: true
---

In einem Monat haben mich 15 Millionen Tokens ungefähr 23,5 CNY gekostet.

Dies war meine Nutzung an einem Tag:

| Typ               | Tokens    |
|-------------------|-----------|
| Eingabe (Cache Hit)  | 946,816   |
| Eingabe (Cache Miss) | 2,753,752 |
| Ausgabe            | 3,100,977 |

Die Berechnung lautet wie folgt:

0.94 * 0.1 + 2.75 * 1 + 3.10 * 2 = 11.83

Je nach Aufgabe hängt die Token-Nutzung also stark von der Eingabe (Cache Miss) und der Ausgabe ab.

Dieses Ergebnis entspricht den erwarteten Kosten.

[DeepSeek API-Preise](https://api-docs.deepseek.com/quick_start/pricing/)

{: .centered }
![](assets/images/deepseek/d.jpg){: .responsive }
*Quelle: Eigenes Screenshot*{: .caption }