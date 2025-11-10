---
audio: false
generated: true
image: false
lang: ar
layout: post
title: تسجيل طلبات الوكيل في إكسبريس
translated: true
type: note
---

إذا كنت تستخدم [`http-proxy-middleware`](https://github.com/chimurai/http-proxy-middleware) في تطبيق Express، فيمكنك الربط مع الأحداث `onProxyReq` و `onProxyRes` لتسجيل معلمات الطلب والنص الأساسي.

إليك مثالًا عمليًا:

```js
const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');
const app = express();

// تحليل النص الأساسي JSON قبل الوكيل
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use('/api', createProxyMiddleware({
  target: 'http://example.com',
  changeOrigin: true,

  // تسجيل النص الأساسي للطلب ومعلمات الاستعلام
  onProxyReq: (proxyReq, req, res) => {
    // معلمات الاستعلام
    console.log('Query:', req.query);

    // النص الأساسي (فقط إذا تم تحليله قبل الوكيل)
    if (req.body && Object.keys(req.body).length) {
      console.log('Body:', req.body);

      // إذا كنت بحاجة إلى إعادة توجيه النص الأساسي (لـ POST/PUT)
      const bodyData = JSON.stringify(req.body);
      proxyReq.setHeader('Content-Type', 'application/json');
      proxyReq.setHeader('Content-Length', Buffer.byteLength(bodyData));
      proxyReq.write(bodyData);
    }
  },

  // تسجيل الاستجابة من الهدف
  onProxyRes: (proxyRes, req, res) => {
    console.log(`Response from target: ${proxyRes.statusCode} for ${req.method} ${req.originalUrl}`);
  }
}));

app.listen(3000, () => {
  console.log('Proxy running on http://localhost:3000');
});
```

### النقاط الرئيسية

*   **تحليل النص الأساسي أولاً**: استخدم `express.json()` أو `express.urlencoded()` قبل الوكيل، وإلا سيكون `req.body` فارغًا.
*   **إعادة توجيه النص الأساسي**: افتراضيًا، لا يقوم `http-proxy-middleware` بإعادة توجيه النصوص الأساسية المحللة. إذا قمت بتسجيل النص الأساسي وأردت أيضًا إعادة توجيهه، فأنت بحاجة إلى إعادة تحويله إلى سلسلة نصية و `write()` إلى الطلب الموكل.
*   **معلمات الاستعلام**: متاحة في `req.query`، لا تحتاج إلى عمل إضافي.
*   **تسجيل الاستجابة**: استخدم `onProxyRes` لاستجابات الخادم الهدف.

---

👉 هل تحتاج فقط إلى التسجيل لأغراض التصحيح، أم تريد أيضًا أن يقوم الوكيل بإعادة توجيه النص الأساسي المعدل بعد التسجيل؟