---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 在 Mac 上修復 VSCode 的 Fn + F5 按鍵
translated: true
type: note
---

如果在 Visual Studio Code (VSCode) 中按下 **Fn + F5** 無法啟動 **Extension Development Host**，這通常是由於 Mac 上 `Fn` 鍵與功能鍵的配置方式、VSCode 快捷鍵衝突，或是擴充功能開發環境設定錯誤所致。以下將說明可能的原因及解決方法。

### 為何 **Fn + F5** 在 Mac 上無效

1. **Mac 功能鍵行為**：
   - 在 Mac 鍵盤上，功能鍵 (F1–F12) 預設通常被指派給系統功能（例如 F5 可能用於控制鍵盤亮度或多媒體播放）。
   - `Fn` 鍵用於存取「標準」功能鍵行為（例如 `Fn + F5` 會發送實際的 F5 鍵訊號，而非系統功能）。
   - 如果 `Fn + F5` 在 VSCode 中未觸發預期動作，可能是 Mac 的鍵盤設定或 VSCode 的快捷鍵設定未能正確解讀輸入。

2. **VSCode 快捷鍵衝突或設定錯誤**：
   - VSCode 可能未將 `F5`（或 `Fn + F5`）對應到用於啟動 Extension Development Host 的「Run Extension」指令。
   - 其他擴充功能或自訂快捷鍵可能覆寫了 `F5` 的設定。

3. **擴充功能開發環境設定問題**：
   - 如果 VSCode 擴充功能專案未正確設定（例如缺少或錯誤的 `launch.json`），按下 `F5`（無論是否搭配 `Fn`）都無法啟動 Extension Development Host。

4. **macOS 系統設定**：
   - macOS 可能攔截了 `F5` 鍵用於系統功能，或者 `Fn` 鍵的行為被自訂設定影響，導致 VSCode 無法偵測到。

### 解決 Mac 上 VSCode 中 **Fn + F5** 無效的步驟

#### 1. **檢查 macOS 鍵盤設定**
   - **啟用標準功能鍵行為**：
     - 前往 **系統設定 > 鍵盤**。
     - 勾選 **「將 F1、F2 等鍵作為標準功能鍵使用」**。
     - 若已啟用，您可直接按下 `F5`（無需 `Fn`）向 VSCode 發送 F5 鍵訊號。嘗試單獨按下 `F5` 查看是否能啟動 Extension Development Host。
     - 若未勾選，則需按下 `Fn + F5` 來發送 F5，因為單獨按下 `F5` 可能控制系統功能（例如鍵盤亮度）。
   - **測試 F5 行為**：
     - 在文字編輯器（例如 TextEdit）中按下 `F5` 和 `Fn + F5`。如果 `F5` 單獨觸發系統動作（如亮度調整），而 `Fn + F5` 無任何反應，則表示 `Fn` 鍵正常運作，發送了標準 F5 訊號。
   - **重置 NVRAM/PRAM**（如有需要）：
     - 重新啟動 Mac，並按住 `Cmd + Option + P + R` 直到聽到開機聲兩次（或在新款 Mac 上看到 Apple 標誌出現兩次）。這將重置鍵盤相關設定，可能解決偵測問題。

#### 2. **確認 VSCode 快捷鍵設定**
   - 開啟 VSCode，前往 **Code > Preferences > Keyboard Shortcuts** (`Cmd+K, Cmd+S`)。
   - 在搜尋欄中輸入 `F5` 或 `Run Extension`。
   - 尋找指令 **「Debug: Start Debugging」** 或 **「Run Extension」**（與啟動 Extension Development Host 相關）。
   - 確保其對應到 `F5`。若未設定，雙擊該指令，按下 `F5`（或如有需要則按 `Fn + F5`），並儲存新的快捷鍵。
   - 檢查衝突：搜尋其他綁定到 `F5` 或 `Fn + F5` 的指令，並移除或重新指派。
   - 如有需要可重置快捷鍵：在 Keyboard Shortcuts 編輯器中點擊三點圖標 (`...`)，選擇 **Reset Keybindings**。

#### 3. **檢查擴充功能專案設定**
   - 確保擴充功能專案正確設定：
     - 在 VSCode 中開啟您的擴充功能專案資料夾（必須包含 `package.json` 和 `extension.js` 或同等檔案）。
     - 確認 `package.json` 包含必要欄位：
       ```json
       {
         "name": "your-extension-name",
         "displayName": "Your Extension Name",
         "version": "0.0.1",
         "engines": {
           "vscode": "^1.60.0"
         },
         "categories": ["Other"],
         "activationEvents": ["*"],
         "main": "./extension.js"
       }
       ```
   - 檢查是否存在 `.vscode/launch.json` 檔案：
     - 若不存在，VSCode 應在按下 `F5` 時自動建立。若未建立，請手動在 `.vscode` 資料夾中建立，內容如下：
       ```json
       {
         "version": "0.2.0",
         "configurations": [
           {
             "name": "Run Extension",
             "type": "extensionHost",
             "request": "launch",
             "args": ["--extensionDevelopmentPath=${workspaceFolder}"],
             "outFiles": ["${workspaceFolder}/out/**/*.js"],
             "preLaunchTask": "npm: watch"
           }
         ]
       }
       ```
     - 確保 `preLaunchTask`（例如 `npm: watch`）與 `.vscode/tasks.json` 中的任務匹配（若使用 TypeScript 或建置步驟）。
   - 在 VSCode 終端機 (`Cmd+``) 中執行 `npm install`，確保依賴項（例如 `@types/vscode`）已安裝。

#### 4. **測試啟動 Extension Development Host**
   - 在擴充功能專案開啟狀態下，嘗試按下 `F5`（或若「將 F1、F2 等鍵作為標準功能鍵使用」設定為關閉，則按 `Fn + F5`）。
   - 或者，開啟 **Run and Debug** 面板 (`Cmd+Shift+D`)，從下拉選單中選擇 **「Run Extension」**，然後點擊綠色播放按鈕。
   - 若 Extension Development Host 未啟動：
     - 檢查 **Output** 面板 (`Cmd+Shift+U`)，並從下拉選單中選擇 **「Extension」** 以查看任何錯誤訊息。
     - 檢查 **Debug Console** 中是否有與擴充功能或偵錯過程相關的錯誤。
     - 確保 Node.js 已安裝（在終端機中執行 `node -v`），且專案無語法錯誤。

#### 5. **使用其他鍵盤測試**
   - 將外接 USB 鍵盤連接到 Mac，並在 VSCode 中按下 `F5`（或 `Fn + F5`）。
   - 若可正常運作，則問題可能出在 Mac 內建鍵盤的硬體或韌體。請透過 Mac 製造商（例如 Apple Software Update）檢查鍵盤韌體更新。

#### 6. **更新 VSCode 和 macOS**
   - 確保 VSCode 為最新版本：前往 **Code > Check for Updates** 或從 VSCode 官網下載最新版本。
   - 更新 macOS：前往 **系統設定 > 一般 > 軟體更新** 安裝任何可用更新，因為這些更新可能包含鍵盤驅動程式修復。

#### 7. **停用干擾的擴充功能或軟體**
   - **VSCode 擴充功能**：
     - 停用所有擴充功能：在終端機中執行 `code --disable-extensions`，然後開啟 VSCode 並再次嘗試 `F5`。
     - 若可運作，則逐一重新啟用擴充功能以找出問題來源。
   - **第三方軟體**：
     - 檢查鍵盤重新對應工具，如 Karabiner-Elements 或 BetterTouchTool。開啟其設定，確保 `F5` 或 `Fn + F5` 未被重新對應。
     - 暫時停用這些工具進行測試。

#### 8. **偵錯記錄**
   - 啟用 VSCode 開發者工具以檢查按鍵事件：
     - 開啟 VSCode，按下 `Cmd+Option+I` 開啟 Developer Tools。
     - 前往 **Console** 分頁，按下 `Fn + F5`。查看按鍵事件記錄，確認 VSCode 是否收到正確輸入。
   - 若無按鍵事件記錄，則問題可能出在系統層級（macOS 或鍵盤硬體）。

### 若問題持續存在
   - 提供更多詳細資訊：
     - macOS 版本（例如 Ventura、Sonoma）。
     - VSCode 版本（透過 **Code > About Visual Studio Code** 查看）。
     - 鍵盤類型（例如 MacBook 內建鍵盤、外接鍵盤型號）。
     - `F5` 或 `Fn + F5` 在其他應用程式中是否有效（例如 `F5` 是否能重新整理瀏覽器？）。
     - VSCode **Output** 或 **Debug Console** 中的任何錯誤訊息。
   - 嘗試建立最小化的擴充功能專案以隔離問題：
     - 執行 `yo code`（需要 Yeoman 和 VSCode 產生器：`npm install -g yo generator-code`）以建立新擴充功能專案。
     - 在 VSCode 中開啟新專案，並按下 `F5` 查看是否能啟動 Extension Development Host。

[VS Code Extension Development](https://code.visualstudio.com/api/get-started/your-first-extension)  
[Mac Keyboard Settings](https://support.apple.com/guide/mac-help/change-the-behavior-of-the-function-keys-mchlp2882/mac)  
[VS Code Keybindings](https://code.visualstudio.com/docs/getstarted/keybindings)