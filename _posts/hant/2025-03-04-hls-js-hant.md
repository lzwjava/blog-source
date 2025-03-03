---
audio: false
generated: true
lang: hant
layout: post
title: JavaScript 影片播放庫
translated: true
---

看來你在詢問如何使用 `hls.js` 圖書館，特別是版本 `^0.7.6`，這是一個用於在瀏覽器中播放 HLS（HTTP Live Streaming）視頻流的 JavaScript 圖書館。我將根據圖書館的一般知識提供一個簡潔的指南，說明如何設置和使用它。請注意，版本 `0.7.6` 相當舊（約於 2017 年發布），因此某些功能或 API 可能與最新版本不同。如果你需要與該特定版本相關的具體信息，請告訴我，我可以進一步完善答案！

### 使用 `hls.js` (v0.7.6) 的步驟

#### 1. **安裝或包含圖書館**
你可以通過以下方式在項目中包含 `hls.js`：

- **通過 npm** (如果你使用構建工具如 Webpack)：
  ```bash
  npm install hls.js@^0.7.6
  ```
  然後在你的 JavaScript 中導入它：
  ```javascript
  var Hls = require('hls.js');
  ```

- **通過 CDN** (如果你直接將其添加到 HTML 文件中)：
  ```html
  <script src="https://cdn.jsdelivr.net/npm/hls.js@0.7.6"></script>
  ```
  這將使 `Hls` 作為全局變量可用。

#### 2. **設置 HTML**
你需要在 HTML 中有一個 `<video>` 元素來附加 HLS 流：
```html
<video id="video" controls></video>
```

#### 3. **初始化 `hls.js`**
這是如何使用 `hls.js` 加載和播放 HLS 流（例如，一個 `.m3u8` 文件）的基本示例：

```javascript
// 檢查瀏覽器是否原生支持 HLS（例如，Safari）
// 如果不支持，則使用 hls.js
var video = document.getElementById('video');
var videoSrc = 'https://example.com/playlist.m3u8'; // 替換為你的 HLS URL

if (Hls.isSupported()) {
    var hls = new Hls();
    hls.loadSource(videoSrc);
    hls.attachMedia(video);
    hls.on(Hls.Events.MANIFEST_PARSED, function () {
        video.play();
    });
} else if (video.canPlayType('application/vnd.apple.mpegurl')) {
    // 針對原生支持 HLS 的瀏覽器（例如，Safari）
    video.src = videoSrc;
    video.addEventListener('loadedmetadata', function () {
        video.play();
    });
}
```

#### 4. **關鍵概念**
- **`Hls.isSupported()`**：檢查瀏覽器是否需要 `hls.js`（如果支持媒體源擴展，則返回 `true`）。
- **`loadSource(url)`**：加載 HLS 宣告（`.m3u8` 文件）。
- **`attachMedia(video)`**：將視頻元素附加到 `hls.js` 實例。
- **`Hls.Events.MANIFEST_PARSED`**：當宣告加載時觸發的事件，表示流已準備好播放。

#### 5. **帶有錯誤處理的示例**
為了使其更加健壯：
```javascript
var video = document.getElementById('video');
var videoSrc = 'https://example.com/playlist.m3u8';

if (Hls.isSupported()) {
    var hls = new Hls();
    hls.loadSource(videoSrc);
    hls.attachMedia(video);
    hls.on(Hls.Events.MANIFEST_PARSED, function () {
        video.play();
    });
    hls.on(Hls.Events.ERROR, function (event, data) {
        console.error('HLS 錯誤:', data);
        if (data.fatal) {
            switch (data.type) {
                case Hls.ErrorTypes.NETWORK_ERROR:
                    console.log('網絡錯誤，重試中...');
                    hls.startLoad();
                    break;
                case Hls.ErrorTypes.MEDIA_ERROR:
                    console.log('媒體錯誤，恢復中...');
                    hls.recoverMediaError();
                    break;
                default:
                    hls.destroy();
                    break;
            }
        }
    });
} else if (video.canPlayType('application/vnd.apple.mpegurl')) {
    video.src = videoSrc;
}
```

#### 版本 `^0.7.6` 的注意事項
- 該版本來自 2017 年，因此缺少後來版本中添加的新功能，如自適應比特率切換改進或低延遲 HLS 支持。
- 核心 API（`loadSource`、`attachMedia`、`MANIFEST_PARSED` 事件等）應該如上所示工作。
- 如果需要精確細節，請檢查 [官方 `hls.js` GitHub 發布](https://github.com/video-dev/hls.js/releases/tag/v0.7.6) 的確切變更日誌。

#### 6. **測試**
- 使用公共可用的 HLS 流進行測試，例如：
  ```
  https://bitdash-a.akamaihd.net/content/sintel/hls/playlist.m3u8
  ```
- 打開瀏覽器的開發者工具（F12）來調試任何問題。

如果你有特定的使用案例或問題（例如，與框架集成、處理字幕等），請告訴我，我將進一步定制回應！