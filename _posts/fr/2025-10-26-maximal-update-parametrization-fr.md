---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Paramétrisation par mise à jour maximale pour les réseaux neuronaux
translated: true
type: note
---

### Qu'est-ce que μP (Maximal Update Parametrization) ?

μP, abréviation de Maximal Update Parametrization, est une technique de reparamétrisation des poids des réseaux de neurones développée par Greg Yang, un mathématicien et chercheur en IA maintenant chez xAI (précédemment chez Microsoft Research). Introduite dans son article de 2022 « Tensor Programs V: Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer », elle reparamétrise les poids des modèles d'apprentissage profond pour les rendre plus évolutifs et efficaces à l'entraînement.

#### Objectif
L'objectif principal de μP est de stabiliser le réglage des hyperparamètres (HP) pour différentes tailles de modèles. Dans les configurations traditionnelles (comme la paramétrisation standard, ou SP), les hyperparamètres tels que les taux d'apprentissage doivent être reréglés à chaque fois que l'on augmente l'échelle d'un modèle (par exemple, de millions à milliards de paramètres), car les gradients et les mises à jour deviennent instables (évoluant souvent de manière quadratique avec la largeur ou la profondeur du modèle). μP résout ce problème en transformant les paramètres de sorte que la « mise à jour maximale » (le plus grand pas de gradient possible) reste cohérente quelle que soit l'échelle. Cela permet le **μTransfer**, un flux de travail où vous réglez les HP sur un minuscule modèle « proxy » et les appliquez directement à un modèle cible massif sans aucun ajustement supplémentaire.

#### Principaux Avantages
- **Économies de Coût Importantes** : Le réglage sur de petits modèles est peu coûteux. Par exemple, le transfert des HP d'un proxy de 13M paramètres a surpassé les résultats publiés pour BERT-large (350M paramètres), avec un coût total de réglage équivalent à seulement une session de pré-entraînement de BERT-large. Pour GPT-3 (6,7G paramètres), un transfert depuis un proxy de 40M a battu les bases de référence avec seulement 7 % du coût total de pré-entraînement.
- **Évolutivité pour les Grands Modèles** : Fonctionne bien sur des architectures comme les Transformers et les ResNets, ce qui la rend idéale pour l'entraînement de réseaux de neurones énormes (par exemple, ceux utilisés chez xAI). Elle garantit des « optima invariants d'échelle », ce qui signifie que le paysage de la fonction de perte ne se déforme pas de manière imprévisible à mesure que les modèles grandissent.
- **Facilité d'Utilisation** : Disponible sous forme de bibliothèque PyTorch (`pip install mup`), et elle a été intégrée dans les pipelines de production pour l'entraînement de grands modèles d'IA.

#### Intuition Mathématique Rapide
Avec la SP, la variance des poids croît de manière instable, conduisant à des gradients qui explosent ou disparaissent. μP reparamétrise les poids (par exemple, pour une couche linéaire, en les mettant à l'échelle par le *fan-in*) pour normaliser la matrice d'information de Fisher, garantissant ainsi que les flux de gradients restent équilibrés. Cela maintient les HP optimaux (comme les taux d'apprentissage) approximativement constants quelle que soit l'échelle, évitant ainsi la nécessité d'un reréglage pour chaque taille.

μP s'appuie sur le cadre plus large des « Tensor Programs » de Greg Yang pour comprendre les limites de largeur/profondeur infinies dans les réseaux de neurones, et elle évolue encore. Les travaux récents (en 2025) soulignent son rôle dans l'apprentissage maximal des caractéristiques (*maximal feature learning*), au-delà du simple transfert d'hyperparamètres.

**Références**
- [Tensor Programs V: Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer](https://arxiv.org/abs/2203.03466)
- [The Practitioner's Guide to the Maximal Update Parameterization](https://www.cerebras.ai/blog/the-practitioners-guide-to-the-maximal-update-parameterization)
- [How To Scale (Blog on μP and Scaling)](https://howtoscalenn.github.io/)
- [Greg Yang's Professional Page](https://thegregyang.com/)