---
audio: false
generated: false
image: false
lang: hant
layout: post
title: 使用AI建構SQL查詢
translated: true
type: post
---

**資料庫架構 (PostgreSQL):**
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    date_of_birth DATE,
    gender VARCHAR(10),
    phone_number VARCHAR(20),
    address TEXT,
    city VARCHAR(100),
    state VARCHAR(100),
    country VARCHAR(100),
    zip_code VARCHAR(20),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE,
    last_login TIMESTAMP WITH TIME ZONE,
    is_active BOOLEAN DEFAULT TRUE,
    role VARCHAR(50),
    profile_picture_url VARCHAR(255),
    bio TEXT,
    failed_login_attempts INTEGER DEFAULT 0,
    account_balance NUMERIC(10, 2) DEFAULT 0.00
);
```

---

以上是 Postgre 資料庫，以下是表格定義。以下是自然語言查詢指示。

我要查詢一些用戶，其名字是 Andy，創建時間在上個月的某一天，且在 2025 年時年齡為 20 歲，並且最近一週有登入過，請給我查詢這些用戶的 SQL 語句。

---

**生成的 SQL 查詢：**
```sql
SELECT *
FROM users
WHERE first_name ILIKE 'andy'
  AND CAST(created_at AS DATE) BETWEEN
      (CURRENT_DATE - INTERVAL '1 MONTH' - INTERVAL '1 DAY')
      AND
      (CURRENT_DATE - INTERVAL '1 MONTH' + INTERVAL '1 DAY')
  AND EXTRACT(YEAR FROM AGE(date_of_birth)) = 20
  AND last_login >= CURRENT_TIMESTAMP - INTERVAL '7 DAYS';
```

---

以下是一個 PostgreSQL 表格定義，用於儲存用戶與類似 Grok 的 AI 系統的互動。該表格旨在追蹤對話，包括涉及的用戶、對話內容、時間戳記和相關元數據。

```sql
CREATE TABLE conversations (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    title VARCHAR(255),
    conversation_type VARCHAR(50) DEFAULT 'chat',
    started_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    ended_at TIMESTAMP WITH TIME ZONE,
    status VARCHAR(50) DEFAULT 'active',
    message_count INTEGER DEFAULT 0,
    last_message_at TIMESTAMP WITH TIME ZONE,
    is_archived BOOLEAN DEFAULT FALSE,
    ai_model_version VARCHAR(100),
    total_tokens_used INTEGER DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

### 說明：
- **id**：每個對話的唯一標識符。
- **user_id**：引用 `users` 表格，將對話與特定用戶連結。
- **title**：對話的可選標題（例如用戶自定義或自動生成的摘要）。
- **conversation_type**：指示對話類型（例如 'chat'、'query'、'voice'）。
- **started_at**：對話開始的時間戳記。
- **ended_at**：對話結束的時間戳記（如果進行中則為可空）。
- **status**：追蹤對話狀態（例如 'active'、'completed'、'paused'）。
- **message_count**：追蹤對話中交換的訊息數量。
- **last_message_at**：最新訊息的時間戳記。
- **is_archived**：布林值，表示對話是否已歸檔。
- **ai_model_version**：儲存使用的 AI 模型版本（例如 'Grok 3'）。
- **total_tokens_used**：追蹤對話的代幣使用量（對 API 計費或分析有用）。
- **created_at** 和 **updated_at**：對話記錄創建和最後更新的時間戳記。
- **FOREIGN KEY**：確保與 `users` 表格的參照完整性，並使用 `ON DELETE CASCADE` 在關聯用戶被刪除時刪除對話。

此表格設計靈活，可根據特定需求擴展，例如在單獨的 `messages` 表格中儲存個別訊息，或添加用於情感分析或對話標籤的欄位。請告訴我如果需要相關表格（例如用於訊息的表格）或與此表格互動的查詢！

---

為了實現一個前端，讓用戶可以使用自然語言查詢自己的對話（例如 "給我最新的 5 個對話" 或 "標題包含 java 字詞的對話"），您需要確保 SQL 查詢僅限於過濾到已驗證用戶的對話。這涉及將用戶身份（例如 `user_id`）納入查詢並將自然語言轉換為 SQL 條件。以下是針對 `conversations` 表格的提示和對應的 SQL 查詢，確保用戶只能訪問自己的數據。

### 關鍵考量
- **用戶驗證**：前端必須將已驗證的 `user_id` 傳遞給後端，以過濾對話。
- **自然語言解析**：自然語言輸入被解析以識別關鍵條件（例如 "最新 5" 或 "標題有 java 字詞"）。
- **安全性**：始終過濾 `user_id` 以防止用戶訪問他人的對話。
- **表格參考**：使用前面定義的 `conversations` 表格。

### 自然語言提示和 SQL 查詢

#### 提示 1："給我最新的 5 個對話"
**解析需求**：
- 過濾對話以符合已驗證用戶的 `user_id`。
- 按 `started_at`（或 `last_message_at` 以獲取最新）降序排序。
- 限制為 5 個結果。

**SQL 查詢**：
```sql
SELECT *
FROM conversations
WHERE user_id = :authenticated_user_id
ORDER BY started_at DESC
LIMIT 5;
```
- `:authenticated_user_id` 是登入用戶 ID 的占位符，安全地從前端/後端傳遞。
- `started_at DESC` 確保返回最新的對話。
- `LIMIT 5` 將輸出限制為 5 個對話。

#### 提示 2："標題包含 java 字詞的對話"
**解析需求**：
- 過濾對話以符合已驗證用戶的 `user_id`。
- 搜索標題中包含 "java" 的對話（不區分大小寫）。
- 在 PostgreSQL 中使用 `ILIKE` 進行部分、不區分大小寫的匹配。

**SQL 查詢**：
```sql
SELECT *
FROM conversations
WHERE user_id = :authenticated_user_id
  AND title ILIKE '%java%';
```
- `:authenticated_user_id` 確保僅查詢用戶的對話。
- `ILIKE '%java%'` 匹配包含 "java" 的標題（例如 "Java 小技巧"、"關於 Java 程式設計"）。

### 前端實現注意事項
1. **用戶驗證**：
   - 前端必須從驗證的會話（例如 JWT 令牌或會話）中獲取用戶的 ID，並將其傳遞給後端 API。
   - 後端應驗證 `user_id` 並在 `WHERE` 子句中使用它來過濾結果。

2. **自然語言處理**：
   - 使用簡單的規則基礎解析器或 AI 模型（如 Grok）來解析自然語言查詢並提取：
     - **意圖**：列出對話。
     - **篩選條件**：關鍵字（例如 "java"）、排序（例如 "最新"）或限制（例如 "5"）。
   - 例如，將 "最新 5" 映射到 `ORDER BY started_at DESC LIMIT 5`，將 "標題有 java 字詞" 映射到 `title ILIKE '%java%'`。

3. **API 設計**：
   - 創建一個端點（例如 `/api/conversations`），接受：
     - `user_id`：來自驗證的會話。
     - `query`：自然語言輸入或結構化參數（例如 `{ filter: "title contains java" }`）。
   - 後端將查詢轉換為 SQL，確保 `user_id` 始終包含在 `WHERE` 子句中。

4. **安全性**：
   - 不要允許用戶直接輸入 SQL 或修改 `user_id` 篩選條件。
   - 使用參數化查詢（例如 `:authenticated_user_id`）來防止 SQL 注入。
   - 驗證輸入以避免 `ILIKE` 搜索中的惡意模式。

5. **前端顯示**：
   - 返回字段如 `id`、`title`、`started_at`、`last_message_at` 和 `status` 以顯示對話列表。
   - 在 UI 中允許排序或篩選選項（例如下拉菜單用於 "最新" 或文本輸入用於標題搜索）。

### 示例工作流程
1. 用戶登入，前端獲取其 `user_id`（例如 `123`）。
2. 用戶在搜索欄中輸入 "給我最新的 5 個對話"。
3. 前端將請求發送到後端：`/api/conversations?user_id=123&query=latest 5`。
4. 後端解析查詢，生成 SQL：
   ```sql
   SELECT *
   FROM conversations
   WHERE user_id = 123
   ORDER BY started_at DESC
   LIMIT 5;
   ```
5. 後端以 JSON 格式返回結果，前端顯示對話。

### 其他說明
- 如果 `title` 為可空，請在第二個查詢中添加 `AND title IS NOT NULL` 以避免匹配空標題。
- 對於更複雜的查詢（例如 "上週關於 java 的對話"），合併條件：
  ```sql
  SELECT *
  FROM conversations
  WHERE user_id = :authenticated_user_id
    AND title ILIKE '%java%'
    AND started_at >= CURRENT_TIMESTAMP - INTERVAL '7 DAYS';
  ```
- 如果需要更先進的自然語言解析器，請考慮整合 AI 模型（例如通過 xAI 的 API 使用 Grok）將複雜查詢映射到 SQL。有關 API 詳細信息，請訪問 [xAI API](https://x.ai/api)。

請告訴我如果需要幫助前端代碼、後端 API 設置或其他查詢示例！