---
audio: false
lang: es
layout: post
title: Revisión de Código del Servidor
translated: true
---

Este es el README.md del proyecto de github [https://github.com/lzwjava/code-review-server](https://github.com/lzwjava/code-review-server).

---

# code-review-server

CodeReview es una plataforma profesional para la revisión de código, la comunicación y el intercambio. Los ingenieros pueden enviar su código para su revisión por expertos para mejorar la calidad de su código. Fue fundada por 6 amantes de Internet, incluyendo yo.

![img](./img/cr1.jpg)

![img](./img/cr2.jpg)

# Proyectos

* [code-review-server](https://github.com/lzwjava/code-review-server)
* [code-review-web](https://github.com/lzwjava/code-review-web)

# Despliegue

Despliegue: fab -H root@reviewcode.cn desplegar

Instalar dependencias: composer install, composer update

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