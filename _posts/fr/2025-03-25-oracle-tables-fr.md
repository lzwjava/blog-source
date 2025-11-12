---
audio: false
generated: true
lang: fr
layout: post
title: Identifier les tables avec des données dans Oracle DB
translated: true
type: note
---

Dans Oracle Database, si vous explorez des schémas et constatez que certaines tables apparaissent "vides" lorsque vous cliquez dessus (par exemple, via un outil graphique comme SQL Developer ou Toad), cela ne signifie pas nécessairement qu'elles ne contiennent pas de données. Plusieurs raisons peuvent expliquer cela : des permissions, des filtres, ou vous consultez simplement les mauvaises tables. Pour déterminer systématiquement quelles tables d'un schéma contiennent des données, vous pouvez interroger les métadonnées de la base de données ou inspecter directement les tables. Voici comment procéder :

#### 1. **Vérifiez vos permissions**
   - Si vous voyez des tables vides, vous pourriez ne pas avoir les privilèges nécessaires pour visualiser les données. Assurez-vous d'avoir les privilèges `SELECT` sur les tables du schéma.
   - Exécutez cette requête pour vérifier vos privilèges sur une table spécifique :
     ```sql
     SELECT privilege
     FROM dba_tab_privs
     WHERE grantee = UPPER('votre_nom_utilisateur')
     AND table_name = UPPER('nom_table');
     ```
     Remplacez `'votre_nom_utilisateur'` et `'nom_table'` en conséquence. Si rien ne s'affiche, demandez au propriétaire du schéma ou au DBA de vous accorder l'accès.

#### 2. **Interrogez le nombre de lignes dans les tables**
   - Oracle conserve des statistiques sur les tables, y compris le nombre de lignes, dans les vues `USER_TABLES`, `ALL_TABLES` ou `DBA_TABLES` (selon votre niveau d'accès).
   - Pour voir les tables avec des données dans le schéma actuel :
     ```sql
     SELECT table_name, num_rows
     FROM user_tables
     WHERE num_rows > 0
     ORDER BY num_rows DESC;
     ```
     - `USER_TABLES` : Affiche les tables détenues par l'utilisateur actuel.
     - `NUM_ROWS` : Nombre approximatif de lignes (basé sur la dernière mise à jour des statistiques).

   - Si vous avez accès à un autre schéma (par exemple, via `ALL_TABLES`) :
     ```sql
     SELECT owner, table_name, num_rows
     FROM all_tables
     WHERE num_rows > 0
     AND owner = UPPER('nom_schema')
     ORDER BY num_rows DESC;
     ```
     Remplacez `'nom_schema'` par le schéma que vous investigatez.

   **Remarque** : `NUM_ROWS` peut être obsolète si les statistiques n'ont pas été récemment collectées. Voir l'Étape 5 pour les mettre à jour.

#### 3. **Vérifiez manuellement des tables spécifiques**
   - Si vous soupçonnez que `NUM_ROWS` n'est pas fiable ou si vous voulez vérifier, exécutez un `COUNT(*)` sur des tables individuelles :
     ```sql
     SELECT table_name
     FROM user_tables;
     ```
     Ceci liste toutes les tables dans votre schéma. Ensuite, pour chaque table :
     ```sql
     SELECT COUNT(*) FROM nom_table;
     ```
     Si le compte est supérieur à 0, la table contient des données. Soyez prudent avec les grandes tables — `COUNT(*)` peut être lent.

#### 4. **Utilisez un script pour automatiser la vérification**
   - Pour éviter d'interroger manuellement chaque table, utilisez un script PL/SQL pour vérifier le nombre de lignes dans toutes les tables d'un schéma :
     ```sql
     BEGIN
         FOR t IN (SELECT table_name FROM user_tables)
         LOOP
             EXECUTE IMMEDIATE 'SELECT COUNT(*) FROM ' || t.table_name INTO v_count;
             IF v_count > 0 THEN
                 DBMS_OUTPUT.PUT_LINE(t.table_name || ' a ' || v_count || ' lignes');
             END IF;
         END LOOP;
     EXCEPTION
         WHEN OTHERS THEN
             DBMS_OUTPUT.PUT_LINE('Erreur sur la table ' || t.table_name || ': ' || SQLERRM);
     END;
     /
     ```
     - Activez la sortie dans votre outil (par exemple, `SET SERVEROUTPUT ON` dans SQL*Plus ou SQL Developer).
     - Ceci n'affiche que les tables avec des données. Ajustez `user_tables` en `all_tables` et ajoutez un filtrage sur `owner` si vous vérifiez un autre schéma.

#### 5. **Mettez à jour les statistiques des tables (si nécessaire)**
   - Si `NUM_ROWS` dans `USER_TABLES` ou `ALL_TABLES` affiche 0 ou semble incorrect, les statistiques sont peut-être obsolètes. Pour les mettre à jour :
     ```sql
     EXEC DBMS_STATS.GATHER_SCHEMA_STATS(ownname => 'nom_schema');
     ```
     Remplacez `'nom_schema'` par le nom du schéma (utilisez votre nom d'utilisateur pour votre propre schéma). Puis réexécutez la requête `USER_TABLES` de l'Étape 2.

#### 6. **Vérifiez les tables partitionnées**
   - Si le schéma utilise des tables partitionnées, les données peuvent être réparties entre les partitions, et une simple requête pourrait ne pas le refléter. Vérifiez les partitions :
     ```sql
     SELECT table_name, partition_name, num_rows
     FROM user_tab_partitions
     WHERE num_rows > 0
     ORDER BY table_name, partition_name;
     ```
     Ceci montre quelles partitions contiennent des données.

#### 7. **Conseils pour les outils graphiques (par exemple, SQL Developer)**
   - Si vous utilisez un outil graphique comme Oracle SQL Developer :
     1. Faites un clic droit sur le schéma dans le panneau Connexions.
     2. Développez le nœud "Tables".
     3. Faites un clic droit sur une table, sélectionnez "Count Rows", ou ouvrez l'onglet "Data" pour prévisualiser le contenu (si autorisé).
     - Si l'onglet "Data" est vide, cela peut être un problème de permissions ou la table n'a vraiment aucune ligne.

---

### Exemple pratique
Supposons que vous soyez dans un schéma appelé `HR`. Vous devriez :
1. Exécuter :
   ```sql
   SELECT table_name, num_rows
   FROM user_tables
   WHERE num_rows > 0;
   ```
   Le résultat pourrait ressembler à :
   ```
   TABLE_NAME   NUM_ROWS
   ----------   --------
   EMPLOYEES    107
   DEPARTMENTS  27
   ```
   Ceci vous indique que `EMPLOYEES` et `DEPARTMENTS` contiennent des données.

2. Si vous soupçonnez des statistiques obsolètes, mettez-les à jour :
   ```sql
   EXEC DBMS_STATS.GATHER_SCHEMA_STATS('HR');
   ```
3. Revérifiez avec la même requête.

---

### Pourquoi les tables peuvent apparaître vides
- **Aucune donnée** : La table n'a vraiment aucune ligne.
- **Permissions** : Vous pouvez voir la structure de la table mais pas les données.
- **Filtres** : Votre outil graphique peut avoir des filtres masquant des lignes (par exemple, une clause `WHERE`).
- **Données tronquées/supprimées** : Les données ont pu être récemment supprimées.
- **Synonyms/Vues** : Vous regardez peut-être un synonyme ou une vue pointant vers une table vide ou inaccessible.

Si vous êtes toujours bloqué, indiquez-moi votre configuration spécifique (par exemple, nom du schéma, outil utilisé), et je pourrai adapter les conseils davantage !