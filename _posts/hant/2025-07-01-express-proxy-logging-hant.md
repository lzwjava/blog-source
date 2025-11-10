---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 在 Express 中記錄代理請求
translated: true
type: note
---

若你在 Express 應用程式中使用 [`http-proxy-middleware`](https://github.com/chimurai/http-proxy-middleware)，可透過掛載其 `onProxyReq` 與 `onProxyRes` 事件來記錄請求參數與主體。

以下為實務範例：

```js
const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');
const app = express();

// 在代理前解析 JSON 主體
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use('/api', createProxyMiddleware({
  target: 'http://example.com',
  changeOrigin: true,

  // 記錄請求主體與查詢參數
  onProxyReq: (proxyReq, req, res) => {
    // 查詢參數
    console.log('Query:', req.query);

    // 主體（僅在代理前已解析時）
    if (req.body && Object.keys(req.body).length) {
      console.log('Body:', req.body);

      // 若需轉發主體（用於 POST/PUT 請求）
      const bodyData = JSON.stringify(req.body);
      proxyReq.setHeader('Content-Type', 'application/json');
      proxyReq.setHeader('Content-Length', Buffer.byteLength(bodyData));
      proxyReq.write(bodyData);
    }
  },

  // 記錄目標伺服器回應
  onProxyRes: (proxyRes, req, res) => {
    console.log(`目標伺服器回應：${proxyRes.statusCode} for ${req.method} ${req.originalUrl}`);
  }
}));

app.listen(3000, () => {
  console.log('代理服務運行於 http://localhost:3000');
});
```

### 關鍵要點

* **優先解析主體**：在代理中介軟體前使用 `express.json()` 或 `express.urlencoded()`，否則 `req.body` 將為空值
* **轉發主體**：預設情況下 `http-proxy-middleware` 不會轉發已解析的主體。若需記錄主體並同時轉發，必須重新序列化並透過 `write()` 寫入代理請求
* **查詢參數**：可直接透過 `req.query` 取得，無需額外處理
* **回應記錄**：使用 `onProxyRes` 捕捉目標伺服器回應

---

👉 你僅需記錄日誌進行除錯，還是希望代理在記錄後也能轉發修改過的主體？