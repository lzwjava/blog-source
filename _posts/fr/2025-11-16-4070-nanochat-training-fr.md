---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Estimation du temps d'entraînement du RTX 4070 NanoChat
translated: true
type: note
---

Pour estimer le temps d'entraînement pour nanochat d32 (1,9 milliard de paramètres, 38 milliards de tokens) sur une seule GPU NVIDIA RTX 4070, nous pouvons effectuer un calcul à partir de la configuration d'origine : 33 heures sur un nœud avec 8x H100.

D'après les comparaisons de performance pour les charges de travail basées sur des transformers (pertinentes pour l'entraînement de LLM), une GPU H100 SXM est environ 8 à 9 fois plus rapide qu'une RTX 4070 dans les tâches intensives en calcul comme les multiplications matricielles en précision FP16/BF16. Ceci prend en compte les différences de débit des tensor cores, de la bande passante mémoire et de l'utilisation effective.

L'entraînement original utilisait 8 H100, ce qui équivaut à environ 264 heures-H100. Passer à une seule RTX 4070 prendrait environ 2 100 à 2 400 heures, soit environ 88 à 100 jours de fonctionnement continu.

Ceci suppose que le script d'entraînement (comme run1000.sh) peut tenir et s'exécuter sur les 12 Go de VRAM de la 4070, éventuellement avec des ajustements comme des tailles de lot plus petites, du gradient checkpointing, ou l'offload de l'optimiseur pour éviter les problèmes de mémoire. En pratique, l'entraînement pourrait être limité par la mémoire ou nécessiter des ajustements, augmentant potentiellement le temps en raison d'une efficacité moindre sur du matériel grand public. La consommation électrique serait d'environ 200W, gardant les coûts d'électricité bas par rapport au cloud.

Références :  
[Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/)  
[GPU Benchmarks NVIDIA H100 NVL (PCIe) vs. NVIDIA RTX 4090 vs. NVIDIA RTX 4080](https://bizon-tech.com/gpu-benchmarks/NVIDIA-H100-NVL-%28PCIe%29-vs-NVIDIA-RTX-4090-vs-NVIDIA-RTX-4080/632vs637vs638)  
[NVIDIA H100 PCIe vs SXM: Performance and Use Cases Compared](https://www.hyperstack.cloud/technical-resources/performance-benchmarks/comparing-nvidia-h100-pcie-vs-sxm-performance-use-cases-and-more)