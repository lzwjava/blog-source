---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Optimierung von Multi-SLO-LLM-Bereitstellung
translated: true
type: note
---

### Übersicht
Das Papier "SLOs-Serve: Optimized Serving of Multi-SLO LLMs" stellt SLOs-Serve vor, ein System, das für das effiziente Bereitstellen großer Sprachmodelle (LLMs) in mehrstufigen Anwendungen entwickelt wurde, bei denen jede Stufe (z. B. Prefill zur Eingabeverarbeitung, Decode zur Tokengenerierung) und jede Anwendung (z. B. Chatbots, Code-Assistenten) spezifische Service Level Objectives (SLOs) hat. Diese SLOs stellen eine niedrige Latenz für benutzerorientierte Aspekte sicher, wie Time-to-First-Token (TTFT) für Prefill und Tokens-Per-Output-Time (TPOT) für Decode. Traditionelle Bereitstellungssysteme wie vLLM oder Sarathi-Serve priorisieren den Durchsatz, verletzen jedoch häufig diese feingranularen SLOs unter gemeinsamen Ressourcen, insbesondere bei Lastspitzen oder gemischten Workloads.

### Hauptherausforderungen und Beiträge
Die Autoren identifizieren Herausforderungen beim Bereitstellen mit mehreren SLOs:
- **Mehrstufige Anfragen**: Anwendungen wie Reasoning-LLMs (enge SLOs während der "Denk"-Phasen) oder Tool-Calling-Agenten (Schleifen mit engem Prefill/Decode) erfordern stufenspezifische Garantien.
- **Ressourcenkonkurrenz**: Gemeinsam genutzte GPUs führen zu SLO-Verletzungen in gemeinsam genutzten oder disaggregierten Setups.
- **Lastspitzen**: Plötzliche Spitzen überlasten Scheduler.

Die Beiträge von SLOs-Serve umfassen:
- Einen auf dynamischer Programmierung (DP) basierenden Scheduler, der Token-Zuteilungen (Prefill-Budget, Batch-Größen) optimiert, um SLOs einzuhalten und gleichzeitig den Durchsatz zu maximieren.
- Unterstützung für gechunkten Prefill, SLO-adaptives spekulatives Decodieren (Anpassen der Spekulationslängen pro SLO-Stufe) und weiche Zugangskontrolle (Garantie der SLOs für angenommene Anfragen, Zurückstellen anderer).
- Eine verteilte Architektur mit Multi-Replica-Routing und Resilienz gegenüber Lastspitzen, aufgebaut auf vLLM für Batching und Ray für Orchestrierung.

| Anwendung | Prefill SLO | Decode SLO | Beispiel |
|-------------|-------------|------------|---------|
| Zusammenfassung | Eng (z. B. max. 3x Verlangsamung) | Locker (100ms TPOT) | Dokumentenverarbeitung |
| Code-Generierung | Locker | Eng (50ms TPOT) | Code-Generierung |
| Chatbot | Locker | Locker | Interaktive Abfragen |
| Tool-Calling | Eng (Schleifen) | Eng (Schleifen), locker (final) | Agenten-Workflows |
| Reasoning | Eng (Denken) | Eng (Denken), locker (Antwort) | Chain-of-Thought |

### Systemdesign
- **Scheduler (Algorithmus 1)**: Verwendet DP, um Anfragen anzunehmen und Batches zu planen, modelliert die Ausführungszeit über einen Roofline-inspirierten Prädiktor (R² > 0,8 Genauigkeit). Zustände verfolgen Speicher, Prefill-Budget und angenommene Anfragen; Übergänge priorisieren frühe Fristen und SLO-Erfüllung.
- **Batch-Bildung**: Dynamische Größenanpassung (bis zu 512+ Tokens) basierend auf dem engsten TPOT, ermöglicht größere Batches für höheren Durchsatz ohne SLO-Verletzungen.
- **Spekulatives Decodieren**: Passt Spekulationslängen (z. B. 1-10 Tokens) pro SLO-Stufe an, um das Prefill-Budget zu erhöhen, löst dies mittels Enumeration für ein optimales Prefill/Decode-Gleichgewicht.
- **Multi-Replica & Lastspitzen**: Ein zentralisierter Controller leitet Anfragen proaktiv weiter; unerreichbare Anfragen gehen in eine Best-Effort-Warteschlange und werden bei Bedarf verdrängt.

Das Design untersucht Kompromisse, wie z. B. größere Batches, die den Durchsatz erhöhen, aber die Latenz gefährden (visualisiert in Diagrammen, die SLO-machbare Regionen zeigen).

### Evaluation
Getestet in 6 Szenarien (Chatbot, Coding, Zusammenfassung, gemischt, Tool-Calling, Reasoning) mit echten Traces (Azure LLM Workloads) und Datensätzen (ShareGPT, HumanEval, etc.). Modelle: OPT-7B/13B/30B, ToolLlama-7B. Hardware: 4×A100 GPUs (Haupttest), bis zu 8×H100.

- **Kapazitätsgewinne**: 2,2× durchschnittliche Verbesserung gegenüber vLLM/Sarathi-Serve/DistServe (geometrisches Mittel über Szenarien). Z. B. 2,4× beim Reasoning, 2,1× bei bursty Coding.
- **Skalierung**: Superlinear mit Replikaten (bis zu 6,2× beim Tool-Calling unter Lastspitzen) durch Routing.
- **Ablationen**: Spekulation fügt 1,66× hinzu, Routing 1,19×, Behandlung von Lastspitzen 1,34×.
- Overhead: <10ms pro Schedule-Aufruf.

Diagramme zeigen, dass SLOs-Serve p99-Latenzen nahe den Zielwerten während Spitzen hält, während Baseline-Systeme sich verschlechtern.

### Schlussfolgerungen
SLOs-Serve verbessert das Bereitstellen von LLMs, indem es Multi-SLOs in diversen, lastspitzenreichen Umgebungen garantiert und so Effizienzgewinne von 2x+ freisetzt. Zukünftige Arbeit könnte sich auf unbekannte Decode-Längen oder mehr Stufen erweitern. Das System demonstriert, dass SLO-angepasste Planung der Schlüssel für produktionsreife LLM-Bereitstellungen ist.

[SLOs-Serve: Optimized Serving of Multi-SLO LLMs](https://arxiv.org/abs/2504.08784)