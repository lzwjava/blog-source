---
audio: false
generated: true
lang: fr
layout: post
title: Guide Redis
translated: true
type: note
---

Voici un guide complet sur Redis, un système de stockage de structures de données en mémoire open source, largement utilisé comme base de données, cache et courtier de messages. Ce guide couvrira ses fondamentaux, ses fonctionnalités, ses cas d'utilisation, son installation, ses opérations de base et ses concepts avancés.

---

### Qu'est-ce que Redis ?
Redis (Remote Dictionary Server) est un magasin clé-valeur haute performance qui fonctionne principalement en mémoire, ce qui le rend exceptionnellement rapide. Il prend en charge diverses structures de données telles que les chaînes de caractères, les hachages, les listes, les ensembles, les ensembles triés, les bitmaps, les hyperloglogs et les index géospatiaux. Créé par Salvatore Sanfilippo en 2009, Redis est maintenant maintenu par une communauté et sponsorisé par Redis Inc.

Caractéristiques principales :
- **En mémoire** : Les données sont stockées dans la RAM pour un accès à faible latence.
- **Persistant** : Offre une persistance optionnelle sur disque pour la durabilité.
- **Polyvalent** : Prend en charge des structures de données complexes au-delà des simples paires clé-valeur.
- **Évolutif** : Fournit le clustering et la réplication pour une haute disponibilité.

---

### Pourquoi utiliser Redis ?
Redis est populaire pour sa vitesse et sa flexibilité. Les cas d'utilisation courants incluent :
1. **Mise en cache** : Accélère les applications en stockant les données fréquemment accédées (ex: réponses d'API, pages web).
2. **Gestion de sessions** : Stocke les données de session utilisateur dans les applications web.
3. **Analyse en temps réel** : Suit les métriques, les classements ou les compteurs d'événements.
4. **Messagerie Pub/Sub** : Permet la messagerie en temps réel entre processus ou services.
5. **Files d'attente de tâches** : Gère les tâches en arrière-plan (ex: avec des outils comme Celery).
6. **Applications géospatiales** : Gère les requêtes basées sur la localisation (ex: trouver des points d'intérêt à proximité).

---

### Fonctionnalités principales
1. **Structures de données** :
   - **Strings** : Paires clé-valeur simples (ex: `SET key "value"`).
   - **Lists** : Collections ordonnées (ex: `LPUSH mylist "item"`).
   - **Sets** : Collections non ordonnées et uniques (ex: `SADD myset "item"`).
   - **Sorted Sets** : Ensembles avec des scores pour le classement (ex: `ZADD leaderboard 100 "player1"`).
   - **Hashes** : Mappages clé-valeur (ex: `HSET user:1 name "Alice"`).
   - **Bitmaps, HyperLogLogs, Streams** : Pour des cas d'utilisation spécialisés comme le comptage d'utilisateurs uniques ou le streaming d'événements.

2. **Persistance** :
   - **RDB (Snapshotting)** : Sauvegarde périodiquement les données sur le disque sous forme d'instantané à un instant donné.
   - **AOF (Append-Only File)** : Journalise chaque opération d'écriture pour la durabilité ; peut être rejoué pour reconstruire le jeu de données.

3. **Réplication** : Réplication maître-esclave pour la haute disponibilité et l'évolutivité en lecture.
4. **Clustering** : Répartit les données sur plusieurs nœuds pour une mise à l'échelle horizontale.
5. **Opérations atomiques** : Garantit un accès concurrent sûr avec des commandes comme `INCR` ou `MULTI`.
6. **Scripting Lua** : Permet une logique personnalisée côté serveur.
7. **Pub/Sub** : Système de messagerie léger pour la communication en temps réel.

---

### Installation
Redis est disponible sur Linux, macOS et Windows (via WSL ou des builds non officiels). Voici comment l'installer sur un système Linux :

1. **Via le gestionnaire de paquets** (Ubuntu/Debian) :
   ```bash
   sudo apt update
   sudo apt install redis-server
   ```

2. **À partir des sources** :
   ```bash
   wget http://download.redis.io/releases/redis-7.0.15.tar.gz
   tar xzf redis-7.0.15.tar.gz
   cd redis-7.0.15
   make
   sudo make install
   ```

3. **Démarrer Redis** :
   ```bash
   redis-server
   ```

4. **Vérifier l'installation** :
   ```bash
   redis-cli ping
   ```
   Sortie : `PONG`

5. **Configuration** : Modifiez `/etc/redis/redis.conf` (ou équivalent) pour ajuster les paramètres comme la persistance, les limites de mémoire ou la liaison à des IP spécifiques.

---

### Opérations de base
Redis utilise une interface simple basée sur des commandes via `redis-cli` ou des bibliothèques client. Voici quelques exemples :

#### Strings
- Définir une valeur : `SET name "Alice"`
- Obtenir une valeur : `GET name` → `"Alice"`
- Incrémenter : `INCR counter` → `1` (s'incrémente à 2, 3, etc.)

#### Lists
- Ajouter à gauche : `LPUSH mylist "item1"`
- Ajouter à droite : `RPUSH mylist "item2"`
- Retirer de gauche : `LPOP mylist` → `"item1"`

#### Sets
- Ajouter des éléments : `SADD myset "apple" "banana"`
- Lister les membres : `SMEMBERS myset` → `"apple" "banana"`
- Vérifier l'appartenance : `SISMEMBER myset "apple"` → `1` (vrai)

#### Hashes
- Définir des champs : `HSET user:1 name "Bob" age "30"`
- Obtenir un champ : `HGET user:1 name` → `"Bob"`
- Obtenir tous les champs : `HGETALL user:1`

#### Sorted Sets
- Ajouter avec un score : `ZADD leaderboard 100 "player1" 200 "player2"`
- Obtenir les meilleurs scores : `ZRANGE leaderboard 0 1 WITHSCORES` → `"player1" "100" "player2" "200"`

---

### Concepts avancés
1. **Configuration de la persistance** :
   - Activer RDB : Définir `save 60 1000` dans `redis.conf` (sauvegarde toutes les 60s si 1000 clés changent).
   - Activer AOF : Définir `appendonly yes` pour la journalisation des écritures.

2. **Réplication** :
   - Configurer un esclave : `SLAVEOF master_ip master_port`.
   - Vérifier le statut : `INFO REPLICATION`.

3. **Clustering** :
   - Activer avec `cluster-enabled yes` dans `redis.conf`.
   - Utiliser `redis-cli --cluster create` pour configurer les nœuds.

4. **Politiques d'éviction** :
   - Contrôler l'utilisation de la mémoire avec `maxmemory` et des politiques comme `LRU` (least recently used) ou `LFU` (least frequently used).
   - Exemple : `maxmemory-policy allkeys-lru`.

5. **Transactions** :
   - Grouper les commandes : `MULTI`, suivi des commandes, puis `EXEC`.
   - Exemple :
     ```
     MULTI
     SET key1 "value1"
     SET key2 "value2"
     EXEC
     ```

6. **Pub/Sub** :
   - S'abonner : `SUBSCRIBE channel1`
   - Publier : `PUBLISH channel1 "Hello"`

---

### Bibliothèques client
Redis prend en charge de nombreux langages de programmation. Exemples :
- **Python** : `redis-py` (`pip install redis`)
  ```python
  import redis
  r = redis.Redis(host='localhost', port=6379, db=0)
  r.set('key', 'value')
  print(r.get('key'))  # b'value'
  ```
- **Node.js** : `ioredis`
  ```javascript
  const Redis = require('ioredis');
  const redis = new Redis();
  redis.set('key', 'value');
  redis.get('key').then(console.log); // 'value'
  ```

---

### Conseils de performance
1. **Utiliser le pipelining** : Regrouper les commandes pour réduire la latence des allers-retours.
2. **Optimiser les structures de données** : Choisir la bonne structure (ex: utiliser des hachages pour les petits objets au lieu de multiples clés).
3. **Surveiller la mémoire** : Utiliser `INFO MEMORY` pour suivre l'utilisation.
4. **Ajuster la persistance** : Équilibrer la vitesse (RDB) et la durabilité (AOF).

---

### Sécurité
- **Lier à localhost** : Définir `bind 127.0.0.1` dans `redis.conf` pour restreindre l'accès.
- **Définir un mot de passe** : Utiliser `requirepass yourpassword`.
- **Désactiver les commandes dangereuses** : Utiliser `rename-command` (ex: `rename-command FLUSHALL ""`).

---

### Limitations
- **Limité par la mémoire** : La taille des données est limitée par la RAM disponible.
- **Monothreadé** : Les opérations principales s'exécutent sur un seul thread (bien que les E/S et la persistance puissent utiliser plusieurs threads dans les versions récentes).
- **Pas de requêtes complexes** : Ne dispose pas de requêtes de type SQL ; repose sur l'accès par clé.

---

### Redis vs. Autres bases de données
- **Redis vs. Memcached** : Redis offre des structures de données plus riches et la persistance ; Memcached est plus simple et purement en mémoire.
- **Redis vs. MongoDB** : Redis est plus rapide pour la mise en cache mais moins adapté au stockage persistant complexe de documents.
- **Redis vs. PostgreSQL** : Redis excelle dans les tâches en temps réel à faible latence ; PostgreSQL est meilleur pour les données relationnelles et la conformité ACID.

---

### Ressources
- **Documentation officielle** : [redis.io](https://redis.io)
- **Essayez Redis** : [try.redis.io](https://try.redis.io) (tutoriel interactif)
- **GitHub** : [github.com/redis/redis](https://github.com/redis/redis)

---

Ce guide fournit une base solide pour comprendre et utiliser Redis. Faites-moi savoir si vous souhaitez une exploration plus approfondie d'un aspect spécifique !