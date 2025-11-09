---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Arbres B pour l'indexation efficace des bases de données
translated: true
type: note
---

### Qu'est-ce qu'un B-Tree ?

Un B-tree (abréviation de « balanced tree » ou arbre équilibré) est une structure de données arborescente auto-équilibrante conçue pour le stockage, l'insertion, la suppression et la récupération efficaces de grands volumes de données. Il est particulièrement optimisé pour les systèmes où les données sont stockées sur disque (comme les bases de données), car il minimise le nombre d'opérations d'E/S disque coûteuses en maintenant l'arbre aussi peu profond que possible.

#### Propriétés clés d'un B-Tree
- **Ordre (ou Degré)** : Défini par un paramètre *t* (degré minimum), où chaque nœud peut contenir entre *t-1* et *2t-1* clés (et jusqu'à *2t* enfants). Cela permet aux nœuds de contenir plusieurs clés, rendant l'arbre plus large et plus court.
- **Structure équilibrée** : Tous les nœuds feuilles sont au même niveau, garantissant une complexité temporelle logarithmique pour les opérations (O(log n), où n est le nombre de clés).
- **Clés triées** : Les clés dans chaque nœud sont stockées dans un ordre trié, et l'arbre maintient cet invariant. Les sous-arbres à gauche d'une clé contiennent des valeurs plus petites, et à droite des valeurs plus grandes.
- **Structure des nœuds** : Les nœuds internes ont des clés qui guident les recherches vers les nœuds enfants. Les nœuds feuilles stockent les données réelles (ou des pointeurs vers celles-ci).

Contrairement aux arbres binaires de recherche (BST), qui sont limités à deux enfants par nœud et peuvent devenir déséquilibrés (conduisant à une performance O(n) dans le pire des cas), les B-trees sont des arbres multi-chemins qui restent équilibrés grâce à la division et à la fusion des nœuds lors des insertions/suppressions.

#### Exemple simple
Imaginez un B-tree d'ordre 3 (*t=3*, donc 2 à 5 clés par nœud). Un petit arbre pourrait ressembler à ceci sous forme textuelle :

```
       [10, 20, 30]
      /    |    |    \
 [5,7]  [15] [22,25] [35,40]
```

- Recherche de 25 : Commencez à la racine, comparez avec 10/20/30 → allez à droite vers [22,25] → trouvé.

Cette structure permet des requêtes de plage efficaces (par exemple, toutes les clés entre 15 et 25) en parcourant quelques nœuds.

### Comment les bases de données utilisent les B-Trees

Les bases de données (comme les bases relationnelles : MySQL, PostgreSQL, SQL Server) s'appuient fortement sur les B-trees (ou des variantes comme les B+ trees) pour l'**indexation** afin d'accélérer les requêtes sur de grandes tables stockées sur disque. Sans index, les requêtes nécessiteraient des analyses complètes de table (temps O(n), lent pour des millions de lignes).

#### Utilisations principales dans les bases de données
1. **Index primaires et secondaires** :
   - Un **index primaire** est construit sur la clé primaire (identifiant unique). Il organise les lignes de la table dans l'ordre du B-tree pour des recherches rapides.
   - Les **index secondaires** sont sur d'autres colonnes (par exemple, nom, date). Les nœuds feuilles pointent vers les emplacements réels des lignes (via des ID de ligne).

2. **Accès disque efficace** :
   - Les disques lisent les données par blocs (par exemple, des pages de 4 Ko). Les nœuds du B-tree sont dimensionnés pour tenir dans un bloc de disque, donc une recherche nécessite typiquement la lecture de seulement 3-4 blocs (hauteur de l'arbre), contre potentiellement des milliers dans une liste chaînée.
   - La hauteur est logarithmique : Pour 1 milliard de clés, la hauteur peut être de seulement 4-5 niveaux.

3. **Variante B+ Tree (courante dans les BD)** :
   - La plupart des bases de données utilisent des **B+ trees**, une variante du B-tree où :
     - Seuls les nœuds feuilles stockent les données/pointeurs.
     - Les nœuds internes n'ont que des clés pour le routage.
     - Les feuilles sont liées (liste doublement chaînée) pour des analyses séquentielles et des requêtes de plage efficaces (par exemple, `SELECT * WHERE age BETWEEN 20 AND 30`).
   - Cela améliore les opérations sur les plages et l'efficacité du cache.

4. **Opérations en pratique** :
   - **INSERT/UPDATE/DELETE** : L'arbre divise ou fusionne les nœuds pour maintenir l'équilibre. Les bases de données gèrent la concurrence avec des verrous (latches/locks).
   - **Optimisation des requêtes** : Le planificateur de requêtes utilise les statistiques d'index pour choisir les index B-tree plutôt que les analyses de table.
   - **Clusterisé vs Non-clusterisé** : Dans les index clusterisés (par exemple, InnoDB dans MySQL), les données de la table sont physiquement stockées dans l'ordre des feuilles du B-tree. Les index non clusterisés pointent simplement vers les données.

#### Avantages et inconvénients
- **Avantages** : Rapide pour les requêtes d'égalité, de plage et triées ; gère bien les données croissantes.
- **Inconvénients** : Surcharge pour les insertions/suppressions (maintenance de l'arbre) ; pas idéal pour des mises à jour très fréquentes sans traitement par lots.

En résumé, les B-trees sont l'épine dorsale des performances des bases de données pour l'accès indexé, transformant ce qui pourrait être des recherches linéaires en opérations à temps quasi constant grâce à leur conception équilibrée et adaptée au disque.

#### Références
- [B-tree - Wikipedia](https://en.wikipedia.org/wiki/B-tree)
- [B+ Tree in DBMS - GeeksforGeeks](https://www.geeksforgeeks.org/introduction-of-b-tree/)
- [How Indexes Work in SQL Databases - Use The Index, Luke](https://use-the-index-luke.com/sql/anatomy/index-btree)