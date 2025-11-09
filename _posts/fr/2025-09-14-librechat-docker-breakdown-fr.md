---
audio: false
date: 2025-09-14
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Décomposition du Service LibreChat Docker Compose
translated: true
type: note
---

Ce que vous avez collé est une configuration `docker-compose.yaml` pour exécuter **LibreChat** ainsi que ses dépendances. Laissez-moi l'expliquer clairement :

---

## Vue d'ensemble

La configuration définit **6 services (conteneurs)** qui fonctionnent ensemble :

1. **API/UI LibreChat (`api`)**
2. **MongoDB (`mongodb`)**
3. **Meilisearch (`meilisearch`)**
4. **Postgres avec pgvector (`vectordb`)**
5. **API RAG (`rag_api`)**
6. **Volumes pour le stockage persistant**

Tous ces éléments sont connectés à l'aide de Docker Compose, ce qui vous permet de tout démarrer avec une seule commande `docker-compose up`.

---

## Explications des Services

### 1. API LibreChat (`api`)

* **Nom du conteneur :** `LibreChat`
* **Image :** `ghcr.io/danny-avila/librechat-dev:latest` (la version de développement de LibreChat)
* **Ports :** Expose `${PORT}` du fichier `.env` sur votre machine hôte.
* **Dépendances :** Attend que `mongodb` et `rag_api` soient démarrés.
* **Variables d'environnement :**

  * `MONGO_URI` : Chaîne de connexion pour MongoDB.
  * `MEILI_HOST` : Pointe vers le service Meilisearch.
  * `RAG_API_URL` : Se connecte au conteneur local de l'API RAG.
* **Volumes :**

  * Le fichier `.env` est monté dans le conteneur.
  * `images`, `uploads` et `logs` sont persistés localement pour ne pas les perdre au redémarrage du conteneur.

👉 C'est l'application principale avec laquelle vous interagissez (le service web/API LibreChat).

---

### 2. MongoDB (`mongodb`)

* **Nom du conteneur :** `chat-mongodb`
* **Image :** `mongo` (image officielle MongoDB).
* **Objectif :** Stocke les données de chat, les sessions utilisateur, la configuration, etc.
* **Commande :** Exécute `mongod --noauth` (sans authentification).
* **Volumes :** `./data-node:/data/db` pour que votre base de données persiste en dehors du conteneur.

---

### 3. Meilisearch (`meilisearch`)

* **Nom du conteneur :** `chat-meilisearch`
* **Image :** `getmeili/meilisearch:v1.12.3`
* **Objectif :** Fournit des **capacités de recherche en texte intégral rapides** pour LibreChat.
* **Variables d'environnement :**

  * `MEILI_NO_ANALYTICS=true` (vie privée).
  * `MEILI_MASTER_KEY` est récupérée depuis `.env`.
* **Volumes :** `./meili_data_v1.12:/meili_data` pour la persistance.

---

### 4. Base de données vectorielle (`vectordb`)

* **Nom du conteneur :** `vectordb`
* **Image :** `pgvector/pgvector:0.8.0-pg15-trixie` (Postgres avec l'extension pgvector).
* **Objectif :** Stocke les embeddings pour le RAG (Retrieval Augmented Generation).
* **Environnement :**

  * `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`.
* **Volume :** `pgdata2:/var/lib/postgresql/data` pour la persistance.

---

### 5. API RAG (`rag_api`)

* **Nom du conteneur :** `rag_api`
* **Image :** `ghcr.io/danny-avila/librechat-rag-api-dev-lite:latest`
* **Objectif :** Gère les workflows RAG — récupération de documents et enrichissement des réponses du modèle avec des connaissances externes.
* **Environnement :**

  * `DB_HOST=vectordb` (se connecte à la base de données vectorielle Postgres).
  * `RAG_PORT` par défaut à `8000`.
* **Dépend de :** `vectordb`.
* **Fichier d'environnement :** Réutilise votre fichier `.env`.

---

### 6. Volumes

* **`pgdata2`** → Données persistantes pour Postgres/pgvector.
* Les autres volumes comme `./meili_data_v1.12`, `./data-node` et les répertoires montés (`images`, `uploads`, `logs`) garantissent que vos données survivent aux redémarrages.

---

## Comment ils fonctionnent ensemble

1.  **LibreChat (UI/API)** est le service central avec lequel vous interagissez.
2.  Il stocke les **données de chat/session dans MongoDB**.
3.  Il interroge **Meilisearch** pour les fonctionnalités de recherche textuelle.
4.  Pour le RAG (récupération de documents), LibreChat appelle **rag\_api**.
5.  L'**API RAG** récupère les embeddings vectoriels depuis **vectordb (Postgres + pgvector)**.
6.  Tout est persisté sur des volumes locaux, donc les données ne sont pas perdues lors du redémarrage des conteneurs.

---

✅ En bref :

* **MongoDB** → données de chat/utilisateur
* **Meilisearch** → recherche par mots-clés rapide
* **Postgres+pgvector** → embeddings vectoriels pour le RAG
* **API RAG** → couche d'augmentation par récupération
* **LibreChat** → l'application qui lie le tout

---

Souhaitez-vous que je vous montre également un **flux de type diagramme (textuel)** illustrant comment les requêtes traversent ces conteneurs (de vous → LibreChat → API RAG → Base de données vectorielle) ? Cela pourrait rendre les choses encore plus claires.