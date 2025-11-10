---
audio: false
generated: true
image: false
lang: de
layout: post
title: 'Myonen: Strukturbewusster Matrixoptimierer'
translated: true
type: note
---

„Muon“ in Kimi bezieht sich auf einen fortschrittlichen Optimierer – genauer gesagt einen **strukturbewussten, matrixorthogonalisierenden Optimierer**, der beim Training des Kimi K2-Sprachmodells verwendet wird.

---

### Was ist der Muon-Optimierer?

1.  **Matrixbewusste Optimierung**
    Im Gegensatz zu AdamW oder SGD behandelt Muon Gewichtsmatrizen als geometrische Einheiten und nicht als unabhängige Skalarparameter. Er wendet **Newton-Schulz-Iterationen** an, um den momentumgemittelten Gradienten zu orthogonalisieren, was zu gut konditionierten, ausgewogenen Updates führt, die sowohl die Zeilen- als auch die Spaltenstruktur der Matrix berücksichtigen ([Medium][1], [kellerjordan.github.io][2]).

2.  **Orthogonalisierung via Newton-Schulz**
    Anstatt eine teure Singulärwertzerlegung (SVD) durchzuführen, verwendet Muon ein schnelles iteratives Verfahren (Newton-Schulz), um die nächstgelegene orthogonale Matrix zum Gradienten anzunähern. Dies hält das Update unter **spektralen Normbeschränkungen**, erhält die Energie und verteilt das Lernen gleichmäßig auf alle Richtungen ([Medium][1], [kellerjordan.github.io][2]).

3.  **Pipeline-Anpassung**
    Der standardmäßige Ablauf – **Gradient → Momentum → Parameter-Update** – wird ersetzt durch:
    **Gradient → Momentum → Newton-Schulz-Orthogonalisierung → Parameter-Update**.
    Diese Modifikation verbessert die Trainings Effizienz und Stabilität für 2D-Parametermatrizen ([Medium][3], [kellerjordan.github.io][2]).

4.  **In der Praxis effizient**
    Trotz eines kleinen zusätzlichen Rechenaufwands liefert Muon erhebliche Beschleunigungen:

    *   Rekorde im NanoGPT-Speedrunning, Verbesserung der Trainingszeit um \~35% ([kellerjordan.github.io][2]).
    *   Skaliert gut beim Training großer Sprachmodelle in Kombination mit Weight Decay und per-Parameter-RMS-Anpassungen ([arXiv][4]).

5.  **Starke theoretische Grundlagen**
    Aktuelle Forschung unterstützt die Konvergenzeigenschaften von Muon, die Vorteile von Weight Decay und die optimale Batch-Größe. Studien bestätigen strengere theoretische Schranken und Effizienz in praktischen Szenarien ([arXiv][5]).

---

### Die Rolle von Muon in **Kimi K2**

Kimi K2 ist Moonshot AIs **Mixture-of-Experts (MoE)-Modell** mit **1 Billion Gesamtparametern** (32B aktiviert), das für agentische Fähigkeiten optimiert ist. Es erzielte eine außergewöhnliche Leistung in Benchmarks für Wissen, logisches Denken und Programmieren, teilweise dank des Trainings mit Muon (und einer Variante namens **MuonClip**) ([Hugging Face][6], [Poe][7]).

*   Der **MuonClip-Optimierer** bezieht sich auf den Einsatz von Muon in massivem Maßstab, während Stabilitätsherausforderungen angegangen werden, die solch großen Modellen innewohnen ([Hugging Face][6], [Poe][7]).
*   Der Optimierer war entscheidend dafür, **null Trainingsinstabilität** über einen großen Token-Datensatz (\~15,5 Billionen Tokens) zu ermöglichen und state-of-the-art Ergebnisse zu liefern ([Hugging Face][6]).

---

### Zusammenfassend (Ohne Tabelle, wie gewünscht)

*   **Muon** = „MomentUm Orthogonalized by Newton–Schulz“ – ein Optimierer, der rohe Gradienten-Updates durch orthogonalisierte Updates ersetzt und so die Lern Dynamik für Matrixparameter verbessert.
*   Er erhält die Struktur, gewährleistet ausgewogene Updates und bleibt durch iterative Orthogonalisierung anstelle teurer Zerlegungen effizient.
*   **Kimi K2** nutzt Muon (und MuonClip), um die Grenzen des groß angelegten MoE-Trainings zu erweitern und erreicht dabei Spitzenleistung mit Stabilität und Recheneffizienz.

---

Lass mich wissen, wenn du einen tieferen Einblick möchtest – vielleicht, wie sich Muon im Vergleich zu AdamW in Trainingsverläufen verhält, wie MuonClip den Algorithmus für MoEs anpasst oder wie die Newton-Schulz-Methode im Code funktioniert!

[1]: https://medium.com/%40gauritr01/the-truth-about-kimi-k2-pretraining-muon-optimizer-moe-unpacked-43554527d94a?utm_source=chatgpt.com "The Truth About KIMI K2 Pretraining: Muon Optimizer ..."
[2]: https://kellerjordan.github.io/posts/muon/?utm_source=chatgpt.com "Muon: An optimizer for hidden layers in neural networks"
[3]: https://medium.com/%40jenwei0312/going-beyond-adamw-a-practical-guide-to-the-muon-optimizer-93d90e91dbd3?utm_source=chatgpt.com "Going Beyond AdamW: A Practical Guide to the Muon ..."
[4]: https://arxiv.org/html/2502.16982v1?utm_source=chatgpt.com "Muon is Scalable for LLM Training"
[5]: https://arxiv.org/abs/2507.01598?utm_source=chatgpt.com "Convergence Bound and Critical Batch Size of Muon Optimizer"
[6]: https://huggingface.co/moonshotai/Kimi-K2-Base?utm_source=chatgpt.com "moonshotai/Kimi-K2-Base"
[7]: https://poe.com/Kimi-K2?utm_source=chatgpt.com "Kimi-K2"