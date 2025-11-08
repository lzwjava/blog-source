---
audio: false
generated: false
image: false
lang: ja
layout: post
title: コードレビューサーバー
translated: true
type: post
---

これは、GitHubプロジェクト[https://github.com/lzwjava/code-review-server](https://github.com/lzwjava/code-review-server)のREADME.mdです。

---

# code-review-server

CodeReviewは、コードレビュー、コミュニケーション、共有のための専門プラットフォームです。エンジニアは、専門家のレビューを受けることで、コードの質を向上させることができます。設立者は、私を含む6人のインターネット愛好家です。

![img](./img/cr1.jpg)

![img](./img/cr2.jpg)

# プロジェクト

* [code-review-server](https://github.com/lzwjava/code-review-server)
* [code-review-web](https://github.com/lzwjava/code-review-web)

# デプロイ

デプロイ: fab -H root@reviewcode.cn deploy

依存関係のインストール: composer install, composer update

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