---
audio: false
generated: true
image: false
lang: fr
layout: post
title: 'JFIF : JPEG avec en-tête'
translated: true
type: note
---

JFIF signifie **JPEG File Interchange Format** — c'est essentiellement une manière de conditionner les données d'image compressées en JPEG afin que différents logiciels et appareils puissent les échanger de manière fiable.

Voici l'essentiel :

* **Objectif** – JFIF a été conçu au début des années 1990 pour standardiser la façon dont les images JPEG sont stockées et transférées, car les données JPEG brutes seules ne définissaient pas des détails importants comme la densité de pixels ou l'espace colorimétrique.
* **Extension de fichier** – Généralement `.jfif`, mais de nombreuses images JPEG (`.jpg` / `.jpeg`) sont en réalité stockées en interne au format JFIF.
* **Structure** –

  1. **Données d'image encodées en JPEG** (les pixels compressés)
  2. **Segment de marqueur APP0 JFIF** (métadonnées comme la résolution, le rapport d'aspect et l'espace colorimétrique)
* **Métadonnées** – Inclut des informations telles que le DPI (points par pouce), une vignette de l'image et des indications sur le rapport d'aspect.
* **Compatibilité** – JFIF est fondamentalement un sous-ensemble de la norme JPEG plus large, donc la plupart des visionneuses d'images, navigateurs et appareils photo peuvent le lire sans problème.

En bref :
Un fichier `.jfif` est simplement une image JPEG avec un petit en-tête standardisé qui facilite son échange entre les systèmes sans confusion concernant la résolution ou l'interprétation des couleurs.

Si vous le souhaitez, je peux également expliquer **comment JFIF diffère des JPEG EXIF** produits par les appareils photo, car c'est une source fréquente de confusion. Souhaitez-vous que j'aborde ce sujet ?