---
audio: false
generated: true
lang: fr
layout: post
title: Transformateur
translated: true
type: note
---

Le **Transformer** est une architecture de réseau neuronal révolutionnaire qui est devenue le fondement de la plupart des modèles de langage de grande taille (LLM) modernes. Elle a été introduite dans le document séminal de 2017 "Attention Is All You Need" par Vaswani et al. et a depuis fondamentalement changé le domaine du traitement du langage naturel (NLP).

Contrairement aux architectures dominantes précédentes comme les réseaux neuronaux récurrents (RNN), qui traitent les données séquentielles étape par étape, le Transformer traite des séquences d'entrée entières **en parallèle**. Cette différence clé permet des améliorations significatives de la vitesse d'entraînement et la capacité de capturer des dépendances à longue portée dans le texte.

Voici une analyse approfondie des composants et concepts clés de l'architecture Transformer dans le contexte des LLMs :

**1. Idée centrale : Mécanisme d'attention**

L'innovation centrale du Transformer est le **mécanisme d'attention**, en particulier l'**auto-attention**. Ce mécanisme permet au modèle de pondérer l'importance des différents mots (ou tokens) dans la séquence d'entrée lors du traitement d'un mot spécifique. Au lieu de se fier uniquement aux mots immédiatement précédents (comme les RNN), l'auto-attention permet au modèle de considérer l'ensemble du contexte pour comprendre le sens et les relations entre les mots.

Imaginez-le ainsi : lorsque vous lisez une phrase, vous ne traitez pas chaque mot de manière isolée. Votre cerveau considère simultanément tous les mots pour comprendre le sens global et la contribution de chaque mot à celui-ci. Le mécanisme d'auto-attention imite ce comportement.

**Comment fonctionne l'auto-attention (version simplifiée) :**

Pour chaque mot de la séquence d'entrée, le Transformer calcule trois vecteurs :

* **Requête (Q) :** Représente ce que le mot actuel "recherche" dans les autres mots.
* **Clé (K) :** Représente l'information que chaque autre mot "contient".
* **Valeur (V) :** Représente l'information réelle que chaque autre mot détient et qui pourrait être pertinente.

Le mécanisme d'auto-attention effectue ensuite les étapes suivantes :

1.  **Calculer les scores d'attention :** Le produit scalaire entre le vecteur Requête d'un mot et le vecteur Clé de chaque autre mot de la séquence est calculé. Ces scores indiquent à quel point l'information de chaque autre mot est pertinente pour le mot actuel.
2.  **Mettre à l'échelle les scores :** Les scores sont divisés par la racine carrée de la dimension des vecteurs Clé (`sqrt(d_k)`). Cette mise à l'échelle aide à stabiliser les gradients pendant l'entraînement.
3.  **Appliquer Softmax :** Les scores mis à l'échelle sont passés par une fonction softmax, qui les normalise en probabilités entre 0 et 1. Ces probabilités représentent les **poids d'attention** – c'est-à-dire la quantité d'"attention" que le mot actuel doit accorder à chacun des autres mots.
4.  **Calculer les valeurs pondérées :** Le vecteur Valeur de chaque mot est multiplié par son poids d'attention correspondant.
5.  **Additionner les valeurs pondérées :** Les vecteurs Valeur pondérés sont additionnés pour produire le **vecteur de sortie** pour le mot actuel. Ce vecteur de sortie contient désormais des informations provenant de tous les autres mots pertinents de la séquence d'entrée, pondérées par leur importance.

**2. Attention multi-têtes**

Pour améliorer davantage la capacité du modèle à capturer différents types de relations, le Transformer utilise l'**attention multi-têtes**. Au lieu d'effectuer le mécanisme d'auto-attention une seule fois, il le fait plusieurs fois en parallèle avec différents ensembles de matrices de poids Requête, Clé et Valeur. Chaque "tête" apprend à se concentrer sur différents aspects des relations entre les mots (par exemple, les dépendances grammaticales, les connexions sémantiques). Les sorties de toutes les têtes d'attention sont ensuite concaténées et transformées linéairement pour produire la sortie finale de la couche d'attention multi-têtes.

**3. Encodage positionnel**

Étant donné que le Transformer traite tous les mots en parallèle, il perd l'information concernant l'**ordre** des mots dans la séquence. Pour résoudre ce problème, un **encodage positionnel** est ajouté aux plongements d'entrée. Ces encodages sont des vecteurs qui représentent la position de chaque mot dans la séquence. Ce sont généralement des motifs fixes (par exemple, des fonctions sinusoïdales) ou des plongements appris. En ajoutant des encodages positionnels, le Transformer peut comprendre la nature séquentielle du langage.

**4. Empilements d'encodeur et de décodeur**

L'architecture Transformer se compose généralement de deux parties principales : un **encodeur** et un **décodeur**, tous deux constitués de multiples couches identiques empilées les unes sur les autres.

* **Encodeur :** Le rôle de l'encodeur est de traiter la séquence d'entrée et d'en créer une représentation riche. Chaque couche d'encodeur contient typiquement :
    * Une sous-couche d'**auto-attention multi-têtes**.
    * Une sous-couche de **réseau neuronal feed-forward**.
    * Des **connexions résiduelles** autour de chaque sous-couche, suivies d'une **normalisation de couche**. Les connexions résiduelles aident au flux des gradients pendant l'entraînement, et la normalisation de couche stabilise les activations.

* **Décodeur :** Le rôle du décodeur est de générer la séquence de sortie (par exemple, en traduction automatique ou en génération de texte). Chaque couche de décodeur contient typiquement :
    * Une sous-couche d'**auto-attention multi-têtes masquée**. Le "masquage" empêche le décodeur de regarder les tokens futurs dans la séquence cible pendant l'entraînement, garantissant qu'il n'utilise que les tokens précédemment générés pour prédire le suivant.
    * Une sous-couche d'**attention multi-têtes** qui se concentre sur la sortie de l'encodeur. Cela permet au décodeur de se concentrer sur les parties pertinentes de la séquence d'entrée lors de la génération de la sortie.
    * Une sous-couche de **réseau neuronal feed-forward**.
    * Des **connexions résiduelles** et une **normalisation de couche** similaires à l'encodeur.

**5. Réseaux Feed-Forward**

Chaque couche d'encodeur et de décodeur contient un réseau neuronal feed-forward (FFN). Ce réseau est appliqué à chaque token indépendamment et aide à traiter davantage les représentations apprises par les mécanismes d'attention. Il se compose généralement de deux transformations linéaires avec une fonction d'activation non linéaire (par exemple, ReLU) entre les deux.

**Comment les Transformers sont utilisés dans les LLMs :**

Les LLM sont principalement basés sur l'architecture Transformer **décodeur uniquement** (comme les modèles GPT) ou l'architecture **encodeur-décodeur** (comme T5).

* **Modèles décodeur uniquement :** Ces modèles sont entraînés à prédire le token suivant dans une séquence étant donné les tokens précédents. Ils empilent plusieurs couches de décodeur. L'invite d'entrée est passée à travers les couches, et la couche finale prédit la distribution de probabilité sur le vocabulaire pour le token suivant. En échantillonnant de manière autorégressive à partir de cette distribution, le modèle peut générer un texte cohérent et contextuellement pertinent.

* **Modèles encodeur-décodeur :** Ces modèles prennent une séquence d'entrée et génèrent une séquence de sortie. Ils utilisent l'architecture complète encodeur-décodeur. L'encodeur traite l'entrée, et le décodeur utilise la sortie de l'encodeur pour générer la séquence cible. Ces modèles sont bien adaptés pour des tâches comme la traduction, la synthèse et la réponse aux questions.

**Comprendre en profondeur la signification :**

L'impact de l'architecture Transformer sur les LLMs est profond :

* **Gestion des dépendances à longue portée :** Le mécanisme d'auto-attention permet au modèle de connecter directement des mots éloignés dans la séquence, surmontant les limitations des RNN pour capturer le contexte à longue portée.
* **Traitement parallèle :** Le traitement de la séquence entière en parallèle réduit considérablement le temps d'entraînement et permet l'utilisation de jeux de données et de modèles beaucoup plus grands.
* **Évolutivité :** L'architecture Transformer s'adapte bien à l'augmentation des données et de la taille des modèles, conduisant au développement de LLM extrêmement puissants avec des milliards, voire des billions de paramètres.
* **Compréhension contextuelle :** Le mécanisme d'attention permet au modèle de comprendre le contexte des mots de manière plus nuancée, conduisant à une meilleure compréhension et génération du langage.
* **Fondement pour l'innovation :** L'architecture Transformer a servi de fondement à de nombreuses avancées et variations, conduisant au paysage diversifié des LLM modernes.

En résumé, l'architecture Transformer, avec son mécanisme d'auto-attention central, ses capacités de traitement parallèle et sa structure encodeur-décodeur (ou ses variations décodeur uniquement), a révolutionné le domaine du NLP et est la force motrice derrière les capacités remarquables des modèles de langage de grande taille modernes.