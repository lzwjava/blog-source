---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: IBM Db2 系統目錄概覽
translated: true
type: note
---

### IBM Db2 系統資料表簡介

IBM Db2 中的系統目錄（亦稱為 Db2 目錄）是一個內建的元資料儲存庫，其中儲存了您資料庫中每個物件與元素的詳細資訊。這包含了資料表、視圖、索引、欄位、使用者、權限、常式等。它本質上是您資料庫的「電話簿」——當您建立、修改或刪除物件時，會由 Db2 自動維護。此目錄能協助資料庫管理員、開發人員及工具查詢資料庫的結構與狀態，而無需解析應用程式碼或外部檔案。

與一般使用者資料表不同，系統目錄對大多數使用者而言是唯讀的，且針對查詢元資料而非高容量資料操作進行了優化。它在您建立新資料庫時會自動建立，並位於特殊的資料表空間中（例如 Db2 LUW 中的 SYSCATSPACE）。

#### 關鍵組件與結構
系統目錄包含：
- **基礎資料表**：這些是底層的標準化資料表，用於儲存原始元資料。它們位於 **SYSIBM** 綱要中，為避免意外修改或效能問題，終端使用者無法直接查詢。範例包括 SYSIBM.SYSTABLES（基礎資料表資訊）和 SYSIBM.SYSCOLUMNS（欄位詳細資料）。
- **目錄視圖**：建構於基礎資料表之上的使用者友善、非標準化視圖。這些視圖更易於查詢，並提供符合 SQL 標準（如 ISO）的標準化介面。它們分組於以下綱要中：
  - **SYSCAT**：關於資料庫物件的核心元資料（例如：資料表、索引、觸發器）。
  - **SYSCOLUMNS**：詳細的欄位層級資訊。
  - **SYSSTAT**：查詢最佳化工具使用的統計資料（例如：列計數、基數）。
  - **SYSPROC** 及其他：用於程序、函數及 XML 相關資訊。

在 Db2 for z/OS 中，目錄位於資料庫 DSNDB06 中，但其概念在各平台（LUW、z/OS、i）間是相似的。

#### 用途
- **探索**：找出存在的物件、其屬性及關聯。
- **管理**：監控權限、相依性及效能統計資料。
- **開發**：產生 DDL 指令碼、驗證綱要，或與工具（如 Db2 Data Studio）整合。
- **最佳化**：查詢最佳化工具使用 SYSSTAT 視圖來選擇執行計畫。

#### 如何存取與查詢
1. **連線到資料庫**：使用 `db2 connect to <dbname>`。
2. **權限**：預設情況下，PUBLIC 對目錄視圖擁有 SELECT 權限。基礎查詢無需特殊授權，但 SYSIBM 基礎資料表需要 SYSADM 或更高權限。
3. **查詢**：使用標準 SQL SELECT 語句。視圖需以綱要限定（例如：`SELECT * FROM SYSCAT.TABLES`）。

**查詢範例**：
- **列出目前綱要中的所有資料表**：
  ```
  SELECT TABSCHEMA, TABNAME, TYPE FROM SYSCAT.TABLES
  WHERE TABSCHEMA = CURRENT SCHEMA;
  ```
  - 輸出：顯示綱要、資料表名稱及類型（例如：'T' 代表資料表，'V' 代表視圖）。

- **取得資料表的欄位詳細資料**：
  ```
  SELECT COLNAME, TYPENAME, LENGTH, NULLS
  FROM SYSCOLUMNS
  WHERE TABSCHEMA = 'YOUR_SCHEMA' AND TABNAME = 'YOUR_TABLE';
  ```
  - 輸出：欄位名稱、資料類型、長度及可為空值性。

- **檢查資料表統計資料**：
  ```
  SELECT CARD, NPAGES FROM SYSSTAT.TABLES
  WHERE TABNAME = 'YOUR_TABLE';
  ```
  - CARD：預估列計數；NPAGES：頁面數量。

要取得完整清單，可執行 `SELECT * FROM SYSCAT.VIEWS WHERE VIEWNAME LIKE 'SYSCAT%'` 以探索所有可用視圖。

#### 重要注意事項
- **效能**：目錄查詢速度很快，但在大型資料庫上可能耗用較多資源；請使用篩選條件（例如 WHERE 子句）來限制結果。
- **更新**：Db2 會自動更新目錄——請勿嘗試手動 INSERT/UPDATE。
- **版本差異**：在 Db2 11.5+ 中，視圖更加標準化。對於 z/OS，部分視圖具有平台特定的欄位。
- **工具整合**：使用 Db2 的 `db2look` 指令從目錄資料產生 DDL：`db2look -d <dbname> -t <table>`。
- 除非您是系統管理員，否則請避免直接存取基礎資料表，因為這可能導致不一致。

若要深入探索，請查閱官方文件或在測試資料庫中進行實驗。

#### 參考資料
- [Db2 目錄概覽](https://www.ibm.com/docs/en/db2-for-zos/12?topic=objects-db2-catalog)
- [Db2 LUW 中的系統目錄視圖](https://www.ibm.com/docs/en/db2/11.5?topic=views-system-catalog)
- [從 DB2 系統目錄取得實用資訊](https://developer.ibm.com/articles/dm-0411melnyk/)