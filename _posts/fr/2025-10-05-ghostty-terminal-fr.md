---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Ghostty Émulateur de Terminal Multiplateforme
translated: true
type: note
---

Oui, Ghostty est conçu comme un émulateur de terminal multiplateforme, ce qui est effectivement l'un de ses principaux atouts — il est construit pour fonctionner de manière cohérente sur plusieurs systèmes d'exploitation avec des performances élevées grâce à l'accélération GPU et à l'intégration d'interface utilisateur native. Cependant, en octobre 2025, sa prise en charge complète est actuellement limitée à macOS et Linux, la version Windows étant encore en phase de planification mais pas encore publiée.

Concernant l'expérience : Elle n'est pas *exactement* identique sur toutes les plateformes car Ghostty utilise des composants d'interface utilisateur natifs (par exemple, Cocoa sur macOS, GTK sur Linux) pour offrir une sensation idiomatique et intégrée sur chacune d'elles — comme une application conçue spécifiquement plutôt qu'un port unique universel. Cela dit, les fonctionnalités de base, les caractéristiques (comme les onglets, les divisions, la recherche et les protocoles de terminal avancés) et les performances sont conçues pour être très similaires et fiables partout où il est pris en charge, minimisant les particularités spécifiques à une plateforme que l'on pourrait rencontrer dans des émulateurs moins aboutis.

Si la version Windows arrive bientôt (sur la base des discussions en cours sur GitHub), elle devrait suivre la même approche native pour une sensation transparente là aussi.

[Fonctionnalités officielles de Ghostty](https://ghostty.org/docs/features)  
[Dépôt GitHub de Ghostty](https://github.com/ghostty-org/ghostty)  
[Notes de version de Ghostty](https://ghostty.org/docs/install/release-notes)