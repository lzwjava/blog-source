---
audio: false
generated: true
lang: fr
layout: post
title: Gestion de la Mémoire en Java
translated: true
type: note
---

Parfait, découvrons le Garbage Collection (GC) en Java ! C'est un aspect crucial de la gestion de la mémoire en Java qui aide les développeurs à éviter l'allocation et la libération manuelles de la mémoire.

**Qu'est-ce que le Garbage Collection en Java ?**

Le Garbage Collection est le processus automatique de récupération de la mémoire occupée par des objets qui ne sont plus utilisés par une application Java. En substance, c'est la manière de Java de nettoyer les "déchets" (objets inutilisés) pour faire de la place pour de nouveaux objets.

**Pourquoi le Garbage Collection est-il nécessaire ?**

Dans de nombreux autres langages de programmation (comme le C ou le C++), les développeurs sont responsables de l'allocation et de la libération explicites de la mémoire à l'aide de fonctions comme `malloc` et `free`. Cette gestion manuelle de la mémoire peut entraîner plusieurs problèmes :

* **Fuites de mémoire :** Si la mémoire est allouée mais jamais libérée, l'application peut finir par manquer de mémoire et planter.
* **Pointeurs pendants :** Si la mémoire est libérée mais qu'un pointeur fait toujours référence à cet emplacement mémoire, l'utilisation de ce pointeur peut entraîner un comportement imprévisible ou des plantages.
* **Complexité de développement accrue :** Gérer la mémoire manuellement ajoute une couche de complexité significative au développement logiciel.

Le Garbage Collection de Java automatise ce processus, libérant les développeurs du fardeau de la gestion manuelle de la mémoire et facilitant l'écriture de code plus sûr et plus fiable.

**Comment fonctionne le Garbage Collection ?**

L'idée centrale derrière le garbage collection est d'identifier quels objets en mémoire sont encore utilisés par l'application et lesquels ne le sont pas. Le ramasse-miettes récupère ensuite la mémoire occupée par les objets inutilisés.

Voici un aperçu simplifié du processus :

1.  **Identification des objets actifs (Marquage) :** Le ramasse-miettes commence par identifier l'ensemble des objets qui sont encore atteignables à partir des objets "racines". Les objets racines sont généralement des objets directement accessibles par l'application, tels que :
    * Les variables locales dans les méthodes en cours d'exécution.
    * Les variables statiques.
    * Les objets référencés par le code natif.
    * Les threads actifs de la Machine Virtuelle Java (JVM).

    Le ramasse-miettes parcourt le graphe d'objets en partant de ces racines, marquant tous les objets qui sont atteignables.

2.  **Récupération de la mémoire (Balayage et Compactage) :** Une fois que les objets actifs sont marqués, le ramasse-miettes doit récupérer la mémoire occupée par les objets non marqués (inatteignables). Différents algorithmes de garbage collection utilisent différentes stratégies pour cela :

    * **Marquage et Balayage :** Cet algorithme identifie et marque les objets actifs, puis balaie la mémoire, libérant l'espace occupé par les objets non marqués. Cela peut entraîner une fragmentation de la mémoire (de petits blocs de mémoire libre éparpillés qui ne sont pas assez grands pour allouer de nouveaux objets).
    * **Marquage et Compactage :** Cet algorithme marque également les objets actifs. Après le marquage, il déplace (compacte) les objets actifs ensemble en mémoire, éliminant la fragmentation et facilitant l'allocation de blocs de mémoire contigus pour de nouveaux objets.
    * **Copie :** Cet algorithme divise la mémoire en deux régions ou plus. Les objets actifs sont copiés d'une région à une autre, récupérant ainsi efficacement l'espace dans la région d'origine.

**Concepts clés dans le Garbage Collection Java :**

* **Tas (Heap) :** La zone de mémoire où les objets sont alloués en Java. Le ramasse-miettes opère principalement sur le tas.
* **Jeune Génération (Nursery) :** Il s'agit d'une partie du tas où les objets nouvellement créés sont initialement alloués. Elle est elle-même divisée en :
    * **Espace Eden :** Là où la plupart des nouveaux objets sont créés.
    * **Espaces Survivants (S0 et S1) :** Utilisés pour contenir les objets qui ont survécu à quelques cycles de garbage collection mineurs.
* **Vieille Génération (Tenured Generation) :** Les objets qui ont survécu à plusieurs cycles de garbage collection dans la jeune génération sont finalement déplacés vers la vieille génération. Les objets dans la vieille génération sont généralement de longue durée de vie.
* **Génération Permanente (PermGen) / Metaspace :** Dans les anciennes versions de Java (avant Java 8), la Génération Permanente stockait les métadonnées sur les classes et les méthodes. Dans Java 8 et les versions ultérieures, celle-ci a été remplacée par Metaspace, qui fait partie de la mémoire native (et non du tas Java).
* **Algorithmes de Garbage Collection :** Différents algorithmes sont utilisés pour le garbage collection, chacun ayant ses propres compromis en termes de performances et d'efficacité.

**Garbage Collection Générationnel :**

La JVM Java HotSpot (la JVM la plus courante) utilise une approche générationnelle pour le garbage collection. Celle-ci est basée sur l'observation que la plupart des objets dans une application ont une durée de vie courte.

1.  **GC Mineur (Young Generation GC) :** Lorsque l'espace Eden est plein, un GC mineur est déclenché. Les objets actifs d'Eden et d'un des espaces Survivants (par exemple, S0) sont copiés vers l'autre espace Survivant (S1). Les objets qui ont survécu à un certain nombre de cycles de GC mineurs sont déplacés vers la vieille génération. Les objets inatteignables sont supprimés.

2.  **GC Majeur (Old Generation GC) / GC Complet :** Lorsque la vieille génération est pleine, un GC majeur (ou parfois un GC complet, qui peut impliquer à la fois les générations jeune et vieille) est effectué. Ce processus est généralement plus long qu'un GC mineur et peut entraîner des pauses plus longues dans l'exécution de l'application.

**Ramasse-miettes courants dans la JVM Java HotSpot :**

La JVM Java HotSpot propose plusieurs algorithmes de garbage collection qui peuvent être choisis en fonction des besoins de l'application (par exemple, faible latence, haut débit). Voici quelques-uns des plus courants :

* **Ramasse-miettes Sériel :** Utilise un seul thread pour le garbage collection. Convient aux petites applications avec des ressources limitées.
* **Ramasse-miettes Parallèle :** Utilise plusieurs threads pour le garbage collection, améliorant le débit. Convient aux applications avec des jeux de données de taille modérée à grande fonctionnant sur des processeurs multi-cœurs.
* **Ramasse-miettes CMS (Concurrent Mark Sweep) :** Tente de minimiser les temps de pause en effectuant la majeure partie du travail de garbage collection concurremment avec les threads de l'application. Cependant, il peut entraîner une fragmentation et pourrait nécessiter un GC complet éventuellement.
* **Ramasse-miettes G1 (Garbage-First) :** Vise à fournir un bon équilibre entre débit et faible latence. Il divise le tas en régions et priorise la collecte des déchets des régions contenant le plus de déchets. C'est le collecteur par défaut dans Java 9 et les versions ultérieures.
* **Ramasse-miettes ZGC (Z Garbage Collector) :** Un ramasse-miettes à faible latence conçu pour les gros tas. Il vise des temps de pause inférieurs à 10 ms.
* **Shenandoah :** Un autre ramasse-miettes à faible latence avec des objectifs similaires à ZGC.

Vous pouvez spécifier quel ramasse-miettes utiliser via les options en ligne de commande de la JVM.

**Quand le Garbage Collection s'exécute-t-il ?**

Le garbage collection est principalement un processus automatique piloté par la JVM. Il s'exécute généralement lorsque :

* La jeune génération (espace Eden) est pleine.
* La vieille génération est pleine.
* Le système est à court de mémoire.

Bien que vous ne puissiez pas contrôler directement *quand* le garbage collection s'exécutera, vous pouvez suggérer à la JVM que c'est peut-être un bon moment pour effectuer le garbage collection en utilisant `System.gc()`. Cependant, il n'y a aucune garantie que la JVM exécutera effectivement le ramasse-miettes immédiatement ou du tout lorsque vous appelez cette méthode. Il est généralement préférable de s'appuyer sur le mécanisme de garbage collection automatique de la JVM.

**`System.gc()` et Finalisation :**

* **`System.gc()` :** Comme mentionné, il s'agit d'une demande à la JVM pour exécuter le ramasse-miettes. Il est souvent conseillé d'éviter de compter sur cette méthode pour la gestion critique de la mémoire, car la JVM est généralement meilleure pour décider du moment où effectuer le GC.
* **Méthode `finalize()` :** Avant qu'un objet ne soit garbage collecté, la JVM lui donne une chance d'effectuer des opérations de nettoyage en appelant sa méthode `finalize()` (si elle est implémentée). Cependant, `finalize()` présente plusieurs inconvénients et est généralement déconseillée dans le développement Java moderne. Elle peut introduire des problèmes de performance et rendre le garbage collection moins prévisible. Envisagez d'utiliser d'autres mécanismes comme try-with-resources pour la gestion des ressources.

**Impact du Garbage Collection sur les Performances de l'Application :**

Bien que le garbage collection soit essentiel pour la gestion de la mémoire, il peut également affecter les performances d'une application en raison des pauses "stop-the-world". Pendant ces pauses, tous les threads de l'application sont arrêtés pendant que le ramasse-miettes effectue son travail. La durée et la fréquence de ces pauses dépendent de l'algorithme de garbage collection utilisé ainsi que de la taille et des caractéristiques du tas.

Les ramasse-miettes à faible latence comme G1, ZGC et Shenandoah visent à minimiser ces temps de pause pour rendre les applications plus réactives.

**Ajustement du Garbage Collection :**

Pour les applications ayant des exigences de performance spécifiques, le garbage collection peut être ajusté en modifiant les paramètres de la JVM tels que :

* La taille du tas (`-Xms`, `-Xmx`)
* La taille de la jeune génération (`-Xmn`)
* Les ratios des espaces survivants (`-XX:SurvivorRatio`)
* Le choix d'un ramasse-miettes spécifique (`-XX:+UseG1GC`, `-XX:+UseZGC`, etc.)
* La définition de drapeaux de garbage collection pour un contrôle plus fin.

L'ajustement du GC est un sujet avancé et nécessite généralement une analyse minutieuse du comportement et des performances de l'application.

**Bonnes pratiques pour écrire un code adapté au Garbage Collection :**

Bien que Java gère la mémoire automatiquement, écrire du code en pensant au ramasse-miettes peut conduire à de meilleures performances :

* **Minimiser la création d'objets :** Créer un grand nombre d'objets à courte durée de vie peut exercer une pression sur le ramasse-miettes. Essayez de réutiliser les objets lorsque c'est approprié.
* **Libérer les références d'objets :** Si vous avez une référence vers un objet dont vous n'avez plus besoin, définissez la référence sur `null`. Cela rend l'objet éligible au garbage collection plus rapidement.
* **Utiliser les structures de données judicieusement :** Choisissez des structures de données adaptées à vos besoins. Par exemple, utiliser une grande `ArrayList` puis supprimer la plupart de ses éléments peut être inefficace.
* **Éviter les finaliseurs :** Comme mentionné précédemment, évitez de compter sur la méthode `finalize()` pour le nettoyage des ressources. Utilisez try-with-resources pour les ressources comme les fichiers et les connexions réseau.
* **Faire attention aux variables statiques :** Les objets référencés par des variables statiques vivront pendant toute la durée de l'application, soyez donc prudent lorsque vous stockez de gros objets ou des objets inutiles dans des champs statiques.

**En résumé :**

Le Garbage Collection en Java est un processus automatique de gestion de la mémoire qui récupère la mémoire occupée par des objets inutilisés. Il simplifie le développement en libérant les développeurs de la gestion manuelle de la mémoire. Comprendre son fonctionnement, les différentes générations du tas et les algorithmes de garbage collection disponibles peut vous aider à écrire des applications Java plus efficaces et performantes.