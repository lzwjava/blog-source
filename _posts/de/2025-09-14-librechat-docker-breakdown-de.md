---
audio: false
date: 2025-09-14
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: LibreChat Docker Compose Dienstaufschlüsselung
translated: true
type: note
---

Was du eingefügt hast, ist ein `docker-compose.yaml`-Setup zum Ausführen von **LibreChat** zusammen mit seinen Abhängigkeiten. Lass es mich klar aufschlüsseln:

---

## Überblick

Das Setup definiert **6 Services (Container)**, die zusammenarbeiten:

1.  **LibreChat API/UI (`api`)**
2.  **MongoDB (`mongodb`)**
3.  **Meilisearch (`meilisearch`)**
4.  **Postgres mit pgvector (`vectordb`)**
5.  **RAG API (`rag_api`)**
6.  **Volumes für persistente Speicherung**

Diese sind alle über Docker Compose miteinander verbunden, sodass du alles mit einem einzigen `docker-compose up` starten kannst.

---

## Erklärungen der Services

### 1. LibreChat API (`api`)

*   **Container-Name:** `LibreChat`
*   **Image:** `ghcr.io/danny-avila/librechat-dev:latest` (der Dev-Build von LibreChat)
*   **Ports:** Macht `${PORT}` aus der `.env`-Datei für deinen Host-Rechner verfügbar.
*   **Abhängigkeiten:** Wartet auf `mongodb` und `rag_api`, bevor es startet.
*   **Umgebungsvariablen:**
    *   `MONGO_URI`: Connection String für MongoDB.
    *   `MEILI_HOST`: Verweist auf den Meilisearch-Service.
    *   `RAG_API_URL`: Verbindet sich mit dem lokalen RAG API-Container.
*   **Volumes:**
    *   Die `.env`-Datei wird in den Container eingebunden.
    *   `images`, `uploads` und `logs` werden lokal persistiert, damit sie nicht verloren gehen, wenn der Container neu startet.

👉 Dies ist die Haupt-App, mit der du interagierst (der LibreChat Web/API Service).

---

### 2. MongoDB (`mongodb`)

*   **Container-Name:** `chat-mongodb`
*   **Image:** `mongo` (offizielles MongoDB-Image).
*   **Zweck:** Speichert Chat-Daten, User-Sessions, Konfiguration etc.
*   **Befehl:** Führt `mongod --noauth` aus (keine Authentifizierung).
*   **Volumes:** `./data-node:/data/db`, damit deine Datenbank außerhalb des Containers bestehen bleibt.

---

### 3. Meilisearch (`meilisearch`)

*   **Container-Name:** `chat-meilisearch`
*   **Image:** `getmeili/meilisearch:v1.12.3`
*   **Zweck:** Bietet **schnelle Volltext-Suche** für LibreChat.
*   **Umgebungsvariablen:**
    *   `MEILI_NO_ANALYTICS=true` (Datenschutz).
    *   `MEILI_MASTER_KEY` wird aus der `.env`-Datei gezogen.
*   **Volumes:** `./meili_data_v1.12:/meili_data` für Persistenz.

---

### 4. Vektor-Datenbank (`vectordb`)

*   **Container-Name:** `vectordb`
*   **Image:** `pgvector/pgvector:0.8.0-pg15-trixie` (Postgres mit pgvector-Erweiterung).
*   **Zweck:** Speichert Embeddings für RAG (Retrieval Augmented Generation).
*   **Umgebung:**
    *   `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`.
*   **Volume:** `pgdata2:/var/lib/postgresql/data` für Persistenz.

---

### 5. RAG API (`rag_api`)

*   **Container-Name:** `rag_api`
*   **Image:** `ghcr.io/danny-avila/librechat-rag-api-dev-lite:latest`
*   **Zweck:** Verarbeitet RAG-Workflows – das Abrufen von Dokumenten und das Anreichern von Modellantworten mit externem Wissen.
*   **Umgebung:**
    *   `DB_HOST=vectordb` (verbindet sich mit der Postgres-Vektor-DB).
    *   `RAG_PORT` standardmäßig auf `8000`.
*   **Hängt ab von:** `vectordb`.
*   **Env-Datei:** Verwendet deine `.env`-Datei erneut.

---

### 6. Volumes

*   **`pgdata2`** → Persistente Daten für Postgres/pgvector.
*   Andere Volumes wie `./meili_data_v1.12`, `./data-node` und eingebundene Verzeichnisse (`images`, `uploads`, `logs`) stellen sicher, dass deine Daten Neustarts überstehen.

---

## Wie sie zusammenarbeiten

1.  **LibreChat (UI/API)** ist der zentrale Service, mit dem du interagierst.
2.  Er speichert **Chat-/Sitzungsdaten in MongoDB**.
3.  Er fragt **Meilisearch** für Textsuchfunktionen ab.
4.  Für RAG (Dokumentenabruf) ruft LibreChat die **rag\_api** auf.
5.  Die **RAG API** holt Vektor-Embeddings aus der **vectordb (Postgres + pgvector)**.
6.  Alles wird auf lokalen Volumes persistiert, sodass Daten bei Container-Neustarts nicht verloren gehen.

---

✅ Kurz gesagt:

*   **MongoDB** → Chat/User-Daten
*   **Meilisearch** → schnelle Schlüsselwortsuche
*   **Postgres+pgvector** → Vektor-Embeddings für RAG
*   **RAG API** → Retrieval-Augmentierungsschicht
*   **LibreChat** → die App, die alles zusammenhält

---

Möchtest du, dass ich dir auch einen **Diagramm-ähnlichen Fluss (in Textform)** zeige, wie sich Anfragen durch diese Container bewegen (von dir → LibreChat → RAG API → Vector DB)? Das könnte es noch klarer machen.