---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Optimisation de la collecte des déchets Git expliquée
translated: true
type: note
---

### Fonctionnement de Git GC
Git GC (garbage collection) est une commande de maintenance qui optimise votre dépôt Git en nettoyant les fichiers inutiles et en compressant les données pour économiser de l'espace et améliorer les performances. Elle opère sur le répertoire `.git`, qui stocke l'ensemble de l'historique, des objets et des métadonnées d'un dépôt.

Actions clés qu'elle effectue :
- **Élagage des objets inaccessibles** : Supprime les commits, les arbres (trees) et les blobs (blobs) qui ne sont plus référencés (par exemple, après un rebasage ou une suppression de branches). Ceux-ci deviennent des "objets libres" (loose objects) dans `.git/objects`, et GC les nettoie.
- **Recompression des objets** : Compresse les objets libres (stockés individuellement) en fichiers pack (`.git/objects/pack`), ce qui est plus efficace. Cela utilise la compression delta pour stocker les différences entre des fichiers similaires, réduisant ainsi l'utilisation du disque.
- **Mise à jour des références** : Actualise l'état interne du dépôt, comme la réécriture de l'index des packs pour des recherches plus rapides.
- **Exécution d'outils associés** : Elle invoque souvent des commandes comme `git prune`, `git repack` et `git rerere` (pour la réutilisation des résolutions) dans le cadre du processus.

Preuve : D'après la documentation officielle de Git (par exemple, `git gc --help`), GC est conçu pour effectuer le "ménage" des dépôts. Par exemple, un dépôt avec 10 000 objets libres pourrait passer de plusieurs centaines de Mo à une fraction de cette taille une fois compressé, car la compression delta tire parti des similitudes (par exemple, entre les versions de fichiers dans un historique de code).

### Fonctionnement interne
1. **Déclencheurs** : GC s'exécute manuellement via `git gc` ou automatiquement lorsque Git détecte certaines conditions (voir ci-dessous). Il ne s'exécute pas à chaque commande pour éviter les ralentissements.
2. **Processus** :
   - Compte les objets libres et les fichiers de pack.
   - Si les seuils sont dépassés (par exemple, >6 700 objets libres par défaut, configurable via `gc.auto`), il recompresse de manière agressive.
   - Il crée des fichiers temporaires (par exemple, `.git/objects/tmp_*`) pour éviter la perte de données, puis les remplace de manière atomique.
   - Les modes plus légers comme `git gc --auto` se contentent d'élaguer sans effectuer de recompression complète.
3. **Détails de la compression** : Utilise zlib pour la compression. La recompression construit des fichiers pack où les objets sont stockés sous forme de deltas (différences) par rapport à des objets de base, ce qui est efficace pour les dépôts avec un code en évolution – par exemple, ajouter une ligne à un fichier dans une grande base de code crée un petit delta au lieu de dupliquer l'intégralité du fichier.

Ceci est étayé par le code source de Git (disponible sur GitHub), qui implémente GC comme une série d'appels shell aux utilitaires d'élagage et de compression pour la fiabilité.

### Pourquoi il s'exécute soudainement
GC se déclenche souvent "soudainement" car il est automatique, mais pas en temps réel, pour équilibrer les performances. Raisons courantes :
- **Seuils atteints** : Après l'accumulation d'objets libres (par exemple, à partir de commits ou de récupérations (fetch) fréquents sans compression). Git vérifie cela après des opérations comme `git commit`, `git merge` ou `push`. Si les objets libres dépassent la limite `gc.auto` (par défaut : environ 6 700), il s'exécute. C'est pourquoi cela peut se produire après une série d'activités, semblant "soudain".
- **Planification de l'élagage** : Si `gc.prune` est défini, il élague les références obsolètes périodiquement, mais le GC automatique principal est basé sur le nombre d'objets.
- **Opérations volumineuses** : Un rebasage lourd ou un clonage peut générer rapidement de nombreux objets libres, le déclenchant.
- **Hooks post-commande** : Certains workflows ou outils (par exemple, les hooks Git ou les IDE) peuvent invoquer `git gc` après de gros changements.

Pour le contrôler : Ajustez les paramètres comme `git config --global gc.auto 0` pour désactiver le GC automatique si vous préférez des exécutions manuelles, ou augmentez le seuil pour réduire les interruptions. L'exécuter empêche les dépôts de gonfler – par exemple, le dépôt du noyau Linux utilise GC pour garder l'historique gérable malgré son échelle massive. Si les problèmes persistent, vérifiez `git count-objects -v` pour les statistiques sur les objets libres.