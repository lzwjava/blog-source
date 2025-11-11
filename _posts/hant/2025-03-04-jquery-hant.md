---
audio: false
generated: true
lang: hant
layout: post
title: 使用 jQuery
translated: true
type: note
---

看來您參考的是 `package.json` 檔案中的片段，其中 `"jquery": "^3.1.0"` 表示對 jQuery 的依賴關係並設定了版本限制。讓我解釋這個版本語法的意義，並指導您如何整合及使用 jQuery。

### 理解 `"jquery": "^3.1.0"`
- `^` 符號表示允許更新至與版本 `3.1.0` 相容的 jQuery 版本，但不包括 `4.0.0`。因此您會獲得 `3.1.1`、`3.2.0` 等版本，但不會升級到 `4.0.0`。
- 這是 Node.js/npm 套件管理的一部分，通常出現在 JavaScript 專案的 `package.json` 檔案中。

### 在專案中使用 jQuery 的步驟

#### 1. **安裝 jQuery**
假設您正在使用 Node.js 環境與 npm：
- 在專案資料夾中開啟終端機。
- 執行以下指令安裝 jQuery：
  ```bash
  npm install jquery
  ```
- 這會將 jQuery（版本 `>=3.1.0` 但 `<4.0.0`）下載到您的 `node_modules` 資料夾，並將其加入 `package.json`。

#### 2. **在專案中包含 jQuery**
根據您的設定，有幾種使用 jQuery 的方式：

##### **在瀏覽器中（純 HTML）**
- 如果未使用打包工具（如 Webpack 或 Parcel），可以透過 CDN 或從 `node_modules` 引入 jQuery：
  ```html
  <!DOCTYPE html>
  <html>
  <head>
      <title>我的頁面</title>
      <!-- 使用 CDN -->
      <script src="https://code.jquery.com/jquery-3.1.0.min.js"></script>
  </head>
  <body>
      <button id="myButton">點擊我</button>
      <script>
          // jQuery 程式碼
          $(document).ready(function() {
              $("#myButton").click(function() {
                  alert("按鈕已點擊！");
              });
          });
      </script>
  </body>
  </html>
  ```

##### **在使用打包工具的 Node.js 專案中**
- 如果使用如 Webpack 等工具：
  - 在 JavaScript 檔案（例如 `index.js`）中導入 jQuery：
    ```javascript
    import $ from 'jquery';

    $(document).ready(function() {
        $("#myButton").click(function() {
            console.log("按鈕已點擊！");
        });
    });
    ```
  - 確保 HTML 包含了打包後的輸出檔案（例如 `<script src="dist/bundle.js"></script>`）。

##### **不使用打包工具（使用 `require`）**
- 在簡單的 Node.js 設定中：
  ```javascript
  const $ = require('jquery');
  // 注意：jQuery 通常需要 DOM（瀏覽器環境）才能完全運作。
  // 在 Node.js 中，您可能需要使用如 `jsdom` 的函式庫來模擬 DOM。
  ```

#### 3. **jQuery 基本用法**
以下是常見 jQuery 操作的簡單範例：
```javascript
// 等待文件載入完成
$(document).ready(function() {
    // 透過 ID 選取元素並更改其文字
    $("#myElement").text("Hello, jQuery!");

    // 加入點擊事件
    $("button").click(function() {
        $(this).css("background-color", "yellow");
    });

    // 操作多個元素
    $(".myClass").hide();
});
```
- `$` 是 jQuery 函式（別名為 `jQuery`）。
- `#myElement` 目標為 ID，`.myClass` 目標為類別，`button` 目標為所有 `<button>` 標籤。

#### 4. **驗證功能**
- 在瀏覽器中開啟 HTML 檔案或執行 Node.js 應用程式。
- 檢查控制台或使用者介面是否符合預期行為（例如按鈕點擊、文字變更）。

### 疑難排解
- **404 錯誤**：確保 jQuery 指令碼正確載入（檢查路徑或 CDN）。
- **$ 未定義**：確保在執行您的指令碼之前已載入 jQuery。
- **Node.js 環境**：如果在沒有瀏覽器的 Node.js 中使用，需要 DOM 模擬器如 `jsdom`。

如果您有更具體的使用情境（例如特定的 jQuery 功能或專案類型），請告訴我，我會進一步調整說明！