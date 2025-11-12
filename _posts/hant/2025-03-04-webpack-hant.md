---
audio: false
generated: true
lang: hant
layout: post
title: 使用 Webpack 作為模塊打包工具
translated: true
type: note
---

### 重點摘要
- 若要使用 webpack 1.13.2 版和 webpack-dev-server 1.14.0 版，似乎需要透過特定配置來建立 Node.js 專案。
- 研究建議透過 npm 安裝這些版本、建立配置檔案，並執行開發伺服器以實現即時更新。
- 證據顯示需確保備有 index.html 檔案，且設定中包含正確的打包檔案路徑。

### 安裝與設定
開始前，請先確認已從 [nodejs.org](https://nodejs.org) 安裝 Node.js。建立專案目錄，使用 npm 初始化並安裝指定版本：

- 執行 `npm init -y` 建立 package.json 檔案。
- 透過 `npm install webpack@1.13.2` 和 `npm install webpack-dev-server@1.14.0` 進行安裝。

### 配置設定
建立 `webpack.config.js` 檔案來定義檔案打包方式。基本設定包含：
- 進入點（例如 `./src/index.js`）。
- 輸出路徑（例如包含 `bundle.js` 的 `dist` 目錄）。
- 開發伺服器設定，例如用於靜態檔案的 `contentBase`。

### 執行開發伺服器
使用 `npx webpack-dev-server` 啟動伺服器，若 npx 不可用則改用 `./node_modules/.bin/webpack-dev-server`。透過 [http://localhost:8080](http://localhost:8080) 存取應用程式，內容將隨變更自動更新。

### 意外細節
較舊版本需使用特定配置（如 `contentBase` 而非現代的 `static`），且設定可能需要手動調整檔案服務功能，這點與具備更高自動化程度的新版本有所不同。

---

### 調查筆記：使用 Webpack 1.13.2 與 Webpack-Dev-Server 1.14.0 詳細指南

本綜合指南逐步詳細說明如何設定與使用 webpack 1.13.2 版及 webpack-dev-server 1.14.0 版，重點在於建立適合 JavaScript 專案的開發環境。由於這些版本較舊，部分配置與行為有別於現代標準，本筆記旨在涵蓋所有必要步驟，讓新手也能清晰完整地依循操作。

#### 背景與情境
Webpack 是 JavaScript 的模組打包工具，歷史上用於編譯和打包網頁應用程式檔案，管理相依性並進行生產環境優化。Webpack-dev-server 作為配套工具，提供具備即時重新載入功能的開發伺服器，非常適合迭代式開發。指定版本 webpack 1.13.2 和 webpack-dev-server 1.14.0 發布於 2016 年，屬於較舊但仍可運作的設定，可能用於舊版專案相容性維護。

#### 逐步安裝與設定
首先請確認已安裝 Node.js，這是使用 npm 套件管理器的必要條件。可從 [nodejs.org](https://nodejs.org) 下載。當前時間 2025 年 3 月 3 日星期一太平洋標準時間上午 09:45 與設定無關，僅為上下文記錄。

1. **建立專案目錄**：開啟終端機並建立新目錄，例如 "myproject"：
   - 指令：`mkdir myproject && cd myproject`

2. **初始化 npm 專案**：執行 `npm init -y` 建立帶有預設設定的 `package.json` 檔案，為專案設定 npm 相依性。

3. **安裝特定版本**：使用 npm 安裝所需版本：
   - 指令：`npm install webpack@1.13.2`
   - 指令：`npm install webpack-dev-server@1.14.0`
   - 這些指令會將指定版本加入 `node_modules` 並更新 `package.json` 中的 `dependencies`。

#### 目錄結構與檔案建立
為使開發伺服器正常運作，需建立基本目錄結構：
- 建立 `public` 目錄存放靜態檔案：`mkdir public`
- 建立 `src` 目錄存放應用程式碼：`mkdir src`

在 `public` 目錄內建立 `index.html` 檔案，這是提供應用程式服務的必備檔案：
```html
<html>
<body>
<script src="/bundle.js"></script>
</body>
</html>
```
此檔案引用 `bundle.js，該檔案將由 webpack 生成並提供。

在 `src` 目錄內建立 `index.js` 檔案並填入基本內容：
```javascript
console.log('Hello, World!');
```
這是 webpack 將進行打包的進入點。

#### 配置檔案設定
在根目錄建立 `webpack.config.js` 檔案來配置 webpack：
```javascript
const path = require('path');
module.exports = {
    entry: './src/index.js',
    output: {
        path: path.join(__dirname, 'dist'),
        filename: 'bundle.js'
    },
    devServer: {
        contentBase: path.join(__dirname, 'public')
    }
};
```
- `entry`：指定起始點（`src/index.js`）。
- `output`：定義打包檔案輸出位置（`dist/bundle.js`）。
- `devServer.contentBase`：指向用於提供靜態檔案（如 `index.html`）的 `public` 目錄。

請注意在 1.14.0 版中使用的是 `contentBase` 而非現代的 `static`，這反映了舊版 API 的特性。

#### 執行開發伺服器
使用以下指令啟動開發伺服器：
- 首選：`npx webpack-dev-server`
- 替代方案（若 npx 不可用）：`./node_modules/.bin/webpack-dev-server`

此指令將啟動伺服器，通常可透過 [http://localhost:8080](http://localhost:8080) 存取。伺服器在記憶體中運行，意味著檔案不會寫入磁碟而是動態提供，並啟用即時重新載入功能以方便開發。

#### 操作細節與注意事項
- **存取應用程式**：在瀏覽器中開啟 [http://localhost:8080](http://localhost:8080)。您應能看到 `index.html` 載入 `bundle.js` 並執行 JavaScript，在控制台記錄 "Hello, World!"。
- **即時更新**：編輯 `src` 中的檔案，伺服器將自動重新編譯並重新載入瀏覽器，這是 webpack-dev-server 用於迭代開發的關鍵功能。
- **連接埠衝突**：若連接埠 8080 被占用，伺服器可能無法啟動。可在 `webpack.config.js` 的 `devServer.port` 中指定其他連接埠，例如 `port: 9000`。

#### 檔案服務與路徑注意事項
考慮到版本特性，`devServer.contentBase` 會從指定目錄提供檔案（若未設定則預設為當前目錄）。請確保 `index.html` 位於 `public` 目錄中以便在根路徑提供服務。指令碼標籤 `<script src="/bundle.js"></script>` 能正常運作是因為 `output.publicPath` 預設為 '/'，且 `output.filename` 為 'bundle.js'，使其可透過 `/bundle.js` 路徑存取。

重要細節是 webpack-dev-server 1.14.0 需要 HTML 檔案才能提供服務，且不會自動注入指令碼，因此需在 `index.html` 中手動加入。這與現代設定中使用 `html-webpack-plugin` 等外掛自動化處理的方式形成對比。

#### 相容性與限制
這些版本發布於 2016 年，雖然功能正常，但缺乏現代功能與安全性更新。應檢查與當前 Node.js 版本（截至 2025 年 3 月）的相容性，因為舊版可能需要 Node.js 6 或 8，這些版本已不再支援。建議在當前 Node.js 版本（例如 20.x）上測試，但需準備應對可能的棄用警告。

#### 表格：版本詳情與使用說明
下表總結關鍵版本資訊與使用注意事項：

| 元件               | 版本    | 發布年份     | 關鍵使用須知                                      |
|--------------------|---------|--------------|-------------------------------------------------|
| Webpack            | 1.13.2  | 2016         | 模組打包工具，需配置進入點/輸出設定 |
| Webpack-Dev-Server | 1.14.0  | 2016         | 開發伺服器，使用 `contentBase` 處理靜態檔案 |

#### 進階配置選項
如需更多功能，可考慮在 `devServer` 中加入 `hot: true` 啟用熱模組替換：
```javascript
devServer: {
    contentBase: path.join(__dirname, 'public'),
    hot: true
}
```
這允許模組更新時無需完整頁面重新載入，提升開發速度。

#### 結論
此設定使用 webpack 1.13.2 和 webpack-dev-server 1.14.0 提供了基本但功能完整的開發環境。考慮到版本較舊，預期會與現代工作流程存在差異，例如手動檔案服務和與當前工具的潛在相容性問題。由於缺乏更新，不建議在生產環境使用這些版本，但對於舊版專案維護，本指南應已足夠。

#### 主要參考文獻
- [Webpack 文件詳細設定指南](https://webpack.js.org/)
- [Webpack-dev-server 配置選項](https://webpack.js.org configuration/dev-server/)