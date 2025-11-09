---
audio: false
date: 2025-09-14
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: LibreChat Docker Compose サービス詳細
translated: true
type: note
---

あなたが貼り付けたのは、**LibreChat** とその依存関係を実行するための `docker-compose.yaml` 設定です。明確に分解してみましょう：

---

## 全体像

この設定は、連携して動作する**6つのサービス（コンテナ）**を定義しています：

1. **LibreChat API/UI (`api`)**
2. **MongoDB (`mongodb`)**
3. **Meilisearch (`meilisearch`)**
4. **pgvector を搭載した Postgres (`vectordb`)**
5. **RAG API (`rag_api`)**
6. **永続ストレージのためのボリューム**

これらはすべて Docker Compose を使用して接続されているため、単一の `docker-compose up` コマンドですべてを起動できます。

---

## サービスの説明

### 1. LibreChat API (`api`)

* **コンテナ名:** `LibreChat`
* **イメージ:** `ghcr.io/danny-avila/librechat-dev:latest` (LibreChat の開発ビルド)
* **ポート:** `.env` の `${PORT}` をホストマシンに公開します。
* **依存関係:** 起動前に `mongodb` と `rag_api` を待機します。
* **環境変数:**

  * `MONGO_URI`: MongoDB への接続文字列。
  * `MEILI_HOST`: Meilisearch サービスを指します。
  * `RAG_API_URL`: ローカルの RAG API コンテナに接続します。
* **ボリューム:**

  * `.env` ファイルがコンテナ内にマウントされます。
  * `images`、`uploads`、`logs` はローカルに永続化され、コンテナが再起動しても失われません。

👉 これがあなたが対話するメインのアプリ（LibreChat の Web/API サービス）です。

---

### 2. MongoDB (`mongodb`)

* **コンテナ名:** `chat-mongodb`
* **イメージ:** `mongo` (公式 MongoDB イメージ)
* **目的:** チャットデータ、ユーザーセッション、設定などを保存します。
* **コマンド:** `mongod --noauth` を実行（認証なし）。
* **ボリューム:** `./data-node:/data/db` により、データベースがコンテナ外で永続化されます。

---

### 3. Meilisearch (`meilisearch`)

* **コンテナ名:** `chat-meilisearch`
* **イメージ:** `getmeili/meilisearch:v1.12.3`
* **目的:** LibreChat に**高速な全文検索**機能を提供します。
* **環境変数:**

  * `MEILI_NO_ANALYTICS=true` (プライバシー設定)。
  * `MEILI_MASTER_KEY` は `.env` から取得されます。
* **ボリューム:** `./meili_data_v1.12:/meili_data` で永続化されます。

---

### 4. ベクトルデータベース (`vectordb`)

* **コンテナ名:** `vectordb`
* **イメージ:** `pgvector/pgvector:0.8.0-pg15-trixie` (pgvector 拡張を搭載した Postgres)
* **目的:** RAG (Retrieval Augmented Generation) のための埋め込み（embeddings）を保存します。
* **環境:**

  * `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`。
* **ボリューム:** `pgdata2:/var/lib/postgresql/data` で永続化されます。

---

### 5. RAG API (`rag_api`)

* **コンテナ名:** `rag_api`
* **イメージ:** `ghcr.io/danny-avila/librechat-rag-api-dev-lite:latest`
* **目的:** RAG ワークフローを処理します — ドキュメントの取得と、外部知識を用いたモデル応答の拡張を行います。
* **環境:**

  * `DB_HOST=vectordb` (Postgres ベクトル DB に接続)。
  * `RAG_PORT` はデフォルトで `8000`。
* **依存関係:** `vectordb`。
* **環境ファイル:** あなたの `.env` を再利用します。

---

### 6. ボリューム

* **`pgdata2`** → Postgres/pgvector の永続データ用。
* `./meili_data_v1.12`、`./data-node` などの他のボリュームや、マウントされたディレクトリ (`images`, `uploads`, `logs`) は、データが再起動後も保持されることを保証します。

---

## 連携の仕組み

1.  **LibreChat (UI/API)** は、あなたが対話する中心的なサービスです。
2.  これは**チャット/セッションデータを MongoDB** に保存します。
3.  テキスト検索機能のために **Meilisearch** にクエリを実行します。
4.  RAG（ドキュメント検索）の場合、LibreChat は **rag\_api** を呼び出します。
5.  **RAG API** は、**vectordb (Postgres + pgvector)** からベクトルの埋め込みを取得します。
6.  すべてがローカルボリューム上で永続化されるため、コンテナが再起動してもデータは失われません。

---

✅ 要約すると：

*   **MongoDB** → チャット/ユーザーデータ
*   **Meilisearch** → 高速なキーワード検索
*   **Postgres+pgvector** → RAG のためのベクトルの埋め込み
*   **RAG API** → 検索拡張レイヤー
*   **LibreChat** → すべてを統合するアプリ

---

これらのコンテナ間でリクエストがどのように流れるかを**図式的なフロー（テキスト）**でもお見せしましょうか？そうすればさらに明確になるかもしれません。