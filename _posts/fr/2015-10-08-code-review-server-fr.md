---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Serveur de Relecture de Code
translated: true
type: post
---

Ceci est le README.md du projet GitHub [https://github.com/lzwjava/code-review-server](https://github.com/lzwjava/code-review-server).

---

# code-review-server

CodeReview est une plateforme professionnelle pour la révision de code, la communication et le partage. Les ingénieurs peuvent soumettre leur code pour une révision par des experts afin d'améliorer la qualité de leur code. Elle a été fondée par 6 amateurs d'Internet, y compris moi.

![img](./img/cr1.jpg)

![img](./img/cr2.jpg)

# Projets

* [code-review-server](https://github.com/lzwjava/code-review-server)
* [code-review-web](https://github.com/lzwjava/code-review-web)

# Déploiement

Déploiement : fab -H root@reviewcode.cn deploy

Installer les dépendances : composer install, composer update

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