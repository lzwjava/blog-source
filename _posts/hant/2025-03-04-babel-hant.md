---
audio: false
generated: true
lang: hant
layout: post
title: 瀏覽器相容性的 Babel 套件
translated: true
---

### 主要要點
- 這些 Babel 套件似乎用於將現代 JavaScript (ES2015) 編譯成較舊的版本，以確保瀏覽器兼容性，特別是在基於 webpack 的前端項目中。
- 研究表明，設置過程涉及安裝特定版本、創建一個 `.babelrc` 文件，並配置 webpack 使用 `babel-loader`。
- 證據顯示，這些較舊版本的兼容性問題可能較少，但請確保所有套件都正確安裝。

### 安裝
首先，使用以下命令安裝套件：

```bash
npm install --save-dev \
  "babel-core@6.13.0" \
  "babel-loader@6.2.5" \
  "babel-plugin-transform-runtime@6.12.0" \
  "babel-preset-es2015@6.13.2" \
  "babel-runtime@6.11.6"
```

### 配置
在項目根目錄中創建一個 `.babelrc` 文件，內容如下：

```json
{
  "presets": ["es2015"],
  "plugins": ["transform-runtime"]
}
```

然後，設置您的 `webpack.config.js` 如下：

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

### 使用
在 `index.js` 等文件中編寫您的 ES2015 JavaScript 代碼，然後運行 `npx webpack` 將其編譯成 `bundle.js`，這樣較舊的瀏覽器就能理解。

### 意外細節
一個意外的方面是這些都是較舊的版本（Babel 6），現在已被 Babel 7 取代，這可能會影響長期維護，但對於遺留項目來說是可以的。

---

### 調查筆記：詳細設置和使用 Babel 套件

這一部分提供了有關使用指定 Babel 套件的全面指南——`babel-core@6.13.0`、`babel-loader@6.2.5`、`babel-plugin-transform-runtime@6.12.0`、`babel-preset-es2015@6.13.2` 和 `babel-runtime@6.11.6`——在 JavaScript 項目中，特別是使用 webpack 的前端開發。考慮到這些版本，這些都是 Babel 6 的一部分，這是一個較舊但仍然功能齊全的套件，用於將現代 JavaScript (ES2015) 轉譯為 ES5，以實現更廣泛的瀏覽器兼容性。以下詳細說明了安裝、配置、使用和考慮事項，確保開發人員在處理遺留項目或特定項目時能夠全面理解。

#### 背景和目的
Babel 是一個 JavaScript 編譯器，將現代語法轉換為較舊、更廣泛支持的版本。列出的套件來自 Babel 6，這是在 Babel 7 發布之前的主要版本。`babel-core@6.13.0` 提供了核心編譯功能，而 `babel-loader@6.2.5` 將與 webpack 集成以進行前端構建。`babel-preset-es2015@6.13.2` 使 ES2015（ECMAScript 2015）轉換為 ES5，而 `babel-plugin-transform-runtime@6.12.0` 以及 `babel-runtime@6.11.6` 通過外部化幫助函數來優化代碼，減少重複。

考慮到當前日期，2025 年 3 月 3 日，這些版本顯著過時，Babel 7 及其以上版本已成為標準。然而，對於遺留項目或特定需求，它們仍然相關。用戶的查詢暗示需要在 webpack 環境中設置，考慮到 `babel-loader` 的包含，儘管也考慮了 Babel CLI 等替代方案。

#### 安裝過程
首先，使用 npm 將套件安裝為開發依賴。命令確保安裝指定的版本：

```bash
npm install --save-dev \
  "babel-core@6.13.0" \
  "babel-loader@6.2.5" \
  "babel-plugin-transform-runtime@6.12.0" \
  "babel-preset-es2015@6.13.2" \
  "babel-runtime@6.11.6"
```

這一步將它們放在 `package.json` 下的 `devDependencies` 中，確保它們在構建過程中可用，但在生產中不會打包。請注意，`babel-runtime` 通常是某些設置中的運行時依賴，但在此，考慮到插件，它被視為開發依賴，以與轉換保持一致。

#### 配置詳細信息
配置涉及兩個主要文件：`.babelrc` 用於 Babel 設置，`webpack.config.js` 用於 webpack 集成。

##### `.babelrc` 文件
在項目根目錄中創建或編輯 `.babelrc`，內容如下：

```json
{
  "presets": ["es2015"],
  "plugins": ["transform-runtime"]
}
```

- **Presets**：`"es2015"` 對應於 `babel-preset-es2015@6.13.2`，啟用所有 ES2015 轉換為 ES5，例如箭頭函數、let/const 和類。
- **Plugins**：`"transform-runtime"` 使用 `babel-plugin-transform-runtime@6.12.0` 來外部化 Babel 幫助程序，參考 `babel-runtime@6.11.6`，這樣可以通過避免幫助程序在文件之間重複來減少編譯代碼的大小。

這種配置確保 ES2015 代碼被轉譯並優化以實現運行時效率。

##### Webpack 配置
對於 webpack，創建或更新 `webpack.config.js` 如下：

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

- **Entry 和 Output**：指定 `index.js` 作為入口點，並輸出 `bundle.js`。
- **Module Rules**：對於 `.js` 文件使用 `babel-loader@6.2.5`，指向 `.babelrc` 以獲取選項，確保 Babel 在打包之前處理文件。

這種設置利用 webpack 的模塊系統來處理 JavaScript 文件，通過 Babel 編譯它們。

#### 使用和工作流程
完成設置後，在 `index.js` 等文件中編寫您的 ES2015 代碼。例如：

```javascript
const arr = [1, 2, 3];
const sum = arr.reduce((a, b) => a + b, 0);
console.log(sum);
```

運行構建命令：

```bash
npx webpack
```

這將代碼編譯成 `bundle.js`，可以包含在 HTML 中以供瀏覽器執行，確保與較舊環境的兼容性。`transform-runtime` 插件確保幫助程序共享，減少了打包大小，這對於大型項目特別有用。

#### 替代使用：Babel CLI
儘管查詢建議使用 webpack 設置，但為了完整性，考慮使用 Babel CLI 進行手動編譯而不使用 webpack。首先，安裝 `babel-cli@6.13.0`：

```bash
npm install --save-dev "babel-cli@6.13.0"
```

然後，使用以下命令編譯文件：

```bash
./node_modules/.bin/babel src/index.js -o lib/index.js
```

或者，將其添加到 `package.json` 腳本中：

```json
"scripts": {
  "build": "babel src --out-dir lib"
}
```

使用 `npm run build` 運行，這將輸出編譯後的文件到 `lib/`，對於 Node.js 項目或服務器端代碼非常有用。

#### 兼容性和考慮事項
考慮到這些版本（所有都是 Babel 6，發布多年），在同一個主要版本內通常可以確保兼容性。然而，請注意：

- `babel-loader@6.2.5` 可以與 webpack 1 和 2 一起使用，因此請確保您的 webpack 版本（例如 `webpack@1.14.0`）兼容。
- 這些套件已被 Babel 7 取代，後者使用了作用域套件（例如 `@babel/core`）。對於長期項目，考慮升級，但對於遺留項目，這些仍然可以正常工作。
- 確保沒有命名衝突；用戶的列表中有空格（例如，“babel loader”），可能是拼寫錯誤，更正為連字符（例如 `babel-loader`）。

#### 可能的陷阱
- 確保 `.babelrc` 在項目根目錄中，或者在 webpack 選項中指定路徑。
- 驗證 `babel-runtime` 是否已安裝，因為 `transform-runtime` 依賴於它來提供幫助程序。
- 安裝過程中檢查過時警告，考慮到這些版本的年齡，但它們應該能夠按預期運行。

#### 表：套件角色和版本

| 套件名稱                  | 版本 | 角色                                                                 |
|-------------------------------|---------|----------------------------------------------------------------------|
| `babel-core`                  | 6.13.0  | Babel 的核心編譯功能。                            |
| `babel-loader`                | 6.2.5   | Webpack 加載器，編譯 JavaScript 文件。                  |
| `babel-plugin-transform-runtime` | 6.12.0 | 插件，外部化幫助程序，減少代碼重複。             |
| `babel-preset-es2015`         | 6.13.2  | 將 ES2015 轉換為 ES5 的預設設置，啟用現代語法。      |
| `babel-runtime`               | 6.11.6  | 提供幫助程序的運行時庫，用於 `transform-runtime` 插件。     |

這張表總結了每個套件的角色，有助於理解它們在設置中的用途。

#### 意外細節：遺留背景
一個有趣的方面是這些都是 Babel 6 版本，現在已被 Babel 7 取代，後者引入了作用域套件（例如 `@babel/core`）。這種設置對於遺留項目來說是典型的，儘管功能齊全，但可能缺乏 Babel 7 中的現代功能，例如更好的 TypeScript 支持或性能優化，這對於習慣於當前標準的開發人員來說可能是意外的。

#### 結論
這份指南涵蓋了在基於 webpack 的前端項目中設置指定 Babel 套件的內容，並提供了 Babel CLI 的替代方案。考慮到這些版本，請確保與 webpack 1 或 2 兼容，並注意過時問題，但對於預期用途，它應該能夠無縫運行。有關更多詳細信息，請參考提供的文檔鏈接。

#### 關鍵引用
- [babel-loader webpack 文檔](https://webpack.js.org/loaders/babel-loader/)
- [babel preset-es2015 npm 套件](https://www.npmjs.com/package/babel-preset-es2015)
- [babel plugin-transform-runtime npm 套件](https://www.npmjs.com/package/babel-plugin-transform-runtime)
- [babel runtime npm 套件](https://www.npmjs.com/package/babel-runtime)
- [Webpack 官方文檔](https://webpack.js.org/)