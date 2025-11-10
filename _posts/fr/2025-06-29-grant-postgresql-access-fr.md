---
audio: false
generated: true
lang: fr
layout: post
title: Octroi d'accès à la base de données PostgreSQL
translated: true
type: note
---

Pour accorder à un utilisateur l'accès à une base de données dans PostgreSQL, vous devez suivre ces étapes. Je vais vous guider à travers le processus en utilisant des commandes SQL dans l'interface en ligne de commande psql.

**Se connecter à PostgreSQL** : Vous êtes déjà connecté à PostgreSQL en utilisant l'utilisateur `postgres`, qui dispose généralement de privilèges de superutilisateur.

**Créer un utilisateur (s'il n'existe pas déjà)** : Si l'utilisateur n'existe pas, vous pouvez en créer un en utilisant la commande suivante. Remplacez `username` et `password` par le nom d'utilisateur et le mot de passe souhaités.

```
CREATE USER username WITH PASSWORD 'password';
```

**Créer une base de données (si elle n'existe pas déjà)** : Si la base de données n'existe pas, vous pouvez la créer en utilisant la commande suivante. Remplacez `database_name` par le nom de base de données souhaité.

```
CREATE DATABASE database_name;
```

**Accorder les privilèges sur la base de données** : Pour accorder tous les privilèges sur une base de données spécifique à l'utilisateur, utilisez la commande suivante. Remplacez `database_name` et `username` par les noms appropriés.

```
GRANT ALL PRIVILEGES ON DATABASE database_name TO username;
```

**Accorder l'utilisation sur le schéma** : Si vous souhaitez que l'utilisateur ait accès à un schéma spécifique dans la base de données, vous pouvez accorder l'utilisation sur le schéma. Remplacez `schema_name` et `username` par les noms appropriés.

```
GRANT USAGE ON SCHEMA schema_name TO username;
```

**Accorder les privilèges sur les tables** : Pour accorder des privilèges spécifiques sur les tables dans un schéma, vous pouvez utiliser la commande suivante. Remplacez `schema_name`, `table_name` et `username` par les noms appropriés.

```
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA schema_name TO username;
```

**Rendre les privilèges effectifs** : Si vous avez accordé des privilèges sur les tables, vous devrez peut-être également définir les privilèges par défaut pour les tables futures.

```
ALTER DEFAULT PRIVILEGES IN SCHEMA schema_name GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO username;
```

Voici un exemple de ce à quoi les commandes pourraient ressembler :

```
CREATE USER myuser WITH PASSWORD 'mypassword';
CREATE DATABASE mydatabase;
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
\c mydatabase
GRANT USAGE ON SCHEMA public TO myuser;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO myuser;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO myuser;
```

Ces commandes configureront un utilisateur avec un accès complet à une base de données spécifique et à ses tables. Ajustez les commandes en fonction de vos besoins spécifiques et de vos politiques de sécurité.