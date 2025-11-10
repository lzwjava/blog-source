---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Journalisation des requêtes proxy dans Express
translated: true
type: note
---

Si vous utilisez [`http-proxy-middleware`](https://github.com/chimurai/http-proxy-middleware) dans une application Express, vous pouvez utiliser les événements `onProxyReq` et `onProxyRes` pour journaliser les paramètres de requête et le corps.

Voici un exemple pratique :

```js
const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');
const app = express();

// Parser le corps JSON avant le proxy
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use('/api', createProxyMiddleware({
  target: 'http://example.com',
  changeOrigin: true,

  // Journaliser le corps de la requête & les paramètres de requête
  onProxyReq: (proxyReq, req, res) => {
    // Paramètres de requête
    console.log('Query:', req.query);

    // Corps (seulement s'il est parsé avant le proxy)
    if (req.body && Object.keys(req.body).length) {
      console.log('Body:', req.body);

      // Si vous devez transmettre le corps (pour POST/PUT)
      const bodyData = JSON.stringify(req.body);
      proxyReq.setHeader('Content-Type', 'application/json');
      proxyReq.setHeader('Content-Length', Buffer.byteLength(bodyData));
      proxyReq.write(bodyData);
    }
  },

  // Journaliser la réponse de la cible
  onProxyRes: (proxyRes, req, res) => {
    console.log(`Response from target: ${proxyRes.statusCode} for ${req.method} ${req.originalUrl}`);
  }
}));

app.listen(3000, () => {
  console.log('Proxy running on http://localhost:3000');
});
```

### Points Clés

* **Parser le corps d'abord** : Utilisez `express.json()` ou `express.urlencoded()` avant le proxy, sinon `req.body` sera vide.
* **Transmission du corps** : Par défaut, `http-proxy-middleware` ne transmet pas les corps parsés. Si vous journalisez le corps et souhaitez aussi le transmettre, vous devez le re-sérialiser et l'`write()` dans la requête proxifiée.
* **Paramètres de requête** : Disponibles dans `req.query`, aucun travail supplémentaire nécessaire.
* **Journalisation de la réponse** : Utilisez `onProxyRes` pour les réponses du serveur cible.

---

👉 Avez-vous seulement besoin de journalisation pour le débogage, ou souhaitez-vous aussi que le proxy transmette le corps modifié après la journalisation ?