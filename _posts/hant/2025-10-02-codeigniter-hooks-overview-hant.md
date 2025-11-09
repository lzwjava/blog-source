---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: CodeIgniter 掛鈎功能概覽
translated: true
type: note
---

### 什麼是 CodeIgniter 中的 Hooks？

Hooks 是 CodeIgniter 中一種無需修改框架核心檔案即可擴展功能的方法。它們允許你在執行週期的特定點運行自定義程式碼，例如在載入控制器前後、覆蓋輸出或快取時。這能透過將你的程式碼與官方程式碼庫分離來保持可升級性。

Hooks 在 `application/config/hooks.php` 中定義，並在 `application/config/config.php` 中透過設定 `$config['enable_hooks'] = TRUE;` 來啟用。

### 啟用 Hooks

1. 開啟 `application/config/config.php`。
2. 設定配置變數：
   ```php
   $config['enable_hooks'] = TRUE;
   ```
   這會告訴 CodeIgniter 檢查並執行 hooks 檔案。

### 定義 Hooks

Hooks 在 `application/config/hooks.php` 中配置為陣列的陣列。每個 hook 陣列指定：
- `class`：（必需）類別名稱（必須與檔案名稱匹配）。
- `function`：（必需）類別中的方法名稱。
- `filename`：（必需）類別的檔案名稱（不含 .php）。
- `filepath`：（可選）檔案的資料夾路徑，預設為 `application/hooks/`。
- `params`：（可選）傳遞給方法的參數陣列。

將你的 hook 類別放置在 `application/hooks/` 中。

### Hook 觸發點

CodeIgniter 提供以下預定義的觸發點可供 hooks 執行：
- **pre_system**：在系統載入前運行（此時尚未運行任何其他內容）。
- **pre_controller**：在控制器被呼叫前立即運行。
- **post_controller_constructor**：在控制器實例化後但其方法執行前運行。
- **post_controller**：在控制器完成後運行。
- **display_override**：取代輸出到瀏覽器的過程運行（覆蓋 _display 建立/結束控制器檔案）。
- **cache_override**：取代載入快取的過程運行（覆蓋 _display 快取）。
- **post_system**：在網頁完全發送到瀏覽器後運行。

### 使用範例

假設你想在控制器運行前記錄每個請求。為 `pre_controller` 建立一個 hook。

1. 建立檔案 `application/hooks/my_hook.php`：
   ```php
   <?php
   class My_hook {
       public function log_request() {
           // 範例：記錄到檔案或資料庫
           log_message('info', 'Controller about to be called: ' . $this->uri->uri_string());
       }
   }
   ```

2. 在 `application/config/hooks.php` 中新增：
   ```php
   $hook['pre_controller'] = array(
       'class' => 'My_hook',
       'function' => 'log_request',
       'filename' => 'my_hook.php',
       'filepath' => 'hooks', // 可選，預設為 application/hooks/
       'params' => array() // 可選參數
   );
   ```

現在，每當控制器即將運行時，`log_request` 就會執行。

### 最佳實踐
- 謹慎使用 hooks；如果可能，優先擴展控制器或使用函式庫。
- 始終在開發環境中測試 hooks，以確保它們不會干擾核心邏輯。
- 更多詳細資訊，請參閱官方 CodeIgniter 使用者指南中有關 hooks 的章節。