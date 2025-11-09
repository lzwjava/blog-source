---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: CodeIgniter 分析器配置指南
translated: true
type: note
---

### 理解 CodeIgniter Profiler 配置

您提供的程式碼片段似乎是 CodeIgniter `config/profiler.php` 檔案（通常位於 `application/config/profiler.php`）的標頭和註釋。此檔案用於配置 **Profiler**，這是一個內建的 CodeIgniter 工具，用於除錯和分析應用程式效能。它允許您在頁面載入結束時顯示（或隱藏）各種資料區塊，例如執行時間、資料庫查詢和載入的類別。

您分享的片段只是標頭 — 這是所有 CodeIgniter 配置檔案的標準格式 — 並附有官方使用者指南的連結（請注意，如果您使用的是 CodeIgniter 3，其文件可能更相關，因為 CI 4 有一些差異）。下面，我將逐步解釋如何在 CodeIgniter 中**使用和配置 Profiler**，包括完整配置檔案的完整範例。

#### 步驟 1：先決條件
- **CodeIgniter 版本**：這適用於 CI 2.x 和 3.x。如果您使用 CI 4，則需透過 `application/Config/Toolbar.php` 中的 Debug Toolbar 來存取 Profiler。
- **環境**：Profiler 僅供**開發環境**使用（不用於生產環境，因為它會暴露敏感資料）。請透過配置檔案啟用它。
- **運作原理**：一旦啟用，Profiler 會在頁面底部附加一個可收合的除錯面板，顯示基準測試、查詢和 POST 資料等指標。它不需要自訂程式碼即可執行 — 在設定後會自動運行。

#### 步驟 2：如何啟用 Profiler
1. **定位配置檔案**：
   - 在您的專案中，前往 `application/config/profiler.php`。
   - 如果檔案不存在，請根據預設範本建立它。

2. **全域啟用**：
   - 開啟 `application/config/profiler.php` 並設定 `$config['enable_profiler'] = TRUE;`。
   - 這將為所有請求啟用 Profiler（您稍後可以在控制器中有條件地啟用/停用它）。

3. **配置檔案的完整範例**：
   基於標準 CI 結構，完整的 `config/profiler.php` 通常如下所示（如果您的檔案缺失，可以將此複製貼上到您的檔案中）。您提供的片段只是頂部部分；配置陣列緊隨其後。

   ```php
   <?php
   defined('BASEPATH') OR exit('No direct script access allowed');

   /*
   | -------------------------------------------------------------------------
   | Profiler Sections
   | -------------------------------------------------------------------------
   | This file lets you determine whether or not various sections of Profiler
   | data are displayed when the Profiler is enabled.
   | Please see the user guide for info:
   |
   |    http://codeigniter.com/user_guide/general/profiling.html
   |
   */

   $config['enable_profiler'] = TRUE;  // 設為 TRUE 啟用，FALSE 全域停用

   // 可配置的區塊（設為 TRUE 顯示，FALSE 隱藏）
   $config['config']         = TRUE;   // 顯示所有配置變數
   $config['queries']        = TRUE;   // 顯示所有執行的資料庫查詢及其執行時間
   $config['get']            = TRUE;   // 顯示傳遞給控制器的所有 GET 資料
   $config['post']           = TRUE;   // 顯示傳遞給控制器的所有 POST 資料
   $config['uri_string']     = TRUE;   // 顯示請求的 URI 字串
   $config['controller_info'] = TRUE;  // 顯示控制器和方法資訊
   $config['models']         = TRUE;   // 顯示已載入模型的詳細資訊
   $config['libraries']      = TRUE;   // 顯示已載入程式庫的詳細資訊
   $config['helpers']        = TRUE;   // 顯示已載入輔助函數的詳細資訊
   $config['memory_usage']   = TRUE;   // 顯示記憶體使用量
   $config['elapsed_time']   = TRUE;   // 顯示總執行時間
   $config['benchmarks']     = TRUE;   // 顯示基準測試資料
   $config['http_headers']   = TRUE;   // 顯示 HTTP 標頭
   $config['session_data']   = TRUE;   // 顯示 session 資料

   /* End of file profiler.php */
   /* Location: ./application/config/profiler.php */
   ```

   - **關鍵設定**：
     - `$config['enable_profiler']`：主開關。
     - 每個區塊（例如 `config['queries']`）控制可見性。根據您要除錯的內容設為 `TRUE`/`FALSE`。

4. **有條件啟用（可選）**：
   - 您不必全域啟用它。在控制器中，您可以使用：
     ```php
     $this->output->enable_profiler(TRUE);  // 僅針對此特定方法/請求啟用
     $this->output->enable_profiler(FALSE); // 停用
     ```
   - 這會覆蓋該頁面的全域配置。

#### 步驟 3：如何在實際中使用 Profiler
1. **存取輸出**：
   - 載入應用程式中的任何頁面（例如，控制器方法）。
   - 滾動到底部 — Profiler 將顯示為一個可收合的方塊，其中包含「Elapsed Time」、「Database Queries」等區塊。
   - 點擊「Close」或「Open」來切換可見性。

2. **每個區塊顯示的內容**：
   - **Benchmarks**：程式碼不同部分的 CPU 時間（對效能優化有用）。
   - **Queries**：所有執行的 SQL 查詢，包括執行時間和錯誤（對除錯資料庫問題非常有用）。
   - **POST/GET**：提交的表單資料，對表單驗證有幫助。
   - **Memory Usage**：您的指令碼使用了多少 RAM（監控記憶體洩漏）。
   - 範例：如果頁面速度慢，啟用 `benchmarks` 和 `queries` 來識別瓶頸。

3. **自訂基準測試**：
   - 在程式碼中加入自訂標記來計時特定區塊：
     ```php
     $this->benchmark->mark('query_start');  // 開始計時器
     // 您的程式碼在此（例如，foreach 迴圈或 DB 查詢）
     $this->benchmark->mark('query_end');    // 結束計時器
     ```
   - 這將自動出現在「Benchmarks」區塊中。

4. **在控制器中的使用範例**：
   假設您有一個速度慢的控制器方法 — 您可以在那裡啟用 Profiler 來除錯：
   ```php
   class Example extends CI_Controller {
       public function index() {
           $this->load->database();
           $this->output->enable_profiler(TRUE);  // 僅針對此頁面啟用

           // 您的邏輯在此，例如獲取資料
           $data['results'] = $this->db->get('users')->result();
           $this->load->view('example_view', $data);
       }
   }
   ```
   - 載入此頁面後，檢查底部的 Profiler 資料。

#### 步驟 4：提示與疑難排解
- **安全性注意**：切勿在生產環境中啟用 — 透過 `$config['enable_profiler'] = FALSE;` 或使用環境變數（例如，透過 hooks 為 DEV 環境設定）來停用它。
- **常見問題**：
  - 沒有顯示？請確保 `$config['enable_profiler']` 是 TRUE，並且您不在生產伺服器上。
  - 錯誤？檢查您的 `view` 檔案是否有正確的結束標籤（例如 `</html>`）。
- **進階**：如需更多控制，請使用 `config/hooks.php` 中的 **Hooks** 來根據 IP 或環境有條件地啟用。
- **資源**：
  - 官方文件：[CodeIgniter 3 Profiling](https://codeigniter.com/user_guide/general/profiling.html) 或 [CI 4 Debugging](https://codeigniter.com/user_guide/testing/debugging.html)。
  - 如果您使用 CI 4，請改用 Debug Toolbar（在 `Toolbar.php` 中啟用）。

如果這不符合您的意思（例如，如果您有不同的配置或錯誤），請提供更多上下文，例如您的完整程式碼或 CI 版本，我將進一步完善答案！