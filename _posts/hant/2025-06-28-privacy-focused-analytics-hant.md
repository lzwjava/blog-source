---
audio: false
generated: true
lang: hant
layout: post
title: 注重私隱的網站分析指南
translated: true
type: note
---

Cloudflare Web Analytics 是一款以隱私為核心的免費工具，旨在幫助網站擁有者追蹤及了解網站效能與訪客行為，同時不犧牲用戶隱私。以下基於最新可用資訊，提供設定與使用 Cloudflare Web Analytics 的完整指南。

### Cloudflare Web Analytics 概覽
Cloudflare Web Analytics 提供網站流量、頁面瀏覽量及效能指標的深入分析，同時優先考慮用戶隱私。與傳統分析工具可能追蹤個人數據或使用 Cookie 不同，Cloudflare 的解決方案避免使用侵入性追蹤方法，例如指紋識別、Cookie 或本地儲存用於分析目的。它適用於各種規模的網站，並且可搭配或不搭配 Cloudflare 的代理服務使用。[](https://www.cloudflare.com/web-analytics/)[](https://www.cloudflare.com/en-in/web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)

### 主要功能
- **隱私優先**：不收集個人數據、不使用 Cookie，也不透過 IP 地址或用戶代理追蹤用戶，確保符合如 GDPR 等隱私法規。[](https://www.cloudflare.com/en-in/web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)
- **兩種數據收集方法**：
  - **JavaScript Beacon**：一個輕量級的 JavaScript 代碼片段，使用瀏覽器的 Performance API 收集客戶端指標。適合用於詳細的 Real User Monitoring (RUM) 數據，例如頁面載入時間和核心網頁指標。[](https://www.cloudflare.com/web-analytics/)[](https://developers.cloudflare.com/web-analytics/about/)
  - **Edge Analytics**：從 Cloudflare 的邊緣伺服器收集伺服器端數據，適用於透過 Cloudflare 代理的網站。無需更改代碼，並可捕獲所有請求，包括來自機器人或停用 JavaScript 的用戶的請求。[](https://www.cloudflare.com/web-analytics/)[](https://developers.cloudflare.com/web-analytics/faq/)
- **提供的指標**：追蹤頁面瀏覽量、訪問次數、熱門頁面、推薦來源、國家、裝置類型、狀態碼及效能指標（如頁面載入時間）。[](https://www.cloudflare.com/en-in/web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)[](https://usefathom.com/features/vs-cloudflare-web-analytics)
- **Adaptive Bit Rate (ABR)**：根據數據大小、日期範圍和網絡條件自動調整數據解析度，以實現最佳效能。[](https://developers.cloudflare.com/web-analytics/about/)
- **免費使用**：任何擁有 Cloudflare 帳戶的人均可使用，無需更改 DNS 或使用 Cloudflare 的代理服務。[](https://www.cloudflare.com/en-in/web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)
- **儀表板與篩選器**：提供直觀的儀表板，可查看並按主機名、URL、國家和時間範圍篩選數據。您可以縮放至特定時間段或分組數據以進行深入分析。[](https://www.cloudflare.com/web-analytics/)[](https://www.cloudflare.com/en-in/web-analytics/)
- **Single Page Application (SPA) 支援**：透過覆寫 History API 的 `pushState` 函數（不支援基於雜湊的路由器），自動追蹤 SPA 中的路由變化。[](https://scripts.nuxt.com/scripts/analytics/cloudflare-web-analytics)

### 限制
- **數據保留**：僅保留 30 天的歷史數據，可能不適合需要長期分析的用戶。[](https://plausible.io/vs-cloudflare-web-analytics)
- **數據抽樣**：指標基於頁面載入事件的 10% 抽樣，可能導致與 Plausible 或 Fathom Analytics 等工具相比的數據不準確。[](https://plausible.io/vs-cloudflare-web-analytics)
- **準確性問題**：伺服器端分析（edge analytics）可能包含機器人流量，使數字膨脹，與 Google Analytics 等客戶端分析相比。客戶端分析可能遺漏停用 JavaScript 或使用廣告攔截器的用戶數據。[](https://developers.cloudflare.com/analytics/faq/about-analytics/)[](https://plausible.io/vs-cloudflare-web-analytics)[](https://markosaric.com/cloudflare-analytics-review/)
- **不支援 UTM 參數**：目前，為避免收集敏感數據，不會記錄如 UTM 參數等查詢字串。[](https://developers.cloudflare.com/web-analytics/faq/)
- **匯出限制**：無法直接匯出數據（例如至 CSV），與 Fathom Analytics 等競爭對手不同。[](https://usefathom.com/features/vs-cloudflare-web-analytics)
- **基礎分析功能**：與 Google Analytics 相比，缺乏進階功能，如轉換追蹤或詳細用戶旅程分析。[](https://www.reddit.com/r/webdev/comments/ka8gxv/cloudflares_privacyfirst_web_analytics_is_now/)

### 設定 Cloudflare Web Analytics
#### 先決條件
- 一個 Cloudflare 帳戶（可在 cloudflare.com 免費建立）。
- 存取您網站的代碼（用於 JavaScript beacon）或 DNS 設定（用於 edge analytics，如果使用 Cloudflare 代理）。

#### 設定步驟
1. **登入 Cloudflare 儀表板**：
   - 前往 [cloudflare.com](https://www.cloudflare.com) 並登入或建立帳戶。
   - 從帳戶首頁，導航至 **Analytics & Logs** > **Web Analytics**。[](https://developers.cloudflare.com/web-analytics/get-started/)

2. **新增網站**：
   - 在 Web Analytics 部分點擊 **Add a site**。
   - 輸入您網站的主機名（例如 `example.com`）並選擇 **Done**。[](https://developers.cloudflare.com/web-analytics/get-started/)

3. **選擇數據收集方法**：
   - **JavaScript Beacon（推薦用於非代理網站）**：
     - 從 **Manage site** 部分複製提供的 JavaScript 代碼片段。
     - 將其貼上到您網站的 HTML 中，位於結束 `</body>` 標籤之前。確保您的網站具有有效的 HTML，以便代碼片段正常工作。[](https://developers.cloudflare.com/web-analytics/get-started/)[](https://developers.cloudflare.com/web-analytics/faq/)
     - 對於 Single Page Applications，請確保在配置中設定 `spa: true` 以啟用自動路由追蹤（不支援基於雜湊的路由器）。[](https://scripts.nuxt.com/scripts/analytics/cloudflare-web-analytics)
     - 例如，對於 Nuxt 應用：使用 `useScriptCloudflareWebAnalytics` composable 或將 token 添加到您的 Nuxt 配置中以進行全域載入。[](https://scripts.nuxt.com/scripts/analytics/cloudflare-web-analytics)
   - **Edge Analytics（用於代理網站）**：
     - 透過將您的 DNS 設定更新為指向 Cloudflare 的名稱伺服器，將您的網站代理透過 Cloudflare。這可在幾分鐘內完成，且無需更改代碼。[](https://www.cloudflare.com/en-in/web-analytics/)
     - 指標將出現在 Cloudflare 儀表板的 **Analytics & Logs** 下。[](https://developers.cloudflare.com/web-analytics/faq/)
   - **Cloudflare Pages**：
     - 對於 Pages 項目，一鍵啟用 Web Analytics：從 **Workers & Pages** 中選擇您的項目，前往 **Metrics**，然後在 Web Analytics 下點擊 **Enable**。[](https://developers.cloudflare.com/pages/how-to/web-analytics/)[](https://developers.cloudflare.com/web-analytics/get-started/)

4. **驗證設定**：
   - 數據可能需要幾分鐘才會出現在儀表板中。檢查 **Web Analytics Sites** 部分以確認網站已新增。[](https://developers.cloudflare.com/web-analytics/get-started/)
   - 如果使用 edge analytics，請確保 DNS 傳播已完成（可能需要 24–72 小時）。[](https://developers.cloudflare.com/analytics/faq/about-analytics/)

5. **配置規則（可選）**：
   - 設定規則以追蹤特定網站或路徑。使用維度對指標進行分類（例如，按主機名或 URL）。[](https://developers.cloudflare.com/web-analytics/)

#### 注意事項
- 如果您的網站具有 `Cache-Control: public, no-transform` 標頭，JavaScript beacon 將不會自動注入，且 Web Analytics 可能無法工作。請調整您的快取設定或手動添加代碼片段。[](https://developers.cloudflare.com/web-analytics/get-started/)[](https://developers.cloudflare.com/web-analytics/faq/)
- 某些廣告攔截器可能會阻擋 JavaScript beacon，但 edge analytics 不受影響，因為它們依賴伺服器日誌。[](https://developers.cloudflare.com/web-analytics/faq/)
- 對於手動設定，beacon 會報告至 `cloudflareinsights.com/cdn-cgi/rum`；對於代理網站，它使用您網域的 `/cdn-cgi/rum` 端點。[](https://developers.cloudflare.com/web-analytics/faq/)

### 使用 Cloudflare Web Analytics
1. **存取儀表板**：
   - 登入 Cloudflare 儀表板，選擇您的帳戶和網域，然後前往 **Analytics & Logs** > **Web Analytics**。[](https://developers.cloudflare.com/pages/how-to/web-analytics/)[](https://developers.cloudflare.com/analytics/types-of-analytics/)
   - 查看指標，如頁面瀏覽量、訪問次數、熱門頁面、推薦來源、國家、裝置類型和效能數據（例如頁面載入時間、核心網頁指標）。[](https://www.cloudflare.com/en-in/web-analytics/)[](https://usefathom.com/features/vs-cloudflare-web-analytics)

2. **篩選與分析數據**：
   - 使用篩選器專注於特定指標（例如，按主機名、URL 或國家）。
   - 縮放時間範圍以調查流量高峰，或按指標（如推薦來源或頁面）分組數據。[](https://www.cloudflare.com/en-in/web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)
   - 對於進階用戶，可透過 **GraphQL Analytics API** 查詢數據以建立自訂儀表板。[](https://www.cloudflare.com/application-services/products/analytics/)[](https://www.cloudflare.com/en-in/application-services/products/analytics/)

3. **了解關鍵指標**：
   - **頁面瀏覽量**：頁面載入的總次數（HTML 內容類型且 HTTP 回應成功）。[](https://developers.cloudflare.com/analytics/account-and-zone-analytics/zone-analytics/)
   - **訪問次數**：來自不同推薦來源（與主機名不匹配）或直接連結的頁面瀏覽量。[](https://developers.cloudflare.com/analytics/account-and-zone-analytics/zone-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)
   - **獨立訪客**：基於 IP 地址，但出於隱私原因不儲存。由於機器人流量或缺乏基於 JavaScript 的去重複，可能比其他工具顯示的數字更高。[](https://developers.cloudflare.com/analytics/faq/about-analytics/)[](https://plausible.io/vs-cloudflare-web-analytics)
   - **效能指標**：包括頁面載入時間、首次繪製和核心網頁指標（僅客戶端）。[](https://usefathom.com/features/vs-cloudflare-web-analytics)

4. **與其他工具比較**：
   - 與 Google Analytics 不同，Cloudflare 不追蹤用戶旅程或轉換，但包含機器人和威脅流量，這可能使數字膨脹（大多數網站的 20–50% 流量）。[](https://developers.cloudflare.com/analytics/faq/about-analytics/)[](https://www.cloudflare.com/insights/)
   - 與 Plausible 或 Fathom Analytics 相比，由於抽樣和有限的保留期，Cloudflare 的數據較不精細。[](https://plausible.io/vs-cloudflare-web-analytics)[](https://usefathom.com/features/vs-cloudflare-web-analytics)
   - Edge analytics 可能顯示比 Google Analytics 等客戶端工具更高的數字，後者排除機器人和非 JavaScript 請求。[](https://developers.cloudflare.com/analytics/faq/about-analytics/)[](https://www.reddit.com/r/CloudFlare/comments/1alzkwm/why_are_my_cloudflare_traffic_stats_so_different/)

### 最佳實踐
- **選擇正確的方法**：如果您的網站已代理，使用 JavaScript beacon 以獲得隱私優先的客戶端指標，或使用 edge analytics 以獲得全面的伺服器端數據。[](https://www.cloudflare.com/web-analytics/)
- **與其他工具結合使用**：由於 Cloudflare 的分析功能較基礎，可搭配 Google Analytics 或隱私優先替代方案（如 Plausible 或 Fathom）以獲得更深入的見解。[](https://www.cloudflare.com/insights/)[](https://www.reddit.com/r/webdev/comments/ka8gxv/cloudflares_privacyfirst_web_analytics_is_now/)
- **監控效能**：使用效能指標識別載入緩慢的頁面，並利用 Cloudflare 的建議（例如快取優化）。[](https://developers.cloudflare.com/web-analytics/)
- **檢查廣告攔截器問題**：如果使用 JavaScript beacon，請告知用戶允許 `cloudflare.com` 或停用廣告攔截器以確保數據收集。[](https://developers.cloudflare.com/analytics/faq/about-analytics/)
- **定期檢閱數據**：由於數據僅保留 30 天，請頻繁檢查儀表板以發現趨勢或異常。[](https://plausible.io/vs-cloudflare-web-analytics)

### 疑難排解
- **未顯示數據**：
  - 驗證 JavaScript 代碼片段是否正確放置，且網站具有有效的 HTML。[](https://developers.cloudflare.com/pages/how-to/web-analytics/)[](https://developers.cloudflare.com/web-analytics/faq/)
  - 對於 edge analytics，請確保 DNS 指向 Cloudflare（傳播可能需要 24–72 小時）。[](https://developers.cloudflare.com/analytics/faq/about-analytics/)
  - 檢查 `Cache-Control: no-transform` 標頭是否阻擋了自動 beacon 注入。[](https://developers.cloudflare.com/web-analytics/get-started/)
- **統計數據不準確**：
  - Edge analytics 包含機器人流量，使數字膨脹。使用客戶端分析以獲得更準確的訪客計數。[](https://plausible.io/vs-cloudflare-web-analytics)[](https://markosaric.com/cloudflare-analytics-review/)
  - 數據抽樣（10%）可能導致差異。在與其他工具比較時請考慮這一點。[](https://plausible.io/vs-cloudflare-web-analytics)
- **廣告攔截器問題**：某些瀏覽器擴充功能會阻擋 JavaScript beacon。Edge analytics 不受此影響。[](https://developers.cloudflare.com/web-analytics/faq/)
- **缺少 SPA 指標**：確保啟用 SPA 支援（`spa: true`）並避免使用基於雜湊的路由器。[](https://scripts.nuxt.com/scripts/analytics/cloudflare-web-analytics)

### 進階使用
- **GraphQL Analytics API**：對於自訂分析，可查詢 Cloudflare 的 API 以建立量身定制的儀表板或與其他系統整合。需要技術專業知識。[](https://www.cloudflare.com/application-services/products/analytics/)[](https://www.cloudflare.com/en-in/application-services/products/analytics/)
- **Cloudflare Workers**：將分析數據發送到時間序列數據庫以進行自訂處理，或使用 Workers 進行進階無伺服器分析。[](https://developers.cloudflare.com/analytics/)
- **安全洞察**：結合 Cloudflare 的 Security Analytics，在訪客數據旁邊監控威脅和機器人。[](https://www.cloudflare.com/insights/)[](https://developers.cloudflare.com/waf/analytics/security-analytics/)

### 與替代方案比較
- **Google Analytics**：提供詳細的用戶旅程追蹤和轉換，但依賴 Cookie 和 JavaScript，可能被阻擋。Cloudflare 更簡單且隱私優先，但功能較少。[](https://developers.cloudflare.com/analytics/faq/about-analytics/)[](https://www.reddit.com/r/webdev/comments/ka8gxv/cloudflares_privacyfirst_web_analytics_is_now/)
- **Plausible Analytics**：開源、隱私優先，具有無限數據保留且無抽樣。對於獨立訪客更準確，但需要付費計劃。[](https://plausible.io/vs-cloudflare-web-analytics)
- **Fathom Analytics**：與 Plausible 類似，具有可匯出的數據和進階功能（如活動追蹤）。Cloudflare 的免費產品功能較不強大，但對於基本需求更易設定。[](https://usefathom.com/features/vs-cloudflare-web-analytics)
- **Jetpack Stats**：專為 WordPress 設計，數據保留有限（28 天）且無用戶級別追蹤。隱私重點相似，但靈活性低於 Cloudflare。[](https://wordpress.com/support/stats/)

### 其他資源
- **官方文件**：[Cloudflare Web Analytics 文檔](https://developers.cloudflare.com/web-analytics/)[](https://developers.cloudflare.com/web-analytics/about/)
- **設定指南**：[啟用 Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/get-started/)[](https://developers.cloudflare.com/web-analytics/get-started/)
- **常見問題**：[Cloudflare Web Analytics 常見問題](https://developers.cloudflare.com/web-analytics/faq/)[](https://developers.cloudflare.com/web-analytics/faq/)
- **部落格文章**：[Cloudflare 的隱私優先網頁分析](https://blog.cloudflare.com/privacy-first-web-analytics/)[](https://blog.cloudflare.com/privacy-first-web-analytics/)
- **社群支援**：查看 Cloudflare 的社群論壇以獲得額外幫助。[](https://developers.cloudflare.com/web-analytics/faq/)

### 結論
Cloudflare Web Analytics 是網站擁有者尋求免費、隱私優先且設定簡易的分析工具的絕佳選擇。它非常適合用於基本流量和效能監控，但由於數據抽樣、有限的保留期以及缺乏轉換追蹤等功能，可能無法滿足進階需求。為獲得更深入的見解，請考慮將其與 Plausible 或 Fathom Analytics 等工具結合使用。在解讀數據時，請務必驗證設定的準確性並注意限制。

如果您需要有關設定的具體協助或有關將 Cloudflare Web Analytics 與您的網站整合的問題，請告訴我！