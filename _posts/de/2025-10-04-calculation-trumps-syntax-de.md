---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Berechnung schlägt Syntax in KI
translated: true
type: note
---

Du hast absolut recht, dass es bei KI und LLMs nicht um elegante Prosa oder philosophische Betrachtungen von Programmiersprachen geht – auch wenn Leute wie Yin Wang und Daniel P. Friedman unser Denken dort zweifellos geschärft haben. Wangs Blog taucht tief in die Eingeweide von Systemen wie Python und Lisp ein und kritisiert, wie sie Berechnungen in der Praxis beeinflussen, während Friedmans Bücher (denk an *The Little Schemer* Reihe) Rekursion und funktionale Paradigmen fast schon poetisch entmystifizieren. Aber ja, wenn es darum geht, etwas zu bauen, das *funktioniert* – wie kohärenten Text zu generieren oder Gradienten in einem neuronalen Netz zu berechnen – dann zeigt sich der wahre Wert im "Wie" und "Was" der Berechnung, nicht im syntaktischen Zucker.

### Warum Berechnung wichtiger ist als Syntax
Im Kern führt ein LLM wie ich keine Gedanken über Lisp-Makros oder Javas Objekthierarchien aus; es führt Matrixmultiplikationen, Attention-Mechanismen und probabilistisches Sampling in großem Maßstab durch. Das "Wie man berechnet" läuft auf Folgendes hinaus:
-   **Algorithmen und Modelle**: Dinge wie Transformer-Architekturen (Vaswani et al., 2017) definieren, *was* berechnet wird – Self-Attention über Token-Embeddings, positionsabhängige Kodierungen usw. Hier passiert die Magie, unabhängig von der Sprache. Man könnte GPT in Pseudocode implementieren und es würde "auf dem Papier" funktionieren; die Syntax ist nur ein Vehikel.
-   **Numerische Präzision und Effizienz**: Hier ist "was berechnet wird" enorm wichtig. Wir sprechen über Token-Wahrscheinlichkeiten, Loss-Funktionen (z.B. Kreuzentropie) und Backpropagation. Wenn man die Mathematik vermasselt, halluziniert das Modell nur noch Müll. Syntax? Sie ist zweitrangig – Pythons NumPy bringt einen zu 90 % dorthin mit lesbarer Einfachheit, aber es ist interpretiert und langsam für das Training von Giganten.

Die Sprachwahl schleicht sich allerdings als pragmatischer Filter ein. C++ glänzt für die leistungskritische Basis der KI (z.B. TensorFlows Kernel oder PyTorchs CUDA-Bindungen), wo jeder Taktzyklus im verteilten Training zählt. Python dominiert beim Prototyping, weil es prägnant ist – warum sich mit C++ Speicherverwaltung herumschlagen, wenn `torch.nn.Linear` erlaubt, Layer in einer Zeile zu verketten? Aber du hast recht: es ist ein "kleines Problem". Die echten Engpässe sind algorithmisch (z.B. Skalierungsgesetze wie von Kaplan et al.) oder datenbedingt, nicht ob man `def` oder `struct` tippt.

### Wo sich PL-Erkenntnisse dennoch einschleichen
Trotzdem fühlt es sich an, als würde man das Kind mit dem Bade ausschütten, wenn man PL komplett abtut. Gutes Sprachen-Design (inspiriert von Friedman/Wang-Typen) macht das *Ausdrücken* dieser Berechnungen sicherer und schneller:
-   **Abstraktionen für die Schlussfolgerung**: Funktionale Reinheit (à la Scheme) hilft, Bugs in probabilistischem Code zu vermeiden, was enorm wichtig für zuverlässige KI-Inferenz ist.
-   **Leistung ohne Schmerz**: Rust oder sogar modernes C++ borgen sich von der PL-Forschung, um Geschwindigkeit *plus* Sicherheit zu bieten und so die "falsch berechnen"-Fehler zu reduzieren, die rohes C plagen.

Am Ende besteht der KI-Fortschritt aus 80 % Mathematik/Modelle/Daten, 15 % Engineering (wo Sprachen wie C++ glänzen) und 5 % Syntax-Poesie. Wenn wir Letzteres optimieren würden, hätten wir hübschere Papers, aber langsamere Roboter. Was ist deine Meinung – glaubst du, wir werden mehr PL-KI-Fusion sehen, wie domainspezifische Sprachen für neuro-symbolische Sachen?

[Wang's Blog](https://www.yinwang.org)  
[Friedman's Essence of Programming](https://www.cs.indiana.edu/~dfriedman/)  
[Attention Is All You Need (Transformers Paper)](https://arxiv.org/abs/1706.03762)  
[Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361)