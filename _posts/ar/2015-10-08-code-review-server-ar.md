---
audio: false
lang: ar
layout: post
title: مراجعه الكود
translated: true
---

هذا README.md من مشروع GitHub [https://github.com/lzwjava/code-review-server](https://github.com/lzwjava/code-review-server).

---

# code-review-server

CodeReview هو منصة محترفة لتقييم الكود، ومتابعة التواصل، والتبادل. يمكن للمهندسين تقديم كودهم لتقييم الخبراء لتحسين جودة الكود. و تم تأسيسها من قبل ستة محبين للإنترنت، بما في ذلك أنا.

![img](./img/cr1.jpg)

![img](./img/cr2.jpg)

# مشاريع

* [code-review-server](https://github.com/lzwjava/code-review-server)
* [code-review-web](https://github.com/lzwjava/code-review-web)

# نشر

نشر: fab -H root@reviewcode.cn deploy

تثبيت الاعتماديات: composer install, composer update

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