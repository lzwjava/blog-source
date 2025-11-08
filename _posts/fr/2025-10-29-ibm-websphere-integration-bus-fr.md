---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Bus de services d'intégration IBM WebSphere
translated: true
type: note
---

### Service Integration Bus dans IBM WebSphere Application Server

Le « bus d'intégration » dans le contexte d'IBM WebSphere Application Server (WAS) fait généralement référence au **Service Integration Bus (SIB ou SIBus)**, une infrastructure de messagerie intégrée fournie par WAS. Il permet une communication asynchrone et fiable entre les applications, en particulier celles utilisant des architectures basées sur les messages ou des architectures orientées services (SOA).

#### Objectif
SIB agit comme une colonne vertébrale de messagerie virtuelle au sein d'un environnement WAS. Il permet aux applications s'exécutant sur différents serveurs ou clusters d'échanger des messages sans connexions point-à-point directes, favorisant ainsi un couplage lâche, une évolutivité et une tolérance aux pannes. Les cas d'utilisation clés incluent :
- La prise en charge de Java Message Service (JMS) pour les modèles de file d'attente et de publication/abonnement.
- L'intégration de services d'entreprise dans les configurations SOA.
- La gestion du routage, de la transformation et de la persistance des messages dans les systèmes distribués.

Contrairement aux Enterprise Service Bus (ESB) autonomes comme IBM Integration Bus (anciennement WebSphere Message Broker), SIB est intégré en natif dans WAS et ne nécessite pas d'installation séparée — il est activé par la configuration.

#### Composants et Architecture Clés
- **Membres du bus** : Ce sont les serveurs d'applications ou les clusters de serveurs dans une cellule WAS qui rejoignent le bus. Chaque membre héberge une partie de l'infrastructure de messagerie.
- **Messaging Engines (MEs)** : Les composants d'exécution principaux qui traitent les messages. Chaque ME s'exécute au sein d'un processus WAS (par exemple, sur un membre du bus) et gère l'envoi, la réception et le stockage des messages. Les ME se connectent dynamiquement pour former un réseau médiatisé pour la haute disponibilité.
- **Service SIB** : Un service par défaut sur chaque serveur d'applications WAS qui est désactivé par défaut. Son activation active les capacités de messagerie.
- **Destinations** : Files d'attente ou topics où les messages sont publiés ou consommés, configurables via la console d'administration WAS.
- **Stores de données** : Pour la persistance, les ME utilisent des stores basés sur des fichiers (locaux pour les serveurs uniques, systèmes de fichiers partagés pour les clusters) ou des bases de données pour garantir la durabilité des messages.

L'architecture est basée sur les cellules : Dans une configuration WAS Network Deployment, plusieurs membres du bus collaborent entre les nœuds, en utilisant des protocoles comme SOAP/HTTP ou JMS pour l'interopérabilité.

#### Configuration et Utilisation
1. **Création** : Via la console administrative WAS (Integrated Solutions Console), naviguez vers *Intégration de service > Buses > Nouveau*. Définissez le nom du bus, ajoutez des membres (serveurs/clusters) et configurez les ME (par exemple, les politiques de haute disponibilité).
2. **Configuration** : Activez le fournisseur JMS SIB, créez des destinations (files d'attente/topics) et associez-les à des noms JNDI pour l'accès des applications.
3. **Utilisation** : Les applications déploient des Message-Driven Beans (MDBs) ou utilisent les API JMS pour interagir avec le bus. Par exemple, une application émettrice place un message dans une file d'attente, et le bus l'achemine vers les récepteurs sur d'autres membres.

SIB prend en charge les standards comme JMS 1.1/2.0 et s'intègre avec des systèmes externes (par exemple, via des ponts WebSphere MQ). Pour la production, envisagez un réglage des performances, comme l'utilisation de datastores partagés pour la reprise sur panne.

**Remarque** : Si vous faites référence à *IBM Integration Bus* (IIB), c'est un produit distinct pour des besoins ESB plus larges ; il peut se connecter à WAS/SIB mais n'est pas « dans » WAS lui-même.

[Service integration buses - IBM Docs](https://www.ibm.com/docs/en/was/9.0.5?topic=integration-service-buses)  
[Service integration bus messaging provider - IBM Docs](https://www.ibm.com/docs/en/was-liberty/nd?topic=providers-service-integration-bus-messaging-provider)  
[Getting Started with Service Integration Bus](https://www.freekb.net/Article?id=1975)