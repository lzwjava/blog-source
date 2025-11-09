---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Tester la généralisation avec des éléments inédits
translated: true
type: note
---

Lors de sa conférence NeurIPS 2024 pour le prix Test of Time, portant sur son article de 2014 « Sequence to Sequence Learning with Neural Networks » (et sur des travaux antérieurs connexes comme sa thèse de doctorat sur la modélisation du langage par RNN), Ilya Sutskever a réfléchi aux premiers efforts pour construire des modèles de langage neuronaux généralisants. Un défi clé était de s'assurer que les modèles ne se contentaient pas de mémoriser les données d'entraînement mais pouvaient traiter de nouvelles entrées—c'est-à-dire, éviter l'overfitting.

La « méthode naïve » spécifique qu'il a mentionnée pour détecter cela consiste à tester le modèle sur **des mots ou des n-grammes (séquences de plusieurs mots) invisibles, non présents dans le corpus d'entraînement (souvent appelé la « base de données »)**.

### Pourquoi cette approche ?
- **Risque d'overfitting dans les premiers modèles de langage** : Les modèles de base simples comme les modèles n-grammes (par exemple, les bigrammes ou trigrammes) « surapprennent » souvent en ne prédisant de manière fluide que si la séquence exacte apparaissait plusieurs fois lors de l'entraînement. Ils attribuent une probabilité proche de zéro à toute nouveauté, échouant à généraliser.
- **Test de détection naïve** : Pour vérifier une véritable généralisation (et non un surapprentissage), entraînez le modèle sur un ensemble de validation/test retenu, conçu avec des éléments « invisibles » délibérés :
  - Remplacez des phrases courantes par des phrases inventées mais plausibles (par exemple, dans sa thèse, tester la complétion de phrase sur une fausse citation comme « (ABC et al., 2003) »—une chaîne que le modèle n'avait jamais rencontrée en raison de sa capitalisation non naturelle et de son nom d'auteur).
  - Mesurez si le modèle attribue des probabilités raisonnables, génère des complétions cohérentes ou maintient des scores de perplexité/BLEU bas malgré la nouveauté.
- Si le modèle échoue (par exemple, perplexité élevée ou sortie incohérente) sur ces éléments invisibles mais excelle sur les données d'entraînement vues, il surapprend (il mémorise les spécificités plutôt que d'apprendre des motifs). S'il réussit, il généralise via des représentations apprises (par exemple, les états LSTM capturant la syntaxe/la sémantique).

### Exemples tirés de ses travaux
- **Dans l'article seq2seq (2014)** : Ils ont utilisé un vocabulaire fixe (80 000 mots français, 160 000 mots anglais), en remplaçant les mots hors vocabulaire (OOV) par « UNK ». Pour détecter les problèmes de généralisation, ils ont pénalisé les scores BLEU pour les occurrences OOV et ont tracé les performances par rapport au « rang de fréquence moyen des mots » (plus le mot est rare, plus il est similaire à un mot invisible). Le LSTM gérait bien les mots rares/invisibles sans dégradation, contrairement aux modèles de base.
- **Dans sa thèse de doctorat (2013, sur la modélisation du langage par RNN)** : Pour la complétion de phrase structurée, ils ont testé sur des chaînes entièrement nouvelles comme « (ABC et al., 2003) » (invisible lors de l'entraînement en raison de sa rareté). Le RNN multiplicatif (MRNN) généralisait de manière robuste (par exemple, en prédisant correctement l'année/le contexte), tandis que les modèles de base n-grammes ne le pouvaient pas à moins que des correspondances exactes n'existent—mettant en évidence leur surapprentissage.

Ce test de « vérification des mots/n-grammes invisibles » était une heuristique simple et précoce, avant les techniques avancées comme le dropout ou les courbes de validation. Sutskever a noté dans sa conférence comment de telles idées ont conduit à la mise à l'échelle vers les LLM modernes, où la généralisation sur de vastes données invisibles reste fondamentale.

[Sequence to Sequence Learning with Neural Networks (PDF arXiv)](https://arxiv.org/pdf/1409.3215.pdf)
[Thèse de doctorat d'Ilya Sutskever (PDF)](https://www.cs.utoronto.ca/~ilya/pubs/ilya_sutskever_phd_thesis.pdf)
[Vidéo de la conférence d'Ilya Sutskever à NeurIPS 2024](https://www.youtube.com/watch?v=YD-9NG1Ke5Y)