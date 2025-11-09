---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: 'vLLM: Effiziente LLM-Bedienungsengine'
translated: true
type: note
---

### Erfindung von vLLM

vLLM (kurz für "virtual LLM") ist eine Open-Source-Bibliothek für hochdurchsatzfähiges und speichereffizientes Inferencing und Serving von Large Language Models (LLMs). Es wurde Anfang 2023 von Forschern des Sky Computing Lab im RISELab der UC Berkeley entwickelt. Das Projekt begann als eine spezialisierte Inferenz-Engine, die für NVIDIA A100 GPUs und eine begrenzte Anzahl von Modellen optimiert war und Schlüsselherausforderungen beim LLM-Serving wie Speicherfragmentierung und niedrigen Durchsatz adressierte.

Wichtige frühe Meilensteine:
- **Mitte April 2023**: Erste öffentliche Integration mit FastChat, die die Vicuna- und Chatbot-Arena-Demos von LMSYS antrieb.
- **Juni 2023**: Offizielle Veröffentlichung und Start des öffentlichen GitHub-Repositorys.
- **12. September 2023**: Das grundlegende Forschungspapier "Efficient Memory Management for Large Language Model Serving with PagedAttention" wurde auf arXiv veröffentlicht und führte den Kernmechanismus PagedAttention ein, der Continuous Batching und nahezu null KV-Cache-Verschwendung ermöglicht.

Das GitHub-Repository (vllm-project/vllm) wurde etwa im Mai–Juni 2023 erstellt, was mit dem anfänglichen Entwicklungsschub zusammenfiel.

### Aufstieg der Popularität

vLLM begann 2024 erheblich an Beliebtheit zu gewinnen und entwickelte sich von einem Nischen-Forschungswerkzeug zum De-facto-Standard für Open-Source-LLM-Serving. Seine Popularität explodierte aufgrund schneller Funktionserweiterungen (z. B. Quantisierung, spekulative Decodierung, multimodale Unterstützung), Hardware-Erweiterungen (NVIDIA, AMD, Google TPUs, etc.) und Produktionseinführungen bei Unternehmen wie Amazon (betreibt Rufus während des Prime Day 2024) und LinkedIn.

Wichtige Wachstumsindikatoren aus dem Jahr 2024:
- **GitHub Stars**: Stieg um das 2,3-fache von 14.000 (Anfang 2024) auf 32.600 (Ende 2024).
- **Monatliche Downloads**: Schnellte um das 4,5-fache von 6.000 auf 27.000 empor.
- **GPU-Nutzung**: Stieg in der zweiten Hälfte des Jahres 2024 um das ~10-fache.
- **Community**: Die Anzahl der Mitwirkenden stieg um das 3,9-fache auf 740, mit zweiwöchentlichen "Office Hours" und Partnerschaften (z. B. mit NVIDIA, IBM, AWS).

Mitte 2024 hatte es ~20.000 Sterne und wurde in AI-Communities häufig dafür diskutiert, Alternativen im Durchsatz zu übertreffen. Der Schwung setzte sich bis 2025 fort:
- Im Dezember 2024 trat es dem PyTorch-Ökosystem bei.
- Im Oktober 2024 wurde es in die LF AI & Data Incubation aufgenommen.
- Bis Juni 2025 erreichte es 50.000 Sterne.

Heute (Oktober 2025) hat es über 55.000 Sterne und unterstützt fast 100 Modellarchitekturen, was es zu einem Grundpfeiler für skalierbare AI-Bereitstellungen macht.

[arXiv-Paper zu PagedAttention](https://arxiv.org/abs/2309.06180)  
[vLLM GitHub Repository](https://github.com/vllm-project/vllm)  
[vLLM Rückblick 2024 Blog](https://blog.vllm.ai/2025/01/10/vllm-2024-wrapped-2025-vision.html)  
[PyTorch Integration Announcement](https://pytorch.org/blog/vllm-joins-pytorch/)