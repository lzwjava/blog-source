---
audio: false
generated: true
lang: hant
layout: post
title: Redis 指南
translated: true
type: note
---

這是一份關於 Redis 的全面指南。Redis 是一個開源的記憶體資料結構儲存系統，廣泛用作資料庫、快取和訊息代理。本指南將涵蓋其基礎知識、功能、使用案例、安裝方法、基本操作及進階概念。

---

### 什麼是 Redis？
Redis（Remote Dictionary Server）是一個高效能的鍵值儲存系統，主要運作於記憶體中，因此速度極快。它支援多種資料結構，例如字串、雜湊、列表、集合、有序集合、點陣圖、基數估計和地理空間索引。Redis 由 Salvatore Sanfilippo 於 2009 年創建，目前由社群維護並受 Redis Inc. 贊助。

主要特性：
- **記憶體內儲存**：資料儲存於 RAM 中，實現低延遲存取。
- **持久性**：提供可選的磁碟持久化功能以確保資料耐久性。
- **多功能**：支援超越簡單鍵值對的複雜資料結構。
- **可擴展**：提供叢集和複製功能以實現高可用性。

---

### 為何使用 Redis？
Redis 因其速度和靈活性而廣受歡迎。常見使用案例包括：
1. **快取**：透過儲存頻繁存取的資料（例如 API 回應、網頁）來加速應用程式。
2. **工作階段管理**：在網路應用程式中儲存使用者工作階段資料。
3. **即時分析**：追蹤指標、排行榜或事件計數器。
4. **發布/訂閱訊息傳遞**：實現程序或服務之間的即時訊息傳遞。
5. **任務佇列**：管理後台作業（例如使用 Celery 等工具）。
6. **地理空間應用**：處理基於位置的查詢（例如尋找附近的景點）。

---

### 主要功能
1. **資料結構**：
   - **字串**：簡單的鍵值對（例如 `SET key "value"`）。
   - **列表**：有序集合（例如 `LPUSH mylist "item"`）。
   - **集合**：無序且唯一的集合（例如 `SADD myset "item"`）。
   - **有序集合**：帶有分數用於排名的集合（例如 `ZADD leaderboard 100 "player1"`）。
   - **雜湊**：鍵值映射（例如 `HSET user:1 name "Alice"`）。
   - **點陣圖、HyperLogLogs、Streams**：用於特殊用例，如計算獨立用戶或事件串流。

2. **持久化**：
   - **RDB（快照）**：定期將資料作為時間點快照儲存到磁碟。
   - **AOF（僅附加檔案）**：記錄每個寫入操作以確保耐久性；可以重播以重建資料集。

3. **複製**：主從複製，實現高可用性和讀取擴展。
4. **叢集**：將資料分佈到多個節點以實現水平擴展。
5. **原子操作**：透過如 `INCR` 或 `MULTI` 等指令確保安全的並行存取。
6. **Lua 腳本**：允許自訂伺服器端邏輯。
7. **發布/訂閱**：用於即時通訊的輕量級訊息系統。

---

### 安裝
Redis 可在 Linux、macOS 和 Windows（透過 WSL 或非官方版本）上使用。以下是在 Linux 系統上安裝的方法：

1. **透過套件管理員**（Ubuntu/Debian）：
   ```bash
   sudo apt update
   sudo apt install redis-server
   ```

2. **從原始碼安裝**：
   ```bash
   wget http://download.redis.io/releases/redis-7.0.15.tar.gz
   tar xzf redis-7.0.15.tar.gz
   cd redis-7.0.15
   make
   sudo make install
   ```

3. **啟動 Redis**：
   ```bash
   redis-server
   ```

4. **驗證安裝**：
   ```bash
   redis-cli ping
   ```
   輸出：`PONG`

5. **配置**：編輯 `/etc/redis/redis.conf`（或等效檔案）以調整持久化、記憶體限制或綁定特定 IP 等設定。

---

### 基本操作
Redis 透過 `redis-cli` 或客戶端函式庫使用簡單的指令型介面。以下是一些範例：

#### 字串
- 設定值：`SET name "Alice"`
- 取得值：`GET name` → `"Alice"`
- 遞增：`INCR counter` → `1`（遞增至 2、3 等）

#### 列表
- 從左側加入：`LPUSH mylist "item1"`
- 從右側加入：`RPUSH mylist "item2"`
- 從左側彈出：`LPOP mylist` → `"item1"`

#### 集合
- 加入項目：`SADD myset "apple" "banana"`
- 列出成員：`SMEMBERS myset` → `"apple" "banana"`
- 檢查成員資格：`SISMEMBER myset "apple"` → `1`（真）

#### 雜湊
- 設定欄位：`HSET user:1 name "Bob" age "30"`
- 取得欄位：`HGET user:1 name` → `"Bob"`
- 取得所有欄位：`HGETALL user:1`

#### 有序集合
- 帶分數加入：`ZADD leaderboard 100 "player1" 200 "player2"`
- 取得頂部分數：`ZRANGE leaderboard 0 1 WITHSCORES` → `"player1" "100" "player2" "200"`

---

### 進階概念
1. **持久化配置**：
   - 啟用 RDB：在 `redis.conf` 中設定 `save 60 1000`（如果 1000 個鍵變更，則每 60 秒儲存一次）。
   - 啟用 AOF：設定 `appendonly yes` 以記錄寫入操作。

2. **複製**：
   - 配置從節點：`SLAVEOF master_ip master_port`。
   - 檢查狀態：`INFO REPLICATION`。

3. **叢集**：
   - 在 `redis.conf` 中透過 `cluster-enabled yes` 啟用。
   - 使用 `redis-cli --cluster create` 來設定節點。

4. **驅逐策略**：
   - 使用 `maxmemory` 和策略如 `LRU`（最近最少使用）或 `LFU`（最不常使用）來控制記憶體使用。
   - 範例：`maxmemory-policy allkeys-lru`。

5. **交易**：
   - 群組指令：`MULTI`，後跟指令，然後 `EXEC`。
   - 範例：
     ```
     MULTI
     SET key1 "value1"
     SET key2 "value2"
     EXEC
     ```

6. **發布/訂閱**：
   - 訂閱：`SUBSCRIBE channel1`
   - 發布：`PUBLISH channel1 "Hello"`

---

### 客戶端函式庫
Redis 支援多種程式語言。範例：
- **Python**：`redis-py`（`pip install redis`）
  ```python
  import redis
  r = redis.Redis(host='localhost', port=6379, db=0)
  r.set('key', 'value')
  print(r.get('key'))  # b'value'
  ```
- **Node.js**：`ioredis`
  ```javascript
  const Redis = require('ioredis');
  const redis = new Redis();
  redis.set('key', 'value');
  redis.get('key').then(console.log); // 'value'
  ```

---

### 效能提示
1. **使用管道傳輸**：批次處理指令以減少往返延遲。
2. **優化資料結構**：選擇正確的結構（例如，對小型物件使用雜湊而非多個鍵）。
3. **監控記憶體**：使用 `INFO MEMORY` 來追蹤使用情況。
4. **調整持久化**：在速度（RDB）和耐久性（AOF）之間取得平衡。

---

### 安全性
- **綁定到 localhost**：在 `redis.conf` 中設定 `bind 127.0.0.1` 以限制存取。
- **設定密碼**：使用 `requirepass yourpassword`。
- **停用危險指令**：使用 `rename-command`（例如 `rename-command FLUSHALL ""`）。

---

### 限制
- **記憶體限制**：資料大小受可用 RAM 限制。
- **單執行緒**：核心操作在單一執行緒上運行（儘管新版本中的 I/O 和持久化可以使用多執行緒）。
- **無複雜查詢**：缺乏類似 SQL 的查詢功能；依賴基於鍵的存取。

---

### Redis 與其他資料庫的比較
- **Redis vs. Memcached**：Redis 提供更豐富的資料結構和持久化；Memcached 更簡單且純記憶體。
- **Redis vs. MongoDB**：Redis 在快取方面更快，但較不適合複雜的持久化文件儲存。
- **Redis vs. PostgreSQL**：Redis 擅長即時、低延遲任務；PostgreSQL 更適合關聯式資料和 ACID 合規性。

---

### 資源
- **官方文件**：[redis.io](https://redis.io)
- **試用 Redis**：[try.redis.io](https://try.redis.io)（互動式教學）
- **GitHub**：[github.com/redis/redis](https://github.com/redis/redis)

---

本指南為理解和應用 Redis 提供了堅實的基礎。如果您想深入了解任何特定方面，請告訴我們！