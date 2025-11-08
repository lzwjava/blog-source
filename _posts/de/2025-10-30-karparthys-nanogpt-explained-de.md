---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Karpathys nanoGPT und nanochat erklärt
translated: true
type: note
---

### Überblick
Sowohl **nanoGPT** als auch **nanochat** sind Open-Source-Projekte, die von Andrej Karpathy (ehemaliger OpenAI/Tesla AI Lead) erstellt wurden, um die internen Abläufe von Large Language Models (LLMs) durch minimale, von Grund auf implementierte Versionen in PyTorch zu vermitteln. Es handelt sich eher um Lehrmittel als um produktionsreife Systeme, die Einfachheit und Lesbarkeit über Optimierungen stellen.

- **nanoGPT** (veröffentlicht 2023): Ein leichtgewichtiges Framework zum Trainieren von GPT-ähnlichen Transformer-Modellen auf Rohtextdaten, das sich ausschließlich auf die Pre-Training-Phase konzentriert.
- **nanochat** (veröffentlicht im Oktober 2025): Eine erweiterte, Full-Stack-Weiterentwicklung von nanoGPT, die end-to-end Training, Fine-Tuning, Inferenz und Deployment einer ChatGPT-ähnlichen Konversations-KI ermöglicht.

### Wichtige Unterschiede
Hier ein direkter Vergleich:

| Aspekt               | nanoGPT                                                                 | nanochat                                                                 |
|----------------------|-------------------------------------------------------------------------|--------------------------------------------------------------------------|
| **Hauptfokus**       | Pre-Training eines GPT-Modells auf unstrukturiertem Text (z.B. Shakespeare-Datensatz). | Vollständige Pipeline: Pre-Training + Fine-Tuning für Chat + Inferenz in einer Web-UI. |
| **Umfang**           | Minimale Transformer-Implementierung (~400 Zeilen Kerncode). Keine Chat-Oberfläche. | ~8.000 Zeilen gesamt, inklusive RLHF-ähnlichem Fine-Tuning, Sampling und einer Streamlit-basierten Chat-Demo. |
| **Training**         | Kausale Sprachmodellierung mittels Next-Token-Prediction. | Erweitert um Supervised Fine-Tuning (SFT) und Preference Optimization (z.B. DPO) für Dialoge. |
| **Inferenz**         | Einfache Texterzeugung.                                                | Interaktiver Chat-Modus mit System/User/Assistant-Prompts, Temperature Sampling und Sicherheitsfiltern. |
| **Hardware/Kosten**  | Trainierbar auf einer einzelnen GPU (z.B. 125M Parameter in Stunden).  | Ähnliche Effizienz; behauptet "besten ChatGPT, den 100 $ kaufen können" via günstiger Cloud-GPUs. |
| **Inspirationen**    | Vermittelt Transformer-Grundlagen.                                     | Baut auf nanoGPT + modded-nanoGPT (gamifizierte Version) auf; zielt auf einen vollständigen "ChatGPT-Klon" ab. |
| **Anwendungsfall**   | Lernen von LLM Pre-Training.                                           | Aufbau und Deployment einer grundlegenden Konversations-KI von Grund auf. |
| **GitHub Stars**     | ~30k+ (Stand 2025).                                                    | Neu veröffentlicht; schnelles Wachstum auf 10k+ in Tagen.                |

Im Wesentlichen ist nanoGPT wie der Aufbau des "Gehirns" eines GPT-Modells, während nanochat den "Mund" (Chat-Oberfläche) und die "Ohren" (Dialogbehandlung) hinzufügt, was es zu einem umfassenderen Tutorial für moderne LLM-Anwendungen macht. Wenn Sie einsteigen, beginnen Sie mit nanoGPT für die Grundlagen und wechseln dann zu nanochat für chat-spezifische Erweiterungen.

### Referenzen
- [nanochat GitHub Repo](https://github.com/karpathy/nanochat)
- [Karpathys Ankündigung auf X](https://x.com/karpathy/status/1977755427569111362)
- [Forbes-Artikel über nanochat](https://www.forbes.com/sites/lanceeliot/2025/10/15/make-your-own-chatgpt-clone-for-just-100-via-newly-released-nanochat-but-theres-a-catch/)
- [Medium Post: From nanoGPT to NanoChat](https://medium.com/@sebuzdugan/nanochat-build-your-own-chatgpt-clone-in-8-000-lines-of-code-e07a70cc435e)