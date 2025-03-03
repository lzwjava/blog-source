---
audio: false
generated: true
lang: hant
layout: post
title: 使用 jQuery
translated: true
---

看來你正在引用一個來自 `package.json` 文件的片段，其中 `"jquery": "^3.1.0"` 指定了一個對 jQuery 的依賴，並附帶版本限制。讓我來解釋如何在項目中使用 jQuery，以及該版本語法的意義，然後指導你如何整合和使用它。

### 了解 `"jquery": "^3.1.0"`
- `^` 符號表示你允許 jQuery 的更新，這些更新與版本 `3.1.0` 兼容，但不包括版本 `4.0.0`。因此，你會得到 `3.1.1`、`3.2.0` 等，但不會得到 `4.0.0`。
- 這是 Node.js/npm 套件管理的一部分，通常在 JavaScript 項目的 `package.json` 文件中找到。

### 在項目中使用 jQuery 的步驟

#### 1. **安裝 jQuery**
假設你在 Node.js 環境中使用 npm：
- 在項目資料夾中打開你的終端。
- 運行以下命令來安裝 jQuery：
  ```bash
  npm install jquery
  ```
- 這會將 jQuery（版本 `>=3.1.0` 但 `<4.0.0`）下載到你的 `node_modules` 資料夾，並將其添加到你的 `package.json`。

#### 2. **在項目中包含 jQuery**
根據你的設置，有幾種使用 jQuery 的方法：

##### **在瀏覽器中（純 HTML）**
- 如果你不使用打包工具（如 Webpack 或 Parcel），可以通過 CDN 或從 `node_modules` 包含 jQuery：
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
          // jQuery 代碼
          $(document).ready(function() {
              $("#myButton").click(function() {
                  alert("按鈕被點擊！");
              });
          });
      </script>
  </body>
  </html>
  ```

##### **在使用打包工具的 Node.js 項目中**
- 如果你使用像 Webpack 這樣的工具：
  - 在你的 JavaScript 文件（例如 `index.js`）中導入 jQuery：
    ```javascript
    import $ from 'jquery';

    $(document).ready(function() {
        $("#myButton").click(function() {
            console.log("按鈕被點擊！");
        });
    });
    ```
  - 確保你的 HTML 包含打包後的輸出文件（例如 `<script src="dist/bundle.js"></script>`）。

##### **不使用打包工具（使用 `require`）**
- 在簡單的 Node.js 設置中：
  ```javascript
  const $ = require('jquery');
  // 注意：jQuery 通常需要 DOM（瀏覽器環境）才能完全工作。
  // 在 Node.js 中，你可能需要像 `jsdom` 這樣的庫來模擬 DOM。
  ```

#### 3. **基本 jQuery 使用**
這是一些常見 jQuery 操作的快速示例：
```javascript
// 等待文件準備就緒
$(document).ready(function() {
    // 通過 ID 選擇元素並更改其文本
    $("#myElement").text("你好，jQuery！");

    // 添加點擊事件
    $("button").click(function() {
        $(this).css("background-color", "yellow");
    });

    // 操作多個元素
    $(".myClass").hide();
});
```
- `$` 是 jQuery 函數（也別名為 `jQuery`）。
- `#myElement` 目標 ID，`.myClass` 目標類，`button` 目標所有 `<button>` 標籤。

#### 4. **驗證它是否工作**
- 在瀏覽器中打開你的 HTML 文件或運行你的 Node.js 應用。
- 檢查控制台或 UI 以查看預期的行為（例如，按鈕點擊、文本更改）。

### 錯誤排除
- **404 錯誤**：確保 jQuery 腳本正確加載（檢查路徑或 CDN）。
- **$ 未定義**：確保在腳本運行之前包含 jQuery。
- **Node.js 環境**：如果在沒有瀏覽器的 Node.js 中使用，你需要像 `jsdom` 這樣的 DOM 模擬器。

如果你有更具體的用例（例如特定的 jQuery 功能或項目類型），請告訴我，我會進一步針對這些進行調整！