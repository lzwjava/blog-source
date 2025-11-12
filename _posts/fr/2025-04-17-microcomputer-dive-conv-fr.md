---
audio: false
lang: fr
layout: post
title: Plongée en micro-informatique – Conversation
translated: true
type: note
---

A: Je me suis replongé récemment dans l'architecture des micro-ordinateurs. Peut-on commencer par comparer les architectures von Neumann et Harvard ?

B: Absolument ! Von Neumann utilise un bus unique pour les données et les instructions, ce qui peut créer des goulots d'étranglement. Harvard les sépare, permettant des accès parallèles—c'est courant dans les DSP et les microcontrôleurs. Quel cas d'usage t'intéresse le plus ?

A: Les systèmes embarqués, en fait. Harvard semble dominant là-bas. Mais comment les hybrides modernes, comme les architectures Harvard modifiées, comblent-ils l'écart ?

B: Excellente question ! Les hybrides utilisent des caches séparés (L1 pour instructions/données) mais un espace mémoire unifié. Prenez l'ARM Cortex-M : il est de type Harvard pour la vitesse mais simplifie la programmation. Des compromis ?

A: Des compromis, en effet. La mémoire unifiée facilite le développement mais sacrifie le débit. Penses-tu que la flexibilité de RISC-V pourrait bouleverser ce domaine ?

B: Potentiellement ! L'ISA modulaire de RISC-V permet aux concepteurs d'ajouter des fonctionnalités de type Harvard par application. Pour les appareils IoT en edge, c'est un changement majeur. Mais l'écosystème d'ARM est bien établi. Quel est ton avis ?

A: Les écosystèmes ont la vie dure, mais le modèle open-source de RISC-V pourrait accélérer les optimisations de niche. Changeons de sujet—à quel point le DMA est-il critique dans les microcontrôleurs modernes ?

B: Crucial ! Déléguez les transferts de données (par exemple, ADC vers la mémoire) permet d'économiser des cycles CPU. Le DMA des STM32 gère même les transferts périphérique-à-périphérique. As-tu déjà travaillé avec des buffers DMA circulaires ?

A: Oui, pour le traitement audio. Mais configurer les modes rafale était délicat. Comment le DMA priorise-t-il les requêtes lorsque plusieurs périphériques sont en concurrence ?

B: La priorité est généralement configurable matériellement. Les MCU de NXP utilisent du round-robin pondéré, tandis que certaines pièces de TI permettent une repriorisation dynamique. La latence d'interruption devient un facteur—l'as-tu déjà mesurée ?

A: Seulement de manière empirique. En parlant d'interruptions, comment les RTOS comme FreeRTOS gèrent-ils les ISR imbriquées différemment du bare-metal ?

B: Les RTOS ajoutent des couches : sauvegarde de contexte, invocations de l'ordonnanceur post-ISR. Les API 'FromISR' de FreeRTOS gèrent cela de manière sécurisée. Mais les ISR en bare-metal sont plus légères—compromis entre complexité et contrôle.

A: C'est logique. Pour les systèmes temps réel stricts, recommanderais-tu jamais un superloop plutôt qu'un RTOS ?

B: Seulement pour des systèmes triviaux ! Les superloops peinent avec les tâches multi-cadences. Un RTOS correctement configuré avec héritage de priorité évite l'inversion de priorité. Les améliorations récentes de Zephyr valent le coup d'œil.

A: Le modèle device tree de Zephyr est intrigant. Comment se compare-t-il à celui de Linux pour une utilisation embarquée ?

B: Le DT de Linux est trop lourd pour les microcontrôleurs. Le Kconfig + devicetree de Zephyr trouve un équilibre—la configuration statique réduit la surcharge d'exécution. As-tu déjà porté un pilote entre les deux ?

A: Pas encore, mais j'ai vu que l'API GPIO de Zephyr abstrait bien les particularités matérielles. Quel est ton avis sur les E/S mappées en mémoire par rapport aux E/S mappées par port pour les microcontrôleurs ?

B: Le mapping mémoire domine maintenant—l'adressage unifié simplifie les compilateurs. L'E/S par port legacy