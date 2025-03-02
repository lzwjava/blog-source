---
audio: false
generated: false
lang: de
layout: post
title: Code-Review-Server
translated: true
---

Das ist die README.md von einem GitHub-Projekt [https://github.com/lzwjava/code-review-server](https://github.com/lzwjava/code-review-server).

---

# code-review-server

CodeReview ist eine professionelle Plattform für Code-Reviews, Kommunikation und Sharing. Ingenieure können ihren Code zur Bewertung durch Experten einreichen, um die Qualität ihres Codes zu verbessern. Es wurde von 6 Internet-Liebhabern, einschließlich mir, gegründet.

![img](./img/cr1.jpg)

![img](./img/cr2.jpg)

# Projekte

* [code-review-server](https://github.com/lzwjava/code-review-server)
* [code-review-web](https://github.com/lzwjava/code-review-web)

# Deploy

Deploy: fab -H root@reviewcode.cn deploy

Abhängigkeiten installieren: composer install, composer update

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