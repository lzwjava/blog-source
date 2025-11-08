---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: GradScaler für Mixed-Precision-Training
translated: true
type: note
---

`torch.cuda.amp.GradScaler` ist eine PyTorch-Hilfsklasse, die entwickelt wurde, um **Gradienten automatisch zu skalieren** während des Mixed-Precision-Trainings mit **Automatic Mixed Precision (AMP)**. Sie hilft, Underflow in Gradienten zu verhindern, wenn `float16` (Halbgenauigkeit) Tensoren verwendet werden, die sonst zu klein für eine genaue Darstellung werden könnten.

---

### Warum `GradScaler` verwenden?

Im Mixed-Precision-Training:
- **Forward/Backward Passes** verwenden `float16` für Geschwindigkeit und Speicherersparnis.
- In `float16` berechnete **Gradienten** können sehr klein werden → **Underflow zu Null**.
- `GradScaler` skaliert den **Loss** um einen Faktor (z.B. 2¹⁵ = 32768) vor dem Backward Pass.
- Gradienten werden proportional skaliert → bleiben im darstellbaren Bereich.
- Vor dem Optimizer Step werden die Gradienten wieder **zurück skaliert** auf den Normalwert.

---

### Grundlegende Verwendung

```python
import torch
from torch.cuda.amp import autocast, GradScaler

model = MyModel().cuda()
optimizer = torch.optim.Adam(model.parameters())
scaler = GradScaler()  # Default init_scale=2**16

for data, target in dataloader:
    optimizer.zero_grad()

    # 1. Autocast für Forward
    with autocast():
        output = model(data)
        loss = loss_fn(output, target)

    # 2. Loss skalieren und Backward
    scaler.scale(loss).backward()

    # 3. Zurückskalieren + Optimizer Step
    scaler.step(optimizer)

    # 4. Skalierungsfaktor für nächste Iteration aktualisieren
    scaler.update()
```

---

### Wichtige Methoden

| Methode | Zweck |
|-------|--------|
| `scaler.scale(loss)` | Skaliert den Loss vor `.backward()` |
| `scaler.step(optimizer)` | Skaliert Gradienten zurück und ruft `optimizer.step()` auf |
| `scaler.update()` | Passt den Skalierungsfaktor für die nächste Iteration an |
| `scaler.unscale_(optimizer)` | Skaliert Gradienten manuell zurück (selten benötigt) |
| `scaler.get_scale()` | Gibt den aktuellen Skalierungsfaktor zurück |

---

### Wie Skalierung funktioniert (Intern)

1. **Initialer Skalierungsfaktor**: Normalerweise `2**16 = 65536`
2. Nach `backward()` wird auf **inf/NaN** in den Gradienten geprüft.
3. Wenn **keine inf/NaN** → Skalierungsfaktor kann **erhöht** werden (z.B. ×2) beim nächsten Mal.
4. Wenn **inf/NaN gefunden** → `optimizer.step()` überspringen, **Skalierungsfaktor verringern** (z.B. ÷2) und später wiederholen.

Dies macht das Training **robust** gegenüber gelegentlichem Overflow.

---

### Häufige Parameter

```python
scaler = GradScaler(
    init_scale=2.**16,     # Startskalierung
    growth_factor=2.0,     # Multiplizieren bei keinem inf
    backoff_factor=0.5,    # Teilen bei inf
    growth_interval=2000,  # Schritte vor Skalierungsvergrößerung
    enabled=True
)
```

---

### Beispiel mit Gradient Clipping

```python
scaler.scale(loss).backward()
scaler.unscale_(optimizer)  # Muss vor Clipping zurück skaliert werden
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
scaler.step(optimizer)
scaler.update()
```

> **Hinweis**: Immer `unscale_` **vor** Clipping oder Inspektion von Gradienten aufrufen.

---

### Best Practices

- Verwenden mit `torch.cuda.amp.autocast()`
- Nur **Forward + Loss** in `autocast()` wrappen
- `scaler.update()` **jede Iteration** aufrufen
- `torch.backends.cuda.matmul.allow_fp16_reduced_precision_reduction=True` für Geschwindigkeit verwenden

---

### Wann nicht zu verwenden

- Reines `float32` Training
- CPU Training
- Benutzerdefinierte Training Loops, die Skalierung manuell handhaben

---

### Offizielle Dokumentation

[https://pytorch.org/docs/stable/amp.html#torch.cuda.amp.GradScaler](https://pytorch.org/docs/stable/amp.html#torch.cuda.amp.GradScaler)

---

Lass mich wissen, wenn du ein vollständiges Trainingsloop-Beispiel oder einen Vergleich mit manueller Skalierung möchtest!