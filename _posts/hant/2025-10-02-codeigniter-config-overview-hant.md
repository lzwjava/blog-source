---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: CodeIgniter 設定檔案概覽
translated: true
type: note
---

### 檔案說明
這是 [CodeIgniter 框架](https://codeigniter.com/)（一個流行的 PHP 網頁應用程式框架，目前已有 3.x 或 4.x 等後續版本，但根據語法和註解判斷，此檔案似乎來自較舊版本）中的 `config.php` 檔案。它定義了 CodeIgniter 用於處理 URL、日誌記錄、會話、安全性等多個方面的各種配置設定。這些設定會在框架執行初期載入，以便自訂應用程式的運行方式。

該檔案通常位於 CodeIgniter 專案的 `application/config/config.php` 路徑中。它並非直接「運行」的檔案——而是會在應用程式啟動時由 CodeIgniter 自動載入。

接下來我將分節解析關鍵設定項目，說明其功能與用途。為了清晰起見，我已將它們分組整理，重點關注最重要的設定。部分章節包含內嵌程式碼（例如用於除錯邏輯的自訂函數），這在條件化設定的配置檔案中相當常見。

### 關鍵章節與說明

1. **基礎 URL 配置**
   - `$config['base_url'] = '';`
   - 設定網站的根 URL（例如 `'http://example.com/'`）。若留空，CodeIgniter 會自動推測，但建議在正式環境中明確設定以避免問題。
   - **用途**：確保生成的 URL（如連結或重新導向）正確無誤。

2. **索引檔案與 URI 協定**
   - `$config['index_page'] = 'index.php';` – 前端控制器檔案（若使用 URL 重寫隱藏則留空）。
   - `$config['uri_protocol'] = 'REQUEST_URI';` – 決定框架如何從伺服器全域變數讀取 URL。
   - **用途**：控制 URL 的解析與處理方式，特別是在路由方面。

3. **URL 與字元處理**
   - `$config['url_suffix'] = '';` – 為生成的 URL 添加尾碼（例如 .html）。
   - `$config['permitted_uri_chars'] = 'a-z 0-9~%.:_-';` – 定義 URL 中允許的字元以提升安全性（防止注入攻擊）。
   - **用途**：強化安全性並塑造 URL 結構。

4. **語言與字元集設定**
   - `$config['language'] = 'english';` – 錯誤訊息和語言檔案載入的預設語言。
   - `$config['charset'] = 'UTF-8';` – 使用的字元編碼（對多語言或特殊字元支援至關重要）。
   - **用途**：處理本地化與編碼相關事宜。

5. **掛鉤、擴充與自動載入**
   - `$config['enable_hooks'] = FALSE;` – 啟用自訂「掛鉤」（在特定時間點執行的程式碼）。
   - `$config['subclass_prefix'] = 'Base';` – 擴充核心類別時使用的前綴詞。
   - `$config['composer_autoload'] = FCPATH . 'vendor/autoload.php';` – 指向 Composer 的自動載入器以載入第三方函式庫。
   - **用途**：允許擴充框架行為並載入外部程式碼。

6. **查詢字串與 URI 處理**
   - `$config['allow_get_array'] = TRUE;` – 允許存取 `$_GET` 陣列。
   - `$config['enable_query_strings'] = FALSE;` – 切換至查詢字串形式的 URL（例如使用 `?c=controller&m=function` 而非分段式結構）。
   - **用途**：為 REST 或非標準路由提供彈性的 URL 處理方式。

7. **錯誤日誌記錄**
   - `$config['log_threshold']` – 開發環境設為 2（除錯模式），正式環境設為 1（僅錯誤）。自訂函數 `isDebug()` 會檢查 `ENVIRONMENT` 常數。
   - `$config['log_path']` – 日誌儲存路徑（開發環境使用應用程式目錄，正式環境使用絕對路徑）。
   - `$config['log_file_extension']`、`$config['log_file_permissions']`、`$config['log_date_format']` – 日誌檔案相關細節。
   - **用途**：控制除錯/正式環境的日誌記錄級別與儲存位置。

8. **快取設定**
   - `$config['cache_path'] = '';` – 輸出快取的儲存目錄（預設為 `application/cache/`）。
   - `$config['cache_query_string'] = FALSE;` – 是否根據查詢字串進行快取。
   - **用途**：透過輸出快取提升效能。

9. **加密與安全性**
   - `$config['encryption_key'] = '';` – 用於資料加密的金鑰（必須設定以確保安全性）。
   - CSRF 設定（例如 `$config['csrf_protection'] = FALSE;`）– 透過要求令牌防範跨站請求偽造攻擊。
   - XSS 過濾：`$config['global_xss_filtering'] = FALSE;` – 已棄用的全域 XSS 防護功能（現由輸入類別處理）。
   - **用途**：保護敏感資料與表單提交安全。

10. **會話與 Cookie 設定**
    - 會話設定：驅動程式（`files`）、過期時間（7200 秒/2 小時）、儲存路徑等。
    - Cookie 設定：網域、路徑、安全標誌等。
    - **用途**：管理用戶會話與 Cookie 狀態（例如登入持續性）。

11. **其他雜項設定**
    - `$config['compress_output'] = FALSE;` – Gzip 壓縮以加速載入。
    - `$config['time_reference'] = 'local';` – 時區處理方式。
    - `$config['proxy_ips'] = '';` – 反向代理的白名單 IP。
    - `$config['standardize_newlines'] = FALSE;` – 跨作業系統統一換行符號。
    - `$config['rewrite_short_tags'] = FALSE;` – 轉換短 PHP 標籤（已棄用語法）。
    - 結尾的 `__autoload($class)` 函數：用於基礎控制器/函式庫的自訂自動載入器（在現代 PHP 中已棄用，建議改用 Composer 或 PSR-4）。

### 這些設定是否僅適用於 PHP CodeIgniter，還是網頁伺服器也常見？

- **主要針對 CodeIgniter 特定**：大多數設定（例如 `base_url`、`uri_protocol`、`permitted_uri_chars`、`subclass_prefix`、日誌記錄閾值）都是為 CodeIgniter 的架構量身訂製。它們在其他 PHP 框架（如 Laravel、Symfony）或純 PHP 腳本中並不存在或無法運作。CodeIgniter 具有高度規範性，因此此配置檔案是框架運作的核心——若缺少它，框架將無法以標準化方式處理 URL、日誌記錄、會話等功能。任何基於 CodeIgniter 的專案都需要類似檔案。

- **部分概念在網頁伺服器/PHP 應用程式中普遍存在**：
  - **日誌記錄路徑與閾值**：許多 PHP 應用程式和網頁伺服器（例如 Apache 的 `ErrorLog` 或 Nginx 的 `error_log`）會處理日誌記錄，但 CodeIgniter 的日誌設定屬於應用層級。其他框架中也可見類似概念（例如 Laravel 的日誌配置）。
  - **會話與 Cookie**：PHP 原生的會話處理（`session_start()`、`setcookie()`）與此處功能重疊，且大多數網頁應用程式都需要這些功能來維持用戶狀態。Apache 或 Nginx 等網頁伺服器可能以類似方式處理反向代理，但實作細節有所不同。
  - **安全性（加密、CSRF、XSS）**：在安全的網頁應用程式中很常見（例如 Express.js 或 Spring 中的基於令牌的 CSRF 防護），但具體實作取決於框架。
  - **自動載入**：PHP 的自動載入功能是通用的（透過 `spl_autoload_register()` 或 Composer），但此處的 `__autoload()` 屬於舊式且專屬於 CodeIgniter。現代 PHP/PSR 標準（由 Composer 使用）在各種專案中更為常見。
  - **URL 與路由**：大多數框架都有基礎 URL 配置，但此處設定與 CodeIgniter 的路由器緊密相關。網頁伺服器通常以不同方式處理 URL 重寫（例如透過 Apache 的 `.htaccess`）。
  - **快取與壓縮**：輸出快存在 PHP 框架中很常見；壓縮則是伺服器層級的功能（例如 Apache 的 `mod_deflate`），但 CodeIgniter 提供了應用層級的控制。

總結來說，此配置檔案對 **CodeIgniter 至關重要**，但並非「網頁伺服器」配置。它屬於框架的應用層級設定。若未使用 CodeIgniter，則不需要此檔案——其他框架擁有各自的配置（例如 Laravel 的 `config/app.php`）。對於「純」網頁伺服器，相關設定（例如日誌記錄）應在伺服器配置檔案中進行（如 Apache 的 `httpd.conf`），而非在 PHP 中設定。

如果您有特定環境（例如部署至 Apache）或 CodeIgniter 版本需求，我可以提供更針對性的建議！您對此檔案的具體目標是什麼？