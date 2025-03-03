---
audio: false
generated: true
lang: hant
layout: post
title: Font Awesome 套件在 NPM
translated: true
---

### 主要要點
- 似乎使用 "font-awesome" npm 套件（版本 4）的方法是先用 `npm install font-awesome` 安裝它，然後在 HTML 中連結 CSS 文件，並使用像 `<i class="fa fa-home"></i>` 這樣的類別來使用圖標。
- 研究顯示版本 4 已過時且不再維護；考慮升級到版本 6 以獲取更新和安全性，使用像 `@fortawesome/fontawesome-free` 這樣的套件。

---

### 安裝和基本使用
要開始使用 "font-awesome" npm 套件（版本 4），首先使用命令 `npm install font-awesome` 安裝它。安裝完成後，在 HTML 中添加 `<link rel="stylesheet" href="node_modules/font-awesome/css/font-awesome.min.css">` 來包含 CSS 文件。然後可以在網頁中使用圖標，添加像 `<i class="fa fa-home"></i>` 的 HTML，將 `fa-home` 替換為所需的圖標名稱，可以在 [Font Awesome 版本 4 文檔](https://fontawesome.com/v4/cheatsheet) 中找到。

### 其他方法
如果使用像 webpack 這樣的構建工具，可以在 JavaScript 文件中直接導入 CSS，使用 `import 'font-awesome/css/font-awesome.min.css';`。對於使用 Less 或 Sass 的項目，可以導入相應的文件，例如在 Less 中使用 `@import "node_modules/font-awesome/less/font-awesome";`，確保路徑根據需要進行調整。

### 版本說明
一個意外的細節是 "font-awesome" 套件是版本 4，已經超過八年未更新且不再維護。為了獲得最新功能和安全性，考慮升級到版本 6，可通過 `@fortawesome/fontawesome-free`（免費）或 `@fortawesome/fontawesome-pro`（專業版，需要訂閱）獲取。使用 `npm install @fortawesome/fontawesome-free` 安裝版本 6，並使用 `import '@fortawesome/fontawesome-free/css/all.min.css';` 導入。更多詳細信息請參閱 [Font Awesome 文檔](https://fontawesome.com/docs/web/use-with/node-js)。

---

### 調查說明：使用 Font Awesome npm 套件的全面指南

本節提供了使用 "font-awesome" npm 套件的詳細探討，重點放在版本 4 上，同時也涉及到轉換到更新的版本 6。這些信息來自官方文檔、npm 套件詳細信息和社區討論，確保開發者在各個層次上都能充分理解。

#### 背景和上下文
"font-awesome" npm 套件，如在 [npm](https://www.npmjs.com/package/font-awesome) 上列出的，對應於 Font Awesome 的 4.7.0 版本，最後發布於八年前，這使其成為一個較舊的、現已結束生命週期的版本。Font Awesome 是一個流行的可縮放矢量圖標工具包，廣泛用於網頁開發中將圖標添加到網站。版本 4 主要依賴 CSS 來實現圖標，使用字體文件，以其簡單性著稱，但缺乏後來版本中的現代功能和更新。

由於其年齡，版本 4 的文檔仍可在 [Font Awesome 版本 4 文檔](https://fontawesome.com/v4/) 中訪問，但官方網站現在專注於版本 6，版本 4 被認為是結束生命週期的，如在 [FortAwesome/Font-Awesome](https://github.com/FortAwesome/Font-Awesome) 的 GitHub 談論中所指出的。這一轉變強調了考慮升級以進行持續項目的重要性，特別是出於安全性和功能增強的原因。

#### 使用 "font-awesome" 套件（版本 4）通過 npm
要使用 "font-awesome" 套件，請按照以下步驟進行操作，這些步驟與標準的 npm 實踐和社區使用相一致：

1. **安裝：**
   - 在項目目錄中運行命令 `npm install font-awesome`。這將安裝 4.7.0 版本，將文件放置在 `node_modules/font-awesome` 目錄中。
   - 該套件包括 CSS、Less 和字體文件，如其 npm 描述中所詳細說明的，該描述提到維護在語義版本控制下，並包括 Less 使用的說明。

2. **在 HTML 中包含：**
   - 針對基本使用，在 HTML 頭部鏈接 CSS 文件：
     ```html
     <link rel="stylesheet" href="node_modules/font-awesome/css/font-awesome.min.css">
     ```
   - 確保路徑正確；如果 HTML 不是在根目錄中，請相應調整（例如，`../node_modules/font-awesome/css/font-awesome.min.css`）。

3. **使用圖標：**
   - 圖標使用 HTML 如 `<i class="fa fa-home"></i>`，其中 `fa` 是基礎類，`fa-home` 指定圖標。完整列表可在 [Font Awesome 版本 4 圖標表](https://fontawesome.com/v4/cheatsheet) 中找到。
   - 這種方法利用了包含的字體文件，確保可縮放性和 CSS 自定義。

4. **與構建工具的替代整合：**
   - 如果使用像 webpack 這樣的構建工具，在 JavaScript 中導入 CSS：
     ```javascript
     import 'font-awesome/css/font-awesome.min.css';
     ```
   - 這種方法在現代網頁開發中很常見，確保 CSS 打包到項目中。

5. **Less 和 Sass 支持：**
   - 對於使用 Less 的項目，可以直接導入文件，如社區討論中所建議的：
     ```less
     @import "node_modules/font-awesome/less/font-awesome";
     ```
   - 類似地，對於 Sass，根據需要調整路徑，雖然該套件主要支持 Less 版本 4，如在 Ruby Gem 為 Rails 的整合中所見，包括 `font-awesome-less` 和 `font-awesome-sass`。

#### 實際考量和社區見解
社區討論，例如在 Stack Overflow 上，揭示了常見的做法，如將文件複製到公共目錄以進行生產，使用 gulp 任務，或導入特定的 Less 組件以減少打包大小。例如，一個用戶建議僅導入必要的 Less 文件以節省字節，雖然指出節省不多，指出：
   - `@import "@{fa_path}/variables.less";`
   - `@import "@{fa_path}/mixins.less";` 等，調整 `@fa_path` 為 `"../node_modules/font-awesome/less"`。

然而，對於大多數用戶，直接鏈接 CSS 文件即可，特別是對於小型到中型項目。該 npm 套件的內容還提到 Bundler 和 Less 插件要求，建議高級用戶進行額外設置，例如：
   - 全局安裝 Less 使用 `npm install -g less`。
   - 使用 Less 插件 Clean CSS 使用 `npm install -g less-plugin-clean-css`。

#### 關於版本 4 的限制和升級路徑
版本 4 雖然功能齊全，但已不再支持，僅對版本 5 提供關鍵錯誤修復，版本 3 和 4 都標記為結束生命週期，如 [FortAwesome/Font-Awesome GitHub](https://github.com/FortAwesome/Font-Awesome) 所指出的。這意味著沒有新功能、安全補丁或更新，這對於長期項目來說是一個重大問題。

升級到版本 6 引入了顯著變化，包括 SVG 與 JavaScript、新樣式（Solid、Regular、Light、Duotone、Thin）和分離的品牌圖標。要轉換，安裝 `@fortawesome/fontawesome-free` 使用：
   - `npm install @fortawesome/fontawesome-free`
   - 使用 `import '@fortawesome/fontawesome-free/css/all.min.css';` 導入，注意 CSS 文件名從版本 6 更改為 `all.min.css`，反映更廣泛的圖標支持。

詳細升級說明請參閱 [Font Awesome 從版本 4 升級](https://fontawesome.com/docs/web/setup/upgrade/upgrade-from-v4)，包括兼容性說明和移除版本 4 文件的步驟，確保平滑過渡。

#### 比較表：版本 4 與版本 6 使用

| 方面                  | 版本 4 (font-awesome)                     | 版本 6 (@fortawesome/fontawesome-free)    |
|-------------------------|---------------------------------------------|---------------------------------------------|
| 安裝命令                | `npm install font-awesome`                  | `npm install @fortawesome/fontawesome-free` |
| CSS 文件名               | `font-awesome.min.css`                      | `all.min.css`                               |
| 圖標使用示例              | `<i class="fa fa-home"></i>`                | `<i class="fas fa-home"></i>` (Solid 樣式) |
| 維護狀態                | 結束生命週期，無更新                     | 活躍維護，最新版本 6.7.2                   |
| 額外功能                | 基本 CSS，Less 支持                     | SVG 與 JS，多種樣式，API 支持               |
| 文檔 URL                | [版本 4 文檔](https://fontawesome.com/v4/) | [版本 6 文檔](https://fontawesome.com/docs/web/use-with/node-js) |

這張表強調了演變，幫助開發者在升級決策中做出選擇。

#### 結論和建議
對於新項目，強烈考慮使用版本 6 以獲取其活躍支持和現代功能。對於使用版本 4 的現有項目，評估升級路徑，特別是出於安全原因，考慮到八年的差距。提供的步驟確保了與版本 4 的功能，但未來的方法在於採用版本 6，詳細指導請參閱 [Font Awesome 文檔](https://fontawesome.com/docs/web/use-with/node-js)。

這個全面指南確保用戶擁有所有必要的信息，從基本安裝到高級整合，同時強調在快速變化的技術環境中更新的重要性。

---

### 主要引用
- [Font Awesome 版本 4 文檔與圖標表](https://fontawesome.com/v4/)
- [font-awesome 套件在 npm 上的版本 4.7.0 詳細信息](https://www.npmjs.com/package/font-awesome)
- [FortAwesome Font-Awesome GitHub 存儲庫與版本歷史](https://github.com/FortAwesome/Font-Awesome)