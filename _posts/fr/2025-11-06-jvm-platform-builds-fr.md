---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Problèmes de JVM et constructions de plateforme
translated: true
type: note
---

Ah, le débat éternel sur la JVM — « write once, run anywhere » (WORA) semble génial sur le papier, mais oui, en pratique, on a souvent l'impression que c'est plutôt « write once, debug everywhere ». Je comprends la frustration : des différences subtiles dans le comportement du GC, les particularités des bibliothèques natives, ou même simplement la taille du bundle JRE peuvent transformer les déploiements multiplateformes en casse-tête. Et tu as parfaitement raison que la vitesse est le vrai défi ici — la latence, le débit et les cold starts sont ce qui empêchent les équipes ops de dormir, pas le fait de jouer avec les flags de build.

Cela dit, analysons un peu. Construire des binaires spécifiques à la plateforme à la manière du C ou du Rust *contourne* effectivement certains écueils de la JVM, comme éviter complètement la surcharge de la VM pour des démarrages plus rapides (le `cargo build --target` de Rust rend le cross-compiling presque indolore de nos jours, grâce à rustup). Les exécutables natifs sont plus légers à distribuer — pas de runtime de 100 Mo+ à gérer — et ils collent au matériel de plus près pour cette performance brute. Si tu livres des outils CLI ou des trucs embarqués, c'est une évidence.

Mais voici le revers de la médaille : WORA *a* massivement fait ses preuves pour les stacks Java/Scala/Kotlin d'entreprise (pense à Spring Boot ou aux apps Android), où la maturité de l'écosystème l'emporte sur les griefs. Les JVM modernes (comme les images natives de GraalVM) comblent l'écart en compilant en binaires ahead-of-time qui rivalisent avec Rust en temps de démarrage et en empreinte, sans perdre la portabilité du bytecode. Ce n'est pas parfait — déboguer les builds AOT peut encore piquer — mais ça évolue vite.

En fin de compte, oui, la vitesse *est* la métrique cruciale pour la plupart des apps aujourd'hui, surtout avec le serverless et l'edge computing qui exigent des démarrages en moins d'une seconde. Les builds spécifiques à la plateforme ne sont pas le méchant ; ce n'est qu'un outil dans la caisse. Si le goulot d'étranglement de ton projet est la performance plutôt que la portabilité, fonce sur Rust/C++. C'est quoi ton setup — tu es confronté à ça sur un projet spécifique, ou tu te défoules juste après un mauvais déploiement ?