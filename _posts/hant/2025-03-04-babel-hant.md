---
audio: false
generated: true
lang: hant
layout: post
title: 適用於瀏覽器兼容性的Babel套件
translated: true
type: note
---

### 重點摘要
- 這些 Babel 套件很可能用於將現代 JavaScript (ES2015) 編譯成舊版本以實現瀏覽器兼容性，特別是在基於 webpack 的前端專案中。
- 研究顯示設定步驟包括安裝特定版本、建立 `.babelrc` 檔案，以及配置 webpack 使用 `babel-loader`。
- 證據顯示這些舊版本的兼容性問題應該較少，但仍需確保所有套件正確安裝。

### 安裝步驟
首先，使用以下指令安裝套件：

```bash
npm install --save-dev \
  "babel-core@6.13.0" \
  "babel-loader@6.2.5" \
  "babel-plugin-transform-runtime@6.12.0" \
  "babel-preset-es2015@6.13.2" \
  "babel-runtime@6.11.6"
```

### 配置設定
在專案根目錄建立 `.babelrc` 檔案，內容如下：

```json
{
  "presets": ["es2015"],
  "plugins": ["transform-runtime"]
}
```

接著，按以下方式設定 `webpack.config.js`：

```javascript
module.exports = {
  entry: './index.js',
  output: {
    filename: 'bundle.js'
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        loader: 'babel-loader',
        options: {
          configFile: './.babelrc'
        }
      }
    ]
  }
};
```

### 使用方式
在 `index.js` 等檔案中編寫 ES2015 JavaScript 程式碼，然後執行 `npx webpack` 將其編譯成 `bundle.js，讓舊版瀏覽器能夠理解。

### 意外細節
令人意外的是這些都是舊版本 (Babel 6)，現已由 Babel 7 取代而棄用，這可能會影響長期維護，但對於遺留專案來說仍可接受。

---

### 調查筆記：Babel 套件的詳細設定與使用

本節提供在 JavaScript 專案中使用指定 Babel 套件的完整指南——特別是針對使用 webpack 的前端開發。考慮到版本號，這些屬於 Babel 6 系列，是較舊但仍可運作的套件組合，用於將現代 JavaScript (ES2015) 轉譯為 ES5 以實現更廣泛的瀏覽器兼容性。以下詳細說明安裝、配置、使用方式及注意事項，確保開發者能在遺留或特定專案中完整理解。

#### 背景與目的
Babel 是一個 JavaScript 編譯器，能將現代語法轉換成較舊且廣泛支援的版本。列出的套件屬於 Babel 6，這是在 Babel 7 重大更新之前普遍使用的版本。`babel-core@6.13.0` 提供核心編譯功能，`babel-loader@6.2.5` 則與 webpack 整合用於前端建置。`babel-preset-es2015@6.13.2` 啟用 ES2015 (ECMAScript 2015) 到 ES5 的轉換，而 `babel-plugin-transform-runtime@6.12.0` 與 `babel-runtime@6.11.6` 則透過外部化輔助函數來優化程式碼，減少重複。

考慮到當前日期為 2025 年 3 月 3 日，這些版本明顯已過時，Babel 7 及以上版本才是現行標準。然而對於遺留專案或特定需求，它們仍然相關。使用者的查詢暗示在 webpack 環境中設定的需求，但同時也考慮了 Babel CLI 等替代方案。

#### 安裝流程
首先使用 npm 將套件安裝為開發依賴。指令確保安裝指定確切版本：

```bash
npm install --save-dev \
  "babel-core@6.13.0" \
  "babel-loader@6.2.5" \
  "babel-plugin-transform-runtime@6.12.0" \
  "babel-preset-es2015@6.13.2" \
  "babel-runtime@6.11.6"
```

此步驟會將它們加入 `package.json` 的 `devDependencies`，確保在建置過程中可用但不會打包到生產環境。請注意，在某些設定中 `babel-runtime` 通常是執行時依賴，但在此處考慮到外掛因素，為保持一致性而將其視為開發依賴。

#### 配置細節
配置主要涉及兩個檔案：用於 Babel 設定的 `.babelrc` 和用於 webpack 整合的 `webpack.config.js`。

##### `.babelrc` 檔案
在專案根目錄建立或編輯 `.babelrc`，內容如下：

```json
{
  "presets": ["es2015"],
  "plugins": ["transform-runtime"]
}
```

- **Presets**：`"es2015"` 對應 `babel-preset-es2015@6.13.2`，啟用所有 ES2015 到 ES5 的轉換，例如箭頭函數、let/const 和類別。
- **Plugins**：`"transform-runtime"` 使用 `babel-plugin-transform-runtime@6.12.0` 來外部化 Babel 輔助函數，引用 `babel-runtime@6.11.6`，透過避免跨檔案重複輔助函數來減少編譯後的程式碼大小。

此配置確保 ES2015 程式碼被轉譯並針對執行時效率進行優化。

##### Webpack 配置
對於 webpack，建立或更新 `webpack.config.js` 如下：

```javascript
module.exports = {
  entry: './index.js',
  output: {
    filename: 'bundle.js'
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        loader: 'babel-loader',
        options: {
          configFile: './.babelrc'
        }
      }
    ]
  }
};
```

- **Entry 和 Output**：指定 `index.js` 為進入點，輸出 `bundle.js`。
- **Module Rules**：對 `.js` 檔案使用 `babel-loader@6.2.5`，指向 `.babelrc` 作為選項來源，確保在打包前由 Babel 處理檔案。

此設定利用 webpack 的模組系統來處理 JavaScript 檔案，透過 Babel 進行編譯。

#### 使用方式與工作流程
設定完成後，在 `index.js` 等檔案中編寫 ES2015 程式碼。例如：

```javascript
const arr = [1, 2, 3];
const sum = arr.reduce((a, b) => a + b, 0);
console.log(sum);
```

執行建置指令：

```bash
npx webpack
```

這會將程式碼編譯成 `bundle.js`，可將其包含在 HTML 中用於瀏覽器執行，確保與舊環境兼容。`transform-runtime` 外掛確保輔助函數共享，減少打包檔案大小，對於大型專案特別有用。

#### 替代用法：Babel CLI
雖然查詢建議使用 webpack 設定，但為求完整，可考慮使用 Babel CLI 進行無需 webpack 的手動編譯。首先安裝 `babel-cli@6.13.0`：

```bash
npm install --save-dev "babel-cli@6.13.0"
```

然後使用以下指令編譯檔案：

```bash
./node_modules/.bin/babel src/index.js -o lib/index.js
```

或加入 `package.json` 的 scripts：

```json
"scripts": {
  "build": "babel src --out-dir lib"
}
```

使用 `npm run build` 執行，會將編譯後的檔案輸出到 `lib/`，適用於 Node.js 專案或伺服器端程式碼。

#### 兼容性與注意事項
考慮到版本號（均屬 Babel 6，發布於數年前），在相同主版本內通常能確保兼容性。但請注意：

- `babel-loader@6.2.5` 與 webpack 1 和 2 相容，請確保您的 webpack 版本（例如 `webpack@1.14.0`）相容。
- 這些套件已被棄用，由 Babel 7 取代，後者使用作用域套件如 `@babel/core`。對於長期專案，建議考慮升級，但對於遺留專案，這些套件仍可正常運作。
- 確保沒有命名衝突；使用者的清單中有空格（例如 "babel loader"），可能是拼寫錯誤，已修正為連字號（例如 `babel-loader`）。

#### 潛在問題
- 確保 `.babelrc` 位於專案根目錄，或在 webpack 選項中指定路徑。
- 確認 `babel-runtime` 已安裝，因為 `transform-runtime` 依賴它提供輔助函數。
- 檢查安裝過程中有無棄用警告，考慮到這些版本的年代，但它們應該能如預期般運作。

#### 表格：套件角色與版本

| 套件名稱                     | 版本    | 角色                                                                 |
|------------------------------|---------|----------------------------------------------------------------------|
| `babel-core`                 | 6.13.0  | Babel 的核心編譯功能。                                               |
| `babel-loader`               | 6.2.5   | Webpack 的 Babel 加載器，用於編譯 JavaScript 檔案。                  |
| `babel-plugin-transform-runtime` | 6.12.0 | 用於外部化輔助函數的外掛，減少程式碼重複。                          |
| `babel-preset-es2015`        | 6.13.2  | 用於 ES2015 到 ES5 轉換的預設組，啟用現代語法。                     |
| `babel-runtime`              | 6.11.6  | 為 `transform-runtime` 外掛提供輔助函數的執行時函式庫。             |

此表格總結了各套件在設定中的角色，有助於理解其用途。

#### 意外細節：遺留環境背景
一個有趣的細節是這些都是 Babel 6 版本，現已棄用，而 Babel 7 引入了作用域套件（例如 `@babel/core`）。這種設定在遺留專案中很典型，雖然功能正常，但可能缺乏現代功能，例如更好的 TypeScript 支援或 Babel 7 中的效能優化，這對於習慣當前標準的開發者來說可能出乎意料。

#### 結論
本指南涵蓋了在基於 webpack 的前端專案中設定指定 Babel 套件的步驟，並提供了 Babel CLI 的替代方案。考慮到版本號，請確保與 webpack 1 或 2 兼容，並注意棄用情況，但對於預期用途，它應該能無縫運作。更多詳細資訊請參閱提供的文件連結。

#### 主要參考文獻
- [babel-loader webpack documentation](https://webpack.js.org/loaders/babel-loader/)
- [babel preset-es2015 npm package](https://www.npmjs.com/package/babel-preset-es2015)
- [babel plugin-transform-runtime npm package](https://www.npmjs.com/package/babel-plugin-transform-runtime)
- [babel runtime npm package](https://www.npmjs.com/package/babel-runtime)
- [Webpack official documentation](https://webpack.js.org/)