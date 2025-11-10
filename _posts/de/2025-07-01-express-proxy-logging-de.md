---
audio: false
generated: true
image: false
lang: de
layout: post
title: Protokollierung von Proxy-Anfragen in Express
translated: true
type: note
---

Wenn Sie [`http-proxy-middleware`](https://github.com/chimurai/http-proxy-middleware) in einer Express-App verwenden, können Sie sich in die `onProxyReq`- und `onProxyRes`-Events einklinken, um Anfrageparameter und den Body zu protokollieren.

Hier ist ein praktisches Beispiel:

```js
const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');
const app = express();

// JSON-Body vor dem Proxy parsen
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use('/api', createProxyMiddleware({
  target: 'http://example.com',
  changeOrigin: true,

  // Request-Body & Query-Parameter protokollieren
  onProxyReq: (proxyReq, req, res) => {
    // Query-Parameter
    console.log('Query:', req.query);

    // Body (nur wenn er vor dem Proxy geparst wurde)
    if (req.body && Object.keys(req.body).length) {
      console.log('Body:', req.body);

      // Wenn der Body weitergeleitet werden muss (für POST/PUT)
      const bodyData = JSON.stringify(req.body);
      proxyReq.setHeader('Content-Type', 'application/json');
      proxyReq.setHeader('Content-Length', Buffer.byteLength(bodyData));
      proxyReq.write(bodyData);
    }
  },

  // Antwort vom Zielserver protokollieren
  onProxyRes: (proxyRes, req, res) => {
    console.log(`Antwort vom Zielserver: ${proxyRes.statusCode} für ${req.method} ${req.originalUrl}`);
  }
}));

app.listen(3000, () => {
  console.log('Proxy läuft auf http://localhost:3000');
});
```

### Wichtige Punkte

*   **Body zuerst parsen**: Verwenden Sie `express.json()` oder `express.urlencoded()` vor dem Proxy, andernfalls ist `req.body` leer.
*   **Body weiterleiten**: Standardmäßig leitet `http-proxy-middleware` geparste Bodies nicht weiter. Wenn Sie den Body protokollieren und auch weiterleiten möchten, müssen Sie ihn neu serialisieren und mit `write()` an die Proxy-Anfrage senden.
*   **Query-Parameter**: Verfügbar unter `req.query`, keine zusätzliche Arbeit erforderlich.
*   **Antwort-Protokollierung**: Verwenden Sie `onProxyRes` für Antworten vom Zielserver.

---

👉 Benötigen Sie die Protokollierung nur für Debugging-Zwecke, oder soll der Proxy den modifizierten Body nach der Protokollierung auch weiterleiten?