---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: CodeIgniter 路由指南
translated: true
type: note
---

### CodeIgniter 路由系統概覽

CodeIgniter 的路由系統讓你能將 URL（URI）映射到特定的控制器類別和方法，從而覆蓋預設的 URL 模式 `example.com/controller/method/id/`。這對於建立 SEO 友好的 URL、處理 RESTful API 或單純自訂請求處理方式非常有用。

提供的程式碼片段來自 CodeIgniter 的 `routes.php` 設定檔。它定義了一個關聯陣列 `$route`，其中每個鍵都是一個 URI 模式，而值則是一個字串（`controller/method`）或一個按 HTTP 方法（例如 GET、POST）指定不同行為的陣列。這種設定支援標準路由和方法特定路由。

我將根據 CodeIgniter 的標準行為以及你的程式碼範例，詳細說明**如何定義路由**、**路由如何運作**以及**如何使用路由**。完整詳情請參閱官方 CodeIgniter 使用者指南關於路由的章節：https://codeigniter.com/userguide4/general/routing.html。

#### 1. **如何定義路由**
路由在 `application/config/routes.php` 中定義為一個陣列。你可以將項目加入 `$route[]`。以下是語法：

- **基本路由**：將任何 HTTP 方法映射到控制器/方法。
  ```
  $route['uri_segment'] = 'controller/method';
  ```
  - 範例：`$route['login'] = 'users/login';` 表示任何對 `/login` 的請求都會路由到 `Users::login()`。

- **方法特定路由**：對於 RESTful API，你可以針對每個 HTTP 方法（GET、POST、PUT 等）指定不同的控制器/方法。這需要使用陣列。
  ```
  $route['uri_segment'] = array(
      'METHOD1' => 'controller/method1',
      'METHOD2' => 'controller/method2'
  );
  ```
  - 你的程式碼範例：`$route['self'] = array('POST' => 'users/update', 'GET' => 'users/self');` 表示：
    - POST 到 `/self` → `Users::update()`。
    - GET 到 `/self` → `Users::self()`。

- **萬用字元佔位符**：使用類似正規表示式的模式來捕捉 URL 的動態部分（作為參數傳遞給方法）。
  - `(:any)`：匹配任何字元（斜線除外）– 例如，slug 或字串。
  - `(:num)` 或 `(\d+)`：僅匹配數字 – 用於 ID。
  - 自訂正規表示式：用括號包圍，例如 `(foo|bar)` 用於特定匹配。
  - 你的程式碼範例：
    - `$route['users/(\d+)']['GET'] = 'users/one/$1';`：GET `/users/123` 路由到 `Users::one(123)`。
    - `$route['lives/(\d+)/notify'] = 'lives/notifyLiveStart/$1';`：任何方法到 `/lives/123/notify` 路由到 `Lives::notifyLiveStart(123)`。

- **保留路由**：
  - `$route['default_controller'] = 'welcome';`：如果未提供 URI（例如根 URL → `Welcome` 控制器）時載入的控制器。
  - `$route['404_override'] = 'errors/page_missing';`：用於未匹配路由的控制器/方法（自訂 404）。
  - `$route['translate_uri_dashes'] = FALSE;`：如果為 TRUE，將 URI 中的破折號轉換為底線以用於控制器/方法名稱（例如 `my-controller` → `my_controller`）。

- **順序很重要**：路由按照出現的順序進行匹配。將帶有萬用字元的特定路由定義在通用路由之前，以避免衝突。
- **HTTP 方法**：如果未指定，路由適用於所有方法。你的程式碼使用陣列來實現精確性，這對於 API 非常有用。

**在你的程式碼中定義路由的提示**：
- 在 `$route['translate_uri_dashes']` 之前，於末尾新增路由。
- 使用 Postman 等工具測試 API 路由，以確保觸及正確的控制器/方法。
- 對於複雜的應用程式，按部分對路由進行分組（如你使用註解 `// users` 所做的那樣）。

#### 2. **路由如何運作**
CodeIgniter 的路由器按以下順序處理每個傳入請求：
1. **解析 URI**：將 URL 分解為片段（例如 `/users/123/edit` → 片段：`users`、`123`、`edit`）。
2. **與路由匹配**：從上到下檢查 `$route` 陣列。它首先尋找完全匹配，然後是帶有萬用字元的模式。
   - 如果找到匹配，則映射到指定的控制器/方法，並將動態部分（例如 `123`）作為方法參數傳遞。
   - 如果沒有匹配，則回退到預設模式（`Controller::method/id/`）。
3. **載入控制器和方法**：CodeIgniter 實例化控制器，呼叫方法，並傳遞任何 URI 片段或捕獲的群組。
4. **方法特定處理**：如果路由是一個陣列（如你的程式碼所示），它會檢查請求中的 HTTP 方法（GET、POST 等）。
5. **回退**：未匹配的請求會觸發 404，或者如果設定了 `$route['404_override']` 則使用該設定。

**範例流程**：
- 請求：`POST https://example.com/lives`
- 匹配：`$route['lives']['POST'] = 'lives/create';`
- 結果：呼叫 `Lives::create()`，不帶參數。
- 如果請求是 `GET https://example.com/lives/456`，它將匹配 `$route['lives/(\d+)']['GET'] = 'lives/one/$1';` → `Lives::one(456)`。

**關鍵機制**：
- **動態參數**：捕獲的群組（例如 `$1`）作為參數傳遞給方法。確保你的控制器方法預期接收它們。
- **安全性**：路由通過隱藏 URL 來防止直接訪問敏感控制器。
- **效能**：簡單的陣列查找；除非你有數百個路由，否則沒有重大開銷。

#### 3. **如何使用路由**
使用路由意味著如上所述設定它們，然後在你的應用程式（控制器、視圖等）中利用它們。

- **在控制器中**：假設路由處理 URL 映射；編寫預期接收路由請求的方法。
  - 範例：對於 `$route['login']['POST'] = 'users/login';`，建立一個 `Users.php` 控制器，其中包含一個 `login()` 方法，該方法處理 POST 資料（例如透過 `$this->input->post()`）。

- **產生 URL**：使用 CodeIgniter 的 `site_url()` 或 `base_url()` 與你的路由鍵來產生連結/按鈕。
  - 範例：在視圖中，`<a href="<?= site_url('login'); ?>">Login</a>` 指向路由的 URL，但你的程式碼定義了它觸發哪個控制器。

- **測試路由**：
  - 使用你的網頁瀏覽器或 API 工具（例如 Postman）來訪問 URL，如 `/users/register`。
  - 如果路由失敗，檢查 `application/logs/log-{date}.php` 中的錯誤。
  - 加入除錯：暫時重設 `$route['404_override']` 並在測試控制器中使用 var_dump 來查看參數。

- **RESTful 用法（如你的程式碼所示）**：你的路由設定為類似 API 的結構。例如：
  - 建立資源：傳送 POST 到 `/lives` → 建立直播活動。
  - 讀取：GET `/lives/123` → 獲取直播活動 #123。
  - 更新：POST `/lives/123` → 更新直播活動 #123。

- **常見陷阱與提示**：
  - **重複**：避免重疊路由（例如 `lives` 和 `lives/(\d+)`）；將特定路由放在前面。
  - **未指定方法**：如果路由是字串，它適用於所有 HTTP 方法。使用陣列以實現精確性。
  - **用於開發**：在控制器中啟用 CodeIgniter 的 Profiler（`$this->output->enable_profiler(TRUE);`）來除錯路由。
  - **版本控制**：你的 routes.php 在版本控制中 – 更改會實時影響路由。
  - **擴充功能**：如果你需要進階功能（例如命名空間支援），請考慮使用 CodeIgniter 4 或第三方函式庫，因為 CI 3（你的程式碼）較舊。

如果你對你的檔案中的特定路由有疑問（例如為什麼使用 `(\d+)` 或如何新增一個新路由），請提供更多細節！對於 CodeIgniter 設定，請確保 `CI_VERSION` 在你的 index.php 中已定義。