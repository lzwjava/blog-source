---
audio: false
generated: true
lang: fr
layout: post
title: Ajouter le pilote JDBC Oracle à Squirrel SQL Client
translated: true
---

Pour ajouter le pilote JDBC Oracle à Squirrel SQL Client, suivez ces étapes détaillées. Ce processus implique la configuration du pilote et la mise en place d'un alias de connexion pour votre base de données Oracle.

### Étape 1 : Localiser le fichier requis
Vous avez besoin du fichier du pilote JDBC Oracle, spécifiquement `ojdbc.jar`. Ce fichier contient les classes nécessaires pour permettre à Squirrel SQL Client de se connecter à une base de données Oracle. Assurez-vous d'avoir téléchargé ce fichier (par exemple, depuis le site web d'Oracle ou auprès de votre administrateur de base de données) et de connaître son emplacement sur votre système.

### Étape 2 : Lancer Squirrel SQL Client
Ouvrez l'application Squirrel SQL Client sur votre ordinateur.

### Étape 3 : Accéder à l'onglet Pilotes
Sur la gauche de l'interface de Squirrel SQL Client, localisez et cliquez sur l'onglet **Pilotes**. Cette section vous permet de gérer les pilotes JDBC disponibles pour l'application.

### Étape 4 : Ajouter un nouveau pilote
- Dans l'onglet Pilotes, cliquez sur le bouton **"+"** pour ouvrir la boîte de dialogue "Ajouter un pilote".

### Étape 5 : Nommer le pilote
- Dans le champ "Nom" de la boîte de dialogue "Ajouter un pilote", entrez **Oracle Thin Driver**. Il s'agit d'un nom descriptif pour identifier le pilote Oracle dans Squirrel SQL Client.

### Étape 6 : Ajouter le fichier `ojdbc.jar`
- Passez à l'onglet **Chemin de classe supplémentaire** dans la boîte de dialogue "Ajouter un pilote".
- Cliquez sur le bouton **Ajouter**.
- Naviguez jusqu'à l'emplacement du fichier `ojdbc.jar` sur votre système, sélectionnez-le et confirmez pour l'ajouter au chemin de classe du pilote.

### Étape 7 : Spécifier la classe du pilote Java
- Dans le champ "Nom de la classe", entrez la classe du pilote Java : **oracle.jdbc.OracleDriver**. Cela indique à Squirrel SQL Client quelle classe utiliser à partir du fichier `ojdbc.jar` pour gérer les connexions à la base de données Oracle.

### Étape 8 : Fournir un exemple d'URL
- Optionnellement, vous pouvez spécifier un format d'URL d'exemple pour la connexion à une base de données Oracle :
  - **Pour la connexion via SID** : `jdbc:oracle:thin:@HOST[:PORT]:DB`
  - **Pour la connexion via le nom du service** : `jdbc:oracle:thin:@//HOST[:PORT]/DB`
- Remplacez `HOST`, `PORT` et `DB` par les valeurs réelles lors de la configuration d'une connexion ultérieure (dans la configuration de l'alias).

### Étape 9 : Enregistrer la configuration du pilote
- Cliquez sur **OK** pour enregistrer les paramètres du pilote et fermer la boîte de dialogue "Ajouter un pilote". Le "Oracle Thin Driver" devrait maintenant apparaître dans l'onglet Pilotes avec une coche verte, indiquant qu'il est correctement configuré.

### Étape 10 : Créer un alias pour votre base de données
- Passez à l'onglet **Alias** sur la gauche de Squirrel SQL Client.
- Cliquez sur le bouton **"+"** pour ouvrir la boîte de dialogue "Ajouter un alias".

### Étape 11 : Configurer l'alias
- Dans la boîte de dialogue "Ajouter un alias" :
  - **Nom** : Entrez un nom pour cette connexion (par exemple, "Ma base de données Oracle").
  - **Pilote** : Sélectionnez **Oracle Thin Driver** dans le menu déroulant.
  - **URL** : Entrez l'URL de connexion pour votre base de données Oracle spécifique :
    - Via SID : `jdbc:oracle:thin:@HOST[:PORT]:DB`
    - Via nom de service : `jdbc:oracle:thin:@//HOST[:PORT]/DB`
    - Remplacez `HOST` (par exemple, localhost ou adresse IP), `PORT` (par défaut 1521) et `DB` (SID ou nom de service) par les détails de votre base de données.
  - **Nom d'utilisateur** : Entrez le nom d'utilisateur de la base de données.
  - **Mot de passe** : Entrez le mot de passe de la base de données.

### Étape 12 : Tester la connexion
- Cliquez sur le bouton **Test** dans la boîte de dialogue "Ajouter un alias" pour vérifier que Squirrel SQL Client peut se connecter à votre base de données Oracle en utilisant les détails fournis. Si la connexion est réussie, vous verrez un message de confirmation.

### Étape 13 : Enregistrer l'alias
- Si le test de connexion réussit, cliquez sur **OK** pour enregistrer l'alias. Le nouvel alias apparaîtra maintenant dans l'onglet Alias.

### Étape 14 : Se connecter à la base de données
- Dans l'onglet Alias, sélectionnez votre nouvel alias créé (par exemple, "Ma base de données Oracle").
- Cliquez sur le bouton **Connecter** pour établir une connexion à votre base de données Oracle. Une fois connecté, vous pouvez commencer à interroger votre base de données en utilisant Squirrel SQL Client.

### Résumé des informations clés
- **Fichier requis** : `ojdbc.jar`
- **Classe du pilote Java** : `oracle.jdbc.OracleDriver`
- **Formats d'URL** :
  - SID : `jdbc:oracle:thin:@HOST[:PORT]:DB`
  - Nom de service : `jdbc:oracle:thin:@//HOST[:PORT]/DB`

En suivant ces étapes, vous aurez ajouté avec succès le pilote JDBC Oracle à Squirrel SQL Client et configuré une connexion à votre base de données Oracle. Assurez-vous que toutes les informations (chemin du fichier, URL, identifiants) sont exactes pour éviter les problèmes de connexion.