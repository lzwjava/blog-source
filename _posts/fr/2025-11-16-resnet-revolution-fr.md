---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: La révolution ResNet dans l'apprentissage profond
translated: true
type: note
---

ResNet (Residual Network) est l'une des avancées les plus importantes dans l'histoire du deep learning. Il a été introduit en 2015 par Kaiming He et al. de Microsoft Research et a remporté la compétition ImageNet cette année-là avec un taux d'erreur top-5 stupéfiant de seulement 3,57 % (meilleur que les performances humaines de l'époque).

Voici pourquoi ResNet est devenu si important :

1.  **Il a résolu le « problème de dégradation » (gradients disparaissants/explosifs dans les réseaux très profonds)**
    Avant ResNet, les gens pensaient que « si 20 couches fonctionnent bien, 56 couches devraient fonctionner encore mieux ». En pratique, empiler plus de couches rendait la précision pire — non pas à cause du surapprentissage, mais parce que l'optimisation elle-même devenait plus difficile. ResNet a prouvé que l'on pouvait entraîner des réseaux de 100+ couches (ils ont montré 152 couches, plus tard les gens sont allés à 1000+ couches) et obtenir tout de même de meilleures performances.

2.  **Blocs résiduels + connexions résiduelles (l'idée clé)**
    Au lieu de demander à la couche d'apprendre H(x) directement, ResNet apprend le résidu F(x) = H(x) − x, donc le bloc calcule x + F(x).
    Mathématiquement :
    y = F(x, {W_i}) + x
    Cette « connexion directe d'identité » permet aux gradients de circuler directement à travers le réseau via les connexions résiduelles, rendant possible l'entraînement de réseaux extrêmement profonds.

3.  **Impact pratique immédiat et massif**
    - Est devenu l'épine dorsale de presque tous les modèles de vision state-of-the-art de 2016 à ~2020 (et est encore largement utilisé aujourd'hui).
    - Utilisé dans la détection d'objets (Faster R-CNN + ResNet), la segmentation (DeepLab, Mask R-CNN), les modèles génératifs (StyleGAN, etc.), la vidéo, l'imagerie médicale, etc.
    - Des variantes comme ResNet-50, ResNet-101, ResNeXt, Wide ResNet et ResNet-RS sont encore des lignes de base standard en 2025.

4.  **A permis toute l'ère du « deep learning devient vraiment profond »**
    Avant ResNet : les meilleurs modèles ImageNet avaient ~20–30 couches (VGG, GoogLeNet).
    Après ResNet : 100–1000+ couches sont devenues normales. Cette profondeur était cruciale pour apprendre des caractéristiques plus riches.

5.  **Idée extrêmement simple, mais transformative**
    Le document est célèbre pour sa clarté et n'ajoute qu'une seule astuce ingénieuse (connexions résiduelles + addition élément par élément). Pas de nouvelles activations fantaisistes, pas de nouvelles fonctions de perte — juste une perspicacité architecturale.

En bref : ResNet a prouvé que « plus profond est meilleur » peut vraiment fonctionner si l'on conçoit l'architecture correctement, et il est devenu le point de départ par défaut pour presque tous les modèles de vision par ordinateur de la décennie suivante.

Même aujourd'hui en 2025, alors que les modèles basés sur les Transformers et ConvNeXt/ViT dominent les classements, ResNet-50 reste l'épine dorsale de référence la plus courante car il est rapide, bien compris et extrêmement fiable.

Article (toujours digne d'être lu) :
[Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385)