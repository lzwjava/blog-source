---
audio: false
generated: true
lang: hant
layout: post
title: Font Awesome 問題
translated: true
type: note
---

「無法解析 .../fonts/fontawesome-webfont.woff2」錯誤通常發生在 Font Awesome CSS 檔案引用了指定路徑中找不到的字型檔案（如 `fontawesome-webfont.woff2`）。此問題常見於使用 npm、Webpack 或其他模組打包工具的專案中。以下步驟可協助解決此錯誤：

---

### 1. 驗證 Font Awesome 安裝
確保 Font Awesome 已正確安裝於專案中。

- **若使用 npm**：
  ```bash
  npm install @fortawesome/fontawesome-free
  ```
  此指令將安裝 Font Awesome 免費版。

- 檢查套件是否列於 `package.json`：
  ```json
  "dependencies": {
    "@fortawesome/fontawesome-free": "^6.x.x"
  }
  ```

---

### 2. 檢查 CSS 中的字型檔案路徑
此錯誤常因 `fontawesome.css` 檔案引用的相對路徑（如 `../fonts/fontawesome-webfont.woff2`）與專案檔案結構或建置流程不符所致。

- **定位 CSS 檔案**：
  在 `node_modules/@fortawesome/fontawesome-free/css/all.css`（或類似路徑）中找到 Font Awesome CSS 檔案。

- **檢查字型宣告**：
  開啟 CSS 檔案並尋找 `@font-face` 規則，內容可能如下：
  ```css
  @font-face {
    font-family: 'FontAwesome';
    src: url('../fonts/fontawesome-webfont.woff2') format('woff2'),
         url('../fonts/fontawesome-webfont.woff') format('woff');
  }
  ```

- **驗證字型檔案**：
  檢查 `node_modules/@fortawesome/fontawesome-free/webfonts/` 中是否存在被引用的字型檔案。`webfonts` 資料夾通常包含如 `fontawesome-webfont.woff2` 等檔案。

---

### 3. 修正路徑問題
若字型檔案無法被解析，可能需要調整建置流程中的路徑處理方式。

#### 選項 1：複製字型檔案至公開目錄
手動將字型檔案複製到應用程式可存取的目錄（如 `public/fonts` 或 `src/fonts`）。

- **複製檔案**：
  ```bash
  mkdir -p public/fonts
  cp -r node_modules/@fortawesome/fontawesome-free/webfonts/* public/fonts/
  ```

- **更新 CSS**：
  修改 `fontawesome.css` 檔案以指向新字型路徑：
  ```css
  @font-face {
    font-family: 'FontAwesome';
    src: url('/fonts/fontawesome-webfont.woff2') format('woff2'),
         url('/fonts/fontawesome-webfont.woff') format('woff');
  }
  ```

- 或使用 CSS 預處理器或後處理器重寫路徑。

#### 選項 2：配置 Webpack（或其他打包工具）
若使用 Webpack，請確保其能解析並載入字型檔案。

- **安裝 file-loader 或 url-loader**：
  ```bash
  npm install file-loader --save-dev
  ```

- **更新 Webpack 配置**（`webpack.config.js`）：
  新增處理字型檔案的規則：
  ```javascript
  module: {
    rules: [
      {
        test: /\.(woff|woff2|eot|ttf|otf)$/,
        use: [
          {
            loader: 'file-loader',
            options: {
              name: '[name].[ext]',
              outputPath: 'fonts/',
              publicPath: '/fonts/',
            },
          },
        ],
      },
    ],
  }
  ```

- 確保在 JavaScript 中匯入 Font Awesome CSS：
  ```javascript
  import '@fortawesome/fontawesome-free/css/all.css';
  ```

#### 選項 3：使用 CDN
若不想打包字型檔案，可透過 CDN 載入 Font Awesome。

- 在 HTML 中以 CDN 連結取代本地匯入：
  ```html
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" />
  ```

- 從程式碼中移除本地 Font Awesome CSS 匯入。

---

### 4. 檢查大小寫敏感性
部分系統（如 Linux）的檔案路徑區分大小寫。請確保 CSS 中的檔案名稱與路徑與實際檔案名稱完全相符。

- 例如，若實際檔案為 `fontawesome-webfont.woff2`，但 CSS 引用 `FontAwesome-WebFont.woff2`，則會導致失敗。

---

### 5. 清除快取並重新建置
有時舊快取會導致解析問題。

- 清除 npm 快取：
  ```bash
  npm cache clean --force
  ```

- 刪除 `node_modules` 與 `package-lock.json`，然後重新安裝：
  ```bash
  rm -rf node_modules package-lock.json
  npm install
  ```

- 重新建置專案：
  ```bash
  npm run build
  ```

---

### 6. 替代方案：透過 SCSS 使用 Font Awesome
若使用 SCSS，可匯入 Font Awesome 的 SCSS 檔案並配置字型路徑。

- 如前所述安裝 Font Awesome。
- 在主 SCSS 檔案中匯入 SCSS：
  ```scss
  $fa-font-path: '~@fortawesome/fontawesome-free/webfonts';
  @import '~@fortawesome/fontawesome-free/scss/fontawesome';
  @import '~@fortawesome/fontawesome-free/scss/solid';
  ```

- 確保 SCSS 編譯器能正確解析 `webfonts` 資料夾。

---

### 7. 除錯技巧
- **檢查瀏覽器主控台**：
  查看字型檔案的 404 錯誤及請求的 URL。
- **檢查建置輸出**：
  確認字型檔案已包含在輸出目錄中（如 `dist/fonts/`）。
- **使用 `resolve-url-loader`**：
  若在 Webpack 中使用 SCSS，可安裝 `resolve-url-loader` 協助解析相對 URL：
  ```bash
  npm install resolve-url-loader --save-dev
  ```

---

### 8. 若使用框架
部分框架（如 React、Vue、Angular）可能需要額外配置：

- **React**：
  確保在 `index.js` 或 `App.js` 中匯入 CSS：
  ```javascript
  import '@fortawesome/fontawesome-free/css/all.css';
  ```
  如有需要，請使用前述 Webpack 配置。

- **Vue**：
  若使用 Vue CLI，請將 Webpack 規則新增至 `vue.config.js`：
  ```javascript
  module.exports = {
    chainWebpack: (config) => {
      config.module
        .rule('fonts')
        .test(/\.(woff|woff2|eot|ttf|otf)$/)
        .use('file-loader')
        .loader('file-loader')
        .options({
          name: '[name].[ext]',
          outputPath: 'fonts/',
          publicPath: '/fonts/',
        });
    },
  };
  ```

- **Angular**：
  將 Font Awesome CSS 新增至 `angular.json`：
  ```json
  "styles": [
    "node_modules/@fortawesome/fontawesome-free/css/all.css",
    "src/styles.css"
  ]
  ```

---

### 9. 測試修正
- 執行開發伺服器：
  ```bash
  npm start
  ```
- 在瀏覽器中開啟應用程式，確認 Font Awesome 圖示正確載入且主控台無錯誤。

---

### 10. 若問題持續存在
- **檢查版本衝突**：
  確保未混用不同版本的 Font Awesome（如 v5 與 v6）。
- **搜尋類似問題**：
  於 Stack Overflow 或 GitHub 上查找與您設定相關的錯誤（如 Webpack、Create React App）。
- **提供更多細節**：
  若需進一步協助，請分享：
  - 專案設定（如 Webpack、React 等）。
  - 確切的錯誤訊息。
  - 相關程式碼片段（如匯入 Font Awesome 的方式）。

---

以上步驟應能解決「無法解析 .../fonts/fontawesome-webfont.woff2」錯誤。若需特定步驟的協助，請告知！