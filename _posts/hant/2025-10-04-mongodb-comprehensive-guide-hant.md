---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: MongoDB 全面指南
translated: true
type: note
---

MongoDB 是一款廣受歡迎的開源 NoSQL 文件數據庫，專為現代應用程式開發而設計。它將數據儲存在靈活的 JSON 格式文件中，稱為 BSON（二進制 JSON），非常適合處理非結構化或半結構化數據。與傳統關聯式數據庫不同，MongoDB 採用無模式設計，允許集合（文件群組）擁有不同的結構。它具有高度可擴展性，支援通過分片進行水平擴展，並通過複製提供高可用性。MongoDB 可以部署在本地、通過 MongoDB Atlas（託管服務）在雲端部署，或在混合環境中部署。本指南涵蓋從基礎到進階主題的所有內容，並使用 MongoDB Shell（mongosh）提供範例。

## 簡介

MongoDB 在需要快速開發、靈活數據模型和高性能的場景中表現出色。主要功能包括：
- **文件模型**：數據以自包含的文件形式存在，具有嵌套結構。
- **查詢語言**：使用類似 JavaScript 物件的語法進行豐富查詢。
- **可擴展性**：內建對分散式系統的支援。
- **生態系統**：通過官方驅動程式與 Python、Node.js、Java 等語言整合。

它被 Adobe、eBay 和 Forbes 等公司用於涉及大數據、實時分析和內容管理的應用程式。

## 安裝

MongoDB 提供社群版（免費、開源）和企業版。安裝方法因平台而異；請務必從官方網站下載以確保安全。

### Windows
- 從 MongoDB 下載中心下載 MSI 安裝程式。
- 運行安裝程式，選擇「完整」設置，並包含 MongoDB Compass（GUI 工具）。
- 將 MongoDB 的 `bin` 目錄（例如 `C:\Program Files\MongoDB\Server\8.0\bin`）添加到您的 PATH 中。
- 創建數據目錄：`mkdir -p C:\data\db`。
- 啟動伺服器：`mongod.exe --dbpath C:\data\db`。

支援：Windows 11、Server 2022/2019。

### macOS
- 使用 Homebrew：`brew tap mongodb/brew && brew install mongodb-community`。
- 或下載 TGZ 存檔，解壓並添加到 PATH。
- 創建數據目錄：`mkdir -p /data/db`。
- 啟動：`mongod --dbpath /data/db`（或使用 `brew services start mongodb/brew/mongodb-community`）。

支援：macOS 11–14（x86_64 和 arm64）。

### Linux
- 對於 Ubuntu/Debian：添加 MongoDB 儲存庫金鑰和列表，然後 `apt-get install -y mongodb-org`。
- 對於 RHEL/CentOS：使用 yum/dnf 與儲存庫文件。
- 創建數據目錄：`sudo mkdir -p /data/db && sudo chown -R $USER /data/db`。
- 啟動：`sudo systemctl start mongod`。

支援：Ubuntu 24.04、RHEL 9+、Debian 12、Amazon Linux 2023 等。使用 XFS/EXT4 文件系統；避免 32 位元。

### 雲端（MongoDB Atlas）
- 在 mongodb.com/atlas 註冊。
- 通過 UI 或 CLI 創建免費集群：`atlas clusters create <name> --provider AWS --region us-east-1 --tier M0`。
- 將您的 IP 加入白名單：`atlas network-access create <IP>`。
- 獲取連接字符串並連接：`mongosh "mongodb+srv://<user>:<pass>@cluster0.abcde.mongodb.net/"`。

Atlas 自動處理備份、擴展和監控。

## 核心概念

### 數據庫
數據庫是集合的容器，邏輯上分隔數據。首次使用時隱式創建：`use mydb`。使用 `use mydb` 切換。列出：`show dbs`。

### 集合
文件的群組，類似表格但模式靈活。隱式創建：`db.mycollection.insertOne({})`。列出：`show collections`。

### 文件
基本單位：具有鍵值對的 BSON 物件。範例：
```javascript
{ "_id": ObjectId("..."), "name": "John", "age": 30, "address": { "city": "NYC", "zip": 10001 } }
```
支援陣列、嵌套物件和日期、二進制等類型。

### BSON
二進制格式，用於高效儲存/網絡傳輸。擴展 JSON 以支援 ObjectId、Date、Binary 等類型。

### 命名空間
唯一標識符：`database.collection`（例如 `mydb.orders`）。

範例設置：
```javascript
use test
db.orders.insertMany([
  { item: "almonds", price: 12, quantity: 2 },
  { item: "pecans", price: 20, quantity: 1 }
])
```

## CRUD 操作

在 mongosh 中使用 `db.collection.method()`。通過會話進行多文件 ACID 事務。

### 創建（插入）
- 單一：`db.users.insertOne({ name: "Alice", email: "alice@example.com" })`
- 多個：`db.users.insertMany([{ name: "Bob" }, { name: "Charlie" }])`
返回插入的 ID。

### 讀取（查找）
- 全部：`db.users.find()`
- 篩選：`db.users.find({ age: { $gt: 25 } })`
- 美觀打印：`.pretty()`
- 限制/排序：`db.users.find().limit(5).sort({ age: -1 })`

### 更新
- 單一：`db.users.updateOne({ name: "Alice" }, { $set: { age: 31 } })`
- 多個：`db.users.updateMany({ age: { $lt: 20 } }, { $set: { status: "minor" } })`
- 遞增：`{ $inc: { score: 10 } }`

### 刪除
- 單一：`db.users.deleteOne({ name: "Bob" })`
- 多個：`db.users.deleteMany({ status: "inactive" })`
- 刪除集合：`db.users.drop()`

## 查詢與索引

### 查詢
使用謂詞進行條件查詢。支援等值、範圍、邏輯操作。

- 基礎：`db.inventory.find({ status: "A" })`（SQL 等效：`WHERE status = 'A'`）
- $in：`db.inventory.find({ status: { $in: ["A", "D"] } })`
- $lt/$gt：`db.inventory.find({ qty: { $lt: 30 } })`
- $or：`db.inventory.find({ $or: [{ status: "A" }, { qty: { $lt: 30 } }] })`
- 正則表達式：`db.inventory.find({ item: /^p/ })`（以 "p" 開頭）
- 嵌入式：`db.users.find({ "address.city": "NYC" })`

投影（選擇字段）：`db.users.find({ age: { $gt: 25 } }, { name: 1, _id: 0 })`

### 索引
通過避免全掃描提高查詢速度。基於 B 樹。

- 類型：單字段（`db.users.createIndex({ name: 1 })`）、複合（`{ name: 1, age: -1 }`）、唯一（`{ email: 1 }`）。
- 好處：更快的等值/範圍查詢、排序結果。
- 創建：`db.users.createIndex({ age: 1 })`（升序）。
- 查看：`db.users.getIndexes()`
- 刪除：`db.users.dropIndex("age_1")`

使用 Atlas Performance Advisor 獲取建議。權衡：寫入速度較慢。

## 聚合框架

通過管道中的階段處理數據。類似 SQL GROUP BY 但更強大。

- 基礎：`db.orders.aggregate([ { $match: { price: { $lt: 15 } } } ])`
- 階段：`$match`（篩選）、`$group`（聚合：`{ $sum: "$price" }`）、`$sort`、`$lookup`（連接：`{ from: "inventory", localField: "item", foreignField: "sku", as: "stock" }`）、`$project`（重塑）。
- 範例（連接和排序）：
```javascript
db.orders.aggregate([
  { $match: { price: { $lt: 15 } } },
  { $lookup: { from: "inventory", localField: "item", foreignField: "sku", as: "inventory_docs" } },
  { $sort: { price: 1 } }
])
```
表達式：`{ $add: [ "$price", 10 ] }`。在 Atlas UI 中預覽。

## 模式設計

MongoDB 的靈活性避免了僵化的模式，但需要為性能進行深思熟慮的設計。

- **原則**：為存取模式（讀取/寫入）建模，使用索引，將工作集保留在 RAM 中。
- **嵌入**：將相關數據非正規化到一個文件中，以實現原子讀取/寫入。例如，將評論嵌入到貼文中。優點：查詢快速。缺點：重複、文件過大。
- **引用**：通過 ID 進行正規化。例如，`posts` 通過 `userId` 引用 `users`。使用 `$lookup` 進行連接。優點：重複較少。缺點：多個查詢。
- 模式：一對少（嵌入）、一對多（引用或嵌入陣列）、多對多（引用）。
- 驗證：使用 `db.createCollection("users", { validator: { $jsonSchema: { ... } } })` 強制執行。

考慮重複權衡和原子性（僅文件級別）。

## 複製與分片

### 複製
通過副本集（一組 `mongod` 實例）提供冗餘/高可用性。

- 組件：主節點（寫入）、從節點（通過操作日誌複製，讀取可選）、仲裁節點（投票，無數據）。
- 部署：使用 `rs.initiate({ _id: "rs0", members: [{ _id: 0, host: "host1:27017" }] })` 初始化。添加成員：`rs.add("host2:27017")`。
- 選舉：如果主節點故障，從節點在約 10-12 秒內選出新的主節點。
- 讀取偏好：`primary`、`secondary`（可能延遲）。
- 用於故障轉移、備份。啟用流量控制以管理延遲。

### 分片
水平擴展：將數據分佈到多個分片上。

- 組件：分片（副本集）、Mongos（路由器）、配置伺服器（元數據）。
- 分片鍵：用於分區的字段（例如，哈希用於均勻分佈）。首先創建索引。
- 設置：啟用分片 `sh.enableSharding("mydb")`，分片集合 `sh.shardCollection("mydb.users", { userId: "hashed" })`。
- 平衡器：遷移塊以實現均勻負載。區域用於地理局部性。
- 策略：哈希（均勻）、範圍（目標查詢）。

通過 mongos 連接；支援事務。

## 安全性

通過分層保護確保部署安全。

- **身份驗證**：SCRAM、LDAP、OIDC、X.509。創建用戶：`db.createUser({ user: "admin", pwd: "pass", roles: ["root"] })`。
- **授權**：基於角色的存取控制（RBAC）。內建角色：read、readWrite、dbAdmin。
- **加密**：TLS/SSL 用於傳輸中，靜態加密（EAR）通過 AWS KMS/Google Cloud KMS/Azure Key Vault。客戶端字段級加密（CSFLE）用於敏感字段。
- 網絡：IP 存取列表、Atlas 中的 VPC 對等。
- 審計：記錄操作。

啟動時啟用身份驗證：`--auth`。使用 Atlas 以獲得內建安全性。

## 最佳實踐

- **生產設置**：作為服務運行（systemctl/brew）。將數據/日誌/日誌分開存放在 SSD 上。使用 WiredTiger 引擎（預設）。
- **監控**：`mongostat`、`mongotop`、Atlas 圖表。監視連接（`connPoolStats`）、快取驅逐、I/O（`iostat`）。
- **備份**：`mongodump`/`mongorestore`，或 Atlas 快照。邏輯（JSON）與物理（文件）。
- **性能**：明智使用索引，限制投影，避免大型陣列。設置 `ulimit -n 64000`，禁用交換（`vm.swappiness=0`），調整 TCP keepalive。
- **擴展**：從副本集開始；在 >100GB 或高吞吐量時進行分片。
- **數據導入**：`mongoimport --db test --collection users --file users.json`。
- **工具**：MongoDB Compass（GUI）、mongosh（外殼）、應用程式的驅動程式。
- **常見陷阱**：過度嵌入（文件大小限制 16MB）、忽略索引、未處理複製延遲。

對於開發，使用 Atlas M0 免費層。使用 `mongoperf` 測試工作負載。

## 參考資料
- [MongoDB 手冊](https://www.mongodb.com/docs/manual/)
- [MongoDB 安裝](https://www.mongodb.com/docs/manual/installation/)
- [MongoDB 核心概念](https://www.mongodb.com/docs/manual/core/)
- [MongoDB CRUD](https://www.mongodb.com/docs/manual/crud/)
- [MongoDB 查詢](https://www.mongodb.com/docs/manual/tutorial/query-documents/)
- [MongoDB 索引](https://www.mongodb.com/docs/manual/indexes/)
- [MongoDB 聚合](https://www.mongodb.com/docs/manual/core/aggregation-pipeline/)
- [MongoDB 模式設計](https://www.mongodb.com/docs/manual/core/data-model-design/)
- [MongoDB 複製](https://www.mongodb.com/docs/manual/replication/)
- [MongoDB 分片](https://www.mongodb.com/docs/manual/sharding/)
- [MongoDB 安全性](https://www.mongodb.com/docs/manual/core/security/)
- [MongoDB 生產注意事項](https://www.mongodb.com/docs/manual/administration/production-notes/)