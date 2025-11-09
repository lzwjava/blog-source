---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: CodeIgniter REST API 配置指南
translated: true
type: note
---

以下將提供清晰逐步指南，協助理解與使用您分享的 CodeIgniter REST API 配置檔案（`application/config/rest.php`）。此檔案用於配置 REST_Controller 函式庫（一套在 CodeIgniter 中建構 RESTful API 的熱門 PHP 函式庫，例如 Phil Sturgeon 的 REST 函式庫，現已成為部分 CodeIgniter 框架版本的維護組件）的行為。

我將說明：
- 此函式庫的功能與關鍵前置條件
- 如何設定與使用
- 您配置檔案中的關鍵選項（附範例）
- 簡易使用範例
- 常見陷阱與安全性的實用技巧

若您的問題針對特定面向（例如身份驗證或限制），請進一步說明以獲得更精準的建議！

### 1. **前置條件與設定**
   - **這是什麼？** 這是 CodeIgniter（PHP 框架）的 REST_Controller 函式庫。它讓您能透過將控制器繼承自 `REST_Controller` 來建構 RESTful API（例如響應 GET/POST 請求並回傳 JSON/XML 的端點）。您的配置檔案控制全域設定，如身份驗證、響應格式、速率限制與安全性。

   - **需求：**
     - CodeIgniter 3.x（或相容版本；此配置適用於舊版 3.x 左右）
     - 若尚未安裝 REST_Controller 函式庫，請進行安裝（可從 GitHub 下載：`chriskacerguis/codeigniter-restserver`）。將函式庫檔案置於 `application/libraries/` 並在 `application/config/autoload.php` 中自動載入：
       ```php
       $autoload['libraries'] = ['rest_controller'];
       ```
     - 資料庫設定（選用；需用於 API 金鑰、記錄或限制等功能）。執行配置註解中提供的 SQL 結構描述（例如用於 `keys`、`logs`、`access`、`limits` 等資料表）
     - 在 CodeIgniter 中啟用簡潔網址（`application/config/routes.php`）以獲得整潔的 API 端點，如 `/api/users`
     - 您的 `rest.php` 配置檔案應置於 `application/config/` 並在 `application/config/autoload.php` 中自動載入：
       ```php
       $autoload['config'] = ['rest'];
       ```

   - **基本安裝步驟：**
     1. 下載並解壓縮 CodeIgniter
     2. 加入 REST_Controller 函式庫檔案
     3. 將您提供的 `rest.php` 複製到 `application/config/`
     4. 在 `routes.php` 中設定路由（例如 `$route['api/(:any)'] = 'api/$1';` 以將 `/api/users` 對應至控制器）
     5. 建立 API 控制器（參見下方範例）
     6. 使用 Postman 或 curl 等工具測試

### 2. **關鍵配置選項**
我將根據用途分組，總結您配置檔案中的主要設定。這些設定控制全域行為，您可依需求調整（例如啟用 HTTPS 或變更預設格式）

- **通訊協定與輸出：**
  - `$config['force_https'] = FALSE;`：強制所有 API 呼叫使用 HTTPS。為確保生產環境安全性，請設為 `TRUE`
  - `$config['rest_default_format'] = 'json';`：預設響應格式（選項：json、xml、csv 等）。請求可透過網址覆寫（例如 `/api/users.format=xml`）
  - `$config['rest_supported_formats']`：允許的格式清單。為確保安全性，請移除不需要的格式
  - `$config['rest_ignore_http_accept'] = FALSE;`：忽略客戶端 HTTP Accept 標頭以加速響應（若您在程式碼中始終使用 `$this->rest_format` 會很有用）

- **身份驗證（安全性）：**
  - `$config['rest_auth'] = FALSE;`：主要驗證模式。選項：
    - `FALSE`：無需驗證
    - `'basic'`：HTTP 基本驗證（base64 編碼的使用者名稱/密碼置於標頭）
    - `'digest'`：更安全的摘要驗證
    - `'session'`：檢查 PHP 會話變數
  - `$config['auth_source'] = 'ldap';`：驗證憑證的來源（例如配置陣列、LDAP、自訂函式庫）
  - `$config['rest_valid_logins'] = ['admin' => '1234'];`：簡易使用者名稱/密碼陣列（若使用 LDAP 則忽略此項）
  - `$config['auth_override_class_method']`：為特定控制器/方法覆寫驗證（例如 `'users' => 'view' => 'basic'`）
  - `$config['auth_library_class/function']`：若使用自訂函式庫，請指定驗證的類別/方法
  - IP 控制：
    - `$config['rest_ip_whitelist_enabled/blacklist_enabled']`：基於 IP 的 API 過濾
    - 適用於限制存取（例如將您應用程式的 IP 加入白名單）

- **API 金鑰（選用安全層）：**
  - `$config['rest_enable_keys'] = FALSE;`：啟用 API 金鑰檢查（儲存於資料表 `keys`）。客戶端必須在標頭中傳送金鑰（例如 `X-API-KEY`）
  - `$config['rest_key_column/name/length']`：自訂金鑰欄位與標頭名稱
  - 搭配 `$config['rest_enable_access']` 可限制金鑰僅用於特定控制器/方法

- **記錄與限制：**
  - `$config['rest_enable_logging/limits'] = FALSE;`：啟用基於資料庫的請求記錄（URI、參數等）或速率限制（例如每個金鑰每小時 X 次呼叫）
  - 資料表：`logs`、`limits`（執行註解中的 SQL 以建立資料表）
  - `$config['rest_limits_method']`：應用限制的方式（依 API 金鑰、網址等）
  - 在控制器中為每個方法自訂（例如 `$this->method['get']['limit'] = 100;`）

- **其他：**
  - `$config['rest_ajax_only'] = FALSE;`：僅限 AJAX 請求（否則回傳 505 錯誤）
  - `$config['rest_language'] = 'english';`：錯誤訊息的語言

修改方式：編輯 `rest.php` 並重啟應用程式。請謹慎測試變更！

### 3. **使用方式：逐步操作指南**
設定完成後，透過建構繼承自 `REST_Controller` 的控制器來建立 API 端點。以下是高階流程：

1. **建立控制器：**
   - 在 `application/controllers/` 中建立 `Api.php`（或針對特定資源建立 `Users.php`）：
     ```php
     <?php
     defined('BASEPATH') OR exit('No direct script access allowed');
     require_once(APPPATH . 'libraries/REST_Controller.php');

     class Api extends REST_Controller {
         public function __construct() {
             parent::__construct();
             // 選用：為每個方法設定驗證與限制
             $this->load->database();
             $this->method['index_get']['limit'] = 100; // 100 次請求/小時
         }

         // GET /api
         public function index_get() {
             $data = ['message' => '歡迎使用 API', 'status' => 'success'];
             $this->response($data, REST_Controller::HTTP_OK);
         }

         // POST /api/users
         public function users_post() {
             $data = $this->input->post(); // 取得 POST 資料
             if (empty($data['name'])) {
                 $this->response(['error' => '姓名為必填欄位'], REST_Controller::HTTP_BAD_REQUEST);
             }
             // 處理（例如新增至資料庫）
             $this->response(['message' => '使用者已建立'], REST_Controller::HTTP_CREATED);
         }

         // PUT /api/users/{id}
         public function users_put($id) {
             $data = $this->put(); // 取得 PUT 資料
             // 更新 ID 為 $id 的使用者
             $this->response(['message' => '使用者已更新'], REST_Controller::HTTP_OK);
         }

         // 其餘 DELETE 等方法
     }
     ```

2. **傳送請求：**
   - 使用任何 HTTP 客戶端：
     - GET：`curl http://yourdomain.com/api` → 回傳 JSON {"message": "歡迎使用 API", "status": "success"}
     - POST：`curl -X POST http://yourdomain.com/api/users -d "name=John"` → 建立使用者
   - 若使用身份驗證/金鑰，請包含標頭（例如 `Authorization: Basic base64(user:pass)` 或 `X-API-KEY: yourkey`）

3. **測試與除錯：**
   - 檢查 CodeIgniter 記錄以找出錯誤
   - 若身份驗證失敗，請確認憑證設定正確
   - 對於限制/記錄，請查詢您的資料表

### 4. **常見技巧與最佳實踐**
- **安全性：** 在生產環境中務必使用 HTTPS（`force_https = TRUE`）。若對外部客戶端開放，請啟用金鑰。為防止 SQL 注入，請清理輸入資料
- **錯誤處理：** 響應包含 `status` 與 `error` 欄位（可在配置中自訂）。使用 CodeIgniter 的分析器進行除錯
- **效能：** 若啟用記錄/限制，您的資料庫將處理查詢——請監控緩慢效能
- **升級：** 此配置適用於舊版 CodeIgniter。對於 CI 4，請使用其內建的 API 資源（此設定可能需要調整）
- **疑難排解：**
  - 「無響應」？請檢查路由、自動載入與函式庫路徑
  - 身份驗證問題？請確認 `$auth_source` 與憑證
  - 格式錯誤？請確保您的格式位於 `rest_supported_formats` 中
- **資源：** 文件請參閱 codeigniter-restserver.org。遷移至 CI4 請參閱官方文件

若此回答未完全解決您的問題，或您需要特定使用情境的程式碼（例如啟用 OAuth），請提供更多細節！