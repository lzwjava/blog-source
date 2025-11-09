---
audio: false
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: PostgreSQLにおけるベクター埋め込み
translated: true
type: note
---

PGVectorは、PostgreSQLデータベース内で**ベクトル埋め込み**（数値の配列、通常128～4096次元）の保存とクエリをサポートする**PostgreSQL拡張機能**です。

OpenAI、Hugging Face、その他の埋め込みプロバイダーによって生成された埋め込みを保存・検索する必要がある**AIおよび機械学習アプリケーション**で一般的に使用されます。例えば、ドキュメント、コードスニペット、商品説明をベクトルに埋め込み、PGVectorを使用してユーザークエリに最も類似したものを素早く見つけることができます。

### 主な機能

* **ベクトルデータ型**: Postgresテーブルに`vector`カラム型を追加します。
* **類似性検索**: コサイン類似性、ユークリッド距離、内積などの操作をサポートし、ベクトルを比較します。
* **高速化のためのインデックス**: 効率的な*近似最近傍探索（ANN）*を可能にする`ivfflat`および`hnsw`インデックスタイプを提供し、数百万の埋め込みがあっても高速な検索を実現します。
* **SQL統合**: Postgres内部で動作するため、ベクトル検索を通常のSQLクエリ、結合、フィルタと組み合わせることができます。

### 使用例

```sql
-- ベクトルカラムを持つテーブルを作成
CREATE TABLE items (
  id bigserial PRIMARY KEY,
  embedding vector(1536)  -- 次元は使用するモデルに合わせる
);

-- 行を挿入
INSERT INTO items (embedding) VALUES ('[0.25, 0.1, ...]');

-- 最も類似した埋め込みを検索
SELECT id, embedding
FROM items
ORDER BY embedding <-> '[0.24, 0.11, ...]'
LIMIT 5;
```

ここで`<->`は類似性演算子です。

### 重要性

PGVectorを使用すると、別途専門のベクトルDB（Pinecone、Weaviate、Milvusなど）を使用するのではなく、**Postgres内に完全なベクトルデータベースを構築**できます。これは、既にPostgresを使用しており、すべてのデータとクエリを一箇所に保持したい場合に魅力的です。

---

**PGVectorと専用ベクトルデータベース**（PineconeやWeaviateなど）の比較も行い、それぞれをいつ使用すべきかを確認してみませんか？