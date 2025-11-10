---
audio: false
generated: true
lang: fr
layout: post
title: L'évolution rapide et sûre de Rust
translated: true
type: note
---

Rust est un langage de programmation système moderne qui a gagné une popularité significative grâce à son accent sur la sécurité, la performance et la concurrence. Son histoire est un parcours intéressant d'innovation et de développement communautaire, largement initié et soutenu par Mozilla.

### Les débuts (2006-2009)

Les origines de Rust remontent à **2006** en tant que projet personnel de **Graydon Hoare**, un développeur chez Mozilla. Frustré par des plantages logiciels récurrents, en particulier un ascenseur défectueux dans son immeuble, Hoare a cherché à créer un langage capable de surmonter les problèmes de gestion et d'allocation de mémoire prévalents dans des langages comme le C et le C++. Il visait un langage offrant le contrôle de bas niveau et la performance des langages système traditionnels, mais sans les bogues de mémoire et les vulnérabilités de sécurité courantes. Le nom "Rust" lui-même serait inspiré d'un groupe de champignons "surdimensionnés pour la survie", reflétant l'accent du langage sur la robustesse.

Durant ces premières années, Rust a été développé par Hoare sur son temps libre et est resté largement interne à Mozilla. Le premier compilateur était écrit en OCaml, et le langage explorait des fonctionnalités telles que la programmation orientée objet explicite et un système de typestates pour suivre l'état des variables.

### Le parrainage de Mozilla et l'open source (2009-2012)

En **2009**, Mozilla a officiellement reconnu le potentiel de Rust et a commencé à parrainer le projet. Des dirigeants comme Brendan Eich y ont vu une opportunité d'utiliser Rust pour un moteur de navigateur web plus sûr. Cela a conduit à une équipe dédiée d'ingénieurs rejoignant Hoare, incluant Patrick Walton, Niko Matsakis et Felix Klock, entre autres.

Cette période a marqué un changement significatif :
* **Compilateur auto-hébergé :** Des travaux ont commencé pour réécrire le compilateur Rust en Rust lui-même, basé sur LLVM, une étape cruciale pour l'indépendance et la maturité du langage.
* **Introduction du système de propriété :** Le concept fondamental du système de propriété de Rust, central pour ses garanties de sécurité mémoire sans ramasse-miettes, a commencé à prendre forme vers **2010**.

En **2010**, Rust a été publié en tant que projet open source, ouvrant son développement à une communauté plus large.

### Évolution et maturation (2012-2015)

Les années précédant la version 1.0 ont été caractérisées par des changements substantiels et parfois radicaux du langage. L'équipe de développement s'est engagée à affiner les fonctionnalités principales de Rust et à assurer sa stabilité. Les développements clés ont inclus :
* **Suppression des Typestates et du Garbage Collector :** Le système initial de typestates a été supprimé, et, de façon critique, le ramasse-miettes expérimental a été progressivement abandonné vers **2013** au profit du système de propriété en évolution. Cette décision a été cruciale pour solidifier l'identité de Rust en tant que langage à hautes performances avec des abstractions sans coût.
* **Consolidation de la gestion de la mémoire :** Le système de propriété, ainsi que l'emprunt et les durées de vie, ont été progressivement étendus et solidifiés pour empêcher les bogues liés à la mémoire au moment de la compilation.
* **Influence de divers langages :** La conception de Rust a été influencée par divers paradigmes de programmation, empruntant des idées au C++ (pour la performance de bas niveau), aux langages de script (pour la gestion de paquets comme Cargo) et à la programmation fonctionnelle (pour son système de types).
* **Concentration sur la stabilité pour la 1.0 :** Durant cette période, l'accent a été fortement mis sur la finalisation des fonctionnalités du langage et la préparation d'une version stable 1.0 offrant la rétrocompatibilité.

### Rust 1.0 et au-delà (2015 à aujourd'hui)

Le **15 mai 2015**, six ans après le parrainage officiel de Mozilla, la première version stable, **Rust 1.0**, a été publiée. Ce fut un moment monumental, signalant que Rust était prêt pour une utilisation en production et son engagement envers la stabilité.

Depuis la version 1.0, Rust a connu :
* **Une croissance rapide de la communauté :** Le compilateur a rapidement accumulé des milliers de contributeurs, et le site de gestion de paquets, Crates.io, a vu une augmentation significative des bibliothèques tierces.
* **Une adoption généralisée :** Des entreprises majeures comme Amazon Web Services (AWS), Microsoft, Google et Meta ont adopté Rust pour des systèmes backend critiques en termes de performance, des composants de systèmes d'exploitation, des services web et de l'infrastructure blockchain. Mozilla lui-même a utilisé Rust pour réécrire des parties du moteur de Firefox (comme Stylo, le moteur CSS), conduisant à des améliorations de performance.
* **La formation de la Rust Foundation :** En **2021**, la Rust Foundation a été établie, formalisant la gouvernance du langage et assurant son développement continu et son indépendance au-delà de ses origines chez Mozilla.
* **Une évolution continue via les "Éditions" :** Rust utilise des "Éditions" pour gérer des changements significatifs du langage sans casser le code existant, permettant au langage d'évoluer tout en maintenant la rétrocompatibilité.

Aujourd'hui, Rust est reconnu pour son unique combinaison d'une performance comparable au C/C++ avec des garanties de sécurité mémoire et de concurrence inégalées, ce qui en fait un langage très prisé dans la programmation système, le développement web (en particulier avec WebAssembly), les systèmes embarqués, et plus encore.