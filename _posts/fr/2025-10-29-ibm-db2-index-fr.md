---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Structure des index IBM DB2 expliquée
translated: true
type: note
---

### Fonctionnement des index IBM DB2

IBM DB2 utilise des **arbres B+** comme structure de données principale pour ses index. Il s'agit d'une variante d'arbre équilibré optimisée pour le stockage sur disque et les requêtes par plage, courants dans les bases de données relationnelles. Les arbres B+ garantissent des recherches, des insertions et des suppressions efficaces avec une complexité temporelle logarithmique (O(log n)), ce qui les rend idéaux pour les grands ensembles de données. Ci-dessous, je détaillerai la structure, les opérations clés et les notes spécifiques à DB2.

#### Structure de l'arbre B+ dans DB2
Un arbre B+ dans DB2 est organisé en une hiérarchie de **pages** (également appelées nœuds), chacune ayant typiquement une taille de 4 Ko sur le disque. L'arbre est auto-équilibrant, ce qui signifie que toutes les feuilles sont à la même profondeur, et il croît ou se réduit dynamiquement au fur et à mesure des modifications des données. Voici le détail :

- **Page Racine** : Le point d'entrée au sommet de l'arbre. Elle contient des valeurs de clés triées et des pointeurs vers les pages enfants en dessous. Pour les petits index, la racine peut pointer directement vers les pages feuilles.
  
- **Pages Internes (Non Feuilles)** : Ces niveaux intermédiaires agissent comme des répertoires. Chaque page contient :
  - Une liste triée de **clés d'index** (les valeurs de la ou des colonnes indexées, par exemple, les ID d'employé).
  - Des pointeurs vers les pages enfants (un pointeur de plus que de clés, séparant les plages).
  - Plus précisément, chaque entrée est la **valeur de clé la plus élevée** dans le sous-arbre en dessous, associée à un **Identifiant d'Enregistrement (RID)** — un pointeur unique vers la page et l'emplacement où la ligne de données réelle réside dans la table.
  
  Les pages non feuilles ne stockent *pas* de pointeurs de données réels ; elles guident le parcours.

- **Pages Feuilles** : Le niveau le plus bas, lié bidirectionnellement (avant et arrière) pour des analyses séquentielles efficaces. Chaque page feuille contient :
  - Les **valeurs de clés** complètes et triées provenant de la ou des colonnes indexées.
  - Les **RID** associés pointant directement vers les lignes de la table.
  - Des pointeurs vers les pages feuilles adjacentes, permettant un accès séquentiel (par exemple, pour `WHERE colonne BETWEEN x AND y`).

L'arbre commence avec au moins 2 niveaux (racine + feuilles) et peut atteindre 3–5+ niveaux pour les tables massives (millions de lignes). Le nombre de niveaux (NLEVELS) peut être interrogé via `SYSCAT.INDEXES` et impacte les performances — moins il y a de niveaux, plus les parcours sont rapides, mais DB2 gère cela automatiquement.

Les index sont stockés séparément des tables dans leur propre tablespace, consommant de l'espace disque proportionnel aux données indexées (par exemple, un index unique sur une table de 1 million de lignes pourrait prendre ~10–20 % de la taille de la table).

#### Fonctionnement de la recherche
1. Commencez à la **page racine** et chargez-la en mémoire.
2. Comparez la clé de recherche (par exemple, `WHERE id = 123`) aux clés triées dans la page courante.
3. Sélectionnez le pointeur enfant approprié (par exemple, si clé de recherche > clé courante, allez à droite).
4. Répétez le long de l'arbre (généralement 1–5 opérations d'E/S) jusqu'à atteindre une **page feuille**.
5. Dans la feuille, parcourez les clés triées pour trouver les correspondances, puis utilisez le RID pour récupérer la ligne exacte dans la table (une opération d'E/S supplémentaire).

Cette compression de chemin maintient les parcours peu profonds. Pour les requêtes par plage, une fois la feuille de départ atteinte, suivez les liens frères pour analyser séquentiellement sans remonter dans l'arbre.

#### Insertion et Suppression
- **Insertion** :
  1. Parcourez jusqu'à la feuille correcte (comme dans la recherche).
  2. Insérez la nouvelle clé + RID dans la page feuille triée.
  3. Si la page déborde (dépasse le nombre maximum d'entrées, ~200–500 selon la taille de la clé), divisez-la en deux pages et insérez une clé de séparation dans la page parent (interne).
  4. Si le parent déborde, divisez vers le haut (peut créer une nouvelle racine). DB2 verrouille brièvement les pages pour la concurrence.

- **Suppression** :
  1. Parcourez jusqu'à la feuille et supprimez la clé + RID.
  2. Si la page est en sous-charge (trop peu d'entrées), empruntez à une page sœur ou fusionnez avec elle, en supprimant la clé de séparation du parent.
  3. Propagez les fusions vers le haut si nécessaire. DB2 peut retarder la réorganisation pour regrouper les changements pour plus d'efficacité.

Ces opérations maintiennent l'équilibre automatiquement, avec un minimum de divisions/fusions de pages (~1 % des opérations).

#### Fonctionnalités spécifiques à DB2
- **Arbres B+ Optimisés** (dans DB2 pour z/OS) : Améliorés pour la concurrence mainframe, avec prélecture fractale pour prédire et précharger les pages, réduisant les E/S.
- **Clustering** : Les index peuvent être "clusterisés" (données physiquement triées selon l'ordre de l'index) pour de meilleures performances sur les plages.
- **Types** : Prend en charge les index uniques, composites (multi-colonnes) et bitmap, tous basés sur B+. Pas d'index de hachage natifs.
- **Maintenance** : Exécutez `RUNSTATS` après des changements en masse pour mettre à jour les statistiques pour l'optimiseur. Des outils comme `INSPECT` vérifient les problèmes.

Les arbres B+ excellent dans DB2 car ils minimisent les E/S aléatoires (clés pour les systèmes limités par le disque) et prennent en charge l'accès trié sans analyses de table complètes.

[Structure d'index - IBM](https://www.ibm.com/docs/en/db2/11.1.0?topic=indexes-index-structure)  
[Index DB2 LUW : Détails des arbres B](https://datageek.blog/2013/09/19/db2-luw-basics-indexes/)  
[Dans Db2 pour z/OS : Comment les arbres B+ optimisés alimentent l'indexation haute vitesse](https://planetmainframe.com/2025/06/inside-db2-for-z-os-how-optimized-b-trees-power-high-speed-indexing/)  
[Comment comprendre rapidement l'index arbre B de DB2](https://srinimf.com/2021/07/26/db2-how-to-understand-b-tree-structure-of-index/)  
[Aperçu des index Db2](https://www.idug.org/news/db2-index-overview)