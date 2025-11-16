---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Karpathys nanoGPT und nanochat
translated: true
type: note
---

### Überblick
nanoGPT und nanochat sind beide Open-Source-Projekte von Andrej Karpathy, die entwickelt wurden, um das Training großer Sprachmodelle (LLM) zugänglich und lehrreich zu machen. nanoGPT (veröffentlicht 2023) konzentriert sich auf die Grundlagen des Trainings von GPT-artigen Modellen von Grund auf, während nanochat (veröffentlicht im Oktober 2025) darauf aufbaut und eine umfassendere "Full-Stack"-Pipeline zur Erstellung eines ChatGPT-ähnlichen Chatbots darstellt. Die Hauptunterschiede liegen im Umfang, den Trainingsphasen, der Komplexität der Codebasis und der End-to-End-Tauglichkeit – nanochat entwickelt nanoGPT im Wesentlichen zu einem vollständigen, produktionsreifen System für konversationelle KI weiter.

### Wichtige Unterschiede im Trainingscode
Der Trainingscode in nanochat ist eine Erweiterung und Verfeinerung des Ansatzes von nanoGPT, beinhaltet jedoch zusätzliche Phasen, Optimierungen und Integrationen, die auf Chat-Anwendungen zugeschnitten sind. Hier eine Aufschlüsselung:

| Aspekt                  | nanoGPT                                                                 | nanochat                                                                 |
|-------------------------|-------------------------------------------------------------------------|--------------------------------------------------------------------------|
| **Hauptfokus**      | Pre-Training eines Transformer-basierten GPT-Modells auf Rohtextdaten (z.B. OpenWebText oder Shakespeare). Vermittelt Kernkonzepte wie Tokenisierung, Modellarchitektur und grundlegende Trainingsschleifen. | Vollständige Pipeline: Pre-Training + Mid-Training (Konversationen/Multiple-Choice) + Supervised Fine-Tuning (SFT) + optional Reinforcement Learning (RLHF via GRPO) + Evaluation + Inferenz. Erstellt einen einsatzbereiten Chatbot. |
| **Trainingsphasen**    | - Einphasiges Pre-Training.<br>- Grundlegende Evaluation (z.B. Perplexity). | - **Pre-Train**: Ähnlich wie nanoGPT, aber auf FineWeb-Datensatz.<br>- **Mid-Train**: Auf SmolTalk (Benutzer-Assistent-Dialoge), Multiple-Choice-Q&A und Tool-Use-Daten.<br>- **SFT**: Feintuning für Chat-Alignment, evaluiert mit Benchmarks wie MMLU, ARC-E/C, GSM8K (Mathe), HumanEval (Code).<br>- **RL**: Optionales RLHF auf GSM8K für Präferenz-Alignment.<br>- Automatisierte Erstellung von Report Cards mit Metriken (z.B. CORE-Score). |
| **Codebasis-Größe & Struktur** | ~600 Zeilen gesamt (z.B. `train.py` ~300 Zeilen, `model.py` ~300 Zeilen). Minimaler, hackbarer PyTorch-Code; priorisiert Einfachheit gegenüber Vollständigkeit. Zugunsten von nanochat als veraltet markiert. | ~8.000 Zeilen sauberer, modularer PyTorch-Code. Beinhaltet Rust-basierte Tokenisierung, effiziente Inferenz-Engine (KV-Cache, Prefill/Decode), Tool-Integration (z.B. Python-Sandbox) und Web-UI. Kohärenter, aber dennoch forkbar. |
| **Optimierer & Hyperparameter** | Standard AdamW; Lernraten abgestimmt auf mittelgroße Modelle (z.B. GPT-2 124M Parameter). | Muon + AdamW Hybrid (inspiriert von modded-nanoGPT); adaptive Lernraten (z.B. niedriger für kleinere Datensätze, um Overfitting zu vermeiden). Skalierung via `--depth`-Flag für Modellgröße. |
| **Datenverarbeitung**      | Rohtext-Korpora; grundlegendes BPE-Tokenizer-Training. | Erweitert: Training eines eigenen Tokenizers (Vokabulargröße ~65K); nutzt Hugging Face Datasets (FineWeb für Pre-Train, SmolTalk für Konversationen). Unterstützt synthetische Daten für Persönlichkeits-Infusion. |
| **Trainingszeit & Kosten** | ~4 Tage auf 8xA100 für GPT-2-Äquivalent (~$500+). Fokussiert auf Lehrläufe. | ~4 Stunden auf 8xH100 für ein grundlegendes 560M-Parameter-Modell (~$100); ~12 Stunden übertrifft GPT-2; skaliert bis ~$1.000 für stärkere Modelle (z.B. 40% MMLU nach 24 Stunden). |
| **Inferenz & Deployment** | Grundlegende Textgenerierung; kein eingebauter Chat oder UI. | Optimierte Engine mit KV-Cache; CLI-Chat; ChatGPT-artige Web-UI; Tool Use (z.B. Code-Ausführung). Modelle sind "naiv/albern", aber unterhaltsam bei kleiner Skalierung. |
| **Lehrziel**   | Bau der "Eingeweide" eines Sprachmodells (Gehirn). Ideal für Anfänger, die mit Architekturen experimentieren. | Bau eines vollständigen ChatGPT-Klons (vom Gehirn zur Schnittstelle). Abschlussprojekt für fortgeschrittene Kurse wie LLM101n; potenzieller Forschungs-Benchmark. |

### Wann man was verwendet
- **Wählen Sie nanoGPT**, wenn Sie neu bei LLMs sind und eine leichtgewichtige Einführung in das Pre-Training wünschen (z.B. zum Experimentieren mit Architekturen oder Datensätzen). Es ist einfacher, aber auf nicht-konversationelle Modelle beschränkt.
- **Wählen Sie nanochat** für die End-to-End-Entwicklung eines Chatbots. Es übertrifft nanoGPT bei Chat-Aufgaben (z.B. 58% Verbesserung in einigen RLHF-Tests) und beinhaltet alles, was benötigt wird, um von den Daten zu einer funktionierenden UI in einem Repository zu gelangen.

Beide betonen Hackbarkeit – z.B. erlaubt nanochat einfaches Skalieren (Modelltiefe ändern) oder Anpassen (Hinzufügen synthetischer Daten für Persönlichkeit). nanochat verleiht dem Modell sogar Selbstbewusstsein (z.B. kennt es seine eigene Größe und Limitationen).

Für praktische Erkundung:
- [nanoGPT GitHub](https://github.com/karpathy/nanoGPT)
- [nanochat GitHub](https://github.com/karpathy/nanochat)

Wenn Sie diese ausführen, starten Sie mit nanochats `speedrun.sh`-Skript auf einer Cloud-GPU wie Lambda Labs für die vollständige Erfahrung.