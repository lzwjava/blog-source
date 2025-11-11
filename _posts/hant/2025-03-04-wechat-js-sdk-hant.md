---
audio: false
generated: true
lang: hant
layout: post
title: 微信 JS SDK
translated: true
type: note
---

### 重點摘要
- 要使用 "weixin-js-sdk" 版本 "^1.2.0"，似乎需要先透過 npm 安裝，然後在 JavaScript 程式碼中引入。
- 研究顯示您需要透過微信公眾號的詳細資料（如 appId 和伺服器端生成的簽名）進行配置。
- 證據傾向於遵循官方微信 JS SDK 文檔的使用方式，因為該套件是官方 SDK 的封裝。

### 安裝步驟
首先在您的專案目錄中使用 npm 安裝套件：
- 執行 `npm install weixin-js-sdk` 將其加入專案依賴。

### 引入與使用
在 JavaScript 檔案中引入 SDK，然後使用微信 API 進行配置和使用：
- ES6 使用 `import wx from 'weixin-js-sdk';`，CommonJS 使用 `const wx = require('weixin-js-sdk');`。
- 使用 `wx.config({ appId: '您的_app_id', timestamp: 您的時間戳記, nonceStr: '您的隨機字串', signature: '您的簽名', jsApiList: ['onMenuShareAppMessage'] });` 進行配置。
- 透過 `wx.ready()` 處理成功情況，透過 `wx.error()` 處理錯誤。

### 伺服器端設定
請注意，您需要擁有微信公眾號、綁定域名，並使用微信 API 在伺服器端生成簽名，因為這涉及敏感憑證。

---

### 調查筆記：使用 "weixin-js-sdk" 版本 "^1.2.0" 的詳細指南

本筆記提供關於使用 "weixin-js-sdk" 套件（特別是版本 "^1.2.0"）的完整指南。該套件是微信 JS SDK 的封裝，讓網頁開發者能在應用程式中利用微信的行動功能。此套件支援 CommonJS 和 TypeScript，適用於 browserify 和 webpack 等現代網頁開發環境。以下我們根據現有文檔和範例詳細說明流程，確保為實作提供全面理解。

#### 背景與情境
根據其 npm 清單顯示，"weixin-js-sdk" 套件旨在封裝官方微信 JS SDK 版本 1.6.0，目前 npm 上的最新版本為 1.6.5（截至 2025 年 3 月 3 日已發布一年）。套件描述強調其支援 CommonJS 和 TypeScript，表明它專為 Node.js 環境和現代打包工具設計。考慮到使用者指定 "^1.2.0"（允許從 1.2.0 到 2.0.0 之前的任何版本），且最新版本為 1.6.5，可以合理推斷與提供的指南相容，但應在官方文檔中檢查版本特定變更。

根據官方文檔，微信 JS SDK 是微信公眾平台提供的網頁開發工具包，支援分享、掃描 QR code 和定位服務等功能。該套件的 GitHub 儲存庫（由 yanxi123-com 維護）強調它是官方 SDK 的直接移植，使用說明指向[微信 JS SDK 文檔](https://developers.weixin.qq.com/doc/offiaccount/OA_Web_Apps/JS-SDK.html)。

#### 安裝流程
首先透過 npm（Node.js 專案的標準套件管理器）安裝套件。指令很簡單：
- 在專案目錄中執行 `npm install weixin-js-sdk`。這將下載與 "^1.2.0" 相容的最新版本（考慮到 npm 註冊表的當前狀態，可能是 1.6.5）。

使用 yarn 的使用者可以執行 `yarn add weixin-js-sdk`，確保將套件加入專案依賴。這一步驟至關重要，因為它將 SDK 整合到專案中，使其可在 JavaScript 檔案中引入。

#### 引入與初始設定
安裝完成後，下一步是將 SDK 引入程式碼。該套件支援 ES6 和 CommonJS 模組，滿足不同的開發偏好：
- ES6 使用 `import wx from 'weixin-js-sdk';` 置於 JavaScript 檔案頂部。
- CommonJS 使用 `const wx = require('weixin-js-sdk');`，這在未轉譯的 Node.js 環境中很常見。

此引入會暴露 `wx` 物件，這是與微信 JS API 互動的核心介面。請注意，與透過 script 標籤引入 SDK（使 `wx` 全域可用）不同，在打包環境（如 webpack）中透過 npm 引入可能需要確保 `wx` 附加到全域 window 物件以滿足某些使用情況，但套件的設計（考慮其 CommonJS 相容性）表明它內部處理了這一點。

#### 配置與使用
配置過程涉及設定 `wx.config`，這對於使用微信公眾號詳細資料初始化 SDK 至關重要。此步驟需要通常由伺服器端生成的參數（出於安全考慮）：
- **所需參數：** `debug`（布林值，用於除錯）、`appId`（您的微信 app ID）、`timestamp`（當前時間戳記，單位為秒）、`nonceStr`（隨機字串）、`signature`（使用 jsapi_ticket 和其他參數生成）和 `jsApiList`（您打算使用的 API 陣列，例如 `['onMenuShareAppMessage', 'onMenuShareTimeline']`）。

基本配置範例：
```javascript
wx.config({
    debug: true,
    appId: '您的_app_id',
    timestamp: 您的時間戳記,
    nonceStr: '您的隨機字串',
    signature: '您的簽名',
    jsApiList: ['onMenuShareAppMessage', 'onMenuShareTimeline']
});
```

配置後處理結果：
- 使用 `wx.ready(function() { ... });` 在配置驗證成功後執行程式碼。您可以在這裡呼叫微信 API，例如分享：
  ```javascript
  wx.ready(function () {
      wx.onMenuShareAppMessage({
          title: '您的標題',
          desc: '您的描述',
          link: '您的連結',
          imgUrl: '您的圖片 URL',
          success: function () {
              // 分享成功的回呼
          },
          cancel: function () {
              // 分享取消的回呼
          }
      });
  });
  ```
- 使用 `wx.error(function(res) { ... });` 處理配置錯誤，這可能表示簽名或域名設定有問題。

#### 伺服器端需求與簽名生成
關鍵在於伺服器端設定，因為簽名生成涉及敏感憑證和對微信伺服器的 API 呼叫。生成簽名：
- 首先，使用您的 appId 和 appSecret 透過微信 API 取得 access token。
- 然後，使用 access token 取得 jsapi_ticket。
- 最後，按照[微信 JS SDK 文檔附錄 1](https://developers.weixin.qq.com/doc/offiaccount/OA_Web_Apps/JS-SDK.html#62) 中的演算法，使用 jsapi_ticket、當前 URL、隨機字串和時間戳記生成簽名。

此過程通常使用 PHP、Java、Node.js 或 Python 等語言實作，文檔中提供了範例程式碼。請快取 access token 和 jsapi_ticket 各 7200 秒，以避免觸發速率限制，如文檔所述。

此外，請確保您的域名已綁定到微信公眾號：
- 登入微信公眾平台，導航至公眾號設定 > 功能設定，輸入 JS API 安全域名。此步驟對安全和 API 存取至關重要。

#### 版本注意事項
考慮到使用者指定 "^1.2.0" 且套件最新版本為 1.6.5，值得注意的是套件版本可能對應於打包更新，而非底層 SDK 版本（根據官方來源為 1.6.0）。使用方式應保持一致，但對於 1.2.0 版本，請檢查 npm 變更日誌或 GitHub 發布說明以了解任何註明的變更，儘管一般指南表明對基本使用影響最小。

#### 範例與其他資源
對於實際實作，可以在各種 GitHub 儲存庫中找到範例，例如 [yanxi123-com/weixin-js-sdk](https://github.com/yanxi123-com/weixin-js-sdk)，它提供了原始碼和使用說明。此外，官方文檔包含 DEMO 連結，例如 [微信 JS-SDK 範例](https://www.weixinsxy.com/jssdk/)，儘管搜尋中未詳細說明具體內容，建議查看該網站以獲取範例程式碼和 zip 檔案。

#### 表格：步驟與需求摘要

| 步驟                  | 描述                                                                 | 注意事項                                                             |
|-----------------------|---------------------------------------------------------------------|----------------------------------------------------------------------|
| 安裝套件              | 執行 `npm install weixin-js-sdk` 或 `yarn add weixin-js-sdk`       | 確保套件在專案依賴中。                                               |
| 引入 SDK              | 使用 `import wx from 'weixin-js-sdk';` 或 `const wx = require('weixin-js-sdk');` | 根據模組系統選擇（ES6 或 CommonJS）。                                |
| 配置 SDK              | 使用 `wx.config` 並提供 appId、timestamp、nonceStr、signature 和 jsApiList | 簽名由伺服器端生成，需要微信公眾號。                                 |
| 處理配置              | 使用 `wx.ready()` 處理成功，`wx.error()` 處理失敗                   | 在 `ready` 中放置頁面載入時的 API 呼叫，適當處理錯誤。               |
| 伺服器端設定          | 使用 access token 和 jsapi_ticket 生成簽名，快取 7200 秒           | 涉及微信 API 呼叫，確保域名已綁定。                                 |

此表格概括了流程，為實作提供快速參考。

#### 意外細節：與打包工具的整合
一個有趣的方面是套件與 webpack 等打包工具的相容性，這從基本使用中並不明顯。這允許模組化開發，可能簡化大型專案中的依賴管理，並支援 TypeScript，增強了類型安全性，對於僅熟悉 script 標籤引入的使用者來說可能出乎意料。

#### 結論
總之，使用 "weixin-js-sdk" 版本 "^1.2.0" 涉及透過 npm 安裝、引入程式碼、使用伺服器生成的參數進行配置，並遵循官方微信 JS SDK 文檔進行 API 使用。確保伺服器端設定以生成簽名和綁定域名，並考慮套件與打包工具的相容性以進行現代網頁開發。有關詳細範例，請查閱提供的 GitHub 儲存庫和官方文檔連結。

### 主要引用來源
- [weixin-js-sdk npm 套件描述](https://www.npmjs.com/package/weixin-js-sdk)
- [微信 JS SDK 官方文檔](https://developers.weixin.qq.com/doc/offiaccount/OA_Web_Apps/JS-SDK.html)
- [weixin-js-sdk GitHub 儲存庫](https://github.com/yanxi123-com/weixin-js-sdk)