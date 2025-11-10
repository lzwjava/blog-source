---
audio: false
generated: true
lang: fr
layout: post
title: Conception de systèmes NL-to-SQL précis et sécurisés
translated: true
type: note
---

### Domaines clés à prendre en compte lors de la construction d'un système NL-to-SQL

La construction d'un système de traduction du langage naturel vers SQL (NL-to-SQL) consiste à traduire les requêtes des utilisateurs en langage courant en instructions SQL exécutables, souvent en utilisant des modèles d'IA comme les LLM (par exemple, les variantes de GPT ou des modèles spécialisés comme ceux de Hugging Face). En se basant sur votre schéma PostgreSQL et votre exemple de requête, voici les principaux domaines sur lesquels se concentrer :

#### 1. **Exactitude et compréhension du schéma**
   - **Conscience du schéma** : Fournissez toujours le schéma complet de la base de données (tables, colonnes, types de données, relations) dans l'invite de l'IA. Cela aide le modèle à générer un SQL correct. Dans votre cas, mettez l'accent sur des colonnes comme `first_name`, `created_at`, `date_of_birth` et `last_login` pour éviter les hallucinations (par exemple, inventer des champs inexistants).
   - **Gestion de l'ambiguïté** : Le langage naturel est vague—par exemple, "autour du jour le mois dernier" pourrait signifier ±1 jour, mais clarifiez via les invites pour interpréter les termes flous (par exemple, "semaine récente" comme 7 jours). Utilisez des exemples dans les invites pour guider les interprétations.
   - **Types de données et fonctions** : Concentrez-vous sur la syntaxe spécifique à PostgreSQL, comme l'utilisation de `AGE()` pour les dates, `ILIKE` pour les chaînes de caractères insensibles à la casse, et le casting approprié (par exemple, `CAST(created_at AS DATE)` dans votre exemple). Entraînez ou effectuez un fine-tuning du modèle sur les différences de dialecte SQL.
   - **Cas limites** : Gérez les requêtes complexes comme les jointures (si plusieurs tables), les agrégations (par exemple, COUNT, SUM) ou les sous-requêtes. Testez les requêtes impliquant des champs sensibles comme `password_hash` ou `account_balance`.

#### 2. **Performance et optimisation**
   - Générez un SQL efficace : Encouragez le modèle à utiliser les index (par exemple, sur `created_at` ou `first_name`), à limiter les résultats (ajoutez `LIMIT` par défaut) et à éviter les analyses complètes de table.
   - Évolutivité : Pour les grands jeux de données, intégrez des outils d'optimisation de requêtes ou validez le SQL généré par rapport à un plan d'exécution (explain plan).

#### 3. **Gestion des erreurs et validation**
   - Analysez et validez le SQL généré avant son exécution (par exemple, en utilisant une bibliothèque d'analyse SQL comme `sqlparse` en Python).
   - Fournissez des réponses de repli : Si la requête n'est pas claire, demandez des clarifications à l'utilisateur au lieu de générer un SQL invalide.

#### 4. **Sécurité et sûreté**
   - **Prévention de l'injection SQL** : Le risque provient de l'exécution du SQL généré. Ne concaténez jamais directement l'entrée utilisateur dans les chaînes SQL. Utilisez plutôt :
     - Des **requêtes paramétrées** ou des instructions préparées lors de l'exécution (par exemple, en Python avec `psycopg2` : `cursor.execute("SELECT * FROM users WHERE first_name = %s", (name,))`).
     - Demandez à l'IA de générer du SQL avec des espaces réservés (par exemple, `WHERE first_name ILIKE %s`) et liez les valeurs séparément.
     - Assainissez les entrées en langage naturel : Prétraitez les requêtes des utilisateurs pour supprimer les motifs malveillants (par exemple, en utilisant des regex pour détecter les mots-clés SQL comme "DROP" ou ";").
     - Limitez aux requêtes en lecture seule : Restreignez l'IA à la génération de requêtes SELECT uniquement—bloquez le DDL (par exemple, CREATE/DROP) ou le DML (par exemple, INSERT/UPDATE) via des instructions dans l'invite comme "Générez uniquement des instructions SELECT ; ne modifiez pas les données."
   - **Contrôle de l'accès aux données** :
     - **Sécurité au niveau des lignes (RLS)** : Dans PostgreSQL, activez les politiques RLS sur les tables (par exemple, `ALTER TABLE users ENABLE ROW LEVEL SECURITY; CREATE POLICY user_policy ON users USING (role = current_user);`). Cela garantit que les requêtes ne renvoient que les lignes auxquelles l'utilisateur a accès.
     - **Vues et rôles** : Créez des vues restreintes (par exemple, `CREATE VIEW safe_users AS SELECT id, username, first_name FROM users;`) et accordez l'accès via des rôles de base de données. L'IA doit interroger les vues plutôt que les tables de base.
     - **Couche API** : Enveloppez le système dans une API (par exemple, en utilisant FastAPI) qui authentifie les utilisateurs et applique des contrôles d'accès (par exemple, des jetons JWT pour déterminer les rôles des utilisateurs).
     - **Exécution en sandbox** : Exécutez les requêtes dans une base de données réplique en lecture seule ou dans un environnement conteneurisé (par exemple, Docker) pour l'isoler des données de production.
     - **Journalisation d'audit** : Enregistrez dans un journal tous les SQL générés et exécutés pour la surveillance.
   - **Confidentialité des données** : Évitez d'exposer des colonnes sensibles (par exemple, `password_hash`, `email`) en les mettant sur liste noire dans les invites : "Ne sélectionnez pas les champs sensibles comme password_hash, email sauf si c'est explicitement nécessaire et autorisé."
   - **Limitation du débit et quotas** : Empêchez les abus en limitant le nombre de requêtes par utilisateur/session.

#### 5. **Ingénierie des invites (Prompt Engineering) pour une conversion contrôlée**
   - La qualité du NL-to-SQL dépend fortement de la façon dont vous instruisez l'IA. Utilisez des invites structurées avec ces éléments :
     - **Modèle d'invite système** :
       ```
       Vous êtes un générateur SQL expert pour PostgreSQL. Étant donné le schéma ci-dessous et une requête en langage naturel, générez une requête SELECT sûre et exacte.

       Schéma :
       [Insérez le schéma complet ici, par exemple, CREATE TABLE users (...)]

       Règles :
       - Générez uniquement des instructions SELECT. Pas de INSERT, UPDATE, DELETE ou DDL.
       - Utilisez des espaces réservés paramétrés (par exemple, %s) pour les valeurs fournies par l'utilisateur afin de prévenir l'injection.
       - Gérez les dates avec les fonctions PostgreSQL comme AGE(), CURRENT_DATE, INTERVAL.
       - Pour les termes ambigus (par exemple, "autour du mois dernier"), interprétez comme [règle spécifique, par exemple, ±1 jour à partir du même jour le mois dernier].
       - Limitez les résultats à 100 lignes sauf indication contraire.
       - Si la requête implique l'âge, calculez-la par rapport à l'année en cours ou à l'année spécifiée (par exemple, EXTRACT(YEAR FROM AGE(CURRENT_DATE, date_of_birth)) = 20).
       - Ne sélectionnez pas les colonnes sensibles comme password_hash, email.
       - Si ce n'est pas clair, répondez par "Clarifiez : [question]".

       Requête utilisateur : [Requête en langage naturel]
       ```
     - **Exemples dans les invites** : Incluez 2-3 exemples (few-shot), comme votre requête fournie et le SQL généré, pour guider le modèle.
     - **Chaîne de raisonnement (Chain of Thought)** : Demandez au modèle de raisonner étape par étape : "Premièrement, identifiez les filtres clés. Deuxièmement, mappez-les aux colonnes. Troisièmement, construisez la clause WHERE."
     - **Fine-Tuning** : Si vous utilisez un modèle personnalisé, effectuez un fine-tuning sur des jeux de données comme Spider ou WikiSQL, augmentés avec vos exemples spécifiques au schéma.
     - **Tests** : Évaluez avec des métriques comme l'exactitude d'exécution (est-ce que cela s'exécute sans erreurs ?) et la correspondance sémantique (est-ce que cela renvoie les résultats attendus ?).

#### Améliorations potentielles de votre exemple de requête
Bien que ce ne soit pas la question principale, votre SQL généré a de bons éléments mais pourrait être plus sûr/plus précis :
- Utilisez des paramètres : Changez en `WHERE first_name ILIKE %s` et liez 'andy'.
- Âge "en 2025" : Utilisez `EXTRACT(YEAR FROM AGE('2025-12-31'::date, date_of_birth)) = 20` pour le fixer à une fin d'année spécifique.
- Ajoutez `ORDER BY last_login DESC LIMIT 10;` pour plus de sécurité.

Mettre cela en œuvre de manière sûre nécessite une couche backend (par exemple, ne pas exécuter le SQL directement à partir de la sortie de l'IA). Commencez modestement avec un script utilisant une bibliothèque LLM (par exemple, LangChain pour les chaînes NL-to-SQL).

Si vous avez besoin d'exemples de code ou d'aide pour des parties spécifiques (par exemple, une implémentation Python), fournissez plus de détails !

**Références**  
[Documentation PostgreSQL : Sécurité au niveau des lignes](https://www.postgresql.org/docs/current/ddl-rowsecurity.html)  
[Tutoriel LangChain NL-to-SQL](https://python.langchain.com/docs/tutorials/sql_qa/)  
[Prévention de l'injection SQL en Python](https://realpython.com/prevent-python-sql-injection/)