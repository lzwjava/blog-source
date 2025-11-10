---
audio: false
generated: true
image: false
lang: fr
layout: post
title: L'ascension rapide des débutants tardifs
translated: true
type: note
---

Plusieurs langages de programmation qui ont démarré relativement tard (après 2000) ont connu une adoption rapide ces dernières années, portés par les avancées technologiques, l'intégration de l'IA et un fort soutien communautaire, un peu comme Rust. Ci-dessous, je vais mettre en lumière les langages clés qui correspondent à ce modèle de démarrage tardif mais de rattrapage rapide, en me concentrant sur leurs trajectoires de croissance, leurs cas d'utilisation et les facteurs contribuant à leur essor. Je comparerai leurs performances d'adoption à des langages établis comme Java, C et C++ lorsque cela est pertinent, et j'éviterai les affirmations spéculatives en fondant l'analyse sur des données et tendances disponibles.

### Langages à adoption rapide malgré un démarrage tardif

1. **Go (Golang)**
   - **Début et Contexte** : Lancé par Google en 2009, Go a été conçu pour la simplicité, les performances et la scalabilité dans les systèmes à grande échelle, abordant des problèmes du C++ et de Java comme la syntaxe complexe et la compilation lente.
   - **Performance d'Adoption** : Go a grimpé régulièrement en popularité. Mi-2025, il se classe autour de la #8-10 place dans l'index TIOBE (contre #13 en 2022) avec une notation d'environ ~2-3 %, et il est dans le top 10 du PYPL. Il compte environ 2 à 3 millions de développeurs, contre 12 à 15 millions pour Java ou 6 à 8 millions pour C++. L'enquête Stack Overflow de 2024 a montré que 13 % des développeurs utilisaient Go, avec une forte croissance dans le cloud et DevOps.
   - **Pourquoi il Rattrape son Retard** :
     - **Avancées Technologiques** : Le modèle de concurrence de Go (goroutines) et sa compilation rapide le rendent idéal pour les applications cloud-natives, les microservices et les conteneurs (par exemple, Docker et Kubernetes sont écrits en Go). Il surpasse Java en efficacité des ressources pour les charges de travail cloud.
     - **Intégration de l'IA** : Les outils d'IA comme GitHub Copilot améliorent la vitesse de développement en Go, générant du code idiomatique et réduisant le code boilerplate. L'utilisation de Go dans l'infrastructure IA (par exemple chez Google) croît en raison de ses performances.
     - **Communauté Open-Source** : La conception simple de Go et sa communauté active (plus de 30 000 packages sur pkg.go.dev) stimulent son adoption. Des entreprises comme Uber, Twitch et Dropbox utilisent Go, renforçant sa crédibilité.
   - **Preuves de Croissance** : L'adoption de Go a augmenté d'environ ~20 % en glissement annuel en 2024-2025, surtout dans l'informatique en cloud. Les offres d'emploi pour les développeurs Go ont explosé, et il devance Java dans les nouveaux projets cloud. Cependant, son écosystème plus petit que celui de Java ou C++ limite sa domination plus large.
   - **Références** : [Top Computer Languages 2025](https://statisticstimes.com/tech/top-computer-languages.php), [Top 10 programming languages in 2025](https://www.pluralsight.com/resources/blog/software-engineering/top-programming-languages), [History of Programming Languages](https://devskiller.com/history-of-programming-languages/).

2. **TypeScript**
   - **Début et Contexte** : Développé par Microsoft en 2012, TypeScript est un sur-ensemble de JavaScript qui ajoute le typage statique pour améliorer l'évolutivité et la maintenabilité dans les grands projets web.
   - **Performance d'Adoption** : TypeScript se classe #5-7 dans TIOBE (2025, ~3-4 %) et PYPL, avec environ ~3 millions de développeurs (contre 15-20 millions pour JavaScript). L'enquête Stack Overflow de 2024 a noté que 28 % des développeurs utilisaient TypeScript, contre 20 % en 2020, en faisant un choix de premier plan pour le développement web.
   - **Pourquoi il Rattrape son Retard** :
     - **Avancées Technologiques** : Le typage statique de TypeScript réduit les erreurs dans les projets JavaScript à grande échelle, le rendant crucial pour des frameworks comme React, Angular et Vue.js. Il est largement utilisé dans les applications web d'entreprise (par exemple, Slack, Airbnb).
     - **Intégration de l'IA** : Les IDE alimentés par l'IA (par exemple, Visual Studio Code) fournissent une vérification de type et un autocomplétion en temps réel, accélérant l'adoption de TypeScript. Son intégration avec les outils de développement pilotés par l'IA le rend convivial pour les débutants.
     - **Communauté Open-Source** : La communauté TypeScript est robuste, avec plus de 90 % des principaux frameworks JavaScript le supportant. Le soutien de Microsoft et l'écosystème npm (des millions de packages) alimentent la croissance.
   - **Preuves de Croissance** : L'utilisation de TypeScript dans les dépôts GitHub a augmenté d'environ ~30 % annuellement de 2022 à 2025, dépassant JavaScript dans les nouveaux projets frontend. Il comble l'écart avec JavaScript mais ne le dépassera pas en raison du support universel de JavaScript dans les navigateurs.
   - **Références** : [Top Computer Languages 2025](https://statisticstimes.com/tech/top-computer-languages.php), [Comparing tag trends with our Most Loved programming languages](https://stackoverflow.blog/2025/07/31/comparing-tag-trends-with-our-most-loved-programming-languages/), [The rise and fall in programming languages' popularity](https://www.zdnet.com/article/the-rise-and-fall-in-programming-languages-popularity-since-2016/).

3. **Kotlin**
   - **Début et Contexte** : Introduit par JetBrains en 2011, avec la version 1.0 sortie en 2016, Kotlin est une alternative moderne à Java, conçue pour une syntaxe concise et la sécurité, particulièrement pour le développement Android.
   - **Performance d'Adoption** : Kotlin se classe ~#12-15 dans TIOBE (2025, ~1-2 %) et PYPL, avec environ ~2 millions de développeurs. L'approbation de Google en 2017 en tant que langage de premier choix pour Android a déclenché une croissance rapide, avec 20 % des applications Android utilisant Kotlin en 2024 (contre 5 % en 2018).
   - **Pourquoi il Rattrape son Retard** :
     - **Avancées Technologiques** : La sécurité nulle (null safety) et la syntaxe concise de Kotlin réduisent le code boilerplate par rapport à Java, le rendant plus rapide pour le développement mobile et backend. Il interopère entièrement avec Java, facilitant les transitions.
     - **Intégration de l'IA** : Les outils d'IA dans les IDE comme IntelliJ IDEA génèrent du code Kotlin, améliorant la productivité. L'utilisation de Kotlin dans les applications mobiles pilotées par l'IA croît en raison de son efficacité.
     - **Communauté Open-Source** : Soutenu par JetBrains et Google, l'écosystème de Kotlin (par exemple, Ktor pour les serveurs, Compose pour l'UI) s'étend. Sa communauté est plus petite que celle de Java mais croît rapidement, avec des milliers de bibliothèques sur Maven.
   - **Preuves de Croissance** : L'adoption de Kotlin dans le développement Android a augmenté d'environ ~25 % annuellement, et il gagne du terrain dans le backend (par exemple, Spring Boot). Il est peu probable qu'il dépasse Java globalement en raison de la domination de Java dans l'entreprise, mais il rattrape son retard dans les niches mobiles et côté serveur.
   - **Références** : [Top Computer Languages 2025](https://statisticstimes.com/tech/top-computer-languages.php), [Top 10 programming languages in 2025](https://www.pluralsight.com/resources/blog/software-engineering/top-programming-languages), [History of Programming Languages](https://devskiller.com/history-of-programming-languages/).

4. **Swift**
   - **Début et Contexte** : Lancé par Apple en 2014, Swift est un langage moderne, sûr et rapide pour le développement iOS, macOS et côté serveur, remplaçant Objective-C.
   - **Performance d'Adoption** : Swift se classe ~#15-16 dans TIOBE (2025, ~1 %) et PYPL, avec environ 1,5 à 2 millions de développeurs. L'enquête Stack Overflow de 2024 a rapporté une utilisation par 8 % des développeurs, contre 5 % en 2020. Il domine le développement iOS, avec environ ~70 % des nouvelles applications iOS utilisant Swift.
   - **Pourquoi il Rattrape son Retard** :
     - **Avancées Technologiques** : Les performances de Swift rivalisent avec le C++ pour les applications natives, et ses fonctionnalités de sécurité (par exemple, les optionnels) réduisent les plantages par rapport à Objective-C. Il s'étend côté serveur (par exemple, le framework Vapor) et dans le développement multiplateforme.
     - **Intégration de l'IA** : Les outils de codage assisté par l'IA dans Xcode (par exemple, complétion de code, débogage) rendent Swift accessible. Son utilisation dans les applications iOS pilotées par l'IA (par exemple, AR/ML) est en croissance.
     - **Communauté Open-Source** : Open-source depuis 2015, Swift a une communauté grandissante, avec des milliers de packages sur Swift Package Manager. L'écosystème fermé d'Apple assure l'adoption, mais la croissance côté serveur ajoute de la versatilité.
   - **Preuves de Croissance** : L'adoption de Swift a augmenté d'environ ~20 % annuellement, dépassant Objective-C (maintenant #33 dans TIOBE). Il ne concurrence pas largement C/C++ ou Java mais domine sa niche et s'étend au-delà d'Apple.
   - **Références** : [Top Computer Languages 2025](https://statisticstimes.com/tech/top-computer-languages.php), [10 dying or 'dead' programming languages](https://www.techtarget.com/searchsoftwarequality/feature/10-dying-or-dead-programming-languages), [Top 10 programming languages in 2025](https://www.pluralsight.com/resources/blog/software-engineering/top-programming-languages).

5. **Julia**
   - **Début et Contexte** : Lancé en 2012, Julia est conçu pour le calcul numérique et scientifique haute performance, concurrençant Python et R dans la science des données et l'IA.
   - **Performance d'Adoption** : Julia se classe ~#20-25 dans TIOBE (2025, ~0,5-1 %) mais grimpe rapidement dans les communautés scientifiques. Il compte environ ~1 million de développeurs, loin derrière les 10-12 millions de Python. L'enquête Stack Overflow de 2024 a noté 2 % d'utilisation, contre <1 % en 2020.
   - **Pourquoi il Rattrape son Retard** :
     - **Avancées Technologiques** : La vitesse de Julia (proche du niveau C) et son typage dynamique le rendent idéal pour l'apprentissage automatique, les simulations et le big data. Des bibliothèques comme Flux.jl rivalisent avec PyTorch de Python.
     - **Intégration de l'IA** : Les outils d'IA génèrent du code Julia pour les tâches scientifiques, et ses performances dans les charges de travail IA/ML (par exemple, les équations différentielles) attirent les chercheurs.
     - **Communauté Open-Source** : La communauté de Julia est plus petite mais active, avec plus de 7 000 packages sur JuliaHub. Le soutien du monde universitaire et de la tech (par exemple, Julia Computing) stimule la croissance.
   - **Preuves de Croissance** : L'adoption de Julia dans la science des données a augmenté d'environ ~30 % annuellement, surtout dans le monde universitaire et la recherche en IA. Il ne dépasse pas Python mais se taille une niche où la performance compte.
   - **Références** : [Comparing tag trends with our Most Loved programming languages](https://stackoverflow.blog/2025/07/31/comparing-tag-trends-with-our-most-loved-programming-languages/), [Top Computer Languages 2025](https://statisticstimes.com/tech/top-computer-languages.php).

### Comparaison avec l'Adoption de Rust
- **Référence Rust** : La croissance annuelle d'environ ~25 % de Rust, ses ~2,3 millions de développeurs et son classement #13-15 dans TIOBE définissent la norme. Il excelle en programmation système, cloud et IA grâce à sa sécurité et ses performances.
- **Go et TypeScript** : Ils correspondent ou dépassent le taux de croissance de Rust (~20-30 %) et se classent plus haut (#8-10 et #5-7, respectivement). La domination de Go dans le cloud et celle de TypeScript dans le web leur donnent une portée plus large que la focalisation système de Rust.
- **Kotlin et Swift** : Ils ont une croissance similaire (~20-25 %) mais sont plus de niche (Android et iOS, respectivement). Ils rattrapent Java/Objective-C dans leurs domaines mais ont un attrait moins universel que Rust.
- **Julia** : Sa croissance (~30 %) est forte mais limitée au calcul scientifique, avec une base d'utilisateurs plus petite. Il est moins susceptible de rivaliser avec C/C++/Java de manière générale comparé à Rust.

### Pourquoi Ces Langages Réussissent
- **Adéquation Technologique** : Chacun répond aux besoins modernes (cloud pour Go, web pour TypeScript, mobile pour Kotlin/Swift, science pour Julia) mieux que les langages plus anciens dans des contextes spécifiques.
- **Accélération par l'IA** : Les outils d'IA abaissent les barrières, générant du code et des tutoriels, surtout pour les langages plus récents avec moins de bagages legacy.
- **Communauté et Industrie** : Un fort soutien (par exemple, Google pour Go/Kotlin, Microsoft pour TypeScript, Apple pour Swift) et des écosystèmes open-source stimulent l'adoption, reflétant le modèle de Rust.

### Limites
- **Taille de l'Écosystème** : Aucun n'égale les bibliothèques matures de Java (Maven), C++ (Boost) ou C (POSIX). Cela ralentit l'adoption large.
- **Courbe d'Apprentissage** : TypeScript et Kotlin sont plus faciles que Rust, mais Go, Swift et Julia peuvent être difficiles pour les débutants.
- **Domination des Legacies** : L'utilisation ancrée de C/C++/Java dans l'entreprise, les OS et les systèmes legacy signifie que ces langages plus récents rattrapent leur retard dans les nouveaux projets, sans remplacer les anciens.

### Conclusion
Go, TypeScript, Kotlin, Swift et Julia sont les langages remarquables démarrés après 2000 avec une adoption rapide, reflétant la trajectoire de Rust. Go et TypeScript sont les plus proches de Rust en impact large, tandis que Kotlin et Swift dominent des écosystèmes spécifiques, et Julia excelle dans une niche. Leur croissance est alimentée par les demandes technologiques modernes, les outils d'IA et l'élan open-source, mais aucun ne « rattrapera » complètement Java/C/C++ dans les 5 à 10 prochaines années en raison de l'ancrage des legacies. Pourtant, ils remodèlent significativement leurs domaines.

**Références**  
[Top Computer Languages 2025](https://statisticstimes.com/tech/top-computer-languages.php)  
[Top 10 programming languages in 2025](https://www.pluralsight.com/resources/blog/software-engineering/top-programming-languages)  
[Comparing tag trends with our Most Loved programming languages](https://stackoverflow.blog/2025/07/31/comparing-tag-trends-with-our-most-loved-programming-languages/)  
[History of Programming Languages](https://devskiller.com/history-of-programming-languages/)  
[10 dying or 'dead' programming languages](https://www.techtarget.com/searchsoftwarequality/feature/10-dying-or-dead-programming-languages)  
[The rise and fall in programming languages' popularity](https://www.zdnet.com/article/the-rise-and-fall-in-programming-languages-popularity-since-2016/)