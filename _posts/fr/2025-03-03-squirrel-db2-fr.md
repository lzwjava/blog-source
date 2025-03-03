---
audio: true
generated: true
lang: fr
layout: post
title: Client SQL SQuirreL et base de données DB2
translated: true
---

Pour utiliser votre fichier JAR IBM DB2 JCC (`db2jcc.jar`) dans SQuirreL SQL Client et vous connecter à une base de données DB2, suivez ces étapes détaillées. Ce processus implique la configuration du pilote DB2 dans SQuirreL et la mise en place d'un alias de connexion.

---

### Étape 1 : Vérifier le fichier JAR
- Assurez-vous d'avoir le bon fichier JAR du pilote JDBC DB2. Le fichier que vous avez mentionné, `db2jcc.jar`, est généralement le bon pour IBM DB2, bien que certaines configurations puissent utiliser `db2jcc4.jar` en fonction de la version.
- Vérifiez si votre installation DB2 nécessite un fichier de licence supplémentaire (par exemple, `db2jcc_license_cisuz.jar`). Si c'est le cas, localisez ce fichier également, car il peut être nécessaire pour éviter les erreurs liées à la licence lors de la connexion.

---

### Étape 2 : Configurer le pilote DB2 dans SQuirreL SQL Client
1. **Ouvrir SQuirreL SQL Client** :
   - Lancez l'application sur votre système.

2. **Accéder à l'onglet Pilotes** :
   - Dans le panneau de gauche, cliquez sur l'onglet **Pilotes** pour afficher la liste des pilotes de bases de données disponibles.

3. **Localiser ou ajouter le pilote DB2** :
   - Recherchez un pilote DB2 existant dans la liste (par exemple, "IBM DB2 App Driver"). Il peut être marqué d'une croix rouge s'il n'est pas configuré correctement.
   - Si le pilote est présent, vous pouvez le modifier. Sinon, vous devrez en créer un nouveau :
     - **Modifier le pilote existant** : Double-cliquez sur l'entrée du pilote DB2.
     - **Ajouter un nouveau pilote** : Cliquez sur l'icône **+** dans l'onglet Pilotes pour ouvrir l'assistant "Ajouter un pilote".

4. **Configurer les paramètres du pilote** :
   - **Nom** : Entrez un nom descriptif, tel que "IBM DB2 JCC Driver."
   - **URL d'exemple** : Définissez-la sur `jdbc:db2://<host>:<port>/<database>` (vous personnaliserez cela plus tard pour votre base de données spécifique).
   - **Nom de la classe** : Entrez `com.ibm.db2.jcc.DB2Driver` (c'est la classe de pilote standard pour JDBC DB2).

5. **Ajouter le fichier JAR** :
   - Allez à l'onglet **Chemin de classe supplémentaire** dans la fenêtre de configuration du pilote.
   - Cliquez sur **Ajouter**, puis parcourez et sélectionnez l'emplacement de votre fichier `db2jcc.jar`.
   - Si vous avez un fichier JAR de licence (par exemple, `db2jcc_license_cisuz.jar`), cliquez à nouveau sur **Ajouter** et incluez-le également.

6. **Enregistrer la configuration** :
   - Cliquez sur **OK** pour enregistrer les paramètres du pilote. Le pilote DB2 devrait maintenant apparaître dans l'onglet Pilotes avec une coche, indiquant qu'il est correctement configuré.

---

### Étape 3 : Créer un alias de base de données
1. **Passer à l'onglet Alias** :
   - Dans le panneau de gauche, cliquez sur l'onglet **Alias**, qui gère vos connexions de bases de données.

2. **Ajouter un nouvel alias** :
   - Cliquez sur l'icône **+** pour ouvrir l'assistant "Ajouter un alias".

3. **Configurer l'alias** :
   - **Nom** : Donnez un nom à votre connexion (par exemple, "Ma base de données DB2").
   - **Pilote** : Dans le menu déroulant, sélectionnez le pilote DB2 que vous avez configuré à l'Étape 2 (par exemple, "IBM DB2 JCC Driver").
   - **URL** : Entrez l'URL de connexion pour votre base de données au format :
     ```
     jdbc:db2://<host>:<port>/<database>
     ```
     Remplacez `<host>` (par exemple, `localhost` ou l'adresse IP de votre serveur), `<port>` (par exemple, `50000`, le port DB2 par défaut), et `<database>` (le nom de votre base de données) par vos détails réels. Par exemple :
     ```
     jdbc:db2://localhost:50000/mydb
     ```
   - **Nom d'utilisateur** et **Mot de passe** : Fournissez vos identifiants de base de données DB2.

4. **Enregistrer et se connecter** :
   - Cliquez sur **OK** pour enregistrer l'alias.
   - Dans l'onglet Alias, double-cliquez sur votre nouvel alias pour vous connecter. Entrez votre mot de passe si vous y êtes invité.

---

### Problèmes potentiels et solutions
- **Erreurs de licence** :
  - Si vous voyez une erreur comme "La licence IBM Data Server for JDBC and SQLJ était invalide," assurez-vous que le fichier JAR de licence (par exemple, `db2jcc_license_cisuz.jar`) est ajouté au chemin de classe supplémentaire du pilote.
- **Erreurs de classe introuvable** :
  - Si SQuirreL signale "Could not find class com.ibm.db2.jcc.DB2Driver," vérifiez que :
    - Le fichier `db2jcc.jar` est correctement ajouté au chemin de classe supplémentaire.
    - Le nom de la classe est défini sur `com.ibm.db2.jcc.DB2Driver` sans fautes de frappe.
- **Conflits de plusieurs JAR** :
  - Évitez d'inclure plusieurs versions du pilote JDBC DB2 (par exemple, à la fois `db2jcc.jar` et `db2jcc4.jar`) dans le chemin de classe supplémentaire, car cela peut provoquer des conflits. Utilisez uniquement les JAR nécessaires pour votre version DB2.
- **Format d'URL incorrect** :
  - Vérifiez deux fois la syntaxe de votre URL de connexion. Une URL mal formée (par exemple, port manquant ou nom de base de données incorrect) empêchera la connexion.

---

En suivant ces étapes, vous devriez pouvoir configurer SQuirreL SQL Client pour utiliser votre fichier `db2jcc.jar` et vous connecter avec succès à votre base de données DB2. Si vous rencontrez des problèmes, consultez les conseils de dépannage ci-dessus ou assurez-vous que votre serveur de base de données est accessible depuis votre réseau.