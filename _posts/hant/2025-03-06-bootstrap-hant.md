---
audio: false
generated: true
lang: hant
layout: post
title: 使用 Bootstrap 打造響應式網站
translated: true
---

要在前端開發中使用 Bootstrap，請按照以下步驟有效地整合和利用這個流行的框架來構建響應式和樣式化的網站：

### 1. **了解什麼是 Bootstrap**
Bootstrap 是一個廣泛使用的前端框架，旨在簡化響應式、移動優先的網站的創建。它提供：
- **預設計組件**：按鈕、導航欄、表單、卡片、模態框等。
- **網格系統**：用於創建適應不同屏幕尺寸的靈活佈局。
- **CSS 和 JavaScript**：用於樣式和互動功能。

通過在項目中包含 Bootstrap，您可以快速構建用戶界面，而無需編寫大量自定義 CSS 或 JavaScript。

---

### 2. **在 HTML 中包含 Bootstrap**
要開始使用 Bootstrap，您需要將其 CSS 和 JavaScript 文件添加到您的 HTML 中。有兩種主要方法：

#### **選項 1：使用 CDN（推薦快速開始）**
在 HTML 文件中添加以下鏈接：
- **CSS**：將此放在 `<head>` 部分以加載 Bootstrap 的樣式。
  ```html
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
  ```
- **JavaScript**：將此放在閉合 `</body>` 標籤之前以啟用互動組件（例如模態框、下拉菜單）。
  ```html
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
  ```

**注意**：`.bundle.min.js` 文件包括 Popper.js，這對於某些 Bootstrap 組件（如工具提示和彈出框）是必需的。請始終檢查 [官方 Bootstrap 文檔](https://getbootstrap.com/) 以獲取最新的 CDN 鏈接。

#### **選項 2：本地托管文件**
如果您更喜歡離線工作或需要自定義 Bootstrap：
- 從 [官方網站](https://getbootstrap.com/docs/5.3/getting-started/download/) 下載 Bootstrap 文件。
- 將 CSS 和 JS 文件提取到您的項目目錄中。
- 在 HTML 中鏈接它們：
  ```html
  <link rel="stylesheet" href="path/to/bootstrap.min.css">
  <script src="path/to/bootstrap.bundle.min.js"></script>
  ```

使用 CDN 對於小型項目或快速原型設計通常更方便。

---

### 3. **使用 Bootstrap 類和組件**
包含 Bootstrap 後，您可以使用其類來樣式化和結構化您的 HTML。

#### **網格系統**
Bootstrap 的 12 列網格系統有助於創建響應式佈局：
- 使用 `.container` 進行居中佈局。
- 使用 `.row` 定義行，使用 `.col`（帶有中斷點如 `col-md-4`）定義列。
範例：
```html
<div class="container">
  <div class="row">
    <div class="col-md-4">Column 1</div>
    <div class="col-md-4">Column 2</div>
    <div class="col-md-4">Column 3</div>
  </div>
</div>
```
- 在中等屏幕 (`md`) 及以上，每個列佔用 4 列的 12 個單位（寬度的三分之一）。
- 在較小的屏幕上，列默認垂直堆疊。使用中斷點如 `col-sm-`、`col-lg-` 等以獲取更多控制。

#### **組件**
Bootstrap 提供了可立即使用的 UI 元素。範例：
- **按鈕**：添加 `.btn` 和修飾符如 `.btn-primary`。
  ```html
  <button class="btn btn-primary">Click Me</button>
  ```
- **導航欄**：創建響應式導航欄。
  ```html
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#">Brand</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link" href="#">Home</a>
        </li>
      </ul>
    </div>
  </nav>
  ```
探索更多組件（卡片、表單、模態框等）在文檔中。

---

### 4. **自定義 Bootstrap**
Bootstrap 的默認樣式可以根據您的設計進行調整：
- **自定義 CSS**：通過在 Bootstrap CSS 鏈接後添加您自己的 CSS 文件來覆蓋樣式。
  ```html
  <link rel="stylesheet" href="custom.css">
  ```
  範例：
  ```css
  .btn-primary {
    background-color: #ff5733; /* 自定義橙色 */
  }
  ```
- **CSS 變量（Bootstrap 5）**：使用 CSS 變量修改主題。
  ```css
  :root {
    --bs-primary: #ff5733;
    --bs-primary-rgb: 255, 87, 51;
  }
  ```
- **Sass 自定義**：對於高級更改，下載 Bootstrap 的源文件，編輯 Sass 變量（例如 `$primary`），然後重新編譯 CSS。

對於大多數項目，添加自定義 CSS 就足夠了。

---

### 5. **確保可訪問性和性能**
- **可訪問性**：Bootstrap 包含一些可訪問性功能（例如 ARIA 屬性），但使用語義 HTML（例如 `<nav>`、`<main>`）並使用螢幕閱讀器進行測試以確保符合性。
- **性能**：Bootstrap 的完整 CSS 和 JS 文件可能很大。為了優化：
  - 使用 Bootstrap 的 Sass 文件或實用工具 API 創建自定義構建，僅使用您需要的組件。
  - 使用工具如 PurgeCSS 移除未使用的樣式。

---

### 6. **參考文檔**
[官方 Bootstrap 文檔](https://getbootstrap.com/docs/5.3/getting-started/introduction/) 是您的主要資源。它提供：
- 所有組件的詳細說明。
- 快速實現的代碼範例。
- 最新功能和最佳實踐的更新。

---

### 範例：簡單的 Bootstrap 頁面
這是一個基本的 HTML 文件，使用 Bootstrap：
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
    <button class="btn btn-primary">Click Me</button>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```
- `mt-4` 類添加頂部間距。
- `.btn.btn-primary` 類樣式化按鈕。

---

通過遵循這些步驟——將 Bootstrap 添加到您的項目中，使用其類，根據需要進行自定義並進行優化，您可以高效地構建現代、響應式的前端介面。從 CDN 方法開始，並探索文檔以發掘 Bootstrap 的全部潛力！