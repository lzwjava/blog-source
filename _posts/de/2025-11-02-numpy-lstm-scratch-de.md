---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: NumPy LSTM-Implementierung von Grund auf
translated: true
type: note
---

Dies ist eine grundlegende Implementierung eines Long Short-Term Memory (LSTM) Netzwerks, das nur NumPy verwendet, inspiriert von den Konzepten in Christopher Olahs Blogbeitrag "Understanding LSTM Networks". Es enthält die zentralen Gatter (Vergessens-, Eingangs-, Kandidaten-Zellen- und Ausgangsgatter) und konzentriert sich auf den Vorwärtsdurchlauf. Die Klasse verarbeitet einen einzelnen Zeitschritt via `forward()` und eine gesamte Sequenz via `forward_sequence()`.

Gewichte werden zufällig initialisiert (in der Praxis sollten bessere Initialisierungen wie Xavier/Glorot verwendet werden). Kein Rückwärtsdurchlauf oder Training ist hier enthalten – erweitern Sie dies mit Backpropagation Through Time (BPTT) dafür.

```python
import numpy as np

class LSTM:
    def __init__(self, input_size, hidden_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        # Initialisiere Gewichte und Biases für Vergessens-, Eingangs-, Zellen- und Ausgangsgatter
        self.Wf = np.random.randn(hidden_size, hidden_size + input_size)
        self.Wi = np.random.randn(hidden_size, hidden_size + input_size)
        self.WC = np.random.randn(hidden_size, hidden_size + input_size)
        self.Wo = np.random.randn(hidden_size, hidden_size + input_size)
        self.bf = np.zeros((hidden_size, 1))
        self.bi = np.zeros((hidden_size, 1))
        self.bC = np.zeros((hidden_size, 1))
        self.bo = np.zeros((hidden_size, 1))

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def tanh(self, z):
        return np.tanh(z)

    def forward(self, x, h_prev, C_prev):
        # x: (input_size, 1), h_prev und C_prev: (hidden_size, 1)
        # Verkette verborgenen Zustand und Eingabe
        concat = np.vstack((h_prev, x))
        # Vergessensgatter
        f_t = self.sigmoid(np.dot(self.Wf, concat) + self.bf)
        # Eingangsgatter
        i_t = self.sigmoid(np.dot(self.Wi, concat) + self.bi)
        C_tilda = self.tanh(np.dot(self.WC, concat) + self.bC)
        # Zellzustandsaktualisierung
        C_t = f_t * C_prev + i_t * C_tilda
        # Ausgangsgatter
        o_t = self.sigmoid(np.dot(self.Wo, concat) + self.bo)
        # Aktualisierung des verborgenen Zustands
        h_t = o_t * self.tanh(C_t)
        return h_t, C_t

    def forward_sequence(self, X):
        # X: (seq_len, input_size)
        h = np.zeros((self.hidden_size, 1))
        C = np.zeros((self.hidden_size, 1))
        outputs = []
        for x in X:
            h, C = self.forward(x.reshape(-1, 1), h, C)
            outputs.append(h)
        return np.hstack(outputs).T  # Gibt (seq_len, hidden_size) zurück

# Beispielverwendung
input_size = 3
hidden_size = 5
lstm = LSTM(input_size, hidden_size)

# Einzelschritt
x_t = np.random.randn(input_size, 1)
h_prev = np.zeros((hidden_size, 1))
C_prev = np.zeros((hidden_size, 1))
h_t, C_t = lstm.forward(x_t, h_prev, C_prev)
print("Einzelschritt - Form des verborgenen Zustands:", h_t.shape)

# Sequenz
X = np.random.randn(4, input_size)  # seq_len=4
outputs = lstm.forward_sequence(X)
print("Sequenzausgaben Form:", outputs.shape)
```

### Kurze Erklärung
- **Initialisierung**: Gewichte verbinden die verkettete Eingabe (vorheriger verborgenen Zustand + aktuelle Eingabe) mit jedem Gatter. Biases sind mit Null initialisiert.
- **Gatter**:
  - **Vergessensgatter** (`f_t`): Entscheidet, was vom vorherigen Zellzustand vergessen werden soll (Sigmoid: 0-1).
  - **Eingangsgatter** (`i_t`) und **Kandidaten-Zelle** (`C_tilda`): Entscheiden, welche neuen Informationen hinzugefügt werden sollen (Sigmoid + Tanh).
  - **Ausgangsgatter** (`o_t`): Filtert den Zellzustand, um den verborgenen Zustand zu erzeugen (Sigmoid + Tanh auf Zelle).
- **Zellzustand** (`C_t`): Linearer Fluss mit additiven Aktualisierungen für das Langzeitgedächtnis.
- **Verwendung**: Für Sequenzen, Schleife über Zeitschritte, die verborgenen und Zellzustände werden fortschreitend aktualisiert.

Dies entspricht der LSTM-Architektur aus Colahs Blog: Zellzustand als "Datenautobahn", gesteuert durch Gatter.

[Understanding LSTMs: Implementation from Scratch](https://medium.com/@samina.amin/understanding-lstms-lstm-implementation-from-scratch-18965a150eca)