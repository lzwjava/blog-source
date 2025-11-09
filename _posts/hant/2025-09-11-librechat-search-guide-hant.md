---
audio: false
date: 2025-09-11
generated: true
image: false
lang: hant
layout: post
model: mistralai/mistral-medium-3.1
title: LibreChat 搜尋功能指南
translated: true
type: note
---

以下是 **LibreChat v0.8.0-rc3** 中**搜尋功能**的運作方式（包含對話搜尋及其與分支功能的差異）：

---

### **1. 在 LibreChat 中進行搜尋**
LibreChat 提供**兩種主要搜尋方式**：
#### **A. 全域搜尋（跨所有對話）**
- **位置**：側邊欄頂部的搜尋列。
- **搜尋範圍**：
  - 對話**標題**（自動生成或自訂）。
  - **訊息內容**（你的提示詞 + AI 回覆）。
  - **元數據**（例如：使用的模型、時間戳）。
- **運作方式**：
  - 使用 **MongoDB/PostgreSQL 全文搜尋**（取決於你的後端）。
  - 返回匹配的對話/訊息列表並顯示**內容片段**。
  - 點擊結果會跳轉至該對話/訊息。

#### **B. 對話內搜尋（Ctrl+F 替代方案）**
- **位置**：在已開啟的聊天視窗內（部分版本提供**放大鏡圖示**或 `Ctrl+F` 快捷鍵）。
- **搜尋範圍**：
  - 僅限**當前對話的訊息**。
  - 在聊天視窗中高亮顯示匹配內容。

---

### **2. 搜尋與分支功能的差異**

| 功能               | **搜尋**                          | **分支**                          |
|-----------------------|-------------------------------------|--------------------------------------|
| **目的**           | 尋找過往訊息/對話。   | 從某個時間點建立替代對話路徑。|
| **輸出**            | 匹配結果列表。                    | 新增分支對話。          |
| **使用情境**          | 「我之前在哪裡問過 React hooks？」| 「讓我們嘗試不同的除錯方法。」|
| **持久性**       | 暫時性（UI 篩選）。              | 永久性（資料庫中新增對話）。  |

---
### **3. 技術細節（適用於自架使用者）**
#### **後端（資料庫搜尋）**
- **MongoDB**：
  - 對 `messages.content` 和 `conversations.title` 使用 `$text` 搜尋。
  - 需要[文字索引](https://www.mongodb.com/docs/manual/core/index-text/)（LibreChat 會自動設定）。
  - 範例查詢：
    ```javascript
    db.messages.find({ $text: { $search: "React hooks" } })
    ```
- **PostgreSQL**：
  - 使用 `tsvector` 全文搜尋。
  - 範例：
    ```sql
    SELECT * FROM messages
    WHERE to_tsvector('english', content) @@ to_tsquery('React & hooks');
    ```

#### **前端（UI 搜尋）**
- 基於 **React 狀態** + 防抖動的後端 API 呼叫。
- 結果以下拉選單/列表形式呈現（類似 Slack 或 Discord 的搜尋介面）。

---
### **4. 限制與解決方案**
#### **已知問題**
- **不支援模糊搜尋**：拼寫錯誤可能導致遺漏結果（嚴格關鍵字匹配）。
- **不支援正則表達式/語法**：UI 中暫無法使用 `AND/OR` 運算子。
- **大型資料庫速度緩慢**：當訊息數量超過 10,000+ 時，全文搜尋可能延遲。

#### **解決方案**
- **使用關鍵字**：搜尋獨特詞彙（例如：用 `"error: ENOENT"` 取代 `"help"`）。
- **按模型篩選**：部分版本支援按 AI 模型篩選搜尋結果（例如：僅顯示 GPT-4 對話）。
- **匯出並使用 grep**：適用於進階使用者：
  ```bash
  mongodump --db librechat --collection messages --query '{"userId": "YOUR_ID"}' --out=- | jq '.' | grep "React"
  ```

---
### **5. 與 ChatGPT 搜尋功能的比較**

| 功能               | LibreChat                          | ChatGPT（網頁版）                     |
|-----------------------|------------------------------------|-----------------------------------|
| **範圍**             | 所有對話 + 訊息。      | 僅限當前聊天記錄。        |
| **運算子**         | 基礎（僅關鍵字）。               | 支援 `AND`、`OR`、引號。     |
| **速度**             | 取決於資料庫（可能較慢）。      | 經過優化（對近期聊天更快）。|
| **UI**                | 側邊欄 + 對話內搜尋。                  | 僅頂部搜尋列。                     |
| **自架支援**       | 是（可控制索引）。         | 否（封閉系統）。               |

---
### **6. 如何改善 LibreChat 的搜尋功能**
#### **對於使用者**
- **使用描述性標題**：重新命名對話（例如：用「Debugging Python Async 2024-05」取代「New Chat」）。
- **標記重要訊息**：部分版本支援釘選重要訊息。

#### **對於開發者/自架使用者**
- **為索引添加權重**：在 MongoDB 中優先搜尋 `title` 而非 `content`：
  ```javascript
  db.conversations.createIndex(
    { title: "text", "messages.content": "text" },
    { weights: { title: 10, "messages.content": 1 } }
  );
  ```
- **整合 Meilisearch/Typesense**：實現更快速的模糊搜尋（已有社群外掛）。
- **啟用分頁功能**：處理大量結果集（歡迎提交 PR！）。

---
### **7. 範例工作流程**
1. **尋找過往除錯記錄**：
   - 搜尋 `"TypeError: cannot read property"` → LibreChat 顯示所有包含該錯誤的對話。
   - 點擊結果 → 跳轉至確切訊息。

2. **從解決方案建立分支**：
   - 在找到的對話中，於 AI 建議修復的訊息處建立分支。
   - 在分支中測試新方法，同時保留原始對話。

---
### **8. 未來計劃（後續版本可能實現）**
- **語義搜尋**：使用嵌入模型（例如：透過 `sentence-transformers`）尋找相關內容。
- **儲存搜尋**：為常用查詢建立書籤（例如：「所有 Python 錯誤」）。
- **跨對話洞察**：「顯示所有我詢問 Docker 網絡的記錄」。

---
### **需要更多協助？**
- **搜尋功能無法運作？**
  檢查資料庫日誌中的索引錯誤，或執行：
  ```bash
  # 適用於 MongoDB
  db.messages.getIndexes();
  db.conversations.getIndexes();
  ```
- **想要貢獻程式碼？**
  搜尋邏輯位於：
  - 後端：[`src/server/db`](https://github.com/danny-avila/LibreChat/tree/dev/src/server/db)
  - 前端：[`src/components/Chat/Sidebar`](https://github.com/danny-avila/LibreChat/tree/dev/src/components/Chat/Sidebar)