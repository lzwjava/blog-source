---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: SLOs-Serve im Vergleich zu vLLM-Funktionen
translated: true
type: note
---

### Vergleich: SLOs-Serve vs. vLLM

SLOs-Serve erweitert vLLM, indem es es als Kern-Batching-Engine integriert und gleichzeitig Ebenen für Multi-SLO (Service Level Objective) Garantien hinzufügt, was es besser für Produktionsumgebungen mit diversen, latenzsensiblen Workloads geeignet macht. vLLM konzentriert sich primär auf Hochdurchsatz-Inferenz für Single-SLO- oder Durchsatz-maximierende Szenarien und verwendet Techniken wie PagedAttention für Speichereffizienz. Nachfolgend finden Sie einen strukturierten Vergleich basierend auf Schlüsselaspekten aus dem SLOs-Serve-Paper und dem Design von vLLM.

| Aspekt                  | SLOs-Serve                                                                 | vLLM                                                                 |
|-------------------------|----------------------------------------------------------------------------|----------------------------------------------------------------------|
| **Primärer Fokus**      | Multi-SLO-Serving für mehrstufige LLM-Apps (z.B. strikte TTFT für Prefill beim Reasoning, strikte TPOT für Decode beim Coding). Verarbeitet burstartige, gemischte Workloads mit stagespezifischen Garantien. | Hochdurchsatz-Batching für kontinuierliches Decoding, optimiert für speicherbegrenzte Workloads via PagedAttention. Geht von einheitlichen SLOs aus oder priorisiert aggregierten Durchsatz. |
| **SLO-Behandlung**       | Explizite Multi-SLO-Unterstützung: Pro-Stage (Prefill/Decode) und pro-App SLOs (z.B. 50ms TPOT für Coding vs. 100ms für Chat). Nutzt Soft Admission Control, um verletzende Anfragen abzulehnen/zu verschieben. | Keine native Multi-SLO-Unterstützung; verlässt sich auf statische Konfigurationen (z.B. maximale Batch-Größe). SLO-Verletzungen sind bei Ressourcenkonflikten häufig (z.B. >2x Latenzspitzen bei Bursts). |
| **Scheduler**          | Dynamische Programmierung (DP)-basiert: Optimiert Prefill-Budgets, Batch-Größen und Speculation-Längen pro SLO-Tier. Sagt Ausführungszeit mit Roofline-Modell vorher (R² > 0,8 Genauigkeit). | Continuous Batching Scheduler: Packt Anfragen gierig in dynamische Batches, Fokus auf decode-lastige Workloads. Keine SLO-bewusste Planung. |
| **Prefill-Optimierung**| Gegliedertes Prefill mit adaptiver Speculation (1-10 Tokens pro SLO). Weist "Prefill-Budget" zu, um es mit dem Decode auszugleichen. | Single-Shot-Prefill pro Anfrage; unterstützt gegliedertes Prefill, aber ohne SLO-Adaption. Anfällig für Head-of-Line-Blocking in gemischten Lasten. |
| **Decode-Optimierung**| SLO-adaptive Batch-Größen (bis zu 512+ Tokens) und spekulatives Decoding, angepasst an TPOT-Ziele. | Effizientes kontinuierliches Decoding mit Look-Ahead-Batching; hoher Durchsatz (z.B. 10-20x über Hugging Face), ignoriert aber pro-Anfrage-Fristen. |
| **Ressourcenmanagement**| Multi-Replica-Routing via Ray; Burst-Resilienz mit Best-Effort-Queues und Preemption. Verarbeitet disaggregierte Setups. | Single-Node oder einfache verteilte Systeme (via Ray-Integration); kein proaktives Routing oder SLO-priorisierte Zuteilung. |
| **Durchsatz & Kapazität**| 2,2× durchschnittlicher Kapazitätsgewinn gegenüber vLLM (geometrisches Mittel über 6 Szenarien: Chatbot, Coding, etc.). Z.B. 2,4× in Reasoning-Bursts. Superlineare Skalierung mit Replikaten. | Baseline für Durchsatz: Bis zu 24x schneller als Alternativen in decode-lastigen Traces, verschlechtert sich aber unter SLO-Beschränkungen (z.B. 50% Kapazitätsverlust in gemischten Workloads). |
| **Overhead**           | <10ms pro Schedule; minimal aufgrund von DP-Effizienz (O(n) Zustände).             | Gering (<1ms Batching); aber es fehlt SLO-Logik, daher kein zusätzlicher Overhead.      |
| **Anwendungsfälle**          | Produktions-Apps mit strikten SLAs: Tool-calling Agents, Reasoning Chains, burstartiger Traffic (z.B. Azure Traces). | Forschungs-/Entwicklungsdurchsatz: Einfaches Serving, Long-Context-Generierung, einheitliche Lasten. |
| **Einschränkungen**        | Setzt bekannte SLOs/Deadlines voraus; zukünftige Erweiterungen für unbekannte Längen nötig. Baut auf vLLM auf, erbt also dessen Decode-Stärken. | Schwierigkeiten mit mehrstufigen/variablen SLOs; hohe Tail-Latenzen in shared GPU-Setups (p99 >2x Ziel in Evaluationen). |
| **Implementierung**     | Open-Source-Prototyp auf vLLM + Ray; unterstützt OPT/ToolLlama-Modelle auf A100/H100 GPUs. | Ausgereifte Open-Source (GitHub); weit verbreitet, unterstützt 100+ Modelle, einfache Bereitstellung. |

Zusammenfassend lässt sich sagen, dass vLLM in roher Effizienz für durchsatzorientiertes Serving glänzt, aber bei der SLO-Compliance in komplexen, realen Szenarien Schwächen zeigt – was zu den 2x+ Gewinnen in SLOs-Serve durch gezielte Optimierungen führt. Wenn Ihre Workload rein durchsatzmaximierend ohne Latenzgarantien ist, bleibt vLLM einfacher und schneller zu deployen.

[SLOs-Serve: Optimized Serving of Multi-SLO LLMs](https://arxiv.org/abs/2504.08784)  
[vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention](https://arxiv.org/abs/2309.06180)