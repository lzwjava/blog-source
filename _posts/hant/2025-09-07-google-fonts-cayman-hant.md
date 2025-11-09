---
audio: false
date: 2025-09-07
generated: true
image: false
lang: hant
layout: post
title: Cayman 主題中的 Google 字型匯入
translated: true
type: note
---

是的——這很可能就是原因。

當你寫入：

```scss
@import "jekyll-theme-cayman";
```

你並非僅僅引入某些本地 SCSS 檔案——而是匯入了整個**主題的樣式表**，而該樣式表本身包含（或連結至）Google Fonts 的引入。Cayman 使用 **Open Sans** 作為其預設字型，並從 `https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap` 獲取該字型。

因此流程如下：

1. 你的 SCSS 寫有 `@import "jekyll-theme-cayman";`。
2. Jekyll 將其擴展為主題的 `_sass` 檔案。
3. 在 Cayman 的 SCSS 內部，有一行類似這樣的程式碼：

   ```scss
   @import url("https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap");
   ```
4. 這就是你在 DevTools 中看到的網路請求。

---

### 如何移除或覆蓋

* **覆蓋字型引入**：將主題的主要 SCSS 複製到你的專案中（例如 `assets/css/style.scss`），刪除 Google Fonts 的那行程式碼，並告知 Jekyll 不要引入它。

* **僅覆蓋字型家族**：保留 Cayman 的其餘部分，但在你自己的 CSS 中強制使用系統字型堆疊：

  ```css
  html, body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Ubuntu,
                 "Helvetica Neue", Arial, "Noto Sans", sans-serif;
  }
  ```

  即使 Google Fonts 請求發生，瀏覽器也不會使用它。

* **自行託管 Open Sans**：如果你喜歡 Open Sans 但不想有外部呼叫，可以下載字型檔案並在你自己的 CSS 中使用 `@font-face` 定義它們，然後移除 Cayman 的 `@import url(...)`。

---

👉 如果你需要，我可以明確指出 Cayman 的哪個 SCSS 檔案包含 Google Fonts 的那行程式碼，以及如何在你的 Jekyll 設定中乾淨地覆蓋它。你需要我逐步詳細說明嗎？