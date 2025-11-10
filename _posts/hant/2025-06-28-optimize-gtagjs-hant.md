---
audio: false
generated: true
lang: hant
layout: post
title: 優化 Jekyll GitHub Pages 上的 gtag.js 效能
translated: true
type: note
---

在使用 Jekyll 建構的 GitHub Pages 網站上使用 `gtag.js` 會面臨一些獨特限制，因為 GitHub Pages 的伺服器端控制有限，且無法直接存取快取標頭或伺服器端指令碼。不過，您仍然可以透過客戶端技術和 Jekyll 特定配置來優化 `https://www.googletagmanager.com/gtag/js?id=UA-66656236-1` 的載入速度。以下是針對此情境的性能提升策略：

---

### 1. **非同步載入 `gtag.js`**
確保 `gtag.js` 指令碼以非同步方式載入，以避免阻擋頁面渲染。在您的 Jekyll 網站中：
- 將指令碼添加到您的 Jekyll 版面或包含檔案中（例如 `_includes/analytics.html` 或直接放在 `default.html` 版面）。
- 使用 `async` 屬性：
```html
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-66656236-1"></script>
```
- 將此程式碼置於 Jekyll 模板中的 `<head>` 或 `</body>` 之前（例如 `_layouts/default.html`）：
```html
<head>
  <script async src="https://www.googletagmanager.com/gtag/js?id=UA-66656236-1"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'UA-66656236-1');
  </script>
</head>
```
- **為何有效**：`async` 確保指令碼不會阻擋 HTML 解析，減少感知載入時間。

---

### 2. **為 Google 網域添加 Preconnect**
透過為 `googletagmanager.com` 添加 `preconnect` 提示，減少 DNS 查詢和連線延遲。在您的 Jekyll 版面（`_layouts/default.html` 或 `_includes/head.html`）中：
```html
<link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>
```
- 將此程式碼置於 `<head>` 中，並放在 `gtag.js` 指令碼之前。
- **為何有效**：提前啟動 DNS 解析和 TCP 連線，加速 `gtag.js` 的擷取。

---

### 3. **延遲載入 `gtag.js`**
由於 GitHub Pages 是靜態的，您可以延遲載入 `gtag.js` 以優先處理關鍵內容。將以下 JavaScript 添加到您的 Jekyll 模板或獨立的 JS 檔案中（例如 `assets/js/analytics.js`）：
```javascript
window.addEventListener('load', () => {
  const script = document.createElement('script');
  script.src = 'https://www.googletagmanager.com/gtag/js?id=UA-66656236-1';
  script.async = true;
  document.head.appendChild(script);
  script.onload = () => {
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'UA-66656236-1');
  };
});
```
- 在您的 Jekyll 版面中包含此指令碼：
```html
<script src="{{ '/assets/js/analytics.js' | relative_url }}"></script>
```
- **為何有效**：延遲 `gtag.js` 的載入，直到頁面關鍵資源（如 HTML、CSS）載入完畢，提升初始頁面速度。

---

### 4. **透過 Cloudflare 使用 CDN 代理**
GitHub Pages 不允許自訂快取標頭，但您可以透過像 Cloudflare 這樣的 CDN 代理 `gtag.js`，將其快取在更接近用戶的位置：
1. **設定 Cloudflare**：
   - 將您的 GitHub Pages 網站添加到 Cloudflare（例如 `username.github.io`）。
   - 為您的網域啟用 Cloudflare 的 DNS 和代理功能。
2. **代理 `gtag.js`**：
   - 在 Cloudflare 中建立頁面規則來快取 `gtag.js` 指令碼，或在您的 Jekyll 網站的 `_site` 資料夾中託管本地副本（例如 `assets/js/gtag.js`）。
   - 更新您的指令碼標籤：
```html
<script async src="{{ '/assets/js/gtag.js' | relative_url }}"></script>
```
   - 定期將本地副本與 Google 的 `gtag.js` 同步，以確保其為最新版本（手動過程或透過 CI/CD 指令碼）。
3. **快取設定**：
   - 在 Cloudflare 中，為指令碼設定快取規則（例如 `Cache Everything` 並設定 TTL 為 1 小時）。
- **為何有效**：Cloudflare 的邊緣伺服器透過從更接近用戶的位置提供指令碼來減少延遲。
- **注意**：代理 Google 的指令碼時需謹慎，因為它們可能頻繁更新。請徹底測試以確保追蹤功能正常。

---

### 5. **優化 Jekyll 建構與傳輸**
確保您的 Jekyll 網站經過優化，以最小化整體頁面載入時間，這間接有助於 `gtag.js` 的性能：
- **最小化資源**：
  - 使用 Jekyll 外掛如 `jekyll-compress` 或 `jekyll-minifier` 來最小化 HTML、CSS 和 JS。
  - 添加到您的 `_config.yml`：
```yaml
plugins:
  - jekyll-compress
```
- **啟用 Gzip 壓縮**：
  - GitHub Pages 會自動為支援的檔案啟用 Gzip，但請透過瀏覽器開發工具檢查 `Content-Encoding` 標頭以確認您的 CSS/JS 檔案已被壓縮。
- **減少阻擋資源**：
  - 最小化在 `gtag.js` 之前載入的渲染阻擋 CSS/JS 檔案數量。
  - 使用 `jekyll-assets` 或類似工具來優化資源傳輸：
```yaml
plugins:
  - jekyll-assets
```
- **內嵌關鍵 CSS**：
  - 在 `<head>` 中內嵌關鍵 CSS 並延遲非關鍵 CSS，以減少渲染阻擋時間，這可以使 `gtag.js` 的載入感覺更快。
- **圖片優化**：
  - 使用 `jekyll-picture-tag` 或類似外掛來壓縮圖片，減少整體頁面重量，釋放頻寬給 `gtag.js`。

---

### 6. **切換至精簡分析**
如果 `gtag.js` 仍然緩慢或分析功能非關鍵：
- 考慮使用輕量級替代方案如 Plausible 或 Fathom，它們使用更小的指令碼（約 1 KB，而 `gtag.js` 約 50 KB）。
- Plausible 範例：
```html
<script defer data-domain="yourdomain.com" src="https://plausible.io/js/plausible.js"></script>
```
- 將此程式碼添加到您的 Jekyll `_includes/analytics.html` 並在版面中包含它。
- **為何有效**：較小的指令碼載入更快，尤其是在 GitHub Pages 的靜態基礎架構上。

---

### 7. **測試與監控性能**
- **測量擷取時間**：
  - 使用 Chrome DevTools（網路標籤）檢查 `gtag.js` 載入時間。
  - 使用 Lighthouse 或 WebPageTest 等工具評估整體頁面性能。
- **模擬用戶位置**：
  - 使用 Pingdom 等工具測試來自您受眾所在區域的載入時間，因為 GitHub Pages 和 Google 的 CDN 性能因地理位置而異。
- **監控真實用戶指標**：
  - 如果使用 Google Analytics，檢查網站速度報告以追蹤 `gtag.js` 的影響。
- **Jekyll 特定除錯**：
  - 執行 `jekyll build --profile` 以識別網站中可能間接影響性能的慢速建構組件。

---

### 8. **GitHub Pages 的限制**
- **無伺服器端控制**：GitHub Pages 是靜態主機，因此您無法為 `gtag.js` 實作伺服器端標記或自訂快取標頭。
- **無 HTTP/3**：GitHub Pages 使用 HTTP/2，雖然快速但不如 HTTP/3 優化。像 Cloudflare 這樣的 CDN 可以升級到 HTTP/3。
- **地理延遲**：GitHub Pages 伺服器主要位於美國，因此遠離美國的用戶可能會經歷較慢的載入。CDN 可以緩解此問題。

---

### Jekyll 設定範例
以下是結合 `preconnect` 和 `async` 的範例 `_includes/analytics.html`，用於您的 Jekyll 網站：
```html
<link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-66656236-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'UA-66656236-1');
</script>
```
在您的版面（`_layouts/default.html`）中包含它：
```html
<head>
</head>
```

---

### 後續步驟
- **測試當前性能**：分享當前的 `gtag.js` 擷取時間（來自瀏覽器開發工具）或您的網站 URL，我可以進一步分析。
- **地理背景**：告訴我您受眾的主要位置（例如美國、歐洲、亞洲），以便量身定制 CDN 或代理建議。
- **Cloudflare 設定**：如果您願意使用 Cloudflare，我可以提供代理 `gtag.js` 的詳細步驟。
- **替代分析工具**：如果您考慮從 Google Analytics 切換，我可以推薦特定的輕量級工具及其 Jekyll 整合。

您希望我專注於任何這些方面，還是執行特定分析（例如測試您網站的性能或提供 Cloudflare 設定指南）？