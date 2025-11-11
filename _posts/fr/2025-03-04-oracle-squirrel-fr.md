---
audio: false
generated: true
lang: fr
layout: post
title: Ajouter le pilote JDBC Oracle au client Squirrel SQL
translated: true
type: note
---

Pour ajouter le pilote JDBC Oracle à Squirrel SQL Client, suivez ces étapes détaillées. Ce processus implique de configurer le pilote et de créer un alias de connexion pour votre base de données Oracle.

### Étape 1 : Localiser le Fichier Requis
Vous avez besoin du fichier pilote JDBC Oracle, spécifiquement `ojdbc.jar`. Ce fichier contient les classes nécessaires pour permettre à Squirrel SQL Client de se connecter à une base de données Oracle. Assurez-vous d'avoir téléchargé ce fichier (par exemple, depuis le site web d'Oracle ou votre administrateur de base de données) et de connaître son emplacement sur votre système.

### Étape 2 : Lancer Squirrel SQL Client
Ouvrez l'application Squirrel SQL Client sur votre ordinateur.

### Étape 3 : Accéder à l'Onglet Drivers
Sur le côté gauche de l'interface de Squirrel SQL Client, localisez et cliquez sur l'onglet **Drivers**. Cette section vous permet de gérer les pilotes JDBC disponibles pour l'application.

### Étape 4 : Ajouter un Nouveau Pilote
- Dans l'onglet Drivers, cliquez sur le bouton **"+"** pour ouvrir la boîte de dialogue "Add Driver".

### Étape 5 : Nommer le Pilote
- Dans le champ "Name" de la boîte de dialogue "Add Driver", entrez **Oracle Thin Driver**. C'est un nom descriptif pour identifier le pilote Oracle dans Squirrel SQL Client.

### Étape 6 : Ajouter le Fichier `ojdbc.jar`
- Passez à l'onglet **Extra Class Path** dans la boîte de dialogue "Add Driver".
- Cliquez sur le bouton **Add**.
- Naviguez jusqu'à l'emplacement du fichier `ojdbc.jar` sur votre système, sélectionnez-le et confirmez pour l'ajouter au classpath du pilote.

### Étape 7 : Spécifier la Classe du Pilote Java
- Dans le champ "Class Name", entrez la classe du pilote Java : **oracle.jdbc.OracleDriver**. Cela indique à Squirrel SQL Client quelle classe utiliser dans le fichier `ojdbc.jar` pour gérer les connexions à la base de données Oracle.

### Étape 8 : Fournir un Exemple d'URL
- Optionnellement, vous pouvez spécifier un exemple de format d'URL pour se connecter à une base de données Oracle :
  - **Pour une connexion via SID** : `jdbc:oracle:thin:@HOST[:PORT]:DB`
  - **Pour une connexion via nom de service** : `jdbc:oracle:thin:@//HOST[:PORT]/DB`
- Remplacez `HOST`, `PORT` et `DB` par les valeurs réelles lors de la configuration d'une connexion ultérieure (dans la configuration de l'alias).

### Étape 9 : Sauvegarder la Configuration du Pilote
- Cliquez sur **OK** pour sauvegarder les paramètres du pilote et fermer la boîte de dialogue "Add Driver". Le "Oracle Thin Driver" devrait maintenant apparaître dans l'onglet Drivers avec une coche verte, indiquant qu'il est correctement configuré.

### Étape 10 : Créer un Alias pour Votre Base de Données
- Passez à l'onglet **Aliases** sur le côté gauche de Squirrel SQL Client.
- Cliquez sur le bouton **"+"** pour ouvrir la boîte de dialogue "Add Alias".

### Étape 11 : Configurer l'Alias
- Dans la boîte de dialogue "Add Alias" :
  - **Name** : Entrez un nom pour cette connexion (par exemple, "Ma Base Oracle").
  - **Driver** : Sélectionnez **Oracle Thin Driver** dans le menu déroulant.
  - **URL** : Entrez l'URL de connexion pour votre base de données Oracle spécifique :
    - Via SID : `jdbc:oracle:thin:@HOST[:PORT]:DB`
    - Via nom de service : `jdbc:oracle:thin:@//HOST[:PORT]/DB`
    - Remplacez `HOST` (par exemple, localhost ou adresse IP), `PORT` (par défaut 1521) et `DB` (SID ou nom de service) par les détails de votre base de données.
  - **Username** : Entrez le nom d'utilisateur de la base de données.
  - **Password** : Entrez le mot de passe de la base de données.

### Étape 12 : Tester la Connexion
- Cliquez sur le bouton **Test** dans la boîte de dialogue "Add Alias" pour vérifier que Squirrel SQL Client peut se connecter à votre base de données Oracle en utilisant les détails fournis. Si la connexion réussit, vous verrez un message de confirmation.

### Étape 13 : Sauvegarder l'Alias
- Si le test de connexion réussit, cliquez sur **OK** pour sauvegarder l'alias. Le nouvel alias apparaîtra maintenant dans l'onglet Aliases.

### Étape 14 : Se Connecter à la Base de Données
- Dans l'onglet Aliases, sélectionnez votre alias nouvellement créé (par exemple, "Ma Base Oracle").
- Cliquez sur le bouton **Connect** pour établir une connexion à votre base de données Oracle. Une fois connecté, vous pouvez commencer à interroger votre base de données en utilisant Squirrel SQL Client.

### Récapitulatif des Informations Clés
- **Fichier Requis** : `ojdbc.jar`
- **Classe du Pilote Java** : `oracle.jdbc.OracleDriver`
- **Formats d'URL** :
  - SID : `jdbc:oracle:thin:@HOST[:PORT]:DB`
  - Nom de Service : `jdbc:oracle:thin:@//HOST[:PORT]/DB`

En suivant ces étapes, vous aurez réussi à ajouter le pilote JDBC Oracle à Squirrel SQL Client et à configurer une connexion à votre base de données Oracle. Assurez-vous que tous les détails (chemin du fichier, URL, identifiants) sont exacts pour éviter les problèmes de connexion.