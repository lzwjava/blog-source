---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Configuration des ressources JMS dans WebSphere
translated: true
type: note
---

### Prérequis
- Assurez-vous d'avoir un accès administratif à la console d'administration intégrée (Integrated Solutions Console) d'IBM WebSphere Application Server (WAS).
- Le serveur doit être en cours d'exécution, et vous devez décider de la portée (par exemple, cellule, nœud, serveur) pour les ressources.
- Ce guide se concentre sur le fournisseur de messagerie par défaut (utilisant Service Integration Bus ou SIBus), qui est le fournisseur JMS intégré dans WAS. Si vous utilisez WebSphere MQ, une configuration supplémentaire pour le fournisseur MQ est nécessaire.
- Redémarrez le serveur après des modifications importantes si vous y êtes invité.

### Étape 1 : Créer un Service Integration Bus
Le bus d'intégration de services sert de fondement de messagerie pour les ressources JMS.

1. Connectez-vous à la WebSphere Integrated Solutions Console.
2. Accédez à **Service integration > Buses**.
3. Cliquez sur **Nouveau**.
4. Entrez un nom de bus unique (par exemple, `MyJMSBus`).
5. Désactivez l'option **Bus security** sauf si nécessaire.
6. Cliquez sur **Suivant**, puis sur **Terminer** pour créer le bus.

### Étape 2 : Ajouter le serveur en tant que membre du bus
Cela permet au serveur d'héberger des moteurs de messagerie sur le bus.

1. Sélectionnez le bus que vous avez créé (par exemple, `MyJMSBus`).
2. Sous **Propriétés supplémentaires**, cliquez sur **Bus members**.
3. Cliquez sur **Ajouter**.
4. Dans l'assistant **Add a New Bus Member** :
   - Sélectionnez **Messaging engine** comme type de membre du bus.
   - Choisissez votre serveur (par exemple, `server1`) dans la liste.
   - Pour le magasin de messages, sélectionnez **File store** (par défaut pour les environnements non clusterisés) ou **Data store** pour une persistance en base de données, et configurez les propriétés si nécessaire.
5. Cliquez sur **Suivant**, puis sur **Terminer**.
6. Redémarrez le WebSphere Application Server pour activer le membre du bus.

### Étape 3 : Créer une fabrique de connexions JMS
Une fabrique de connexions est nécessaire pour connecter les clients JMS au fournisseur.

1. Accédez à **Resources > JMS > Connection factories**.
2. Sélectionnez la portée appropriée (par exemple, Server scope pour `server1`) et cliquez sur **Nouveau**.
3. Sélectionnez **Default messaging provider** et cliquez sur **OK**.
4. Entrez les détails :
   - **Nom** : par exemple, `MyJMSConnectionFactory`.
   - **Nom JNDI** : par exemple, `jms/MyConnectionFactory`.
   - **Nom du bus** : Sélectionnez `MyJMSBus` dans la liste déroulante.
   - Conservez les autres valeurs par défaut (par exemple, Provider endpoints en auto-détection).
5. Cliquez sur **Appliquer**, puis sur **Sauvegarder** pour enregistrer dans la configuration maîtresse.

### Étape 4 : Créer une file d'attente JMS
Ceci définit la destination de la file d'attente pour la messagerie point-à-point.

1. Accédez à **Resources > JMS > Queues**.
2. Sélectionnez la portée appropriée et cliquez sur **Nouveau**.
3. Sélectionnez **Default messaging provider** et cliquez sur **OK**.
4. Entrez les détails :
   - **Nom** : par exemple, `MyJMSQueue`.
   - **Nom JNDI** : par exemple, `jms/MyQueue`.
   - **Nom du bus** : Sélectionnez `MyJMSBus`.
   - **Nom de la file d'attente** : Sélectionnez **Create Service Integration Bus Destination**, entrez un identifiant unique (par exemple, `MyQueueDestination`), et sélectionnez le membre du bus créé précédemment.
   - **Nom de base de la file d'attente** : par exemple, `$MyJMSBus:MyQueueDestination` (généré automatiquement).
5. Configurez les propriétés supplémentaires si nécessaire (par exemple, mode de livraison, expiration).
6. Cliquez sur **Appliquer**, puis sur **Sauvegarder** pour enregistrer dans la configuration maîtresse.

### Étape 5 : (Optionnel) Créer des spécifications d'activation pour les Message-Driven Beans (MDB)
Si vous utilisez des MDB pour consommer les messages de la file d'attente, configurez les spécifications d'activation.

1. Accédez à **Resources > JMS > Activation specifications**.
2. Sélectionnez la portée appropriée et cliquez sur **Nouveau**.
3. Sélectionnez **Default messaging provider** et cliquez sur **OK**.
4. Entrez les détails :
   - **Nom** : par exemple, `MyActivationSpec`.
   - **Nom JNDI** : par exemple, `jms/activation/MyActivationSpec`.
   - **Nom du bus** : Sélectionnez `MyJMSBus`.
   - **Type de destination** : Queue.
   - **Destination** : Entrez le nom JNDI de la file d'attente (par exemple, `jms/MyQueue`).
5. Cliquez sur **Appliquer**, puis sur **Sauvegarder** pour enregistrer dans la configuration maîtresse.

### Vérification et test
- Après avoir sauvegardé, synchronisez les nœuds si vous êtes dans un environnement clusterisé.
- Redémarrez le serveur.
- Utilisez une application cliente JMS pour tester l'envoi et la réception de messages via les noms JNDI.
- Surveillez via **Service integration > Buses > [Votre Bus] > Bus members > [Votre Membre] > Messaging engines**.

Pour les configurations avancées (par exemple, sécurité, clustering), reportez-vous à la documentation IBM.

[Configuring IBM WebSphere Application Server for Decision Server](https://docs.redhat.com/en/documentation/red_hat_decision_manager/7.4/html/installing_and_configuring_decision_server_on_ibm_websphere_application_server/was-configure-proc)  
[Managing messaging with the default messaging provider](https://www.ibm.com/docs/en/was/9.0.5?topic=resources-managing-messaging-default-messaging-provider)