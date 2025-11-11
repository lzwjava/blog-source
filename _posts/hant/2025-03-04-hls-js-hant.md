---
audio: false
generated: true
lang: hant
layout: post
title: HLS 播放用 JavaScript 程式庫
translated: true
type: note
---

看來您是想了解如何使用 `hls.js` 函式庫（版本 `^0.7.6`），這是一個能在瀏覽器中播放 HLS（HTTP Live Streaming）視訊串流的 JavaScript 函式庫。我將根據對該函式庫的通用知識，提供簡明的設定與使用指南。請注意，版本 `0.7.6` 相當舊（約在 2017 年發布），因此部分功能或 API 可能與最新版本有所不同。如果您需要該特定版本的詳細資訊，請告知，我將進一步調整回答！

### 使用 `hls.js` (v0.7.6) 的步驟

#### 1. **安裝或引入函式庫**
您可以透過以下方式將 `hls.js` 加入專案：

- **透過 npm**（若使用如 Webpack 的建置工具）：
  ```bash
  npm install hls.js@^0.7.6
  ```
  然後在 JavaScript 中引入：
  ```javascript
  var Hls = require('hls.js');
  ```

- **透過 CDN**（若直接加入 HTML 檔案）：
  ```html
  <script src="https://cdn.jsdelivr.net/npm/hls.js@0.7.6"></script>
  ```
  這會將 `Hls` 設為全域變數。

#### 2. **設定 HTML**
您需要在 HTML 中加入 `<video>` 元素以連接 HLS 串流：
```html
<video id="video" controls></video>
```

#### 3. **初始化 `hls.js`**
以下是使用 `hls.js` 載入並播放 HLS 串流（例如 `.m3u8` 檔案）的基本範例：

```javascript
// 檢查瀏覽器是否原生支援 HLS（例如 Safari）
// 若不支援，則使用 hls.js
var video = document.getElementById('video');
var videoSrc = 'https://example.com/playlist.m3u8'; // 替換為您的 HLS URL

if (Hls.isSupported()) {
    var hls = new Hls();
    hls.loadSource(videoSrc);
    hls.attachMedia(video);
    hls.on(Hls.Events.MANIFEST_PARSED, function () {
        video.play();
    });
} else if (video.canPlayType('application/vnd.apple.mpegurl')) {
    // 針對原生支援 HLS 的瀏覽器（例如 Safari）
    video.src = videoSrc;
    video.addEventListener('loadedmetadata', function () {
        video.play();
    });
}
```

#### 4. **關鍵概念**
- **`Hls.isSupported()`**：檢查瀏覽器是否需要 `hls.js`（若支援 Media Source Extensions 則回傳 `true`）。
- **`loadSource(url)`**：載入 HLS 清單（`.m3u8` 檔案）。
- **`attachMedia(video)`**：將 video 元素附加至 `hls.js` 實例。
- **`Hls.Events.MANIFEST_PARSED`**：當清單載入完成時觸發的事件，表示串流已準備好播放。

#### 5. **包含錯誤處理的範例**
為增強穩定性：
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
        console.error('HLS 錯誤：', data);
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

#### 版本 `^0.7.6` 注意事項
- 此版本來自 2017 年，因此缺少新功能，例如後續版本中加入的自適應位元率切換改進或低延遲 HLS 支援。
- 核心 API（`loadSource`、`attachMedia`、`MANIFEST_PARSED` 等事件）應能如上所述運作。
- 如需精確細節，請查閱[官方 `hls.js` GitHub 發布頁面](https://github.com/video-dev/hls.js/releases/tag/v0.7.6)以獲取確切更新日誌。

#### 6. **測試**
- 使用公開的 HLS 串流進行測試，例如：
  ```
  https://bitdash-a.akamaihd.net/content/sintel/hls/playlist.m3u8
  ```
- 開啟瀏覽器的開發者工具（F12）以除錯任何問題。

如果您有特定使用情境或問題（例如與框架整合、處理字幕等），請告知，我將進一步調整回答！