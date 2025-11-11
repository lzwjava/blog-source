---
audio: false
generated: true
lang: hant
layout: post
title: GitHub 的 Markdown 樣式
translated: true
type: note
---

### 重點摘要
- 使用 "github-markdown-css" npm 套件時，似乎需要先執行 `npm install github-markdown-css` 進行安裝。
- 研究顯示，接著需將 CSS 檔案匯入專案，並將 Markdown 內容包裹在帶有 "markdown-body" class 的 div 中。
- 證據傾向建議設定可選的寬度和內邊距以匹配 GitHub 風格，並確保使用 DOctype 以避免樣式問題。

### 安裝步驟
首先在專案目錄中使用 npm 安裝套件：
- 執行 `npm install github-markdown-css` 將其加入依賴項。

### 使用方法
安裝完成後，將 CSS 整合至專案：
- 匯入 CSS 檔案，例如在 JavaScript/React 中使用 `import 'github-markdown-css';`。
- 將渲染的 Markdown 內容包裹在 `<div class="markdown-body">...</div>` 中以應用樣式。
- 可選添加 CSS 設定寬度和內邊距以模擬 GitHub 外觀：
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
- 確保 HTML 包含 DOctype（例如 `<!DOCTYPE html>`）以防止觸發 quirks 模式影響樣式呈現。

### 意外細節
您可能沒想到，該套件還支援透過相關套件 [generate-github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css) 生成自定義 CSS，以滿足特定樣式需求。

---

### 調查備註：github-markdown-css npm 套件完整使用指南

本詳細指南深入探討 "github-markdown-css" npm 套件的使用方法，該套件專為在網頁專案中複製 GitHub 的 Markdown 樣式而設計。提供從安裝到整合的逐步說明，並針對不同開發環境（如 React 或純 HTML）給出進階使用建議。資訊來源涵蓋官方套件文件、GitHub 儲存庫及相關網路資源，確保各層級開發者都能獲得全面理解。

#### 背景與目的
由 [sindresorhus](https://github.com/sindresorhus) 維護的 "github-markdown-css" 套件，提供最精簡的 CSS 來模擬 GitHub 的 Markdown 渲染風格。對於希望文件或部落格文章能保持與 GitHub 一致清新風格的開發者特別實用。根據近期更新數據，該套件已被 npm 註冊表中超過 1,168 個專案使用，顯示其受歡迎程度與可靠性。

#### 安裝流程
首先需透過 Node.js 套件管理器 npm 安裝套件：
- 在專案目錄中執行 `npm install github-markdown-css`，此指令會將套件加入 `node_modules` 資料夾並更新 `package.json` 中的依賴項。

經查證，套件最新版本為 5.8.1，約三個月前發布，表明其持續維護狀態，這確保了與現代網頁開發實踐及框架的相容性。

#### 整合與應用
安裝完成後，下一步是將 CSS 整合至專案。套件提供名為 `github-markdown.css` 的檔案，可根據專案配置進行匯入：

- **JavaScript/現代框架（如 React、Vue）：**
  - 在 JavaScript 或 TypeScript 檔案中使用匯入語句，例如 `import 'github-markdown-css';`。此方式可與 Webpack 或 Vite 等打包工具完美配合。
  - 在 React 專案中，開發者通常會在元件檔案中匯入，確保樣式能全域或按需作用。

- **純 HTML 專案：**
  - 直接在 HTML 的 head 區塊連結 CSS 檔案：
    ```html
    <link rel="stylesheet" href="node_modules/github-markdown-css/github-markdown.css">
    ```
  - 請注意路徑可能因專案結構而異，需確保相對路徑正確指向 `node_modules` 目錄。

匯入後，透過將渲染的 Markdown 內容包裹在帶有 "markdown-body" class 的 `<div>` 中來應用樣式：
```html
<div class="markdown-body">
  <h1>Unicorns</h1>
  <p>All the things</p>
</div>
```
此 class 至關重要，因為 CSS 會針對 `.markdown-body` 內的元素應用 GitHub 風格樣式，包括排版、程式碼區塊、表格等元素。

#### 樣式設定注意事項
為完整複製 GitHub 的 Markdown 外觀，建議設定 `.markdown-body` 的寬度和內邊距。文件建議：
- 最大寬度 980px，大螢幕內邊距 45px，行動裝置（螢幕 ≤ 767px）內邊距 15px。
- 可透過以下 CSS 實現：
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
此設定確保響應式設計並符合 GitHub 設計規範，提升可讀性與使用者體驗。

#### 技術細節與最佳實踐
- **DOctype 要求：** 文件特別指出，若瀏覽器進入 quirks 模式可能導致樣式異常（例如深色模式下的表格渲染錯誤）。為避免此問題，請務必在 HTML 頂部宣告 DOctype，例如 `<!DOCTYPE html>`，以確保符合標準的渲染效果。
- **Markdown 解析：** 此套件僅提供 CSS 樣式，不包含 Markdown 到 HTML 的解析功能。您需要搭配 Markdown 解析器如 [marked.js](https://marked.js.org/) 或 React 專用的 [react-markdown](https://github.com/remarkjs/react-markdown) 來轉換 Markdown 文字。
- **自定義 CSS 生成：** 進階使用者可透過相關套件 [generate-github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css) 生成自定義 CSS，這對於特定主題需求或修改特別有用，是許多使用者未曾預期的進階功能。

#### 特定情境下的應用
- **React 專案：** 在 React 中常將 `github-markdown-css` 與 `react-markdown` 結合使用。安裝兩者後匯入 CSS 並使用元件：
  ```javascript
  import React from 'react';
  import ReactMarkdown from 'react-markdown';
  import 'github-markdown-css';

  const MarkdownComponent = () => (
    <div className="markdown-body">
      <ReactMarkdown># Hello, World!</ReactMarkdown>
    </div>
  );
  ```
  同時建議設定前述的寬度與內邊距 CSS 以完整實現 GitHub 風格。

- **使用 CDN 的純 HTML：** 快速原型開發時，可透過 [cdnjs](https://cdnjs.com/libraries/github-markdown-css) 直接使用 CDN 版本：
  ```html
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.8.1/github-markdown.min.css">
  ```
  接著如前所述應用 `.markdown-body` class。

#### 潛在問題與解決方案
- **樣式衝突：** 若專案使用其他 CSS 框架（如 Tailwind、Bootstrap），請確認沒有特異性衝突。雖然 `.markdown-body` class 應能覆蓋多數樣式，但仍需徹底測試。
- **深色模式支援：** 套件包含深色模式支援，但需確保 Markdown 解析器與專案設定能正確處理主題切換，特別是程式碼區塊和表格元素。
- **瀏覽器相容性：** 由於套件廣泛使用，相容性普遍良好，但仍建議在主流瀏覽器（Chrome、Firefox、Safari）中測試以確保渲染一致性。

#### 比較分析
相較於其他 Markdown CSS 方案（如 [Markdown CSS](https://markdowncss.github.io/)），"github-markdown-css" 的優勢在於直接複製 GitHub 風格，特別適合需要與 GitHub 外觀一致的文件。然而若需開箱即用的多主題支援，其他替代方案可能更適合。

#### 表格：主要功能與注意事項

| 功能要點             | 說明                                                                        |
|----------------------|-----------------------------------------------------------------------------|
| 安裝指令             | `npm install github-markdown-css`                                           |
| CSS 匯入方式         | `import 'github-markdown-css';` 或 HTML 中使用 `<link>`                     |
| 必要 Class           | `.markdown-body` 用於套用樣式                                               |
| 寬度與內邊距設定     | 最大 980px，內邊距 45px（桌面端）；15px（行動端 ≤ 767px）                   |
| DOctype 要求         | 必須宣告以避免 quirks 模式並確保正確渲染                                    |
| 自定義 CSS 生成      | 可透過 [generate-github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css) 實現 |
| 相容性               | 可搭配 marked.js、react-markdown 等解析器；支援多數瀏覽器                  |

#### 結論
對於希望複製 GitHub Markdown 樣式的開發者而言，"github-markdown-css" 的使用相當直觀。透過遵循安裝與整合步驟，並考量額外的樣式設定與技術細節，即可為 Markdown 內容實現一致且專業的外觀。進階自定義需求可探索生成套件，並建議在複雜專案中持續測試相容性與渲染問題。

#### 主要參考來源
- [github-markdown-css npm 套件頁面](https://www.npmjs.com/package/github-markdown-css)
- [複製 GitHub Markdown 風格的最精簡 CSS GitHub 儲存庫](https://github.com/sindresorhus/github-markdown-css)
- [GitHub Markdown CSS 演示頁面](https://sindresorhus.com/github-markdown-css/)
- [生成 github-markdown-css 的 npm 套件](https://www.npmjs.com/package/generate-github-markdown-css)
- [cdnjs 提供的 github-markdown-css CDN](https://cdnjs.com/libraries/github-markdown-css)