---
audio: false
generated: true
lang: fr
layout: post
title: Pourquoi Kafka est-il rapide
translated: true
type: note
---

### Points Clés
- Il semble probable que la vidéo "System Design: Why is Kafka fast?" explique la vitesse d'Apache Kafka par son architecture et ses choix de conception.
- Les recherches suggèrent que les performances de Kafka sont améliorées par les journaux en mode ajout seul (append-only logs), les principes de zéro copie (zero-copy), le traitement par lots (batch processing) et le partitionnement efficace.
- Les preuves tendent à indiquer que la vitesse de Kafka est due à la conception de sa plateforme de streaming d'événements distribuée, avec des composants clés comme les producteurs, les brokers et les consommateurs.

### Introduction
Ce billet de blog est basé sur le contenu de la vidéo YouTube "System Design: Why is Kafka fast?" de ByteByteGo, visant à transformer ses enseignements en un format écrit pour une lecture et une référence plus faciles. Apache Kafka est réputé pour ses hautes performances dans le traitement de données en temps réel, et ce billet explore les raisons de sa rapidité, le rendant accessible à ceux qui découvrent le sujet.

### Composants Principaux de Kafka
Apache Kafka fonctionne comme une plateforme de streaming d'événements distribuée avec trois composants principaux :
- **Producteurs (Producers)** : Applications qui envoient des données vers les topics Kafka.
- **Brokers** : Serveurs qui stockent et gèrent les données, assurant la réplication et la distribution.
- **Consommateurs (Consumers)** : Applications qui lisent et traitent les données des topics.

Cette structure permet à Kafka de gérer efficacement de grands volumes de données, contribuant à sa rapidité.

### Couches Architecturales et Optimisations des Performances
L'architecture de Kafka est divisée en deux couches :
- **Couche de Calcul (Compute Layer)** : Inclut les API pour les producteurs, les consommateurs et le traitement de flux (stream processing), facilitant l'interaction.
- **Couche de Stockage (Storage Layer)** : Comprend les brokers qui gèrent le stockage des données dans les topics et les partitions, optimisé pour les performances.

Les optimisations clés incluent :
- **Journaux en Ajout Seul (Append-Only Logs)** : Écrire les données séquentiellement à la fin d'un fichier, ce qui est plus rapide que les écritures aléatoires.
- **Principe de Zéro Copie (Zero-Copy Principle)** : Transférer les données directement du producteur au consommateur, réduisant la charge CPU.
- **Traitement par Lots (Batch Processing)** : Traiter les données par lots pour réduire la surcharge par enregistrement.
- **Réplication Asynchrone (Asynchronous Replication)** : Permettre au broker leader de traiter les requêtes pendant que les répliques se mettent à jour, garantissant la disponibilité sans perte de performance.
- **Partitionnement (Partitioning)** : Distribuer les données sur plusieurs partitions pour un traitement parallèle et un débit élevé.

Ces choix de conception, détaillés dans un billet de blog de support de ByteByteGo ([Why is Kafka so fast? How does it work?](https://bytebytego.substack.com/p/why-is-kafka-so-fast-how-does-it)), expliquent pourquoi Kafka excelle en vitesse et en extensibilité.

### Flux de Données et Structure d'un Enregistrement
Lorsqu'un producteur envoie un enregistrement à un broker, celui-ci est validé, ajouté à un journal de validation (commit log) sur le disque, et répliqué pour la durabilité, le producteur étant notifié une fois l'engagement (commit) effectué. Ce processus est optimisé pour les E/S séquentielles, améliorant les performances.

Chaque enregistrement comprend :
- Horodatage (Timestamp) : Quand l'événement a été créé.
- Clé (Key) : Pour le partitionnement et l'ordonnancement.
- Valeur (Value) : Les données réelles.
- En-têtes (Headers) : Métadonnées optionnelles.

Cette structure, telle que décrite dans le billet de blog, garantit une gestion efficace des données et contribue à la vitesse de Kafka.

---

### Note d'Enquête : Analyse Détaillée des Performances d'Apache Kafka

Cette section propose une exploration complète des performances d'Apache Kafka, développant le contenu de la vidéo "System Design: Why is Kafka fast?" de ByteByteGo, et s'appuyant sur des ressources supplémentaires pour assurer une compréhension approfondie. L'analyse est structurée pour couvrir l'architecture de Kafka, ses composants et ses optimisations spécifiques, avec des explications détaillées et des exemples pour plus de clarté.

#### Contexte
Apache Kafka, développé comme une plateforme de streaming d'événements distribuée, est réputé pour sa capacité à gérer le streaming de données à haut débit et faible latence, ce qui en fait un pilier des architectures de données modernes. La vidéo, publiée le 29 juin 2022 et faisant partie d'une playlist sur la conception de systèmes, vise à élucider pourquoi Kafka est rapide, un sujet d'intérêt majeur compte tenu de la croissance exponentielle des besoins en streaming de données. L'analyse ici présentée s'inspire d'un billet de blog détaillé de ByteByteGo ([Why is Kafka so fast? How does it work?](https://bytebytego.substack.com/p/why-is-kafka-so-fast-how-does-it)), qui complète le contenu de la vidéo et fournit des insights supplémentaires.

#### Composants Principaux et Architecture de Kafka
La rapidité de Kafka commence par ses composants principaux :
- **Producteurs (Producers)** : Ce sont des applications ou des systèmes qui génèrent et envoient des événements vers les topics Kafka. Par exemple, une application web peut produire des événements pour les interactions des utilisateurs.
- **Brokers** : Ce sont les serveurs formant un cluster, responsables du stockage des données, de la gestion des partitions et de la réplication. Une configuration typique peut impliquer plusieurs brokers pour la tolérance aux pannes et l'extensibilité.
- **Consommateurs (Consumers)** : Applications qui s'abonnent aux topics pour lire et traiter les événements, comme des moteurs d'analyse traitant des données en temps réel.

L'architecture positionne Kafka comme une plateforme de streaming d'événements, utilisant le terme "événement" au lieu de "message", ce qui le distingue des files de messages traditionnelles. Cela est évident dans sa conception, où les événements sont immuables et ordonnés par des offsets dans les partitions, comme détaillé dans le billet de blog.

| Composant       | Rôle                                                                 |
|-----------------|----------------------------------------------------------------------|
| Producteur (Producer) | Envoie des événements vers les topics, initiant le flux de données. |
| Broker          | Stocke et gère les données, gère la réplication et sert les consommateurs. |
| Consommateur (Consumer) | Lit et traite les événements des topics, permettant l'analyse en temps réel. |

Le billet de blog inclut un diagramme à [cette URL](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd3690db-87b8-4165-8798-37d1d083f837_1600x1527.png), illustrant cette architecture, qui montre l'interaction entre les producteurs, les brokers et les consommateurs en mode cluster.

#### Architecture en Couches : Calcul et Stockage
L'architecture de Kafka est divisée en :
- **Couche de Calcul (Compute Layer)** : Facilite la communication via des API :
  - **API Producteur (Producer API)** : Utilisée par les applications pour envoyer des événements.
  - **API Consommateur (Consumer API)** : Permet de lire les événements.
  - **API Kafka Connect** : Intègre avec des systèmes externes comme des bases de données.
  - **API Kafka Streams** : Prend en charge le traitement de flux, comme la création d'un KStream pour un topic comme "orders" avec Serdes pour la sérialisation, et ksqlDB pour les travaux de traitement de flux avec une API REST. Un exemple fourni est de s'abonner à "orders", d'agréger par produits et d'envoyer vers "ordersByProduct" pour l'analyse.
- **Couche de Stockage (Storage Layer)** : Comprend les brokers Kafka dans des clusters, avec les données organisées en topics et partitions. Les topics sont similaires à des tables de base de données, et les partitions sont distribuées sur les nœuds, assurant l'extensibilité. Les événements dans les partitions sont ordonnés par des offsets, immuables et en ajout seul, la suppression étant traitée comme un événement, améliorant les performances d'écriture.

Le billet de blog détaille cela, notant que les brokers gèrent les partitions, les lectures, les écritures et les réplications, avec un diagramme à [cette URL](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb869cd88-3d6e-43af-8fd0-26f3737d8f1f_1600x559.png) illustrant la réplication, comme la Partition 0 dans "orders" avec trois répliques : leader sur le Broker 1 (offset 4), followers sur le Broker 2 (offset 2) et le Broker 3 (offset 3).

| Couche           | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| Couche de Calcul (Compute Layer) | APIs pour l'interaction : Producer, Consumer, Connect, Streams et ksqlDB. |
| Couche de Stockage (Storage Layer) | Brokers en clusters, topics/partitions distribués, événements ordonnés par offsets. |

#### Plans de Contrôle et de Données
- **Plan de Contrôle (Control Plane)** : Gère les métadonnées du cluster, utilisant historiquement Zookeeper, maintenant remplacé par le module KRaft avec des contrôleurs sur des brokers sélectionnés. Cette simplification élimine Zookeeper, rendant la configuration plus facile et la propagation des métadonnées plus efficace via un topic spécial, comme noté dans le billet de blog.
- **Plan de Données (Data Plane)** : Gère la réplication des données, avec un processus où les followers émettent un FetchRequest, le leader envoie les données et valide (commit) les enregistrements avant un certain offset, garantissant la cohérence. L'exemple de la Partition 0 avec les offsets 2, 3 et 4 met cela en évidence, avec un diagramme à [cette URL](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe17a4454-a194-45f9-8a1f-f4882501657c_1095x1600.png).

#### Structure d'un Enregistrement et Opérations des Brokers
Chaque enregistrement, l'abstraction d'un événement, comprend :
- Horodatage (Timestamp) : Quand il a été créé.
- Clé (Key) : Pour l'ordonnancement, la colocalisation et la rétention, crucial pour le partitionnement.
- Valeur (Value) : Le contenu des données.
- En-têtes (Headers) : Métadonnées optionnelles.

La clé et la valeur sont des tableaux d'octets, encodés/décodés avec serdes, garantissant la flexibilité. Les opérations des brokers impliquent :
- La requête du producteur atterrissant dans le tampon de réception du socket (socket receive buffer).
- Le thread réseau la déplaçant vers une file d'attente de requêtes partagée.
- Le thread E/S validant le CRC, l'ajoutant au journal de validation (commit log) (segments de disque avec données et index).
- Les requêtes stockées dans "purgatory" en attente de réplication.
- La réponse mise en file d'attente, le thread réseau l'envoyant via le tampon d'envoi du socket (socket send buffer).

Ce processus, optimisé pour les E/S séquentielles, est détaillé dans le billet de blog, avec des diagrammes illustrant le flux, contribuant significativement à la vitesse de Kafka.

| Composant de l'Enregistrement | Objectif                                                                 |
|------------------|-------------------------------------------------------------------------|
| Horodatage (Timestamp) | Enregistre quand l'événement a été créé.                                     |
| Clé (Key) | Assure l'ordonnancement, la colocalisation et la rétention pour le partitionnement. |
| Valeur (Value) | Contient le contenu réel des données.                                       |
| En-têtes (Headers) | Métadonnées optionnelles pour des informations supplémentaires.          |

#### Optimisations des Performances
Plusieurs décisions de conception améliorent la vitesse de Kafka :
- **Journaux en Ajout Seul (Append-Only Logs)** : Écrire séquentiellement à la fin d'un fichier minimise le temps de recherche sur le disque, comparable à ajouter des entrées à un journal à la fin, plus rapide qu'une insertion au milieu du document.
- **Principe de Zéro Copie (Zero-Copy Principle)** : Transfère les données directement du producteur au consommateur, réduisant la charge CPU, comme déplacer une boîte du camion à l'entrepôt sans la déballer, économisant du temps.
- **Traitement par Lots (Batch Processing)** : Traiter les données par lots réduit la surcharge par enregistrement, améliorant l'efficacité.
- **Réplication Asynchrone (Asynchronous Replication)** : Le broker leader traite les requêtes pendant que les répliques se mettent à jour, garantissant la disponibilité sans impact sur les performances.
- **Partitionnement (Partitioning)** : Distribue les données sur les partitions pour un traitement parallèle, augmentant le débit, un facteur clé pour gérer de grands volumes de données.

Ces optimisations, telles qu'explorées dans le billet de blog, expliquent pourquoi Kafka atteint un haut débit et une faible latence, le rendant adapté aux applications en temps réel.

#### Conclusion et Insights Supplémentaires
La rapidité d'Apache Kafka est le résultat de son architecture méticuleusement conçue et de ses optimisations de performances, tirant parti des journaux en ajout seul, des principes de zéro copie, du traitement par lots, de la réplication asynchrone et d'un partitionnement efficace. Cette analyse, basée sur la vidéo et complétée par le billet de blog, offre une vision complète, inattendue par sa profondeur pour ceux qui s'attendaient à un simple aperçu, révélant l'équilibre complexe des choix de conception qui font de Kafka un leader dans le streaming de données.

Le billet de blog propose également un essai gratuit de 7 jours pour les archives complètes, accessible via [ce lien d'abonnement](https://blog.bytebytego.com/subscribe?simple=true&next=https%3A%2F%2Fblog.bytebytego.com%2Fp%2Fwhy-is-kafka-so-fast-how-does-it&utm_source=paywall-free-trial&utm_medium=web&utm_content=137028631&coupon=3920da80), fournissant d'autres ressources pour les personnes intéressées.

Cette exploration détaillée assure une compréhension complète, s'alignant sur l'intention de la vidéo d'éduquer sur les performances de Kafka, et est informée par les recherches et insights recueillis auprès de diverses sources, garantissant exactitude et profondeur.

#### Citations Clés
- [Vidéo YouTube System Design: Why is Kafka fast?](https://www.youtube.com/watch?v=UNUz1-msbOM)
- [Billet de blog ByteByteGo : Why is Kafka so fast? How does it work?](https://bytebytego.substack.com/p/why-is-kafka-so-fast-how-does-it)
- [Diagramme d'architecture Kafka ByteByteGo](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd3690db-87b8-4165-8798-37d1d083f837_1600x1527.png)
- [Diagramme de réplication Kafka ByteByteGo](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb869cd88-3d6e-43af-8fd0-26f3737d8f1f_1600x559.png)
- [Diagramme des opérations des brokers Kafka ByteByteGo](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe17a4454-a194-45f9-8a1f-f4882501657c_1095x1600.png)
- [Abonnement à la newsletter ByteByteGo pour le billet sur Kafka](https://blog.bytebytego.com/subscribe?simple=true&next=https%3A%2F%2Fblog.bytebytego.com%2Fp%2Fwhy-is-kafka-so-fast-how-does-it&utm_source=paywall-free-trial&utm_medium=web&utm_content=137028631&coupon=3920da80)