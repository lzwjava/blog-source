---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: CodeIgniter 自動加載系統概覽
translated: true
type: note
---

### CodeIgniter 自動載入系統概覽

在 CodeIgniter（一個 PHP 框架）中，`autoload.php` 檔案（通常位於 `application/config/autoload.php`）允許你指定在每個請求中應自動載入的資源。這使得常用元件無需在每個控制器或其他地方手動載入即可使用，從而提高效率並減少程式碼重複。框架會在初始化過程中、路由請求之前載入這些資源。

該檔案定義了一個 `$autoload` 陣列，其中包含針對不同資源類型的子陣列：套件、程式庫、驅動程式、輔助函式、設定檔、語言檔案和模型。你可以在這些陣列中填入要自動載入的資源名稱。取消註解或修改這些行以啟用載入；留空則跳過。

### 實際運作方式

CodeIgniter 的啟動流程（透過 `index.php` 和 CI 核心）在系統初始化期間檢查此檔案。它會遍歷 `$autoload` 陣列，並透過以下方式載入每個指定的資源：
- 在適當的目錄中尋找檔案（例如，核心程式庫在 `system/libraries/`，自訂程式庫在 `application/libraries/`）。
- 實例化類別（用於程式庫/模型）或引入檔案（用於輔助函式/設定檔）。
- 使它們全域可用（例如，程式庫可透過控制器中的 `$this->library_name` 存取）。

如果找不到資源，可能會導致錯誤——請確保路徑和名稱正確。如有需要，你稍後可以使用像 `$this->load->library('session')` 這樣的方法手動載入其他項目。

### 檔案中各區段詳解

以下是根據提供的程式碼進行的逐區段解釋。我包含了每個陣列的作用、使用說明和範例。預設值大多為空，以保持框架輕量。

#### 1. 自動載入套件
```php
$autoload['packages'] = array();
```
- **目的**：載入第三方套件。這些通常是可重用的程式庫/輔助函式/模型集合，通常位於像 `APPPATH.'third_party'` 或自訂路徑的子目錄中。
- **運作方式**：將指定的目錄加入套件路徑陣列。CodeIgniter 隨後將在這些路徑中搜尋 `MY_` 前綴的類別並按需載入。
- **用法**：範例：`$autoload['packages'] = array(APPPATH.'third_party', '/usr/local/shared');` – 取代像 `$this->load->add_package_path()` 這樣的呼叫中的路徑。
- **注意**：預設為空；對於在不修改核心的情況下擴展框架非常有用。

#### 2. 自動載入程式庫
```php
$autoload['libraries'] = array();
```
- **目的**：載入類別程式庫（例如，會話管理、電子郵件等）。
- **運作方式**：從 `system/libraries/` 或 `application/libraries/` 載入並實例化類別。常見的包括 'database'、'session'、'email'。
- **用法**：範例：`$autoload['libraries'] = array('database', 'email', 'session');` 或使用別名如 `$autoload['libraries'] = array('user_agent' => 'ua');`（允許使用 `$this->ua` 而非 `$this->user_agent`）。
- **注意**：Database 較特殊——載入它會自動連線。避免過度自動載入以最小化記憶體使用。

#### 3. 自動載入驅動程式
```php
$autoload['drivers'] = array();
```
- **目的**：載入基於驅動程式的程式庫，這些程式庫提供多個可互換的實作（例如，快取、圖片處理）。
- **運作方式**：`CI_Driver_Library` 的子類別。載入驅動程式類別及其子目錄。
- **用法**：範例：`$autoload['drivers'] = array('cache');` – 載入 `system/libraries/Cache/drivers/cache_apc_driver.php` 或類似檔案。
- **注意**：驅動程式是模組化的；你可以在執行時指定使用哪個驅動程式（例如，`$this->cache->apc->save()`）。

#### 4. 自動載入輔助函式檔案
```php
$autoload['helper'] = array('base');
```
- **目的**：載入輔助函式（PHP 函式庫，例如用於 URL、檔案、表單）。
- **運作方式**：引入檔案（例如，`application/helpers/base_helper.php`），使其函式全域可用。
- **用法**：範例：`$autoload['helper'] = array('url', 'file');` – 允許呼叫 `site_url()` 而無需手動載入輔助函式。
- **注意**：在你的檔案中，'base' 是自動載入的——請確保 `base_helper.php` 存在。

#### 5. 自動載入設定檔
```php
$autoload['config'] = array();
```
- **目的**：載入預設 `config.php` 之外的自訂設定檔。
- **運作方式**：將其他設定（例如，`application/config/custom.php`）合併到全域設定陣列中。
- **用法**：範例：`$autoload['config'] = array('custom', 'seo');` – 將 `custom.php` 和 `seo.php` 作為設定檔載入。
- **注意**：如果使用預設值則留空；對於站點特定設定非常有用。

#### 6. 自動載入語言檔案
```php
$autoload['language'] = array();
```
- **目的**：載用於國際化的語言陣列。
- **運作方式**：從 `application/language/english/`（或當前語言）載入檔案，例如 `form_lang.php`。
- **用法**：範例：`$autoload['language'] = array('form', 'calendar');` – 載入 `form_lang.php`（無需 '_lang' 後綴）。
- **注意**：語言會從設定中自動偵測；很少需要全域載入。

#### 7. 自動載入模型
```php
$autoload['model'] = array('BaseDao');
```
- **目的**：載入用於資料庫互動的模型類別。
- **運作方式**：從 `application/models/` 載入並實例化，例如 `BaseDao.php`。
- **用法**：範例：`$autoload['model'] = array('user_model', 'BaseDao' => 'base');` – 允許使用 `$this->base` 作為別名。
- **注意**：在你的檔案中，'BaseDao' 是自動載入的——請確保它是一個有效的模型類別。

### 使用提示
- **編輯檔案**：修改 `autoload.php` 以添加項目。更改後進行測試以確保沒有衝突。
- **效能**：自動載入所有內容可能會減慢請求速度；僅載入全域需要的內容。
- **手動載入**：如果某項目未自動載入，請在控制器中使用 `$this->load->library('name');` 或類似方法。
- **版本說明**：這適用於 CodeIgniter 2.x/3.x。在 4.x 中，自動載入轉向基於 Composer（命名空間），但此類設定檔在舊版本中仍在使用。

如果你有關於添加項目或疑難排解錯誤的具體問題，請提供更多詳細資訊！