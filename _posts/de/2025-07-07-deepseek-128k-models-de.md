---
audio: false
generated: true
lang: de
layout: post
title: DeepSeek 128K-Token-Modelle im Jahr 2025
translated: true
type: note
---

Stand Juni 2025 verfügt DeepSeek über eine Reihe von Modellen mit beeindruckenden Kontextlängen, die oft ihre Mixture-of-Experts (MoE)-Architektur für Effizienz nutzen. Hier eine Übersicht:

*   **DeepSeek-R1:** Dieses Modell, veröffentlicht im Januar 2025, zeichnet sich durch eine Kontextlänge von **128.000 Tokens** (oder 131.072 Tokens in einigen Benchmarks) aus. Es ist besonders stark in Mathematik, Coding und strukturiertem Denken aufgrund seines Reinforcement Learning (RL) Post-Trainings.
*   **DeepSeek-V3:** Veröffentlicht im Dezember 2024, unterstützt DeepSeek-V3, einschließlich seines Basismodells, ebenfalls eine Kontextlänge von **128.000 Tokens**. Es ist ein leistungsstarkes MoE-Modell mit 671 Milliarden Gesamtparametern (37 Milliarden aktive pro Abfrage).
*   **DeepSeek-Coder-V2:** Dieses code-fokussierte MoE-Modell, veröffentlicht im Juli 2024, hat ein signifikantes Kontextfenster von **128.000 Tokens**. Es unterstützt eine breite Palette von Programmiersprachen (338).
*   **DeepSeek-V2:** Veröffentlicht im Mai 2024, weist DeepSeek-V2 eine Kontextlänge von **128.000 Tokens** auf. Dieses MoE-Modell zielt auf wirtschaftliches Training und effiziente Inferenz ab.
*   **DeepSeek-V2.5:** Veröffentlicht im September 2024, kombiniert dieses Modell allgemeine und Coding-Fähigkeiten und unterstützt ebenfalls ein **128.000 Token** Kontextfenster.

**Wichtige Überlegungen:**

*   **Native Kontextlänge vs. API-Limits:** Während einige DeepSeek-Modelle eine native Kontextlänge von bis zu 163.840 Tokens haben, kann die DeepSeek-API das verfügbare Kontextfenster für bestimmte Modelle begrenzen (z. B. haben "deepseek-chat" und "deepseek-reasoner" derzeit ein 64K-Kontextlimit über ihre API). Wenn Sie den vollen Kontext benötigen, könnte es erforderlich sein, die Modelle lokal auszuführen oder API-Anbieter zu nutzen, die längere Kontexte erlauben.
*   **Leistungsabfall:** Ähnlich wie bei anderen Large Language Models kann die Leistung (Genauigkeit, Logik) manchmal abnehmen, wenn die Modelle an ihre absolute maximale Länge gebracht werden. DeepSeek R2 wird voraussichtlich den in R1 beobachteten Leistungsabfall von 15 % bei dessen maximaler Kontextlänge von 128.000 Tokens adressieren.

Zusammenfassend ist DeepSeek ein starker Akteur im Bereich der LLMs mit langem Kontext, wobei mehrere Modelle im Juni 2025 ein 128K-Token-Kontextfenster bieten, was sie für die Verarbeitung umfangreicher Eingaben und komplexer Aufgaben geeignet macht.