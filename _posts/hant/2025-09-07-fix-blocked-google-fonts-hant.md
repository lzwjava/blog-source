---
audio: false
date: 2025-09-07
generated: true
image: false
lang: hant
layout: post
title: 修復被封鎖的 Google 字型請求
translated: true
type: note
---

該請求是你的頁面嘗試從 Google Fonts 載入網頁字型樣式表：

* **這是什麼：** `https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap` 是定義 **Open Sans** 字型樣式的 CSS。你的主題或自訂 CSS 包含了它，以便網站能以 Open Sans 字型呈現。
* **為何會看到「狀態：— / 0 B / 無標頭」：** 當請求被**阻擋或取消**時（例如：被廣告/隱私阻擋器、嚴格的內容安全政策、不穩定的網路或國家級阻擋），DevTools 會顯示此訊息。頁面仍會*嘗試*請求，因此會出現在網路記錄中。

### 在 Jekyll 部落格中可能的來源

通常以下其中一項為真：

1. **主題在 `<head>` 中包含它**
   在 `_layouts/default.html` 或 `_includes/head.html`（或如果你使用 `remote_theme`，則在主題的對應檔案中）尋找類似這樣的程式碼：
   `<link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap" rel="stylesheet">`

2. **SCSS 匯入了它**
   在 `/assets/css/*.scss` 或 `/_sass/**` 中檢查是否有：
   `@import url("https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap");`

3. **遠端主題**（例如 jekyll-theme-cayman）在其 head include 中硬編碼了 Google Fonts。在你的儲存庫中覆寫主題的 head/layout 將允許你移除它。

### 如何快速找到它

從你的網站儲存庫根目錄，嘗試以下任一指令：

```
rg -n "fonts.googleapis.com"
rg -n "Open Sans"
rg -n "display=swap"
```

### 修復或變更的選項

**A) 移除 Google Fonts 並使用系統字型堆疊（最快且隱私友好）**

1. 刪除引入 Google Fonts 的 `<link>`（或 SCSS 中的 `@import`）。
2. 在你的主要樣式表中設定系統字型堆疊：

   ```css
   html, body {
     font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Ubuntu,
                  "Helvetica Neue", Arial, "Noto Sans", sans-serif,
                  "Apple Color Emoji", "Segoe UI Emoji";
   }
   ```

   （在 Jekyll 中，將此程式碼放入 `assets/css/style.scss`，並在頂部加上 front-matter `---` 行。）

**B) 保留 Open Sans 但自行託管**

1. 下載 Open Sans（400 和 700）的 WOFF2 檔案，並將其置於 `assets/fonts/` 目錄下。
2. 新增至你的 CSS：

   ```css
   @font-face {
     font-family: "Open Sans";
     font-style: normal;
     font-weight: 400;
     font-display: swap;
     src: url("/assets/fonts/OpenSans-400.woff2") format("woff2");
   }
   @font-face {
     font-family: "Open Sans";
     font-style: normal;
     font-weight: 700;
     font-display: swap;
     src: url("/assets/fonts/OpenSans-700.woff2") format("woff2");
   }
   body { font-family: "Open Sans", system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; }
   ```
3. 移除 Google Fonts 的 `<link>`/`@import`。

**C) 保持原樣但避免請求失敗**

* 為你的網站停用阻擋擴充功能，或放寬你的內容安全政策以允許 `https://fonts.googleapis.com` 和 `https://fonts.gstatic.com`。
* 如果你所在的區域這些網域被阻擋，建議選擇方案 A 或 B。

### Jekyll 專用的覆寫技巧

* **遠端主題：** 將主題的 `/_includes/head.html` 或 `/_layouts/default.html` 複製到你的儲存庫中的相同路徑，移除 Google Fonts 的程式碼行，Jekyll 將使用你的覆寫版本。
* **精簡的 head include：** 有時主題會透過變數注入字型。如果是這種情況，將該變數設為空值或覆寫 include 以排除字型。

如果你提供你的主題名稱（或你的 `_config.yml` 中的 `theme` / `remote_theme`），我可以顯示確切的覆寫檔案和最小差異。