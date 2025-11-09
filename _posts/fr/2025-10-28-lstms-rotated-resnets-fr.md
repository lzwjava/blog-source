---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Les LSTM n'étaient que des ResNets pivotés
translated: true
type: note
---

Lors de sa conférence NeurIPS 2024 pour le prix Test of Time décerné à l'article de 2014 "Sequence to Sequence Learning with Neural Networks", Ilya Sutskever a partagé ses réflexions sur les idées clés et les erreurs de cette époque. Un point majeur qu'il a abordé sous la rubrique "ce que nous avons eu tort" était la complexité excessive et les limitations finales des LSTM (réseaux à mémoire à long terme), qui ont propulsé les premières avancées en modélisation de séquences comme la traduction automatique.

### L'idée fausse fondamentale sur les LSTM
Nous avons traité les LSTM comme une architecture fondamentalement nouvelle et complexe, spécialement conçue pour les données séquentielles — quelque chose de "spécial" que les chercheurs en apprentissage profond ont dû ingénieusement concevoir pour gérer les dépendances temporelles, les gradients disparaissants et la récurrence. En réalité, Sutskever a expliqué que les LSTM étaient bien plus simples que cela : **ils sont essentiellement un ResNet (Réseau Résiduel) tourné de 90 degrés**.

- **Les ResNets** (introduits en 2015) ont révolutionné le traitement d'images en ajoutant des connexions résiduelles (skip connections) qui permettent à l'information de circuler directement à travers les couches, permettant ainsi la création de réseaux bien plus profonds sans instabilité lors de l'entraînement.
- Les LSTM (datant de 1997) ont fait une chose analogue mais dans la *dimension temporelle* : leurs portes et leur état de cellule agissent comme des résidus, permettant aux gradients et à l'information de se propager sur de longues séquences sans s'estomper. C'est le même principe — simplement "tourné" d'un empilement spatial (par exemple, des pixels dans une image) vers un empilement temporel (par exemple, des mots dans une phrase).

Sutskever a plaisanté en disant : "Pour ceux qui ne les connaissent pas, un LSTM est ce que les pauvres chercheurs en apprentissage profond utilisaient avant les Transformers. C'est essentiellement un ResNet mais tourné de 90 degrés... Et il est arrivé avant ; c'est comme un ResNet légèrement plus complexe, avec un intégrateur et quelques multiplications." Cette analogie souligne que les LSTM n'étaient pas une rupture radicale ; ils étaient une application précoce et élégante des idées résiduelles à la récurrence.

### Pourquoi cela importait (et ce qui a mal tourné)
- **Ce qui a brillamment fonctionné** : Les LSTM ont étonnamment bien passé à l'échelle pour leur époque, permettant au modèle seq2seq de surpasser les méthodes statistiques traditionnelles sur les tâches de traduction. Les résidus ont rendu les réseaux récurrents profonds entraînables, un peu comme ils l'ont fait plus tard pour les réseaux feedforward.
- **Ce que nous avons eu tort (et pourquoi les LSTM ont décliné)** : Nous avons sous-estimé à quel point la nature séquentielle des LSTM deviendrait un goulot d'étranglement pour la mise à l'échelle. Contrairement aux ResNets ou aux Transformers parallélisables, les LSTM traitent les données étape par étape, ce qui les rend inefficaces pour les jeux de données massifs ou les contextes longs. Ils ont également ajouté une complexité inutile (par exemple, des portes multiples) que les mécanismes d'attention dans les Transformers ont su simplifier et éliminer. Dès 2017, les Transformers ont exposé ces limites, déplaçant l'attention vers l'auto-attention pour une meilleure parallélisation et des dépendances à plus long terme.

Avec le recul, la partie "erronée" n'était pas d'avoir inventé les LSTM — ils ont été une solution intérimaire héroïque — mais de s'y être accrochés comme à la solution ultime pour les séquences, au lieu de reconnaître les résidus comme un outil général et de pousser plus tôt vers des architectures plus parallèles.

Cette perspective replace les LSTM non pas comme une relique, mais comme une étape fondatrice dans la compréhension de la façon dont les connexions résiduelles libèrent la profondeur à travers les dimensions.

[Sequence to Sequence Learning with Neural Networks: What a Decade – Transcript & Video](https://kingy.ai/news/sequence-to-sequence-learning-with-neural-networks-what-a-decade-transcript-video/)
[Ilya Sutskever NeurIPS 2024 full talk](https://www.youtube.com/watch?v=1yvBqasHLZs)
[Reflections from Ilya's Full Talk at NeurIPS 2024](https://dlyog.com/papers/one_internet_v1)