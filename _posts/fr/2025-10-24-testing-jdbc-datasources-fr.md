---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Test des sources de données JDBC dans WebSphere
translated: true
type: note
---

### Test des sources de données JDBC dans la console d'administration d'IBM WebSphere Application Server (WAS)

Dans IBM WebSphere Application Server (WAS), vous pouvez utiliser la fonctionnalité "Test connection" dans la console intégrée (console d'administration) pour vérifier qu'une source de données JDBC est correctement configurée et peut se connecter à la base de données sous-jacente. Ceci est utile pour résoudre les problèmes de connectivité sans déployer d'application.

Voici un guide étape par étape (en supposant que vous utilisez WAS Traditional ou Liberty avec la console complète ; les versions peuvent légèrement varier, par exemple v8.5, v9.x) :

#### Prérequis
- Assurez-vous d'avoir un accès administratif au serveur WAS et à sa console.
- La source de données doit déjà être configurée (sous Ressources > JDBC > Sources de données) avec des détails comme le nom JNDI, le fournisseur JDBC, l'URL de la base de données, le nom d'utilisateur, le mot de passe, etc.
- Le serveur de base de données doit être en cours d'exécution et accessible depuis le serveur WAS (vérifiez les pare-feux, le réseau, etc.).
- Si vous utilisez une configuration sécurisée (par exemple, SSL), assurez-vous que les certificats sont configurés.

#### Étapes pour tester la connexion

1. **Connectez-vous à la console d'administration** :
   - Ouvrez un navigateur web et accédez à l'URL de la console : `http://<was-host>:<admin-port>/ibm/console` (le port admin par défaut est 9060 pour HTTP ou 9043 pour HTTPS ; remplacez par votre hôte et port réels).
   - Connectez-vous avec vos identifiants administrateur.

2. **Accédez aux Sources de données JDBC** :
   - Dans le volet de navigation de gauche, développez **Ressources** > **JDBC**.
   - Cliquez sur **Data sources**.

3. **Sélectionnez la portée appropriée** :
   - La console vous invitera à sélectionner une portée si elle n'est pas déjà définie (par exemple, Cellule, Nœud, Serveur ou Cluster). Choisissez la portée où votre source de données est définie.
   - Cliquez sur **OK** ou **Continue** pour poursuivre.

4. **Localisez votre source de données** :
   - Dans la liste des sources de données, trouvez et sélectionnez celle que vous souhaitez tester (par exemple, par son nom JNDI comme `jdbc/myDataSource`).
   - Si elle n'est pas listée, assurez-vous qu'elle a été créée et sauvegardée. Vous pouvez en créer une via **New** si nécessaire.

5. **Accédez à la fonctionnalité de test de connexion** :
   - Avec la source de données sélectionnée, cliquez sur **Test connection** (ce bouton se trouve généralement en haut de la page de détails de la source de données).
   - Si le bouton est grisé ou indisponible :
     - Vérifiez si la source de données est activée (recherchez une option "Enable" si elle est désactivée).
     - Assurez-vous qu'un fournisseur JDBC est associé (sous Ressources > JDBC > JDBC providers).
     - Pour certaines configurations, vous devrez peut-être arrêter/démarrer le serveur ou sauvegarder la configuration d'abord.

6. **Exécutez le test** :
   - La console tentera d'établir une connexion en utilisant les paramètres configurés (URL, pilote, identifiants, etc.).
   - Attendez le résultat (cela peut prendre quelques secondes, selon la réponse du réseau/de la base de données).
   - **Succès** : Vous verrez un message comme "Test connection for data source <Nom> on server <NomDuServeur> at Node <NomDuNoeud> was successful."
   - **Échec** : Vous obtiendrez un message d'erreur avec des détails, tels que :
     - Connexion refusée (problème de réseau).
     - Identifiants invalides (nom d'utilisateur/mot de passe incorrect).
     - Pilote non trouvé (fournisseur JDBC mal configuré).
     - Détails d'une SQLException provenant de la base de données.

7. **Examinez et résolvez les problèmes** :
   - En cas d'échec, vérifiez la zone **Messages** de la console (en haut de la page) pour plus de détails.
   - Consultez les journaux du serveur : Allez dans **Troubleshooting** > **Logs and trace** > Sélectionnez votre serveur > **JVM logs** ou **Application logs** pour les traces de la pile d'exécution.
   - Corrections courantes :
     - Vérifiez le format de l'URL de la base de données (par exemple, `jdbc:oracle:thin:@localhost:1521:orcl` pour Oracle).
     - Testez les identifiants manuellement en utilisant un outil de base de données comme SQL*Plus ou DBeaver.
     - Assurez-vous que le JAR du pilote JDBC est déployé au bon emplacement (par exemple, via le fournisseur JDBC).
     - Pour les pools de connexion, vérifiez les paramètres comme les connexions minimum/maximum sous **Connection pool properties**.

#### Conseils supplémentaires
- **Sécurité** : Si la source de données utilise une authentification gérée par le conteneur, assurez-vous que les identifiants sont définis dans **Security** > **Global security** ou via JAAS.
- **Propriétés personnalisées** : Sur la page de la source de données, examinez les onglets comme **Connection pool**, **Container-managed authentication alias** et **Custom properties** pour détecter d'éventuels problèmes.
- **Serveurs/Clusters multiples** : Le test s'exécute sur le serveur/nœud spécifique sélectionné. Pour les clusters, testez sur chaque membre si nécessaire.
- **Profil WAS Liberty** : Si vous utilisez Liberty, le processus est similaire mais utilise le fichier `server.xml` ou le Liberty Admin Center. Activez la fonctionnalité `adminCenter-1.0` et accédez-y via `http://localhost:9080/adminCenter`. Le test se trouve sous **Servers** > Votre Serveur > **Resources** > **Data sources**.
- **Automatisation** : Pour les scripts, utilisez les commandes wsadmin (Jython/Python) comme `AdminConfig.testConnection(dsId)` où `dsId` est l'ID de configuration de la source de données.

Si vous rencontrez un message d'erreur spécifique ou une version particulière de WAS, fournissez plus de détails pour une aide ciblée ! Pour la documentation officielle, reportez-vous à IBM Knowledge Center pour votre version de WAS.