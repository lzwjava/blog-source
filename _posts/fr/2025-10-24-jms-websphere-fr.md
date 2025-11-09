---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: JMS dans WebSphere Application Server
translated: true
type: note
---

### Fonctionnement de JMS dans IBM WebSphere Application Server (WAS)

JMS (Java Message Service) est une API standard pour envoyer et recevoir des messages entre des applications Java de manière découplée et asynchrone. Dans WAS, JMS est implémenté via le **Default Messaging Provider**, qui utilise le **Service Integration Bus (SIBus)** comme moteur de messagerie sous-jacent. SIBus est un bus intégré et évolutif qui gère le routage, la mise en file d'attente et la livraison des messages sans nécessiter de logiciel externe.

#### Composants clés et flux
1. **Service Integration Bus (SIBus)** : Il s'agit de l'infrastructure centrale. C'est comme un réseau virtuel où les moteurs de messagerie (un par serveur ou cluster) traitent les messages. Vous créez un bus, y ajoutez des serveurs en tant que membres, et vous définissez des destinations (files d'attente ou topics) sur celui-ci.

2. **Connection Factory** : Agit comme point d'entrée. Votre application Java recherche ceci via JNDI (par exemple, `jms/MyConnectionFactory`) pour créer une connexion JMS vers le SIBus.

3. **Destinations (Queues/Topics)** : Les queues sont pour la messagerie point-à-point (un expéditeur, un destinataire). Une fois créées et liées au bus, elles stockent les messages de manière persistante (en utilisant des stockages fichiers ou des bases de données, configurable).

4. **Flux des messages** :
   - **Envoi** : L'application crée une session JMS via la connection factory, obtient une référence à une queue via JNDI, et envoie un message (par exemple, `TextMessage`). Le SIBus l'achemine vers le moteur de messagerie cible, qui le met en file d'attente.
   - **Réception** : Un consommateur (par exemple, une autre application ou un Message-Driven Bean) se connecte de manière similaire et interroge (poll) ou écoute les messages. SIBus les livre de manière fiable, en gérant les nouvelles tentatives, les accusés de réception et les transactions.
   - SIBus prend en charge le clustering pour la haute disponibilité, la répartition de charge et les liens de bus étrangers (foreign bus links) pour l'intégration avec d'autres systèmes.

WAS gère le cycle de vie : démarrage/arrêt des moteurs, surveillance des files d'attente et garantit la durabilité en fonction de votre configuration (par exemple, messages persistants vs non persistants).

#### La création d'une file d'attente JMS permet-elle aux applications Java d'envoyer/recevoir des messages ?
Oui, exactement. Après la configuration (comme décrit précédemment : bus, membre, connection factory, queue), votre application Java peut :
- Utiliser les API JMS standard (`javax.jms.*`) pour envoyer/recevoir.
- Rechercher les ressources via JNDI dans le contexte du serveur d'applications.
- Exemple de code pour l'envoi :
  ```java
  InitialContext ctx = new InitialContext();
  QueueConnectionFactory qcf = (QueueConnectionFactory) ctx.lookup("jms/MyConnectionFactory");
  Queue queue = (Queue) ctx.lookup("jms/MyQueue");
  QueueConnection conn = qcf.createQueueConnection();
  QueueSession session = conn.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
  QueueSender sender = session.createSender(queue);
  TextMessage msg = session.createTextMessage("Hello JMS!");
  sender.send(msg);
  // Fermer les ressources...
  ```
La réception fonctionne de manière similaire avec `QueueReceiver` ou les MDBs. Aucun code personnalisé n'est nécessaire pour le bus—tout est abstrait.

#### Est-ce que WAS gère correctement la file d'attente ?
Absolument. SIBus se charge de :
- **Persistence** : Les messages survivent aux redémarrages (stockage fichier/BDD).
- **Fiabilité** : Livraison garantie, files d'attente de lettres mortes (dead-letter queues) pour les échecs.
- **Évolutivité** : Gère un débit élevé, le clustering.
- **Surveillance** : Affichez les statistiques dans la console d'administration (par exemple, nombre de messages, backlog).
Si des problèmes surviennent (par exemple, file d'attente pleine), les journaux et alertes sont disponibles. C'est une solution prête pour la production en environnement enterprise.

#### Avons-nous besoin de plugins supplémentaires comme Kafka ?
Non, rien comme Kafka n'est requis—SIBus est entièrement intégré à WAS (pas d'installation séparée ni de licence au-delà de WAS lui-même). Kafka est une plateforme de streaming distribuée différente ; SIBus est spécifique à JMS et plus simple pour les applications WAS. Si vous avez besoin de fonctionnalités similaires à Kafka (par exemple, les streams), vous pourriez intégrer via des liens de bus étrangers, mais pour la mise en file d'attente JMS standard, utilisez le fournisseur par défaut.

Pour approfondir, consultez la documentation IBM sur [Managing messaging with the default messaging provider](https://www.ibm.com/docs/en/was/9.0.5?topic=resources-managing-messaging-default-messaging-provider) et [How JMS applications connect to a messaging engine on a bus](https://www.ibm.com/docs/en/was-nd/8.5.5?topic=messaging-how-jms-applications-connect-engine-bus).