---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Expressでのプロキシリクエストのログ記録
translated: true
type: note
---

Expressアプリで[`http-proxy-middleware`](https://github.com/chimurai/http-proxy-middleware)を使用している場合、`onProxyReq`および`onProxyRes`イベントをフックしてリクエストパラメータとボディをログ出力できます。

以下は実用的な例です：

```js
const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');
const app = express();

// プロキシ前にJSONボディをパース
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use('/api', createProxyMiddleware({
  target: 'http://example.com',
  changeOrigin: true,

  // リクエストボディとクエリパラメータをログ出力
  onProxyReq: (proxyReq, req, res) => {
    // クエリパラメータ
    console.log('Query:', req.query);

    // ボディ（プロキシ前にパースされている場合のみ）
    if (req.body && Object.keys(req.body).length) {
      console.log('Body:', req.body);

      // ボディを転送する必要がある場合（POST/PUT用）
      const bodyData = JSON.stringify(req.body);
      proxyReq.setHeader('Content-Type', 'application/json');
      proxyReq.setHeader('Content-Length', Buffer.byteLength(bodyData));
      proxyReq.write(bodyData);
    }
  },

  // ターゲットからのレスポンスをログ出力
  onProxyRes: (proxyRes, req, res) => {
    console.log(`Response from target: ${proxyRes.statusCode} for ${req.method} ${req.originalUrl}`);
  }
}));

app.listen(3000, () => {
  console.log('Proxy running on http://localhost:3000');
});
```

### 重要なポイント

* **ボディの事前パース**: プロキシの前に`express.json()`または`express.urlencoded()`を使用しないと、`req.body`は空になります。
* **ボディの転送**: デフォルトでは、`http-proxy-middleware`はパースされたボディを転送しません。ボディをログ出力しつつ転送もしたい場合は、再文字列化して`write()`でプロキシリクエストに書き込む必要があります。
* **クエリパラメータ**: `req.query`で利用可能で、追加作業は不要です。
* **レスポンスのログ出力**: ターゲットサーバーのレスポンスには`onProxyRes`を使用します。

---

👉 デバッグのためのログ出力だけが必要ですか？それともログ出力後に変更されたボディをプロキシで転送したいですか？