---
audio: false
generated: true
lang: hant
layout: post
title: NPM 中的 Font Awesome 套件
translated: true
type: note
---

### 重點摘要
- 若要使用 "font-awesome" npm 套件（版本 4），似乎需要先透過 `npm install font-awesome` 指令安裝，然後在 HTML 中連結 CSS 檔案，並使用如 `<i class="fa fa-home"></i>` 的類別來顯示圖示。
- 研究顯示版本 4 已過時且不再維護；建議升級至版本 6 以獲取更新和安全性修復，可使用如 `@fortawesome/fontawesome-free` 等套件。

---

### 安裝與基本用法
要開始使用 "font-awesome" npm 套件（版本 4），請先透過指令 `npm install font-awesome` 進行安裝。安裝完成後，在 HTML 中加入 `<link rel="stylesheet" href="node_modules/font-awesome/css/font-awesome.min.css">` 來引入 CSS 檔案。接著您就可以在網頁中使用如 `<i class="fa fa-home"></i>` 的 HTML 程式碼來顯示圖示，將 `fa-home` 替換為您想要的圖示名稱，圖示名稱可在 [Font Awesome 版本 4 文件](https://fontawesome.com/v4/cheatsheet) 中找到。

### 替代方法
如果您使用像 webpack 這樣的建置工具，可以直接在 JavaScript 檔案中透過 `import 'font-awesome/css/font-awesome.min.css';` 導入 CSS。對於使用 Less 或 Sass 的專案，您可以導入相應的檔案，例如在 Less 中使用 `@import "node_modules/font-awesome/less/font-awesome";`，並確保路徑根據需要進行調整。

### 版本注意事項
一個值得注意的細節是 "font-awesome" 套件是版本 4，該版本已超過八年未更新且不再維護。為了獲得最新功能和安全性，建議升級至版本 6，可透過 `@fortawesome/fontawesome-free`（免費版）或 `@fortawesome/fontawesome-pro`（專業版，需訂閱）取得。使用 `npm install @fortawesome/fontawesome-free` 安裝版本 6，並透過 `import '@fortawesome/fontawesome-free/css/all.min.css';` 導入。更多詳細資訊請參閱 [Font Awesome 文件](https://fontawesome.com/docs/web/use-with/node-js)。

---

### 調查說明：Font Awesome npm 套件完整使用指南

本節詳細探討如何使用 "font-awesome" npm 套件，重點關注版本 4，同時也說明如何過渡到較新的版本 6。這些資訊來自官方文件、npm 套件詳情和社群討論，確保各級開發者都能全面理解。

#### 背景與情境
"font-awesome" npm 套件（在 [npm](https://www.npmjs.com/package/font-awesome) 上列出）對應於 Font Awesome 的版本 4.7.0，該版本於八年前發布，屬於較舊且已停止支援的版本。Font Awesome 是一個用於可縮放向量圖示的熱門工具包，廣泛用於網頁開發中為網站添加圖示。版本 4 主要依賴 CSS 來實現圖示，使用字型檔案，以其簡單性著稱，但缺乏後續版本中的現代功能和更新。

考慮到其年代久遠，版本 4 的文件仍可在 [Font Awesome 版本 4 文件](https://fontawesome.com/v4/) 中訪問，但官方網站現在主要關注版本 6，版本 4 被視為已停止支援，如 [FortAwesome/Font-Awesome](https://github.com/FortAwesome/Font-Awesome) 的 GitHub 討論中所註明。這一轉變凸顯了在進行中的專案中考慮升級的重要性，特別是為了安全性和功能增強。

#### 透過 npm 使用 "font-awesome" 套件（版本 4）
要使用 "font-awesome" 套件，請遵循以下步驟，這些步驟符合標準的 npm 實踐和社群用法：

1. **安裝：**
   - 在您的專案目錄中執行指令 `npm install font-awesome`。這將安裝版本 4.7.0，並將檔案放置在 `node_modules/font-awesome` 目錄中。
   - 該套件包含 CSS、Less 和字型檔案，如其 npm 描述中所述，其中提到遵循語意化版本控制進行維護，並包含 Less 使用的說明。

2. **在 HTML 中引入：**
   - 對於基本用法，在 HTML 的 head 中連結 CSS 檔案：
     ```html
     <link rel="stylesheet" href="node_modules/font-awesome/css/font-awesome.min.css">
     ```
   - 確保路徑正確；如果您的 HTML 不在根目錄中，請相應調整（例如 `../node_modules/font-awesome/css/font-awesome.min.css`）。

3. **使用圖示：**
   - 使用如 `<i class="fa fa-home"></i>` 的 HTML 來使用圖示，其中 `fa` 是基礎類別，`fa-home` 指定圖示。完整列表可在 [Font Awesome 版本 4 速查表](https://fontawesome.com/v4/cheatsheet) 中找到。
   - 此方法利用包含的字型檔案，確保可縮放性和 CSS 自訂性。

4. **與建置工具的替代整合：**
   - 如果使用像 webpack 這樣的建置工具，在您的 JavaScript 中導入 CSS：
     ```javascript
     import 'font-awesome/css/font-awesome.min.css';
     ```
   - 這種方法在現代網頁開發中很常見，確保 CSS 與您的專案一起打包。

5. **Less 和 Sass 支援：**
   - 對於使用 Less 的專案，您可以直接導入檔案，如社群討論中所建議，例如：
     ```less
     @import "node_modules/font-awesome/less/font-awesome";
     ```
   - 類似地，對於 Sass，根據需要調整路徑，儘管該套件在版本 4 中主要支援 Less，如 Rails 的 Ruby Gem 整合中所見，其中包含 `font-awesome-less` 和 `font-awesome-sass`。

#### 實際考量與社群見解
社群討論（例如 Stack Overflow 上的討論）揭示了常見實踐，例如將檔案複製到公共目錄以供生產環境使用、使用 gulp 任務，或導入特定的 Less 組件以減少打包大小。例如，一位用戶建議僅導入必要的 Less 檔案以節省位元組，但指出節省有限，表明：
   - `@import "@{fa_path}/variables.less";`
   - `@import "@{fa_path}/mixins.less";` 等，將 `@fa_path` 調整為 `"../node_modules/font-awesome/less"`。

然而，對於大多數用戶來說，直接連結 CSS 檔案就足夠了，特別是對於中小型專案。該 npm 套件的內容還提到了 Bundler 和 Less 插件要求，建議進階用戶進行額外設置，例如：
   - 使用 `npm install -g less` 全域安裝 Less。
   - 使用 `npm install -g less-plugin-clean-css` 安裝 Less Plugin Clean CSS。

#### 關於版本 4 的限制和升級路徑的說明
版本 4 雖然功能正常，但不再受支援，關鍵錯誤修復僅在長期支援（LTS）下的版本 5 中提供，而版本 3 和 4 被標記為已停止支援，根據 [FortAwesome/Font-Awesome GitHub](https://github.com/FortAwesome/Font-Awesome)。這意味著沒有新功能、安全性修補程式或更新，這對於長期專案來說是一個重大問題。

對於升級，版本 6 引入了重大變更，包括 SVG 與 JavaScript、新樣式（Solid、Regular、Light、Duotone、Thin）以及分離的 Brand 圖示。要過渡，請安裝 `@fortawesome/fontawesome-free`：
   - `npm install @fortawesome/fontawesome-free`
   - 使用 `import '@fortawesome/fontawesome-free/css/all.min.css';` 導入，請注意從版本 6 開始，CSS 檔案名稱更改為 `all.min.css`，反映了更廣泛的圖示支援。

詳細的升級說明請參閱 [Font Awesome 從版本 4 升級](https://fontawesome.com/docs/web/setup/upgrade/upgrade-from-v4)，其中包括相容性說明和移除版本 4 檔案的步驟，確保平穩過渡。

#### 比較表格：版本 4 與版本 6 用法

| 方面                  | 版本 4 (font-awesome)                     | 版本 6 (@fortawesome/fontawesome-free)    |
|-------------------------|---------------------------------------------|---------------------------------------------|
| 安裝指令    | `npm install font-awesome`                  | `npm install @fortawesome/fontawesome-free` |
| CSS 檔案名稱           | `font-awesome.min.css`                      | `all.min.css`                               |
| 圖示使用範例      | `<i class="fa fa-home"></i>`                | `<i class="fas fa-home"></i>` (Solid 樣式) |
| 維護狀態      | 已停止支援，無更新                     | 積極維護，最新版本 6.7.2   |
| 附加功能     | 基本 CSS、Less 支援                     | SVG 與 JS、多樣式、API 支援   |
| 文件網址       | [版本 4 文件](https://fontawesome.com/v4/) | [版本 6 文件](https://fontawesome.com/docs/web/use-with/node-js) |

此表格突出了演變過程，有助於開發者做出升級決策。

#### 結論與建議
對於新專案，強烈建議使用版本 6，以獲得其積極支援和現代功能。對於現有使用版本 4 的專案，請評估升級路徑，特別是出於安全性考慮，考慮到八年的時間差距。提供的步驟確保了版本 4 的功能性，但面向未來的方法在於採用版本 6，詳細指南請參閱 [Font Awesome 文件](https://fontawesome.com/docs/web/use-with/node-js)。

本完整指南確保用戶擁有所有必要資訊，從基本安裝到進階整合，同時解決在快速發展的技術環境中進行更新的關鍵需求。

---

### 主要引用來源
- [Font Awesome 版本 4 文件與速查表](https://fontawesome.com/v4/)
- [npm 上的 font-awesome 套件，包含版本 4.7.0 詳情](https://www.npmjs.com/package/font-awesome)
- [FortAwesome Font-Awesome GitHub 儲存庫，包含版本歷史](https://github.com/FortAwesome/Font-Awesome)