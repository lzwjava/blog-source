---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Impact du Nombre de Couches de Transformateurs sur les Performances
translated: true
type: note
---

Dans NanoGPT, le nombre de blocs transformateurs (contrôlé par le paramètre `n_layer`) détermine la profondeur du modèle, ce qui impacte directement sa capacité à apprendre des représentations hiérarchiques dans les données linguistiques. Les configurations standard utilisent 6 couches pour l'exemple léger au niveau des caractères de Shakespeare (pour tenir sur un seul GPU en quelques minutes) et 12 couches pour reproduire le modèle GPT-2 124M (sur des configurations multi-GPU sur plusieurs jours). Réduire ce nombre à 4 ou 1 couche crée un modèle moins profond qui s'entraîne plus vite et utilise moins de mémoire, mais cela se fait au détriment des performances—entraînant typiquement une perte de validation plus élevée, un sous-apprentissage et une génération de texte de moindre qualité.

### Effets clés d'un nombre réduit de couches
- **Capacité du modèle et performances** : Chaque bloc transformateur ajoute des couches d'auto-attention et de feedforward qui construisent des caractéristiques de plus en plus abstraites (par exemple, des tokens à la syntaxe, puis à la sémantique). Moins de blocs limitent cet empilement, donc le modèle a du mal avec les motifs complexes. Sur le jeu de données Shakespeare :
  - 6 couches (par défaut) : ~1,47 de perte de validation après ~3 minutes sur un GPU A100 ; génère un texte cohérent mais imparfait de type Shakespeare (par exemple, "To be or not to be...").
  - 4 couches : ~1,88 de perte de validation après ~3 minutes sur CPU (avec des embeddings/têtes réduits pour la faisabilité) ; les échantillons sont plus bruités et moins structurés (par exemple, "GLEORKEN VINGHARD III: Whell's the couse..."), montrant un "hint of the right character gestalt" mais une sortie plus déformée.
  - 1 couche : Aucun benchmark direct dans la doc de NanoGPT ou les expériences courantes, mais on peut s'attendre à une perte encore plus élevée (~2,0+ basé sur les tendances de mise à l'échelle) et une génération primitive—essentiellement un seul passage d'attention + MLP, bon pour des démos jouets de prédiction basique de type n-gramme mais échouant sur la modélisation linguistique nuancée. Il pourrait surapprendre rapidement sur de courtes séquences mais généraliser mal.

- **Impact sur l'entraînement et les ressources** :
  - **Vitesse/Mémoire** : 4 couches réduit le temps d'entraînement de ~20-30 % par rapport à 6 couches sur un matériel similaire et divise par deux l'utilisation de la mémoire (par exemple, tient facilement sur CPU ou des GPU bas de gamme). 1 couche serait encore ~50-70 % plus rapide, pouvant s'entraîner en quelques secondes sur CPU.
  - **Hyperparamètres** : On associe souvent moins de couches avec un `n_embd` plus petit (par exemple, 128-256) et `n_head` (par exemple, 4) pour éviter la sous-utilisation, plus moins d'itérations (par exemple, 1000-2000) puisque le modèle converge plus vite mais plafonne plus tôt.
  - **Comportement de mise à l'échelle** : Les expériences montrent que la perte s'améliore logarithmiquement avec le nombre de couches (par exemple, 6 couches : ~1,78 val loss ; 8 : ~1,73 ; 12 : ~1,68 sur des configurations similaires). Les modèles plus profonds (12+ couches) excellent sur des jeux de données plus grands comme OpenWebText, atteignant ~2,85 val loss pour la reproduction de GPT-2.

### Comment expérimenter dans NanoGPT
Pour tester cela, modifiez `config/train_shakespeare_char.py` (ou votre fichier de configuration) et exécutez :
```
python train.py config/train_shakespeare_char.py --n_layer=4 --n_head=4 --n_embd=128 --max_iters=2000
```
Pour 1 couche : `--n_layer=1 --n_head=2 --n_embd=64` (réduit davantage pour rester léger). Utilisez `sample.py` sur le checkpoint de sortie pour générer du texte et comparer.

En résumé, 4 couches est une réduction pratique pour du prototypage rapide ou des exécutions à faibles ressources (sortie encore utilisable), tandis qu'1 couche est plus éducative qu'efficace—excellente pour comprendre le rôle du bloc mais pas pour une modélisation sérieuse. Si vous ciblez les 12 couches de GPT-2, descendre à 4 doublerait approximativement la perte et diviserait par deux la cohérence sur les benchmarks.

[karpathy/nanoGPT GitHub](https://github.com/karpathy/nanoGPT)  
[VizuaraAI/nano-gpt-oss GitHub](https://github.com/VizuaraAI/nano-gpt-oss)