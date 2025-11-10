---
audio: false
generated: true
lang: fr
layout: post
title: PingCAP et Cloudflare louent Go
translated: true
type: note
---

Ni PingCAP ni Cloudflare n'ont exprimé de "regret" d'avoir utilisé Go. En fait, les deux entreprises ont publiquement loué les forces de Go et continuent de l'utiliser massivement dans leurs produits principaux. Cependant, elles font également preuve de pragmatisme dans leurs choix de langage et utilisent d'autres langages lorsqu'ils sont mieux adaptés à des problèmes spécifiques.

Voici une analyse détaillée :

### PingCAP (TiDB) et Go

* **Aucun regret :** PingCAP a choisi Go pour la couche SQL (`tidb-server`) de TiDB en raison de son excellent modèle de concurrence (goroutines et canaux), de sa facilité de développement et de sa bibliothèque standard robuste. Ces fonctionnalités leur ont permis de construire une base de données distribuée complexe relativement rapidement.
* **Défis reconnus :** Bien que Go soit central pour TiDB, PingCAP est très transparent concernant les défis, notamment en ce qui concerne le ramasse-miettes de Go. Leurs documentations et articles de blog en discutent fréquemment :
    * **Pauses du GC :** Ils reconnaissent que les pauses du ramasse-miettes, même courtes, peuvent introduire de la gigue de latence dans une base de données haute performance. Ils travaillent activement à les atténuer en ajustant `GOGC`, `GOMEMLIMIT` et en mettant en œuvre un déclenchement adaptatif du GC.
    * **Gestion de la mémoire :** Ils fournissent des guides détaillés pour surveiller l'utilisation de la mémoire et résoudre les problèmes d'OOM, reconnaissant que des modèles de mémoire inefficaces en Go peuvent entraîner des problèmes.
* **Utilisation stratégique de Rust :** PingCAP a choisi **Rust** pour TiKV, leur moteur de stockage clé-valeur distribué. Cela ne représente pas un "regret" envers Go, mais plutôt une **décision stratégique** pour la couche de stockage où une performance extrêmement faible latence, prévisible, et un contrôle granulaire de la mémoire sont primordiaux.
    * Le modèle de propriété et d'emprunt de Rust, ainsi que l'absence de ramasse-miettes, sont idéaux pour la programmation système où chaque microseconde et chaque octet compte.
    * Ils ont reconnu que le compromis d'une courbe d'apprentissage plus raide et de temps de compilation plus lents avec Rust était acceptable pour le moteur de stockage critique, mais moins souhaitable pour la couche SQL en évolution rapide.
* **Conclusion pour PingCAP :** Ils considèrent clairement Go et Rust comme des outils complémentaires. Go pour la logique de haut niveau et l'itération rapide, Rust pour les composants de bas niveau et critiques pour la performance.

### Cloudflare et Go

* **Adoption extensive de Go :** Cloudflare a été l'un des premiers et plus enthousiastes adoptants de Go. Ils utilisent Go pour une vaste gamme de leurs services, y compris l'infrastructure DNS, le traitement SSL, les outils de test de charge et de nombreux systèmes internes. Ils ont constamment parlé positivement de la concurrence de Go, de sa facilité de déploiement et de la productivité des développeurs.
* **Évolution, pas de regret :** Cloudflare a certainement diversifié son utilisation des langages, avec un virage notable vers **Rust** dans certains domaines critiques. Cela est motivé par des besoins de performance, de sécurité et d'efficacité des ressources, et non par un "regret" envers Go.
    * **Pingora (Rust) :** Un exemple primaire est le développement par Cloudflare de **Pingora**, un nouveau proxy HTTP construit en Rust pour remplacer des parties de leur infrastructure NGINX (écrite en C). Ce passage à Rust était largement motivé par :
        * **Sécurité mémoire :** Les garanties de Rust contre les bogues mémoire courants (débordements de tampon, use-after-free) qui sont prévalents en C/C++ (comme dans NGINX). Cela améliore significativement la sécurité et la stabilité.
        * **Performance extrême :** Pour un composant central traitant des billions de requêtes, les "abstractions à coût nul" de Rust et son contrôle granulaire permettent d'atteindre des performances encore plus élevées et une consommation de ressources plus faible que ce qui est facilement réalisable en Go (en raison de la surcharge du GC de Go).
        * **Expérience développeur améliorée pour la programmation système :** Bien que Rust ait une courbe d'apprentissage initiale plus raide, pour les ingénieurs systèmes travaillant sur des composants réseau de très bas niveau, sa rigueur et son système de type puissant peuvent conduire à long terme à un code plus robuste et plus facile à raisonner.
    * **Go toujours solide :** Même avec Pingora, Cloudflare continue de développer et de maintenir de nombreux services en Go. Ils considèrent Go comme "suffisamment rapide" pour la majorité de leurs charges de travail et apprécient sa vitesse de développement et sa simplicité opérationnelle.
* **Conclusion pour Cloudflare :** Cloudflare adopte une stratégie multi-langages, choisissant le meilleur outil pour chaque tâche. Go reste un langage fondamental pour eux, particulièrement pour les services qui bénéficient de son développement rapide et de sa concurrence. Rust est de plus en plus utilisé pour les composants de niveau système où une performance maximale, la sécurité mémoire et un contrôle granulaire sont primordiaux.

En substance, les deux entreprises sont des organisations d'ingénierie sophistiquées qui comprennent les compromis des différents langages de programmation. Elles n'expriment pas de "regret" d'avoir choisi Go, mais démontrent plutôt une approche pragmatique en utilisant d'autres langages comme Rust pour des domaines problématiques spécifiques où leurs forces (par exemple, l'absence de GC, la sécurité mémoire) offrent des avantages significatifs pour les infrastructures critiques.