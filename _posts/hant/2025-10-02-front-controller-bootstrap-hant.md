---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: CodeIgniter 前端控制器啟動流程
translated: true
type: note
---

您提供的 PHP 程式碼是使用 CodeIgniter（一個開源 PHP 框架）建構的網頁應用程式的主要入口點（通常是 `index.php`）。這個腳本充當「前端控制器」，負責啟動（初始化）框架、處理傳入的 HTTP 請求，並將它們路由到應用程式的適當部分。它不直接渲染網頁——其工作是設定一切，以便框架的其餘部分（以及您的程式碼）能夠完成其工作。

我將根據程式碼逐步分解其運作方式。這是一個高層次的流程說明；CodeIgniter 專為效能、安全性和模組化而設計，因此它會漸進式載入元件並使用物件導向原則。如果您是 CodeIgniter 的新手，可以將其視為在音樂會開始前讓樂團準備就緒的「指揮」。

### 1. **初始檢查與常數**
   - **CodeIgniter 版本**：它定義了 `CI_VERSION`（例如，這裡是 '3.0.2'），用於追蹤框架版本。
   - **檢查直接存取**：`defined('BASEPATH') OR exit('No direct script access allowed');` 防止任何人透過 URL 直接存取此檔案（一種保護敏感程式碼的安全措施）。
   - **載入常數**：它包含設定檔以獲取常數（例如 `APPPATH.'config/'.ENVIRONMENT.'/constants.php'` 和 `APPPATH.'config/constants.php'`）。這些定義了路徑、設定和其他全域變數。
   - **載入全域函數**：引入 `BASEPATH.'core/Common.php'`，其中包含在整個框架中使用的實用函數（例如，用於載入類別或錯誤處理）。

### 2. **安全程序**
   - **PHP 版本檢查**：確保運行的是 PHP 5.4 或更高版本。
   - **安全調整**：
     - 停用 `magic_quotes_runtime`（已棄用的功能）。
     - 處理「register globals」（另一個已棄用的功能，可能將變數全域暴露）。它掃描超全域變數（`$_GET`、`$_POST` 等）並取消設定未受保護的變數，以防止注入攻擊。
   此部分保護免受舊版 PHP 常見漏洞的影響。

### 3. **錯誤處理**
   - 設定自訂錯誤處理程式（`_error_handler`、`_exception_handler`）和一個關閉函數（`_shutdown_handler`）來記錄 PHP 錯誤/例外。這確保問題被追蹤，而不是將原始錯誤顯示給使用者。

### 4. **設定覆寫**
   - 檢查 `subclass_prefix` 覆寫（來自 `index.php` 變數）並透過 `get_config()` 載入它。這允許您擴展核心類別。

### 5. **Composer Autoloader（可選）**
   - 如果您的設定中啟用了 `composer_autoload`，它會載入 Composer 的 autoloader（用於第三方函式庫）。如果找不到，則記錄錯誤。

### 6. **效能基準測試初始化**
   - 載入 `Benchmark` 類別並啟動計時器（例如，用於 `total_execution_time_start` 和 `loading_time:_base_classes_start`）。CodeIgniter 在此追蹤效能——時間被記錄/標記用於除錯。

### 7. **掛鉤系統**
   - 載入 `Hooks` 類別。
   - 呼叫 `pre_system` 掛鉤。掛鉤允許您在關鍵點注入自訂程式碼（例如，外掛或擴充功能）。
   - 稍後，它將檢查並呼叫其他掛鉤，如 `post_system`。

### 8. **核心類別實例化（載入關鍵元件）**
   - **Config 類別**：首先載入，因為其他類別依賴於它。它處理設定（例如，資料庫設定）。如果設定了 `$assign_to_config`（來自 `index.php`），則應用覆寫。
   - **字元集與 Unicode 處理**：設定 `mbstring` 和 `iconv` 以支援 UTF-8，設定預設值以防止編碼問題。
   - **相容性檔案**：為舊版 PHP 載入 polyfills（例如，用於字串雜湊、密碼）。
   - **核心類別**：實例化基本元件，如：
     - `Utf8`：用於 Unicode 支援。
     - `URI`：解析傳入的 URL/請求路徑。
     - `Router`：將 URL 映射到控制器/方法（例如，`/users/profile` → Users 控制器，profile 方法）。
     - `Output`：處理回應渲染（HTML、JSON 等）。
   - **快取檢查**：如果此請求有有效的快取，它會跳過其餘部分並直接輸出快取版本（為了效能）。
   - **更多類別**：載入 `Security`（CSRF/XSS 保護）、`Input`（清理 GET/POST 資料）和 `Lang`（語言/本地化）。

### 9. **控制器載入與健全性檢查**
   - 定義一個全域 `get_instance()` 函數（返回主控制器物件）。
   - 載入基礎 `Controller.php` 和任何子類別（來自您應用程式的擴充控制器）。
   - **健全性檢查**：確保請求的控制器/方法存在且有效：
     - 檢查控制器類別是否存在（例如 `Users.php`）。
     - 驗證方法不是私有的（`_` 前綴）或已在 `CI_Controller` 中定義。
     - 如果使用 `_remap`，則調整路由。
     - 如果無效，設定 404 錯誤標誌。
   - **404 處理**：如果 `$e404` 為 true，則嘗試 `404_override` 路由（來自設定）或顯示 404 頁面。
   - 停止「loading_time」的效能基準測試。

### 10. **請求執行**
   - 呼叫 `pre_controller` 掛鉤。
   - **實例化控制器**：建立您請求的控制器類別的實例（例如 `$CI = new Users();`）。
   - 呼叫 `post_controller_constructor` 掛鉤。
   - **呼叫方法**：使用 `call_user_func_array()` 執行控制器方法（例如 `profile()`），並帶有來自 URL 的參數。
   - 對控制器執行時間進行效能基準測試。
   - 呼叫 `post_controller` 掛鉤。

### 11. **輸出與清理**
   - 如果沒有 `display_override` 掛鉤阻止，則使用 `Output` 將最終回應發送到瀏覽器（例如，渲染視圖/HTML）。
   - 呼叫 `post_system` 掛鉤。
   - 腳本在此結束——PHP 處理其餘部分（發送輸出）。

### 關鍵概念與整體運作方式
- **MVC 模式**：CodeIgniter 遵循 Model-View-Controller。此腳本路由到 Controller（您的邏輯），它可能載入 Model（資料/資料庫）和 View（範本/輸出）。
- **掛鉤**：允許擴充性——例如，在流程的某些部分之前/之後執行自訂程式碼。
- **環境感知**：檢查 `ENVIRONMENT`（例如 'production'）以載入環境特定的設定。
- **效能**：使用懶載入（僅在需要時實例化類別）和快取以保持速度。
- **常見陷阱**：如果出現問題（例如 404），通常是由於路由設定錯誤、控制器缺失或檔案路徑與 `APPPATH` 不匹配。
- **版本說明**：此程式碼來自 CodeIgniter 3.x。較新版本（4.x）具有不同的結構。

如果此腳本成功運行，您的應用程式就會載入。此處記錄的錯誤可以在日誌中檢查。如需深入了解，請參閱[官方 CodeIgniter 文件](https://codeigniter.com/user_guide/general/index.html)。如果您有特定問題（例如，「路由如何運作？」），請提供更多細節！