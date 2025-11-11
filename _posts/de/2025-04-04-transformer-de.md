---
audio: false
generated: true
lang: de
layout: post
title: Transformator
translated: true
type: note
---

Der **Transformer** ist eine revolutionäre Architektur für neuronale Netze, die zur Grundlage der meisten modernen Large Language Models (LLMs) geworden ist. Sie wurde in dem bahnbrechenden Papier "Attention Is All You Need" aus dem Jahr 2017 von Vaswani et al. vorgestellt und hat seitdem das Feld der Natural Language Processing (NLP) grundlegend verändert.

Im Gegensatz zu früheren dominierenden Architekturen wie Recurrent Neural Networks (RNNs), die sequentielle Daten Schritt für Schritt verarbeiten, verarbeitet der Transformer gesamte Eingabesequenzen **parallel**. Dieser entscheidende Unterschied ermöglicht erhebliche Verbesserungen der Trainingsgeschwindigkeit und die Fähigkeit, langreichweitige Abhängigkeiten innerhalb des Textes zu erfassen.

Hier ein detaillierter Blick auf die Schlüsselkomponenten und Konzepte der Transformer-Architektur im Kontext von LLMs:

**1. Kernidee: Attention-Mechanismus**

Die zentrale Innovation des Transformers ist der **Attention-Mechanismus**, insbesondere **Self-Attention**. Dieser Mechanismus ermöglicht es dem Modell, die Bedeutung verschiedener Wörter (oder Tokens) in der Eingabesequenz zu gewichten, wenn es ein bestimmtes Wort verarbeitet. Anstatt sich nur auf die unmittelbar vorangehenden Wörter zu verlassen (wie RNNs), ermöglicht Self-Attention dem Modell, den gesamten Kontext zu berücksichtigen, um die Bedeutung und die Beziehungen zwischen den Wörtern zu verstehen.

Man kann es sich so vorstellen: Wenn Sie einen Satz lesen, verarbeiten Sie nicht jedes Wort isoliert. Ihr Gehirn berücksichtigt gleichzeitig alle Wörter, um die Gesamtbedeutung und den Beitrag jedes Wortes dazu zu verstehen. Der Self-Attention-Mechanismus ahmt dieses Verhalten nach.

**Wie Self-Attention funktioniert (vereinfacht):**

Für jedes Wort in der Eingabesequenz berechnet der Transformer drei Vektoren:

* **Query (Q):** Stellt dar, wonach das aktuelle Wort in den anderen Wörtern "sucht".
* **Key (K):** Stellt dar, welche Information jedes andere Wort "enthält".
* **Value (V):** Stellt die eigentliche Information dar, die jedes andere Wort enthält und die relevant sein könnte.

Der Self-Attention-Mechanismus führt dann die folgenden Schritte durch:

1.  **Berechnung der Attention-Scores:** Das Skalarprodukt zwischen dem Query-Vektor eines Wortes und dem Key-Vektor jedes anderen Wortes in der Sequenz wird berechnet. Diese Scores zeigen an, wie relevant die Information jedes anderen Wortes für das aktuelle Wort ist.
2.  **Skalierung der Scores:** Die Scores werden durch die Quadratwurzel der Dimension der Key-Vektoren (`sqrt(d_k)`) geteilt. Diese Skalierung hilft, die Gradienten während des Trainings zu stabilisieren.
3.  **Anwendung von Softmax:** Die skalierten Scores werden durch eine Softmax-Funktion geleitet, die sie in Wahrscheinlichkeiten zwischen 0 und 1 normalisiert. Diese Wahrscheinlichkeiten repräsentieren die **Attention-Gewichte** – also, wie viel "Aufmerksamkeit" das aktuelle Wort jedem der anderen Wörter schenken sollte.
4.  **Berechnung der gewichteten Values:** Der Value-Vektor jedes Wortes wird mit seinem entsprechenden Attention-Gewicht multipliziert.
5.  **Summierung der gewichteten Values:** Die gewichteten Value-Vektoren werden aufsummiert, um den **Ausgabevektor** für das aktuelle Wort zu erzeugen. Dieser Ausgabevektor enthält nun Informationen von allen anderen relevanten Wörtern in der Eingabesequenz, gewichtet nach ihrer Wichtigkeit.

**2. Multi-Head Attention**

Um die Fähigkeit des Modells, verschiedene Arten von Beziehungen zu erfassen, weiter zu verbessern, verwendet der Transformer **Multi-Head Attention**. Anstatt den Self-Attention-Mechanismus nur einmal durchzuführen, geschieht dies mehrmals parallel mit verschiedenen Sätzen von Query-, Key- und Value-Gewichtsmatrizen. Jeder "Head" lernt, sich auf verschiedene Aspekte der Beziehungen zwischen den Wörtern zu konzentrieren (z.B. grammatikalische Abhängigkeiten, semantische Verbindungen). Die Ausgaben aller Attention-Heads werden dann konkateniert und linear transformiert, um die endgültige Ausgabe der Multi-Head-Attention-Schicht zu erzeugen.

**3. Positional Encoding**

Da der Transformer alle Wörter parallel verarbeitet, gehen Informationen über die **Reihenfolge** der Wörter in der Sequenz verloren. Um dies zu beheben, wird den Eingabe-Embeddings ein **Positional Encoding** hinzugefügt. Diese Kodierungen sind Vektoren, die die Position jedes Wortes in der Sequenz repräsentieren. Es handelt sich typischerweise um feste Muster (z.B. sinusförmige Funktionen) oder gelernte Embeddings. Durch das Hinzufügen von Positional Encodings kann der Transformer die sequentielle Natur der Sprache verstehen.

**4. Encoder- und Decoder-Stacks**

Die Transformer-Architektur besteht typischerweise aus zwei Hauptteilen: einem **Encoder** und einem **Decoder**, die beide aus mehreren identischen, übereinandergestapelten Schichten bestehen.

* **Encoder:** Die Rolle des Encoders besteht darin, die Eingabesequenz zu verarbeiten und eine reichhaltige Repräsentation davon zu erstellen. Jede Encoder-Schicht enthält typischerweise:
    * Eine **Multi-Head-Self-Attention**-Sub-Schicht.
    * Ein **Feed-Forward Neural Network**-Sub-Schicht.
    * **Residual Connections** um jede Sub-Schicht, gefolgt von **Layer Normalization**. Residual Connections helfen beim Gradientenfluss während des Trainings, und Layer Normalization stabilisiert die Aktivierungen.

* **Decoder:** Die Rolle des Decoders besteht darin, die Ausgabesequenz zu generieren (z.B. bei maschineller Übersetzung oder Textgenerierung). Jede Decoder-Schicht enthält typischerweise:
    * Eine **maskierte Multi-Head-Self-Attention**-Sub-Schicht. Die "Maskierung" verhindert, dass der Decoder während des Trainings auf zukünftige Tokens in der Zielsequenz vorausschaut, und stellt sicher, dass er nur bereits generierte Tokens verwendet, um den nächsten vorherzusagen.
    * Eine **Multi-Head-Attention**-Sub-Schicht, die sich auf die Ausgabe des Encoders konzentriert. Dies ermöglicht es dem Decoder, sich auf die relevanten Teile der Eingabesequenz zu konzentrieren, während er die Ausgabe generiert.
    * Ein **Feed-Forward Neural Network**-Sub-Schicht.
    * **Residual Connections** und **Layer Normalization**, ähnlich wie beim Encoder.

**5. Feed-Forward Networks**

Jede Encoder- und Decoder-Schicht enthält ein Feed-Forward Neural Network (FFN). Dieses Netzwerk wird auf jeden Token unabhängig angewendet und hilft, die durch die Attention-Mechanismen gelernten Repräsentationen weiter zu verarbeiten. Es besteht typischerweise aus zwei linearen Transformationen mit einer nichtlinearen Aktivierungsfunktion (z.B. ReLU) dazwischen.

**Wie Transformers in LLMs verwendet werden:**

LLMs basieren primär auf der **Decoder-only**-Transformer-Architektur (wie GPT-Modelle) oder der **Encoder-Decoder**-Architektur (wie T5).

* **Decoder-only-Modelle:** Diese Modelle sind darauf trainiert, den nächsten Token in einer Sequenz vorherzusagen, basierend auf den vorangehenden Tokens. Sie stapeln mehrere Decoder-Schichten. Der Eingabe-Prompt wird durch die Schichten geleitet, und die letzte Schicht sagt die Wahrscheinlichkeitsverteilung über den Vokabular für den nächsten Token voraus. Durch autoregressives Sampling aus dieser Verteilung kann das Modell kohärenten und kontextuell relevanten Text generieren.

* **Encoder-Decoder-Modelle:** Diese Modelle nehmen eine Eingabesequenz und generieren eine Ausgabesequenz. Sie verwenden die vollständige Encoder-Decoder-Architektur. Der Encoder verarbeitet die Eingabe, und der Decoder verwendet die Ausgabe des Encoders, um die Zielsequenz zu generieren. Diese eignen sich gut für Aufgaben wie Übersetzung, Zusammenfassung und Fragebeantwortung.

**Die Bedeutung im Detail verstehen:**

Die Auswirkung der Transformer-Architektur auf LLMs ist tiefgreifend:

* **Verarbeitung langreichweitiger Abhängigkeiten:** Der Self-Attention-Mechanismus ermöglicht es dem Modell, Wörter direkt zu verbinden, die in der Sequenz weit voneinander entfernt sind, und überwindet so die Einschränkungen von RNNs bei der Erfassung von Kontext über lange Distanzen.
* **Parallele Verarbeitung:** Die parallele Verarbeitung der gesamten Sequenz reduziert die Trainingszeit erheblich und ermöglicht die Verwendung viel größerer Datensätze und Modelle.
* **Skalierbarkeit:** Die Transformer-Architektur skaliert gut mit zunehmender Daten- und Modellgröße, was zur Entwicklung extrem leistungsstarker LLMs mit Milliarden oder sogar Billionen von Parametern führt.
* **Kontextuelles Verständnis:** Der Attention-Mechanismus ermöglicht es dem Modell, den Kontext von Wörtern auf nuanciertere Weise zu verstehen, was zu einem besseren Sprachverständnis und besserer Sprachgenerierung führt.
* **Grundlage für Innovation:** Die Transformer-Architektur diente als Grundlage für zahlreiche Fortschritte und Variationen, die zur vielfältigen Landschaft moderner LLMs geführt haben.

Zusammenfassend lässt sich sagen, dass die Transformer-Architektur mit ihrem Kernmechanismus der Self-Attention, ihren Fähigkeiten zur parallelen Verarbeitung und ihrer Encoder-Decoder-Struktur (oder Decoder-only-Varianten) das Feld des NLP revolutioniert hat und die treibende Kraft hinter den bemerkenswerten Fähigkeiten moderner Large Language Models ist.