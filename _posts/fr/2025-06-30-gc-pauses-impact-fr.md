---
audio: false
generated: true
lang: fr
layout: post
title: 'Pauses du ramasse-miettes Go : Cloudflare contre TiDB'
translated: true
type: note
---

Oui, les pauses du ramasse-miettes (GC) de Go peuvent impacter à la fois les services de Cloudflare et la base de données TiDB, car les deux utilisent massivement Go dans leur architecture. Cependant, la nature et l'impact de ces pauses, ainsi que la manière dont elles sont atténuées, diffèrent.

Voici une analyse détaillée :

**Le GC de Go et ses caractéristiques :**

* **GC Marque-Balayage :** Go utilise un ramasse-miettes concurrent, de type marque-balayage à trois couleurs. Cela signifie que la majeure partie du travail du GC (marquer les objets vivants) se produit de manière concurrente avec l'exécution de l'application.
* **Pauses "Stop-the-World" (STW) :** Bien que concurrent, le GC de Go nécessite toujours de brèves pauses "stop-the-world" (STW). Ces pauses se produisent lors de phases spécifiques (comme la configuration initiale du "marquage" et les phases finales de "terminaison du marquage" et de "terminaison du balayage") où les goroutines de l'application sont suspendues pour garantir la cohérence de la mémoire. L'objectif des ingénieurs du runtime Go est de minimiser la durée de ces pauses STW, les maintenant généralement dans la plage de la microseconde.
* **Facteurs influençant le GC :** La fréquence et la durée des pauses du GC sont influencées par :
    * **Le taux d'allocation :** La rapidité avec laquelle l'application alloue de nouvelle mémoire.
    * **La taille du tas :** La quantité totale de mémoire gérée par le runtime Go.
    * **`GOGC` :** Un paramètre qui contrôle le pourcentage cible du ramasse-miettes (valeur par défaut 100%). Un `GOGC` plus bas signifie des GC plus fréquents.
    * **`GOMEMLIMIT` :** Un nouveau paramètre (Go 1.19+) qui définit une limite supérieure pour la taille cible du tas, aidant à prévenir les OOM et à gérer la mémoire de manière plus prévisible.

**Impact sur Cloudflare :**

Cloudflare utilise Go de manière extensive pour nombre de ses services critiques, y compris l'infrastructure DNS, le traitement SSL, les tests de charge, et plus encore. Pour un système haute performance et à faible latence comme Cloudflare, même des pauses de l'ordre de la microseconde peuvent être significatives.

* **Services sensibles à la latence :** Les services traitant un taux de requêtes élevé (comme le DNS ou le proxying) sont très sensibles aux pics de latence. Les pauses du GC, même courtes, peuvent contribuer à ces pics, affectant l'expérience utilisateur.
* **Applications gourmandes en mémoire :** Certains services Cloudflare peuvent être gourmands en mémoire, conduisant à des cycles de GC plus fréquents s'ils ne sont pas correctement réglés.
* **Atténuation chez Cloudflare :** Les ingénieurs de Cloudflare travaillent activement sur :
    * **Le réglage de `GOGC` et `GOMEMLIMIT` :** Ils expérimentent avec ces paramètres pour équilibrer l'utilisation de la mémoire et la fréquence du GC.
    * **Le profilage et l'optimisation du code :** Identifier et réduire les allocations de mémoire inutiles dans leur code Go.
    * **Les Optimisations Guidées par le Profilage (PGO) :** Cloudflare a constaté des économies significatives de CPU (et donc probablement une réduction de la pression sur le GC) en utilisant la fonctionnalité PGO de Go.
    * **Considérations architecturales :** Concevoir des services résilients aux courtes pauses, potentiellement en ayant suffisamment de redondance ou en traitant les requêtes d'une manière qui minimise l'impact de la pause d'une seule goroutine.

**Impact sur TiDB Database :**

TiDB est une base de données SQL distribuée construite par PingCAP, dont la couche SQL (`tidb-server`) est principalement écrite en Go. En tant que base de données, elle a des caractéristiques et des exigences de performance différentes d'un service de proxy.

* **GC spécifique à la base de données :** TiDB a ses propres mécanismes de garbage collection pour les données MVCC (Multi-Version Concurrency Control) (nettoyage des anciennes versions de données dans TiKV, son moteur de stockage). Ceci est distinct du GC du runtime Go, bien que le "coordinateur" TiDB (écrit en Go) initie et gère ce processus.
* **GC du Runtime Go dans TiDB :** Le GC de Go *impacte* bel et bien TiDB car `tidb-server` traite les requêtes SQL, gère la mémoire pour les plans de requête, les résultats et autres données d'exécution.
    * **Variabilité de la latence :** Des pauses STW fréquentes peuvent entraîner des pics de latence dans l'exécution des requêtes, affectant la réactivité de la base de données.
    * **Surcharge CPU :** L'activité du GC consomme des ressources CPU, qui pourraient autrement être utilisées pour traiter les requêtes.
    * **Déclenchement adaptatif du GC :** TiDB déclenche proactivement le GC de Go lorsque l'utilisation de la mémoire atteint un certain seuil (configurable via `tidb_server_memory_limit` et `tidb_server_memory_limit_gc_trigger`). Il utilise également une stratégie adaptative pour `tidb_server_memory_limit_gc_trigger` pour éviter des GC excessivement fréquents.
* **Surveillance et Réglage :** PingCAP fournit des outils de surveillance étendus (comme le Tableau de bord Runtime de TiDB) pour observer le comportement du GC de Go (fréquence du GC, durée, latence STW, temps CPU consacré au GC) et permet aux utilisateurs de configurer `GOGC` et `GOMEMLIMIT` pour optimiser les performances.
* **Efforts continus :** Les ingénieurs de PingCAP travaillent continuellement à l'optimisation de la gestion de la mémoire Go et du comportement du GC dans TiDB pour minimiser son impact sur les performances et la stabilité.

**En résumé :**

Cloudflare et TiDB, étant des systèmes haute performance s'appuyant sur Go, sont tous deux susceptibles de subir les impacts des pauses du GC de Go. Bien que le GC de Go soit hautement optimisé pour de courtes durées STW, à grande échelle, ces pauses peuvent contribuer à des pics de latence et à une surcharge CPU. Les deux entreprises surveillent, règlent et optimisent activement leurs applications et infrastructures Go pour atténuer ces effets, en tirant parti des paramètres du runtime Go et de leurs propres conceptions architecturales spécifiques.