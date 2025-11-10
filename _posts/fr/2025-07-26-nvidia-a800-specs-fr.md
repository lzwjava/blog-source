---
audio: false
generated: true
lang: fr
layout: post
title: 'NVIDIA A800 GPU : variante A100'
translated: true
type: note
---

Le NVIDIA A800 est une unité de traitement graphique (GPU) de qualité professionnelle développée par NVIDIA, principalement conçue pour le calcul haute performance (HPC), l'intelligence artificielle (IA), la science des données et les flux de travail pour stations de travail. Il est basé sur l'architecture NVIDIA Ampere et utilise le processeur graphique GA100, fabriqué selon un procédé 7 nm. L'A800 a été introduit en novembre 2022 en tant que variante du GPU NVIDIA A100, spécifiquement adaptée pour se conformer aux restrictions d'exportation américaines sur les puces IA avancées vers certaines régions, comme la Chine. La différence principale avec l'A100 est une vitesse d'interconnexion NVLink réduite (400 Go/s sur l'A800 contre 600 Go/s sur l'A100), ce qui impacte la mise à l'échelle multi-GPU mais maintient des performances de base similaires pour les tâches mono-GPU.

### Spécifications Clés (pour la variante A800 PCIe 40GB, à titre d'exemple) :
- **Cœurs CUDA** : 6 912
- **Cœurs Tensor** : 432 (troisième génération)
- **Mémoire** : 40 GB HBM2 (mémoire à haut débit) ; certaines variantes offrent 80 GB
- **Bande passante mémoire** : Jusqu'à 1,55 To/s
- **Performances** :
  - Simple précision (FP32) : Jusqu'à 19,5 TFLOPS
  - Double précision (FP64) : Jusqu'à 9,7 TFLOPS
  - Performance Tensor (TF32) : Jusqu'à 312 TFLOPS
- **Interface** : PCIe 4.0 x16
- **Consommation d'énergie** : Environ 250-300 W TDP (thermal design power)
- **Facteur de forme** : Disponible en versions refroidissement passif ou actif pour serveurs et stations de travail

L'A800 excelle dans l'accélération de tâches exigeantes comme l'entraînement de modèles de machine learning, l'inférence, les simulations scientifiques et la visualisation. Dans les benchmarks, ses performances se situent souvent entre 70 et 100 % de celles de l'A100, selon la charge de travail—elle est quasiment identique en calcul simple et double précision, mais est à la traîne dans les scénarios nécessitant une communication multi-GPU à haute vitesse en raison du NVLink limité.

Les variantes incluent l'A800 40GB Active (pour stations de travail avec refroidissement actif) et des modèles orientés serveur comme l'A800 PCIe 80GB. Il n'est pas destiné au gaming grand public mais à un usage professionnel et en entreprise.

[Carte Graphique NVIDIA A800 40GB Active](https://www.nvidia.com/en-us/design-visualization/a800/)  
[Spécifications NVIDIA A800 PCIe 40 GB](https://www.techpowerup.com/gpu-specs/a800-pcie-40-gb.c3964)  
[NVIDIA présente le GPU A800 pour remplacer l'A100 interdit en Chine](https://analyticsdrift.com/nvidia-introduces-a800-gpu-chips-to-replace-banned-a100-chips-for-china/)  
[ThinkSystem NVIDIA A800 PCIe 4.0 GPUs](https://lenovopress.lenovo.com/lp1813-thinksystem-nvidia-a800-pcie-gpu)  
[Puces IA Nvidia : A100 A800 H100 H800 B200](https://www.fibermall.com/blog/nvidia-ai-chip.htm)