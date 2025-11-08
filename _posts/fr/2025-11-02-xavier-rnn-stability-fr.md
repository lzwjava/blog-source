---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Initialisation de Xavier pour la stabilité des RNN
translated: true
type: note
---

### Pourquoi l'initialisation Xavier dans les RNN ?

Les RNN (réseaux de neurones récurrents) reposent sur l'initialisation Xavier (aussi appelée Glorot) pour leurs matrices de poids—comme `Wxh` (entrée vers caché), `Whh` (caché vers caché, les poids récurrents), et `Why` (caché vers sortie)—afin de maintenir une dynamique d'entraînement stable. La forme spécifique dans votre code utilise une distribution gaussienne (normale) mise à l'échelle par `sqrt(1 / fan_in)`, où `fan_in` est le nombre de neurones d'entrée de cette couche. Cela maintient la variance des poids autour de `1 / fan_in`, garantissant que les signaux entrants ne soient pas amplifiés ou réduits de manière trop agressive.

Voici pourquoi c'est crucial pour les RNN, et pourquoi un simple tirage aléatoire uniforme depuis [0, 1] causerait des problèmes :

#### 1. **Préserver la variance du signal à travers les couches et les pas de temps**
   - Dans les réseaux feedforward, Xavier aide à maintenir la *variance des activations* à peu près constante pendant la propagation des signaux (et des gradients en sens inverse). Sans cela, les couches profondes pourraient voir leurs activations exploser (devenir énormes) ou disparaître (tomber proches de zéro), rendant l'entraînement impossible.
   - Les RNN sont comme des réseaux "profonds" *déroulés dans le temps* : Le poids récurrent `Whh` multiplie l'état caché à chaque pas de temps, créant une chaîne de multiplications (par exemple, pour une longueur de séquence *T*, c'est comme *T* couches de profondeur). Si les poids dans `Whh` ont une variance >1, les gradients explosent exponentiellement en remontant (mauvais pour les longues séquences). Si elle est <1, ils disparaissent.
   - La mise à l'échelle de Xavier (par exemple, `* sqrt(1. / hidden_size)` pour `Whh`) garantit que la variance attendue de l'état caché reste ~1, évitant ce problème. Pour une initialisation uniforme [0,1] :
     - Moyenne ~0.5 (biaisée positivement, causant des dérives).
     - Variance ~1/12 ≈ 0.083—trop petite pour une grande `hidden_size` (par exemple, 512), conduisant à une disparition rapide des signaux.

#### 2. **S'adapter aux dimensions des couches**
   - Xavier prend en compte le *fan_in* (entrées de la couche) et parfois le *fan_out* (sorties). Pour `Wxh`, la mise à l'échelle par `sqrt(1 / input_size)` normalise en fonction de la taille du vocabulaire ou des dimensions de plongement. Pour `Whh`, c'est basé sur `hidden_size` pour correspondre à la boucle récurrente.
   - [0,1] ignore les dimensions : Dans une grande couche cachée (par exemple, 1000 unités), sommer de nombreuses entrées [0,1] sans mise à l'échelle submergerait la couche suivante. Dans les petites couches, cela causerait un sous-débit.

#### 3. **Flux de gradient dans la rétropropagation dans le temps (BPTT)**
   - L'entraînement des RNN utilise la BPTT, où les gradients remontent sur *T* pas de temps. Une mauvaise initialisation mène au "problème du gradient qui disparaît" (commun dans les RNN simples, raison pour laquelle les LSTM/GRU existent). Xavier atténue ceci en commençant avec des magnitudes équilibrées.
   - Des études empiriques (par exemple, l'article original de Glorot & Bengio) montrent que Xavier réduit le nombre d'époques nécessaires à la convergence par un facteur de 2 à 10x dans les réseaux profonds/récurrents.

#### Alternatives et quand [0,1] pourrait "fonctionner"
- [0,1] pourrait "fonctionner" pour des modèles jouets minuscules (par exemple, monocouche, séquences courtes) mais échoue à grande échelle—pensez à des pertes qui explosent ou des NaNs.
- Ajustements modernes : Initialisation He (pour les ReLU, mise à l'échelle par `sqrt(2 / fan_in)`) ou initialisation orthogonale (pour les RNN, préserve exactement les normes). Mais Xavier est une valeur par défaut sûre pour les activations sigmoïde/tanh courantes dans les RNN.

En bref, Xavier concerne avant tout la *stabilité* : Il fixe les poids petits-mais-pas-trop-petits, conscients des dimensions, pour laisser les gradients circuler librement. L'aléatoire [0,1] est trop grossier—comme mettre le pied au plancher sans équilibrer les pneus.

Pour approfondir :  
[Understanding the Difficulty of Training Deep Feedforward Neural Networks](http://proceedings.mlr.press/v9/glorot10a/glorot10a.pdf) (Glorot & Bengio, 2010)  
[Recurrent Neural Network Regularization](https://arxiv.org/abs/1409.2329) (Zaremba et al., sur les problèmes d'initialisation des RNN)