---
audio: false
generated: false
image: false
lang: hant
layout: post
title: 程式碼審查伺服器
translated: true
type: post
---

這是來自 GitHub 項目 [https://github.com/lzwjava/code-review-server](https://github.com/lzwjava/code-review-server) 的 README.md。

---

# code-review-server

CodeReview 是一個專業的程式碼審查、溝通和分享平台。工程師可以提交他們的程式碼以接受專家審查，以提高程式碼的質量。這個平台由我和另外五位網絡愛好者創立。

![img](./img/cr1.jpg)

![img](./img/cr2.jpg)

# 項目

* [code-review-server](https://github.com/lzwjava/code-review-server)
* [code-review-web](https://github.com/lzwjava/code-review-web)

# 部署

部署: fab -H root@reviewcode.cn deploy

安裝依賴: composer install, composer update

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