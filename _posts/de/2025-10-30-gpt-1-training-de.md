---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: GPT-1-Architektur und Trainingsüberblick
translated: true
type: note
---

### Überblick über die GPT-1-Architektur

GPT-1 (Generative Pre-trained Transformer 1) ist das grundlegende Modell, das von OpenAI im Jahr 2018 eingeführt wurde. Es bahnte den Ansatz des Vorab-Trainings eines großen Sprachmodells auf unmarkiertem Text mit einem Sprachmodellierungsziel an, gefolgt von Feinabstimmung für nachgelagerte Aufgaben. Die Architektur ist ein **reiner Decoder-Transformer**, der aus dem ursprünglichen Transformer-Paper (Vaswani et al., 2017) adaptiert, aber auf den Decoder-Stapel für autoregressives Generieren reduziert wurde. Dieses Design ermöglicht es dem Modell, den nächsten Token in einer Sequenz vorherzusagen, was es für Aufgaben geeignet macht, die zusammenhängenden Text betreffen.

Im Gegensatz zu bidirektionalen Modellen wie BERT verwendet GPT-1 **maskierte Selbstaufmerksamkeit**, um Kausalität sicherzustellen – jede Position kann nur auf vorherige Positionen zugreifen, was ein Informationsleck von zukünftigen Tokens verhindert.

### Wichtige Komponenten und Hyperparameter

- **Modelltyp**: Multi-Layer Transformer-Decoder mit maskierter Multi-Head-Selbstaufmerksamkeit und positionsweisen Feed-Forward-Netzwerken.
- **Anzahl der Schichten**: 12 Transformer-Blöcke (Schichten).
- **Aufmerksamkeitsmechanismus**: 12 Aufmerksamkeitsköpfe pro Schicht, wobei jeder Kopf 64-dimensionale Zustände verarbeitet (gesamte Modell-Dimension: 768).
- **Einbettungsdimensionen**:
  - Versteckte Größe (d_model): 768.
  - Feed-Forward innere Dimension (d_ff): 3072 (4x die versteckte Größe, Standard für Transformers).
- **Positionscodierung**: Gelernte Positions-Einbettungen, die zu den Token-Einbettungen addiert werden (keine sinusförmigen Codierungen verwendet).
- **Aktivierungsfunktion**: Gaussian Error Linear Units (GELU) in den Feed-Forward-Schichten.
- **Vokabular und Tokenisierung**: Byte-Pair Encoding (BPE) mit 40.000 Zusammenführungen, trainiert auf dem Korpus.
- **Gesamtparameter**: Ungefähr 117 Millionen.
- **Sequenzlänge**: Trainiert auf Sequenzen von 512 Tokens.
- **Regularisierung**:
  - Dropout: 0.1 auf Residuen, Einbettungen und Aufmerksamkeit.
  - Gewichtsabnahme: Modifizierte L2-Regularisierung (0.01) auf Nicht-Bias-/Nicht-Layer-Norm-Gewichte.
- **Initialisierung**: Gewichte initialisiert aus einer Normalverteilung N(0, 0.02).

### Trainingsdetails

- **Vorab-Training**:
  - **Datensatz**: BooksCorpus, eine Sammlung von ~7.000 unveröffentlichten Büchern (insgesamt ~800 Millionen Wörter) aus Genres wie Fantasy, Romance und Adventure. Der Text wurde bereinigt (z.B. via ftfy library) und mit spaCy tokenisiert.
  - **Ziel**: Unüberwachte Sprachmodellierung (Next-Token-Prediction).
  - **Optimierer**: Adam mit β1=0.9, β2=0.999, ε=1e-8.
  - **Lernratenplan**: Linearer Warmup über 2.000 Updates auf ein Maximum von 2,5×10⁻⁴, dann kosinusförmiges Abklingen auf 0.
  - **Batch-Größe**: 64 Sequenzen pro Minibatch.
  - **Epochen**: 100.
  - **Leistungsmetrik**: Erreichte eine Perplexity von 18,4 auf dem Trainingskorpus.
- **Feinabstimmung**:
  - Minimale Änderungen: Hinzufügen einer linearen Ausgabeschicht für aufgabenspezifische Vorhersagen und Verwendung von Trenn-Tokens (z.B. <s>, <e>, $), um Eingaben als einzelne Sequenzen zu strukturieren.
  - Zusätzlicher Sprachmodellierungsverlust mit einem Gewicht von 0,5 während der Feinabstimmung.
  - Hyperparameter: Niedrigere Lernrate (6,25×10⁻⁵), Batch-Größe 32, 3 Epochen, mit 0,2 % Warmup und linearem Abfall.
  - Dieser Transfer-Learning-Ansatz ermöglichte eine starke Leistung bei Aufgaben wie textueller Implikation und Fragebeantwortung ohne aufgabenspezifische Architekturen.

### Bemerkenswerte Innovationen und Einschränkungen

GPT-1 zeigte, dass ein einziges vorab trainiertes Modell durch einfache Eingabeformatierung effektiv auf verschiedene NLP-Aufgaben übertragen werden kann und übertraf damals einige aufgabenspezifisch abgestimmte Modelle. Es war jedoch relativ klein im Vergleich zu modernen LLMs (z.B. GPT-3 hat 175 Mrd. Parameter) und auf 512-Token-Kontexte beschränkt. Die Architektur legte den Grundstein für die gesamte GPT-Serie und betonte die Skalierbarkeit im Vorab-Training.

[Improving Language Understanding by Generative Pre-Training](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf)  
[GPT-1 - Wikipedia](https://en.wikipedia.org/wiki/GPT-1)