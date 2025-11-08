---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Steuerung der RNN-Textgenerationstemperatur
translated: true
type: note
---

### Temperatur beim RNN-Sampling verstehen

Bei rekurrenten neuronalen Netzen (RNNs) für die Texterzeugung – wie sie Andrej Karpathy in seinem berühmten Blogbeitrag über Character-Level-Sprachmodelle untersucht – ist die Temperatur ein Hyperparameter, der beeinflusst, wie "zufällig" oder "vorhersehbar" der erzeugte Text wirkt. Sie wird während des Sampling-Schritts angewendet, bei dem das RNN das nächste Zeichen (oder Token) auf der Grundlage der vorherigen Zeichen vorhersagt. Ohne Temperaturkontrolle kann die Erzeugung zu starr sein (immer die wahrscheinlichste Wahl, was zu langweiligen Schleifen führt) oder zu wild (reine Zufälligkeit). Die Temperatur schafft einen Ausgleich, indem sie die Wahrscheinlichkeitsverteilung des Modells über die möglichen nächsten Zeichen glättet.

#### Kurze Erklärung der Mathematik
Das RNN gibt *Logits* (rohe, nicht normalisierte Werte) für jedes mögliche nächste Zeichen aus. Diese werden mit der Softmax-Funktion in Wahrscheinlichkeiten umgewandelt:

\\[
p_i = \frac{\exp(\text{logit}_i / T)}{\sum_j \exp(\text{logit}_j / T)}
\\]

- \\(T\\) ist die Temperatur (typischerweise zwischen 0,1 und 2,0).
- Wenn \\(T = 1\\), ist es die Standard-Softmax-Funktion: Die Wahrscheinlichkeiten spiegeln das "natürliche" Vertrauen des Modells wider.
- Anschließend wird das nächste Zeichen aus dieser Verteilung *gesampelt* (z.B. via multinomialem Sampling), anstatt immer die Wahl mit der höchsten Wahrscheinlichkeit zu treffen (greedy Decoding).

Dieses Sampling geschieht iterativ: Das gewählte Zeichen wird als Eingabe zurückgeführt, das nächste wird vorhergesagt, und dieser Vorgang wird wiederholt, um eine Sequenz zu erzeugen.

#### Niedrige Temperatur: Wiederholend aber sicher
- **Effekt**: \\(T < 1\\) (z.B. 0,5 oder nahe 0) *verschärft* die Verteilung. Vorhersagen mit hohem Konfidenzniveau erhalten noch höhere Wahrscheinlichkeiten, während niedrige Wahrscheinlichkeiten gegen Null gedrückt werden.
- **Ausgabe**: Der Text bleibt "sicher" und kohärent, wird aber schnell repetitiv. Das Modell bleibt auf den wahrscheinlichsten Pfaden, als wäre es in einer Schleife gefangen.
- **Beispiel aus Karpathys Beitrag** (Erzeugung von Paul Graham-artigen Essays): Bei sehr niedriger Temperatur erzeugt es etwa so etwas:  
  > “is that they were all the same thing that was a startup is that they were all the same thing that was a startup is that they were all the same thing that was a startup is that they were all the same”  

  Es ist selbstsicher und grammatikalisch korrekt, aber es fehlt an Kreativität – man denke an ein unendliches Echo der Trainingsdaten.

#### Hohe Temperatur: Kreativ aber sprunghaft
- **Effekt**: \\(T > 1\\) (z.B. 1,5 oder 2,0) *ebnet* die Verteilung ein. Die Wahrscheinlichkeiten werden gleichmäßiger, sodass Außenseiter (weniger wahrscheinliche Zeichen) eine bessere Chance erhalten.
- **Ausgabe**: Vielfältigerer und erfinderischerer Text, aber er neigt zu Unsinn, Rechtschreibfehlern oder wilden Abschweifungen. Das Modell erkundet seltene Pfade, was Originalität fördern kann, aber auf Kosten der Kohärenz.
- **Beispiel von Karpathy**: Höhere Temperaturen ergeben abwechslungsreichere Essays mit frischen Formulierungen, aber "at cost of more mistakes (e.g. spelling mistakes, etc.)". Es ist, als ob das RNN frei brainstormt – gut für Poesie oder Science-Fiction, riskant für sachliches Schreiben.

#### Warum sie bei RNNs wichtig ist
RNNs (oder LSTMs in Karpathys Setup) sind autoregressiv: Jede Vorhersage baut auf der letzten auf, sodass sich kleine Verzerrungen im Sampling über lange Sequenzen hinweg verstärken. Die Temperatur ermöglicht es, Exploration vs. Exploitation abzustimmen:
- Verwende niedriges \\(T\\) für zuverlässige, on-brand Texte (z.B. Produktbeschreibungen).
- Erhöhe sie für Brainstorming oder künstlerische Generierung (z.B. surreale Geschichten).
- Experimentiere im Code: Karpathys Vanilla-RNN-Repo enthält einen Temperatur-Schieberegler – probiere ihn mit Shakespeare-Samples aus, um den Übergang von langweiligen Sonetten zu chaotischen Versen zu sehen.

Im Wesentlichen "lernt" die Temperatur nichts Neues; sie stellt lediglich den Kreativitätsregler des RNNs während der Inferenz ein. Niedrig hält es ruhig und vorhersehbar; hoch entfesselt das Chaos.

[The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)