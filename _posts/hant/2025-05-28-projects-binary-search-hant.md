---
audio: false
generated: true
lang: hant
layout: post
title: 二分查找在金融數據項目中的應用
translated: true
type: note
---

二元搜尋是一種高效演算法，透過不斷將搜尋區間對半分割，從**已排序**的項目清單中尋找特定項目。在您專注於數據、數據庫、Angular 前端和 SQL 查詢的金融專案中，二元搜尋可應用於需要搜尋已排序數據的特定場景。以下將根據您的技術堆疊和金融領域，說明如何在專案中應用二元搜尋。

### 二元搜尋的關鍵特性
- **必要條件**：數據必須**已排序**（例如升序或降序排列）
- **時間複雜度**：O(log n)，對於大型數據集比線性搜尋（O(n)）快得多
- **使用場景**：最適合靜態或較少變動的已排序數據，需要快速定位特定值的情況

### 二元搜尋在金融專案中的應用場景
在具有數據庫密集型後端和 Angular 前端的金融專案中，二元搜尋可應用於以下領域：

#### 1. **後端：在已排序的數據庫結果中搜尋**
   - **場景**：您的金融專案可能涉及查詢大型數據集（例如交易記錄、股價或帳戶餘額），這些數據按交易ID、日期或金額等字段排序。如果數據已排序（或透過 SQL 查詢排序），您可以在提取到記憶體後使用二元搜尋高效定位特定記錄
   - **範例**：
     - 您透過類似以下查詢從數據庫檢索已排序的交易清單：
       ```sql
       SELECT * FROM transactions WHERE account_id = ? ORDER BY transaction_date;
       ```
     - 將結果提取到後端（例如 Node.js、Java 或 Python）後，可使用二元搜尋按日期或 ID 查找特定交易，無需遍歷整個清單
   - **實作方式**：
     - 將已排序數據加載到後端的陣列或清單中
     - 實作二元搜尋來尋找目標記錄，例如在 JavaScript 中：
       ```javascript
       function binarySearch(arr, target, key) {
           let left = 0;
           let right = arr.length - 1;
           while (left <= right) {
               let mid = Math.floor((left + right) / 2);
               if (arr[mid][key] === target) return arr[mid];
               if (arr[mid][key] < target) left = mid + 1;
               else right = mid - 1;
           }
           return null; // 未找到
       }

       // 範例：尋找特定日期的交易
       const transactions = [
           { id: 1, date: '2025-01-01', amount: 100 },
           { id: 2, date: '2025-01-02', amount: 200 },
           { id: 3, date: '2025-01-03', amount: 150 }
       ];
       const result = binarySearch(transactions, '2025-01-02', 'date');
       console.log(result); // { id: 2, date: '2025-01-02', amount: 200 }
       ```
   - **使用時機**：
     - 數據集已排序且相對靜態（例如歷史交易數據）
     - 數據集過大不適合線性搜尋，但經過 SQL 查詢後可放入記憶體
     - 需要在同一已排序數據集上執行多次搜尋

#### 2. **前端：在 Angular 中實現 UI 功能搜尋**
   - **場景**：在 Angular 前端中，您可能顯示已排序數據（例如按價格或日期排序的股價表格）。如果用戶需要快速查找特定項目（例如特定價格的股票或特定日期的交易），可以在前端實作二元搜尋來避免掃描整個數據集
   - **範例**：
     - 透過 API 從後端獲取已排序數據並存儲在 Angular 元件中
     - 在 TypeScript 中實作二元搜尋來尋找已排序陣列中的項目
     - 在 UI 中顯示結果（例如高亮顯示交易或滾動到表格特定行）
     - Angular 元件中的 TypeScript 範例：
       ```typescript
       export class TransactionComponent {
         transactions: any[] = [
           { id: 1, date: '2025-01-01', amount: 100 },
           { id: 2, date: '2025-01-02', amount: 200 },
           { id: 3, date: '2025-01-03', amount: 150 }
         ];

         findTransaction(targetDate: string) {
           let left = 0;
           let right = this.transactions.length - 1;
           while (left <= right) {
             let mid = Math.floor((left + right) / 2);
             if (this.transactions[mid].date === targetDate) {
               return this.transactions[mid];
             }
             if (this.transactions[mid].date < targetDate) {
               left = mid + 1;
             } else {
               right = mid - 1;
             }
           }
           return null; // 未找到
         }
       }
       ```
   - **使用時機**：
     - 前端接收已排序數據集（例如透過 API），需要為用戶互動執行快速搜尋（例如表格中的篩選或搜尋）
     - 數據集足夠小，可在瀏覽器中處理而不影響效能
     - 希望減少向後端發送搜尋 API 呼叫的次數

#### 3. **用於金融計算的記憶體數據結構**
   - **場景**：金融專案常涉及投資組合分析、歷史價格查詢或利率計算等計算。如果維護已排序的記憶體數據結構（例如歷史股價或利率陣列），二元搜尋可快速定位計算所需的值
   - **範例**：
     - 您有一個按日期排序的歷史股價陣列，需要為金融模型（例如計算回報）查找特定日期的價格
     - 使用二元搜尋高效定位價格，而非掃描整個陣列
     - Python 後端範例：
       ```python
       def binary_search(prices, target_date):
           left, right = 0, len(prices) - 1
           while left <= right:
               mid = (left + right) // 2
               if prices[mid]['date'] == target_date:
                   return prices[mid]['price']
               if prices[mid]['date'] < target_date:
                   left = mid + 1
               else:
                   right = mid - 1
           return None  # 未找到

       prices = [
           {'date': '2025-01-01', 'price': 100},
           {'date': '2025-01-02', 'price': 105},
           {'date': '2025-01-03', 'price': 110}
       ]
       price = binary_search(prices, '2025-01-02')
       print(price)  # 輸出：105
       ```
   - **使用時機**：
     - 對已排序數據集執行計算，如時間序列金融數據（例如股價、匯率）
     - 數據已排序或可在無顯著開銷的情況下預先排序

#### 4. **使用二元搜尋邏輯優化 SQL 查詢**
   - **場景**：雖然 SQL 數據庫已針對搜尋進行優化（例如使用索引），但在特定情況下可模擬二元搜尋邏輯，例如處理已建立索引的排序數據時，或在存儲過程中實作自定義搜尋邏輯時
   - **範例**：
     - 如果有一個帶有排序索引的大型表格（例如 transaction_date 上的索引），可編寫使用類似二元搜尋邏輯的存儲過程來縮小搜尋範圍
     - 例如在 PostgreSQL 存儲過程中：
       ```sql
       CREATE OR REPLACE FUNCTION find_transaction(target_date DATE)
       RETURNS TABLE (id INT, amount NUMERIC) AS $$
       DECLARE
           mid_point DATE;
           lower_bound DATE;
           upper_bound DATE;
       BEGIN
           SELECT MIN(transaction_date), MAX(transaction_date)
           INTO lower_bound, upper_bound
           FROM transactions;

           WHILE lower_bound <= upper_bound LOOP
               mid_point := lower_bound + (upper_bound - lower_bound) / 2;
               IF EXISTS (
                   SELECT 1 FROM transactions
                   WHERE transaction_date = target_date
                   AND transaction_date = mid_point
               ) THEN
                   RETURN QUERY
                   SELECT id, amount FROM transactions
                   WHERE transaction_date = target_date;
                   RETURN;
               ELSIF target_date > mid_point THEN
                   lower_bound := mid_point + INTERVAL '1 day';
               ELSE
                   upper_bound := mid_point - INTERVAL '1 day';
               END IF;
           END LOOP;
           RETURN;
       END;
       $$ LANGUAGE plpgsql;
       ```
   - **使用時機**：
     - 處理非常大型的數據集，且數據庫內建索引無法滿足特定搜尋模式
     - 在存儲過程中實作自定義邏輯以進行效能優化
     - 注意：此做法較不常見，因為數據庫索引（例如 B-tree）內部已使用類似原理

#### 5. **快取頻繁搜尋的數據**
   - **場景**：在金融應用中，某些數據（例如匯率、稅率或歷史數據）會被頻繁訪問，可以按排序顺序進行快取。二元搜尋可用於快速查詢此快取數據
   - **範例**：
     - 在 Redis 快取或記憶體數據結構中快取已排序的匯率清單
     - 使用二元搜尋查找特定日期或貨幣對的匯率
     - Node.js 與 Redis 的範例：
       ```javascript
       const redis = require('redis');
       const client = redis.createClient();

       async function findExchangeRate(targetDate) {
           const rates = JSON.parse(await client.get('exchange_rates')); // 已排序陣列
           let left = 0;
           let right = rates.length - 1;
           while (left <= right) {
               let mid = Math.floor((left + right) / 2);
               if (rates[mid].date === targetDate) return rates[mid].rate;
               if (rates[mid].date < targetDate) left = mid + 1;
               else right = mid - 1;
           }
           return null;
       }
       ```
   - **使用時機**：
     - 快取靜態或半靜態數據（例如每日匯率、稅表）
     - 快取數據已排序，且需要執行頻繁查詢

### **不適合**使用二元搜尋的情況
- **未排序數據**：二元搜尋需要已排序數據。如果排序成本過高（O(n log n)），請考慮其他演算法或數據結構（例如用於 O(1) 查詢的雜湊表）
- **動態數據**：如果數據集頻繁變動（例如實時股價），維護排序狀態的成本很高。請改用數據庫索引或其他數據結構如雜湊映射或樹結構
- **小型數據集**：對於小型數據集（例如 < 100 個項目），由於開銷較低，線性搜尋可能更快
- **數據庫層級搜尋**：具有適當索引（例如 B-tree 或雜湊索引）的 SQL 數據庫已針對搜尋進行優化。二元搜尋更適用於記憶體數據或查詢後處理

### 專案實務考量
1. **數據量**：二元搜尋在大型數據集（例如數千或數百萬條記錄）中表現出色。請評估您的數據集是否足夠大，能從二元搜尋中受益，而非使用線性搜尋或數據庫查詢
2. **排序開銷**：確保數據已排序或排序可行。例如從 SQL 檢索已排序數據（`ORDER BY`）或在記憶體中維護已排序陣列
3. **與 Angular 整合**：在前端，對客戶端篩選或已排序表格中的搜尋使用二元搜尋，以改善用戶體驗（例如在分頁表格中快速找到交易）
4. **金融特定使用案例**：
   - **交易查詢**：在已排序清單中按 ID、日期或金額查找特定交易
   - **時間序列分析**：在歷史金融數據中定位特定日期（例如股價、利率）
   - **投資組合管理**：在已排序投資組合中搜尋特定資產或指標
5. **替代數據結構**：
   - 如果二元搜尋不適用（例如未排序或動態數據），請考慮：
     - **雜湊映射**：用於按鍵值進行 O(1) 查詢（例如交易 ID）
     - **B-Tree 或索引**：讓數據庫高效處理搜尋
     - **Trie 或前綴樹**：用於基於字串的搜尋（例如搜尋帳戶名稱）

### 專案中的範例工作流程
1. **後端**：
   - 執行 SQL 查詢獲取已排序交易：`SELECT * FROM transactions WHERE account_id = ? ORDER BY transaction_date`
   - 將結果加載到記憶體陣列中
   - 使用二元搜尋按日期或金額查找特定交易
2. **前端**：
   - 透過 API 獲取已排序數據並在 Angular 表格中顯示
   - 在 Angular 元件中使用二元搜尋實作搜尋功能，以高亮顯示或篩選特定記錄
3. **快取**：
   - 在 Redis 或記憶體存儲中快取頻繁訪問的已排序數據（例如匯率）
   - 使用二元搜尋查詢快取以實現快速查找

### 結論
二元搜尋是處理**已排序、靜態或半靜態**記憶體數據時的強大工具，無論在後端（例如 SQL 查詢後）還是前端（例如 Angular 表格）都能發揮作用。它特別適用於大型數據集，其中 O(log n) 的效能優勢明顯，例如交易查詢、時間序列數據搜尋或快取數據查詢。但請確保數據已排序，並對於未排序或動態數據考慮替代方案，如數據庫索引或雜湊映射。如果您有特定的數據集或使用案例，請告訴我，我可以進一步調整範例！