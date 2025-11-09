---
audio: false
date: 2025-09-14
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: LibreChat Docker Compose 服務詳解
translated: true
type: note
---

你貼上的是一個用於運行 **LibreChat** 及其依賴項的 `docker-compose.yaml` 設定。讓我清晰地拆解說明：

---

## 高層次概覽

這個設定定義了 **6 個協同工作的服務（容器）**：

1. **LibreChat API/UI (`api`)**
2. **MongoDB (`mongodb`)**
3. **Meilisearch (`meilisearch`)**
4. **帶有 pgvector 的 Postgres (`vectordb`)**
5. **RAG API (`rag_api`)**
6. **用於持久化儲存的 Volume**

這些服務透過 Docker Compose 連接在一起，因此你可以透過單一的 `docker-compose up` 指令啟動所有服務。

---

## 服務說明

### 1. LibreChat API (`api`)

* **容器名稱：** `LibreChat`
* **映像檔：** `ghcr.io/danny-avila/librechat-dev:latest` (LibreChat 的開發版本)
* **連接埠：** 將 `.env` 中的 `${PORT}` 暴露給你的主機。
* **依賴項：** 在啟動前等待 `mongodb` 和 `rag_api`。
* **環境變數：**

  * `MONGO_URI`: 連接到 MongoDB 的連接字串。
  * `MEILI_HOST`: 指向 Meilisearch 服務。
  * `RAG_API_URL`: 連接到本地的 RAG API 容器。
* **Volume：**

  * `.env` 檔案被掛載到容器內部。
  * `images`、`uploads` 和 `logs` 目錄在本地持久化，以便容器重啟時不會遺失資料。

👉 這是你與之互動的主要應用程式（LibreChat 網頁/API 服務）。

---

### 2. MongoDB (`mongodb`)

* **容器名稱：** `chat-mongodb`
* **映像檔：** `mongo` (官方 MongoDB 映像檔)。
* **用途：** 儲存聊天資料、使用者工作階段、設定等。
* **指令：** 執行 `mongod --noauth` (無身份驗證)。
* **Volume：** `./data-node:/data/db` 使你的資料庫在容器外部持久化。

---

### 3. Meilisearch (`meilisearch`)

* **容器名稱：** `chat-meilisearch`
* **映像檔：** `getmeili/meilisearch:v1.12.3`
* **用途：** 為 LibreChat 提供**快速的全文搜尋**功能。
* **環境變數：**

  * `MEILI_NO_ANALYTICS=true` (隱私)。
  * `MEILI_MASTER_KEY` 從 `.env` 檔案讀取。
* **Volume：** `./meili_data_v1.12:/meili_data` 用於持久化。

---

### 4. 向量資料庫 (`vectordb`)

* **容器名稱：** `vectordb`
* **映像檔：** `pgvector/pgvector:0.8.0-pg15-trixie` (帶有 pgvector 擴充功能的 Postgres)。
* **用途：** 為 RAG (Retrieval Augmented Generation) 儲存嵌入向量。
* **環境：**

  * `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`。
* **Volume：** `pgdata2:/var/lib/postgresql/data` 用於持久化。

---

### 5. RAG API (`rag_api`)

* **容器名稱：** `rag_api`
* **映像檔：** `ghcr.io/danny-avila/librechat-rag-api-dev-lite:latest`
* **用途：** 處理 RAG 工作流程 — 檢索文件並使用外部知識增強模型回應。
* **環境：**

  * `DB_HOST=vectordb` (連接到 Postgres 向量資料庫)。
  * `RAG_PORT` 預設為 `8000`。
* **依賴於：** `vectordb`。
* **環境檔案：** 重複使用你的 `.env`。

---

### 6. Volume

* **`pgdata2`** → 用於 Postgres/pgvector 的持久化資料。
* 其他 Volume 如 `./meili_data_v1.12`、`./data-node` 以及掛載的目錄 (`images`、`uploads`、`logs`) 確保你的資料在重啟後得以保留。

---

## 它們如何協同工作

1. **LibreChat (UI/API)** 是你與之互動的核心服務。
2. 它將**聊天/工作階段資料儲存在 MongoDB** 中。
3. 它查詢 **Meilisearch** 以獲得文字搜尋功能。
4. 對於 RAG (文件檢索)，LibreChat 呼叫 **rag\_api**。
5. **RAG API** 從 **vectordb (Postgres + pgvector)** 獲取向量嵌入。
6. 所有資料都持久化在本地 Volume 上，因此容器重啟時資料不會遺失。

---

✅ 簡而言之：

* **MongoDB** → 聊天/使用者資料
* **Meilisearch** → 快速關鍵字搜尋
* **Postgres+pgvector** → 用於 RAG 的向量嵌入
* **RAG API** → 檢索增強層
* **LibreChat** → 將所有組件整合在一起的應用程式

---

你是否還需要我展示一個**圖表式流程（文字版）**來說明請求如何透過這些容器流動（從你 → LibreChat → RAG API → 向量資料庫）？這可能會讓整個流程更加清晰。