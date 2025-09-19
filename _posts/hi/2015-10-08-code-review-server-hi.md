---
audio: false
generated: false
image: false
lang: hi
layout: post
title: कोड समीक्षा सर्वर
translated: true
---

यह GitHub प्रोजेक्ट [https://github.com/lzwjava/code-review-server](https://github.com/lzwjava/code-review-server) का README.md है।

---

# code-review-server

CodeReview एक प्रोफेशनल प्लेटफॉर्म है, जो कोड रिव्यू, संचार, और शेयरिंग के लिए है। इंजीनियर अपने कोड को महान रिव्यू के लिए सुमित कर सकते हैं, ताकि उनकी कोड की गुणवत्ता में सुधार हो सके। इसे 6 इंटरनेट प्रेमियों ने स्थापित किया था, जिनमें मैं भी शामिल हूँ.

![img](./img/cr1.jpg)

![img](./img/cr2.jpg)

# प्रोजेक्ट्स

* [code-review-server](https://github.com/lzwjava/code-review-server)
* [code-review-web](https://github.com/lzwjava/code-review-web)

# डिप्लॉय

डिप्लॉय: fab -H root@reviewcode.cn deploy

डिपेंडेंसी इंस्टॉल करें: composer install, composer update

# API

- `GET /user/self`
- `DELETE /user/tags/:tagId`
- `POST /user/tags`
- `POST /orders`
- `GET /user/orders`
- `GET /orders/:orderId`
- `POST /orders/:orderId`
- `POST /orders/:orderId`
- `POST /orders/:orderId/reward`
- `GET /qiniu/token`
- `GET /reviewers`
- `GET /reviewers/:reviewerId`
- `POST /reviews`
- `PATCH /reviews/:reviewId`
- `GET /reviews`
- `GET /reviewers/:reviewerId/reviews`
- `POST /reviews/:reviewId/visits`
- `GET /videos`
- `POST /videos/:videoId/visits`
- `DELETE /orders/:orderId`
- `POST /user/requestResetPassword`
- `POST /user/resetPassword`