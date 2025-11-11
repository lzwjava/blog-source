---
audio: false
generated: true
lang: fr
layout: post
title: Comprendre Git Fetch
translated: true
type: note
---

Permettez-moi d'expliquer la commande Git `/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=5 origin` étape par étape. Cette commande est utilisée pour récupérer les mises à jour d'un dépôt Git distant avec des options spécifiques pour contrôler quelles données sont récupérées et en quelle quantité. Voici une analyse détaillée :

### Analyse de la Commande

1.  **`/usr/bin/git`**
    Il s'agit simplement du chemin vers l'exécutable Git sur le système. Il indique au système d'exécuter le programme Git avec les options et la commande qui suivent.

2.  **`-c protocol.version=2`**
    Cela définit une option de configuration pour cette commande Git spécifique, l'obligeant à utiliser la version 2 du protocole lors de la communication avec le dépôt distant. La version 2 du protocole est une version plus récente du protocole de communication de Git, qui peut offrir des performances ou des fonctionnalités améliorées par rapport à l'ancienne version 1.

3.  **`fetch`**
    La commande `fetch` récupère les mises à jour (comme les nouveaux commits et branches) d'un dépôt distant. Contrairement à `pull`, elle ne fusionne pas ces changements dans vos branches locales—elle met seulement à jour vos *branches de suivi distantes* (par exemple, `origin/main`) afin que vous puissiez voir ce qu'il y a de nouveau sur le dépôt distant.

4.  **`--no-tags`**
    Normalement, `fetch` récupère également les tags (des étiquettes qui marquent des commits spécifiques, comme les numéros de version pour les releases). Cette option indique à Git de *ne pas* récupérer les tags du dépôt distant, gardant ainsi votre dépôt local exempt de ces marqueurs.

5.  **`--prune`**
    Cette option nettoie vos branches de suivi distantes locales. Si une branche a été supprimée sur le dépôt distant, `--prune` supprime la branche de suivi distante correspondante (par exemple, `origin/old-branch`) de votre dépôt local, maintenant ainsi l'ordre.

6.  **`--no-recurse-submodules`**
    Les submodules sont des dépôts séparés imbriqués dans votre dépôt principal. Par défaut, `fetch` pourrait également récupérer les mises à jour pour ces submodules. Cette option empêche cela, de sorte que seules les données du dépôt principal sont récupérées, ignorant tout submodule.

7.  **`--depth=5`**
    Cette option crée un *fetch shallow* (récupération peu profonde), limitant l'historique aux 5 derniers commits pour chaque branche. Au lieu de télécharger l'intégralité de l'historique des commits, vous obtenez une version tronquée, ce qui permet de gagner du temps et de l'espace disque—utile si vous n'avez pas besoin de l'historique complet.

8.  **`origin`**
    Il s'agit du nom du dépôt distant depuis lequel vous effectuez la récupération. `origin` est le nom par défaut que Git donne au dépôt distant principal lorsque vous clonez un projet. Cette commande récupère donc les mises à jour depuis cette source.

### Que Fait Globalement Cette Commande ?

Cette commande Git récupère les mises à jour du dépôt distant `origin` avec plusieurs contraintes :

- Elle utilise la version 2 du protocole pour la communication.
- Elle ne récupère que les 5 derniers commits par branche (`--depth=5`).
- Elle ignore la récupération des tags (`--no-tags`).
- Elle supprime toute branche de suivi distante locale qui n'existe plus sur le dépôt distant (`--prune`).
- Elle ignore les submodules (`--no-recurse-submodules`).

En bref, c'est une méthode légère pour mettre à jour votre vue locale du dépôt distant, en se concentrant sur les changements récents et en évitant les données supplémentaires comme les tags, les submodules ou l'historique complet. Cela peut être utilisé pour économiser de la bande passante, accélérer le processus ou garder votre dépôt local minimal.

### Exemple de Scénario
Imaginez que vous travaillez sur un projet avec un grand dépôt, et que vous avez seulement besoin des derniers changements de la branche `main` pour vérifier quelque chose rapidement. Exécuter cette commande permettrait de :
- Mettre à jour `origin/main` avec les 5 derniers commits.
- Supprimer les branches obsolètes (par exemple, si `origin/feature-x` a été supprimée à distance).
- Ignorer les tags et les submodules, rendant votre opération `fetch` rapide et ciblée.

C'est tout ! Cette commande est entièrement axée sur l'efficacité et le contrôle lors de la synchronisation avec un dépôt distant.