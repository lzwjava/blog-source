---
audio: false
generated: true
lang: hant
layout: post
title: 構建精準安全的自然語言至SQL系統
translated: true
type: note
---

### 建構自然語言轉 SQL 系統時的關鍵重點領域

建構自然語言轉 SQL（NL-to-SQL）系統涉及將日常語言的使用者查詢轉換為可執行的 SQL 語句，通常使用 AI 模型如 LLM（例如 GPT 變體或 Hugging Face 的專用模型）。根據您的 PostgreSQL 架構和範例查詢，以下是需要關注的主要領域：

#### 1. **準確性與架構理解**
   - **架構認知**：始終在 AI 提示中提供完整的資料庫架構（資料表、欄位、資料類型、關聯）。這有助於模型生成正確的 SQL。在您的情況中，請特別強調如 `first_name`、`created_at`、`date_of_birth` 和 `last_login` 等欄位，以避免幻覺（例如虛構不存在的欄位）。
   - **處理模糊性**：自然語言具有模糊性——例如「上個月左右的那天」可能意味著 ±1 天，但需透過提示來澄清模糊術語的解釋（例如將「最近一週」解釋為 7 天）。在提示中使用範例來引導解釋。
   - **資料類型與函數**：專注於 PostgreSQL 專用語法，例如對日期使用 `AGE()`、對不區分大小寫的字串使用 `ILIKE`，以及正確的類型轉換（例如在您的範例中使用 `CAST(created_at AS DATE)`）。針對 SQL 方言差異進行模型訓練或微調。
   - **邊緣案例**：處理複雜查詢，如聯結（若涉及多個資料表）、聚合（例如 COUNT、SUM）或子查詢。測試涉及敏感欄位（如 `password_hash` 或 `account_balance`）的查詢。

#### 2. **效能與優化**
   - 生成高效的 SQL：鼓勵模型使用索引（例如在 `created_at` 或 `first_name` 上）、限制結果（預設添加 `LIMIT`）並避免全表掃描。
   - 可擴展性：對於大型資料集，整合查詢優化工具或根據執行計劃驗證生成的 SQL。

#### 3. **錯誤處理與驗證**
   - 在執行前解析並驗證生成的 SQL（例如使用 Python 中的 `sqlparse` 等 SQL 解析庫）。
   - 提供後備回應：若查詢不明確，提示使用者澄清而非生成無效的 SQL。

#### 4. **安全性與防護**
   - **預防 SQL 注入**：風險來自執行生成的 SQL。切勿將使用者輸入直接串接到 SQL 字串中。取而代之的是：
     - 在執行時使用**參數化查詢**或預備語句（例如在 Python 中使用 `psycopg2`：`cursor.execute("SELECT * FROM users WHERE first_name = %s", (name,))`）。
     - 指示 AI 生成帶有佔位符的 SQL（例如 `WHERE first_name ILIKE %s`）並單獨綁定值。
     - 清理自然語言輸入：預處理使用者查詢以移除惡意模式（例如使用正則表達式檢測 SQL 關鍵字如 "DROP" 或 ";"）。
     - 限制為唯讀：限制 AI 僅生成 SELECT 查詢——透過提示指令（如「僅生成 SELECT 語句；不修改資料」）來封鎖 DDL（例如 CREATE/DROP）或 DML（例如 INSERT/UPDATE）。
   - **控制資料存取**：
     - **列層級安全性 (RLS)**：在 PostgreSQL 中，對資料表啟用 RLS 政策（例如 `ALTER TABLE users ENABLE ROW LEVEL SECURITY; CREATE POLICY user_policy ON users USING (role = current_user);`）。這確保查詢僅傳回使用者有權存取的列。
     - **檢視與角色**：建立受限檢視（例如 `CREATE VIEW safe_users AS SELECT id, username, first_name FROM users;`）並透過資料庫角色授予存取權限。AI 應查詢檢視而非基礎資料表。
     - **API 層**：將系統封裝在 API 中（例如使用 FastAPI），該 API 對使用者進行身份驗證並應用存取控制（例如使用 JWT 令牌來決定使用者角色）。
     - **沙箱執行**：在唯讀複本資料庫或容器化環境（例如 Docker）中執行查詢，以與生產資料隔離。
     - **審計日誌**：記錄所有生成的 SQL 和執行情況以進行監控。
   - **資料隱私**：透過在提示中黑名單敏感欄位來避免暴露：「除非明確需要且授權，否則不要選擇敏感欄位如 password_hash、email」。
   - **速率限制與配額**：透過限制每個使用者/工作階段的查詢來防止濫用。

#### 5. **用於受控轉換的提示工程**
   - NL-to-SQL 的品質在很大程度上取決於您如何指示 AI。使用包含以下元素的結構化提示：
     - **系統提示範本**：
       ```
       您是一位 PostgreSQL 的專家 SQL 生成器。根據以下架構和自然語言查詢，生成安全、準確的 SELECT 查詢。

       架構：
       [在此插入完整架構，例如 CREATE TABLE users (...)]

       規則：
       - 僅生成 SELECT 語句。不生成 INSERT、UPDATE、DELETE 或 DDL。
       - 對使用者提供的值使用參數化佔位符（例如 %s）以防止注入。
       - 使用 PostgreSQL 函數如 AGE()、CURRENT_DATE、INTERVAL 處理日期。
       - 對於模糊術語（例如「上個月左右」），解釋為 [特定規則，例如上個月同一天的 ±1 天]。
       - 除非指定，否則將結果限制為 100 列。
       - 若查詢涉及年齡，計算截至當前年份或指定年份（例如 EXTRACT(YEAR FROM AGE(CURRENT_DATE, date_of_birth)) = 20）。
       - 不要選擇敏感欄位如 password_hash、email。
       - 若不明確，回應「請澄清：[問題]」。

       使用者查詢：[自然語言查詢]
       ```
     - **提示中的範例**：包含 2-3 個範例，如您提供的查詢和生成的 SQL，以引導模型。
     - **思維鏈**：指示模型逐步推理：「首先，識別關鍵過濾條件。其次，對應到欄位。第三，建立 WHERE 子句。」
     - **微調**：若使用自訂模型，可在 Spider 或 WikiSQL 等資料集上進行微調，並增補您架構特定的範例。
     - **測試**：使用如執行準確度（是否無錯誤運行？）和語義匹配（是否返回預期結果？）等指標進行評估。

#### 對您範例查詢的潛在改進
雖然這不是主要問題，但您生成的 SQL 有一些優點，但可以更安全/更精確：
- 使用參數：更改為 `WHERE first_name ILIKE %s` 並綁定 'andy'。
- 年齡「截至 2025 年」：使用 `EXTRACT(YEAR FROM AGE('2025-12-31'::date, date_of_birth)) = 20` 以固定到特定年末。
- 添加 `ORDER BY last_login DESC LIMIT 10;` 以確保安全。

安全地實現此功能需要後端層（例如不直接從 AI 輸出執行 SQL）。從使用 LLM 庫（例如用於 NL-to-SQL 鏈的 LangChain）的腳本開始小規模實施。

若您需要程式碼範例或特定部分的協助（例如 Python 實現），請提供更多細節！

**參考資料**  
[PostgreSQL 文件：列層級安全性](https://www.postgresql.org/docs/current/ddl-rowsecurity.html)  
[LangChain NL-to-SQL 教程](https://python.langchain.com/docs/tutorials/sql_qa/)  
[在 Python 中預防 SQL 注入](https://realpython.com/prevent-python-sql-injection/)