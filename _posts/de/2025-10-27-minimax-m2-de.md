---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: MiniMax M2 Open-Source KI-Modell
translated: true
type: note
---

### Was ist MiniMax M2?

MiniMax M2 ist ein neu veröffentlichtes Open-Source-Großsprachmodell (LLM) von MiniMax AI, einem chinesischen KI-Unternehmen, das sich auf Foundation-Modelle für Text, Audio, Bild und Video konzentriert. Es wurde vor wenigen Stunden veröffentlicht (Stand: 27. Oktober 2025) und ist ein Mixture of Experts (MoE)-Modell, das für Coding und agentenbasierte Workflows optimiert ist – man denke an autonome KI-Agenten, die planen, Tools ausführen und komplexe Aufgaben wie Full-Stack-Entwicklung, Datenanalyse oder mehrstufige Recherchen bewältigen. Es ist kein Generalist wie GPT oder Claude, glänzt aber in End-to-End-Programmierung und Agentenanwendungen und integriert sich nahtlos mit Tools wie Claude Code, Cursor oder Browser-/Shell-Interpretern.

Wichtige Spezifikationen:
- **Parameter**: 230 Milliarden gesamt, aber nur 10 Milliarden aktiv (für Effizienz).
- **Kontextlänge**: Bis zu 128.000 Tokens.
- **Bereitstellung**: Verfügbar auf Hugging Face unter MIT-Lizenz; unterstützt Frameworks wie SGLang und vLLM für Self-Hosting.
- **Zugang**: Kostenlose API-Testphase bis zum 7. November 2025 über MiniMax Agent (agent.minimax.io). Die kostenpflichtige API kostet 0,30 $ pro Million Input-Tokens und 1,20 $ pro Million Output-Tokens – das sind etwa 8 % der Kosten von Claude 3.5 Sonnet.

Es wird von einem "interleaved thinking"-Ansatz angetrieben (Verwendung von `