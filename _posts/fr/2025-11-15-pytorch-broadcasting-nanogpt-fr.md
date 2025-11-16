---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Comprendre le Broadcasting PyTorch dans NanoGPT
translated: true
type: note
---

Excellente question ! C'est un point de confusion très fréquent lorsqu'on découvre le code de NanoGPT ou de GPT-2.

Examinons attentivement les formes :

```python
tok_emb = self.transformer.wte(idx)    # Forme : (B, T, n_embd)
pos_emb = self.transformer.wpe(pos)    # Forme : (T, n_embd)   ← seulement 1D !
```

Comment peut-on additionner `(B, T, n_embd)` + `(T, n_embd)` ?

**Réponse : PyTorch diffuse automatiquement les embeddings de position sur la dimension du lot.**

Lorsque PyTorch voit :
```python
tok_emb + pos_emb
```
il traite `pos_emb` (forme `(T, n_embd)`) comme s'il s'agissait de `(1, T, n_embd)` et le **diffuse** pour correspondre à `(B, T, n_embd)`.

Cette addition devient donc :
```
(B, T, n_embd)
     + 
(1, T, n_embd)   ← ajouté automatiquement par diffusion
     =
(B, T, n_embd)
```

C'est exactement ainsi que fonctionnent le GPT-2 original et toutes les implémentations modernes de transformers — les embeddings de position sont partagés entre toutes les séquences du lot.

Vous pouvez vérifier que cela fonctionne en Python :

```python
import torch
B, T, C = 2, 3, 768
tok_emb = torch.randn(B, T, C)
pos_emb = torch.randn(T, C)

result = tok_emb + pos_emb
print(result.shape)  # → torch.Size([2, 3, 768])
```

Aucune erreur, cela fonctionne parfaitement.

Ainsi, dans NanoGPT (et le GPT-2 original), cette ligne est correcte à 100% et intentionnelle :

```python
x = self.transformer.drop(tok_emb + pos_emb)
```

Elle s'appuie sur la diffusion de PyTorch — propre, efficace et une pratique standard.

Aucun besoin de `pos_emb.unsqueeze(0)` ou autre chose. La diffusion fait le travail de manière élégante.