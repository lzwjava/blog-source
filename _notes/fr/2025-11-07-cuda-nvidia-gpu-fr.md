---
audio: false
generated: true
image: false
lang: fr
layout: post
model: anthropic/claude-4.5-sonnet
title: CUDA nécessite un GPU NVIDIA
translated: true
type: note
---

La raison pour laquelle le GPU de votre Lenovo XiaoXin ne peut pas être utilisé avec CUDA est simple : **CUDA est une technologie propriétaire de NVIDIA qui fonctionne uniquement avec les GPU NVIDIA**.

Votre système dispose d'un GPU intégré **Intel UHD Graphics (Alder Lake-P GT1)**, qui est un processeur graphique d'Intel. CUDA (Compute Unified Device Architecture) est exclusivement conçu pour les cartes graphiques NVIDIA.

## Vos options pour le calcul GPU sur les graphiques Intel :

1. **Intel oneAPI / SYCL**
   - L'équivalent d'Intel à CUDA
   - Fonctionne avec les GPU Intel (y compris votre UHD Graphics)
   - Multi-plateforme et peut cibler plusieurs backends matériels

2. **OpenCL**
   - Standard ouvert pour la programmation parallèle
   - Pris en charge par les GPU Intel
   - Plus largement compatible mais moins optimisé que les solutions spécifiques aux fabricants

3. **Intel Extension for PyTorch**
   - Si vous faites du machine learning/deep learning
   - Optimisé pour le matériel Intel (CPU et GPU)

## Pourquoi CUDA est indiqué comme non détecté :

Le script signale correctement "CUDA/NVIDIA drivers not detected" car :
- Aucun GPU NVIDIA n'est présent dans votre système
- Aucun pilote NVIDIA n'est installé
- La boîte à outils CUDA (si elle est installée) n'a rien sur quoi s'exécuter

Si vous avez spécifiquement besoin de CUDA pour certains logiciels ou frameworks, vous auriez besoin d'un ordinateur portable avec un GPU discret NVIDIA (comme les cartes GeForce RTX, GTX, ou les cartes professionnelles Quadro/A-series).