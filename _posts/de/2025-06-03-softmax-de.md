---
audio: false
generated: true
lang: de
layout: post
title: Softmax-Funktion im Deep Learning
translated: true
type: note
---

### Was ist Softmax?

Die **Softmax-Funktion** ist eine mathematische Funktion, die im maschinellen Lernen, insbesondere im Deep Learning, verwendet wird, um einen Vektor von Rohwerten (oft als Logits bezeichnet) in eine Wahrscheinlichkeitsverteilung umzuwandeln. Sie stellt sicher, dass die Ausgabewerte positiv sind und sich zu 1 summieren, was sie als Wahrscheinlichkeiten interpretierbar macht.

Die Softmax-Funktion ist für einen Vektor \\( z = [z_1, z_2, \dots, z_n] \\) wie folgt definiert:

\\[
\text{Softmax}(z_i) = \frac{e^{z_i}}{\sum_{j=1}^n e^{z_j}}
\\]

Wobei:
- \\( z_i \\): Der Eingabewert (Logit) für die \\( i \\)-te Klasse.
- \\( e^{z_i} \\): Die Exponentialfunktion des Eingabewerts, die Positivität sicherstellt.
- \\( \sum_{j=1}^n e^{z_j} \\): Die Summe der Exponentialfunktionen aller Eingabewerte, verwendet für die Normalisierung.
- Die Ausgabe \\( \text{Softmax}(z_i) \\) stellt die Wahrscheinlichkeit der \\( i \\)-ten Klasse dar.

Wichtige Eigenschaften:
- **Ausgabebereich**: Jeder Ausgabewert liegt zwischen 0 und 1.
- **Summe zu 1**: Die Summe aller Ausgabewerte ergibt 1, was sie zu einer gültigen Wahrscheinlichkeitsverteilung macht.
- **Verstärkt Unterschiede**: Die Exponentialfunktion in Softmax betont größere Eingabewerte, was die Ausgabewahrscheinlichkeiten für größere Logits entschiedener macht.

### Wie Softmax im Deep Learning angewendet wird

Die Softmax-Funktion wird häufig in der **Ausgabeschicht** von neuronalen Netzen für **Multi-Class-Klassifikationsaufgaben** verwendet. So wird sie angewendet:

1. **Kontext in neuronalen Netzen**:
   - In einem neuronalen Netz erzeugt die letzte Schicht oft Rohwerte (Logits) für jede Klasse. Zum Beispiel könnte das Netzwerk in einem Klassifikationsproblem mit 3 Klassen (z.B. Katze, Hund, Vogel) Logits wie \\([2.0, 1.0, 0.5]\\) ausgeben.
   - Diese Logits sind nicht direkt als Wahrscheinlichkeiten interpretierbar, da sie negativ, unbeschränkt sein können und sich nicht zu 1 summieren.

2. **Rolle von Softmax**:
   - Die Softmax-Funktion wandelt diese Logits in Wahrscheinlichkeiten um. Für das obige Beispiel:
     \\[
     \text{Softmax}([2.0, 1.0, 0.5]) = \left[ \frac{e^{2.0}}{e^{2.0} + e^{1.0} + e^{0.5}}, \frac{e^{1.0}}{e^{2.0} + e^{1.0} + e^{0.5}}, \frac{e^{0.5}}{e^{2.0} + e^{1.0} + e^{0.5}} \right]
     \\]
     Dies könnte zu Wahrscheinlichkeiten wie \\([0.665, 0.245, 0.090]\\) führen, was eine 66,5%ige Chance für Klasse 1 (Katze), 24,5% für Klasse 2 (Hund) und 9,0% für Klasse 3 (Vogel) anzeigt.

3. **Anwendungen**:
   - **Multi-Class-Klassifikation**: Softmax wird in Aufgaben wie Bildklassifikation (z.B. Erkennen von Objekten in Bildern), Natural Language Processing (z.B. Sentiment-Analyse mit mehreren Kategorien) oder jedem Problem verwendet, bei dem eine Eingabe einer von mehreren Klassen zugeordnet werden muss.
   - **Verlustberechnung**: Softmax wird typischerweise mit der **Cross-Entropy-Loss**-Funktion kombiniert, die die Differenz zwischen der vorhergesagten Wahrscheinlichkeitsverteilung und der wahren Verteilung (One-Hot-kodierte Labels) misst. Dieser Verlust leitet das Training des neuronalen Netzes.
   - **Entscheidungsfindung**: Die Ausgabewahrscheinlichkeiten können verwendet werden, um die wahrscheinlichste Klasse auszuwählen (z.B. durch Nehmen der Klasse mit der höchsten Wahrscheinlichkeit).

4. **Beispiele im Deep Learning**:
   - **Bildklassifikation**: In einem Convolutional Neural Network (CNN) wie ResNet erzeugt die letzte Fully-Connected-Schicht Logits für jede Klasse (z.B. 1000 Klassen in ImageNet). Softmax wandelt diese in Wahrscheinlichkeiten um, um das Objekt in einem Bild vorherzusagen.
   - **Natural Language Processing**: In Modellen wie Transformern (z.B. BERT) wird Softmax in der Ausgabeschicht für Aufgaben wie Textklassifikation oder Next-Word-Prediction verwendet, bei denen Wahrscheinlichkeiten über einem Vokabular oder einer Menge von Klassen benötigt werden.
   - **Reinforcement Learning**: Softmax kann verwendet werden, um Aktionsbewertungen in Wahrscheinlichkeiten für die Auswahl von Aktionen in einer policy-basierten Methode umzuwandeln.

5. **Implementierung in Frameworks**:
   - In Frameworks wie **PyTorch** oder **TensorFlow** ist Softmax oft als eingebaute Funktion implementiert:
     - PyTorch: `torch.nn.Softmax(dim=1)` oder `torch.nn.functional.softmax()`
     - TensorFlow: `tf.nn.softmax()`
   - Viele Frameworks kombinieren Softmax mit Cross-Entropy-Loss in einer einzigen Operation (z.B. `torch.nn.CrossEntropyLoss` in PyTorch) für numerische Stabilität, da die separate Berechnung von Softmax zu Problemen wie Überlauf bei großen Logits führen kann.

### Praktische Überlegungen
- **Numerische Stabilität**: Die direkte Berechnung von Softmax kann aufgrund der Exponentialfunktion zu einem Überlauf führen. Ein üblicher Trick ist, den maximalen Logit-Wert von allen Logits zu subtrahieren (\\( z_i - \max(z) \\)), bevor Softmax angewendet wird. Dies ändert die Ausgabe nicht, verhindert aber große Exponentialwerte.
- **Softmax vs. Sigmoid**: Für **binäre Klassifikation** wird oft die Sigmoid-Funktion anstelle von Softmax verwendet, da sie zwei Klassen effizienter handhabt. Softmax verallgemeinert Sigmoid auf mehrere Klassen.
- **Einschränkungen**:
  - Softmax geht von gegenseitigem Ausschluss (eine korrekte Klasse) aus. Für Multi-Label-Klassifikation (bei der mehrere Klassen wahr sein können) wird Sigmoid bevorzugt.
  - Softmax kann aufgrund der Exponentialfunktion in Vorhersagen übermäßig zuversichtlich sein, was kleine Unterschiede in den Logits verstärken kann.

### Beispielberechnung
Angenommen, ein neuronales Netz gibt die Logits \\([1.5, 0.8, -0.2]\\) für ein 3-Klassen-Problem aus:
1. Berechne Exponentialwerte: \\( e^{1.5} \approx 4.482, e^{0.8} \approx 2.225, e^{-0.2} \approx 0.819 \\).
2. Summiere die Exponentialwerte: \\( 4.482 + 2.225 + 0.819 = 7.526 \\).
3. Berechne Wahrscheinlichkeiten:
   - Klasse 1: \\( \frac{4.482}{7.526} \approx 0.596 \\)
   - Klasse 2: \\( \frac{2.225}{7.526} \approx 0.296 \\)
   - Klasse 3: \\( \frac{0.819}{7.526} \approx 0.109 \\)
4. Ausgabe: \\([0.596, 0.296, 0.109]\\), eine gültige Wahrscheinlichkeitsverteilung.

### Visualisierung von Softmax
Um zu veranschaulichen, wie Softmax Logits in Wahrscheinlichkeiten umwandelt, betrachten Sie das folgende Diagramm, das Logits und ihre entsprechenden Softmax-Wahrscheinlichkeiten zeigt:

```chartjs
{
  "type": "bar",
  "data": {
    "labels": ["Klasse 1", "Klasse 2", "Klasse 3"],
    "datasets": [
      {
        "label": "Logits",
        "data": [1.5, 0.8, -0.2],
        "backgroundColor": "rgba(75, 192, 192, 0.6)",
        "borderColor": "rgba(75, 192, 192, 1)",
        "borderWidth": 1
      },
      {
        "label": "Softmax-Wahrscheinlichkeiten",
        "data": [0.596, 0.296, 0.109],
        "backgroundColor": "rgba(255, 99, 132, 0.6)",
        "borderColor": "rgba(255, 99, 132, 1)",
        "borderWidth": 1
      }
    ]
  },
  "options": {
    "scales": {
      "y": {
        "beginAtZero": true,
        "title": {
          "display": true,
          "text": "Wert"
        }
      },
      "x": {
        "title": {
          "display": true,
          "text": "Klassen"
        }
      }
    },
    "plugins": {
      "legend": {
        "display": true
      },
      "title": {
        "display": true,
        "text": "Logits vs. Softmax-Wahrscheinlichkeiten"
      }
    }
  }
}
```

Dieses Diagramm vergleicht die rohen Logits mit den Wahrscheinlichkeiten nach Anwendung von Softmax und hebt hervor, wie Softmax die Werte in eine Wahrscheinlichkeitsverteilung normalisiert.

### Zusammenfassung
Die Softmax-Funktion ist ein Grundpfeiler der Multi-Class-Klassifikation im Deep Learning und wandelt Rohwerte in eine Wahrscheinlichkeitsverteilung um. Sie wird weitgehend in den Ausgabeschichten neuronaler Netze für Aufgaben wie Bild- und Textklassifikation verwendet, ermöglicht es Modellen, Wahrscheinlichkeiten mehreren Klassen zuzuordnen und erleichtert das Training mit Verlustfunktionen wie Cross-Entropy. Ihre exponentielle Natur macht sie empfindlich für Unterschiede in Logits, und eine sorgfältige Implementierung stellt numerische Stabilität sicher.