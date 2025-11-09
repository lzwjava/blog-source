---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Pionniers de l'apprentissage profond avant Hinton
translated: true
type: note
---

### Travail d'Alexey Ivakhnenko

Alexey Grigoryevich Ivakhnenko, un cybernéticien ukraino-soviétique, est souvent appelé le « père fondateur du deep learning » pour ses efforts pionniers dans les années 1960 et 1970. Travaillant avec des ressources limitées pendant la guerre froide – une époque où la puissance de calcul était des millions de fois plus limitée qu'aujourd'hui – il s'est concentré sur les réseaux de neurones multicouches qui pouvaient apprendre automatiquement des représentations hiérarchiques des données.

- **1965 : Méthode de groupe de traitement des données (GMDH)** : Avec Valentin Lapa, Ivakhnenko a publié le premier algorithme d'apprentissage général et fonctionnel pour les perceptrons multicouches (MLP) profonds et feedforward supervisés. Cette méthode entraînait les réseaux couche par couche en utilisant l'analyse de régression sur des paires de données d'entrée-sortie. Elle faisait croître les couches de manière incrémentielle, les entraînait séquentiellement et incluait l'élagage des unités cachées inutiles via des ensembles de validation. Surtout, elle permettait aux réseaux d'apprendre des représentations internes distribuées des données d'entrée – une idée centrale dans le deep learning moderne – sans feature engineering manuel. Cela a précédé des concepts similaires dans l'IA occidentale par plusieurs décennies et a été appliqué à des problèmes réels comme la reconnaissance de formes et la prévision.

- **1971 : Implémentation d'un réseau profond** : Ivakhnenko a démontré un réseau de neurones profond à 8 couches utilisant les principes du GMDH, montrant ainsi la possibilité d'une profondeur évolutive pour des tâches complexes. Son approche traitait les réseaux profonds comme une forme d'approximation polynomiale, permettant une sélection automatique de modèle et évitant le « fléau de la dimensionnalité » dans les architectures à nombreuses couches.

Le GMDH d'Ivakhnenko a évolué vers un cadre de modélisation inductive plus large, influençant des domaines comme les systèmes de contrôle et l'économie. Malgré son impact, une grande partie de son travail a été publiée en russe et est passée inaperçue dans les cercles anglophones de l'IA.

### Travail de Shun-ichi Amari

Shun-ichi Amari, un mathématicien et neuroscientifique japonais, a apporté des contributions fondamentales à la théorie des réseaux de neurones dans les années 1960 et 1970, en mettant l'accent sur l'apprentissage adaptatif et les perspectives géométriques sur le traitement de l'information. Ses recherches ont fait le lien entre les neurosciences et le calcul, jetant les bases des systèmes auto-organisés.

- **1967-1968 : Classification adaptative de motifs et descente de gradient stochastique (SGD)** : Amari a proposé la première méthode pour l'entraînement de bout en bout de MLP profonds en utilisant la SGD, une technique d'optimisation remontant à 1951 mais nouvellement appliquée aux réseaux multicouches. Dans des simulations avec un réseau à cinq couches (deux couches modifiables), son système a appris à classer des motifs non linéairement séparables en ajustant les poids directement à travers les couches. Cela a permis à des représentations internes d'émerger via des mises à jour basées sur le gradient, un précurseur direct des méthodes de type rétropropagation, le tout sous des contraintes de calcul des milliards de fois plus sévères que les standards modernes.

- **1972 : Réseaux de mémoire associative adaptatifs** : S'appuyant sur le modèle de Lenz-Ising de 1925 (une architecture récurrente basée sur la physique), Amari a introduit une version adaptative qui apprenait à stocker et à rappeler des motifs en ajustant les poids de connexion basés sur des corrélations. Il gérait le traitement de séquences et récupérait des motifs stockés à partir d'entrées bruitées ou partielles via la dynamique neuronale. Publié d'abord en japonais en 1969, ce travail est considéré comme l'origine du « réseau de Hopfield » pour la mémoire associative.

Amari a également fondé la géométrie de l'information, un domaine utilisant la géométrie différentielle pour analyser les modèles statistiques et la dynamique neuronale, qui sous-tend les réseaux de neurones probabilistes modernes.

### Contexte de la controverse du Nobel 2024

Dans son rapport de 2024 « Un prix Nobel pour le plagiat », Jürgen Schmidhuber soutient que les idées récompensées par le Nobel de Hinton et Hopfield – telles que la machine de Boltzmann (1985) pour l'apprentissage de représentations et le réseau de Hopfield (1982) pour la mémoire associative – ont remballé l'apprentissage profond couche par couche d'Ivakhnenko et les modèles récurrents adaptatifs/SGD d'Amari sans attribution. Par exemple, la machine de Boltzmann a omis de citer l'apprentissage de représentations internes d'Ivakhnenko de 1965 et la SGD d'Amari de 1967, tandis que le réseau de Hopfield a ignoré le modèle d'Ising adaptatif d'Amari de 1972. Schmidhuber affirme que cette omission a persisté dans les études ultérieures et dans le document scientifique de fond du Nobel, mettant en lumière un biais centré sur l'Occident dans l'histoire de l'IA.

[Alexey Ivakhnenko - Wikipedia](https://en.wikipedia.org/wiki/Alexey_Ivakhnenko)
[Deep Learning in a Nutshell: History and Training - NVIDIA Developer](https://developer.nvidia.com/blog/deep-learning-nutshell-history-training/)
[Shun-ichi Amari | Kyoto Prize](https://www.kyotoprize.org/en/laureates/shun-ichi_amari/)
[Japanese scientists were pioneers of AI, yet they're being written out of history](https://modernsciences.org/japanese-ai-pioneers-history-shuninchi-amari-kunihiko-fukushima-december-2024/)
[A Nobel Prize for Plagiarism - Technical Report IDSIA-24-24](https://people.idsia.ch/~juergen/physics-nobel-2024-plagiarism.pdf)
[Machine Learning Stirs Controversy in Nobel Prize in Physics - Harvard Technology Review](https://harvardtechnologyreview.com/2024/11/18/machine-learning-stirs-controversy-in-nobel-prize-in-physics/)