---
audio: false
generated: true
lang: hant
layout: post
title: VS Code VSIX 下載
translated: true
type: note
---

要手動下載 Visual Studio Code（VS Code）擴充功能的 `.vsix` 檔案，你可以使用 Visual Studio Marketplace，該平台收錄了所有官方擴充功能。`.vsix` 檔案是 VS Code 擴充功能的封裝格式，雖然 Marketplace 不一定提供直接下載按鈕，但你可以透過建構下載 URL 或使用其他方法來取得。以下是詳細步驟：

### 手動下載 `.vsix` 檔案的步驟

1. **在 Visual Studio Marketplace 上找到擴充功能**  
   - 在網頁瀏覽器中前往 [Visual Studio Marketplace](https://marketplace.visualstudio.com/vscode)。
   - 搜尋你想要的擴充功能（例如 Microsoft 的 "Python"、"Prettier - Code formatter" 等）。
   - 開啟擴充功能的頁面。例如，Python 擴充功能的 URL 可能如下：  
     `https://marketplace.visualstudio.com/items?itemName=ms-python.python`。

2. **識別發行者和擴充功能名稱**  
   - 在擴充功能頁面上，記下**發行者**和**擴充功能識別碼**。這些資訊會顯示在頁面上或包含在 URL 中。
   - 例如，在 `ms-python.python` 中，`ms-python` 是發行者，`python` 是擴充功能名稱。

3. **建構下載 URL**  
   - 可以使用 Marketplace 提供的特定 URL 模式直接下載 `.vsix` 檔案。通用格式如下：  
     ```
     https://<publisher>.gallery.vsassets.io/_apis/public/gallery/publisher/<publisher>/extension/<extension-name>/latest/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage
     ```
   - 將 `<publisher>` 替換為發行者名稱，`<extension-name>` 替換為擴充功能名稱。
   - 以 Python 擴充功能（`ms-python.python`）為例，URL 會是：  
     ```
     https://ms-python.gallery.vsassets.io/_apis/public/gallery/publisher/ms-python/extension/python/latest/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage
     ```
   - 將此 URL 貼到瀏覽器中，即可觸發 `.vsix` 檔案的下載。

4. **替代方法：使用 Marketplace 頁面的「下載擴充功能」連結（如果可用）**  
   - 部分擴充功能頁面會在 **Resources** 區塊或其他位置提供「Download Extension」連結。如果存在，點擊即可直接下載 `.vsix` 檔案。但此方法較不常見，因此 URL 方法更為可靠。

5. **驗證下載**  
   - 下載的檔案會具有 `.vsix` 副檔名（例如 `ms-python.python-<version>.vsix`）。
   - 檢查檔案大小和名稱，確保符合你預期的擴充功能和版本。

6. **在 VS Code 中安裝 `.vsix` 檔案（可選）**  
   - 開啟 VS Code。
   - 前往擴充功能檢視（快捷鍵 `Ctrl+Shift+X` 或 macOS 上的 `Cmd+Shift+X`）。
   - 點擊擴充功能窗格右上角的三點選單（`...`）。
   - 選擇 **Install from VSIX**，然後瀏覽並選擇已下載的 `.vsix` 檔案。

### 範例演練
假設你想要 Dirk Baeumer 的 **ESLint** 擴充功能：
- Marketplace URL：`https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint`
- 發行者：`dbaeumer`
- 擴充功能名稱：`vscode-eslint`
- 下載 URL：  
  ```
  https://dbaeumer.gallery.vsassets.io/_apis/public/gallery/publisher/dbaeumer/extension/vscode-eslint/latest/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage
  ```
- 在瀏覽器中開啟此 URL，即可下載 `.vsix` 檔案（例如 `dbaeumer.vscode-eslint-<version>.vsix`）。

### 注意事項
- **版本**：URL 中的 `/latest/` 部分確保你取得最新版本。如果你需要特定版本，通常需要知道版本號（可在 Marketplace 的「Version History」分頁中查看），並可能需要調整 URL 或使用如 `ovsx` 等工具（見下文），但 Marketplace API 不一定能透過直接 URL 輕鬆取得舊版本。
- **下載被阻擋**：如果 URL 無效，可能是發行者限制了直接存取，或你的瀏覽器/網路阻擋了下載。此時可嘗試使用其他瀏覽器或下載管理員。
- **替代工具**：你可以使用命令列工具如 `ovsx`（來自 Open VSX Registry）來下載擴充功能。透過 npm 安裝（`npm install -g ovsx`），然後執行：  
  ```
  ovsx download ms-python.python
  ```
  即可透過程式化方式下載 `.vsix` 檔案。

### 最終步驟
要手動下載 VS Code 擴充功能的 `.vsix` 檔案：
1. 前往 [Visual Studio Marketplace](https://marketplace.visualstudio.com/vscode) 上的擴充功能頁面。
2. 識別發行者和擴充功能名稱（例如 `ms-python.python`）。
3. 在瀏覽器中使用此 URL 格式：  
   ```
   https://<publisher>.gallery.vsassets.io/_apis/public/gallery/publisher/<publisher>/extension/<extension-name>/latest/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage
   ```
4. 下載 `.vsix` 檔案，並可選擇在 VS Code 中安裝。