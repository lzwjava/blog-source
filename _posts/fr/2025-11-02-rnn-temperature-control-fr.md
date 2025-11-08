---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Contrôle de la température de génération de texte par RNN
translated: true
type: note
---

### Comprendre la température dans l'échantillonnage des RNN

Dans les réseaux de neurones récurrents (RNN) pour la génération de texte—comme ceux qu'Andrej Karpathy explore dans son célèbre article de blog sur les modèles de langage au niveau des caractères—la température est un hyperparamètre qui ajuste le caractère "aléatoire" ou "prévisible" du texte généré. Elle est appliquée durant l'étape d'échantillonnage, où le RNN prédit le caractère (ou token) suivant en se basant sur les précédents. Sans contrôle de la température, la génération peut être trop rigide (toujours choisir le caractère suivant le plus probable, menant à des boucles ennuyeuses) ou trop désordonnée (aléatoire pur). La température trouve un équilibre en adoucissant la distribution de probabilité du modèle sur les caractères suivants possibles.

#### Les Mathématiques Rapides Derrière le Concept
Le RNN produit des *logits* (scores bruts, non normalisés) pour chaque caractère suivant possible. Ceux-ci sont transformés en probabilités en utilisant la fonction softmax :

\\[
p_i = \frac{\exp(\text{logit}_i / T)}{\sum_j \exp(\text{logit}_j / T)}
\\]

- \\(T\\) est la température (typiquement entre 0,1 et 2,0).
- Quand \\(T = 1\\), c'est le softmax standard : les probabilités reflètent la confiance "naturelle" du modèle.
- Vous *échantillonnez* ensuite le caractère suivant à partir de cette distribution (par exemple, via un échantillonnage multinomial) au lieu de toujours choisir celui avec la probabilité la plus élevée (décodage glouton).

Cet échantillonnage se produit de manière itérative : le caractère choisi est réinjecté en entrée, on prédit le suivant, et on répète pour générer une séquence.

#### Basse Température : Répétitif mais Sûr
- **Effet** : \\(T < 1\\) (par exemple, 0,5 ou proche de 0) *accentue* la distribution. Les prédictions à haute confiance obtiennent des probabilités encore plus élevées, tandis que les faibles sont écrasées vers zéro.
- **Résultat** : Le texte reste "sûr" et cohérent mais devient rapidement répétitif. Le modèle s'en tient aux chemins les plus probables, comme s'il était piégé dans une boucle.
- **Exemple de l'article de Karpathy** (générant des essais de style Paul Graham) : À une température très basse, il produit quelque chose comme :
  > “is that they were all the same thing that was a startup is that they were all the same thing that was a startup is that they were all the same thing that was a startup is that they were all the same”

  C'est confiant et grammaticalement correct, mais manque de créativité—on pense à des échos infinis des données d'entraînement.

#### Haute Température : Créatif mais Erratique
- **Effet** : \\(T > 1\\) (par exemple, 1,5 ou 2,0) *aplanit* la distribution. Les probabilités deviennent plus uniformes, donnant aux outsiders (caractères moins probables) une meilleure chance.
- **Résultat** : Un texte plus diversifié et inventif, mais il verse dans le non-sens, les fautes d'orthographe ou les digressions sauvages. Le modèle explore des chemins rares, ce qui peut susciter de l'originalité au prix de la cohérence.
- **Exemple de Karpathy** : Des températures plus élevées produisent des essais variés avec des formulations fraîches, mais "au prix de plus d'erreurs (par exemple, des fautes d'orthographe, etc.)". C'est comme si le RNN brainstormait librement—amusant pour la poésie ou la science-fiction, risqué pour l'écriture factuelle.

#### Pourquoi C'est Important dans les RNN
Les RNN (ou les LSTMs dans la configuration de Karpathy) sont autorégressifs : chaque prédiction s'appuie sur la précédente, donc de petits biais dans l'échantillonnage s'amplifient sur de longues séquences. La température vous permet d'ajuster l'exploration contre l'exploitation :
- Utilisez un faible \\(T\\) pour un texte fiable et conforme (par exemple, des descriptions de produits).
- Augmentez-la pour le brainstorming ou la génération artistique (par exemple, des histoires surréalistes).
- Expérimentez dans le code : le dépôt de RNN vanilla de Karpathy inclut un curseur de température—essayez-le sur des échantillons de Shakespeare pour voir le passage de sonnets fades à des vers chaotiques.

En substance, la température n'"apprend" rien de nouveau ; elle règle simplement le niveau de créativité du RNN pendant l'inférence. Une valeur basse le garde calme et prévisible ; une valeur élevée libère le chaos.

[The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)