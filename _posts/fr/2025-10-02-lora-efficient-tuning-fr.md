---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: LoRA pour un réglage fin efficace des LLM
translated: true
type: note
---

### Résumé de l'article de blog LoRA de Thinking Machines

L'article de blog de Thinking Machines (intitulé "LoRA" sur leur site) fournit une explication détaillée de l'Adaptation Bas-Rang (LoRA), une technique pour affiner efficacement les grands modèles de langage (LLM) avec un minimum de ressources computationnelles. Il décompose l'idée centrale de LoRA, son implémentation, ses avantages et ses applications pratiques, dans le but de rendre le concept accessible aux lecteurs familiers avec les bases du machine learning.

#### Concept central de LoRA
LoRA relève le défi d'adapter des LLM pré-entraînés, qui peuvent avoir des milliards de paramètres, à de nouvelles tâches sans avoir à ré-entraîner le modèle entier. Au lieu de mettre à jour tous les poids, il introduit des "adaptations bas-rang" en gelant le modèle original et en ajoutant des matrices bas-rang entraînables à des couches spécifiques. Cela réduit considérablement le nombre de paramètres entraînables, parfois par un facteur de 10 000, tout en atteignant des performances comparables à un affinage complet.

Les mécanismes clés incluent :
- **Décomposition** : La mise à jour des poids \\(\Delta W\\) est approximée par \\(A \times B\\), où \\(A\\) est de dimension \\(d \times r\\) et \\(B\\) est de dimension \\(r \times k\\), avec \\(r\\) (le rang) étant bien plus petit que \\(d\\) ou \\(k\\).
- **Points d'Injection** : Les couches LoRA sont typiquement ajoutées aux modules d'attention (matrices de requête, clé, valeur, de projection) dans les transformers, car celles-ci sont les plus spécifiques à la tâche.
- **Stockage et Inférence** : Le modèle adapté stocke seulement les petites matrices \\(A\\) et \\(B\\), et durant l'inférence, les poids LoRA sont fusionnés dans les poids originaux pour plus d'efficacité.

#### Avantages et Compromis
L'article souligne l'efficacité de LoRA pour l'entraînement sur des GPU plus petits avec moins de données, permettant une adaptation rapide pour des tâches comme le réglage sur instructions ou l'affinage spécifique à un domaine. Il peut atteindre des performances proches de l'affinage complet avec seulement 0,5 à 1 % des paramètres entraînables. Cependant, il peut être moins performant sur des tâches très divergentes nécessitant des changements architecturaux significatifs, et il y a une légère augmentation de la latence d'inférence due aux multiplications matricielles.

#### Implémentation et Exemples
Le blog inclut des extraits de code (en PyTorch) montrant comment ajouter des couches LoRA, par exemple en encapsulant des modules linéaires avec une classe LoRA personnalisée. Il démontre des cas d'utilisation comme l'affinage de modèles LLaMA ou GPT pour des jeux de données spécifiques, avec des conseils comme commencer avec un rang \\(r=8\\) et n'affiner que les paramètres LoRA. Il aborde également le réglage des hyperparamètres, comme l'équilibre entre le rang et la régularisation pour éviter le surapprentissage.

#### Contexte Comparatif et Potentiel Futur
LoRA est positionné comme une alternative à l'affinage complet et à d'autres méthodes PEFT (Parameter-Efficient Fine-Tuning) comme le réglage par prompt ou les adapteurs, en soulignant sa simplicité et son extensibilité. L'article note son adoption croissante dans les communautés open-source et son potentiel pour des configurations d'apprentissage continu. Des références aux articles originaux (par exemple, Hu et al.) sont incluses pour une lecture plus approfondie.

Globalement, l'article sert de guide pratique, encourageant l'expérimentation tout en notant le rôle de LoRA dans la démocratisation de la personnalisation des LLM.