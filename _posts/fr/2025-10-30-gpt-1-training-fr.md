---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Architecture et formation de GPT-1
translated: true
type: note
---

### Aperçu de l'architecture GPT-1

GPT-1 (Generative Pre-trained Transformer 1) est le modèle fondateur introduit par OpenAI en 2018. Il a été le pionnier de l'approche consistant à pré-entraîner un grand modèle linguistique sur du texte non étiqueté en utilisant un objectif de modélisation du langage, suivi d'un affinage pour des tâches spécifiques. L'architecture est un **Transformer décodeur uniquement**, adapté du document original sur le Transformer (Vaswani et al., 2017), mais réduit à seulement l'empilement du décodeur pour une génération autoregressive. Cette conception permet au modèle de prédire le token suivant dans une séquence, le rendant adapté aux tâches impliquant du texte continu.

Contrairement aux modèles bidirectionnels comme BERT, GPT-1 utilise une **auto-attention masquée** pour assurer la causalité — chaque position ne peut accéder qu'aux positions précédentes, empêchant ainsi la fuite d'information des tokens futurs.

### Composants clés et hyperparamètres

- **Type de modèle** : Décodeur Transformer multicouche avec auto-attention multi-têtes masquée et réseaux feed-forward positionnels.
- **Nombre de couches** : 12 blocs Transformer (couches).
- **Mécanisme d'attention** : 12 têtes d'attention par couche, chaque tête traitant des états de dimension 64 (dimension totale du modèle : 768).
- **Dimensions des plongements** :
  - Taille cachée (d_model) : 768.
  - Dimension interne du feed-forward (d_ff) : 3072 (4x la taille cachée, standard pour les Transformers).
- **Encodage positionnel** : Plongements positionnels appris ajoutés aux plongements de tokens (pas d'encodages sinusoïdaux utilisés).
- **Fonction d'activation** : Gaussian Error Linear Units (GELU) dans les couches feed-forward.
- **Vocabulaire et tokenisation** : Encodage par paires d'octets (Byte-Pair Encoding - BPE) avec 40 000 fusions, entraîné sur le corpus.
- **Paramètres totaux** : Environ 117 millions.
- **Longueur de séquence** : Entraîné sur des séquences de 512 tokens.
- **Régularisation** :
  - Dropout : 0.1 sur les résiduels, les plongements et l'attention.
  - Décroissance de poids : Régularisation L2 modifiée (0.01) sur les poids non biais/non couche de normalisation.
- **Initialisation** : Poids initialisés à partir d'une distribution normale N(0, 0.02).

### Détails de l'entraînement

- **Pré-entraînement** :
  - **Jeu de données** : BooksCorpus, une collection de ~7 000 livres non publiés (total ~800 millions de mots) couvrant des genres comme la Fantasy, la Romance et l'Aventure. Le texte a été nettoyé (par exemple, via la bibliothèque ftfy) et tokenisé avec spaCy.
  - **Objectif** : Modélisation du langage non supervisée (prédiction du token suivant).
  - **Optimiseur** : Adam avec β1=0.9, β2=0.999, ε=1e-8.
  - **Plan de taux d'apprentissage** : Augmentation linéaire sur 2 000 mises à jour jusqu'à un maximum de 2,5×10⁻⁴, puis décroissance cosinusoïdale jusqu'à 0.
  - **Taille de lot** : 64 séquences par mini-lot.
  - **Époques** : 100.
  - **Métrique de performance** : Atteint une perplexité de 18,4 sur le corpus d'entraînement.
- **Affinage** :
  - Changements minimaux : Ajout d'une couche de sortie linéaire pour les prédictions spécifiques à la tâche et utilisation de tokens délimiteurs (par exemple, <s>, <e>, $) pour structurer les entrées en séquences uniques.
  - Perte auxiliaire de modélisation du langage pondérée à 0,5 pendant l'affinage.
  - Hyperparamètres : Taux d'apprentissage plus faible (6,25×10⁻⁵), taille de lot 32, 3 époques, avec 0,2 % de préchauffage et décroissance linéaire.
  - Cette approche de transfert d'apprentissage a permis des performances solides sur des tâches comme l'implication textuelle et la réponse aux questions sans architectures spécifiques à la tâche.

### Innovations et limitations notables

GPT-1 a démontré qu'un seul modèle pré-entraîné pouvait être transféré efficacement à diverses tâches de TAL via un simple formatage des entrées, surpassant certains modèles ajustés à des tâches spécifiques à l'époque. Cependant, il était relativement petit par rapport aux LLM modernes (par exemple, GPT-3 a 175 milliards de paramètres) et limité à des contextes de 512 tokens. L'architecture a jeté les bases de toute la série GPT, en mettant l'accent sur l'évolutivité du pré-entraînement.

[Improving Language Understanding by Generative Pre-Training](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf)  
[GPT-1 - Wikipedia](https://en.wikipedia.org/wiki/GPT-1)