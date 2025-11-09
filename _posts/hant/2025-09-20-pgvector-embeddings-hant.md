---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: PGVector：PostgreSQL 中的向量嵌入技術
translated: true
type: note
---

PGVector 是一套 **PostgreSQL 擴充套件**，可支援在 Postgres 資料庫內儲存及查詢 *向量嵌入*（由 128–4096 維數字組成的陣列）。

這項技術常見於 **人工智慧與機器學習應用** 中，當您需要儲存並搜尋由 OpenAI、Hugging Face 或其他嵌入供應商模型所生成的嵌入時。舉例來說，您可以將文件、程式碼片段或產品描述轉換為向量，再透過 PGVector 快速找出與使用者查詢最相近的結果。

### 核心功能

* **向量資料類型**：為 Postgres 資料表新增 `vector` 欄位類型。
* **相似度搜尋**：支援餘弦相似度、歐幾里得距離或內積等向量比對運算。
* **高效能索引**：提供 `ivfflat` 與 `hnsw` 索引類型，實現高效的 *近似最近鄰 (ANN)* 搜尋，即使面對數百萬筆嵌入資料仍能快速檢索。
* **SQL 整合**：由於直接在 Postgres 內運行，您可將向量搜尋與標準 SQL 查詢、資料表連結及篩選條件結合使用。

### 使用範例

```sql
-- 建立含向量欄位的資料表
CREATE TABLE items (
  id bigserial PRIMARY KEY,
  embedding vector(1536)  -- 維度需與您的模型匹配
);

-- 插入資料列
INSERT INTO items (embedding) VALUES ('[0.25, 0.1, ...]');

-- 搜尋最相似的嵌入向量
SELECT id, embedding
FROM items
ORDER BY embedding <-> '[0.24, 0.11, ...]'
LIMIT 5;
```

此處的 `<-> 符號代表相似度運算子。

### 重要性說明

PGVector 讓您能 **直接在 Postgres 內建置完整的向量資料庫**，無需另尋專用向量資料庫（如 Pinecone、Weaviate 或 Milvus）。若您已在使用 Postgres 並希望集中管理所有資料與查詢，這將是極具吸引力的解決方案。

---

您是否需要進一步瞭解 **PGVector 與專用向量資料庫**（如 Pinecone 或 Weaviate）的比較，以便根據需求選擇合適方案？