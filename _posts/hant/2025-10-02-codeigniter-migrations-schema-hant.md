---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: CodeIgniter 遷移數據庫架構管理
translated: true
type: note
---

### 什麼是 CodeIgniter Migrations？

CodeIgniter（CI）Migrations 是一項功能，可協助以版本控制的方式管理資料庫結構描述變更，類似於 Flyway 或 Liquibase 等工具。它允許您編寫 PHP 腳本來定義資料庫變更（例如建立資料表、新增欄位或修改資料），然後按順序執行這些腳本，以確保在不同環境中結構描述保持最新。這能避免手動 SQL 錯誤並支援回滾。

Migrations 的運作方式如下：
- 將遷移檔案儲存在目錄中（預設為 `application/migrations/`）。
- 在資料庫的資料表中追蹤「版本」，以了解哪些遷移已被應用。
- 根據需求向前（up）或向後（down）執行腳本。

您分享的設定檔（`migration.php`）控制遷移的行為。它使用 PHP 陣列來設定選項。下面，我將透過範例解釋關鍵設定。

### 關鍵配置設定

| 設定 | 您的程式碼中的值 | 說明 | 運作方式 |
|---------|---------------------|-------------|-------------|
| `migration_enabled` | `FALSE` | 全域啟用或停用遷移。當設為 `FALSE` 時，無法執行遷移（出於安全考慮，因為它們會修改資料庫）。 | CI 在執行任何遷移命令前會檢查此設定。在開發期間設為 `TRUE`，然後在生產環境中設回 `FALSE`。範例：若啟用，可透過控制器中的 `$this->migration->current()` 執行。 |
| `migration_type` | `'timestamp'` | 檔案命名風格：`'sequential'`（例如 `001_add_blog.php`）或 `'timestamp'`（例如 `20121031104401_add_blog.php`）。建議使用時間戳以獲得更好的版本控制。 | 檔案按時間順序載入。時間戳使用 `YYYYMMDDHHIISS` 格式（例如 `20121031104401` 表示 2012 年 10 月 31 日 10:44:01）。 |
| `migration_table` | `'migrations'` | 用於追蹤已應用遷移的資料表名稱。必需。 | 如果此資料表不存在，CI 會建立它。它儲存最新的遷移版本。刪除或更新此資料表會重設遷移歷史。 |
| `migration_auto_latest` | `FALSE` | 如果設為 `TRUE` 且 `migration_enabled` 為 `TRUE`，則在 Migration 程式庫載入時（例如頁面載入時）自動執行遷移至最新版本。 | 在開發環境中很有用，可自動同步結構描述。設為 `FALSE` 可手動執行遷移以獲得控制（在生產環境中更安全）。 |
| `migration_version` | `0` | 要遷移到的目標版本/編號。設定為檔案名稱前綴（例如 `20121031104401`）。`0` 表示未應用任何遷移。 | 執行 `$this->migration->version(20121031104401)` 會遷移到該版本。用於目標回滾——負數表示降級。 |
| `migration_path` | `APPPATH.'migrations/'` | 儲存遷移檔案的目錄。`APPPATH` 是 CI 常量，指向 `application/`。 | CI 掃描此資料夾中符合命名約定的 PHP 檔案。必須可由網頁伺服器寫入。可使用自訂路徑，如 `BASEPATH.'custom/migrations/'`。 |

### 如何使用 Migrations（逐步指南）

1. **啟用 Migrations**：在設定檔中暫時設定 `$config['migration_enabled'] = TRUE;`。

2. **建立遷移檔案**：在 `application/migrations/` 中新增一個 PHP 檔案，名稱類似 `20121031104401_add_blog.php`。內部使用 CI 的 Migration 類別：
   ```php
   defined('BASEPATH') OR exit('No direct script access allowed');

   class Migration_Add_blog extends CI_Migration {
       public function up() {
           $this->dbforge->add_field('id');
           $this->dbforge->create_table('blogs');
       }

       public function down() {
           $this->dbforge->drop_table('blogs');
       }
   }
   ```
   - `up()` 應用變更（例如建立資料表）。
   - `down()` 還原變更（例如刪除資料表）。

3. **執行遷移**：
   - 載入程式庫：`$this->load->library('migration');`
   - 遷移至最新版本：`$this->migration->current();`
   - 遷移至特定版本：`$this->migration->version('20121031104401');`
   - 從命令列執行（若啟用 CLI）：`php index.php migrate current`

4. **常用指令**：
   - `$this->migration->latest()`：`current()` 的別名。
   - `$this->migration->find_migratables()`：列出可用檔案。
   錯誤會記錄到 CI 的日誌檔案或拋出例外。

5. **最佳實踐**：
   - 保持遷移的冪等性（可安全重新執行）。
   - 先在開發環境測試；避免在生產環境啟用自動遷移，以防止意外的結構描述變更。
   - 如果資料庫支援，請使用交易以確保變更的原子性。
   - 使用後停用：設回 `FALSE` 以確保安全。

如果您遇到問題（例如路徑權限），請檢查 CI 的日誌或文件：[codeigniter.com/user_guide/libraries/migration.html](https://codeigniter.com/user_guide/libraries/migration.html)。請提供您的 CI 版本以獲得更有針對性的建議！