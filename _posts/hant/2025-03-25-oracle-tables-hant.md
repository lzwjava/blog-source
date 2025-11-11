---
audio: false
generated: true
lang: hant
layout: post
title: 識別 Oracle 資料庫中具資料的表格
translated: true
type: note
---

在 Oracle 資料庫中，若您正在探索結構描述並發現點擊某些資料表時顯示「空白」（例如透過 SQL Developer 或 Toad 等圖形化工具），這並不必然表示它們沒有資料。可能原因包括：權限設定、篩選條件，或您只是查看錯誤的資料表。要系統性地找出結構描述中包含資料的資料表，您可以查詢資料庫中繼資料或直接檢查資料表。具體方法如下：

#### 1. **檢查您的權限**
   - 若您看到空白資料表，可能是缺乏檢視資料的權限。請確保您對結構描述中的資料表擁有 `SELECT` 權限。
   - 執行以下指令檢查特定資料表的權限：
     ```sql
     SELECT privilege
     FROM dba_tab_privs
     WHERE grantee = UPPER('your_username')
     AND table_name = UPPER('table_name');
     ```
     請相應替換 `'your_username'` 和 `'table_name'`。若未顯示任何結果，請向結構描述擁有者或 DBA 申請存取權限。

#### 2. **查詢資料表的列數**
   - Oracle 會在 `USER_TABLES`、`ALL_TABLES` 或 `DBA_TABLES` 視圖中維護資料表的統計資訊（包括列數統計，具體取決於您的存取層級）。
   - 查看當前結構描述中包含資料的資料表：
     ```sql
     SELECT table_name, num_rows
     FROM user_tables
     WHERE num_rows > 0
     ORDER BY num_rows DESC;
     ```
     - `USER_TABLES`：顯示當前使用者擁有的資料表。
     - `NUM_ROWS`：近似列數（基於最後統計資料更新）。

   - 若您有權存取其他結構描述（例如透過 `ALL_TABLES`）：
     ```sql
     SELECT owner, table_name, num_rows
     FROM all_tables
     WHERE num_rows > 0
     AND owner = UPPER('schema_name')
     ORDER BY num_rows DESC;
     ```
     將 `'schema_name'` 替換為您要調查的結構描述名稱。

   **注意**：若統計資料未及時更新，`NUM_ROWS` 可能已過時。請參閱步驟 5 更新統計資料。

#### 3. **手動檢查特定資料表**
   - 若您懷疑 `NUM_ROWS` 不可靠或需要驗證，可對個別資料表執行 `COUNT(*)`：
     ```sql
     SELECT table_name
     FROM user_tables;
     ```
     此指令會列出結構描述中所有資料表。接著對每個資料表執行：
     ```sql
     SELECT COUNT(*) FROM table_name;
     ```
     若計數結果大於 0，表示該資料表包含資料。請注意：對大型資料表執行 `COUNT(*)` 可能耗時較長。

#### 4. **使用指令碼自動化檢查**
   - 為避免手動查詢每個資料表，可使用 PL/SQL 指令碼檢查結構描述中所有資料表的列數：
     ```sql
     BEGIN
         FOR t IN (SELECT table_name FROM user_tables)
         LOOP
             EXECUTE IMMEDIATE 'SELECT COUNT(*) FROM ' || t.table_name INTO v_count;
             IF v_count > 0 THEN
                 DBMS_OUTPUT.PUT_LINE(t.table_name || ' 包含 ' || v_count || ' 列資料');
             END IF;
         END LOOP;
     EXCEPTION
         WHEN OTHERS THEN
             DBMS_OUTPUT.PUT_LINE('資料表 ' || t.table_name || ' 檢查錯誤: ' || SQLERRM);
     END;
     /
     ```
     - 請在工具中啟用輸出功能（例如在 SQL*Plus 或 SQL Developer 中執行 `SET SERVEROUTPUT ON`）。
     - 此指令碼僅輸出包含資料的資料表。若需檢查其他結構描述，請將 `user_tables` 調整為 `all_tables` 並加入 `owner` 篩選條件。

#### 5. **更新資料表統計資料（如需要）**
   - 若 `USER_TABLES` 或 `ALL_TABLES` 中的 `NUM_ROWS` 顯示為 0 或數值不準確，可能是統計資料過時。更新方式：
     ```sql
     EXEC DBMS_STATS.GATHER_SCHEMA_STATS(ownname => 'schema_name');
     ```
     將 `'schema_name'` 替換為結構描述名稱（若為自身結構描述請使用您的使用者名稱）。然後重新執行步驟 2 的 `USER_TABLES` 查詢。

#### 6. **檢查分割區資料表**
   - 若結構描述使用分割區資料表，資料可能分散於多個分割區，簡單查詢可能無法反映實際情況。檢查分割區：
     ```sql
     SELECT table_name, partition_name, num_rows
     FROM user_tab_partitions
     WHERE num_rows > 0
     ORDER BY table_name, partition_name;
     ```
     此查詢會顯示哪些分割區包含資料。

#### 7. **圖形化工具使用技巧（例如 SQL Developer）**
   - 若您使用 Oracle SQL Developer 等圖形化工具：
     1. 在連線面板中對結構描述按右鍵。
     2. 展開「Tables」節點。
     3. 對資料表按右鍵，選擇「Count Rows」或開啟「Data」分頁預覽內容（若有權限）。
     - 若「Data」分頁顯示空白，可能是權限問題或資料表確實無資料列。

---

### 實務範例
假設您位於名為 `HR` 的結構描述中。您需要：
1. 執行：
   ```sql
   SELECT table_name, num_rows
   FROM user_tables
   WHERE num_rows > 0;
   ```
   輸出結果可能如下：
   ```
   TABLE_NAME   NUM_ROWS
   ----------   --------
   EMPLOYEES    107
   DEPARTMENTS  27
   ```
   這表示 `EMPLOYEES` 和 `DEPARTMENTS` 包含資料。

2. 若懷疑統計資料過時，請更新：
   ```sql
   EXEC DBMS_STATS.GATHER_SCHEMA_STATS('HR');
   ```
3. 重新執行相同查詢。

---

### 資料表顯示空白的可能原因
- **無資料**：資料表確實沒有任何資料列。
- **權限不足**：您可查看資料表結構但無法存取資料。
- **篩選條件**：圖形化工具可能設有篩選條件隱藏資料列（例如 `WHERE` 子句）。
- **資料截斷/刪除**：資料可能近期被移除。
- **同義詞/視圖**：您可能正在檢視指向空白或無法存取資料表的同義詞或視圖。

若問題仍未解決，請提供您的具體環境資訊（例如結構描述名稱、使用工具），我將進一步提供客製化建議！