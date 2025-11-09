---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Maximale Update-Parametrisierung für Neuronale Netze
translated: true
type: note
---

### Was ist μP (Maximal Update Parametrization)?

μP, kurz für Maximal Update Parametrization, ist eine Parametrisierungstechnik für neuronale Netze, die von Greg Yang, einem Mathematiker und KI-Forscher, der jetzt bei xAI (zuvor bei Microsoft Research) tätig ist, entwickelt wurde. Eingeführt in seinem 2022er Paper "Tensor Programs V: Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer", parametrisiert sie die Gewichte von Deep-Learning-Modellen neu, um sie skalierbarer und effizienter für das Training zu machen.

#### Zweck
Das Kernziel von μP ist es, die Hyperparameter-Optimierung (HP) über verschiedene Modellgrößen hinweg zu stabilisieren. In traditionellen Setups (wie Standard Parametrization, oder SP) müssen Hyperparameter wie Lernraten jedes Mal neu optimiert werden, wenn man ein Modell vergrößert – z.B. von Millionen zu Milliarden von Parametern –, weil Gradienten und Updates instabil werden (oft skaliert dies quadratisch mit der Modellbreite oder -tiefe). μP behebt dies, indem es die Parameter so transformiert, dass das "maximale Update" (der größtmögliche Gradientenschritt) unabhängig von der Skalierung konsistent bleibt. Dies ermöglicht **μTransfer**, einen Workflow, bei dem man HPs an einem winzigen "Proxy"-Modell optimiert und sie direkt auf ein massives Zielmodell anwendet, ohne weitere Anpassungen.

#### Hauptvorteile
- **Erhebliche Kosteneinsparungen**: Die Optimierung an kleinen Modellen ist günstig. Beispielsweise übertraf die Übertragung von HPs von einem 13M-Parameter-Proxy die veröffentlichten Ergebnisse für BERT-large (350M Parameter), wobei die Gesamtkosten für die Optimierung denen nur eines einzigen Vor-Trainingslaufs von BERT-large entsprachen. Für GPT-3 (6,7 Mrd. Parameter) übertraf ein 40M-Proxy-Transfer die Baseline-Ergebnisse bei nur 7 % der vollen Vor-Trainingskosten.
- **Skalierbarkeit für große Modelle**: Funktioniert gut mit Architekturen wie Transformers und ResNets und ist damit ideal für das Training enormer neuronaler Netze (z.B. solche, die bei xAI verwendet werden). Es gewährleistet "skaleninvariante Optima", was bedeutet, dass die Loss-Landschaft bei wachsenden Modellen nicht unvorhersehbar verzerrt wird.
- **Einfache Anwendung**: Verfügbar als PyTorch-Bibliothek (`pip install mup`) und wurde bereits in Produktions-Trainingspipelines für große KI-Modelle integriert.

#### Kurze mathematische Intuition
In SP wächst die Varianz der Gewichte instabil, was zu explodierenden/verschwindenden Gradienten führt. μP parametrisiert Gewichte neu (z.B. für eine lineare Schicht durch Skalierung mit Fan-In), um die Fisher-Informationsmatrix zu normalisieren und sicherzustellen, dass der Gradientenfluss ausgeglichen bleibt. Dies hält optimale HPs (wie Lernraten) über verschiedene Skalierungen hinweg annähernd konstant und vermeidet so die Notwendigkeit einer größenabhängigen Nachoptimierung.

μP baut auf Yangs breiterem "Tensor Programs"-Framework zum Verständnis von Grenzwerten unendlicher Breite/Tiefe in neuronalen Netzen auf und entwickelt sich weiter – neuere Arbeiten (Stand 2025) betonen seine Rolle beim maximalen Feature-Learning, das über reine HP-Übertragung hinausgeht.

**Referenzen**  
- [Tensor Programs V: Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer](https://arxiv.org/abs/2203.03466)  
- [The Practitioner's Guide to the Maximal Update Parameterization](https://www.cerebras.ai/blog/the-practitioners-guide-to-the-maximal-update-parameterization)  
- [How To Scale (Blog on μP and Scaling)](https://howtoscalenn.github.io/)  
- [Greg Yang's Professional Page](https://thegregyang.com/)