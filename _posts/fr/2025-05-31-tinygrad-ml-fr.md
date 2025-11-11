---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: TinyGrad Bibliothèque d'Apprentissage Automatique Légère
translated: true
type: note
---

### Introduction à TinyGrad
TinyGrad est une bibliothèque de machine learning et de deep learning légère et minimaliste en Python, conçue pour l'éducation et la simplicité. Elle implémente la différenciation automatique (autograd) comme PyTorch mais est beaucoup plus petite—environ 1 000 lignes de code. Elle est idéale pour apprendre les concepts du ML ou pour construire de petits modèles sans la complexité des bibliothèques plus importantes. Elle prend en charge les tenseurs, les réseaux de neurones et les opérations de base, y compris l'accélération GPU via PyTorch ou Metal.

Vous pouvez trouver le dépôt officiel à : [tinygrad GitHub](https://github.com/geohot/tinygrad). Note : C'est expérimental et moins robuste que PyTorch ou TensorFlow pour un usage en production.

### Installation
Installez TinyGrad via pip :

```bash
pip install tinygrad
```

Elle a des dépendances minimales mais utilise optionnellement PyTorch pour certains backends. Pour le support GPU, assurez-vous d'avoir PyTorch installé.

### Utilisation de base
Commencez par importer et définir le contexte (TinyGrad nécessite de spécifier si vous êtes en phase d'entraînement ou d'inférence, car les gradients sont calculés différemment).

#### Importation et Contexte
```python
from tinygrad import Tensor
from tinygrad.nn import Linear, BatchNorm2d  # Pour les réseaux de neurones

# Définir le contexte : entraînement (pour les gradients) ou inférence
Tensor.training = True  # Activer le suivi des gradients
```

#### Création et Manipulation de Tenseurs
Les tenseurs sont la structure de données principale, similaire aux tableaux NumPy ou aux tenseurs PyTorch.

```python
# Créer des tenseurs à partir de listes, de tableaux NumPy ou par forme
a = Tensor([1, 2, 3])          # À partir d'une liste
b = Tensor.zeros(3)            # Tenseur de zéros de forme (3,)
c = Tensor.rand(2, 3)          # Tenseur aléatoire de forme (2, 3)

# Opérations de base
d = a + b                      # Addition élément par élément
e = d * 2                      # Multiplication par un scalaire
f = a @ Tensor([[1], [2], [3]])  # Multiplication matricielle (a est 1D, transposée implicitement)

print(e.numpy())               # Convertir en NumPy pour affichage ou utilisation ultérieure
```

#### Différenciation Automatique (Rétropropagation)
TinyGrad calcule automatiquement les gradients en utilisant la règle de la chaîne.

```python
# Activer le suivi des gradients
Tensor.training = True

x = Tensor([1.0, 2.0, 3.0])
y = (x * 2).sum()             # Une opération ; y est un scalaire

y.backward()                  # Calculer les gradients
print(x.grad.numpy())         # Gradients par rapport à x : devrait être [2, 2, 2]
```

Pour exporter vers NumPy, utilisez `.numpy()`—les gradients s'accumulent sauf réinitialisation.

#### Réseaux de Neurones et Entraînement
TinyGrad inclut des couches de base et des optimiseurs. Voici un exemple simple de MLP :

```python
from tinygrad.nn import Linear, optim

# Définir un modèle simple (par exemple, une couche linéaire)
model = Linear(3, 1)          # Entrée 3, sortie 1

# Données fictives
x = Tensor.rand(4, 3)         # Lot de 4 échantillons, 3 caractéristiques
y_true = Tensor.rand(4, 1)    # Cible

# Passe forward
pred = model(x).sigmoid()      # Supposant une classification binaire

# Perte (par exemple, MSE)
loss = ((pred - y_true) ** 2).mean()

# Rétropropagation et optimisation
loss.backward()
optim.Adam([model], lr=0.01).step()
```

Pour les réseaux de convolution, utilisez `Conv2d` de `tinygrad.nn`.

### Fonctionnalités Avancées
- **Fonctions de Perte et Activations** : Disponibles dans `tinygrad.nn` (par exemple, `sigmoid`, `relu`, `cross_entropy`).
- **Optimiseurs** : `SGD`, `Adam` dans `tinygrad.nn.optim`.
- **Couches** : `Linear`, `Conv2d`, `BatchNorm`, etc.
- **Sauvegarde/Chargement** : Les modèles peuvent être sauvegardés sous forme de dictionnaires d'état (similaire à PyTorch).
- **GPU/Accélération** : TinyGrad peut fonctionner sur GPU via le backend PyTorch : `TESOR_SET_DEVICE='cuda:0'`. Il prend également en charge Metal sur macOS.
- **Exemples Vision/Débruitage** : Le dépôt contient des exemples comme l'entraînement d'un ResNet sur MNIST.

Pour des exemples complets, consultez le dossier `examples/` dans le dépôt GitHub, comme la classification d'images ou l'apprentissage par renforcement.

### Exemple : Entraînement d'un Réseau de Neurones
Voici un script complet et simple pour entraîner un réseau sur le XOR :

```python
from tinygrad import Tensor
from tinygrad.nn import Linear, optim

# Données
X = Tensor([[0,0], [0,1], [1,0], [1,1]])
Y = Tensor([[0], [1], [1], [0]])

# Modèle
model = Linear(2, 1)
opt = optim.Adam([model], lr=0.1)

Tensor.training = True

for epoch in range(1000):
    pred = model(X).sigmoid()
    loss = ((pred - Y) ** 2).mean()
    loss.backward()
    opt.step()
    opt.zero_grad()

# Test
print(model(Tensor([[0,0]])))  # Devrait être ~0
```

### Conseils et Mises en Garde
- **Changement de Mode** : Toujours définir `Tensor.training = True` pour l'entraînement ; passez à `False` pour l'inférence pour éviter le calcul des gradients.
- **Gestion des Formes** : Les tenseurs suivent le broadcasting de type NumPy, mais attention aux débordements dans les petits modèles.
- **Débogage** : Utilisez `.numpy()` pour inspecter les valeurs. Si quelque chose échoue, vérifiez les incohérences de forme.
- **Performances** : C'est lent pour les grands modèles—utilisez PyTorch pour la production.
- **Mises à Jour** : TinyGrad évolue rapidement ; consultez le dépôt pour la dernière version.

Pour plus de détails, visitez [docs/README.md](https://github.com/geohot/tinygrad/blob/master/README.md) ou exécutez les exemples localement. Si vous avez un cas d'utilisation spécifique, fournissez plus de détails pour un conseil personnalisé !