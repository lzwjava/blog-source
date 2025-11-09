---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast:free
title: Analyse et Explication du Code LoRA
translated: true
type: note
---

Je vais décomposer le code de démonstration LoRA en parties clés, en expliquant chaque étape en détail avant de passer à la suivante. Cela aidera à illustrer le fonctionnement de LoRA de manière claire et progressive. Le code est basé sur l'exemple précédent, utilisant PyTorch pour implémenter LoRA sur une couche linéaire simple.

### Partie de code 1 : Définition de la couche LoRA
```python
import torch
import torch.nn as nn

class LoRALayer(nn.Module):
    def __init__(self, in_features, out_features, rank=4):
        super(LoRALayer, self).__init__()
        # Poids originaux gelés
        self.linear = nn.Linear(in_features, out_features)
        self.linear.weight.requires_grad = False  # Geler les poids originaux
        # Paramètres LoRA : matrices de faible rang A et B
        self.lora_A = nn.Parameter(torch.randn(in_features, rank))
        self.lora_B = nn.Parameter(torch.randn(rank, out_features))
        self.scaling = 1.0  # Facteur d'échelle pour les mises à jour LoRA
```

#### Explication
Cette partie définit la classe `LoRALayer`, qui implémente la technique LoRA. Voici ce qui se passe :

- **Imports et configuration de la classe** : Nous importons PyTorch (`torch`) et son module de réseau neuronal (`nn`). La classe `LoRALayer` hérite de `nn.Module`, ce qui en fait un module PyTorch pouvant être intégré dans des modèles plus larges.
- **Couche linéaire originale** : `self.linear = nn.Linear(in_features, out_features)` crée une couche linéaire standard (comme une couche entièrement connectée dans un réseau neuronal) avec `in_features` entrées et `out_features` sorties. Cela représente les poids pré-entraînés que nous souhaitons adapter.
- **Gel des poids** : `self.linear.weight.requires_grad = False` gèle les poids originaux de la couche linéaire, garantissant qu'ils ne sont pas mis à jour pendant l'entraînement. C'est un élément clé de l'efficacité de LoRA, car cela évite de modifier le grand modèle pré-entraîné.
- **Paramètres LoRA** : `self.lora_A` et `self.lora_B` sont des matrices de faible rang. `lora_A` a la forme `(in_features, rank)`, et `lora_B` a la forme `(rank, out_features)`. Le paramètre `rank` (par défaut=4) contrôle la taille de ces matrices, les gardant bien plus petites que la matrice de poids originale (forme `in_features x out_features`). Ces matrices sont entraînables (`nn.Parameter`) et initialisées avec des valeurs aléatoires (`torch.randn`).
- **Facteur d'échelle** : `self.scaling = 1.0` est un hyperparamètre pour mettre à l'échelle l'ajustement LoRA, permettant un réglage fin de la force de l'adaptation.

Cette configuration garantit que seules les petites matrices `lora_A` et `lora_B` sont mises à jour pendant l'entraînement, réduisant considérablement le nombre de paramètres entraînables.

---

### Partie de code 2 : Passe avant (Forward Pass) de LoRA
```python
    def forward(self, x):
        # Transformation linéaire originale + ajustement LoRA
        original = self.linear(x)
        lora_adjustment = self.scaling * torch.matmul(torch.matmul(x, self.lora_A), self.lora_B)
        return original + lora_adjustment
```

#### Explication
Cette partie définit la passe avant de la `LoRALayer`, qui calcule la sortie de la couche :

- **Entrée** : L'entrée `x` est un tenseur de forme `(batch_size, in_features)`, représentant un lot de données d'entrée.
- **Sortie originale** : `original = self.linear(x)` calcule la sortie de la couche linéaire gelée, appliquant les poids pré-entraînés à l'entrée.
- **Ajustement LoRA** : Le terme `torch.matmul(torch.matmul(x, self.lora_A), self.lora_B)` calcule l'adaptation de faible rang. D'abord, `x` est multiplié par `lora_A` (forme `in_features x rank`), produisant un tenseur de forme `(batch_size, rank)`. Ensuite, celui-ci est multiplié par `lora_B` (forme `rank x out_features`), donnant un tenseur de forme `(batch_size, out_features)`—la même forme que la sortie originale. Cet ajustement représente la mise à jour spécifique à la tâche.
- **Mise à l'échelle et combinaison** : L'ajustement est mis à l'échelle par `self.scaling` et ajouté à la sortie originale, produisant la sortie finale. Cela garantit que le modèle conserve les connaissances pré-entraînées tout en incorporant les adaptations spécifiques à la tâche.

La structure de faible rang (`rank` est petit, par exemple 4) garantit que l'ajustement est peu coûteux en calcul et efficace en paramètres par rapport à la mise à jour de la matrice de poids complète.

---

### Partie de code 3 : Jeu de données factice et entraînement
```python
def create_toy_dataset(n_samples=1000):
    X = torch.randn(n_samples, 64)  # Caractéristiques d'entrée aléatoires
    y = torch.randn(n_samples, 10)  # Sorties cibles aléatoires
    return X, y

def train_model(model, X, y, epochs=10, lr=0.01):
    criterion = nn.MSELoss()
    optimizer = optim.Adam([param for param in model.parameters() if param.requires_grad], lr=lr)
    
    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        outputs = model(X)
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()
        print(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item():.4f}")
```

#### Explication
Cette partie crée un jeu de données factice et entraîne le modèle adapté avec LoRA :

- **Jeu de données factice** : La fonction `create_toy_dataset` génère des données synthétiques pour la démonstration. `X` est un tenseur de forme `(1000, 64)` (1000 échantillons, 64 caractéristiques), et `y` est un tenseur de forme `(1000, 10)` (1000 échantillons, 10 dimensions de sortie). Ce sont des tenseurs aléatoires simulant des paires entrée-sortie.
- **Fonction d'entraînement** : La fonction `train_model` configure une boucle d'entraînement simple :
  - **Fonction de perte** : `nn.MSELoss()` définit l'erreur quadratique moyenne comme perte, adaptée à cette tâche factice de type régression.
  - **Optimiseur** : `optim.Adam` optimise uniquement les paramètres entraînables (`param.requires_grad` est `True`), c'est-à-dire `lora_A` et `lora_B`. Le `linear.weight` gelé est exclu, garantissant l'efficacité.
  - **Boucle d'entraînement** : Pour chaque epoch, le modèle calcule les sorties, calcule la perte, effectue la rétropropagation (`loss.backward()`) et met à jour les paramètres LoRA (`optimizer.step()`). La perte est affichée pour suivre la progression de l'entraînement.

Cette configuration montre comment LoRA effectue un réglage fin uniquement sur les matrices de faible rang, gardant le processus léger.

---

### Partie de code 4 : Exécution principale et décompte des paramètres
```python
def main():
    # Définir la graine aléatoire pour la reproductibilité
    torch.manual_seed(42)
    
    # Créer le jeu de données factice
    X, y = create_toy_dataset()
    
    # Initialiser le modèle avec LoRA
    model = LoRALayer(in_features=64, out_features=10, rank=4)
    
    # Compter les paramètres entraînables
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total_params = sum(p.numel() for p in model.parameters())
    print(f"Paramètres entraînables: {trainable_params}")
    print(f"Paramètres totaux: {total_params}")
    
    # Entraîner le modèle
    train_model(model, X, y)

if __name__ == "__main__":
    main()
```

#### Explication
Cette partie rassemble tous les éléments et met en évidence l'efficacité de LoRA :

- **Graine aléatoire** : `torch.manual_seed(42)` assure la reproductibilité des initialisations aléatoires.
- **Jeu de données et modèle** : Le jeu de données factice est créé, et une `LoRALayer` est initialisée avec `in_features=64`, `out_features=10` et `rank=4`.
- **Décompte des paramètres** : Le code calcule :
  - **Paramètres entraînables** : Seulement `lora_A` (64 × 4 = 256) et `lora_B` (4 × 10 = 40), totalisant 296 paramètres.
  - **Paramètres totaux** : Inclut le `linear.weight` gelé (64 × 10 = 640) et le `linear.bias` (10), plus les paramètres LoRA, totalisant 946.
  - Cela montre l'efficacité de LoRA : seulement ~31 % (296/946) des paramètres sont entraînables, contre 100 % dans un réglage fin complet.
- **Entraînement** : La fonction `train_model` est appelée pour effectuer le réglage fin des paramètres LoRA sur le jeu de données factice.

Lorsque vous exécutez ceci, vous verrez que le nombre de paramètres entraînables est bien plus petit que le total, et le modèle s'entraîne rapidement grâce aux mises à jour de faible rang.

---

### Exécution du code
Pour exécuter ceci, vous devez avoir PyTorch installé (`pip install torch`). Sauvegardez le code complet dans un fichier `.py` et exécutez-le. La sortie affichera le nombre de paramètres et la perte d'entraînement sur 10 epochs, démontrant l'efficacité de LoRA pour le réglage fin.

[LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)

Faites-moi savoir si vous souhaitez approfondir une partie ou modifier l'exemple !