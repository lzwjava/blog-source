---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: AMD mène la prise en charge des GPU open source
translated: true
type: note
---

### AMD vs. NVIDIA : Engagement Open Source

Oui, AMD est généralement considérée comme plus open source que NVIDIA, particulièrement dans le contexte des pilotes GPU, des piles logicielles et du support de l'écosystème. Cela découle de l'accent de longue date d'AMD sur des solutions entièrement open source, surtout pour Linux, où ses pilotes sont matures, intégrés au noyau et pilotés par la communauté. NVIDIA, bien qu'ayant fait des progrès vers l'ouverture ces dernières années, repose encore largement sur des composants propriétaires pour les performances et fonctionnalités complètes. Ci-dessous, je vais détailler par domaines clés.

#### Pilotes GPU
- **AMD** : Le pilote AMDGPU est entièrement open source et est celui par défaut pour les GPU Radeon depuis 2016. Il est inclus directement dans le noyau Linux (plus de 5,9 millions de lignes de code mi-2025), offrant un support prêt à l'emploi pour le rendu, le calcul et Vulkan sans avoir besoin de binaires propriétaires. Cela le rend transparent pour les utilisateurs et développeurs Linux.
- **NVIDIA** : Les pilotes traditionnels de NVIDIA sont propriétaires, nécessitant une installation manuelle pour des performances optimales. Ils ont ouvert le code des modules du noyau depuis 2022 (via le projet `nvidia-open`), mais les composants de l'espace utilisateur restent fermés. Leurs efforts plus récents, comme le pilote NOVA basé sur Rust et les améliorations de Nouveau, sont encore expérimentaux et manquent de parité fonctionnelle complète (par exemple, pas de support complet de DLSS ou de ray tracing avancé dans les variantes ouvertes fin 2025).

**Avantage** : AMD l'emporte pour la fiabilité et l'intégration dans les environnements ouverts comme Linux.

#### Piles logicielles pour le Calcul et l'IA
- **AMD** : ROCm (Radeon Open Compute) est entièrement open source, supportant les frameworks de machine learning comme PyTorch et TensorFlow sur les GPU AMD. Il est conçu pour la portabilité entre le matériel et les OS, bien qu'il ait historiquement accusé un retard en maturité de l'écosystème par rapport aux concurrents.
- **NVIDIA** : CUDA est la référence pour le calcul accéléré par GPU mais est propriétaire et exclusif à NVIDIA. Des alternatives comme OpenCL existent, mais elles sont moins optimisées. NVIDIA a ouvert le code de certains composants (par exemple, des sous-ensembles de cuDNN), mais le cœur de la pile reste fermé, limitant l'interopérabilité.

**Avantage** : AMD pour l'ouverture, mais NVIDIA domine avec des outils aboutis et riches en fonctionnalités — souvent au prix d'un verrouillage fournisseur.

#### Écosystème et Communauté au sens large
- AMD contribue activement à des projets open source comme Mesa (pour les graphismes) et a un meilleur support de Wayland prêt à l'emploi. Leur approche favorise les contributions de la communauté, réduisant les maux de tête pour les utilisateurs de distributions open source.
- Les progrès de NVIDIA incluent des correctifs open source pour vGPU et une meilleure fiabilité de Nouveau en 2025, mais des problèmes comme les binaires de micrologiciel et le support Vulkan incomplet persistent. Ils pratiquent plus "l'open-washing" qu'un engagement total, selon les retours de la communauté.

En résumé, si "plus open source" signifie un code accessible et modifiable sans dépendances propriétaires, AMD mène — particulièrement pour le gaming Linux, le développement et l'inférence IA. NVIDIA excelle en performances brutes et fonctionnalités propriétaires mais est à la traîne en transparence. Votre choix dépend des priorités : ouverture (AMD) vs domination de l'écosystème (NVIDIA).

#### Références
- [AMD vs Nvidia GPU: Which is better on Linux? (Reddit, 2023)](https://www.reddit.com/r/linux_gaming/comments/18nv50w/amd_vs_nvidia_gpu_which_is_better_on_linux_updated/)
- [NVIDIA vs AMD on Linux: Which GPU Should You Choose? (Linuxiac, 2025)](https://linuxiac.com/nvidia-vs-amd-gpus-on-linux/)
- [Open-Source NVIDIA Linux Driver Usage About To Become Much More Reliable (Phoronix, 2025)](https://www.phoronix.com/news/Nouveau-More-Reliable-Fix)
- [AMD Kernel Graphics Driver Exceeds 5.9 Million Lines In Linux 6.16 (Phoronix, 2025)](https://www.phoronix.com/news/Linux-6.16-AMDGPU-Driver-Size)
- [NVIDIA Posts Latest Linux Driver Patches For Open-Source vGPU Support (Phoronix, 2025)](https://www.phoronix.com/news/NVIDIA-vGPU-RFC-v2)