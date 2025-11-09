---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: CodeIgniter 數據庫配置概述
translated: true
type: note
---

### CodeIgniter 資料庫配置概述

此 PHP 檔案是 CodeIgniter 資料庫連線的配置腳本。它定義了多個資料庫群組（例如 'default'、'lzwjava'、'leo66'、'testing'）的連線設定，讓應用程式能根據環境（開發、測試、生產）切換使用不同的配置。`$active_group` 變數決定了預設使用的連線群組。

關鍵組件：
- **$query_builder**：設為 `TRUE` 可啟用 Query Builder 類別載入，該類別提供以物件導向方式構建 SQL 查詢的功能。
- **$db[][]**：一個關聯陣列，其中每個子陣列（例如 'default'）包含資料庫連線的詳細配置選項。

`$active_group` 會根據 `ENVIRONMENT` 常數（例如透過 switch 語句）動態設定，確保不同部署階段使用不同設定。下面我將詳細解釋每個配置選項，參考自 CodeIgniter 的文件和標準用法。請注意，實際的敏感值（如憑證）在此為安全起見已省略；實務中應安全儲存這些值，例如透過環境變數。

### 詳細配置選項

每個資料庫群組都是一個包含以下鍵的陣列。大多數是直觀的設定，但有些（如 `encrypt`）支援進階功能的子選項。

- **dsn** (字串)：完整的資料來源名稱 (DSN) 字串，用於描述連線。這是分別指定 hostname、username 等欄位的替代方案。對於複雜設定（如 ODBC）非常有用。若提供，將覆蓋個別的主機/憑證欄位。格式範例：`'dsn' => 'mysql:host=yourhost;dbname=yourdatabase'`。

- **hostname** (字串)：資料庫伺服器的地址（例如 'localhost' 或 IP 如 '127.0.0.1'）。用於識別資料庫運行的位置，允許透過 TCP/IP 或 socket 進行連線。

- **username** (字串)：用於向資料庫伺服器進行身份驗證的帳戶名稱。應與資料庫管理系統中的有效使用者匹配。

- **password** (字串)：與使用者名稱配對用於身份驗證的密鑰。請務必安全儲存以防洩露。

- **database** (字串)：你要連線的伺服器上特定資料庫名稱。除非另有指定，否則所有查詢都將針對此資料庫。

- **dbdriver** (字串)：指定要使用的資料庫驅動程式（例如 MySQL 用 'mysqli'）。常見驅動程式包括 'cubrid'、'ibase'、'mssql'、'mysql'、'mysqli'、'oci8'、'odbc'、'pdo'、'postgre'、'sqlite'、'sqlite3' 和 'sqlsrv'。'mysqli' 是 MySQL 的現代、安全選擇。

- **dbprefix** (字串)：使用 CodeIgniter 的 Query Builder 時，可選的前綴會加到資料表名稱前（例如，若設為 'prefix_'，'mytable' 會變成 'prefix_mytable'）。這有助於在共享主機或多租戶應用中為資料表命名空間。

- **pconnect** (布林值)：啟用持久連線 (`TRUE`) 或常規連線 (`FALSE`)。持久連線會重複使用相同的連結，對高負載應用可提升效能，但過度使用可能耗盡伺服器資源。

- **db_debug** (布林值)：控制是否顯示資料庫錯誤 (`TRUE`) 以進行除錯。在生產環境中應停用 (`FALSE`)，避免向使用者洩露敏感的錯誤詳細資訊。

- **cache_on** (布林值)：啟用 (`TRUE`) 或停用 (`FALSE`) 查詢快取。啟用時，結果會被儲存以加速重複查詢。

- **cachedir** (字串)：快取查詢結果儲存目錄的檔案路徑。必須可由網頁伺服器寫入。與 `cache_on` 結合使用可減少資料庫負載。

- **char_set** (字串)：資料庫通訊的字元編碼（例如，現代 Unicode 支援用 'utf8mb4'）。確保多語言應用的資料完整性。

- **dbcollat** (字串)：用於排序和比較字元的校對規則（例如，不區分大小寫的 Unicode 用 'utf8mb4_unicode_ci'）。這在舊版 PHP/MySQL 中作為後備機制；否則會被忽略。

- **swap_pre** (字串)：用於動態替換 `dbprefix` 的資料表前綴。對於在現有應用中交換前綴而無需重新命名資料表非常有用。

- **encrypt** (布林值或陣列)：用於加密支援。對於 'mysql'（已棄用）、'sqlsrv' 和 'pdo/sqlsrv'，使用 `TRUE`/`FALSE` 來啟用/停用 SSL。對於 'mysqli' 和 'pdo/mysql'，使用帶有 SSL 子選項的陣列：
  - 'ssl_key'：私鑰檔案的路徑（例如，用於客戶端憑證）。
  - 'ssl_cert'：公鑰憑證檔案的路徑。
  - 'ssl_ca'：憑證授權檔案的路徑（驗證伺服器憑證）。
  - 'ssl_capath'：PEM 格式受信任 CA 憑證目錄的路徑。
  - 'ssl_cipher'：允許的加密演算法清單，以冒號分隔（例如 'AES128-SHA'）。
  - 'ssl_verify'：僅適用於 'mysqli'；`TRUE` 表示驗證伺服器憑證，`FALSE` 表示跳過（安全性較低；用於自簽憑證）。

- **compress** (布林值)：啟用 MySQL 連線的客戶端壓縮，減少網路流量（僅適用於 MySQL；其他驅動程式會忽略）。

- **stricton** (布林值)：強制使用 'Strict Mode' 連線 (`TRUE`)，強制執行嚴格的 SQL 規則以早期捕獲錯誤（例如，無效的資料類型）。在開發期間很有用。

- **ssl_options** (陣列)：用於 'pdo' 等驅動程式的高級 SSL 配置選項。允許微調 `encrypt` 未涵蓋的加密參數。

- **failover** (陣列)：備份連線陣列，當主要連線失敗時自動切換。每個元素都鏡像主配置（例如，替代主機名/端口）。範例：`array(array('hostname' => 'backuphost', ...))`。

- **save_queries** (布林值)：在記憶體中儲存已執行的查詢以供除錯 (`TRUE`)。提供對 `$this->db->last_query()` 等方法存取，但可能增加記憶體使用；在生產環境中停用 (`FALSE`) 以節省資源。

### 資料庫群組與環境切換

- **default**：基礎配置陣列，作為範本。設定為 'production' 預設值（例如，無除錯、安全設定）。
- **lzwjava**：繼承基礎配置，但覆蓋使用者名為不同值（密碼留空，表示無需驗證或使用預設值）。
- **leo66**：繼承基礎設定，但將主機名更改為本地迴環，使用者名/密碼設為預設值，並添加端口（3306，MySQL 標準端口）。
- **testing**：專用於測試環境的群組；繼承基礎配置。

`switch` 語句根據 `ENVIRONMENT` 啟動相應群組：
- 開發環境：使用 'lzwjava'。
- 測試環境：使用 'testing'。
- 生產環境：使用 'default'。

此設定促進了本地開發、測試和線上部署的靈活性。請務必清理輸入以防止 SQL 注入，並考慮將憑證移至環境變數以確保安全。完整文件請參考 CodeIgniter 官方使用者指南中的資料庫連線部分。如果你有特定選項或群組需要澄清，請告訴我！