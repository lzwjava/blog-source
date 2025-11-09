---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Tinker API vereinfacht das Feinabstimmen von Modellen
translated: true
type: note
---

Tinker ist eine neue flexible API von Thinking Machines AI für das Feinabstimmen von Sprachmodellen. Sie wurde entwickelt, um Forschern, Entwicklern und "Hackern" das Experimentieren mit Open-Weight-Modellen (sowohl großen wie Qwen-235B-A22B als auch kleineren) zu ermöglichen und ihnen gleichzeitig vollständige Kontrolle über Algorithmen und Daten zu geben. Der Service übernimmt die anspruchsvolle Arbeit des verteilten Trainings – wie Planung, Ressourcenzuteilung und Fehlerbehebung – auf ihren internen Clustern und verwendet Techniken wie LoRA, um dies effizient und kostengünstig zu gestalten.

Wichtige Highlights:
- **Einfache Bedienung**: Wechseln Sie Modelle mit nur einem String im Python-Code.
- **API-Primitive**: Low-Level-Tools wie `forward_backward` und `sample` für gängige Post-Training-Methoden.
- **Open-Source-Unterstützung**: Wird mit der Tinker Cookbook-Bibliothek auf GitHub geliefert, die moderne Implementierungen von Feinabstimmungstechniken enthält.
- **Zweck**: Vereinfacht die Forschung an modernsten Modellen und reduziert Infrastrukturaufwand, damit Sie sich auf Innovation konzentrieren können.

Der Service befindet sich derzeit in einer privaten Beta (kostenlos zum Start, mit nutzungsbasierter Preisgestaltung in Kürze), und Sie können sich auf der Warteliste unter [thinkingmachines.ai/tinker](https://thinkingmachines.ai/tinker) eintragen. Zu den frühen Nutzern gehören Teams von Princeton, Stanford, Berkeley und Redwood Research.

[Announcing Tinker](https://thinkingmachines.ai/blog/announcing-tinker/)