---
audio: false
generated: true
lang: hant
layout: post
title: 疑難排解使用代理伺服器時 VSCode 擴充功能安裝問題
translated: true
type: note
---

若要在 Visual Studio Code (VSCode) 中檢查擴充功能安裝記錄，或使用指令列透過 `code --install-extension` 安裝擴充功能並檢視記錄（特別是當您懷疑存在代理伺服器問題時），可按照以下步驟操作：

---

### 透過指令列使用 `code --install-extension`
您可透過指令列安裝擴充功能，並觀察安裝過程的輸出訊息，這有助於診斷代理伺服器問題。

1. **啟用詳細輸出模式安裝**  
   執行以下指令安裝擴充功能並顯示詳細輸出：
   ```bash
   code --install-extension <extension-id> --verbose
   ```
   - 將 `<extension-id>` 替換為擴充功能 ID（例如 `vscodevim.vim`）
   - `--verbose` 參數會顯示更詳細的輸出內容，包含進度狀態及可能錯誤（如代理伺服器或網路問題）

2. **處理代理伺服器問題**  
   若您處於代理伺服器環境，可嘗試以下方法：
   - **設定代理伺服器環境變數**：  
     在執行指令前先設定代理伺服器：
     ```bash
     export HTTP_PROXY=http://您的代理伺服器:埠號
     export HTTPS_PROXY=http://您的代理伺服器:埠號
     code --install-extension <extension-id>
     ```
     - Windows 系統請使用 `set` 指令：
       ```cmd
       set HTTP_PROXY=http://您的代理伺服器:埠號
       set HTTPS_PROXY=http://您的代理伺服器:埠號
       code --install-extension <extension-id>
       ```
   - **直接指定代理伺服器**：  
     使用 `--proxy-server` 參數：
     ```bash
     code --install-extension <extension-id> --proxy-server=http://您的代理伺服器:埠號
     ```

3. **檢查輸出結果**  
   - 透過 `--verbose` 參數產生的主控台輸出會顯示安裝進度及錯誤資訊（例如連線逾時或代理伺服器驗證失敗）
   - 注意：指令列介面 (`code`) 的代理伺服器支援功能較 VSCode 圖形介面有限，記錄內容可能不如預期詳細

---

### 在 VSCode 中檢查記錄
若需更詳細的記錄（特別是在安裝嘗試後），請使用 VSCode 內建的記錄功能：

1. **開啟記錄資料夾**  
   - 開啟 VSCode 並呼叫命令選擇區：
     - 按下 `Ctrl+Shift+P`（macOS 請按 `Cmd+Shift+P`）
     - 輸入並選取 **Developer: Open Logs Folder**
   - 系統會開啟包含各種記錄檔的資料夾，請重點檢查：
     - **`exthost.log`**：記錄擴充功能主機處理程序的相關資訊，包含安裝嘗試
     - **`sharedprocess.log`**：記錄可能包含擴充功能相關事件的共享處理程序
   - 使用文字編輯器開啟這些檔案，搜尋提及擴充功能 ID、網路問題或代理伺服器錯誤的內容

2. **檢視輸出面板**  
   - 在 VSCode 中前往 `檢視 > 輸出` 開啟 **輸出** 面板
   - 在右側下拉選單中選取 **Extensions**
   - 此處會顯示在 VSCode 內安裝擴充功能時的即時記錄（不包含直接透過 CLI 的安裝）。若透過 VSCode 介面重新嘗試安裝，可能會在此看到代理伺服器相關錯誤

---

### 代理伺服器疑難排解補充步驟
若懷疑存在代理伺服器問題，請透過以下技巧確保設定正確：

- **在 VSCode 中設定代理伺服器**  
  - 開啟 VSCode 設定（`檔案 > 偏好設定 > 設定` 或 `Ctrl+,`）
  - 搜尋 `proxy` 並設定：
    ```json
    "http.proxy": "http://您的代理伺服器:埠號"
    ```
  - 可選調整 `"http.proxyStrictSSL"`（必要時設為 `false`）或 `"http.proxyAuthorization"`（用於需驗證的代理伺服器）
  - 這些設定僅適用於 VSCode 內部安裝，不一定影響 CLI 操作

- **測試網路連線**  
  - 手動測試代理伺服器是否允許存取 VSCode Marketplace：
    - 從 Marketplace 網站取得擴充功能的 VSIX 檔案網址
    - 使用 `curl` 等工具測試：
      ```bash
      curl -x http://您的代理伺服器:埠號 <vsix-網址>
      ```
    - 若測試失敗，可能是代理伺服器阻擋了連線

---

### 建議操作流程
- **CLI 安裝**：使用 `code --install-extension <extension-id> --verbose` 配合代理伺服器環境變數或 `--proxy-server` 參數，即時檢查終端機內的錯誤訊息
- **詳細記錄分析**：透過 VSCode 介面（Marketplace）安裝擴充功能，並檢查 **輸出 > Extensions** 面板或記錄資料夾（`exthost.log`）
- **代理伺服器驗證**：確保系統與 VSCode 中的代理伺服器設定皆正確無誤

透過結合以上方法，您將能有效監控安裝進度並診斷代理伺服器問題。若 CLI 輸出資訊不足時，VSCode 記錄將能提供更深入的錯誤分析線索。