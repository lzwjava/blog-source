---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Configuration du serveur d'applications IBM MQ WebSphere
translated: true
type: note
---

### Prérequis
Avant de configurer IBM MQ (anciennement WebSphere MQ) dans IBM WebSphere Application Server (WAS), assurez-vous des points suivants :
- IBM MQ est installé sur un serveur dédié (ou sur le même serveur que WAS pour le mode liaisons locales).
- Un gestionnaire de files d'attente est créé dans IBM MQ (par exemple, en utilisant `crtmqm NOM_QM`).
- Les files d'attente requises sont créées dans le gestionnaire de files d'attente (par exemple, en utilisant MQ Explorer ou `runmqsc`).
- Les bibliothèques clientes IBM MQ (fichiers JAR comme `com.ibm.mq.allclient.jar`, `com.ibm.mqjms.jar`) sont disponibles. Si WAS est distant de MQ, installez le client IBM MQ sur la machine WAS.
- Ajoutez l'utilisateur du processus WAS au groupe `mqm` pour les autorisations.
- Pour les utilisateurs non root sur les systèmes de type Unix, utilisez `setmqaut` pour accorder les autorisations.

### Configuration étape par étape
La configuration implique la mise en place du fournisseur JMS, des fabriques de connexion et des destinations dans la console d'administration WAS. Ceci suppose une connexion en mode distribué (client) via TCP/IP ; ajustez pour le mode liaisons si local.

1. **Accéder à la console d'administration WAS** :
   - Démarrez le serveur WAS.
   - Ouvrez un navigateur et accédez à `https://localhost:9043/ibm/console` (remplacez par votre hôte/port).
   - Connectez-vous avec les identifiants administrateur.

2. **Configurer le fournisseur JMS IBM MQ** :
   - Allez dans **Ressources > JMS > Fournisseurs**.
   - Cliquez sur **Nouveau**.
   - Sélectionnez **Fournisseur de messagerie WebSphere MQ**.
   - Remplissez les détails :
     - **Nom** : par exemple, `MQProvider`.
     - **Description** : Optionnel.
     - **Chemin de classe** : Chemin vers les fichiers JAR MQ (par exemple, `/opt/mqm/java/lib/*` ou copiez-les dans `<WAS_HOME>/lib/ext`).
     - **Chemin des bibliothèques natives** : Requis pour le mode liaisons (chemin vers les bibliothèques MQ, par exemple, `/opt/mqm/lib64`).
     - **Nom de la fabrique de contexte initial externe** : `com.ibm.mq.jms.context.WMQInitialContextFactory` (pour le mode client).
     - **URL du fournisseur de contexte externe** : par exemple, `hôte:1414/CANAL` (hôte = IP du serveur MQ, 1414 = port par défaut, CANAL = par exemple, `SYSTEM.DEF.SVRCONN`).
   - Enregistrez la configuration.

3. **Créer une fabrique de connexion de file d'attente** :
   - Allez dans **Ressources > JMS > Fabriques de connexion de file d'attente** (définissez la portée sur votre serveur ou cellule).
   - Cliquez sur **Nouveau**.
   - Sélectionnez le fournisseur créé à l'étape 2.
   - Remplissez :
     - **Nom** : par exemple, `MQQueueCF`.
     - **Nom JNDI** : par exemple, `jms/MQQueueCF`.
     - **Gestionnaire de files d'attente** : Le nom de votre gestionnaire de files d'attente MQ (par exemple, `QM1`).
     - **Hôte** : Nom d'hôte ou IP du serveur MQ.
     - **Port** : 1414 (par défaut).
     - **Canal** : par exemple, `SYSTEM.DEF.SVRCONN`.
     - **Type de transport** : `CLIENT` (pour TCP/IP) ou `BINDINGS` (local).
     - **Informations d'identification de sécurité** : ID utilisateur et mot de passe si requis.
   - Propriétés avancées optionnelles : Définissez les tailles du pool de connexions (par exemple, connexions max en fonction de votre charge).
   - Enregistrez.

4. **Créer les destinations de file d'attente** :
   - Allez dans **Ressources > JMS > Files d'attente**.
   - Cliquez sur **Nouveau**.
   - Sélectionnez le fournisseur.
   - Pour chaque file d'attente :
     - **Nom** : par exemple, `MyQueue`.
     - **Nom JNDI** : par exemple, `jms/MyQueue`.
     - **Nom de la file d'attente** : Nom exact de la file d'attente dans MQ (par exemple, `MY.LOCAL.QUEUE`).
     - **Gestionnaire de files d'attente** : Identique à ci-dessus.
     - **Type de client cible** : `MQ` ou `JMS`.
   - Enregistrez. Répétez pour les topics si vous utilisez pub/sub.

5. **(Optionnel) Configurer le serveur WebSphere MQ pour le mode liaisons** :
   - Si vous utilisez les liaisons locales, allez dans **Serveurs > Types de serveur > Serveurs WebSphere MQ**.
   - Cliquez sur **Nouveau**.
   - Définissez le **Nom**, le **Nom du gestionnaire de files d'attente**.
   - Spécifiez les **Installations MQ** (chemin d'installation de MQ).
   - Enregistrez et redémarrez le serveur.

6. **Configurer l'adaptateur de ressources JCA (pour les MDB)** :
   - Allez dans **Ressources > Adaptateurs de ressources > Fabriques de connexion J2C**.
   - Si vous utilisez le RA MQ intégré, assurez-vous qu'il est déployé (WAS inclut `wmq.jmsra.rar`).
   - Définissez des propriétés comme le nombre max de connexions (par exemple, 10-50 en fonction de la charge).

7. **Tester la configuration** :
   - Déployez un exemple d'application JMS ou utilisez l'exemple JMS de WAS.
   - Vérifiez les journaux pour les erreurs (par exemple, connexion refusée sur le port 1414).
   - Vérifiez dans MQ : Utilisez MQ Explorer pour surveiller les profondeurs des files d'attente et les canaux.

8. **Sécurité et configuration avancée** :
   - Activez SSL : Configurez les keystores dans WAS et MQ (canal avec `SSLCIPH`).
   - Définissez l'authentification : Utilisez les groupes d'utilisateurs MQ ou les ID utilisateur alternatifs.
   - Pour les clusters : Synchronisez les configurations entre les nœuds.

### Conseils de dépannage
- **ClassNotFoundException** : Assurez-vous que les JARs MQ sont dans le classpath.
- **Échecs de connexion** : Vérifiez le pare-feu sur le port 1414, le statut du canal (`DISPLAY CHSTATUS(*)` dans runmqsc).
- **Problèmes de mode liaisons** : Vérifiez les bibliothèques natives et l'utilisateur dans le groupe `mqm`.
- Redémarrez WAS après les modifications.

Pour les détails spécifiques à la version (par exemple, WAS 9.x avec MQ 9.x), reportez-vous à la documentation officielle d'IBM.

[Utilisation de WebSphere Application Server avec IBM MQ](https://www.ibm.com/docs/en/ibm-mq/9.2.x?topic=together-using-websphere-application-server-mq)  
[Configuration de WebSphere Application Server pour une utilisation avec IBM MQ](https://help.hcl-software.com/commerce/9.0.0/integration/tasks/tcvconfigure_was_for_mq.html)  
[Création d'une définition de serveur WebSphere MQ](https://www.ibm.com/docs/SSAW57_8.5.5/com.ibm.websphere.nd.multiplatform.doc/ae/tjfp0004_.html)