---
audio: false
generated: true
image: false
lang: de
layout: post
title: Leitfaden zu KI-Modellkosten und Leistung
translated: true
type: note
---

Hier ist eine übersichtliche Aufschlüsselung der **Benchmark-Ergebnisse** und **API-Preise** für jedes Modell – Claude 4 Opus (auch als Claude Opus 4 bezeichnet), GPT‑5 (Standard/Vollversion), GPT‑5 Mini, GPT‑5 Nano, sowie o3 (OpenAI) und Claude 4 Sonnet – ohne Tabellen, um es übersichtlich und lesbar zu halten.

---

## Benchmark-Leistung (SWE-bench)

Dies zeigt, wie gut die Modelle bei Software-Engineering-Aufgaben abschneiden:

* **Claude 4 Opus (14. Mai 2025)**: 67,60
* **GPT‑5 (7. Aug. 2025, Medium Reasoning)**: 65,00
* **Claude 4 Sonnet (14. Mai 2025)**: 64,93 ([SWE-bench][1])

**Fazit**: Claude 4 Opus führt bei der SWE-bench-Leistung leicht an, dicht gefolgt von GPT-5 und Claude Sonnet.

---

## API-Preise (pro Million Tokens)

### **Claude 4 Opus**

* Input: **15 $**
* Output: **75 $** ([Anthropic][2], [LaoZhang AI][3], [Simon Willison’s Weblog][4])

### **GPT-5 (Standard/Vollversion)**

* Input: **1,25 $**
* Gecachte Eingabe (bei Wiederverwendung): **0,125 $**
* Output: **10 $** ([OpenAI][5])

### **GPT-5 Mini**

* Input: **0,25 $**
* Output: **2 $** ([OpenAI][5], [WIRED][6])

### **GPT-5 Nano**

* Input: **0,05 $**
* Output: **0,40 $** ([OpenAI][5], [WIRED][6])

### **o3-mini** (zum Vergleich)

* Preis verfügbar über o4‑mini-Referenz:
* Input: **1,10 $**, Output: **4,40 $** ([Simon Willison’s Weblog][4])

### **Claude 4 Sonnet**

* Input: **3 $**, Output: **15 $** ([LaoZhang AI][3])

---

## Schneller Vergleich – Die Highlights

* **Beste Leistung**: Claude 4 Opus übertrifft sowohl GPT-5 als auch Claude Sonnet in Coding-Benchmarks leicht.
* **Geringste Kosten pro Token**:

  * **GPT-5 Nano** ist bei weitem der günstigste – perfekt für einfache Aufgaben wie Zusammenfassungen.
  * **GPT-5 Mini** bietet eine gute Balance aus Geschwindigkeit und Erschwinglichkeit.
  * **GPT-5 Standard** bleibt sehr kosteneffektiv, besonders durch günstige Caches.
* **Claude-Modelle**, sowohl Opus als auch Sonnet, sind deutlich teurer pro Token, rechtfertigen ihren Preis aber durch stärkere Reasoning- und Agent-Fähigkeiten.

---

## Zusammenfassung (klar und knapp):

* **Claude 4 Opus**: Top-Leistung, hohe Kosten (15 $ Input / 75 $ Output).
* **GPT-5 (Vollversion)**: Hervorragende Leistung (knapp hinter Opus), viel günstiger (1,25 $ Input / 10 $ Output).
* **GPT-5 Mini**: Budgetfreundliche Option der Mittelklasse (0,25 $ Input / 2 $ Output).
* **GPT-5 Nano**: Ideal für einfache Aufgaben oder großangelegte, kostengünstige Nutzung (0,05 $ Input / 0,40 $ Output).
* **Claude 4 Sonnet**: Mittleres Kosten-Leistungs-Verhältnis (3 $ Input / 15 $ Output), aber Benchmark-Leistung etwas niedriger als bei den anderen.

---

Lass mich wissen, wenn du Hilfe bei der Schätzung der **monatlichen Kosten** für ein bestimmtes Nutzungsmuster benötigst oder Vergleiche unter Berücksichtigung von Prompt-Caching und Batch-Rabatten brauchst!

[1]: https://www.swebench.com/?utm_source=chatgpt.com "SWE-bench Leaderboards"
[2]: https://www.anthropic.com/pricing?utm_source=chatgpt.com "Pricing"
[3]: https://blog.laozhang.ai/ai-tools/claude-4-pricing-guide-2025/?utm_source=chatgpt.com "Claude 4.0 Pricing Guide: Complete Cost Analysis & Best ..."
[4]: https://simonwillison.net/2025/Aug/7/gpt-5/?utm_source=chatgpt.com "GPT-5: Key characteristics, pricing and model card"
[5]: https://openai.com/api/pricing/?utm_source=chatgpt.com "API Pricing"
[6]: https://www.wired.com/story/openais-gpt-5-is-here/?utm_source=chatgpt.com "OpenAI Finally Launched GPT-5. Here's Everything You ..."