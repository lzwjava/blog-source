---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Files d'attente JMS dans WebSphere Application Server
translated: true
type: note
---

### Présentation de Java Message Service (JMS)
Java Message Service (JMS) est une API standard pour envoyer des messages entre des applications Java, permettant une communication asynchrone. Il prend en charge deux modèles de messagerie principaux : point-à-point (en utilisant des files d'attente) et publication-abonnement (en utilisant des topics). Dans IBM WebSphere Application Server (WAS), JMS est intégré pour gérer la messagerie au sein des applications d'entreprise, utilisant souvent le fournisseur de messagerie par défaut intégré ou des fournisseurs externes comme IBM MQ.

### Files d'attente dans JMS
Dans JMS, une **file d'attente** est un type de destination utilisé pour la **messagerie point-à-point**. Voici une explication :
- **Objectif** : Les messages envoyés à une file d'attente sont délivrés à exactement un consommateur (récepteur). C'est idéal pour les scénarios où un message doit être traité par une seule application ou composant, comme la distribution de tâches ou les modèles requête-réponse.
- **Caractéristiques principales** :
  - **FIFO (Premier entré, premier sorti)** : Les messages sont généralement traités dans l'ordre de leur arrivée, bien que JMS permette la priorisation.
  - **Persistance** : Les messages peuvent être persistants (stockés durablement) ou non persistants, garantissant la fiabilité en cas de défaillance.
  - **Consommateurs** : Plusieurs consommateurs peuvent être attachés à une file d'attente, mais chaque message est consommé par un seul. Si aucun consommateur n'est disponible, les messages s'accumulent jusqu'à leur traitement.
- **Composants impliqués** :
  - **Expéditeur/Producteur de file d'attente** : Envoie des messages à la file d'attente.
  - **Récepteur/Consommateur de file d'attente** : Interroge ou écoute les messages sur la file d'attente.
  - **Fabrique de connexions** : Utilisée pour créer des connexions au fournisseur JMS.

### Files d'attente dans IBM WebSphere Application Server
Dans IBM WAS, les files d'attente JMS sont configurées en tant que ressources au sein de l'infrastructure de messagerie du serveur. WAS prend en charge :
- **Fournisseur de messagerie par défaut** : Moteur JMS intégré pour une messagerie légère.
- **Intégration avec IBM MQ** : Pour une mise en file d'attente plus robuste et évolutive.

#### Bases de la configuration
Pour utiliser les files d'attente dans WAS :
1.  **Créer un bus JMS** : Un regroupement logique de serveurs pour le routage des messages.
2.  **Ajouter des membres au bus** : Inclure les serveurs d'applications au bus.
3.  **Créer des destinations de file d'attente** : Définir la file d'attente (par exemple, le nom, la liaison JNDI) et la lier au bus.
4.  **Configurer les fabriques de connexions** : Pour que les producteurs/consommateurs puissent se connecter.
5.  **Spécifications d'activation** : Pour que les message-driven beans (MDBs) consomment automatiquement les messages des files d'attente.

Les files d'attente peuvent être surveillées via la console d'administration de WAS pour la profondeur, l'âge et le débit. Par exemple, vous pourriez créer une file d'attente nommée `MyApp.Queue` avec un nom JNDI comme `jms/queue/MyQueue` pour la recherche dans le code.

#### Exemple d'utilisation
Dans une application bancaire, une file d'attente pourrait gérer les demandes de transaction : Un frontend envoie un message à la file d'attente, et un MDB backend le traite un par un, garantissant l'absence de doublons.

Pour une configuration détaillée, reportez-vous à la documentation d'IBM.

### Références
- [Configuration de Java Message Service pour WebSphere Application Server](https://www.ibm.com/docs/en/mfci/7.6.2?topic=clusters-configuring-jms-websphere-application-server)
- [Collection de files d'attente dans WebSphere Application Server](https://www.ibm.com/docs/en/was/8.5.5?topic=s-queue-collection)