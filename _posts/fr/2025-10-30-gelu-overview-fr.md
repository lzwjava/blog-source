---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Aperçu de la fonction d'activation GELU
translated: true
type: note
---

### Qu’est-ce que GELU ?

L’unité linéaire à erreur gaussienne (GELU) est une fonction d’activation lisse utilisée dans les réseaux de neurones, en particulier dans les modèles basés sur les transformers comme les séries BERT et GPT. Proposée en 2016 par les chercheurs Dan Hendrycks et Kevin Gimpel, elle combine les avantages des transformations linéaires avec une pondération probabiliste inspirée de la distribution gaussienne (normale). Contrairement aux fonctions d’activation plus simples comme ReLU (qui donne une sortie nulle pour les entrées négatives), GELU permet un faible flux de gradient pour les valeurs négatives, ce qui améliore les performances dans les réseaux profonds en réduisant les problèmes tels que le gradient qui disparaît et en accélérant la convergence.

#### Définition mathématique
La formule principale de GELU est :

\\[
\text{GELU}(x) = x \cdot \Phi(x)
\\]

où \\(\Phi(x)\\) est la fonction de répartition (CDF) de la distribution normale centrée réduite :

\\[
\Phi(x) = \frac{1}{2} \left[ 1 + \erf\left( \frac{x}{\sqrt{2}} \right) \right]
\\]

Ici, \\(\erf\\) est la fonction d’erreur, qui mesure à quel point une gaussienne approxime une fonction échelon. Cela rend GELU probabiliste : elle « supprime » les entrées négatives moins brutalement que ReLU, tout en conservant intactes les entrées positives.

Pour des raisons d’efficacité computationnelle, des approximations sont souvent utilisées, comme la version basée sur sigmoïde :

\\[
\text{GELU}(x) \approx x \cdot \sigma(1.702x)
\\]

où \\(\sigma\\) est la fonction sigmoïde.

#### Pourquoi utiliser GELU ?
- **Lissage** : elle est différentiable partout, ce qui facilite l’optimisation.
- **Non-monotonie** : elle supprime légèrement les valeurs négatives sans les annuler, préservant ainsi l’information.
- **Avantages empiriques** : elle surpasse ReLU et ELU dans des tâches comme le traitement du langage naturel, avec un apprentissage plus rapide et une meilleure précision dans les grands modèles.
- **Inconvénients** : légèrement plus coûteuse en calcul que ReLU à cause du calcul de erf ou sigmoïde.

En pratique, des bibliothèques comme PyTorch et TensorFlow disposent d’implémentations intégrées de GELU (par exemple `torch.nn.GELU()`).

#### Références
- [Gaussian Error Linear Units (GELUs)](https://arxiv.org/abs/1606.08415)
- [GELU Explained](https://www.baeldung.com/cs/gelu-activation-function)
- [GELU Activation](https://medium.com/@shauryagoel/gelu-gaussian-error-linear-unit-4ec59fb2e47c)