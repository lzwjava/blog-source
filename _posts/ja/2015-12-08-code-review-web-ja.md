---
audio: false
generated: false
image: false
lang: ja
layout: post
title: コードレビューウェブ
translated: true
---

これは GitHub プロジェクト [https://github.com/lzwjava/code-review-web](https://github.com/lzwjava/code-review-web) の README.md です。

---

# code-review-web

CodeReview は、コードレビュー、コミュニケーション、共有のための専門プラットフォームです。エンジニアは、専門家によるレビューを受けることで、コードの質を向上させることができます。創設メンバーは6人のインターネット愛好家で、その中には自分も含まれています。

![img](./img/cr1.jpg)

![img](./img/cr2.jpg)

# プロジェクト

* [code-review-server](https://github.com/lzwjava/code-review-server)
* [code-review-web](https://github.com/lzwjava/code-review-web)

### ビルド

``` bash
npm install
# ウォッチ:
node server.js
# ビルド:
npm run build
# デプロイ
npm run deploy
# サブモジュール
git submodule init
git submodule update
```

### デバッグ

apitest.conf を /usr/local/nginx/conf/sites/ 配下にコピーします。nginx.conf で sites/*.conf をインポートし、nginx を再起動します。

### コントリビューター

| author  | コミット |
| ------------- | ------------- |
| lzwjava  | 302 |
| LeslieYQ | 73  |
| Martin | 52 |
| zangqilong | 4 |