---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: PGVector : Intégration de Vecteurs dans PostgreSQL
translated: true
type: note
---

PGVector est une **extension PostgreSQL** qui ajoute la prise en charge du stockage et de l'interrogation *d'embeddings vectoriels* (tableaux de nombres, souvent de 128 à 4096 dimensions) dans une base de données Postgres.

Elle est couramment utilisée dans **les applications d'IA et de machine learning** où vous devez stocker et rechercher des embeddings générés par des modèles comme OpenAI, Hugging Face, ou d'autres fournisseurs d'embeddings. Par exemple, vous pouvez transformer des documents, des extraits de code ou des descriptions de produits en vecteurs, puis utiliser PGVector pour trouver rapidement les plus similaires à une requête utilisateur.

### Fonctionnalités Clés

* **Type de données vectoriel** : Ajoute un type de colonne `vector` aux tables Postgres.
* **Recherche de similarité** : Prend en charge des opérations comme la similarité cosinus, la distance euclidienne ou le produit scalaire pour comparer les vecteurs.
* **Indexes pour la vitesse** : Fournit les types d'index `ivfflat` et `hnsw` pour une recherche *approximative des plus proches voisins (ANN)* efficace, permettant une récupération rapide même avec des millions d'embeddings.
* **Intégration SQL** : Comme elle s'exécute dans Postgres, vous pouvez combiner la recherche vectorielle avec des requêtes SQL normales, des jointures et des filtres.

### Exemple d'Utilisation

```sql
-- Créer une table avec une colonne vectorielle
CREATE TABLE items (
  id bigserial PRIMARY KEY,
  embedding vector(1536)  -- la dimension doit correspondre à votre modèle
);

-- Insérer une ligne
INSERT INTO items (embedding) VALUES ('[0.25, 0.1, ...]');

-- Rechercher l'embedding le plus similaire
SELECT id, embedding
FROM items
ORDER BY embedding <-> '[0.24, 0.11, ...]'
LIMIT 5;
```

Ici, `<->` est l'opérateur de similarité.

### Pourquoi C'est Important

PGVector vous permet de construire **une base de données vectorielle entière directement dans Postgres**, plutôt que d'utiliser une base de données vectorielle spécialisée distincte (comme Pinecone, Weaviate ou Milvus). C'est intéressant si vous utilisez déjà Postgres et que vous souhaitez garder toutes les données et requêtes au même endroit.

---

Souhaitez-vous que je compare également **PGVector vs les bases de données vectorielles dédiées** (comme Pinecone ou Weaviate) afin que vous puissiez voir quand utiliser laquelle ?