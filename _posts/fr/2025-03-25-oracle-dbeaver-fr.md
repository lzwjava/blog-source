---
audio: false
generated: true
lang: fr
layout: post
title: Comment utiliser DBeaver pour vérifier les données des tables Oracle DB
translated: true
type: note
---

Je suppose que vous demandez comment utiliser DBeaver pour vérifier quelles tables de la base de données Oracle contiennent des données, suite à votre question précédente sur la recherche de tables avec des données dans Oracle DB. DBeaver est un outil de base de données populaire, gratuit et multi-plateforme qui fonctionne bien avec Oracle et d'autres bases de données. Ci-dessous, je vais vous expliquer comment utiliser DBeaver pour inspecter vos schémas Oracle et identifier les tables contenant des données.

---

#### 1. **Configurer une connexion à votre base de données Oracle**
   - **Installer DBeaver** : Si ce n'est pas déjà fait, téléchargez et installez DBeaver (l'édition Community convient) depuis [dbeaver.io](https://dbeaver.io/).
   - **Créer une nouvelle connexion** :
     1. Ouvrez DBeaver et cliquez sur **Base de données** > **Nouvelle connexion de base de données** dans le menu.
     2. Sélectionnez **Oracle** dans la liste et cliquez sur **Suivant**.
     3. Saisissez les détails de votre connexion :
        - **Hôte** : Le nom d'hôte ou l'adresse IP de votre serveur Oracle.
        - **Port** : Typiquement 1521 (port par défaut pour Oracle).
        - **Base de données/SID ou Nom du service** : Selon votre configuration (par exemple, SID = `XE` pour l'édition Express ou un nom de service).
        - **Nom d'utilisateur** et **Mot de passe** : Vos identifiants Oracle.
     4. Cliquez sur **Tester la connexion** pour vérifier qu'elle fonctionne. Vous devrez peut-être télécharger le pilote JDBC Oracle si vous y êtes invité (DBeaver peut le faire automatiquement).
     5. Cliquez sur **Terminer** pour sauvegarder la connexion.

#### 2. **Explorer les schémas dans le navigateur de base de données**
   - Dans le **Navigateur de base de données** (volet de gauche), développez votre connexion Oracle.
   - Vous verrez une liste de schémas (par exemple, votre nom d'utilisateur ou d'autres auxquels vous avez accès). Développez le schéma que vous souhaitez inspecter.
   - Sous chaque schéma, développez le nœud **Tables** pour voir toutes les tables.

#### 3. **Vérifier les tables pour les données via l'interface graphique**
   - **Voir les données de la table** :
     1. Double-cliquez sur un nom de table ou faites un clic droit dessus et sélectionnez **Modifier la table**.
     2. Passez à l'onglet **Données** dans l'éditeur qui s'ouvre.
     3. Si la table contient des données, vous verrez des lignes affichées. Si elle est vide, vous ne verrez aucune ligne (ou un message comme "Aucune donnée").
     - Par défaut, DBeaver récupère jusqu'à 200 lignes. Pour récupérer toutes les lignes, cliquez sur le bouton **Récupérer toutes les lignes** (une petite icône de flèche) dans la barre d'outils en bas de l'onglet Données.
   - **Compter les lignes rapidement** :
     1. Faites un clic droit sur la table dans le Navigateur de base de données.
     2. Sélectionnez **Naviguer** > **Nombre de lignes**.
     3. DBeaver exécute une requête `SELECT COUNT(*)` et affiche le résultat dans une fenêtre contextuelle. Si c'est 0, la table est vide.

#### 4. **Exécuter des requêtes SQL pour vérifier plusieurs tables**
   - Si vous souhaitez vérifier plusieurs tables à la fois (plus efficace que de cliquer sur chacune), utilisez l'Éditeur SQL :
     1. Cliquez sur **Éditeur SQL** > **Nouveau script SQL** (ou appuyez sur `Ctrl + [`).
     2. Définissez le contexte du schéma :
        - Utilisez la liste déroulante en haut de l'Éditeur SQL pour sélectionner votre schéma, ou exécutez :
          ```sql
          ALTER SESSION SET CURRENT_SCHEMA = nom_du_schema;
          ```
          Remplacez `nom_du_schema` par votre schéma cible (par exemple, `HR`).
     3. Interrogez le nombre de lignes pour toutes les tables :
        - Utilisez ce SQL pour lister les tables avec des données (similaire à ma réponse précédente) :
          ```sql
          SELECT table_name, num_rows
          FROM user_tables
          WHERE num_rows > 0
          ORDER BY num_rows DESC;
          ```
        - Exécutez-la en appuyant sur `Ctrl + Entrée`. Les résultats apparaissent dans l'onglet **Résultats** en dessous.
        - `USER_TABLES` affiche les tables dans votre schéma. Utilisez `ALL_TABLES` pour les tables auxquelles vous avez accès dans tous les schémas :
          ```sql
          SELECT owner, table_name, num_rows
          FROM all_tables
          WHERE num_rows > 0
          AND owner = UPPER('nom_du_schema');
          ```
     4. **Remarque** : `NUM_ROWS` est une estimation provenant de la dernière mise à jour des statistiques. Si elle est inexacte, mettez à jour les statistiques avec :
        ```sql
        EXEC DBMS_STATS.GATHER_SCHEMA_STATS('nom_du_schema');
        ```