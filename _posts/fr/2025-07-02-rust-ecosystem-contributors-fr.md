---
audio: false
generated: true
lang: fr
layout: post
title: Principaux contributeurs et fondateurs de Rust
translated: true
type: note
---

L'écosystème Rust est dynamique et en pleine croissance, avec de nombreuses personnes et organisations qui y contribuent de manière significative. Voici une répartition des principaux contributeurs, programmeurs, projets influents et fondateurs :

### Fondateurs de Rust

Le fondateur principal du langage de programmation Rust est :

* **Graydon Hoare :** Il a commencé Rust comme un projet personnel alors qu'il travaillait chez Mozilla en 2006, motivé par le désir de créer un langage système qui résoudrait les problèmes de sécurité mémoire prévalents en C et C++. Il a jeté les principes fondateurs du langage.

D'autres figures clés qui ont été instrumentales dans le développement et l'évolution précoces de Rust chez Mozilla incluent :

* **Niko Matsakis :** Un contributeur de longue date au compilateur Rust et à la conception du langage, notamment concernant le *borrow checker*.
* **Patrick Walton**
* **Felix Klock**
* **Manish Goregaokar**

### Principaux Contributeurs & Programmeurs de l'Écosystème Rust (Hautement Reconnus, Travail Open Source)

Il est difficile d'établir une liste définitive des "30 meilleurs" car les contributions sont diverses et réparties entre de nombreux individus et équipes. Cependant, voici quelques programmeurs hautement reconnus et contributeurs clés connus pour leur travail open source et leur impact sur la communauté Rust :

* **Steve Klabnik :** Un écrivain, éducateur et membre de l'équipe centrale prolifique. Il est connu pour ses contributions à la documentation de Rust (par exemple, "The Rust Programming Language Book") et son plaidoyer pour Rust. Il travaille désormais chez Oxide Computer Company, appliquant Rust aux systèmes matériels/logiciels.
* **Nicholas Matsakis (nikomatsakis) :** Instrumental dans la conception et l'implémentation du compilateur Rust, en particulier le *borrow checker*, qui est central pour les garanties de sécurité mémoire de Rust. Il travaille sur Rust chez AWS.
* **Mara Bos :** Un membre éminent de l'équipe des bibliothèques Rust et active dans la communauté, contribuant à divers aspects de la bibliothèque standard et à l'évolution du langage. Elle est également co-fondatrice de Fusion Engineering.
* **Carol Nichols :** Une autre figure clé de la communauté Rust, co-auteure de "The Rust Programming Language Book", et siège au conseil d'administration de la Rust Foundation. Elle plaide activement pour l'adoption et la durabilité de Rust.
* **Jon Gjengset (jonhoo) :** Connu pour ses plongées approfondies dans les internes de Rust, notamment la concurrence, et pour son excellent contenu éducatif et ses streams qui aident beaucoup à apprendre les concepts avancés de Rust.
* **Alex Crichton :** Un contributeur significatif à divers projets Rust, y compris `rust-lang/rust` et `crates.io-index`, jouant un rôle crucial dans l'infrastructure de l'écosystème.
* **Ralf Jung :** Connu pour son travail sur Miri, un interpréteur UBM (*Undefined Behavior Machine*) pour Rust, qui aide à identifier les comportements indéfinis dans le code Rust.
* **Bryan Cantrill :** CTO et co-fondateur d'Oxide Computer Company, un ardent défenseur de Rust dans la programmation système et l'industrie.
* **Josh Triplett :** Un contributeur de longue date à Rust et membre de l'équipe centrale, impliqué dans de nombreux aspects du développement du langage.
* **Armin Ronacher (mitsuhiko) :** Créateur du framework Python Flask, il est devenu une force motrice significative pour l'adoption de Rust, notamment chez Sentry.
* **Andrew Gallant (BurntSushi) :** Connu pour des crates Rust hautement optimisées et largement utilisées comme `ripgrep` (une alternative rapide à grep) et `regex`.
* **Syrus Akbary :** Créateur de Wasmer, un runtime WebAssembly propulsé par Rust.
* **Frank McSherry :** Connu pour son travail sur *differential dataflow* et d'autres projets qui explorent la concurrence avancée et le traitement des données en Rust.
* **Jeremy Soller :** Son travail chez System76 et maintenant chez Oxide Computer Company démontre la viabilité de Rust jusqu'au niveau du système d'exploitation.
* **Guillaume Gomez :** Un contributeur prolifique au compilateur Rust et au projet GTK-RS (liaisons Rust pour GTK).
* **Pietro Albini :** Contribue de manière significative à l'infrastructure cruciale de Rust et est membre de l'équipe centrale de Rust.
* **Dirkjan Ochtman :** Pour la maintenance de `rustls` et `quinn`, des bibliothèques importantes pour la communication sécurisée en Rust.
* **Gary Guo :** Pour la maintenance de Rust for Linux, un effort critique pour intégrer Rust dans le noyau Linux.
* **Manish Goregaokar :** Un ingénieur logiciel senior chez Google, contribue à divers projets Rust, y compris des travaux liés à Unicode.

### Principaux Projets Open Source Rust (Hautement Impactants)

De nombreux projets open source mettent en valeur les forces de Rust et ont un impact significatif :

1.  **Rust Lang/Rust (le Compilateur Rust et la Bibliothèque Standard) :** Le projet central lui-même, permettant à tous de construire des logiciels fiables et efficaces.
2.  **Tauri Apps/Tauri :** Un framework pour construire des applications de bureau et mobiles plus petites, plus rapides et plus sécurisées avec un frontend web, similaire à Electron mais plus efficace.
3.  **RustDesk/RustDesk :** Une application de bureau à distance open source, une alternative populaire à TeamViewer.
4.  **Alacritty/Alacritty :** Un émulateur de terminal multiplateforme, OpenGL, connu pour ses hautes performances.
5.  **Tokio/Tokio :** Le runtime asynchrone fondamental pour Rust, largement utilisé pour construire des applications réseau hautes performances.
6.  **Hyper/Hyper :** Une bibliothèque HTTP rapide et correcte pour Rust, souvent utilisée conjointement avec Tokio.
7.  **Actix/Actix-web :** Un framework web puissant, rapide et hautement concurrent pour Rust.
8.  **Axum/Axum :** Un framework d'application web construit avec Tokio et Hyper, mettant l'accent sur l'ergonomie et le typage fort.
9.  **Ripgrep (BurntSushi/ripgrep) :** Un outil de recherche orienté ligne qui recherche récursivement dans les répertoires un motif regex, significativement plus rapide que `grep`.
10. **Bat (sharkdp/bat) :** Un clone de `cat(1)` avec des ailes, offrant la coloration syntaxique, l'intégration Git et plus encore.
11. **Fd (sharkdp/fd) :** Une alternative simple, rapide et conviviale à `find`.
12. **Meilisearch/Meilisearch :** Un moteur de recherche puissant, rapide et pertinent.
13. **Polars/Polars :** Une bibliothèque DataFrame ultra-rapide, souvent considérée comme une alternative Rust à Pandas pour la manipulation de données.
14. **BevyEngine/Bevy :** Un moteur de jeu axé sur les données, rafraîchissant de simplicité, construit en Rust.
15. **Helix Editor/Helix :** Un éditeur de texte modal moderne inspiré par Neovim et Kakoune, écrit en Rust.
16. **Nushell/Nushell (ou Nu) :** Un shell moderne qui vise à apporter les concepts des langages de programmation en ligne de commande.
17. **Deno/Deno :** Un runtime sécurisé pour JavaScript et TypeScript, construit avec Rust et V8.
18. **Firecracker MicroVM/Firecracker :** Développé par AWS, une technologie de virtualisation légère utilisée pour le calcul *serverless*.
19. **Crates.io :** Le registre officiel des paquets pour le langage de programmation Rust, essentiel pour l'écosystème.
20. **Rustlings (rust-lang/rustlings) :** De petits exercices pour habituer les utilisateurs à lire et écrire du code Rust, incroyablement précieux pour les débutants.
21. **Yewstack/Yew :** Un framework Rust moderne pour construire des applications web côté client en utilisant WebAssembly.
22. **DioxusLabs/Dioxus :** Une autre bibliothèque UI déclarative populaire pour Rust pour construire des applications multiplateformes.
23. **Servo/Servo :** Un moteur de navigateur haute performance et parallèle écrit en Rust, développé par Mozilla et ensuite transféré à la Linux Foundation.
24. **Rocket/Rocket :** Un framework web pour Rust, connu pour sa sécurité des types et son expérience développeur.
25. **Solana/Solana :** Une plateforme blockchain haute performance, avec une partie significative de ses composants principaux écrite en Rust.
26. **Substrate/Substrate :** Un framework pour construire des blockchains personnalisées, utilisant également fortement Rust.
27. **Wasmtime/Wasmtime :** Un runtime autonome de style JIT pour WebAssembly et WASI (*WebAssembly System Interface*).
28. **Delta (dandavison/delta) :** Un *pager* avec coloration syntaxique pour la sortie de `diff`, `git` et `merge`.
29. **Spotify TUI (Rigellute/spotify-tui) :** Une interface utilisateur en terminal pour Spotify.
30. **mdBook (rust-lang/mdBook) :** Un outil en ligne de commande pour créer des livres à partir de fichiers Markdown, utilisé pour de nombreux projets Rust, y compris "The Rust Programming Language Book."

Cette liste n'est pas exhaustive, et l'écosystème Rust évolue constamment avec de nouveaux projets impactants émergeant régulièrement. La force de la communauté réside dans sa nature collaborative et la haute qualité de ses contributions open source.