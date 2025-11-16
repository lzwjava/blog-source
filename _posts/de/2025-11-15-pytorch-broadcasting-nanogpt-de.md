---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Verstehen von PyTorch Broadcasting in NanoGPT
translated: true
type: note
---

Gute Frage! Das ist ein sehr häufiger Punkt der Verwirrung, wenn man sich den NanoGPT- oder GPT-2-Code zum ersten Mal ansieht.

Schauen wir uns die Formen genau an:

```python
tok_emb = self.transformer.wte(idx)    # Shape: (B, T, n_embd)
pos_emb = self.transformer.wpe(pos)    # Shape: (T, n_embd)   ← nur 1D!
```

Wie kann man `(B, T, n_embd)` + `(T, n_embd)` addieren?

**Antwort: PyTorch broadcasted die Positionsembedding automatisch über die Batch-Dimension.**

Wenn PyTorch sieht:
```python
tok_emb + pos_emb
```
behandelt es `pos_emb` (Form `(T, n_embd)`) so, als ob es `(1, T, n_embd)` wäre, und **broadcasted** es dann, um `(B, T, n_embd)` zu entsprechen.

Diese Addition wird also zu:
```
(B, T, n_embd)
     +
(1, T, n_embd)   ← automatisch durch Broadcasting hinzugefügt
     =
(B, T, n_embd)
```

Genau so funktioniert das ursprüngliche GPT-2 und alle modernen Transformer-Implementierungen — Positionsembedding werden über alle Sequenzen im Batch hinweg geteilt.

Sie können überprüfen, ob das in Python funktioniert:

```python
import torch
B, T, C = 2, 3, 768
tok_emb = torch.randn(B, T, C)
pos_emb = torch.randn(T, C)

result = tok_emb + pos_emb
print(result.shape)  # → torch.Size([2, 3, 768])
```

Kein Fehler, funktioniert einwandfrei.

In NanoGPT (und dem ursprünglichen GPT-2) ist diese Zeile also 100% korrekt und beabsichtigt:

```python
x = self.transformer.drop(tok_emb + pos_emb)
```

Sie verlässt sich auf PyTorchs Broadcasting — sauber, effizient und Standardpraxis.

`pos_emb.unsqueeze(0)` oder etwas anderes ist nicht nötig. Broadcasting erledigt die Aufgabe elegant.