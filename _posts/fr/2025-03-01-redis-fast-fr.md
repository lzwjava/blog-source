---
audio: false
generated: true
lang: fr
layout: post
title: Pourquoi Redis est-il rapide
translated: true
type: note
---

### Points Clés
- Il semble probable que la vidéo YouTube "System Design: Why is single-threaded Redis so fast?" de ByteByteGo explique la vitesse de Redis par son stockage en mémoire, le multiplexage des E/S et ses structures de données efficaces.
- Les recherches suggèrent que ces facteurs permettent à Redis de traiter jusqu'à 100 000 requêtes par seconde, bien qu'il soit single-threadé pour le traitement des requêtes.
- Les éléments indiquent que les versions récentes de Redis ont ajouté le multi-threading pour des tâches spécifiques, mais le cœur reste single-threadé.

---

### Introduction
Cet article de blog est basé sur la vidéo YouTube "System Design: Why is single-threaded Redis so fast?" de ByteByteGo, faisant partie de leur série sur la conception de systèmes. Redis, connu pour ses hautes performances, peut traiter jusqu'à 100 000 requêtes par seconde sur une seule machine, ce qui est impressionnant pour un système single-threadé. Explorons pourquoi c'est possible et ce qui rend Redis si rapide.

### Raisons de la Vitesse de Redis
La vitesse de Redis peut être attribuée à plusieurs facteurs clés, probablement couverts dans la vidéo :

- **Stockage en Mémoire** : Redis stocke les données dans la RAM, qui est beaucoup plus rapide que le stockage sur disque. Cela réduit la latence et augmente le débit, car les temps d'accès à la mémoire sont de l'ordre de la nanoseconde contre la milliseconde pour un disque.

- **Multiplexage des E/S et Exécution Single-Threadée** : Le multiplexage des E/S, utilisant des mécanismes comme epoll sous Linux, permet à un seul thread de gérer efficacement de multiples connexions client. Cela évite la surcharge de la commutation de contexte, et la boucle single-threadée simplifie les opérations en éliminant les problèmes de synchronisation.

- **Structures de Données Efficaces** : Redis utilise des structures de données optimisées comme les tables de hachage (recherches en O(1)), les listes chaînées et les listes à sauts, qui améliorent les performances en minimisant l'utilisation de la mémoire et en accélérant les opérations.

### Mise à l'Échelle et Évolution
Pour une haute concurrence, Redis peut être mis à l'échelle horizontalement en utilisant plusieurs instances ou le clustering. Un détail inattendu est que bien que le traitement principal des requêtes reste single-threadé, les versions récentes (depuis la 4.0) ont introduit le multi-threading pour des tâches comme la suppression d'objets en arrière-plan, améliorant encore les performances sans changer le modèle principal.

---

### Note d'Enquête : Analyse Détaillée des Performances Single-Threadées de Redis

Cette section fournit une analyse complète des raisons pour lesquelles Redis single-threadé est si rapide, basée sur la vidéo YouTube "System Design: Why is single-threaded Redis so fast?" de ByteByteGo et des recherches connexes. La vidéo, publiée le 13 août 2022, fait partie d'une série axée sur la conception de systèmes, créée par les auteurs des livres à succès System Design Interview. Compte tenu de l'orientation de la chaîne, la vidéo fournit probablement des informations détaillées adaptées aux entretiens techniques et aux discussions sur la conception de systèmes.

#### Contexte
Redis, un magasin clé-valeur en mémoire open source, est largement utilisé comme cache, courtier de messages et moteur de streaming. Il prend en charge des structures de données comme les chaînes, les listes, les ensembles, les hachages, les ensembles triés et des structures probabilistes comme le Filtre de Bloom et l'HyperLogLog. Le titre de la vidéo suggère une exploration des raisons pour lesquelles Redis maintient des performances élevées malgré son traitement de requêtes single-threadé, qui est au cœur de sa conception.

D'après des articles connexes, Redis peut traiter jusqu'à 100 000 Requêtes Par Seconde (QPS) sur une seule machine, un chiffre souvent cité dans les benchmarks de performance. Cette vitesse est surprenante étant donné le modèle single-threadé, mais les recherches indiquent qu'elle est due à plusieurs choix architecturaux.

#### Facteurs Clés Contribuant à la Vitesse de Redis

1. **Stockage en Mémoire**  
   Redis stocke les données dans la RAM, qui est au moins 1000 fois plus rapide que l'accès aléatoire à un disque. Cela élimine la latence des E/S disque, avec des temps d'accès à la RAM d'environ 100-120 nanosecondes contre 50-150 microsecondes pour les SSD et 1-10 millisecondes pour les HDD. La vidéo met probablement l'accent sur ce point comme raison principale, car il correspond à l'orientation de la chaîne sur les fondamentaux de la conception de systèmes.

   | Aspect               | Détails                                      |
   |----------------------|----------------------------------------------|
   | Support de Stockage  | RAM (en mémoire)                             |
   | Temps d'Accès        | ~100-120 nanosecondes                       |
   | Comparaison au Disque| 1000x plus rapide que l'accès aléatoire au disque |
   | Impact sur les Performances| Réduit la latence, augmente le débit     |

2. **Multiplexage des E/S et Boucle d'Exécution Single-Threadée**  
   Le multiplexage des E/S permet à un seul thread de surveiller plusieurs flux d'E/S simultanément en utilisant des appels système comme `select`, `poll`, `epoll` (Linux), `kqueue` (Mac OS) ou `evport` (Solaris). Ceci est crucial pour gérer de multiples connexions client sans blocage, un point probablement détaillé dans la vidéo. La boucle d'exécution single-threadée évite la surcharge de la commutation de contexte et de la synchronisation, simplifiant le développement et le débogage.

   | Mécanisme            | Description                                  |
   |----------------------|----------------------------------------------|
   | epoll/kqueue         | Efficace pour la haute concurrence, non-bloquant |
   | select/poll          | Plus anciens, moins évolutifs, complexité O(n) |
   | Impact               | Réduit la surcharge des connexions, permet le pipelining |

   Cependant, les commandes bloquantes pour le client comme `BLPOP` ou `BRPOP` peuvent retarder le trafic, un inconvénient potentiel mentionné dans des articles connexes. La vidéo peut discuter de la façon dont ce choix de conception équilibre simplicité et performance.

3. **Structures de Données de Bas Niveau Efficaces**  
   Redis utilise des structures de données comme les tables de hachage pour les recherches de clés en O(1), les listes chaînées pour les listes et les listes à sauts pour les ensembles triés. Celles-ci sont optimisées pour les opérations en mémoire, minimisant l'utilisation de la mémoire et maximisant la vitesse. La vidéo inclut probablement des diagrammes ou des exemples, comme la façon dont les tables de hachage permettent des opérations clé-valeur rapides, un sujet courant dans les entretiens sur la conception de systèmes.

   | Structure de Données | Cas d'Utilisation                            | Complexité Temporelle |
   |----------------------|----------------------------------------------|-----------------|
   | Table de Hachage     | Stockage clé-valeur                         | O(1) en moyenne |
   | Liste Chaînée        | Listes, efficaces aux extrémités            | O(1) pour les extrémités |
   | Liste à Sauts        | Ensembles triés, stockage ordonné           | O(log n)        |

   Cette optimisation est critique, car la plupart des opérations de Redis sont basées sur la mémoire, les goulots d'étranglement étant généralement la mémoire ou le réseau, et non le CPU.

#### Considérations Supplémentaires et Évolution
Bien que le traitement principal des requêtes soit single-threadé, les versions récentes de Redis ont introduit le multi-threading pour des tâches spécifiques. Depuis Redis 4.0, la libération asynchrone de la mémoire (lazy-free) a été implémentée, et depuis la 6.0, le multi-threading pour l'analyse du protocole sous haute concurrence a été ajouté. Ces changements, probablement mentionnés dans la vidéo, améliorent les performances sans altérer le modèle single-threadé pour les opérations principales.

Pour une mise à l'échelle au-delà d'une seule instance, Redis prend en charge le clustering et l'exécution de multiples instances, une stratégie qui peut être discutée pour répondre aux besoins de haute concurrence. C'est un aspect important pour la conception de systèmes, correspondant à l'orientation de la chaîne sur les systèmes à grande échelle.

#### Inconvénients Potentiels et Comparaisons
Le modèle single-threadé a des avantages comme l'absence de contention de verrous et un débogage plus simple, mais il peut rencontrer des difficultés avec les opérations bloquantes et les goulots d'étranglement mémoire/réseau sous charge élevée. Des articles connexes suggèrent que pour les tâches intensives en CPU, les bases de données multi-threadées pourraient mieux performer, mais pour les cas d'utilisation typiques de Redis, la conception single-threadée est optimale.

#### Conclusion
La vidéo "System Design: Why is single-threaded Redis so fast?" de ByteByteGo couvre probablement le stockage en mémoire, le multiplexage des E/S et les structures de données efficaces comme des raisons clés de la vitesse de Redis. Ces facteurs lui permettent de gérer un QPS élevé, les versions récentes ayant ajouté le multi-threading pour des optimisations spécifiques. Cette analyse fournit une compréhension complète, adaptée à la fois aux apprenants techniques et aux professionnels de la conception de systèmes.

---

### Citations Clés
- [Why is redis so fast blog post](https://blog.bytebytego.com/p/why-is-redis-so-fast)
- [Why is Redis So Fast Despite Being Single-Threaded article](https://medium.com/@aditimishra_541/why-is-redis-so-fast-despite-being-single-threaded-dc06ba33fc75)
- [Interview on Redis thread model article](https://medium.com/javarevisited/interview-why-is-redis-so-fast-even-though-it-is-single-threaded-bfe663dabe08)
- [Why is single threaded Redis so fast article](https://www.pixelstech.net/article/1677580861-Why-is-single-threaded-Redis-so-fast)