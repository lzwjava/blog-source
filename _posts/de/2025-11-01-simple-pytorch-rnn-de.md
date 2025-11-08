---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Einfaches PyTorch-RNN-Beispiel
translated: true
type: note
---

### Einfaches RNN-Beispiel in PyTorch

Recurrent Neural Networks (RNNs) eignen sich hervorragend für die Verarbeitung sequenzieller Daten wie Zeitreihen oder Text. Hier ist ein grundlegendes Beispiel, das PyTorch verwendet, um ein einfaches RNN für die Klassifizierung von Sequenzen zu erstellen (z.B. binäre Klassifizierung von Zufallssequenzen). Dies setzt voraus, dass PyTorch installiert ist (`import torch` und `import torch.nn as nn`).

```python
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# Hyperparameter
input_size = 1      # Feature-Größe (z.B. univariate Zeitreihe)
hidden_size = 32    # Größe des Hidden State
output_size = 1     # Binäre Ausgabe (Sigmoid für Klassifizierung)
sequence_length = 10  # Länge jeder Sequenz
batch_size = 32
num_epochs = 10

# Generiere Dummy-Daten: Sequenzen der Länge 10, Labels basierend auf Summe (binär)
def generate_data(num_samples):
    X = torch.randn(num_samples, sequence_length, input_size)
    y = (torch.sum(X, dim=1) > 0).float().unsqueeze(1)
    return X, y

# Einfaches RNN-Modell
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleRNN, self).__init__()
        self.hidden_size = hidden_size
        self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
        self.sigmoid = nn.Sigmoid()
    
    def forward(self, x):
        # x shape: (batch, seq_len, input_size)
        h0 = torch.zeros(1, x.size(0), self.hidden_size)  # Initialer Hidden State
        out, _ = self.rnn(x, h0)
        # Nimm die letzte Ausgabe für die Klassifizierung
        out = self.fc(out[:, -1, :])  # Letzter Zeitschritt
        return self.sigmoid(out)

# Initialisiere Modell, Loss, Optimizer
model = SimpleRNN(input_size, hidden_size, output_size)
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Training Loop
num_samples = 1000
X, y = generate_data(num_samples)
dataset = torch.utils.data.TensorDataset(X, y)
dataloader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=True)

for epoch in range(num_epochs):
    for batch_X, batch_y in dataloader:
        optimizer.zero_grad()
        outputs = model(batch_X)
        loss = criterion(outputs, batch_y)
        loss.backward()
        optimizer.step()
    print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# Inferenz-Beispiel
test_seq = torch.randn(1, sequence_length, input_size)
prediction = model(test_seq)
print(f'Prediction: {prediction.item():.4f}')
```

#### So funktioniert es:
- **Daten-Generierung**: Erstellt Zufallssequenzen der Länge 10 mit einem binären Label (1 wenn Summe > 0, sonst 0).
- **Modell**: Verwendet `nn.RNN` (grundlegende RNN-Zelle). Der Forward-Pass verarbeitet die Sequenz schrittweise und verwendet den letzten Hidden State für die Ausgabe.
- **Training**: Standard PyTorch Loop mit BCE Loss für binäre Klassifizierung.
- **Ausgabe**: Die Sigmoid-Aktivierung ergibt eine Wahrscheinlichkeit zwischen 0 und 1.

Dies ist ein einfaches RNN; für eine bessere Performance bei langen Sequenzen sollten LSTM- oder GRU-Varianten in Betracht gezogen werden (z.B. ersetze `nn.RNN` mit `nn.LSTM`).

### LSTM-Variante (Schnelle Erweiterung)
Für das Problem der verschwindenden Gradienten, wechsle zu LSTM:

```python
# In der Modellklasse, ersetze:
self.rnn = nn.LSTM(input_size, hidden_size, batch_first=True)

# Und im Forward:
h0 = torch.zeros(1, x.size(0), self.hidden_size)
c0 = torch.zeros(1, x.size(0), self.hidden_size)  # LSTM benötigt Cell State
out, (hn, cn) = self.rnn(x, (h0, c0))
```

Führe dies in einer PyTorch-Umgebung aus, um zu experimentieren!

[PyTorch RNN Dokumentation](https://pytorch.org/docs/stable/generated/torch.nn.RNN.html)  
[PyTorch LSTM Dokumentation](https://pytorch.org/docs/stable/generated/torch.nn.LSTM.html)