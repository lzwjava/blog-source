---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Vue d'ensemble du catalogue système IBM Db2
translated: true
type: note
---

### Introduction aux tables système d'IBM Db2

Le catalogue système d'IBM Db2 (également appelé catalogue Db2) est un référentiel de métadonnées intégré qui stocke des informations détaillées sur chaque objet et élément de votre base de données. Cela inclut les tables, les vues, les index, les colonnes, les utilisateurs, les privilèges, les routines, et plus encore. C'est essentiellement l'"annuaire" de votre base de données — automatiquement maintenu par Db2 chaque fois que vous créez, modifiez ou supprimez des objets. Le catalogue aide les administrateurs de base de données (DBA), les développeurs et les outils à interroger la structure et l'état de la base de données sans avoir besoin d'analyser le code d'application ou les fichiers externes.

Contrairement aux tables utilisateur classiques, le catalogue système est en lecture seule pour la plupart des utilisateurs et est optimisé pour l'interrogation de métadonnées plutôt que pour les opérations sur de grands volumes de données. Il est créé automatiquement lorsque vous créez une nouvelle base de données et réside dans des espaces de table spéciaux (comme SYSCATSPACE dans Db2 LUW).

#### Composants clés et structure
Le catalogue système se compose de :
- **Tables de base** : Ce sont les tables sous-jacentes et normalisées où les métadonnées brutes sont stockées. Elles se trouvent dans le schéma **SYSIBM** et ne sont pas directement interrogeables par les utilisateurs finaux pour éviter des modifications accidentelles ou des problèmes de performance. Les exemples incluent SYSIBM.SYSTABLES (informations de base sur les tables) et SYSIBM.SYSCOLUMNS (détails des colonnes).
- **Vues du catalogue** : Des vues dénormalisées et conviviales construites au-dessus des tables de base. Elles sont plus faciles à interroger et fournissent une interface standardisée conforme aux normes SQL (comme ISO). Elles sont regroupées en schémas :
  - **SYSCAT** : Métadonnées principales sur les objets de la base de données (par exemple, tables, index, déclencheurs).
  - **SYSCOLUMNS** : Informations détaillées au niveau des colonnes.
  - **SYSSTAT** : Données statistiques utilisées par l'optimiseur de requêtes (par exemple, nombre de lignes, cardinalités).
  - **SYSPROC** et autres : Pour les procédures, les fonctions et les informations liées au XML.

Dans Db2 pour z/OS, le catalogue se trouve dans la base de données DSNDB06, mais les concepts sont similaires entre les plateformes (LUW, z/OS, i).

#### Objectif
- **Découverte** : Découvrir quels objets existent, leurs propriétés et leurs relations.
- **Administration** : Surveiller les privilèges, les dépendances et les statistiques de performance.
- **Développement** : Générer des scripts DDL, valider les schémas ou s'intégrer à des outils comme Db2 Data Studio.
- **Optimisation** : L'optimiseur de requêtes utilise les vues SYSSTAT pour choisir les plans d'exécution.

#### Comment y accéder et l'interroger
1. **Se connecter à la base de données** : Utilisez `db2 connect to <nom_bdd>`.
2. **Permissions** : Par défaut, PUBLIC a le droit SELECT sur les vues du catalogue. Aucune autorisation spéciale n'est nécessaire pour les requêtes de base, mais les tables de base SYSIBM nécessitent SYSADM ou un privilège supérieur.
3. **Interrogation** : Utilisez les instructions SQL SELECT standard. Les vues sont qualifiées par schéma (par exemple, `SELECT * FROM SYSCAT.TABLES`).

**Exemples de requêtes** :
- **Lister toutes les tables dans le schéma actuel** :
  ```
  SELECT TABSCHEMA, TABNAME, TYPE FROM SYSCAT.TABLES
  WHERE TABSCHEMA = CURRENT SCHEMA;
  ```
  - Résultat : Affiche le schéma, le nom de la table et le type (par exemple, 'T' pour table, 'V' pour vue).

- **Obtenir les détails des colonnes pour une table** :
  ```
  SELECT COLNAME, TYPENAME, LENGTH, NULLS
  FROM SYSCOLUMNS
  WHERE TABSCHEMA = 'VOTRE_SCHEMA' AND TABNAME = 'VOTRE_TABLE';
  ```
  - Résultat : Noms des colonnes, types de données, longueurs et possibilité de valeurs NULL.

- **Vérifier les statistiques d'une table** :
  ```
  SELECT CARD, NPAGES FROM SYSSTAT.TABLES
  WHERE TABNAME = 'VOTRE_TABLE';
  ```
  - CARD : Nombre estimé de lignes ; NPAGES : Nombre de pages.

Pour des listes complètes, exécutez `SELECT * FROM SYSCAT.VIEWS WHERE VIEWNAME LIKE 'SYSCAT%'` pour découvrir toutes les vues disponibles.

#### Notes importantes
- **Performance** : Les requêtes sur le catalogue sont rapides mais peuvent être gourmandes en ressources sur les grandes bases de données ; utilisez des filtres (par exemple, des clauses WHERE) pour limiter les résultats.
- **Mises à jour** : Db2 met à jour le catalogue automatiquement — n'essayez pas d'y faire des INSERT/UPDATE manuellement.
- **Différences de version** : Dans Db2 11.5+, les vues sont plus standardisées. Pour z/OS, certaines vues ont des colonnes spécifiques à la plateforme.
- **Intégration d'outils** : Utilisez la commande `db2look` de Db2 pour générer du DDL à partir des données du catalogue : `db2look -d <nom_bdd> -t <table>`.
- Évitez l'accès direct aux tables de base sauf si vous êtes un administrateur système, car cela peut entraîner des incohérences.

Pour des analyses plus approfondies, explorez la documentation officielle ou expérimentez dans une base de données de test.

#### Références
- [Aperçu du catalogue Db2](https://www.ibm.com/docs/en/db2-for-zos/12?topic=objects-db2-catalog)
- [Vues du catalogue système dans Db2 LUW](https://www.ibm.com/docs/en/db2/11.5?topic=views-system-catalog)
- [Obtenir des informations utiles à partir du catalogue système DB2](https://developer.ibm.com/articles/dm-0411melnyk/)