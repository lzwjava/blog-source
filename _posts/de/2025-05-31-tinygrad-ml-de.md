---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: TinyGrad Leichtgewichtige ML-Bibliothek
translated: true
type: note
---

### Einführung in TinyGrad
TinyGrad ist eine leichtgewichtige, minimalistische Machine Learning und Deep Learning Bibliothek in Python, die für Ausbildung und Einfachheit konzipiert ist. Sie implementiert automatische Differentiation (autograd) wie PyTorch, ist aber viel kleiner – etwa 1.000 Codezeilen. Sie eignet sich hervorragend zum Erlernen von ML-Konzepten oder zum Erstellen kleiner Modelle ohne den Overhead größerer Bibliotheken. Sie unterstützt Tensoren, neuronale Netze und grundlegende Operationen, einschließlich GPU-Beschleunigung über PyTorch oder Metal.

Das offizielle Repository finden Sie unter: [tinygrad GitHub](https://github.com/geohot/tinygrad). Hinweis: Es ist experimentell und nicht so robust wie PyTorch oder TensorFlow für den Produktionseinsatz.

### Installation
Installieren Sie TinyGrad via pip:

```bash
pip install tinygrad
```

Es hat minimale Abhängigkeiten, verwendet aber optional PyTorch für einige Backends. Für GPU-Unterstützung stellen Sie sicher, dass PyTorch installiert ist.

### Grundlegende Verwendung
Beginnen Sie mit dem Importieren und Setzen des Kontexts (TinyGrad erfordert die Angabe, ob Sie trainieren oder Inferenz durchführen, da Gradienten unterschiedlich berechnet werden).

#### Importieren und Kontext
```python
from tinygrad import Tensor
from tinygrad.nn import Linear, BatchNorm2d  # Für neuronale Netze

# Kontext setzen: Training (für Gradienten) oder Inferenz
Tensor.training = True  # Gradientenverfolgung aktivieren
```

#### Erstellen und Manipulieren von Tensoren
Tensoren sind die Kern-Datenstruktur, ähnlich wie NumPy-Arrays oder PyTorch-Tensoren.

```python
# Tensoren aus Listen, NumPy-Arrays oder durch Form erstellen
a = Tensor([1, 2, 3])          # Aus Liste
b = Tensor.zeros(3)            # Null-Tensor der Form (3,)
c = Tensor.rand(2, 3)          # Zufälliger Tensor der Form (2, 3)

# Grundlegende Operationen
d = a + b                      # Elementweise Addition
e = d * 2                      # Skalare Multiplikation
f = a @ Tensor([[1], [2], [3]])  # Matrixmultiplikation (a ist 1D, implizit transponiert)

print(e.numpy())               # Zur Ausgabe oder weiteren Verwendung in NumPy konvertieren
```

#### Automatische Differentiation (Backpropagation)
TinyGrad berechnet automatisch Gradienten mithilfe der Kettenregel.

```python
# Gradientenverfolgung aktivieren
Tensor.training = True

x = Tensor([1.0, 2.0, 3.0])
y = (x * 2).sum()             # Irgendeine Operation; y ist ein Skalar

y.backward()                  # Gradienten berechnen
print(x.grad.numpy())         # Gradienten bzgl. x: sollte [2, 2, 2] sein
```

Für den Export nach NumPy verwenden Sie `.numpy()` – Gradienten akkumulieren, sofern nicht zurückgesetzt.

#### Neuronale Netze und Training
TinyGrad enthält grundlegende Layer und Optimierer. Hier ein einfaches MLP-Beispiel:

```python
from tinygrad.nn import Linear, optim

# Ein einfaches Modell definieren (z.B. lineare Schicht)
model = Linear(3, 1)          # Input 3, Output 1

# Dummy-Daten
x = Tensor.rand(4, 3)         # Batch von 4 Samples, 3 Features
y_true = Tensor.rand(4, 1)    # Ziel

# Forward Pass
pred = model(x).sigmoid()      # Angenommen binäre Klassifikation

# Loss (z.B. MSE)
loss = ((pred - y_true) ** 2).mean()

# Backpropagation und Optimieren
loss.backward()
optim.Adam([model], lr=0.01).step()
```

Für Faltungsnetzwerke verwenden Sie `Conv2d` aus `tinygrad.nn`.

### Erweiterte Funktionen
- **Loss-Funktionen und Aktivierungen**: Verfügbar in `tinygrad.nn` (z.B. `sigmoid`, `relu`, `cross_entropy`).
- **Optimierer**: `SGD`, `Adam` in `tinygrad.nn.optim`.
- **Layer**: `Linear`, `Conv2d`, `BatchNorm`, etc.
- **Speichern/Laden**: Modelle können als Zustandswörterbücher gespeichert werden (ähnlich wie bei PyTorch).
- **GPU/Beschleunigung**: TinyGrad kann über das PyTorch-Backend auf der GPU laufen: `TESOR_SET_DEVICE='cuda:0'`. Es unterstützt auch Metal auf macOS.
- **Vision/Denoising-Beispiele**: Das Repo enthält Beispiele wie das Training eines ResNet auf MNIST.

Vollständige Beispiele finden Sie im Ordner `examples/` im GitHub-Repo, wie z.B. Bildklassifizierung oder Reinforcement Learning.

### Beispiel: Training eines neuronalen Netzes
Hier ein vollständiges, einfaches Skript zum Training eines Netzes für XOR:

```python
from tinygrad import Tensor
from tinygrad.nn import Linear, optim

# Daten
X = Tensor([[0,0], [0,1], [1,0], [1,1]])
Y = Tensor([[0], [1], [1], [0]])

# Modell
model = Linear(2, 1)
opt = optim.Adam([model], lr=0.1)

Tensor.training = True

for epoch in range(1000):
    pred = model(X).sigmoid()
    loss = ((pred - Y) ** 2).mean()
    loss.backward()
    opt.step()
    opt.zero_grad()

# Test
print(model(Tensor([[0,0]])))  # Sollte ~0 sein
```

### Tipps und Hinweise
- **Moduswechsel**: Setzen Sie `Tensor.training = True` für das Training; wechseln Sie zu `False` für die Inferenz, um die Gradientenberechnung zu vermeiden.
- **Formbehandlung**: Tensoren folgen NumPy-ähnlichem Broadcasting, achten Sie aber auf Überläufe in kleinen Modellen.
- **Debugging**: Verwenden Sie `.numpy()`, um Werte zu überprüfen. Wenn etwas fehlschlägt, prüfen Sie auf Forminkonsistenzen.
- **Leistung**: Es ist langsam für große Modelle – verwenden Sie PyTorch für die Produktion.
- **Updates**: TinyGrad entwickelt sich schnell weiter; prüfen Sie das Repo auf die neueste Version.

Weitere Details finden Sie in der [docs/README.md](https://github.com/geohot/tinygrad/blob/master/README.md) oder führen Sie Beispiele lokal aus. Wenn Sie einen spezifischen Anwendungsfall haben, geben Sie weitere Details für maßgeschneiderte Ratschläge an!