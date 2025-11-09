---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 王垠博客技術架構分析
translated: true
type: note
---

[當然我在扯淡](https://www.yinwang.org/) 網站似乎是個自建部落格。根據提供的 HTML 原始碼分析：

- **框架**：主要採用 **Vue.js**（推測為第 3 版），可從 Vue 專用屬性如 `data-v-app`、用於作用域 CSS 的 `data-v-[hash]` 及元件引用（例如 `HomeView`、`PostView`、用於 Vue Router 處理導航的 `router-link-active`）看出端倪。
- **建置工具**：使用 **Vite** 進行打包和開發，可從 favicon（`/vite.svg`）、帶哈希檔名的預載模組腳本（例如 `/assets/index-DS_1rR7p.js`）及 Vite 輸出特有的整體資源結構得知。
- **樣式處理**：採用 **Tailwind CSS** 的 utility-first 類別（例如 `bg-gray-50 dark:bg-gray-900`、`flex items-center`、響應式前缀如 `sm:px-4`）。
- **其他觀察**：未發現伺服器端渲染標記（例如無 Nuxt.js 痕跡），故推測為靜態網站或客戶端渲染的 SPA。其內容結構（文章、標籤、分頁功能）顯示這是為個人部落格打造的簡易自訂架構，可能使用 Markdown 撰寫文章內容。

此網站 **並非全手動編寫**——HTML 是在建置過程中由 Vue 元件與模板自動生成。核心邏輯（路由、元件）以 JS/TS 編碼，最終輸出為經優化的靜態檔案。未發現使用 Hugo 或 Jekyll 等完整靜態網站生成器的跡象，較接近輕量級的 Vue + Vite 專案架構。

[當然我在扯淡](https://www.yinwang.org/)