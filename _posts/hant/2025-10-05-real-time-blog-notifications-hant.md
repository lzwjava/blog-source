---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 即時部落格訪問電報通知
translated: true
type: note
---

是的，你可以建立一個系統來近乎即時地分析 Cloudflare 日誌或流量，並為每個部落格訪問發送 Telegram 通知，但僅使用標準分析日誌並不容易實現。Cloudflare 的分析大多為匯總數據（例如每日/每週摘要），即使其 Logpush 功能（用於導出日誌）也會每 1-5 分鐘批量處理數據，因此不適合用於即時的每次訪問警報。Instant Logs 提供即時串流功能，但需要 Business 或 Enterprise 方案，並且需要自訂處理（例如透過 WebSocket 和腳本）來觸發 Telegram 訊息——這對大多數用戶來說過於複雜。

最實用且即時的方法是使用 **Cloudflare Workers** 來攔截發往你部落格的每個傳入請求。這會在每次訪問時運行無伺服器代碼，讓你能夠記錄事件並立即透過 Telegram API 發送訊息。對於低流量（每天最多 10 萬次請求）是免費的，但高流量的部落格可能會達到限制或產生費用——此外，你可能會收到大量通知，因此請考慮設置過濾條件（例如僅針對唯一 IP 或特定頁面）。

### 快速設置步驟
1. **創建 Telegram Bot**：
   - 在 Telegram 中向 @BotFather 發送訊息，使用 `/newbot` 創建一個 bot，並記下 bot token（例如 `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`）。
   - 與你的 bot 開啟對話，然後向 @userinfobot 發送訊息以獲取你的 chat ID（例如 `123456789`）。
   - 透過 curl 測試發送訊息：  
     ```
     curl -X POST "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/sendMessage" \
     -H "Content-Type: application/json" \
     -d '{"chat_id":"<YOUR_CHAT_ID>","text":"Test visit!"}'
     ```

2. **創建 Cloudflare Worker**：
   - 登入你的 Cloudflare 儀表板 > Workers & Pages > Create application > Create Worker。
   - 為其命名（例如 `blog-visit-notifier`）並部署預設模板。

3. **添加通知代碼**：
   - 編輯 worker 的代碼以攔截請求並發送訊息到 Telegram。以下是一個基本示例（請替換佔位符）：
     ```javascript
     export default {
       async fetch(request, env) {
         // 可選：記錄或過濾訪問（例如僅針對部落格首頁）
         const url = new URL(request.url);
         if (url.pathname !== '/') {  // 根據需要調整路徑
           return fetch(request);  // 跳過非部落格頁面
         }

         // 發送 Telegram 訊息（非同步以避免阻塞）
         const message = `New visit to ${url.origin}! IP: ${request.headers.get('cf-connecting-ip')}, User-Agent: ${request.headers.get('user-agent')}`;
         await fetch(`https://api.telegram.org/bot${env.TELEGRAM_BOT_TOKEN}/sendMessage`, {
           method: 'POST',
           headers: { 'Content-Type': 'application/json' },
           body: JSON.stringify({
             chat_id: env.TELEGRAM_CHAT_ID,
             text: message,
             parse_mode: 'HTML'  // 如需格式化可使用
           })
         }).catch(err => console.error('Telegram send failed:', err));

         // 將原始請求代理到你的部落格
         return fetch(request);
       }
     };
     ```
     - 這會在每個符合條件的請求上運行，記錄基本訪問者資訊，並透過 Telegram 發送，且不會延遲頁面加載。

4. **配置環境變數**：
   - 在 worker 設定 > Variables > Add：  
     - `TELEGRAM_BOT_TOKEN`：你的 bot token。  
     - `TELEGRAM_CHAT_ID`：你的 chat ID。  
   - 保存並重新部署。

5. **將 Worker 路由到你的部落格**：
   - 在 Workers 設定 > Triggers > Add route。  
   - 將其設置為你的部落格網域/路徑（例如 `yourblog.com/*`）。  
   - 這確保 worker 在每次訪問時運行，然後才到達你的原始伺服器。

6. **測試和監控**：
   - 訪問你的部落格——你應該會立即收到 Telegram 通知。  
   - 在儀表板中檢查 worker 日誌以查找錯誤。如果你達到速率限制（例如 Telegram 的每秒 30 條訊息），請使用 KV storage 添加防抖動。

### 如果 Workers 不適合的替代方案
- **用於批量日誌分析**：使用 Logpush 將 HTTP 請求日誌導出到 AWS S3 或 Google Pub/Sub 等服務，然後通過 Zapier 或 n8n 等工具管道傳輸以發送 Telegram 警報（例如每小時匯總訪問次數）。但這不是即時的。
- **整合**：Albato 或 n8n 等工具可以將 Cloudflare webhooks 連接到 Telegram 以處理更廣泛的事件，但不適用於每次訪問。
- **限制**：免費 Workers 每個請求有 10ms 的 CPU 時間——對此用途足夠，但如有需要可擴展。在高流量網站上使用時，若未進行節流處理，請避免使用。

此設置將你的 Cloudflare 流量轉化為可操作的即時警報。如果你需要代碼調整或幫助解決錯誤，請分享更多詳細資訊！

[Cloudflare Workers 文檔](https://developers.cloudflare.com/workers/)  
[Telegram Bot API](https://core.telegram.org/bots/api)  
[Cloudflare Instant Logs](https://developers.cloudflare.com/logs/instant-logs/)