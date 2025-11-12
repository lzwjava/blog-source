---
audio: false
generated: true
lang: fr
layout: post
title: Modèle de mémoire Java
translated: true
type: note
---

Plongeons dans le Java Memory Model (JMM) ! C'est un concept fondamental pour comprendre le comportement des programmes Java multithreadés, en particulier lorsqu'ils manipulent des données partagées.

**Qu'est-ce que le Java Memory Model (JMM) ?**

Le Java Memory Model est une description abstraite de la manière dont les threads d'un programme Java interagissent avec la mémoire. Il définit les règles qui régissent comment et quand les modifications apportées par un thread aux variables partagées sont visibles par les autres threads. Ce n'est pas une architecture mémoire physique, mais plutôt un ensemble de règles que la JVM doit suivre pour garantir un comportement cohérent et prévisible des programmes concurrents sur différentes plates-formes matérielles.

**Pourquoi le Java Memory Model est-il nécessaire ?**

Dans un environnement multithreadé, plusieurs threads peuvent accéder et modifier des variables partagées. Sans un modèle de mémoire bien défini, plusieurs problèmes peuvent survenir :

* **Problèmes de visibilité :** Les modifications apportées par un thread à une variable partagée pourraient ne pas être immédiatement visibles par les autres threads. Cela peut se produire en raison d'optimisations comme la mise en cache, où chaque thread peut avoir sa propre copie locale de la variable.
* **Problèmes d'ordonnancement :** L'ordre dans lequel les opérations apparaissent dans le code source pourrait ne pas être le même que l'ordre dans lequel elles sont réellement exécutées par le processeur. Les compilateurs et les processeurs peuvent réordonnancer les instructions pour optimiser les performances. Bien que cela soit généralement sûr dans les programmes mono-thread, cela peut entraîner un comportement inattendu dans les programmes multithreadés s'il n'est pas géré correctement.
* **Problèmes d'atomicité :** Certaines opérations qui semblent être des opérations uniques dans le code source pourraient être décomposées en plusieurs étapes plus petites au niveau du processeur. Dans un environnement multithreadé, ces étapes pourraient être entrelacées avec des opérations d'autres threads, conduisant à des résultats incohérents.

Le JMM fournit un cadre pour résoudre ces problèmes et garantit que les programmes concurrents se comportent correctement, quelle que soit l'architecture matérielle sous-jacente.

**Architecture abstraite du JMM :**

Le JMM définit une relation abstraite entre les threads et la mémoire principale :

1.  **Mémoire principale :** C'est l'endroit où résident toutes les variables partagées. C'est comme le stockage central pour toutes les données accessibles par plusieurs threads.
2.  **Mémoire de travail (Cache local) :** Chaque thread possède sa propre mémoire de travail (conceptuellement similaire aux caches CPU). Lorsqu'un thread a besoin d'accéder à une variable partagée, il copie d'abord la variable de la mémoire principale dans sa mémoire de travail. Lorsque le thread modifie la variable, il le fait généralement dans sa mémoire de travail, et la modification est éventuellement écrite dans la mémoire principale.

**Défis clés abordés par le JMM :**

* **Visibilité :** Le JMM définit des règles sur le moment et la manière dont les modifications apportées par un thread à une variable partagée dans sa mémoire de travail sont rendues visibles aux autres threads (c'est-à-dire, écrites dans la mémoire principale et lues ultérieurement par d'autres threads).
* **Ordonnancement :** Le JMM spécifie des contraintes sur la façon dont le compilateur et le processeur peuvent réordonnancer les instructions pour garantir l'existence d'une relation happens-before cohérente entre certaines opérations dans différents threads.

**La relation "Happens-Before" :**

La relation "happens-before" est le concept le plus fondamental du JMM. Elle définit un ordre partiel des opérations dans un programme. Si une opération se produit avant (happens-before) une autre, alors les effets de la première opération (par exemple, une écriture dans une variable) sont garantis d'être visibles par la seconde opération.

Voici quelques règles clés "happens-before" définies par le JMM :

1.  **Règle de l'ordre du programme :** Au sein d'un même thread, chaque action dans le programme se produit avant (happens-before) chaque action qui la suit dans l'ordre du programme.

2.  **Règle du verrou de moniteur :** Une opération de déverrouillage (unlock) sur un moniteur (le verrou associé aux blocs ou méthodes `synchronized`) se produit avant (happens-before) toute opération de verrouillage (lock) ultérieure sur le même moniteur. Cela garantit que lorsqu'un thread libère un verrou, toutes les modifications qu'il a apportées dans le bloc synchronisé sont visibles par le thread suivant qui acquiert le même verrou.

3.  **Règle des variables volatiles :** Une opération d'écriture dans une variable `volatile` se produit avant (happens-before) toute opération de lecture ultérieure de la même variable. Cela garantit que lorsqu'un thread écrit dans une variable `volatile`, la valeur est immédiatement écrite dans la mémoire principale, et tout autre thread lisant cette variable obtiendra la dernière valeur.

4.  **Règle du démarrage de thread :** La méthode start() d'un objet Thread se produit avant (happens-before) toute action dans le thread nouvellement démarré.

5.  **Règle de terminaison de thread :** Toutes les actions d'un thread, y compris les écritures dans les variables partagées, se produisent avant (happens-before) le retour réussi de la méthode join() de ce thread ou avant qu'un autre thread ne détecte que le thread a terminé (par exemple, en vérifiant `isAlive()`).

6.  **Transitivité :** Si l'opération A se produit avant (happens-before) l'opération B, et que l'opération B se produit avant (happens-before) l'opération C, alors l'opération A se produit avant (happens-before) l'opération C.

7.  **Règle de création d'objet :** L'achèvement du constructeur d'un objet se produit avant (happens-before) le début de toute autre opération utilisant cet objet.

**Constructions linguistiques clés et le JMM :**

* **Mot-clé `volatile` :** Déclarer une variable comme `volatile` a deux effets principaux liés au JMM :
    * **Visibilité :** Garantit que toutes les écritures dans cette variable seront immédiatement écrites dans la mémoire principale, et que toutes les lectures récupéreront la dernière valeur depuis la mémoire principale. Cela empêche les threads d'utiliser des valeurs mises en cache obsolètes.
    * **Interdit le réordonnancement d'instructions (dans une certaine mesure) :** Empêche certains types de réordonnancement d'instructions qui pourraient conduire à un comportement incorrect dans les programmes multithreadés. Plus précisément, les opérations précédant une écriture dans une variable `volatile` ne peuvent pas être réordonnées après l'écriture, et les opérations suivant une lecture d'une variable `volatile` ne peuvent pas être réordonnées avant la lecture.

* **Mot-clé `synchronized` :** Lorsqu'un thread entre dans un bloc ou une méthode `synchronized`, il acquiert un verrou sur le moniteur associé. Le JMM garantit :
    * **Exclusion mutuelle (Atomicité) :** Un seul thread peut détenir le verrou pour un moniteur particulier à un moment donné, garantissant que le code dans le bloc synchronisé est exécuté de manière atomique par rapport aux autres threads se synchronisant sur le même moniteur.
    * **Visibilité :** Lorsqu'un thread libère le verrou (en sortant du bloc ou de la méthode `synchronized`), il rafraîchit efficacement toutes les modifications qu'il a apportées aux variables partagées dans ce bloc vers la mémoire principale. Lorsqu'un autre thread acquiert le même verrou, il relira les variables partagées depuis la mémoire principale, garantissant ainsi qu'il verra les dernières mises à jour.

* **Champs `final` :** Le JMM fournit des garanties concernant la visibilité des champs `final`. Une fois qu'un champ `final` est correctement initialisé dans le constructeur d'un objet, sa valeur sera visible par tous les autres threads sans avoir besoin d'une synchronisation explicite. En effet, l'écriture dans un champ `final` dans le constructeur se produit avant (happens-before) que tout autre thread puisse accéder à l'objet.

**Implications pour la programmation concurrente :**

Comprendre le JMM est crucial pour écrire des programmes concurrents corrects et efficaces en Java. En respectant les règles définies par le JMM et en utilisant des mécanismes de synchronisation appropriés (`volatile`, `synchronized`, les verrous du package `java.util.concurrent`), les développeurs peuvent s'assurer que les données partagées sont accédées et modifiées en toute sécurité par plusieurs threads.

**Pièges courants et comment le JMM aide :**

* **Conditions de course :** Se produisent lorsque le résultat d'un programme dépend de l'ordre imprévisible dans lequel plusieurs threads accèdent aux ressources partagées. Le JMM, associé à une synchronisation appropriée, aide à prévenir les conditions de course en garantissant que l'accès aux variables partagées est correctement coordonné.
* **Courses aux données :** Se produisent lorsque plusieurs threads accèdent à la même variable partagée de manière concurrente, et qu'au moins un des accès est une écriture, sans aucune synchronisation. Le JMM définit que si un programme a une course aux données, son comportement est indéfini. L'utilisation de `volatile` ou `synchronized` aide à prévenir les courses aux données.
* **Problèmes d'exécution hors ordre :** Sans les garanties du JMM, le compilateur ou le processeur pourrait réordonnancer les opérations d'une manière qui brise la logique prévue d'un programme multithreadé. Le JMM impose des contraintes sur le réordonnancement, en particulier autour des variables `volatile` et des blocs synchronisés, pour empêcher de tels problèmes.

**En résumé :**

Le Java Memory Model est un ensemble de règles qui régissent la manière dont les threads interagissent avec la mémoire en Java. Il aborde les défis liés à la visibilité, l'ordonnancement et l'atomicité dans les programmes multithreadés. Les concepts clés incluent la mémoire principale, la mémoire de travail et la relation "happens-before". Les constructions linguistiques comme `volatile` et `synchronized` fournissent des mécanismes pour garantir un comportement correct et prévisible dans les applications Java concurrentes en adhérant aux spécifications du JMM. Comprendre le JMM est essentiel pour écrire du code Java multithreadé robuste et efficace.