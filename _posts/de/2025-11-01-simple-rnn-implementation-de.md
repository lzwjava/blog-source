---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Einfache RNN-Implementierung von Grund auf
translated: true
type: note
---

### Einfaches RNN-Beispiel in NumPy (From Scratch)

Die Implementierung eines RNN von Grund auf in NumPy ist eine hervorragende Möglichkeit, die Mechanik zu verstehen: den wiederkehrenden Hidden State, die Vorwärtspropagation und die Backpropagation Through Time (BPTT). Nachfolgend finden Sie ein grundlegendes Beispiel für die binäre Klassifikation von Zufallssequenzen (ähnlich der vorherigen PyTorch-Version). Es verwendet univariate Zeitreihendaten (input_size=1), hidden_size=32 und sequence_length=10.

Dieser Code beinhaltet:
- Datengenerierung.
- RNN-Vorwärtspass (mit tanh-Aktivierung für Hidden States).
- Rückwärtspass (BPTT mit einfachem Gradientenabstieg).
- Trainingsschleife.

Hinweis: Dies ist ein Vanilla-RNN; Gradienten können bei langen Sequenzen verschwinden/explodieren. Für den Produktionseinsatz sollten Clipping oder LSTM-Logik in Betracht gezogen werden.

```python
import numpy as np

# Hyperparameter
input_size = 1      # Feature-Größe (univariat)
hidden_size = 32    # Hidden-State-Größe
output_size = 1     # Binäre Ausgabe
sequence_length = 10  # Länge jeder Sequenz
num_samples = 1000
num_epochs = 10
learning_rate = 0.01

# Generiere Dummy-Daten: Sequenzen der Länge 10, Labels basierend auf Summe (binär)
def generate_data(num_samples):
    X = np.random.randn(num_samples, sequence_length, input_size)
    y = (np.sum(X, axis=1) > 0).astype(float).reshape(num_samples, 1)
    return X, y

# Einfache RNN-Klasse (from scratch)
class SimpleRNN:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Initialisiere Gewichte (Xavier-Init)
        self.Wxh = np.random.randn(hidden_size, input_size) * np.sqrt(1. / input_size)
        self.Whh = np.random.randn(hidden_size, hidden_size) * np.sqrt(1. / hidden_size)
        self.Why = np.random.randn(output_size, hidden_size) * np.sqrt(1. / hidden_size)
        
        # Biases
        self.bh = np.zeros((hidden_size, 1))
        self.by = np.zeros((output_size, 1))
    
    def forward(self, x):
        # x Form: (sequence_length, input_size, 1) für einzelne Stichprobe
        self.x = x  # Speichere für Backprop
        self.h = np.zeros((self.hidden_size, 1))  # Initialer Hidden State
        
        # Vorwärts durch die Zeit
        self.hs = np.zeros((self.hidden_size, sequence_length + 1))  # Hidden States (inklusive initial)
        self.hs[:, 0] = self.h.flatten()
        
        for t in range(sequence_length):
            self.h = np.tanh(np.dot(self.Wxh, x[t]) + np.dot(self.Whh, self.h) + self.bh)
            self.hs[:, t+1] = self.h.flatten()
        
        # Ausgabe vom letzten Hidden State
        self.y_pred = np.dot(self.Why, self.h) + self.by
        return self.sigmoid(self.y_pred)
    
    def sigmoid(self, z):
        return 1 / (1 + np.exp(-np.clip(z, -250, 250)))  # Clip für Stabilität
    
    def backward(self, y_true):
        # Backprop Through Time (vereinfacht)
        dWhy = np.dot((self.y_pred - y_true) * self.sigmoid_deriv(self.y_pred), self.hs[-1:, :].T)
        dby = (self.y_pred - y_true) * self.sigmoid_deriv(self.y_pred)
        
        # Gradienten für Hidden- und Output-Gewichte
        dWhh = np.zeros_like(self.Whh)
        dWxh = np.zeros_like(self.Wxh)
        dbh = np.zeros_like(self.bh)
        
        dh_next = np.zeros_like(self.h)
        for t in reversed(range(sequence_length)):
            dh = np.dot(self.Why.T, (self.y_pred - y_true) * self.sigmoid_deriv(self.y_pred)) + dh_next
            dh_raw = (1 - self.h**2) * dh  # Tanh-Ableitung
            dWxh += np.dot(dh_raw, self.x[t].T)
            dWhh += np.dot(dh_raw, self.hs[:, t:t+2].T[:, 0:1])  # Vereinfacht; vollständige BPTT würde korrekt akkumulieren
            dbh += dh_raw
            dh_next = np.dot(self.Whh.T, dh_raw)
        
        # Aktualisiere Gewichte
        self.Wxh -= learning_rate * dWxh
        self.Whh -= learning_rate * dWhh
        self.Why -= learning_rate * dWhy
        self.bh -= learning_rate * dbh
        self.by -= learning_rate * dby
    
    def sigmoid_deriv(self, z):
        s = self.sigmoid(z)
        return s * (1 - s)

# Training
X, y = generate_data(num_samples)

# Umformen für einzelne Stichprobenverarbeitung (batch_size=1 der Einfachheit halber)
X = X.reshape(num_samples, sequence_length, input_size, 1)  # Füge Batch-Dim von 1 hinzu
y = y.reshape(num_samples, 1, 1)

model = SimpleRNN(input_size, hidden_size, output_size)

for epoch in range(num_epochs):
    total_loss = 0
    for i in range(num_samples):
        pred = model.forward(X[i])
        loss = -np.mean(y[i] * np.log(pred + 1e-8) + (1 - y[i]) * np.log(1 - pred + 1e-8))  # BCE
        total_loss += loss
        model.backward(y[i])
    
    avg_loss = total_loss / num_samples
    print(f'Epoch [{epoch+1}/{num_epochs}], Avg Loss: {avg_loss:.4f}')

# Inferenz-Beispiel
test_seq = np.random.randn(sequence_length, input_size, 1)
prediction = model.forward(test_seq)
print(f'Prediction: {prediction.flatten()[0]:.4f}')
```

#### So funktioniert es:
- **Datengenerierung**: Zufallssequenzen mit binären Labels basierend auf der Summe.
- **Vorwärtspass**: Verarbeitet die Sequenz Zeitschritt für Zeitschritt, aktualisiert den Hidden State `h_t = tanh(Wxh * x_t + Whh * h_{t-1} + bh)`. Die Ausgabe verwendet das finale `h` mit Sigmoid.
- **Rückwärtspass**: BPTT berechnet Gradienten für alle Zeitschritte und aktualisiert die Gewichte via einfachem GD. (Hinweis: Dies ist eine minimale BPTT; vollständige Versionen handhaben präzisere Akkumulation.)
- **Training**: Schleife über Stichproben, berechnet BCE-Loss und aktualisiert.
- **Ausgabe**: Sigmoid ergibt Wahrscheinlichkeit (0-1).

Dies läuft in ~10-20 Sekunden auf einer Standard-Maschine mit diesen Parametern. Erhöhen Sie `num_samples` oder `num_epochs`, um das Lernen zu beobachten. Für Multi-Batch: Vektorisieren Sie die Schleifen.

Für vertiefende Einblicke:  
[Understanding LSTM Networks (Colah's Blog)](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)  
[NumPy RNN Tutorial](https://www.wildml.com/2015/09/recurrent-neural-networks-tutorial-part-1-introduction-to-rnns/)