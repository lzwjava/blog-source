---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Avancées en classification ImageNet pour 2025
translated: true
type: note
---

L'état de l'art (SOTA) sur ImageNet (spécifiquement le jeu de validation ImageNet-1K pour la classification d'images) a continué de progresser régulièrement depuis les améliorations spectaculaires post-2012. En novembre 2025, les modèles leaders atteignent des précisions top-1 d'environ 91 %, ce qui correspond à un taux d'erreur top-1 de ~9 %. Les précisions top-5 sont encore plus élevées, dépassant typiquement 99 %, pour un taux d'erreur top-5 inférieur à 1 %.

### Principaux modèles SOTA (Top-5 du classement Papers With Code)
Voici un aperçu des meilleurs modèles actuels (affinés sur ImageNet-1K), basé sur la précision top-1. Les précisions top-5 ne sont pas toujours explicitement re-rapportées pour ces modèles très performants (car elles se saturent à des niveaux quasi parfaits), mais un recoupement avec des architectures récentes similaires suggère des erreurs top-5 inférieures à 1 % pour tous :

| Rang | Modèle | Précision Top-1 | Précision Top-5 Est. | Paramètres | Notes |
|------|--------|----------------|---------------------|------------|-------|
| 1 | CoCa (affiné) | 91,0 % (9,0 % d'erreur) | ~99,5 % (<0,5 % d'erreur) | 2,1B | Modèle multimodal image-texte ; excelle en zero-shot (86,3 % top-1) et avec encodeur gelé (90,6 % top-1). |
| 2 | Model Soups (BASIC-L) | 90,98 % (9,02 % d'erreur) | ~99,4 % (<0,6 % d'erreur) | ~1B | Moyenne d'ensemble de modèles affinés pour une robustesse améliorée. |
| 3 | Model Soups (ViT-G/14) | 90,94 % (9,06 % d'erreur) | ~99,4 % (<0,6 % d'erreur) | 1,8B | Basé sur ViT ; forte généralisation sur des données hors distribution. |
| 4 | DaViT-Giant | 90,4 % (9,6 % d'erreur) | ~99,3 % (<0,7 % d'erreur) | 1,4B | ViT à double attention ; entraîné sur 1,5 milliard de paires image-texte. |
| 5 | ConvNeXt V2-Huge | 88,9 % (11,1 % d'erreur) | ~99,0 % (~1,0 % d'erreur) | 660M | Renaissance des CNN avec prétraining par autoencodeur masqué ; efficace pour les appareils edge. |

### Clarification sur le "<3% Aujourd'hui"
- Cela fait référence au **taux d'erreur top-5**, et non au top-1. Les lignes de base pré-2012 (par exemple, les SVM) oscillaient autour de 25 % d'erreur top-5. En 2017 (SENet), il est tombé à ~2,3 %. Les modèles SOTA modernes l'ont poussé en dessous de 1 %, rendant les prédictions top-5 essentiellement fiables pour la plupart des cas d'usage réels.
- L'erreur top-1 reste plus élevée (~9 %) car elle exige que la *précision* supérieure exacte corresponde, ce qui est plus strict et plus sensible aux cas limites comme les images ambiguës.

Le progrès a ralenti ces dernières années en raison de la saturation du jeu de données—les gains proviennent désormais d'un prétraining massif (par exemple sur ImageNet-21K ou des données à l'échelle du web) et de techniques comme l'assemblage de modèles ou la distillation. La performance d'un expert humain est estimée à ~5 % d'erreur top-1 (ou 2-12 % top-5, selon l'étude), donc l'IA a surpassé les humains sur ce benchmark.

[ImageNet Benchmark (Papers With Code)](https://paperswithcode.com/sota/image-classification-on-imagenet)  
[Image Classification: State-of-the-Art Models in 2025 (HiringNet)](https://hiringnet.com/image-classification-state-of-the-art-models-in-2025)  
[CoCa: Contrastive Captioners are Image-Text Foundation Models (arXiv)](https://arxiv.org/abs/2205.01917)