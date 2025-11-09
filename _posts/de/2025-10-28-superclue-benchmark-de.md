---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: 'SuperCLUE: Chinesischer LLM-Benchmark'
translated: true
type: note
---

SuperCLUE ist ein umfassender Benchmark-Satz zur Bewertung chinesischer Large Language Models (LLMs). Er baut auf dem ursprünglichen CLUE-Benchmark (Chinese Language Understanding Evaluation) auf und erweitert ihn, um fortgeschrittene Fähigkeiten von LLMs zu bewerten, anstatt nur kleinerer Modelle. Entwickelt wurde SuperCLUE vom CLUEbenchmark-Team – einer gemeinsamen Initiative von Forschern aus Institutionen wie der Tsinghua-Universität und Unternehmen im chinesischen KI-Ökosystem. SuperCLUE wurde erstmals 2023 eingeführt, um Lücken bei der Bewertung chinesischer LLMs nach internationalen Standards zu schließen.

### Wichtige Merkmale
- **Schwerpunkte**: Es bewertet Modelle in vier Hauptbereichen:
  - Sprachverständnis und -generierung (z. B. Leseverständnis, Zusammenfassung).
  - Fachkenntnisse und Wissen (z. B. mathematisches Denken, Coding).
  - Agent Intelligence (z. B. Werkzeugnutzung, Planung).
  - Sicherheit (z. B. Bias-Erkennung, ethische Ausrichtung).
- **Struktur**: Unterteilt in 12 Kernaufgaben, mit Datensätzen wie SuperCLUE-Math6 für mehrstufige Mathematikprobleme.
- **Zweck**: Hilft, die Fortschritte in der chinesischen KI zu verfolgen, und hebt sowohl Stärken (z. B. Handling kultureller Nuancen) als auch Lücken im Vergleich zu globalen Modellen wie der GPT-Serie hervor.
- **Aktualisierungen**: Stand Mitte 2025 wird es für regelmäßige Zwischenbewertungen verwendet, wobei Bestenlisten zeigen, dass chinesische Modelle wie Qwen und GLM den Rückstand zu internationalen Modellen verringern.

Der Benchmark ist Open-Source und wird aktiv gepflegt. Bewertungen werden oft über arXiv-Papers und GitHub geteilt.

[SuperCLUE: A Comprehensive Chinese Large Language Model Benchmark](https://arxiv.org/abs/2307.15020)  
[SuperCLUE GitHub Repository](https://github.com/CLUEbenchmark/SuperCLUE)  
[ChinAI: SuperCLUE Benchmarks —2025 Midyear Check-in](https://chinai.substack.com/p/chinai-324-superclue-large-model)