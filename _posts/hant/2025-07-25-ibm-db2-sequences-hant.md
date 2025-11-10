---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast:free
title: IBM DB2 序列使用指南
translated: true
type: note
---

### IBM DB2 序列使用與 NEXT VALUE FOR

在 IBM DB2 中，`NEXT VALUE FOR` 用於從序列中擷取下一個值，該序列會產生唯一且遞增的數字。序列適用於生成主鍵或其他唯一識別符。

#### 範例：建立與使用序列
1. **建立序列**（請在您的 DB2 環境中執行一次）：
   ```sql
   CREATE SEQUENCE my_sequence
   START WITH 1
   INCREMENT BY 1
   NO CYCLE;
   ```
   - 這會建立一個名為 `my_sequence` 的序列，從 1 開始，每次遞增 1。

2. **在 INSERT 語句中使用序列**以獲取下一個值：
   ```sql
   INSERT INTO employees (id, name, department)
   VALUES (NEXT VALUE FOR my_sequence, 'Alice Johnson', 'Engineering');
   ```
   - 這會插入一筆新資料列，其中 `id` 為序列的下一個值（例如，第一次使用時為 1，下一次為 2，依此類推）。

#### 關鍵注意事項
- 您也可以在 SELECT 查詢中使用它：`SELECT NEXT VALUE FOR my_sequence FROM SYSIBM.SYSDUMMY1;`
- 序列與資料表是分開的，如果需要，可以在多個資料表之間共享。
- 如需更多詳細資訊，請參閱 IBM DB2 關於序列的文件。如果您需要其他序列函數（例如 `PREVIOUS VALUE FOR`）的範例，請告訴我！