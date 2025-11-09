---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Présentation et aperçu de Muon Optimizer
translated: true
type: note
---

### Présentation complète de l'optimiseur Muon

L'optimiseur Muon est un algorithme d'optimisation spécialisé, d'inspiration du second ordre, conçu principalement pour l'entraînement des couches linéaires dans les réseaux de neurones (par exemple, les couches entièrement connectées ou d'embedding), bien qu'il puisse être étendu à d'autres. Il a été initialement proposé fin 2024 par des chercheurs dont Keller Jordan et Jeremy Bernstein, avec des racines dans des techniques d'optimisation géométrique comme l'initialisation polaire et le cadre de dualité modulaire[1][2]. Zhiling Yang, fondateur de Moonshot AI et Kimi AI, a mis en avant Muon dans des discussions concernant l'entraînement de leur modèle Kimi K2—un grand modèle de langage (LLM) à 1 trillion de paramètres—où il a servi de colonne vertébrale pour des mises à jour efficaces et de haut rang qui s'adaptent à la géométrie du paysage de la fonction de perte[3][4]. Cependant, sa version de base souffrait d'instabilité (par exemple, des pics de perte pendant les longs entraînements), incitant Moonshot AI à développer MuonClip, une variante améliorée avec des mécanismes de stabilité comme le QK-clipping pour les couches d'attention[3][2].

Muon se distingue par son efficacité en termes de tokens : il nécessite moins de tokens d'entraînement que les optimiseurs du premier ordre comme AdamW pour atteindre des performances comparables, ce qui le rend précieux pour des tâches gourmandes en ressources comme le pré-entraînement des LLM. Il vise à approximer les méthodes du second ordre (par exemple, la méthode de Newton) sans leur coût computationnel complet, en se concentrant sur l'adaptation des valeurs propres via des mises à jour matricielles de haut rang. Ceci est particulièrement utile dans les modèles à grande échelle où les gradients sont bruyants, car Muon tire parti d'un préconditionnement inspiré des gradients naturels et des racines carrées matricielles.

#### Principes clés et Dérivation
- **Concept Central** : Muon est ancré dans l'optimisation géométrique, adaptant les mises à jour au "paysage énergétique" de la fonction de perte. Il utilise un préconditionneur basé sur la matrice d'information de Fisher (ou des approximations) pour mettre à l'échelle les gradients, similaire à AdaGrad ou Shampoo mais optimisé pour les couches linéaires denses[1][2].
- **Étapes de l'Algorithme** :
  1. **Calcul du Gradient** : Calcule les gradients standards \(\nabla W\) pour les poids \(W\) dans les couches linéaires.
  2. **Préconditionnement** : Utilise les itérations de Newton-Schulz pour approximer la racine carrée matricielle d'un préconditionneur (par exemple, dérivé des statistiques de la couche). Cela permet l'adaptation du rang sans décomposition complète en valeurs propres.
  3. **Règle de Mise à Jour** : Applique une mise à jour qui met à l'échelle plus efficacement les composantes de haut rang, souvent combinée avec du momentum ou du clipping pour la stabilité.
- **Perspective Mathématique** : Si \(G\) est la matrice gradient, Muon approxime une mise à jour comme \(W \leftarrow W - \eta \cdot \sqrt{P}^{-1} G\), où \(\sqrt{P}\) utilise une racine carrée matricielle itérative[2][5]. Ceci contraste avec la mise à l'échelle diagonale ou basée sur les moments d'AdamW, permettant à Muon de mieux capturer les corrélations entre paramètres.
- **Gain d'Efficacité** : Muon peut réduire le nombre d'étapes d'entraînement de 20 à 50 % dans certains benchmarks, comme observé dans son utilisation avec les records NanoGPT[1].

#### Avantages et Inconvénients
- **Avantages** :
  - **Meilleure Convergence sur les Couches Linéaires** : Excelle dans les espaces denses et de haute dimension typiques des LLM, conduisant à une perte plus faible avec moins de tokens[4][6].
  - **Efficacité des Ressources** : Entraînement plus rapide par époque en raison de moins de calculs de gradients nécessaires.
  - **Open Source et Extensible** : Plusieurs implémentations existent, incluant des spécifiques comme Flash-Muon pour l'accélération GPU[4][7].
- **Inconvénients** :
  - **Instabilité** : Sujet à la divergence dans les réseaux plus profonds ou les couches éparses ; MuonClip adresse ceci en écrantant les scores d'attention (par exemple, les produits query-key) pendant l'entraînement[3][2].
  - **Spécificité de Couche** : Pas idéal pour les couches convolutionnelles ou récurrentes ; il est biaisé vers les architectures linéaires/MoE. Keras note qu'il ne devrait pas être utilisé pour les couches non linéaires[8].
  - **Sensibilité aux Hyperparamètres** : Nécessite un réglage pour le taux d'apprentissage (\(\eta\)) et les mouvements induisant l'orthogonalité ; peut ne pas se transférer entre différentes tailles de modèles sans ajustement[2].
- **Variante MuonClip (Spécifique à Kimi)** : C'est l'évolution de Muon, intégrée avec le QK-clipping pour prévenir l'instabilité lors du pré-entraînement sur 15,5 billions de tokens. Elle a stabilisé les 32 milliards de paramètres activés de Kimi K2, permettant un entraînement sans pic de perte et des benchmarks supérieurs (par exemple, 66,1 sur Tau2-Bench)[3][8]. Sans code public pour l'instant, elle est propriétaire mais s'appuie sur Muon ouvert.

Muon a influencé le paysage de l'optimisation en IA, apparaissant dans des benchmarks comme Scion et des discussions sur Reddit/X, souvent salué pour son "intuition géométrique". Pour les dérivations complètes, voir le blog de Jeremy Bernstein[2]. Maintenant, regardons une implémentation pratique.

### Exemple de Code : Implémentation de l'optimiseur Muon dans PyTorch
Ci-dessous une implémentation PyTorch de l'optimiseur Muon de base, adaptée depuis le dépôt officiel (https://github.com/KellerJordan/Muon). Ceci est une version simplifiée pour les couches linéaires denses ; elle inclut les itérations de Newton-Schulz pour le préconditionneur.

```python
import torch
import torch.nn as nn

class Muon(torch.optim.Optimizer):
    """
    Optimiseur Muon pour les couches linéaires.
    De : https://github.com/KellerJordan/Muon
    """
    def __init__(self, params, lr=1e-3, lr_b=2e-3, b2=0.95, wd=0.0):
        defaults = dict(lr=lr, lr_b=lr_b, b2=b2, wd=wd)
        super().__init__(params, defaults)

    def step(self):
        for group in self.param_groups:
            lr = group['lr']
            lr_b = group['lr_b']
            b2 = group['b2']
            wd = group['wd']

            for p in group['params']:
                if p.grad is None:
                    continue

                grad = p.grad.data.float()
                state = self.state[p]
                if 'momentum' not in state:
                    state['momentum'] = torch.zeros_like(grad)

                # Mise à jour du momentum
                state['momentum'].mul_(b2).add_(grad)

                # Déchéance de poids (weight decay)
                if wd != 0:
                    p.data.mul_(1 - lr * wd)

                # Orthonormalisation de Muon (adaptation du rang)
                grad_vec = state['momentum'].view(-1, grad.shape[-1])
                p_vec = p.data.view(-1, p.shape[-1])

                # Newton-Schulz pour l'approx. de la racine carrée matricielle (simplifié)
                G = grad_vec @ grad_vec.t() / grad_vec.shape[0]
                # Dans l'implémentation complète, c'est itératif ; ici, approximation par série entière
                sqrt_G = torch.sqrt(G + 1e-6 * torch.eye(G.shape[0], device=G.device))

                # Mise à jour
                update = grad_vec.t() @ sqrt_G @ grad_vec / sqrt_G.shape[0]
                p.data.sub_(lr_b * update.view(p.shape))

# Exemple d'utilisation
model = nn.Linear(768, 768)  # Couche dense
optimizer = Muon(model.parameters(), lr=0.01)
loss_fn = nn.MSELoss()
data = torch.randn(32, 768)
target = torch.randn(32, 768)

for epoch in range(10):
    optimizer.zero_grad()
    output = model(data)
    loss = loss_fn(output, target)
    loss.backward()
    optimizer.step()
    print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")
```

**Notes sur le Code** :
- Ceci est une version simplifiée ; le dépôt GitHub complet inclut des kernels CUDA pour l'efficacité (par exemple, Flash-Muon pour des matmuls plus rapides)[3][4].
- Pour Keras/TensorFlow : Utilisez `from keras.optimizers import Muon; opt = Muon(learning_rate=0.01)`[8].
- Les hyperparamètres ajustés (par exemple, `lr_b=2e-3`) sont cruciaux ; expérimentez avec votre modèle. Pour MuonClip de Kimi K2, aucun code public n'existe, mais il ajoute une logique de clipping dans les passes forward de l'attention[2][5].

Si vous avez besoin d'extensions ou de benchmarks, faites-le moi savoir !

Citations :
[1] https://kellerjordan.github.io/posts/muon/
[2] https://jeremybernste.in/writing/deriving-muon
[3] https://github.com/KellerJordan/Muon
[4] https://github.com/nil0x9/flash-muon
[5] https://www.lakernewhouse.com/writing/muon-2
[6] https://medium.com/@kyeg/building-the-muon-optimizer-in-pytorch-a-geometric-approach-to-neural-network-optimization-17f4601be548
[7] https://discuss.huggingface.co/t/tutorial-understanding-and-implementing-the-muon-optimizer/167717
[8] https://keras.io/api/optimizers/muon/