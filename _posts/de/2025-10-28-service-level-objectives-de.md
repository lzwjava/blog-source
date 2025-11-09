---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Grundlagen von Service Level Objectives
translated: true
type: note
---

### Was ist ein Service Level Objective (SLO)?

Ein **Service Level Objective (SLO)** ist ein messbares Ziel, das das gewünschte Maß an Zuverlässigkeit, Leistung oder Verfügbarkeit für einen Dienst oder ein System definiert. Es ist ein Schlüsselkonzept in Site Reliability Engineering (SRE), bei dem SLOs als interne Ziele fungieren, um die Benutzerzufriedenheit zu gewährleisten, ohne Ressourcen zu überdimensionieren.

#### Wichtige Komponenten:
- **Service Level Indicator (SLI)**: Die tatsächlich gemessene Metrik (z. B. Anforderungslatenz, Fehlerrate oder Verfügbarkeitsprozentsatz).
- **Zielwert**: Ein spezifischer Schwellenwert oder Bereich (z. B. "99,9 % der Anfragen werden in unter 200 ms bedient").
- **Zeitfenster**: Der Zeitraum, über den der SLO ausgewertet wird (z. B. gleitender 28-Tage-Durchschnitt).

#### SLO vs. SLA:
- **SLO**: Interne, anspruchsvolle Ziele für das Engineering-Team (z. B. eine Verfügbarkeit von 99,95 % anstreben).
- **SLA**: Externe, vertragliche Verpflichtungen gegenüber Kunden, die oft aus SLOs abgeleitet werden und Vertragsstrafen bei Verstößen beinhalten (z. B. 99,9 % Verfügbarkeit mit Gutschriften bei Nichteinhaltung).

#### Im Kontext von LLMs (z. B. aus SLOs-Serve):
Beim Serving von Large Language Models sind SLOs oft phasespezifisch:
- **Time-to-First-Token (TTFT)**: Enges SLO für die Prefill-Phase (Eingabeverarbeitung) in interaktiven Apps wie Chatbots.
- **Tokens-Per-Output-Time (TPOT)**: SLO für die Decode-Phase bezüglich der Generierungsgeschwindigkeit, die je nach Workload variiert (z. B. 50 ms/Token für Coding vs. 100 ms für Zusammenfassungen).

SLOs helfen, Durchsatz und Latenz in Shared-Umgebungen auszugleichen und verhindern Verstöße während Lastspitzen.

Zum vertiefenden Lesen:  
[SRE Book: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/)  
[SLOs-Serve Paper](https://arxiv.org/abs/2504.08784)