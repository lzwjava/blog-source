---
audio: false
generated: true
lang: hant
layout: post
title: 使用 Bootstrap 建立響應式網站
translated: true
type: note
---

要在前端開發中使用 Bootstrap，請遵循以下步驟，有效整合並運用這個熱門框架來建構響應式且美觀的網站：

### 1. **了解 Bootstrap 是什麼**
Bootstrap 是一個廣泛使用的前端框架，旨在簡化響應式、行動優先網站的建立。它提供：
- **預先設計的元件**：按鈕、導覽列、表單、卡片、模態框等。
- **網格系統**：用於建立適應不同螢幕尺寸的靈活版面配置。
- **CSS 和 JavaScript**：用於樣式設計和互動功能。

通過在專案中包含 Bootstrap，您可以快速建立使用者介面，無需編寫大量自訂 CSS 或 JavaScript。

---

### 2. **在 HTML 中包含 Bootstrap**
要開始使用 Bootstrap，您需要將其 CSS 和 JavaScript 檔案添加到 HTML 中。主要有兩種方法：

#### **選項 1：使用 CDN（快速入門推薦）**
將以下連結添加到您的 HTML 檔案：
- **CSS**：將其放在 `<head>` 部分以載入 Bootstrap 的樣式。
  ```html
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
  ```
- **JavaScript**：將其放在 `</body>` 結束標籤之前，以啟用互動元件（例如模態框、下拉選單）。
  ```html
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
  ```

**注意**：`.bundle.min.js` 檔案包含了 Popper.js，這是某些 Bootstrap 元件（如工具提示和彈出框）所必需的。請務必查閱 [官方 Bootstrap 文檔](https://getbootstrap.com/) 以獲取最新的 CDN 連結。

#### **選項 2：本地託管檔案**
如果您偏好離線工作或需要自訂 Bootstrap：
- 從 [官方網站](https://getbootstrap.com/docs/5.3/getting-started/download/) 下載 Bootstrap 檔案。
- 將 CSS 和 JS 檔案解壓縮到您的專案目錄中。
- 在 HTML 中連結它們：
  ```html
  <link rel="stylesheet" href="path/to/bootstrap.min.css">
  <script src="path/to/bootstrap.bundle.min.js"></script>
  ```

對於小型專案或快速原型設計，使用 CDN 通常更為方便。

---

### 3. **使用 Bootstrap 類別和元件**
一旦包含了 Bootstrap，您就可以使用其類別來設計和結構化您的 HTML。

#### **網格系統**
Bootstrap 的 12 欄網格系統有助於建立響應式版面配置：
- 使用 `.container` 來建立置中的版面配置。
- 使用 `.row` 定義行，並使用 `.col`（帶有斷點如 `col-md-4`）定義列。
範例：
```html
<div class="container">
  <div class="row">
    <div class="col-md-4">欄 1</div>
    <div class="col-md-4">欄 2</div>
    <div class="col-md-4">欄 3</div>
  </div>
</div>
```
- 在中等螢幕（`md`）及以上，每個欄位佔 12 個單位中的 4 個（寬度的三分之一）。
- 在較小的螢幕上，欄位預設會垂直堆疊。使用斷點如 `col-sm-`、`col-lg-` 等來進行更多控制。

#### **元件**
Bootstrap 提供即用型 UI 元素。範例：
- **按鈕**：添加 `.btn` 和修飾符如 `.btn-primary`。
  ```html
  <button class="btn btn-primary">點擊我</button>
  ```
- **導覽列**：建立響應式導覽列。
  ```html
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#">品牌</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link" href="#">首頁</a>
        </li>
      </ul>
    </div>
  </nav>
  ```
在文檔中探索更多元件（卡片、表單、模態框等）。

---

### 4. **自訂 Bootstrap**
Bootstrap 的預設樣式可以根據您的設計進行調整：
- **自訂 CSS**：在 Bootstrap CSS 連結之後添加您自己的 CSS 檔案來覆蓋樣式。
  ```html
  <link rel="stylesheet" href="custom.css">
  ```
  範例：
  ```css
  .btn-primary {
    background-color: #ff5733; /* 自訂橙色 */
  }
  ```
- **CSS 變數（Bootstrap 5）**：使用 CSS 變數修改主題。
  ```css
  :root {
    --bs-primary: #ff5733;
    --bs-primary-rgb: 255, 87, 51;
  }
  ```
- **Sass 自訂**：對於進階更改，請下載 Bootstrap 的原始檔案，編輯 Sass 變數（例如 `$primary`），然後重新編譯 CSS。

對於大多數專案，添加自訂 CSS 已經足夠。

---

### 5. **確保無障礙性和效能**
- **無障礙性**：Bootstrap 包含一些無障礙功能（例如 ARIA 屬性），但請使用語義化 HTML（例如 `<nav>`、`<main>`）並使用螢幕閱讀器進行測試以確保符合標準。
- **效能**：Bootstrap 的完整 CSS 和 JS 檔案可能較大。要優化：
  - 僅使用您需要的元件，通過 Bootstrap 的 Sass 檔案或實用程式 API 建立自訂建置。
  - 使用 PurgeCSS 等工具移除未使用的樣式。

---

### 6. **參考文檔**
[官方 Bootstrap 文檔](https://getbootstrap.com/docs/5.3/getting-started/introduction/) 是您的主要資源。它提供：
- 所有元件的詳細說明。
- 快速實作的程式碼範例。
- 最新功能和最佳實踐的更新。

---

### 範例：一個簡單的 Bootstrap 頁面
這是一個使用 Bootstrap 的基本 HTML 檔案：
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bootstrap 範例</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body>
  <div class="container">
    <h1 class="mt-4">Hello, Bootstrap!</h1>
    <button class="btn btn-primary">點擊我</button>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```
- `mt-4` 類別添加了上邊距間距。
- `.btn.btn-primary` 類別設計了按鈕的樣式。

---

通過遵循這些步驟——將 Bootstrap 添加到您的專案中，使用其類別，根據需要進行自訂和優化——您可以高效地建立現代、響應式的前端介面。從 CDN 方法開始，並探索文檔以釋放 Bootstrap 的全部潛力！