---
audio: false
lang: de
layout: post
title: Code-Review-Server
translated: true
---

Dies ist die README.md vom GitHub-Projekt [https://github.com/lzwjava/code-review-server](https://github.com/lzwjava/code-review-server).

---

# code-review-server

CodeReview ist eine professionelle Plattform für Code-Reviews, Kommunikation und das Teilen von Code. Ingenieure können ihren Code zur Expertise-Revision einreichen, um die Qualität ihres Codes zu verbessern. Sie wurde von 6 Internet-Liebhabern, einschließlich mir, gegründet.

![img](./img/cr1.jpg)

![img](./img/cr2.jpg)

# Projekte

* [code-review-server](https://github.com/lzwjava/code-review-server)
* [code-review-web](https://github.com/lzwjava/code-review-web)

# Bereitstellen

Bereitstellen: fab -H root@reviewcode.cn deploy

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