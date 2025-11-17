---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Pénalité L2 dans l'Entraînement des Modèles GPT
translated: true
type: note
---

La décroissance de poids (weight decay) est une technique de régularisation couramment utilisée lors de l'entraînement des modèles GPT (et de presque tous les grands modèles de langage) pour éviter le surapprentissage et améliorer la généralisation.

### Ce qu'elle fait réellement
La décroissance de poids ajoute un terme de pénalité à la fonction de perte qui pousse les poids du modèle vers des valeurs plus petites. Mathématiquement, si votre perte originale est ℒ (par exemple, l'entropie croisée), avec la décroissance de poids, vous optimisez :

ℒ_total = ℒ + (λ / 2) × ||w||²

où :
- w sont les paramètres du modèle (les poids)
- ||w||² est la norme L2 au carré des poids
- λ (lambda) est le coefficient de décroissance de poids (typiquement 0.01 ~ 0.1 dans l'entraînement de style GPT)

Ce terme supplémentaire décourage le modèle d'apprendre des poids très grands, à moins qu'ils ne réduisent significativement la perte originale.

### Comment elle est implémentée en pratique (AdamW)
Dans la plupart des entraînements GPT (GPT-2, GPT-3 d'OpenAI, LLaMA, Mistral, etc.), on n'utilise PAS l'optimiseur Adam standard avec une régularisation L2 classique. On utilise plutôt AdamW (Adam avec décroissance de poids découplée).

La différence clé :
- La régularisation L2 standard dans Adam ajoute la pénalité directement dans le gradient.
- AdamW la découple : elle applique la décroissance de poids comme une étape de mise à jour séparée, ce qui fonctionne bien mieux avec les optimiseurs adaptatifs comme Adam.

Ainsi, lorsque vous voyez quelque chose comme ceci dans les configurations d'entraînement :

```python
optimizer = AdamW(model.parameters(), lr=5e-5, weight_decay=0.1)
```

Cette valeur 0.1 est le λ mentionné ci-dessus, et il s'agit de la version correcte avec découplage.

### Valeurs typiques dans les modèles de style GPT réels

| Modèle / Article     | Décroissance de Poids | Notes                                   |
|----------------------|-----------------------|-----------------------------------------|
| GPT-2 (OpenAI)       | 0.01                  |                                         |
| GPT-3 (OpenAI)       | 0.1                   | Brown et al. 2020                       |
| LLaMA 1 & 2 (Meta)   | 0.1                   | Souvent combinée avec aucune décroissance sur les normes/biais |
| PaLM (Google)        | 0.1                   |                                         |
| Grok-1 (xAI)         | 0.1                   | D'après la configuration de la version ouverte |
| Mistral / Mixtral    | 0.1                   |                                         |

### Nuance importante : quels paramètres reçoivent la décroissance de poids ?
La pratique moderne (depuis LLaMA) consiste à appliquer la décroissance de poids seulement à certaines couches :
- Oui : Couches linéaires (matrices de poids), matrice d'embedding
- Non : Termes de biais (bias), poids des LayerNorm, tout paramètre 1D

Ceci est généralement réalisé avec des groupes de paramètres dans PyTorch :

```python
decay = set()
no_decay = set()
for name, param in model.named_parameters():
    if "bias" in name or "layer_norm" in name or param.ndim == 1:
        no_decay.add(param)
    else:
        decay.add(param)

optimizer = AdamW([
    {"params": list(decay),   "weight_decay": 0.1},
    {"params": list(no_decay), "weight_decay": 0.0}
], lr=...)
```

### Pourquoi c'est important pour les modèles à l'échelle GPT
Avec des milliards ou des centaines de milliards de paramètres, les modèles peuvent facilement mémoriser les données d'entraînement. La décroissance de poids est l'un des outils les plus simples et les plus efficaces (avec le dropout, la profondeur stochastique, etc.) pour maintenir la capacité effective sous contrôle et améliorer les performances en aval.

En bref : la décroissance de poids ≈ régularisation L2, mais correctement implémentée via AdamW et appliquée de manière sélective, est un ingrédient standard dans pratiquement toutes les recettes de pré-entraînement modernes de style GPT.