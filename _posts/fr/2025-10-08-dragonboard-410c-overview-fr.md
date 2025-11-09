---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Présentation de l'ordinateur compact DragonBoard 410c
translated: true
type: note
---

La carte Snapdragon 410 fait généralement référence au DragonBoard 410c, un ordinateur monocarte (SBC) compact développé par Qualcomm en tant que plateforme de référence pour l'IoT, les systèmes embarqués et le prototypage. Commercialisé vers 2015, il fait partie de l'écosystème 96Boards et a à peu près la taille d'une carte de crédit. Ses principales caractéristiques sont :

- **Processeur** : Qualcomm Snapdragon 410 (MSM8916/APQ8016), un processeur quadricœur ARM Cortex-A53 cadencé jusqu'à 1,2 GHz.
- **GPU** : Adreno 306 à 450 MHz, prenant en charge la lecture vidéo 1080p et les graphiques de base.
- **Mémoire/Stockage** : 1 Go de RAM LPDDR3 et 8 Go de stockage eMMC (extensible via microSD).
- **Connectivité** : Wi-Fi double bande 802.11ac, Bluetooth 4.1, GPS, USB 2.0, HDMI et broches GPIO pour le matériel.
- **Support OS** : Exécute Linux (par exemple, Ubuntu), Android et Windows 10 IoT Core dès la sortie de boîte.

Il est conçu pour les développeurs construisant des appareils à faible consommation comme les gadgets pour la maison intelligente ou les capteurs industriels, avec un accent particulier sur les fonctionnalités sans fil et l'extensibilité.

### Performances
Le Snapdragon 410 est un SoC d'entrée de gamme du milieu des années 2010, fabriqué en procédé 28nm, ce qui le rend économe en énergie mais dépassé selon les standards de 2025. Il est adapté pour les tâches de base comme la navigation web, les e-mails, la lecture multimédia légère et les applications IoT simples, mais il est à la traîne pour le multitâche, le gaming ou les calculs exigeants.

Points clés des benchmarks (provenant d'appareils utilisant cette puce) :
- **Geekbench 6** : Monocœur ~200–250, multi-cœurs ~600–700 (comparable aux puces modernes les plus bas de gamme).
- **3DMark Ice Storm** : Environ 8 500–9 000 points (tests de physique/graphismes), adapté pour les interfaces 2D mais peine avec les jeux 3D.
- **AnTuTu v6** : Score total d'environ 20 000–25 000, soulignant son positionnement économique.

Dans un usage réel sur le DragonBoard, attendez-vous à un fonctionnement fluide pour le script de développement ou l'intégration de capteurs, mais il peut subir une baisse de performance sous des charges soutenues en raison des limites thermiques et de la RAM limitée. Il est surpassé par les puces même de milieu de gamme de l'ère 2020 (par exemple, 5 à 10 fois plus lent qu'un Snapdragon 888 dans les tâches multi-cœurs), il est donc préférable pour les projets de hobbyistes plutôt que pour des besoins de production haute performance.

[DragonBoard 410c - 96Boards](https://www.96boards.org/product/dragonboard410c/)  
[Qualcomm Snapdragon 410 Benchmarks - NotebookCheck](https://www.notebookcheck.net/Qualcomm-Snapdragon-410-APQ8016-Benchmarks-and-Specs.142822.0.html)  
[CPU Benchmark - PassMark](https://www.cpubenchmark.net/cpu.php?cpu=Qualcomm%2BTechnologies%252C%2BInc%2BMSM8916&id=4009)