---
audio: false
generated: true
lang: hant
layout: post
title: ES6 风格的 Promise
translated: true
---

### 主要要點
- 要在 npm 中使用 `es6-promise` 套件，首先使用 `npm install es6-promise` 安裝它。
- 然後可以在 JavaScript 代碼中引入它，以在本地使用 Promise 類別或為更廣泛的相容性進行全域補丁。
- 研究表明，現代環境支持原生承諾，因此這個套件主要是為了較舊的系統或特定需求。

### 安裝
在項目目錄中使用 npm 安裝套件：
- 運行命令：`npm install es6-promise`。

### 使用方法
使用這個套件有兩個主要選項：

#### 本地使用
如果你想在不影響全域範圍的情況下在代碼中使用 Promise 類別：
- 引入套件並像這樣使用它：
  ```javascript
  const Promise = require('es6-promise').Promise;
  // 然後按需使用 Promise，例如 new Promise((resolve, reject) => {...});
  ```

#### 全域補丁
為了確保全域 Promise 設定為 `es6-promise` 實現，特別是對於較舊的環境：
- 使用補丁方法：
  ```javascript
  require('es6-promise').polyfill();
  // 現在，全域 Promise 將使用 es6-promise 實現。
  ```
- 或者，為了自動補丁，你可以這樣做：
  ```javascript
  require('es6-promise/auto');
  ```

### 意外細節
請注意，`es6-promise` 已經六年多沒有更新，這可能會引起安全和與新 JavaScript 功能相容性的擔憂，儘管它在其預定用途上仍然有效。

---

### 調查筆記：詳細探討在 npm 中使用 `es6-promise` 套件

這一部分提供了在 npm 項目中使用 `es6-promise` 套件的全面概述，擴展了直接答案，並提供了額外的背景、技術細節和開發者考量。信息結構模仿專業文章，確保包含所有相關細節，並使用表格以便於理解。

#### `es6-promise` 簡介
`es6-promise` 套件是一個輕量級庫，設計為 ES6 风格承諾的補丁，提供了組織非同步代碼的工具。它在缺乏或不可靠的原生 ES6 Promise 支持的環境中特別有用，例如較舊的瀏覽器或舊版 Node.js。由於其最後更新時間是 2019 年，最新版本 4.2.8 發布於 2025 年 3 月 3 日，這是一個成熟但可能維護較少的解決方案，與現代替代方案相比。

#### 安裝過程
將 `es6-promise` 整合到項目中，通過 npm 安裝非常簡單。命令是：
- `npm install es6-promise`

這將套件安裝到 `node_modules` 目錄中，並更新 `package.json` 以包含依賴項。對於使用 Yarn 的用戶，替代方案是 `yarn add es6-promise`，儘管 npm 是這裡的重點，因為用戶的查詢。

| 安裝方法 | 命令                     |
|---------------------|-----------------------------|
| npm                 | `npm install es6-promise`   |
| Yarn                | `yarn add es6-promise`      |

這個套件已被廣泛採用，npm 註冊表中有 5,528 個其他項目使用它，這表明其在遺留或特定用例中的相關性。

#### 在 JavaScript 中使用
安裝後，`es6-promise` 可以在兩種主要方式下使用：在代碼中本地使用或作為全域補丁。選擇取決於項目的需求，特別是是否需要確保跨不同環境的相容性。

##### 本地使用
對於本地使用，你引入套件並直接訪問 Promise 類別。語法是：
- `const Promise = require('es6-promise').Promise;`

這允許你在不修改全域範圍的情況下在代碼中使用 Promise 類別。例如：
```javascript
const Promise = require('es6-promise').Promise;
const myPromise = new Promise((resolve, reject) => {
  resolve('成功！');
});
myPromise.then(result => console.log(result)); // 輸出：成功！
```

這種方法適合你的項目已經支持原生承諾，但你想要使用 `es6-promise` 進行特定操作或一致性。

##### 全域補丁
為了補丁全域環境，確保項目中所有 Promise 使用 `es6-promise` 實現，你可以調用補丁方法：
- `require('es6-promise').polyfill();`

這將全域 `Promise` 設定為 `es6-promise` 實現，這對於較舊的環境（例如 IE<9 或舊版 Node.js）特別有用，這些環境中原生承諾可能缺失或損壞。或者，為了自動補丁，你可以使用：
- `require('es6-promise/auto');`

"auto" 版本，文件大小為 27.78 KB（7.3 KB gzipped），自動提供或替換缺失或損壞的 `Promise`，簡化設置。例如：
```javascript
require('es6-promise/auto');
// 現在，全域 Promise 已經補丁，你可以在代碼的任何地方使用 new Promise(...)。
```

##### 瀏覽器使用
儘管用戶的查詢集中在 npm，但值得一提的是，對於瀏覽器環境，你可以通過 CDN 包含 `es6-promise`，例如：
- `<script src="https://cdn.jsdelivr.net/npm/es6-promise@4/dist/es6-promise.js"></script>`
- 也有生產用的縮減版本，例如 `es6-promise.min.js`。

然而，考慮到 npm 上下文，重點仍在 Node.js 使用。

#### 相容性和考量
這個套件是 rsvp.js 的子集，由 @jakearchibald 提取，並設計為模仿 ES6 Promise 行為。然而，有相容性注意事項需要考慮：
- 在 IE<9 中，`catch` 和 `finally` 是保留關鍵字，會導致語法錯誤。解決方案包括使用字符串表示法，例如 `promise['catch'](function(err) { ... });`，儘管大多數縮減器會自動修復這一點。
- 由於其最後更新時間是 2019 年，開發者應該評估 `es6-promise` 是否滿足當前的安全和相容性需求，特別是針對目標現代 JavaScript 環境，這些環境中原生承諾是標準。

npm 套件健康分析表明它每週下載超過 950 萬次，被認為是關鍵生態系統項目，擁有 7,290 個 GitHub 星標，這表明強大的歷史社群。然而，過去 12 個月沒有新版本，可能被視為已停止的項目，儘管根據存儲庫活動，維護被評為可持續。

#### TypeScript 和額外資源
對於 TypeScript 用戶，儘管查詢中沒有明確提到，請注意，類型定義可通過 `@types/es6-promise` 獲得，可通過 `npm i @types/es6-promise` 安裝。這是一個存根套件，因為 `es6-promise` 提供了自己的類型，但它對於確保類型安全非常有用。

要了解更多關於承諾的知識，文檔建議 [JavaScript Promises HTML5Rocks 文章](http://www.html5rocks.com/en/tutorials/es6/promises/)，該文章提供了詳細的 API 使用和模式。

#### 潛在陷阱和社群見解
一些用戶可能會遇到安裝問題，例如 404 錯誤，特別是在較舊系統上或依賴項配置不當的情況下。例如，清除 `node_modules` 並重新安裝可能解決這些問題，如社群討論中所見。此外，確保你的 Node.js 版本支持 CommonJS 要求，因為套件的結構。

#### 結論
總結來說，`es6-promise` 是確保 npm 項目中 ES6 Promise 相容性的有價值工具，特別是對於遺留環境。安裝簡單，使用 `npm install es6-promise`，並可以通過 `require('es6-promise').Promise` 本地使用或通過 `require('es6-promise').polyfill()` 或 `require('es6-promise/auto')` 全域使用。考慮到其年齡，評估其是否適合你項目的需求，特別是在現代 JavaScript 上下文中，原生承諾是標準。

#### 主要引用
- [es6-promise npm 套件詳細信息](https://www.npmjs.com/package/es6-promise)
- [es6-promise GitHub 存儲庫](https://github.com/stefanpenner/es6-promise)