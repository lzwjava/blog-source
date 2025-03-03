---
audio: false
generated: true
lang: hant
layout: post
title: GitHub 的 Markdown 格式
translated: true
---

### 主要要點
- 使用 "github-markdown-css" npm 套件似乎需要先用 `npm install github-markdown-css` 安裝。
- 研究顯示，接下來應該將 CSS 文件導入到項目中，並將 Markdown 內容包裹在一個帶有類別 "markdown-body" 的 div 中。
- 證據顯示，應該設置可選的寬度和填充以匹配 GitHub 的樣式，並確保有 DOctype 以避免樣式問題。

### 安裝
在項目目錄中使用 npm 安裝套件：
- 運行 `npm install github-markdown-css` 將其添加到依賴項中。

### 使用
安裝後，將 CSS 集成到項目中：
- 例如，在 JavaScript/React 中導入 CSS 文件，使用 `import 'github-markdown-css';`。
- 將渲染的 Markdown 內容包裹在 `<div class="markdown-body">...</div>` 中以應用樣式。
- 可選地，添加 CSS 以設置寬度和填充，以模仿 GitHub 的外觀：
  ```css
  .markdown-body {
    box-sizing: border-box;
    min-width: 200px;
    max-width: 980px;
    margin: 0 auto;
    padding: 45px;
  }
  @media (max-width: 767px) {
    .markdown-body {
      padding: 15px;
    }
  }
  ```
- 確保 HTML 包含 DOctype（例如 `<!DOCTYPE html>`），以防止怪異模式問題，這可能會影響樣式。

### 意外細節
您可能不會想到，該套件還支持通過相關套件 [generate-github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css) 生成自定義 CSS，如果需要定制樣式。

---

### 調查筆記：使用 github-markdown-css npm 套件的全面指南

這篇詳細指南探討了使用 "github-markdown-css" npm 套件，旨在在網頁項目中複製 GitHub 的 Markdown 樣式。它提供了安裝和集成的逐步方法，以及在各種開發環境（如 React 或純 HTML）中最佳使用的額外考量。信息來自官方套件文檔、GitHub 存儲庫和相關網絡資源，確保開發者在所有水平上都能全面理解。

#### 背景與目的
由 [sindresorhus](https://github.com/sindresorhus) 維護的 "github-markdown-css" 套件提供了一組最小的 CSS，以模仿 GitHub 的 Markdown 渲染樣式。這對於希望其 Markdown 內容（如文檔或部落格文章）外觀與 GitHub 的熟悉和乾淨的呈現一致的開發者特別有用。該套件被廣泛使用，npm 註冊表中有 1,168 個其他項目使用它，這表明其流行和可靠性。

#### 安裝過程
首先，您需要通過 npm（Node.js 套件管理器）安裝套件。命令非常簡單：
- 在項目目錄中執行 `npm install github-markdown-css`。這將套件添加到 `node_modules` 文件夾中，並更新 `package.json` 以包含依賴項。

該套件的最新版本（截至最近的檢查）是 5.8.1，最後發布約三個月前，這表明其活躍維護和更新。這確保了與現代網頁開發實踐和框架的兼容性。

#### 集成與使用
安裝後，下一步是將 CSS 集成到項目中。該套件提供了一個名為 `github-markdown.css` 的文件，您可以根據項目設置進行導入：

- **用於 JavaScript/現代框架（例如 React、Vue）：**
  - 在 JavaScript 或 TypeScript 文件中使用導入語句，例如 `import 'github-markdown-css';`。這與 Webpack 或 Vite 等打包器很好地一起工作，它們無縫地處理 CSS 導入。
  - 在 React 中，您可能會看到開發者在組件文件中導入它，確保樣式全局可用或按需可用。

- **用於純 HTML：**
  - 直接在 HTML 頭部部分鏈接 CSS 文件：
    ```html
    <link rel="stylesheet" href="node_modules/github-markdown-css/github-markdown.css">
    ```
  - 注意，路徑可能會根據項目結構而異；確保相對路徑正確指向 `node_modules` 目錄。

導入後，通過將渲染的 Markdown 內容包裹在帶有類別 "markdown-body" 的 `<div>` 中來應用樣式。例如：
```html
<div class="markdown-body">
  <h1>獨角獸</h1>
  <p>所有的東西</p>
</div>
```
這個類別至關重要，因為 CSS 針對 `.markdown-body` 中的元素應用 GitHub 樣式，包括排版、代碼塊、表格等。

#### 樣式考量
為了完全複製 GitHub 的 Markdown 外觀，考慮為 `.markdown-body` 類設置寬度和填充。文檔建議：
- 大屏幕的最大寬度為 980px，填充為 45px，移動設備（屏幕 ≤ 767px）的填充為 15px。
- 您可以使用以下 CSS 來實現：
  ```css
  .markdown-body {
    box-sizing: border-box;
    min-width: 200px;
    max-width: 980px;
    margin: 0 auto;
    padding: 45px;
  }
  @media (max-width: 767px) {
    .markdown-body {
      padding: 15px;
    }
  }
  ```
這確保了響應性並與 GitHub 的設計一致，增強了可讀性和用戶體驗。

#### 技術筆記和最佳實踐
- **DOctype 要求：** 文檔強調了潛在的樣式問題，例如在暗模式下錯誤渲染表格，如果瀏覽器進入怪異模式。為防止這一點，始終在 HTML 頂部包含 DOctype，例如 `<!DOCTYPE html>`。這確保了標準兼容的渲染並避免了意外行為。
- **Markdown 解析：** 雖然該套件提供了 CSS，但它不會將 Markdown 轉換為 HTML。您需要一個 Markdown 解析器，例如 [marked.js](https://marked.js.org/) 或 [react-markdown](https://github.com/remarkjs/react-markdown) 來將 Markdown 文本轉換為 HTML，然後可以使用這個 CSS 進行樣式設計。
- **自定義 CSS 生成：** 針對高級用戶，相關套件 [generate-github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css) 允許生成自定義 CSS，這對於特定主題或修改可能有用。這是對那些可能認為該套件僅用於直接使用的用戶的意外細節。

#### 特定上下文中的使用
- **React 項目：** 在 React 中，結合 `github-markdown-css` 和 `react-markdown` 是常見的。安裝兩者後，導入 CSS 並使用組件：
  ```javascript
  import React from 'react';
  import ReactMarkdown from 'react-markdown';
  import 'github-markdown-css';

  const MarkdownComponent = () => (
    <div className="markdown-body">
      <ReactMarkdown># 你好，世界！</ReactMarkdown>
    </div>
  );
  ```
  確保您也設置了早期顯示的寬度和填充 CSS，以獲得完整的 GitHub 樣式。

- **使用 CDN 的純 HTML：** 針對快速原型設計，您可以使用可在 [cdnjs](https://cdnjs.com/libraries/github-markdown-css) 找到的 CDN 版本，通過直接鏈接：
  ```html
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.8.1/github-markdown.min.css">
  ```
  然後像以前一樣應用 `.markdown-body` 類。

#### 潛在問題及解決方案
- **樣式衝突：** 如果您的項目使用其他 CSS 框架（例如 Tailwind、Bootstrap），請確保沒有特異性衝突。`.markdown-body` 類應該覆蓋大多數樣式，但請仔細測試。
- **暗模式支持：** 該套件包括對暗模式的支持，但請確保您的 Markdown 解析器和項目設置正確處理主題切換，特別是代碼塊和表格。
- **瀏覽器兼容性：** 由於該套件的廣泛使用，兼容性通常很好，但始終在主要瀏覽器（Chrome、Firefox、Safari）上測試，以確保一致的渲染。

#### 比較分析
與其他 Markdown CSS 選項（如 [Markdown CSS](https://markdowncss.github.io/)）相比，"github-markdown-css" 以其直接複製 GitHub 樣式而脫穎而出，使其非常適合鏡像 GitHub 外觀的文檔。然而，它在沒有額外自定義的情況下缺乏內置主題選項，而某些替代方案則提供多個主題。

#### 表：關鍵功能和考量

| 功能                  | 描述                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| 安裝命令     | `npm install github-markdown-css`                                           |
| CSS 導入方法        | `import 'github-markdown-css';` 或 `<link>` 在 HTML 中                         |
| 必要類           | `.markdown-body` 用於樣式應用                                    |
| 寬度和填充        | 最大 980px，45px 填充（桌面）；15px 填充（移動設備 ≤ 767px）            |
| DOctype 要求      | 避免怪異模式並確保正確渲染的必要條件                  |
| 自定義 CSS 生成    | 通過 [generate-github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css) 可能 |
| 兼容性            | 適用於 marked.js、react-markdown 等 Markdown 解析器；廣泛的瀏覽器支持 |

#### 結論
使用 "github-markdown-css" 對於尋求複製 GitHub 的 Markdown 樣式的開發者來說非常簡單。通過遵循安裝和集成步驟，並考慮額外的樣式和技術筆記，您可以為 Markdown 內容實現一致且專業的外觀。針對高級自定義，探索生成套件，並始終測試兼容性和渲染問題，特別是在複雜項目中。

#### 關鍵引用
- [github-markdown-css npm 套件頁面](https://www.npmjs.com/package/github-markdown-css)
- [GitHub 存儲庫](https://github.com/sindresorhus/github-markdown-css)
- [GitHub Markdown CSS 演示頁面](https://sindresorhus.com/github-markdown-css/)
- [npm 套件生成 CSS](https://www.npmjs.com/package/generate-github-markdown-css)
- [github-markdown-css CDN 由 cdnjs](https://cdnjs.com/libraries/github-markdown-css)