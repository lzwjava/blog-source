---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: PyTorch-Parameter für lernbare Gewichte
translated: true
type: note
---

`torch.nn.Parameter` ist eine Unterklasse von `torch.Tensor` in PyTorch, die speziell dafür entwickelt wurde, lernbare Parameter in neuronalen Netzwerkmodulen zu repräsentieren. Ihr Hauptzweck ist es, Tensoren automatisch als Modulparameter zu registrieren, wenn sie als Attribute einem `torch.nn.Module` zugewiesen werden. Dadurch werden sie über Methoden wie `module.parameters()` oder `module.named_parameters()` zugänglich. Dies hilft dabei, trainierbare Gewichte (z.B. für Layer) von regulären Tensoren zu unterscheiden und verhindert, dass temporäre Berechnungen (wie zwischengespeicherte Zustände in RNNs) fälschlicherweise als Parameter behandelt werden.

### Wichtige Eigenschaften
- **Automatische Registrierung**: Wenn Sie einen `Parameter` einem Modul zuweisen (z.B. `self.weight = nn.Parameter(torch.randn(3, 3))` im `__init__` eines benutzerdefinierten Moduls), wird er ohne zusätzlichen Code zur Parameterliste des Moduls hinzugefügt.
- **Gradientenverfolgung**: Standardmäßig ist `requires_grad=True`, sodass er an der Backpropagation teilnimmt. Dies gilt auch innerhalb eines `torch.no_grad()`-Kontexts – für eine feinere Kontrolle verwenden Sie die lokale Deaktivierung von Autograd.
- **Attribute**: Er erbt alle Eigenschaften eines `Tensor`, fügt aber über sein spezielles Modulverhalten hinaus keine neuen hinzu.

### Grundlegende Verwendung
Hier ist ein einfaches Beispiel in einem benutzerdefinierten Modul:

```python
import torch
import torch.nn as nn

class MyModule(nn.Module):
    def __init__(self):
        super().__init__()
        # Dies wird automatisch als Parameter registriert
        self.weight = nn.Parameter(torch.randn(2, 3))
        # Ein einfacher Tensor wird nicht registriert
        self.bias = torch.zeros(3)

    def forward(self, x):
        return x @ self.weight + self.bias

model = MyModule()
print(list(model.parameters()))  # Ausgabe: [Parameter containing: tensor(...)]
```

Weitere Details finden Sie in der offiziellen Dokumentation: [Parameter — PyTorch 2.9 documentation](https://pytorch.org/docs/stable/generated/torch.nn.parameter.Parameter.html)