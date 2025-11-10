---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Angular 深色模式元件檢查清單
translated: true
type: note
---

當你在 Angular 前端實作深色模式時，通常會從 `body`、`select` 和 `option` 開始，但還有不少其他常見的 HTML 元素需要重新設計樣式，以確保主題風格一致。以下是一份實用檢查清單：

### 頁面層級與容器

* `html`、`body` → 背景與文字顏色
* `div`、`section`、`article`、`aside`、`header`、`footer`、`main`、`nav` → 設定背景與文字顏色（特別是預設為白色背景的元素）

### 文字與標題

* `h1, h2, h3, h4, h5, h6` → 確保文字在深色背景上清晰可見
* `p`、`span`、`a` → 調整文字顏色、連結懸停顏色及已訪問連結狀態

### 表單與輸入欄位

* `input[type="text"]`、`input[type="password"]`、`input[type="email"]`、`textarea` → 背景、文字顏色與邊框
* `input[type="checkbox"]`、`input[type="radio"]` → 有時需要特殊處理以確保可見性
* `select`、`option` → 如你所提及，需設定背景與文字顏色
* `button` → 背景、邊框與文字顏色，以及懸停/啟用狀態
* `label` → 確保文字與深色背景形成對比
* `fieldset`、`legend` → 背景與邊框

### 清單與表格

* `ul`、`ol`、`li` → 文字顏色
* `table` → 背景、邊框顏色與文字顏色
* `thead`、`tbody`、`tr`、`th`、`td` → 個別調整背景與邊框

### 互動元素

* `details`、`summary` → 背景與文字
* `dialog` → 背景與文字
* `mark` → 螢光標記顏色需適應深色模式（預設黃色可能過於刺眼）

### 媒體與雜項

* `hr` → 邊框顏色（預設樣式在深色背景下通常過亮）
* `code`、`pre` → 背景與文字顏色以確保可讀性
* `blockquote` → 背景與邊框顏色
* `progress`、`meter` → 軌道與數值顏色

---

💡 **最佳實踐**：與其到處使用 `!important`，不如定義 CSS 變數（如 `--bg-color`、`--text-color` 等），並在深色模式啟用時切換它們（例如在 `body` 添加 `.dark-mode` 類別）。這樣 Angular 元件與自訂元素也能更整潔地接入主題。

需要我為你起草一份**基礎 CSS 程式碼片段**（含變數）嗎？你可以直接放入 Angular 專案作為深色模式的起始點。