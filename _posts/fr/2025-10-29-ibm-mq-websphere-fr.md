---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Configuration d'IBM MQ dans WebSphere
translated: true
type: note
---

### Configuration des files d'attente de messages dans IBM WebSphere Application Server (Utilisation d'IBM MQ comme fournisseur)

IBM WebSphere Application Server (WAS) prend en charge la mise en file d'attente de messages via l'intégration Java Message Service (JMS) avec IBM MQ (anciennement WebSphere MQ). La configuration s'effectue généralement via la **Console de solutions intégrées WebSphere** (l'interface administrative), accessible à l'adresse `https://your-server:9043/ibm/console` (port sécurisé par défaut ; à ajuster si nécessaire). Ce guide se concentre sur le profil complet traditionnel de WAS (par exemple, version 9.0+), mais les étapes sont similaires pour WebSphere Liberty avec des ajustements mineurs.

#### Prérequis
- IBM MQ doit être installé, en cours d'exécution et accessible (par exemple, le gestionnaire de files d'attente démarré).
- Le serveur WAS est démarré et vous avez un accès administrateur à la console.
- Téléchargez et installez les bibliothèques clientes JMS d'IBM MQ (par exemple, `com.ibm.mq.allclient.jar`) dans les bibliothèques partagées de WAS si elles ne sont pas déjà présentes (sous **Environnement > Bibliothèques partagées**).
- Assurez-vous que le fournisseur de messagerie WebSphere MQ est configuré (sous **Ressources > JMS > Fournisseurs JMS**). Sinon, créez-en un avec des détails tels que l'hôte, le port (par défaut 1414) et le nom du gestionnaire de files d'attente.

Après la configuration, enregistrez les modifications (bouton **Enregistrer** en haut) et redémarrez le serveur d'applications pour qu'elles prennent effet.

#### Étape 1 : Créer une fabrique de connexions de file d'attente JMS
La fabrique de connexions établit les connexions au gestionnaire de files d'attente IBM MQ.

1. Connectez-vous à la console d'administration WAS.
2. Dans le volet de navigation, développez **Ressources > JMS > Fabriques de connexions de file d'attente**.
3. Sélectionnez la **Portée** appropriée (par exemple, Cellule, Nœud, Serveur) dans la liste déroulante et cliquez sur **Appliquer**.
4. Cliquez sur **Nouveau**.
5. Sélectionnez **Fournisseur de messagerie WebSphere MQ** et cliquez sur **OK**.
6. Sur l'écran suivant :
   - **Nom** : Entrez un nom descriptif (par exemple, `MyMQQueueConnectionFactory`).
   - **Nom JNDI** : Entrez une liaison JNDI (par exemple, `jms/MyQueueConnectionFactory`).
   - Cliquez sur **Suivant**.
7. Entrez les détails de connexion :
   - **Gestionnaire de files d'attente** : Nom de votre gestionnaire de files d'attente IBM MQ (par exemple, `QM1`).
   - **Nom d'hôte** : Nom d'hôte ou IP du serveur IBM MQ.
   - **Port** : Port d'écoute (par défaut : 1414).
   - **Type de transport** : CHANNEL (pour le mode client) ou BINDINGS (pour le mode intégré).
   - **Canal** : Nom du canal par défaut (par exemple, `SYSTEM.DEF.SVRCONN`).
   - **ID utilisateur** et **Mot de passe** : Informations d'identification pour l'authentification MQ (si nécessaire).
   - Cliquez sur **Suivant**.
8. Passez en revue le résumé et cliquez sur **Terminer**.
9. Sélectionnez la nouvelle fabrique, allez dans **Propriétés supplémentaires > Pool de connexions** (optionnel) et ajustez les paramètres tels que **Connexions maximum** (par exemple, en fonction de la charge prévue).
10. Cliquez sur **Tester la connexion** pour vérifier.

#### Étape 2 : Créer une destination de file d'attente JMS
Ceci définit le point de terminaison de la file d'attente réelle pour l'envoi/la réception de messages.

1. Dans le volet de navigation, développez **Ressources > JMS > Files d'attente**.
2. Sélectionnez la **Portée** appropriée (correspondant à la fabrique de connexions) et cliquez sur **Appliquer**.
3. Cliquez sur **Nouveau**.
4. Sélectionnez **Fournisseur de messagerie WebSphere MQ** et cliquez sur **OK**.
5. Spécifiez les propriétés :
   - **Nom** : Nom descriptif (par exemple, `MyRequestQueue`).
   - **Nom JNDI** : Liaison JNDI (par exemple, `jms/MyRequestQueue`).
   - **Nom de base de la file d'attente** : Nom exact de la file d'attente dans IBM MQ (par exemple, `REQUEST.QUEUE` ; doit exister ou être créée dans MQ).
   - **Client cible** : JMS (pour les applications JMS) ou MQ (pour les applications MQ natives).
   - **Mode de destination cible** : Une fois seulement (par défaut pour la fiabilité).
   - Cliquez sur **OK**.
6. (Optionnel) Sous **Propriétés supplémentaires**, configurez les paramètres de persistance, d'expiration ou de priorité.
7. Enregistrez la configuration.

#### Étape 3 : (Optionnel) Créer une spécification d'activation pour les Message-Driven Beans (MDBs)
Si vous utilisez des MDBs pour consommer des messages de manière asynchrone :

1. Dans le volet de navigation, développez **Ressources > JMS > Spécifications d'activation**.
2. Sélectionnez la **Portée** et cliquez sur **Nouveau**.
3. Sélectionnez **Fournisseur de messagerie WebSphere MQ** et cliquez sur **OK**.
4. Entrez :
   - **Nom** : par exemple, `MyQueueActivationSpec`.
   - **Nom JNDI** : par exemple, `jms/MyQueueActivation`.
   - **Type de destination** : File d'attente.
   - **Nom JNDI de la destination** : Le JNDI de votre file d'attente (par exemple, `jms/MyRequestQueue`).
   - **Nom JNDI de la fabrique de connexions** : Le JNDI de votre fabrique de connexions (par exemple, `jms/MyQueueConnectionFactory`).
   - Sélecteur de messages (optionnel) : Sélecteur JMS pour filtrer les messages.
5. Sous **Propriétés supplémentaires > Service d'écouteur de messages > Ports d'écoute**, créez un port si nécessaire :
   - **Nom** : par exemple, `MyListenerPort`.
   - **JNDI de la fabrique de connexions** : Comme ci-dessus.
   - **JNDI de la destination** : Comme ci-dessus.
   - **Composant** : Le descripteur de déploiement de votre MDB.
6. Cliquez sur **OK** et enregistrez.

#### Étape 4 : Vérifier et tester
- **Tester dans la console** : Utilisez la fonction **Tester la connexion** sur les fabriques et les spécifications.
- **Déployer une application** : Créez une application cliente JMS ou MDB simple, déployez-la et envoyez/testez des messages via les outils IBM MQ (par exemple, MQ Explorer).
- **Surveillance** : Sous **Surveillance et réglage > Visionneuse de performances** ou **Dépannage > Journaux**, vérifiez la présence d'erreurs liées à JMS.
- Problèmes courants :
  - Échecs de connexion : Vérifiez le pare-feu, l'état du canal MQ (`DISPLAY CHANNEL`) et les informations d'identification.
  - Erreurs de recherche JNDI : Assurez-vous que les liaisons sont correctes et que l'application utilise la bonne portée.
  - Persistance : Alignez les paramètres de durabilité entre WAS et MQ.

Pour les alternatives en ligne de commande (scripting wsadmin), reportez-vous à la documentation IBM. Ajustez en fonction de votre version (par exemple, WAS 9.0.5+ prend en charge JMS 2.0).

#### Références
- [Configuring JMS resources in WebSphere Application Server](https://www.ibm.com/docs/en/ibm-mq/9.2.x?topic=resources-configuring-jms-in-websphere-application-server)
- [WebSphere MQ messaging provider queue settings](https://www.ibm.com/docs/en/was/8.5.5?topic=settings-websphere-mq-messaging-provider-queue)
- [Creating a WebSphere MQ messaging provider queue connection factory](https://help.hcl-software.com/commerce/7.0.0/com.ibm.commerce.integration.doc/tasks/tcvjmsqueuefactory.html)
- [Configure a JMS queue destination for WebSphere MQ](http://www.setgetweb.com/p/i5/portal/WAS60/Configure_JMS_queue_destinationfor_WebSphere_MQ.html)