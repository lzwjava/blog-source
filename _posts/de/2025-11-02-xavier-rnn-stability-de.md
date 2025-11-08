---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Xavier-Initialisierung für RNN-Stabilität
translated: true
type: note
---

### Warum Xavier-Initialisierung in RNNs?

RNNs (Recurrent Neural Networks) nutzen die Xavier-Initialisierung (auch Glorot-Initialisierung genannt) für ihre Gewichtsmatrizen – wie `Wxh` (Eingabe-zu-Versteckt), `Whh` (Versteckt-zu-Versteckt, die rekurrenten Gewichte) und `Why` (Versteckt-zu-Ausgabe) – um stabile Trainingsdynamiken zu gewährleisten. Die spezifische Form in Ihrem Code verwendet eine Gaußsche (Normal-)Verteilung, skaliert mit `sqrt(1 / fan_in)`, wobei `fan_in` die Anzahl der Eingabeneuronen für diese Schicht ist. Dies hält die Varianz der Gewichte bei etwa `1 / fan_in` und stellt sicher, dass eingehende Signale nicht zu stark verstärkt oder unterdrückt werden.

Hier ist der Grund, warum dies für RNNs entscheidend ist und warum eine einfache gleichmäßige Zufallsziehung aus [0, 1] Probleme verursachen würde:

#### 1. **Bewahrung der Signalvarianz über Schichten und Zeitschritte hinweg**
   - In Feedforward-Netzen hilft Xavier, die *Varianz der Aktivierungen* ungefähr konstant zu halten, während Signale vorwärts (und Gradienten rückwärts) propagieren. Ohne dies könnten tiefe Schichten explodierende (riesig werdende) oder verschwindende (auf nahe Null fallende) Aktivierungen sehen, was Training unmöglich macht.
   - RNNs sind wie "tiefe" Netzwerke, die *über die Zeit entrollt* sind: Das rekurrente Gewicht `Whh` multipliziert den versteckten Zustand bei jedem Zeitschritt, was eine Kette von Multiplikationen erzeugt (z.B. für Sequenzlänge *T* ist es wie *T* Schichten tief). Wenn Gewichte in `Whh` eine Varianz >1 haben, explodieren Gradienten exponentiell rückwärts (schlecht für lange Sequenzen). Bei <1 verschwinden sie.
   - Xaviers Skalierung (z.B. `* sqrt(1. / hidden_size)` für `Whh`) stellt sicher, dass die erwartete Varianz des versteckten Zustands bei ~1 bleibt und dies verhindert. Für [0,1] Gleichverteilungs-Init:
     - Mittelwert ~0,5 (positiv verzerrt, verursacht Drifts).
     - Varianz ~1/12 ≈ 0,083 – zu klein für große `hidden_size` (z.B. 512), was schnell zu verschwindenden Signalen führt.

#### 2. **Anpassung an Schichtdimensionen**
   - Xavier berücksichtigt *fan_in* (Eingänge in die Schicht) und manchmal *fan_out* (Ausgänge). Für `Wxh` normalisiert die Skalierung mit `sqrt(1 / input_size)` basierend auf Vokabulargröße oder Embedding-Dimensionen. Für `Whh` basiert sie auf `hidden_size`, um der rekurrenten Schleife zu entsprechen.
   - [0,1] ignoriert Dimensionen: In einer großen versteckten Schicht (z.B. 1000 Einheiten) würde die Summierung vieler [0,1]-Eingänge ohne Skalierung die nächste Schicht überfordern. In kleinen Schichten würde sie unterlaufen.

#### 3. **Gradientenfluss in Backpropagation Through Time (BPTT)**
   - RNN-Training verwendet BPTT, bei dem Gradienten rückwärts über *T* Schritte fließen. Schlechte Initialisierung führt zum "Vanishing Gradient Problem" (häufig in vanilla RNNs, weshalb LSTMs/GRUs existieren). Xavier mildert dies, indem es mit ausgeglichenen Magnituden startet.
   - Empirische Studien (z.B. das Originalpapier von Glorot & Bengio) zeigen, dass Xavier die für die Konvergenz benötigten Epochen in tiefen/rekurrenten Netzen um das 2-10-fache reduziert.

#### Alternativen und wann [0,1] "funktionieren" könnte
- [0,1] könnte für winzige Toy-Modelle (z.B. Einzelschicht, kurze Sequenzen) "funktionieren", versagt aber bei Skalierung – denke an explodierende Loss-Werte oder NaNs.
- Moderne Anpassungen: He-Initialisierung (für ReLUs, skaliert mit `sqrt(2 / fan_in)`) oder orthogonale Initialisierung (für RNNs, erhält Normen exakt). Aber Xavier ist eine sichere Standardwahl für sigmoid/tanh Aktivierungen, die in RNNs üblich sind.

Kurz gesagt, bei Xavier geht es um *Stabilität zuerst*: Es setzt Gewichte klein-aber-nicht-zu-klein, dimensionsabhängig, um Gradientenfluss frei zu ermöglichen. Zufällige [0,1]-Werte sind zu grob – wie ein Auto ohne Auswuchten der Reifen zu beschleunigen.

Für vertiefende Einblicke:  
[Understanding the Difficulty of Training Deep Feedforward Neural Networks](http://proceedings.mlr.press/v9/glorot10a/glorot10a.pdf) (Glorot & Bengio, 2010)  
[Recurrent Neural Network Regularization](https://arxiv.org/abs/1409.2329) (Zaremba et al., zu RNN-Init-Problemen)