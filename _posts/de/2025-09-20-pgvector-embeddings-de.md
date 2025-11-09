---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: 'PGVector: Vektoreinbettungen in PostgreSQL'
translated: true
type: note
---

PGVector ist eine **PostgreSQL-Erweiterung**, die die Speicherung und Abfrage von *Vektor-Embeddings* (Zahlenarrays, oft mit 128–4096 Dimensionen) innerhalb einer Postgres-Datenbank ermöglicht.

Sie wird häufig in **KI- und Machine-Learning-Anwendungen** eingesetzt, bei denen Embeddings von Modellen wie OpenAI, Hugging Face oder anderen Embedding-Anbietern gespeichert und durchsucht werden müssen. Beispielsweise können Sie Dokumente, Code-Snippets oder Produktbeschreibungen in Vektoren umwandeln und dann mit PGVector die ähnlichsten zu einer Benutzeranfrage schnell finden.

### Wichtige Funktionen

* **Vektor-Datentyp**: Fügt einen `vector`-Spaltentyp zu Postgres-Tabellen hinzu.
* **Ähnlichkeitssuche**: Unterstützt Operationen wie Kosinus-Ähnlichkeit, euklidische Distanz oder inneres Produkt zum Vergleichen von Vektoren.
* **Indizes für Geschwindigkeit**: Bietet `ivfflat`- und `hnsw`-Indextypen für eine effiziente *annähernde nächste-Nachbar-Suche (ANN)*, die auch bei Millionen von Embeddings eine schnelle Abfrage ermöglicht.
* **SQL-Integration**: Da die Erweiterung innerhalb von Postgres läuft, können Sie Vektorsuche mit normalen SQL-Abfragen, Joins und Filtern kombinieren.

### Beispiel zur Verwendung

```sql
-- Tabelle mit Vektorspalte erstellen
CREATE TABLE items (
  id bigserial PRIMARY KEY,
  embedding vector(1536)  -- Dimension muss zu Ihrem Modell passen
);

-- Eine Zeile einfügen
INSERT INTO items (embedding) VALUES ('[0.25, 0.1, ...]');

-- Nach dem ähnlichsten Embedding suchen
SELECT id, embedding
FROM items
ORDER BY embedding <-> '[0.24, 0.11, ...]'
LIMIT 5;
```

Hier ist `<->` der Ähnlichkeitsoperator.

### Warum es wichtig ist

PGVector ermöglicht den Aufbau einer **kompletten Vektordatenbank direkt in Postgres**, anstatt eine separate, spezialisierte Vektor-DB (wie Pinecone, Weaviate oder Milvus) zu verwenden. Das ist attraktiv, wenn Sie Postgres bereits nutzen und alle Daten und Abfragen an einem Ort behalten möchten.

---

Möchten Sie, dass ich auch **PGVector vs. dedizierte Vektordatenbanken** (wie Pinecone oder Weaviate) vergleiche, damit Sie sehen können, wann Sie was verwenden sollten?