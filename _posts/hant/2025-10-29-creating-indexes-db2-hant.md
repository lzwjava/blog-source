---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 在 IBM DB2 中建立索引
translated: true
type: note
---

### 在 IBM DB2 中建立索引

IBM DB2 支援透過索引來最佳化查詢效能，實現更快速的資料擷取。索引可以建立在資料表的一個或多個欄位上。以下我將介紹基礎知識，包括唯一索引與多欄位（複合）索引。請注意，「聯合索引」並非 DB2 文件中的標準術語——它可能指複合索引（涵蓋多個鍵值）或是對查詢中聯合操作的誤解。若您有其他意圖，請提供更多細節！

#### 基礎索引建立
使用 `CREATE INDEX` 語句在單一欄位上建立簡單索引。這能加速對該欄位的搜尋、排序及聯結操作。

**語法：**
```sql
CREATE INDEX index_name
ON table_name (column_name [ASC | DESC]);
```

**範例：**
```sql
CREATE INDEX idx_employee_id
ON employees (employee_id ASC);
```

- `ASC` 表示遞增排序（預設值）；使用 `DESC` 則為遞減排序。
- 索引預設為非唯一，允許重複值。

#### 唯一索引（強制唯一鍵）
唯一索引能確保索引欄位中不出現重複值，類似於唯一約束。當您定義主鍵或唯一約束時，DB2 會自動建立唯一索引。

**語法：**
```sql
CREATE UNIQUE INDEX index_name
ON table_name (column_name [ASC | DESC]);
```

**範例：**
```sql
CREATE UNIQUE INDEX uidx_email
ON users (email ASC);
```

- 此操作能防止插入重複的電子郵件。
- 若需部分唯一性（例如忽略 NULL 值），可加入 `WHERE NOT NULL`：  
  ```sql
  CREATE UNIQUE WHERE NOT NULL INDEX uidx_email
  ON users (email ASC);
  ```
- 您可包含非鍵值欄位以擴充查詢涵蓋範圍：  
  ```sql
  CREATE UNIQUE INDEX uidx_email
  ON users (email ASC) INCLUDE (first_name, last_name);
  ```

#### 複合索引（多個鍵值，例如兩個或更多欄位）
複合（或多欄位）索引涵蓋多個鍵值，適用於需根據欄位組合進行篩選或聯結的查詢。欄位順序至關重要——應將選擇性最高的欄位置於首位。

**語法：**
```sql
CREATE INDEX index_name
ON table_name (column1 [ASC | DESC], column2 [ASC | DESC], ...);
```

**範例（雙鍵值）：**
```sql
CREATE INDEX idx_order_date_customer
ON orders (order_date ASC, customer_id DESC);
```

- 此索引可最佳化類似 `SELECT * FROM orders WHERE order_date > '2023-01-01' AND customer_id = 123;` 的查詢。
- 若需唯一複合索引：請加入 `UNIQUE`（例如 `CREATE UNIQUE INDEX ...`）。

#### 額外提示
- **驗證索引：** 使用 `SELECT * FROM SYSCAT.INDEXES WHERE TABSCHEMA = 'YOUR_SCHEMA' AND TABNAME = 'YOUR_TABLE';`。
- **刪除索引：** `DROP INDEX index_name;`。
- 索引會佔用儲存空間並減慢插入/更新操作——請審慎使用。
- 若需分區資料表或進階選項（例如叢集索引），請參閱 DB2 文件。

[Db2 CREATE INDEX 語句](https://www.ibm.com/docs/en/db2-for-zos/12.0.0?topic=statements-create-index)  
[Db2 唯一索引](https://www.ibm.com/docs/en/db2-for-zos/12.0.0?topic=attributes-unique-indexes)  
[Db2 複合索引範例](https://stackoverflow.com/questions/21597015/composite-index-creation-in-db2)  
[Db2 唯一索引教學](https://www.db2tutorial.com/db2-index/db2-unique-index/)