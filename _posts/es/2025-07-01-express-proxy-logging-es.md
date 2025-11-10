---
audio: false
generated: true
image: false
lang: es
layout: post
title: Registro de Solicitudes de Proxy en Express
translated: true
type: note
---

Si estás usando [`http-proxy-middleware`](https://github.com/chimurai/http-proxy-middleware) en una aplicación Express, puedes conectarte a sus eventos `onProxyReq` y `onProxyRes` para registrar los parámetros y el cuerpo de la solicitud.

Aquí tienes un ejemplo práctico:

```js
const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');
const app = express();

// Analizar el cuerpo JSON antes del proxy
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use('/api', createProxyMiddleware({
  target: 'http://example.com',
  changeOrigin: true,

  // Registrar el cuerpo de la solicitud y los parámetros de consulta
  onProxyReq: (proxyReq, req, res) => {
    // Parámetros de consulta
    console.log('Query:', req.query);

    // Cuerpo (solo si se analizó antes del proxy)
    if (req.body && Object.keys(req.body).length) {
      console.log('Body:', req.body);

      // Si necesitas reenviar el cuerpo (para POST/PUT)
      const bodyData = JSON.stringify(req.body);
      proxyReq.setHeader('Content-Type', 'application/json');
      proxyReq.setHeader('Content-Length', Buffer.byteLength(bodyData));
      proxyReq.write(bodyData);
    }
  },

  // Registrar la respuesta del objetivo
  onProxyRes: (proxyRes, req, res) => {
    console.log(`Response from target: ${proxyRes.statusCode} for ${req.method} ${req.originalUrl}`);
  }
}));

app.listen(3000, () => {
  console.log('Proxy running on http://localhost:3000');
});
```

### Puntos Clave

*   **Analizar el cuerpo primero**: Usa `express.json()` o `express.urlencoded()` antes del proxy, de lo contrario `req.body` estará vacío.
*   **Reenviar el cuerpo**: Por defecto, `http-proxy-middleware` no reenvía los cuerpos analizados. Si registras el cuerpo y también quieres reenviarlo, necesitas reconvertirlo a string y `write()` en la solicitud proxy.
*   **Parámetros de consulta**: Disponibles en `req.query`, no se necesita trabajo adicional.
*   **Registro de respuestas**: Usa `onProxyRes` para las respuestas del servidor objetivo.

---

👉 ¿Solo necesitas el registro para depurar, o también quieres que el proxy reenvíe el cuerpo modificado después del registro?