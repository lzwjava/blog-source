---
audio: false
generated: true
lang: hant
layout: post
title: Webpack ResolverFactory 問題
translated: true
type: note
---

看起來你在執行 `npm run build` 時遇到了 Webpack 的問題。錯誤訊息提到「webpack ResolverFactory」和「can not find module './ResolverFactory'」，這表示 Webpack 在嘗試定位或使用其內部的 `ResolverFactory` 模組時出現了問題。這情況並不常見，因為 `ResolverFactory` 是 Webpack 的核心組件，通常不會以相對路徑方式（如 `./ResolverFactory`）來導入。讓我們來分析可能出錯的地方以及如何解決。

### 錯誤原因
這個錯誤表示在你的專案或依賴項中，有某處試圖從相對路徑 `./ResolverFactory` 載入一個不存在的模組。這之所以有問題是因為：
- **`ResolverFactory` 是 Webpack 的內部模組**，通常透過 `require('webpack').ResolverFactory` 或類似方式存取，而不是從像 `./ResolverFactory` 這樣的相對路徑載入。
- **`./` 前綴表示存在誤解**，因為這暗示 Webpack 正在當前目錄中尋找名為 `ResolverFactory.js` 的檔案，但 Webpack 的內部結構並非如此設計。

這通常指向以下其中一個問題：
- 你的 Webpack 設定檔（例如 `webpack.config.js`）中存在**拼寫錯誤或設定錯誤**。
- 某個**自訂外掛或載入器**錯誤地嘗試導入或使用 `ResolverFactory`。
- **依賴項問題**，可能是 Webpack 安裝版本過舊或損毀。

### 解決步驟
以下是排查和修復此錯誤的方法：

#### 1. 在專案中搜尋 `"./ResolverFactory"`
   - 此錯誤很可能源自某個錯誤的 `require` 或 `import` 語句，試圖載入 `./ResolverFactory` 而非從 Webpack 正確存取。
   - 使用你的 IDE 搜尋功能，或在專案目錄中執行以下指令來找出問題來源：
     ```bash
     grep -r "\./ResolverFactory" .
     ```
   - **如果在你的程式碼中發現**（例如在 `webpack.config.js` 或自訂外掛中），請修正為從 Webpack 正確導入。例如：
     ```javascript
     const { ResolverFactory } = require('webpack');
     ```
   - **如果在依賴項中發現**（位於 `node_modules` 內），請繼續執行步驟 3。

#### 2. 檢查你的 Webpack 設定
   - 開啟你的 `webpack.config.js`（或其他 Webpack 設定檔），檢查是否有引用 `ResolverFactory` 的地方。
   - 確保若使用到該模組，是透過 Webpack API 正確存取，而非作為相對模組。
   - 確認沒有拼寫錯誤或錯誤路徑，以免干擾 Webpack 的模組解析。

#### 3. 檢查自訂外掛或載入器
   - 若你使用自訂的 Webpack 外掛或載入器，請檢查其原始碼中是否有不正確的導入或使用 `ResolverFactory` 的情況。
   - 尋找類似 `require('./ResolverFactory')` 的程式行，並修正為使用正確的 Webpack 導入方式。
   - 對於第三方外掛或載入器，請檢查是否有更新版本：
     ```bash
     npm update <外掛名稱>
     ```
   - 若外掛已過時或無人維護，你可能需要自行複製並修復該問題。

#### 4. 驗證 Webpack 安裝狀態
   - 損毀或過時的 Webpack 安裝可能導致意外錯誤。檢查你的 Webpack 版本：
     ```bash
     npm list webpack
     ```
   - 若缺失或過時，請重新安裝：
     ```bash
     npm install webpack --save-dev
     ```
   - 為徹底修復，可刪除 `node_modules` 資料夾和 `package-lock.json`，然後重新安裝所有依賴項：
     ```bash
     rm -rf node_modules package-lock.json
     npm install
     ```

#### 5. 使用最小化設定進行測試
   - 為隔離問題，可建立一個最小化的 `webpack.config.js`：
     ```javascript
     const path = require('path');
     module.exports = {
       entry: './src/index.js', // 請調整為你的入口檔案
       output: {
         filename: 'bundle.js',
         path: path.resolve(__dirname, 'dist'),
       },
     };
     ```
   - 如有需要，更新你的 `package.json` 建置指令（例如 `"build": "webpack --config webpack.config.js"`），然後執行：
     ```bash
     npm run build
     ```
   - 若此設定可正常運作，請逐步加回原始設定（外掛、載入器等），直到錯誤再次出現以識別問題來源。

#### 6. 啟用詳細日誌以獲取更多資訊
   - 使用詳細輸出模式執行 Webpack 以獲取更多細節：
     ```bash
     webpack --config webpack.config.js --verbose
     ```
   - 檢查你的 `package.json` 中 `build` 指令的內容（例如 `"build": "webpack"`），並暫時修改為包含 `--verbose` 參數。日誌可能會指出有問題的模組或外掛。

#### 7. 檢查 Node.js 與 Webpack 的相容性
   - 確保你的 Node.js 版本與 Webpack 版本相容（例如 Webpack 5 需要 Node.js 10.13.0+）。檢查你的 Node.js 版本：
     ```bash
     node -v
     ```
   - 如有需要，可使用 `nvm` 等工具或從 [nodejs.org](https://nodejs.org) 下載來更新 Node.js。

### 可能問題根源
最可能的原因是 **Webpack 設定中的拼寫錯誤或配置錯誤**，導致 `ResolverFactory` 被錯誤地以相對模組（`./ResolverFactory`）方式引用，而非從 `webpack` 套件導入。另外，某個自訂外掛或載入器也可能是問題來源。

### 如何修復
- **若問題出現在你的程式碼中：** 將導入語句修正為使用 `require('webpack').ResolverFactory` 或適當的 Webpack API。
- **若問題出現在依賴項中：** 更新該套件或必要時進行修補。
- **若不確定問題來源：** 使用最小化設定和詳細日誌來定位問題，然後根據需要調整設定或重新安裝依賴項。

透過以上步驟，你應能解決「can not find module './ResolverFactory'」錯誤並成功執行 `npm run build`。若問題仍然存在，請考慮提供更多專案設定細節（例如 `webpack.config.js`、`package.json` 或完整錯誤日誌）以獲得進一步協助。