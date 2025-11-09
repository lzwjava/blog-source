---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: 開發依賴與建置工具
translated: true
type: note
---

### 開發依賴套件
這些套件僅在開發過程中使用，不會包含在最終構建版本中。

- **babel-core** (6.13.0): Babel 核心編譯器，用於將現代 JavaScript (ES6+) 轉譯為 ES5 以實現更廣泛的瀏覽器兼容性。
- **babel-loader** (6.2.5): Webpack 加載器，在構建過程中集成 Babel 進行 JavaScript 轉換。
- **babel-plugin-transform-runtime** (6.12.0): Babel 插件，可重複使用運行時輔助程式以減少轉譯後代碼的打包體積。
- **babel-preset-es2015** (6.13.2): Babel 預設配置，用於將 ES2015 (ES6) 功能編譯為 ES5。
- **babel-runtime** (6.11.6): 運行時函式庫，為 Babel 轉譯後的代碼提供 polyfill 和輔助程式。
- **cross-env** (^1.0.8): 跨平台設置環境變數（例如 NODE_ENV），無需考慮 shell 差異。
- **css-loader** (^0.23.1): 加載並處理 CSS 文件，解析導入和依賴關係。
- **detect-indent** (4.0.0): 檢測文件的縮排風格（空格/製表符）以保持格式一致。
- **exports-loader** (^0.6.3): 在不同上下文中提供模組導出（例如用於非 AMD 模組）。
- **extract-text-webpack-plugin** (^1.0.1): 將 CSS 從 JavaScript 打包文件中提取到獨立文件，以提升效能。
- **file-loader** (0.9.0): 處理文件加載（例如圖片），將其輸出到目標目錄並返回 URL。
- **html-webpack-plugin** (^2.22.0): 生成 HTML 文件並注入打包後的資源，簡化單頁應用程式設置。
- **rimraf** (^2.5.4): 跨平台遞歸文件刪除工具（類似 Unix 的 rm -rf）。
- **style-loader** (^0.13.1): 通過 style 標籤將 CSS 注入 DOM，實現動態加載。
- **stylus** (^0.54.5): 具表現力的語法 CSS 預處理器，可編譯為 CSS。
- **stylus-loader** (^2.1.1): Webpack 加載器，用於將 Stylus 文件處理為 CSS。
- **url-loader** (0.5.7): 對小文件（例如圖片）進行 Base64 編碼內聯處理，較大文件則輸出；可回退至 file-loader。
- **vue-hot-reload-api** (^1.2.0): 在開發過程中為 Vue.js 組件啟用熱模組替換功能。
- **vue-html-loader** (^1.0.0): Webpack 加載器，用於解析 Vue 單文件組件中的 HTML 模板。
- **vue-loader** (8.5.3): 加載並處理 Vue 單文件組件（.vue 文件）為 JavaScript 和 CSS。
- **vue-style-loader** (^1.0.0): 處理 Vue 組件中的 CSS，與 style-loader 集成。
- **webpack** (1.13.2): 模組打包工具，用於構建和優化 Web 資源（如 JS、CSS 和圖片）。
- **webpack-dev-server** (1.14.0): 開發伺服器，支援即時重新加載和熱模組替換功能。

### 運行時依賴套件
這些是包含在最終應用程式構建中的運行時套件。

- **debug** (^2.2.0): 除錯工具，支援命名空間日誌記錄和條件輸出（僅通過 DEBUG 環境變數啟用）。
- **es6-promise** (^3.0.2): 為舊版瀏覽器/環境提供 ES6 Promise API 的 polyfill。
- **font-awesome** (^4.6.3): 流行的圖標庫，通過 CSS 類提供可縮放向量圖標。
- **github-markdown-css** (^2.4.0): 用於 GitHub 風格 Markdown 樣式的 CSS。
- **highlight.js** (^9.6.0): 支援多種語言的代碼區塊語法高亮工具。
- **hls.js** (^0.7.6): 用 HTML5 視頻播放 HTTP Live Streaming (HLS) 視頻的 JavaScript 函式庫。
- **inherit** (^2.2.6): 用於 JavaScript 物件中經典和原型繼承的實用工具。
- **jquery** (^3.1.0): 快速、功能豐富的 JavaScript 函式庫，用於 DOM 操作、AJAX 和事件處理。
- **json-loader** (^0.5.4): 將 JSON 文件作為 JavaScript 模組加載。
- **leancloud-realtime** (^3.2.3): LeanCloud 即時通訊和數據同步服務的 SDK。
- **marked** (^0.3.6): 將 Markdown 轉換為 HTML 的 Markdown 解析器。
- **moment** (^2.14.1): 用於解析、驗證和格式化日期時間的日期時間操作函式庫。
- **moment-timezone** (^0.5.7): Moment.js 的擴展，用於處理時區和夏令時。
- **qiniu-js-sdk** (0.0.2): 用於與七牛雲存儲互動（上傳/下載文件）的 JavaScript SDK。
- **raw-loader** (^0.5.1): Webpack 加載器，將文件作為原始字符串加載（例如文本模板）。
- **rupture** (^0.6.1): Stylus 的媒體查詢擴展，為響應式設計提供斷點功能。
- **sprintf-js** (^1.0.3): JavaScript 的 sprintf 實現，用於帶佔位符的字符串格式化。
- **vue** (^1.0.26): 用於構建用戶界面的漸進式 MVVM 框架（v1.x，舊版本）。
- **vue-resource** (^0.6.1): Vue.js 的 HTTP 客戶端，用於簡化 AJAX/API 請求。
- **vue-router** (^0.7.13): Vue.js 的官方路由，支援單頁應用程式導航。
- **vue-spinner** (^1.0.2): Vue.js 的加載指示器/旋轉組件函式庫。
- **vue-weui** (^0.3.2): WeUI 組件的 Vue.js 封裝（用於微信風格界面的 UI 函式庫）。
- **weixin-js-sdk** (^1.2.0): 微信 JavaScript SDK，用於集成微信網頁功能（例如分享、掃描）。
- **weui** (^0.4.3): 受微信設計啟發的移動端界面 CSS 框架。
- **word-color** (^1.2.0): 根據哈希值或語言等因素為單詞著色的函式庫，可能用於熱力圖類效果。