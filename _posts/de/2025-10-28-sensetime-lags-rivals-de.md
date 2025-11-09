---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: SenseTime KI-Modelle hinken Konkurrenz hinterher
translated: true
type: note
---

### Verständnis von SenseTimes DayDayNew- und Riri-Xin-Modellen

SenseTime, einer der „KI-Drachen“ Chinas, ist seit 2014 ein führendes Unternehmen in den Bereichen Computer Vision und Gesichtserkennung. Im Zeitalter der generativen KI haben sie sich unter dem Dach von SenseNova auf Large Language Models (LLMs) verlegt. „DayDayNew“ (im Chinesischen oft als „日日新“ stilisiert) bezieht sich auf ihre interaktive KI-Plattform und Modellreihe, wobei die neueste Version DayDayNew 6.5 Ende Oktober 2025 auf der World Artificial Intelligence Conference (WAIC) vorgestellt wurde. Es ist für multimodale Aufgaben wie die Verarbeitung von Text, Bildern und Videos konzipiert, mit starkem Fokus auf Unternehmensanwendungen, API-Integrationen und Hardware-Anbindungen (z.B. Xiaomi AI-Brillen). „Riri Xin“ (日日新 integrated model) ist ein verwandtes, leichtgewichtiges multimodales LLM, das bereits früher im Jahr 2025 eingeführt wurde und sich auf tiefgehendes Reasoning, cross-modale Generierung und Effizienz für Consumer-Geräte konzentriert.

Diese Modelle zielen darauf ab, in Chinas hyperwettbewerbsintensiver KI-Landschaft zu konkurrieren, hinken jedoch in Rohleistungs-Benchmarks tatsächlich den Spitzenreitern wie DeepSeek (DeepSeek-V3), Kimi (Moonshot AIs Kimi-Serie) und MiniMax (ABAB-Serie) hinterher. Zum Vergleich: In den SuperCLUE-Benchmarks Mitte 2025 (eine wichtige chinesische LLM-Evaluierung für Reasoning, Mathematik und allgemeine Fähigkeiten) belegte DeepSeek-V3 die Spitzenposition bei den Gesamtpunkten (~85/100), Kimi K2 erreichte ~82 und MiniMax ABAB ~80, während SenseNova-Varianten (einschließlich Riri-Xin-Integrationen) bei etwa 70-75 lagen und oft gegen MiniMax in Reasoning- und Coding-Aufgaben verloren. Ähnliche Lücken zeigen sich in globalen Evaluationen wie MMLU oder HumanEval, bei denen SenseTime Multimodalität über reines Text-Reasoning priorisiert.

### Warum das Hinterherhinken hinter DeepSeek, Kimi und MiniMax?

Mehrere Faktoren, die in SenseTimes Vergangenheit, den Marktdynamiken und externen Druck wurzeln, erklären dies:

1.  **Später Wechsel von Computer Vision zu LLMs**: SenseTime baute sein Imperium auf Wahrnehmungs-KI (z.B. Überwachungstechnologie) auf und stieg erst 2023 mit SenseNova vollständig in generative LLMs ein. Dies verzögerte ihre Skalierung im Vergleich zu LLM-nativen Startups. DeepSeek (gegründet 2023) und Moonshot AI (Kimi, 2023) starteten mit einem scharfen Fokus auf effiziente, Open-Weight-Modelle und iterierten schnell an Architekturen wie Sparse Attention für kosteneffizientes Training. MiniMax, obwohl jünger (2021), optimierte von Anfang an für Consumer-Apps wie Video-Generierung (Hailuo).

2.  **US-Entity-List-Sanktionen**: Seit 2019 auf der US-Blacklist wegen mutmaßlicher Menschenrechtsverletzungen, hat SenseTime eingeschränkten Zugang zu modernen Chips (z.B. NVIDIA-GPUs) und US-Technologie. Dies behindert das Training im Maßstab der Konkurrenten – DeepSeek nutzt einheimische Huawei-Ascend-Chips innovativ, während Kimi und MiniMax Hybrid-Setups ohne die gleichen Exportbeschränkungen nutzen. Ergebnis: Langsamere Modell-Updates und höhere Kosten, was die Leistungslücke vergrößert.

3.  **Bewegliche Startups vs. etablierter Gigant**: SenseTime ist ein börsennotiertes Unternehmen (HKEX) mit einem Umsatz von ~1 Mrd. USD+, das Enterprise-Kunden (z.B. Banken, Regierungen) bedient. Dies bringt Bürokratie und einen Fokus auf konforme, multimodale Lösungen statt auf Benchmark-Spitzenleistungen mit sich. Im Gegensatz dazu:
    - DeepSeek betont „schnelle, günstige, offene“ Modelle und führt Open-Source-Ranglisten mit niedrigen Inferenzkosten an.
    - Kimi glänzt im Long-Context-Reasoning (bis zu 200K Tokens) und rivalisiert mit OpenAIs o1.
    - MiniMax überzeugt in Multimodalität (Text-zu-Video) und Effizienz und schlägt SenseTime oft im direkten Vergleich.

    Ironischerweise sind die Gründer von MiniMax (Yan Junjie und Zhou Yucong) ehemalige SenseTime-Ingenieure, die dort Deep-Learning-Toolchains leiteten. Sie verließen das Unternehmen, um ein wendigeres Startup aufzubauen, und nutzen dieses Fachwissen, um ihren alten Arbeitgeber zu überflügeln – was zeigt, wie Talentmobilität das chinesische KI-Wettrüsten antreibt.

4.  **Benchmark- und Hype-Dynamiken**: Chinesische Evaluationen wie SuperCLUE belohnen Reasoning/Mathematik, wo Startups überproportional investieren. SenseTimes Stärke liegt in der Integration (z.B. SenseCore-Cloud für Fine-Tuning), aber sie schneiden in „Frontier“-Tests schlechter ab. Weniger Hype bedeutet weniger Nutzer/Daten für Iterationen, was eine Feedback-Schleife erzeugt. Stand Oktober 2025 hält SenseTime ~14 % Marktanteil im AIGC-Bereich (Top 3), aber das bezieht sich auf Umsatz, nicht auf Fähigkeiten.

### Aktuelle Nachrichten und was SenseTime getan hat

Die Nachrichten über SenseTime waren ruhiger als der Start-up-Trubel (z.B. DeepSeeks virale R1-Veröffentlichung), aber sie sind im Enterprise-/Gen-AI-Wachstum aktiv:

-   **April 2025**: Einführung von SenseNova V6 Omni, Chinas „fortschrittlichstem“ multimodalen Modell laut eigenen Angaben, mit Upgrades für die SenseCore 2.0-Infrastruktur für ein besseres Modellverständnis.
-   **Juni 2025**: Schloss sich ByteDance/Alibaba bei Modellupdates im KI-Wettlauf an und betonte kosteneffiziente APIs.
-   **August 2025**: DayDayNew-Plattform in Xiaomi AI-Brillen integriert; Umsatz stieg um 21 % im Vorjahresvergleich aufgrund der Gen-AI-Nachfrage (Trainings-/Inferenzdienste).
-   **September 2025**: Ausgliederung nicht-kerniger Geschäftsbereiche, um den Fokus auf Gen-AI zu straffen und die Profitabilität voranzutreiben.
-   **Oktober 2025**: DayDayNew 6.5 und Mynie-Plattform auf der WAIC, Verbesserung der multimodalen Interaktion (z.B. Video-Verständnis um 30 % gesteigert).

Sie setzen vermehrt auf B2B (z.B. Cloud-Dienste, Geräte-Einbettungen) statt auf Consumer-Chatbots, was den „Keine-Nachrichten“-Eindruck erklärt – weniger virale Demos, mehr stille Enterprise-Erfolge. Dennoch könnten sie mit Gesprächen über eine Lockerung der Sanktionen und Fortschritten bei einheimischen Chips die Lücke bis 2026 schließen.

Kurz gesagt: SenseTimes Erbe bremst es in einem Start-up-Sprint, aber ihre multimodale Wette positioniert sie für praktische Erfolge gegenüber der reinen Jagd nach Benchmark-Punkten.

[ChinAI #324: SuperCLUE Benchmarks —2025 Midyear Check-in](https://chinai.substack.com/p/chinai-324-superclue-large-model)  
[SenseTime's SenseNova Foundation Models Among Top Three](https://www.sensetime.com/en/news-detail/51169429?categoryId=1072)  
[An Overview of Chinese AI Tigers](https://www.topbots.com/chinese-ai-tigers-overview/)  
[China's SenseTime Reshapes to Focus on Generative AI Growth](https://www.reuters.com/technology/artificial-intelligence/chinas-sensetime-reshapes-focus-generative-ai-growth-2024-12-04/)  
[SenseTime Unveils DayDayNew 6.5 AI Model](https://forntend-test-5sqwmq-3a22a9-107-172-80-230.traefik.me/sensetime-unveils-daydaynew-6-5-ai-model-and-mynie-platform-1753705726167)