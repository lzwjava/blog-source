---
audio: false
generated: true
lang: hant
layout: post
title: 數據庫阻塞
translated: true
type: note
---

我假設您想了解資料庫管理系統（DBMS）中的資料庫阻塞範例。當某個交易因並行存取或修改相同資料而阻礙另一個交易進行時，就會發生阻塞現象。這通常透過鎖定機制來管理，以確保資料的一致性與完整性。以下是幾種常見的資料庫阻塞情境：

---

### 範例一：讀寫阻塞
- **情境**：交易 T1 正在更新資料表中的某列（例如修改客戶餘額），此時交易 T2 嘗試讀取同一列資料。
- **運作機制**：T1 會取得該列的獨佔鎖，防止其他交易在更新完成前讀取或修改資料。T2 將被阻塞，必須等待 T1 提交或回滾後才能繼續。
- **SQL 範例**：
  ```sql
  -- 交易 T1
  BEGIN TRANSACTION;
  UPDATE Accounts SET Balance = Balance - 100 WHERE AccountID = 1;

  -- 交易 T2（被阻塞）
  SELECT Balance FROM Accounts WHERE AccountID = 1;
  ```
  由於 T1 對資料列持有獨佔鎖，T2 需等待 T1 完成作業。

---

### 範例二：寫寫阻塞
- **情境**：交易 T1 正在更新產品庫存數量，同時交易 T2 也嘗試更新同一筆產品庫存。
- **運作機制**：T1 持有該資料列的獨佔鎖，T2 將被阻塞直至 T1 完成操作。這種機制可避免因衝突更新導致資料不一致。
- **SQL 範例**：
  ```sql
  -- 交易 T1
  BEGIN TRANSACTION;
  UPDATE Products SET Stock = Stock - 5 WHERE ProductID = 100;

  -- 交易 T2（被阻塞）
  UPDATE Products SET Stock = Stock + 10 WHERE ProductID = 100;
  ```
  T2 需等待 T1 提交或回滾後才能執行。

---

### 範例三：死結（阻塞導致的僵局）
- **情境**：交易 T1 鎖定資料列 A 後需更新資料列 B，而交易 T2 鎖定資料列 B 後需更新資料列 A。
- **運作機制**：T1 被 T2 對資料列 B 的鎖定阻塞，T2 同時被 T1 對資料列 A 的鎖定阻塞，形成死結。此時 DBMS 需介入處理（例如回滾其中一筆交易）。
- **SQL 範例**：
  ```sql
  -- 交易 T1
  BEGIN TRANSACTION;
  UPDATE Table1 SET Value = 10 WHERE ID = 1;  -- 鎖定資料列 A
  UPDATE Table2 SET Value = 20 WHERE ID = 2;  -- 被 T2 阻塞

  -- 交易 T2
  BEGIN TRANSACTION;
  UPDATE Table2 SET Value = 30 WHERE ID = 2;  -- 鎖定資料列 B
  UPDATE Table1 SET Value = 40 WHERE ID = 1;  -- 被 T1 阻塞
  ```
  兩筆交易皆無法繼續執行，直到 DBMS 解除死結狀態。

---

### 範例四：資料表層級阻塞
- **情境**：交易 T1 在缺乏適當索引的情況下對整張資料表進行大規模更新，此時交易 T2 嘗試從同一張資料表讀取單筆資料列。
- **運作機制**：T1 可能將資料列層級鎖定升級為資料表層級鎖定，導致 T2 即使讀取無關資料列也會被阻塞。
- **SQL 範例**：
  ```sql
  -- 交易 T1
  BEGIN TRANSACTION;
  UPDATE Employees SET Salary = Salary * 1.1;  -- 鎖定整張資料表

  -- 交易 T2（被阻塞）
  SELECT Name FROM Employees WHERE EmployeeID = 5;
  ```
  由於 T1 持有資料表獨佔鎖，T2 的讀取操作將被阻塞。

---

### 阻塞管理機制
- **鎖定類型**：資料庫透過共享鎖（用於讀取）與獨佔鎖（用於寫入）來控管存取權限。
- **隔離層級**：較高的隔離層級（如 Serializable）會增加阻塞以確保一致性，較低層級（如 Read Uncommitted）則能減少阻塞但可能產生髒讀問題。
- **逾時設定**：若交易被阻塞過久，系統將強制回滾以解除僵局。
- **死結偵測**：DBMS 會自動偵測死結狀況，並透過終止其中一筆交易來化解僵局。

如果您需要針對特定資料庫系統（如 MySQL、PostgreSQL、SQL Server）的詳細說明或範例，歡迎隨時提出！