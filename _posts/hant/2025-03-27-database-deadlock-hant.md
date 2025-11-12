---
audio: false
generated: true
lang: hant
layout: post
title: 數據庫死鎖
translated: true
type: note
---

**數據庫死鎖**發生在兩個或多個交易互相等待對方釋放資源鎖定時，形成循環依賴關係，導致所有交易都無法繼續執行。數據庫管理系統（DBMS）通常會檢測到此情況，並通過回滾其中一個交易來解決問題。以下是一個詳細的死鎖情境範例：

---

### 範例：兩個交易之間的死鎖
- **情境**： 
  - 交易 T1 更新 `Orders` 表中的一列，然後需要更新 `Customers` 表中的一列。
  - 交易 T2 更新 `Customers` 表中的一列，然後需要更新 `Orders` 表中的一列。
  - 兩個交易以不同的順序鎖定資源，導致死鎖。

- **逐步過程**：
  1. T1 鎖定 `Orders` 中的一列。
  2. T2 鎖定 `Customers` 中的一列。
  3. T1 嘗試鎖定 `Customers` 中的列（被 T2 阻塞）。
  4. T2 嘗試鎖定 `Orders` 中的列（被 T1 阻塞）。
  - 結果：兩個交易都無法繼續，形成死鎖。

- **SQL 範例**：
  ```sql
  -- 交易 T1
  BEGIN TRANSACTION;
  UPDATE Orders SET Status = '已發貨' WHERE OrderID = 100;  -- 鎖定 OrderID 100
  -- （某些延遲或處理）
  UPDATE Customers SET LastOrderDate = '2025-03-27' WHERE CustomerID = 1;  -- 被 T2 阻塞

  -- 交易 T2
  BEGIN TRANSACTION;
  UPDATE Customers SET Balance = Balance - 50 WHERE CustomerID = 1;  -- 鎖定 CustomerID 1
  -- （某些延遲或處理）
  UPDATE Orders SET PaymentStatus = '已付款' WHERE OrderID = 100;  -- 被 T1 阻塞
  ```

- **發生情況**：
  - T1 持有 `OrderID = 100` 的獨佔鎖，並等待 `CustomerID = 1`。
  - T2 持有 `CustomerID = 1` 的獨佔鎖，並等待 `OrderID = 100`。
  - 這種循環等待條件即為死鎖。
  - DBMS 檢測到死鎖（例如通過超時或死鎖檢測算法），並回滾其中一個交易（例如 T2），讓 T1 完成。

---

### 死鎖的視覺化表示
```
T1: 鎖定 Orders(100) --> 等待 Customers(1)
   |                        ↑
   |                        |
T2: 等待 Orders(100)  <-- 鎖定 Customers(1)
```

- **解決方式**：DBMS 可能會輸出類似以下的錯誤：
  ```
  交易 T2 在鎖定資源時與另一個進程發生死鎖，已被選為死鎖犧牲者。請重新執行該交易。
  ```

---

### 發生成因
- **鎖定順序**：T1 和 T2 以不同順序獲取鎖定（T1：Orders → Customers；T2：Customers → Orders）。
- **並發性**：兩個交易同時運行，並需要重疊的資源。
- **獨佔鎖**：更新操作需要獨佔鎖，這會阻止其他交易訪問同一數據。

---

### 如何避免死鎖
1. **一致的鎖定順序**：確保所有交易以相同順序獲取鎖定（例如總是先鎖定 `Orders`，再鎖定 `Customers`）。
   ```sql
   -- T1 和 T2 都應先鎖定 Orders，再鎖定 Customers
   ```
2. **縮短交易時間**：盡量減少交易內的延遲，以降低重疊機會。
3. **使用較低隔離級別**：如果合適，使用較寬鬆的隔離級別（例如 Read Committed）以縮短鎖定時間。
4. **設定超時**：設置較短的鎖定超時時間，以便快速失敗並重試。

---

如果需要更具體的範例（例如使用特定 DBMS 如 PostgreSQL 或 SQL Server）或進一步說明，請告訴我！