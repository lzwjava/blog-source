---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Détails d'initialisation et d'activation de NanoGPT
translated: true
type: note
---

Dans **NanoGPT** d'Andrej Karpathy (l'implémentation minimale populaire de GPT de fin 2022 à 2025), le modèle n'utilise **pas** ReLU. Il utilise **GELU** (Gaussian Error Linear Unit) comme fonction d'activation, qui est le choix standard dans les modèles modernes de style GPT (identique à GPT-2, GPT-3, Llama, etc.).

### Plages d'initialisation des paramètres clés dans NanoGPT (à partir de la dernière version 2025)

| Paramètre / Composant          | Méthode d'initialisation                      | Échelle / plage typique                           | Notes |
|--------------------------------|------------------------------------------------|---------------------------------------------------|-------|
| Couche d'embedding (token + position) | `nn.Embedding` → distribution normale      | écart-type = 0.02                                 | Très petite pour garder les logits initiaux petits |
| Couches linéaires dans le FFN (proj) | `nn.Linear` → init PyTorch par défaut → puis mise à l'échelle | poids : écart-type ≈ 0.02–0.03 après mise à l'échelle | Karpathy applique un facteur d'échelle de `0.02 / sqrt(n_embd)` ou similaire dans certaines configs |
| Tête LM finale (projection de sortie) | Identique aux embeddings (poids liés)        | écart-type = 0.02                                 | Liée à l'embedding de token |
| Biais LayerNorm                | Zéros                                          | 0                                                 | Standard |
| Poids LayerNorm                | Uns                                            | 1.0                                               | Standard |
| Mise à l'échelle résiduelle (post-init) | Poids multipliés par un petit facteur        | Souvent `poids *= 0.02` ou `poids *= sqrt(2/n_layers)` | Astuce cruciale pour stabiliser l'entraînement à l'init |
| Projection QKV de l'attention  | Mise à l'échelle comme ci-dessus               | Écart-type effectif ≈ 0.02                        | Même mise à l'échelle que les autres couches linéaires |
| Projection de sortie de l'attention | Mise à l'échelle supplémentaire : `cproj.poids *= 0.02` ou similaire | Encore plus petite (pour compenser le chemin résiduel) | Très important pour les modèles profonds |

### Astuce d'initialisation spéciale dans NanoGPT
Dans `model.py`, après avoir créé chaque couche `nn.Linear`, Karpathy fait quelque chose comme ceci (les valeurs exactes dépendent de la configuration) :

```python
if isinstance(m, nn.Linear):
    torch.nn.init.normal_(m.weight, mean=0.0, std=0.02)
    if m.bias is not None:
        torch.nn.init.zeros_(m.bias)
    # Mise à l'échelle résiduelle importante pour les réseaux plus profonds
    if "cproj" in name:          # projection de sortie de l'attention ou du FFN
        m.weight.data *= 0.02    # ou parfois *= 1/sqrt(n_layer)
```

Ou dans les versions plus récentes (2024–2025), il utilise une mise à l'échelle pilotée par la configuration :

```python
std = 0.02 / math.sqrt(2 * n_layer)   # aide pour les modèles plus profonds
```

Cela garantit que la variance du flux résiduel n'explose pas ne disparaît pas à mesure que la profondeur augmente.

### Résumé : NanoGPT n'utilise PAS ReLU
- Activation : **GELU** (pas ReLU)
- Écart-type d'initialisation principal : **~0.02**
- Mise à l'échelle supplémentaire sur les projections de sortie : **0.02 ou plus petite** (particulièrement important)
- Pas de biais dans la plupart des couches linéaires sauf LayerNorm

Cette initialisation très petite + la mise à l'échelle résiduelle est la raison pour laquelle NanoGPT s'entraîne de manière stable même sans période de préchauffage du taux d'apprentissage dans les plus petites configurations.

Si vous entraînez votre propre NanoGPT à partir de zéro, copiez ces astuces d'initialisation exactes — elles sont bien plus importantes que ce que les gens pensent !