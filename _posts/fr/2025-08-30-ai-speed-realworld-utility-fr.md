---
audio: false
generated: true
image: false
lang: fr
layout: post
title: L'IA à Grande Vitesse Rencontre l'Utilité Pratique
translated: true
type: note
---

Voici les **points clés** de l'article :

---

### Concept Fondamental

* Les **benchmarks d'IA traditionnels** se concentrent principalement sur la précision/qualité, mais négligent la **vitesse de traitement**, qui est cruciale dans les applications réelles sensibles au temps (par exemple, la conduite autonome, le service client).
* Les métriques de vitesse existantes (TTFT, TPS) sont **centrées sur les tokens** et inadéquates pour un futur IA multi-modal.
* **Nouvelle métrique proposée** : **Intelligence Bandwidth** (Bande Passante Intelligence) — la quantité d'informations utiles qu'une IA peut produire par unité de temps.

---

### Approximations de la Bande Passante Intelligence

1. **Score de benchmark par unité de temps**

   * Utiliser la performance normalisée du benchmark divisée par le temps pris.
   * Plus informatif que les tokens/sec pour les tâches pratiques.

2. **Approche par la théorie de l'information**

   * Mesurer le contenu informationnel de la sortie via les distributions de probabilité.
   * Limité car l'information n'est pas égale à l'utilité et nécessite un accès aux vecteurs de probabilité.

3. **Bits bruts de sortie par seconde**

   * La plus simple, agnostique à la modalité.
   * Mesure les bits/sec de la sortie de l'IA (texte, image, vidéo).
   * Ne mesure pas directement l'utilité, mais fonctionne si appliquée uniquement aux modèles les plus performants.

---

### Contexte Historique

* La vitesse était auparavant ignorée car :

  1. L'IA n'était pas assez avancée pour en avoir besoin.
  2. Les applications étaient étroites et spécifiques à une tâche.
* Avec les **LLM** et l'**IA multi-modale**, une **métrique de vitesse unifiée** est devenue nécessaire.

---

### Implications pour l'Interaction Humain-IA

* Similaire à la **Loi de Moore** et la **Loi de Nielsen**, cette métrique peut révéler des tendances de croissance.
* **Concept de seuil** : une fois que la vitesse de sortie de l'IA dépasse la vitesse de perception humaine (par exemple, la lecture ou l'écoute), l'interaction en temps réel devient possible.
* L'IA dépasse déjà les vitesses de lecture et d'écoute humaines ; la prochaine frontière est **l'intégration d'images et de vidéos en temps réel**.
* Avenir : L'IA pourrait prendre en charge le **raisonnement visuel en temps réel, la conception de type tableau blanc et les environnements virtuels immersifs**.

---

### Expériences & Données

* Mesures à travers les LLM historiques, et les générateurs d'images et de vidéos en utilisant les **bits bruts de sortie/sec**.
* **Observations** :

  * LLM : 0–3 Ko/s.
  * Générateurs d'images : croissance exponentielle.
  * Générateurs de vidéos : actuellement à la traîne mais devraient accélérer.
  * **Gemini 2.5 Flash** est un cas particulier (optimisé pour une faible latence).

---

### Loi de Jin

* **Formulation** : *La bande passante intelligence du meilleur modèle d'IA hébergé public double chaque année.*
* Actuellement menée par les **générateurs d'images** ; la vidéo devrait prendre le relais à mesure que le service s'améliore.
* **Prédictions** :

  1. **L'intégration d'images dans le chat IA** deviendra standard dans 1 an.
  2. **L'interaction vidéo en temps réel** sera réalisable dans environ 3 ans (nécessite une accélération d'environ 8×).

---

### Limites

* La définition de **« l'information utile »** reste non résolue.
* Les données actuelles sont rares, donc l'estimation d'un doublement annuel est incertaine.
* La croissance peut être limitée par l'énergie/l'économie, et pas seulement par le progrès technologique.

---

### Conclusion

* L'évaluation de l'IA doit tenir compte à la fois de **l'exactitude et de la vitesse**, reflétant l'évaluation de l'intelligence humaine.
* La **Bande Passante Intelligence** offre un cadre prédictif pour l'avenir de l'IA, en particulier pour **l'interaction multi-modale en temps réel**.

---

Souhaitez-vous que je crée également une **chronologie visuelle** des prédictions de la Loi de Jin (texte → images → vidéo → environnements immersifs) pour une compréhension plus facile en un coup d'œil ?