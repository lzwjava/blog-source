---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4.1-fast
title: Fragen für Vorstellungsgespräche als Embodied AI Engineer
translated: true
type: note
---

Hier ist ein umfassender Fragenkatalog für Interviews, zugeschnitten auf die Rolle eines **Embodied AI Engineers**, mit starkem Fokus auf modernes visuomotorisches Policy-Lernen, insbesondere **Diffusion Policy**, **RT-2**, **ACT (Action Chunking Transformer)** und allgemeine Embodied-Intelligence-Technologien.

### Grundlagen zu Embodied AI & Robotik
1.  Was sind die Hauptunterschiede zwischen Embodied AI und traditionellen "körperlosen" großen Sprach-/Visionsmodellen?
2.  Warum ist Sim-to-Real-Transfer in Embodied AI deutlich schwieriger als bei Computer-Vision- oder NLP-Aufgaben?
3.  Vergleichen Sie die Datenanforderungen und Skalierungsgesetze, die Sie in Embodied AI im Vergleich zu LLMs oder Vision-Foundation-Modellen beobachtet haben.
4.  Wie denken Sie über Sicherheit und Robustheit beim Einsatz von Robotern in der realen Welt (z.B. Fehlermodi, Erholungsverhalten)?

### Diffusion Policy (UC Berkeley, Chi et al., 2023–2025)
5.  Erklären Sie die Kernidee von Diffusion Policy und warum Diffusionsmodelle besonders gut für die visuomotorische Steuerung geeignet sind.
6.  Beschreiben Sie den Vorwärts-/Rückwärtsprozess, wenn ein Diffusionsmodell als Policy verwendet wird. Wie wird die Aktionsentrauschung auf visuelle Beobachtungen konditioniert?
7.  Was sind die Hauptvorteile von Diffusion Policy gegenüber früheren Imitationslern-Baselines (z.B. Behavioral Cloning mit MSE, GCBC, Transformer BC)?
8.  Diffusion Policy verwendet oft ein U-Net-Backbone mit FiLM-Konditionierung oder Cross-Attention. Vergleichen Sie diese beiden visuellen Konditionierungsmethoden in Bezug auf Leistung und Inferenzgeschwindigkeit.
9.  Wie funktioniert Classifier-Free Guidance in Diffusion Policy und wie beeinflusst es Exploration vs. Exploitation zur Testzeit?
10. In den Versionen 2024–2025 wurde Diffusion Policy mit Szenengraphen- oder Sprachkonditionierung kombiniert. Wie würden Sie hochsprachliche Ziele zu einer Diffusionspolicy hinzufügen?
11. Welche häufigen Fehlermodi haben Sie bei Diffusion Policy im realen Roboter-Einsatz gesehen und wie wurden sie behoben?

### RT-2 (Google DeepMind, 2023–2024)
12. Was ist RT-2 und wie trainiert es ein Vision-Language-Model (PaLI-X / PaLM-E) gemeinsam zu Roboteraktionen fein?
13. Erklären Sie das Tokenisierungsschema, das in RT-2 für kontinuierliche Aktionen verwendet wird. Warum werden Aktionen in Bins diskretisiert?
14. RT-2 beansprucht emergente Fähigkeiten (z.B. Chain-of-Thought-Reasoning, Arithmetik, Symbolverständnis), die auf die Robotik übertragen wurden. Haben Sie diese in der Praxis reproduziert oder beobachtet?
15. Vergleichen Sie RT-2 mit OpenVLA und Octo. In welchen Szenarien würden Sie RT-2 den anderen vorziehen?
16. Wie behandelt RT-2 Langzeithorizont-Aufgaben und Multi-Task-Generalisierung im Vergleich zu Diffusion Policy oder ACT?

### ACT (Action Chunking Transformer, Tony Zhao et al., 2023)
17. Welches Problem löst Action Chunking in Transformer-basierten Policies und warum ist Chunking kritisch für Echtzeitsteuerung bei 10–50 Hz?
18. Beschreiben Sie die ACT-Architektur: Wie werden Aktionen gechunkt, wie wird das latente Ziel berechnet und wie wird die Varianz modelliert?
19. Vergleichen Sie ACT mit Diffusion Policy in Bezug auf Sample-Effizienz, Inferenzgeschwindigkeit und Erfolgsrate bei kontaktintensiven Aufgaben.
20. ACT verwendete ursprünglich CVAE für die latente Modellierung, spätere Versionen verwenden Flow-Matching oder Diffusion. Welche Vorteile brachten die neueren Versionen?

### Breitere Visuomotorische Policy-Landschaft
21. Vergleichen Sie die vier großen Visuomotor-Policy-Familien in 2024–2025:
    - Transformer-Sequenzmodelle (ACT, Octo)
    - Diffusion-Policy-Familie
    - VLA-artige Modelle (RT-2, OpenVLA, Octo-Transformer)
    - Flow-Matching-Policies (z.B. MIMo, Aurora)
22. Wann würden Sie Flow-Matching gegenüber Diffusion für einen Echtzeit-Roboter (z.B. Humanoid oder Mobile Manipulator) wählen?
23. Wie kombinieren neuere Modelle wie Octo (UC Berkeley, 2024) und OpenVLA (Stanford/PMI, 2024) die Stärken von ACT und RT-2?
24. Welche Rolle sehen Sie Foundation-Models (z.B. das Einbetten von Aktionen in den gleichen Raum wie Sprach-/Bild-Tokens) in den nächsten 2–3 Jahren der Embodied AI?

### Systemdesign & Technische Fragen
25. Entwerfen Sie eine vollständige Trainingspipeline zur Erfassung eines 100k+ Episoden umfassenden Realwelt-Datensatzes für einen bimanuellen mobilen Manipulator mit Diffusion Policy oder ACT.
26. Wie würden Sie eine visuomotorische Policy so gestalten, dass sie in Echtzeit (≥30 Hz) auf einer Edge-GPU (z.B. Jetson Orin) läuft und dabei eine hohe Erfolgsrate beibehält?
27. Sie haben eine Policy, die in der Simulation perfekt funktioniert, aber auf dem echten Roboter komplett versagt. Systematische Debugging-Checkliste?
28. Wie würden Sie Kraft-/Taktilsensorik als zusätzliche Modalitäten zu einer bestehenden, nur auf Vision basierenden, Diffusion-Policy- oder RT-2-Architektur hinzufügen?
29. Erklären Sie, wie Sie mit einer dieser Methoden eine schnelle Anpassung (Few-Shot oder Zero-Shot) an eine neue Objektinstanz oder einen neuen Hintergrund vornehmen würden.

### Forschung & Zukünftige Richtungen
30. Wo, Ihrer Meinung nach, wird sich das Feld der Embodied AI im Jahr 2027 befinden – werden wir generalistische Haushaltsroboter haben? Was ist der größte Blockierer heute?
31. Glauben Sie, dass das aktuelle Paradigma Imitationslernen + Internet-Skalenvortraining (OpenVLA, Octo, etc.) ausreicht, oder brauchen wir für echte Generalisierung immer noch Reinforcement Learning oder aktive Datensammlung?

Diese Fragen reichen von Grundlagenwissen über Details aus der Spitzenforschung bis hin zu praktischen technischen Herausforderungen – perfekt für Interviews mit mittleren bis erfahrenen Embodied AI Engineers oder Forschern im Jahr 2025. Viel Erfolg bei Ihren Interviews!