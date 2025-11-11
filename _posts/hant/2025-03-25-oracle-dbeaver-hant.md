---
audio: false
generated: true
lang: hant
layout: post
title: 使用 DBeaver 檢查 Oracle 數據庫表格數據的步驟
translated: true
type: note
---

我假設您是基於先前關於在 Oracle 資料庫中尋找有資料的資料表的問題，想了解如何使用 DBeaver 進行檢查。DBeaver 是一款流行、免費、跨平台的資料庫工具，能良好支援 Oracle 及其他資料庫。以下我將逐步說明如何使用 DBeaver 檢視您的 Oracle 結構描述並識別含有資料的資料表。

---

#### 1. **設定連線至您的 Oracle 資料庫**
   - **安裝 DBeaver**：若尚未安裝，請從 [dbeaver.io](https://dbeaver.io/) 下載並安裝 DBeaver（社區版即可）。
   - **建立新連線**：
     1. 開啟 DBeaver，點選選單中的 **Database** > **New Database Connection**。
     2. 從清單中選擇 **Oracle**，然後點選 **Next**。
     3. 輸入您的連線詳細資訊：
        - **Host**：您的 Oracle 伺服器主機名稱或 IP。
        - **Port**：通常為 1521（Oracle 預設埠）。
        - **Database/SID 或 Service Name**：依您的設定而定（例如 SID = `XE` 表示 Express Edition，或服務名稱）。
        - **Username** 與 **Password**：您的 Oracle 登入憑證。
     4. 點選 **Test Connection** 以驗證連線是否正常。若系統提示，您可能需要下載 Oracle JDBC 驅動程式（DBeaver 可自動完成）。
     5. 點選 **Finish** 以儲存連線。

#### 2. **在資料庫導覽器中瀏覽結構描述**
   - 在 **Database Navigator**（左側面板）中，展開您的 Oracle 連線。
   - 您將看到結構描述清單（例如您的使用者名稱或其他您有權限存取的結構描述）。展開您要檢視的結構描述。
   - 在每個結構描述下，展開 **Tables** 節點以查看所有資料表。

#### 3. **使用圖形介面檢查資料表是否含有資料**
   - **檢視資料表資料**：
     1. 雙擊資料表名稱，或右鍵點選並選擇 **Edit Table**。
     2. 在開啟的編輯器中切換至 **Data** 分頁。
     3. 若資料表含有資料，您將看到顯示的資料列；若為空，則不會顯示任何資料列（或出現「No data」等訊息）。
     - 預設情況下，DBeaver 最多擷取 200 列資料。若要擷取所有資料列，請點選 Data 分頁底部工具列中的 **Fetch All Rows** 按鈕（小型箭頭圖示）。
   - **快速計算資料列數**：
     1. 在 Database Navigator 中右鍵點選資料表。
     2. 選擇 **Navigate** > **Row Count**。
     3. DBeaver 將執行 `SELECT COUNT(*)` 查詢並在彈出視窗中顯示結果。若結果為 0，表示該資料表為空。

#### 4. **執行 SQL 查詢以檢查多個資料表**
   - 若您希望一次檢查多個資料表（比逐個點選更有效率），請使用 SQL 編輯器：
     1. 點選 **SQL Editor** > **New SQL Script**（或按 `Ctrl + [`）。
     2. 設定結構描述上下文：
        - 使用 SQL 編輯器頂部的下拉選單選擇您的結構描述，或執行：
          ```sql
          ALTER SESSION SET CURRENT_SCHEMA = schema_name;
          ```
          將 `schema_name` 替換為您的目標結構描述（例如 `HR`）。
     3. 查詢所有資料表的資料列數：
        - 使用以下 SQL 列出含有資料的資料表（類似我先前的回答）：
          ```sql
          SELECT table_name, num_rows
          FROM user_tables
          WHERE num_rows > 0
          ORDER BY num_rows DESC;
          ```
        - 按 `Ctrl + Enter` 執行。結果將顯示於下方的 **Results** 分頁。
        - `USER_TABLES` 顯示您結構描述中的資料表。若需跨結構描述存取資料表，請使用 `ALL_TABLES`：
          ```sql
          SELECT owner, table_name, num_rows
          FROM all_tables
          WHERE num_rows > 0
          AND owner = UPPER('schema_name');
          ```
     4. **注意**：`NUM_ROWS` 是基於上次統計資料更新後的估計值。若數值不準確，請使用以下指令更新統計資料：
        ```sql
        EXEC DBMS_STATS.GATHER_SCHEMA_STATS('schema_name');
        ```