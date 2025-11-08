---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Paramètre PyTorch pour les poids ajustables
translated: true
type: note
---

`torch.nn.Parameter` est une sous-classe de `torch.Tensor` dans PyTorch, conçue spécifiquement pour représenter les paramètres apprenables dans les modules de réseaux neuronaux. Son objectif principal est d'enregistrer automatiquement les tenseurs en tant que paramètres du module lorsqu'ils sont assignés comme attributs à un `torch.nn.Module`, les rendant accessibles via des méthodes comme `module.parameters()` ou `module.named_parameters()`. Cela aide à distinguer les poids entraînables (par exemple, pour les couches) des tenseurs réguliers, empêchant les calculs temporaires (comme les états mis en cache dans les RNNs) d'être traités par erreur comme des paramètres.

### Caractéristiques principales
- **Enregistrement automatique** : Lorsque vous assignez un `Parameter` à un module (par exemple, `self.weight = nn.Parameter(torch.randn(3, 3))` dans la méthode `__init__` d'un module personnalisé), il est ajouté à la liste des paramètres du module sans code supplémentaire.
- **Suivi du gradient** : Par défaut, `requires_grad=True`, donc il participe à la rétropropagation. Cela reste vrai même à l'intérieur d'un contexte `torch.no_grad()` — utilisez la désactivation locale d'autograd pour un contrôle plus fin.
- **Attributs** : Il hérite de toutes les propriétés de `Tensor` mais n'ajoute aucune nouvelle propriété au-delà de son comportement spécial lié au module.

### Utilisation de base
Voici un exemple simple dans un module personnalisé :

```python
import torch
import torch.nn as nn

class MyModule(nn.Module):
    def __init__(self):
        super().__init__()
        # Ceci est automatiquement enregistré comme un paramètre
        self.weight = nn.Parameter(torch.randn(2, 3))
        # Un tenseur standard ne sera pas enregistré
        self.bias = torch.zeros(3)

    def forward(self, x):
        return x @ self.weight + self.bias

model = MyModule()
print(list(model.parameters()))  # Affiche : [Parameter contenant : tensor(...)]
```

Pour plus de détails, consultez la documentation officielle : [Parameter — PyTorch 2.9 documentation](https://pytorch.org/docs/stable/generated/torch.nn.parameter.Parameter.html)