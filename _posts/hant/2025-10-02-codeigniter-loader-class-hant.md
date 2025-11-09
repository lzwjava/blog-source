---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: CodeIgniter 載入類別概覽
translated: true
type: note
---

以下將對提供的 PHP 程式碼片段進行清晰、結構化的說明。這似乎是 CodeIgniter PHP 框架（一個開源網頁框架）中的 `CI_Loader` 類別。CodeIgniter 旨在簡化常見的網頁開發任務，而 Loader 類別是負責載入和管理各種框架資源（例如模型、視圖、程式庫）的核心元件。我將逐步分解說明，包括其目的、關鍵組件、方法及運作方式。由於這是一個大型類別（超過 1,000 行），我將進行總結而非逐行分析，並盡可能避免使用技術術語以保持簡潔。

如果您是 CodeIgniter 或 PHP 框架的新手，可以將其視為應用程式的「調度器」或「匯入器」——它能動態載入檔案（如類別或視圖），而無需您在程式碼中手動引入。

### 1. **整體目的與背景**
   - **功能**：`CI_Loader` 類別是 CodeIgniter 中資源載入的核心。它允許您動態載入和實例化程式庫、模型、視圖、輔助函式、驅動程式等。例如，在控制器中，您可以透過 `$this->load->model('User_model')` 載入模型，並將其作為 `$this->User_model` 使用。
   - **存在原因**：雖然 PHP 的 `require_once` 可以運作，但像 CodeIgniter 這樣的框架能自動化檔案載入、處理命名慣例（例如類別名稱大寫）、管理路徑（例如應用程式與系統資料夾），並避免重複載入等錯誤，從而促進更乾淨、模組化的程式碼。
   - **定位**：它在框架生命週期早期實例化（透過 `CI_Controller::__construct()`），並與主控制器實例（`$CI =& get_instance()`）互動以附加載入的資源。
   - **授權與元數據**：標頭顯示其為 MIT 授權，版權歸 EllisLab Inc. 及其他方所有，並以 CodeIgniter（基於程式碼判斷為 3.x 版）發布。
   - **定義於**：`system/core/Loader.php`（在標準 CodeIgniter 安裝中）。

### 2. **類別結構與屬性**
   - **類別名稱**：`CI_Loader`。
   - **繼承**：未明確繼承任何類別——它獨立存在但與框架緊密整合。
   - **可見性**：大多數方法為 `public`（供使用者存取），部分為 `protected`（內部使用）。
   - **關鍵屬性**（均為 protected，用於儲存路徑和已載入項目）：
     - `$_ci_ob_level`：追蹤輸出緩衝層級（用於處理視圖的 PHP `ob_start()`）。
     - `$_ci_view_paths`、`$_ci_library_paths`、`$_ci_model_paths`、`$_ci_helper_paths`：用於搜尋檔案的路径陣列（例如 `APPPATH` 用於應用程式資料夾，`BASEPATH` 用於系統資料夾）。
     - `$_ci_classes`、`$_ci_models`、`$_ci_helpers`：追蹤已載入項目以避免重複。
     - `$_ci_cached_vars`：儲存傳遞給視圖的變數（透過 `vars()` 傳遞）。
     - `$_ci_varmap`：映射類別名稱（例如 `'unit_test' => 'unit'`）以保持向後兼容性。
   - **建構函式**：設定初始路徑並取得輸出緩衝層級。呼叫內部自動載入器初始化程式。
   - **繼承模式**：對大多數載入器使用 PHP 的動態實例化（例如 `new $class_name()`），而非固定的基礎類別。

### 3. **關鍵方法與功能**
該類別有許多方法，按主題分組如下：

#### **載入資源（公開方法）**
這些是開發者主要呼叫的 API：
   - **`library($library, $params, $object_name)`**：載入程式庫類別（例如 email、session）。若 `$library` 為陣列，則載入多個。處理子目錄並在控制器上實例化類別（`$CI->some_library`）。
   - **`model($model, $name, $db_conn)`**：載入模型類別（用於資料庫互動）。確保模型繼承 `CI_Model`。需要時可自動載入資料庫。
   - **`view($view, $vars, $return)`**：載入視圖檔案（PHP 模板）並輸出。傳遞變數，使用輸出緩衝以提升效能。搜尋路徑如 `APPPATH/views/`。
   - **`helper($helpers)`**：載入輔助函式（全域工具函式，如表單輔助函式）。包含基礎（系統）和應用層級的覆寫。
   - **`database($params, $return, $query_builder)`**：載入資料庫連接。可回傳物件或附加至 `$CI->db`。
   - **`driver($library, $params, $object_name)`**：類似 `library()`，但用於「驅動程式」（具有子驅動程式的程式庫，如 cache_db）。
   - **`config($file, $use_sections)`**：載入設定檔案（代理至設定元件）。
   - **`language($files, $lang)`**：載用於國際化的語言檔案（代理至語言元件）。
   - **`file($path, $return)`**：載入任意檔案（類似視圖，用於非視圖的 PHP 檔案）。

#### **變數與快取管理**
   - **`vars($vars, $val)`**：設定傳遞給視圖的變數（例如傳遞給模板的資料）。
   - **`get_var($key)`、`get_vars()`、`clear_vars()`**：檢索或清除快取的視圖變數。

#### **套件與路徑管理**
   - **`add_package_path($path, $view_cascade)`**：允許將自訂路徑（例如第三方套件）加入載入器的搜尋路徑。
   - **`remove_package_path($path)`**：移除路徑，重置為預設值（應用程式和基礎路徑）。
   - **`get_package_paths($include_base)`**：回傳目前路徑。

#### **內部/保護方法**
這些處理「幕後」工作：
   - **`_ci_load($_ci_data)`**：視圖/檔案的核心載入器。使用輸出緩衝、提取變數、引入檔案並記錄日誌。處理舊版 PHP 的短標籤重寫。
   - **`_ci_load_library($class, $params, $object_name)` 與 `_ci_load_stock_library(...)`**：尋找並載入程式庫檔案，檢查重複，並呼叫 `_ci_init_library()`。
   - **`_ci_init_library($class, $prefix, $config)`**：實例化類別，載入設定（例如 `libraries/config/somelib.php`），並附加至控制器。處理類別名稱映射。
   - **`_ci_autoloader()`**：在啟動時執行，自動載入 `config/autoload.php` 中的項目（例如套件、輔助函式）。
   - **工具方法**：`_ci_prep_filename()` 標準化檔案名稱（例如添加 `.php`），`_ci_object_to_array()` 將物件轉換為陣列以供視圖變數使用。

#### **事件/日誌掛鉤**
   - 使用 `log_message()` 記錄資訊/除錯/錯誤訊息（例如「Helper loaded」）。
   - 呼叫 `show_error()` 處理致命問題（例如遺失檔案）。

### 4. **運作方式：高層級流程範例**
1. **初始化**：建構函式設定路徑（例如應用程式和基礎資料夾）。`initialize()` 呼叫 `_ci_autoloader()` 以載入自動設定的項目（來自 `autoload.php`）。
2. **載入資源**（例如模型）：
   - 您呼叫 `$this->load->model('user_model')`。
   - 它解析名稱，檢查路徑（先 `APPPATH/models/` 後 `BASEPATH/models/`），找到檔案。
   - 引入檔案，確保其繼承 `CI_Model`，並將其實例化為 `$CI->user_model`。
   - 防止重複並處理子目錄（例如 `models/admin/user_model.php`）。
3. **視圖與輸出**：`view()` 緩衝輸出以允許後處理（例如添加頁面載入時間）。變數被提取並在視圖中全域可用。
4. **錯誤處理**：對問題（如遺失檔案或無效類別）拋出 `RuntimeException` 或呼叫 `show_error()`。
5. **路徑與靈活性**：支援級聯（先搜尋應用程式，後系統）和套件（例如 HMVC 模組）。

### 5. **關鍵特性與優勢**
   - **效能**：快取已載入項目，對視圖使用緩衝。
   - **靈活性**：處理自訂路徑、覆寫（例如應用層級程式庫優先於系統）和環境特定設定（透過 `ENVIRONMENT` 常數）。
   - **慣例優於設定**：自動大寫類別名稱，假設標準資料夾結構（`libraries/`、`models/`）。
   - **安全性**：限制於定義的路徑，避免任意引入。
   - **可擴展性**：可載入驅動程式（具有子驅動程式的程式庫）和輔助函式。
   - **PHP 兼容性**：處理 PHP 功能如短標籤或物件到陣列轉換。

### 6. **常見使用範例**
```php
// 在控制器中
$this->load->library('email');       // 載入 CI_Email，可作為 $this->email 使用
$this->load->model('User_model');    // 載入 User_model，可作為 $this->User_model 使用
$this->load->view('welcome', array('title' => 'Hello'));  // 渲染 views/welcome.php
$this->load->helper('url');          // 使 url_title() 等全域可用
$this->load->add_package_path(APPPATH.'third_party/some_package/');  // 添加自訂路徑
```

### 7. **潛在問題或注意事項**
   - **路徑**：若路徑錯誤（例如權限問題），載入會失敗。對自訂模組使用 `$this->add_package_path()`。
   - **重複**：不會重新載入相同項目——而是記錄除錯訊息。
   - **類別命名**：確保載入的類別與檔案名稱匹配（例如 `User_model.php` 宣告 `class User_model`）。
   - **PHP 版本**：使用如 `ob_get_level()` 等功能；對非常舊的 PHP（<5.4）可能需要調整。
   - **除錯**：檢查日誌中的「File loaded」或錯誤。啟用錯誤報告。

若此程式碼來自特定 CodeIgniter 版本（例如 3.x），行為可能在 4.x 中有所不同。如果您希望更詳細說明程式碼的特定部分（例如某個方法），或用於除錯/修改，請告知！有關官方文件，請參閱 CodeIgniter 使用者指南中關於載入資源的章節。