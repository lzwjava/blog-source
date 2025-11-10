---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 在 VSCode 中啟動擴充功能主機
translated: true
type: note
---

若要在 Visual Studio Code (VSCode) 中按下 **F5** 來啟動 **Extension Development Host** 以開發 VSCode 擴充功能，請遵循以下步驟：

1. **在 VSCode 中開啟您的擴充功能專案**：
   - 確保您已設定好 VSCode 擴充功能專案。這通常包含一個具有必要擴充功能配置（例如 `contributes`、`activationEvents`）的 `package.json` 檔案。
   - 透過選擇 `檔案 > 開啟資料夾` 或使用 `Ctrl+K, Ctrl+O`（Windows/Linux）或 `Cmd+K, Cmd+O`（Mac），在 VSCode 中開啟包含您擴充功能專案的資料夾。

2. **驗證您的擴充功能設定**：
   - 確保您的專案根目錄中有一個有效的 `package.json` 檔案，至少包含以下欄位：
     ```json
     {
       "name": "your-extension-name",
       "displayName": "Your Extension Name",
       "description": "Description of your extension",
       "version": "0.0.1",
       "engines": {
         "vscode": "^1.60.0"
       },
       "categories": ["Other"],
       "activationEvents": ["*"],
       "main": "./extension.js",
       "contributes": {}
     }
     ```
   - 確保您有一個 `extension.js`（或同等檔案）作為擴充功能代碼的進入點。
   - 如果您的擴充功能使用 Node.js 模組，請在整合式終端機（`Ctrl+``）中執行 `npm install` 以安裝相依套件。

3. **按下 F5 啟動 Extension Development Host**：
   - 當您的擴充功能專案在 VSCode 中開啟時，按下鍵盤上的 **F5**。
   - 這將啟動 **Extension Development Host**，這是一個獨立的 VSCode 視窗，您的擴充功能將在此載入以供測試。
   - VSCode 會自動：
     - 建置您的擴充功能（如果使用 TypeScript，它會將 `.ts` 檔案編譯為 `.js`）。
     - 啟動一個新的 VSCode 實例，並啟用您的擴充功能。
     - 開啟一個附加到 Extension Host 程序的偵錯程式。

4. **偵錯配置**：
   - VSCode 使用 `.vscode` 資料夾中的 `launch.json` 檔案來配置偵錯。如果該檔案不存在，當您首次按下 F5 時，VSCode 會自動建立一個。
   - 典型的擴充功能 `launch.json` 如下所示：
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
   - 確保 `preLaunchTask`（如果存在）與 `tasks.json` 中的任務相符（例如用於編譯 TypeScript）。

5. **測試您的擴充功能**：
   - 在 Extension Development Host 視窗中，您的擴充功能應該已啟用。請測試其功能（例如指令、UI 貢獻），如您的 `package.json` 和代碼中所定義。
   - 使用主 VSCode 視窗中的 **Debug Console** 來查看擴充功能的日誌或錯誤。

6. **疑難排解**：
   - 如果 F5 無效：
     - 確保已安裝 Node.js 和 npm，因為擴充功能開發需要它們。
     - 檢查您是否已安裝 VSCode Extension API 相依套件（`npm install @types/vscode`）。
     - 驗證 `launch.json` 配置指向正確的路徑。
     - 如果看到錯誤，請檢查 Extension Development Host 視窗中的 **Output** 面板（在下拉式選單中選擇 "Extension"）。
   - 如果 Extension Host 未啟動，請確保您的專案在 `package.json` 或主要擴充功能檔案中沒有語法錯誤。

**補充說明**：
- 您也可以透過開啟 **Run and Debug** 面板（`Ctrl+Shift+D` 或 Mac 上的 `Cmd+Shift+D`），從下拉式選單中選擇 “Run Extension”，然後點擊綠色播放按鈕來啟動 Extension Development Host。
- 若要在進行變更後重新載入 Extension Host，請在 Extension Development Host 視窗中使用 `Ctrl+R`（Windows/Linux）或 `Cmd+R`（Mac），或使用 F5 重新啟動它。

如需更多詳細資訊，請參閱官方 VSCode 擴充功能開發指南：  
[VS Code Extension Development](https://code.visualstudio.com/api/get-started/your-first-extension)