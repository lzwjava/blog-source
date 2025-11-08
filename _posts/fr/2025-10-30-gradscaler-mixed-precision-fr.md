---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: GradScaler pour l'Entraînement en Précision Mixte
translated: true
type: note
---

`torch.cuda.amp.GradScaler` est une classe utilitaire PyTorch conçue pour **mettre automatiquement à l'échelle les gradients** pendant l'entraînement en précision mixte utilisant **Automatic Mixed Precision (AMP)**. Elle aide à prévenir le sous-dépassement des gradients lors de l'utilisation de tenseurs `float16` (demi-précision), qui pourraient autrement devenir trop petits pour être représentés avec précision.

---

### Pourquoi utiliser `GradScaler` ?

Dans l'entraînement en précision mixte :
- **Les passes avant/arrière** utilisent `float16` pour la vitesse et les économies de mémoire.
- Les **gradients** calculés en `float16` peuvent devenir très petits → **sous-dépassement vers zéro**.
- `GradScaler` met à l'échelle la **perte** par un facteur (par exemple, 2¹⁵ = 32768) avant la passe arrière.
- Les gradients sont mis à l'échelle proportionnellement → restent dans une plage représentable.
- Avant l'étape de l'optimiseur, les gradients sont **remis à l'échelle normale**.

---

### Utilisation de base

```python
import torch
from torch.cuda.amp import autocast, GradScaler

model = MyModel().cuda()
optimizer = torch.optim.Adam(model.parameters())
scaler = GradScaler()  # Initialisation par défaut init_scale=2**16

for data, target in dataloader:
    optimizer.zero_grad()

    # 1. Autocast pour la passe avant
    with autocast():
        output = model(data)
        loss = loss_fn(output, target)

    # 2. Mettre à l'échelle la perte et passe arrière
    scaler.scale(loss).backward()

    # 3. Rétablir l'échelle + étape de l'optimiseur
    scaler.step(optimizer)

    # 4. Mettre à jour le facteur d'échelle pour la prochaine itération
    scaler.update()
```

---

### Méthodes principales

| Méthode | Objectif |
|-------|--------|
| `scaler.scale(loss)` | Met à l'échelle la perte avant `.backward()` |
| `scaler.step(optimizer)` | Rétablit l'échelle des grads et appelle `optimizer.step()` |
| `scaler.update()` | Ajuste le facteur d'échelle pour la prochaine itération |
| `scaler.unscale_(optimizer)` | Rétablit manuellement l'échelle des grads (rarement nécessaire) |
| `scaler.get_scale()` | Renvoie le facteur d'échelle actuel |

---

### Fonctionnement de la mise à l'échelle (en interne)

1. **Échelle initiale** : Généralement `2**16 = 65536`
2. Après `backward()`, vérifie la présence de **inf/NaN** dans les gradients.
3. Si **pas de inf/NaN** → l'échelle peut **augmenter** (par exemple, ×2) la prochaine fois.
4. Si **inf/NaN détecté** → ignore `optimizer.step()`, **diminue l'échelle** (par exemple, ÷2), et réessaie plus tard.

Cela rend l'entraînement **robuste** aux dépassements occasionnels.

---

### Paramètres courants

```python
scaler = GradScaler(
    init_scale=2.**16,     # Échelle de départ
    growth_factor=2.0,     # Multiplie en l'absence de inf
    backoff_factor=0.5,    # Divise en présence de inf
    growth_interval=2000,  # Pas avant d'augmenter l'échelle
    enabled=True
)
```

---

### Exemple avec écrêtage des gradients

```python
scaler.scale(loss).backward()
scaler.unscale_(optimizer)  # Nécessaire de rétablir l'échelle avant l'écrêtage
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
scaler.step(optimizer)
scaler.update()
```

> **Note** : Toujours utiliser `unscale_` **avant** l'écrêtage ou l'inspection des gradients.

---

### Bonnes pratiques

- À utiliser avec `torch.cuda.amp.autocast()`
- Inclure **uniquement la passe avant + la perte** dans `autocast()`
- Appeler `scaler.update()` **à chaque itération**
- Utiliser `torch.backends.cuda.matmul.allow_fp16_reduced_precision_reduction=True` pour la vitesse

---

### Quand ne pas l'utiliser

- Entraînement en pur `float32`
- Entraînement sur CPU
- Boucles d'entraînement personnalisées qui gèrent manuellement la mise à l'échelle

---

### Documentation officielle

[https://pytorch.org/docs/stable/amp.html#torch.cuda.amp.GradScaler](https://pytorch.org/docs/stable/amp.html#torch.cuda.amp.GradScaler)

---

Faites-moi savoir si vous voulez un exemple complet de boucle d'entraînement ou une comparaison avec la mise à l'échelle manuelle !