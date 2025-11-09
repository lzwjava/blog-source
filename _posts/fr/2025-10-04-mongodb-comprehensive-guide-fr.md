---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Guide Complet de MongoDB
translated: true
type: note
---

MongoDB est une base de données de documents NoSQL open-source populaire conçue pour le développement d'applications modernes. Elle stocke les données dans des documents flexibles, de type JSON, appelés BSON (Binary JSON), ce qui la rend idéale pour gérer des données non structurées ou semi-structurées. Contrairement aux bases de données relationnelles traditionnelles, MongoDB utilise une approche sans schéma, permettant aux collections (groupes de documents) d'avoir des structures variables. Elle est hautement évolutive, prend en charge la mise à l'échelle horizontale via le sharding et offre une haute disponibilité grâce à la réplication. MongoDB peut être déployée sur site, dans le cloud via MongoDB Atlas (un service managé) ou dans des environnements hybrides. Ce guide couvre tout, des bases aux sujets avancés, avec des exemples utilisant le MongoDB Shell (mongosh).

## Introduction

MongoDB excelle dans les scénarios nécessitant un développement rapide, des modèles de données flexibles et des performances élevées. Les principales fonctionnalités incluent :
- **Modèle de document** : Les données sont stockées sous forme de documents autonomes avec des structures imbriquées.
- **Langage de requête** : Requêtes riches utilisant une syntaxe similaire aux objets JavaScript.
- **Évolutivité** : Prise en charge intégrée des systèmes distribués.
- **Écosystème** : S'intègre avec des langages comme Python, Node.js, Java via des pilotes officiels.

Elle est utilisée par des entreprises comme Adobe, eBay et Forbes pour des applications impliquant le big data, l'analyse en temps réel et la gestion de contenu.

## Installation

MongoDB propose des éditions Community (gratuite, open-source) et Enterprise. L'installation varie selon la plateforme ; téléchargez toujours depuis le site officiel pour des raisons de sécurité.

### Windows
- Téléchargez le programme d'installation MSI depuis le Centre de téléchargement MongoDB.
- Exécutez l'installateur, sélectionnez l'installation "Complete" et incluez MongoDB Compass (outil graphique).
- Ajoutez le répertoire `bin` de MongoDB (par exemple, `C:\Program Files\MongoDB\Server\8.0\bin`) à votre variable d'environnement PATH.
- Créez un répertoire de données : `mkdir -p C:\data\db`.
- Démarrez le serveur : `mongod.exe --dbpath C:\data\db`.

Pris en charge : Windows 11, Server 2022/2019.

### macOS
- Utilisez Homebrew : `brew tap mongodb/brew && brew install mongodb-community`.
- Ou téléchargez l'archive TGZ, extrayez-la et ajoutez-la au PATH.
- Créez le répertoire de données : `mkdir -p /data/db`.
- Démarrez : `mongod --dbpath /data/db` (ou utilisez `brew services start mongodb/brew/mongodb-community`).

Pris en charge : macOS 11–14 (x86_64 et arm64).

### Linux
- Pour Ubuntu/Debian : Ajoutez la clé du dépôt MongoDB et la liste, puis `apt-get install -y mongodb-org`.
- Pour RHEL/CentOS : Utilisez yum/dnf avec le fichier de dépôt.
- Créez le répertoire de données : `sudo mkdir -p /data/db && sudo chown -R $USER /data/db`.
- Démarrez : `sudo systemctl start mongod`.

Pris en charge : Ubuntu 24.04, RHEL 9+, Debian 12, Amazon Linux 2023, etc. Utilisez les systèmes de fichiers XFS/EXT4 ; évitez le 32-bit.

### Cloud (MongoDB Atlas)
- Inscrivez-vous sur mongodb.com/atlas.
- Créez un cluster gratuit via l'interface utilisateur ou la CLI : `atlas clusters create <nom> --provider AWS --region us-east-1 --tier M0`.
- Mettez votre IP sur liste blanche : `atlas network-access create <IP>`.
- Obtenez la chaîne de connexion et connectez-vous : `mongosh "mongodb+srv://<utilisateur>:<motdepasse>@cluster0.abcde.mongodb.net/"`.

Atlas gère automatiquement les sauvegardes, la mise à l'échelle et la surveillance.

## Concepts de base

### Bases de données
Conteneurs pour les collections, séparant logiquement les données. Créées implicitement lors du premier usage : `use mabase`. Changez avec `use mabase`. Lister : `show dbs`.

### Collections
Groupes de documents, comme des tables mais avec un schéma flexible. Créées implicitement : `db.macollection.insertOne({})`. Lister : `show collections`.

### Documents
Unités de base : objets BSON avec des paires clé-valeur. Exemple :
```javascript
{ "_id": ObjectId("..."), "name": "John", "age": 30, "address": { "city": "NYC", "zip": 10001 } }
```
Prend en charge les tableaux, les objets imbriqués et les types comme les dates, les binaires.

### BSON
Format binaire pour un stockage et une transmission réseau efficaces. Étend JSON avec des types comme ObjectId, Date, Binary.

### Namespaces
Identifiants uniques : `base_de_données.collection` (par exemple, `mabase.commandes`).

Exemple de configuration :
```javascript
use test
db.orders.insertMany([
  { item: "amandes", price: 12, quantity: 2 },
  { item: "noix de pécan", price: 20, quantity: 1 }
])
```

## Opérations CRUD

Utilisez `db.collection.méthode()` dans mongosh. Transactions via des sessions pour l'ACID multi-documents.

### Créer (Insérer)
- Unique : `db.users.insertOne({ name: "Alice", email: "alice@example.com" })`
- Multiple : `db.users.insertMany([{ name: "Bob" }, { name: "Charlie" }])`
Retourne les IDs insérés.

### Lire (Trouver)
- Tous : `db.users.find()`
- Filtré : `db.users.find({ age: { $gt: 25 } })`
- Affichage formaté : `.pretty()`
- Limiter/trier : `db.users.find().limit(5).sort({ age: -1 })`

### Mettre à jour
- Unique : `db.users.updateOne({ name: "Alice" }, { $set: { age: 31 } })`
- Multiple : `db.users.updateMany({ age: { $lt: 20 } }, { $set: { status: "mineur" } })`
- Incrémenter : `{ $inc: { score: 10 } }`

### Supprimer
- Unique : `db.users.deleteOne({ name: "Bob" })`
- Multiple : `db.users.deleteMany({ status: "inactif" })`
- Supprimer la collection : `db.users.drop()`

## Interrogation et Indexation

### Interrogation
Utilisez des prédicats pour les conditions. Prend en charge l'égalité, les plages, les opérations logiques.

- Basique : `db.inventory.find({ status: "A" })` (équivalent SQL : `WHERE status = 'A'`)
- $in : `db.inventory.find({ status: { $in: ["A", "D"] } })`
- $lt/$gt : `db.inventory.find({ qty: { $lt: 30 } })`
- $or : `db.inventory.find({ $or: [{ status: "A" }, { qty: { $lt: 30 } }] })`
- Regex : `db.inventory.find({ item: /^p/ })` (commence par "p")
- Imbriqué : `db.users.find({ "address.city": "NYC" })`

Projection (sélectionner des champs) : `db.users.find({ age: { $gt: 25 } }, { name: 1, _id: 0 })`

### Indexation
Améliore la vitesse des requêtes en évitant les analyses complètes. Basée sur les arbres B.

- Types : Champ unique (`db.users.createIndex({ name: 1 })`), Composé (`{ name: 1, age: -1 }`), Unique (`{ email: 1 }`).
- Avantages : Requêtes d'égalité/plage plus rapides, résultats triés.
- Création : `db.users.createIndex({ age: 1 })` (ascendant).
- Voir : `db.users.getIndexes()`
- Supprimer : `db.users.dropIndex("age_1")`

Utilisez l'Atlas Performance Advisor pour des recommandations. Compromis : écritures plus lentes.

## Cadre d'agrégation

Traite les données à travers des étapes dans un pipeline. Similaire à SQL GROUP BY mais plus puissant.

- Basique : `db.orders.aggregate([ { $match: { price: { $lt: 15 } } } ])`
- Étapes : `$match` (filtrer), `$group` (agréger : `{ $sum: "$price" }`), `$sort`, `$lookup` (joindre : `{ from: "inventory", localField: "item", foreignField: "sku", as: "stock" }`), `$project` (remodeler).
- Exemple (joindre et trier) :
```javascript
db.orders.aggregate([
  { $match: { price: { $lt: 15 } } },
  { $lookup: { from: "inventory", localField: "item", foreignField: "sku", as: "inventory_docs" } },
  { $sort: { price: 1 } }
])
```
Expressions : `{ $add: [ "$price", 10 ] }`. Aperçu dans l'interface Atlas.

## Conception du schéma

La flexibilité de MongoDB évite les schémas rigides mais nécessite une conception réfléchie pour les performances.

- **Principes** : Modéliser selon les modèles d'accès (lectures/écritures), utiliser les index, garder le jeu de travail en RAM.
- **Incorporation** : Dénormaliser les données liées dans un seul document pour des lectures/écritures atomiques. Par ex., incorporer les commentaires dans les articles. Avantages : Requêtes rapides. Inconvénients : Duplication, documents volumineux.
- **Référencement** : Normaliser avec des IDs. Par ex., `posts` référence `users` via `userId`. Utilisez `$lookup` pour les jointures. Avantages : Moins de duplication. Inconvénients : Requêtes multiples.
- Modèles : Un-à-peu (incorporer), Un-à-plusieurs (référencer ou incorporer un tableau), Plusieurs-à-plusieurs (référencer).
- Validation : Appliquer avec `db.createCollection("users", { validator: { $jsonSchema: { ... } } })`.

Envisagez les compromis de duplication et l'atomicité (uniquement au niveau du document).

## Réplication et Sharding

### Réplication
Fournit la redondance et la haute disponibilité via des ensembles de réplicas (groupe d'instances `mongod`).

- Composants : Primaire (écritures), Secondaires (répliquent via l'oplog, lectures optionnelles), Arbitre (vote, pas de données).
- Déploiement : Initialiser avec `rs.initiate({ _id: "rs0", members: [{ _id: 0, host: "host1:27017" }] })`. Ajouter des membres : `rs.add("host2:27017")`.
- Élections : Si le primaire tombe en panne, un secondaire est élu en ~10-12s.
- Préférence de lecture : `primary`, `secondary` (peut être en retard).
- Utiliser pour le basculement, les sauvegardes. Activez le contrôle de flux pour gérer le décalage.

### Sharding
Mise à l'échelle horizontale : Distribuer les données sur plusieurs shards.

- Composants : Shards (ensembles de réplicas), Mongos (routeurs), Serveurs de configuration (métadonnées).
- Clé de sharding : Champ(s) pour le partitionnement (par ex., haché pour une distribution uniforme). Créez d'abord l'index.
- Configuration : Activer le sharding `sh.enableSharding("mabase")`, sharder la collection `sh.shardCollection("mabase.users", { userId: "hashed" })`.
- Balancer : Migre les chunks pour une charge uniforme. Zones pour la localisation géographique.
- Stratégies : Haché (uniforme), Par plage (requêtes ciblées).

Connectez-vous via mongos ; prend en charge les transactions.

## Sécurité

Sécurisez les déploiements avec des protections superposées.

- **Authentification** : SCRAM, LDAP, OIDC, X.509. Créer des utilisateurs : `db.createUser({ user: "admin", pwd: "pass", roles: ["root"] })`.
- **Autorisation** : Contrôle d'accès basé sur les rôles (RBAC). Rôles intégrés : read, readWrite, dbAdmin.
- **Chiffrement** : TLS/SSL pour le transit, Chiffrement au repos (EAR) via AWS KMS/Google Cloud KMS/Azure Key Vault. Chiffrement côté client au niveau des champs (CSFLE) pour les champs sensibles.
- Réseau : Listes de contrôle d'accès IP, appairage VPC dans Atlas.
- Audit : Journaliser les opérations.

Activez l'authentification au démarrage : `--auth`. Utilisez Atlas pour la sécurité intégrée.

## Bonnes pratiques

- **Configuration de production** : Exécutez en tant que service (systemctl/brew). Séparez les données/journaux/logs sur des SSD. Utilisez le moteur WiredTiger (par défaut).
- **Surveillance** : `mongostat`, `mongotop`, graphiques Atlas. Surveillez les connexions (`connPoolStats`), les évictions du cache, les E/S (`iostat`).
- **Sauvegardes** : `mongodump`/`mongorestore`, ou les instantanés Atlas. Logique (JSON) vs physique (fichiers).
- **Performances** : Indexez judicieusement, limitez les projections, évitez les grands tableaux. Définissez `ulimit -n 64000`, désactivez le swap (`vm.swappiness=0`), ajustez TCP keepalive.
- **Mise à l'échelle** : Commencez avec des ensembles de réplicas ; shardez au-delà de 100 Go ou pour un débit élevé.
- **Import de données** : `mongoimport --db test --collection users --file users.json`.
- **Outils** : MongoDB Compass (interface graphique), mongosh (shell), pilotes pour les applications.
- **Pièges courants** : Incorporation excessive (limite de taille de document 16 Mo), ignorance des index, non-gestion du décalage de réplication.

Pour le développement, utilisez le niveau gratuit Atlas M0. Testez les charges de travail avec `mongoperf`.

## Références
- [Manuel MongoDB](https://www.mongodb.com/docs/manual/)
- [Installation MongoDB](https://www.mongodb.com/docs/manual/installation/)
- [Concepts de base MongoDB](https://www.mongodb.com/docs/manual/core/)
- [CRUD MongoDB](https://www.mongodb.com/docs/manual/crud/)
- [Interrogation MongoDB](https://www.mongodb.com/docs/manual/tutorial/query-documents/)
- [Index MongoDB](https://www.mongodb.com/docs/manual/indexes/)
- [Agrégation MongoDB](https://www.mongodb.com/docs/manual/core/aggregation-pipeline/)
- [Conception du schéma MongoDB](https://www.mongodb.com/docs/manual/core/data-model-design/)
- [Réplication MongoDB](https://www.mongodb.com/docs/manual/replication/)
- [Sharding MongoDB](https://www.mongodb.com/docs/manual/sharding/)
- [Sécurité MongoDB](https://www.mongodb.com/docs/manual/core/security/)
- [Notes de production MongoDB](https://www.mongodb.com/docs/manual/administration/production-notes/)