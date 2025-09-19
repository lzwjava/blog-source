---
audio: false
generated: false
image: false
lang: ja
layout: post
title: ライブモバイルウェブ
translated: true
---

これは、GitHubプロジェクト [https://github.com/lzwjava/live-mobile-web](https://github.com/lzwjava/live-mobile-web) のREADME.mdです。

---

# live-mobile-web

* [live-server](https://github.com/lzwjava/live-server)
* [live-web](https://github.com/lzwjava/live-web)
* [live-mobile-web](https://github.com/lzwjava/live-mobile-web)

<div align="center">
<img src="./img/img1.jpg" width="300px" /><img/>
<img src="./img/img2.jpg" width="300px" /><img/>
</div>

<div align="center">
<img src="./img/funlive4.jpg" width="300px" /><img/>
<img src="./img/funlive5.jpg" width="300px" /><img/>
</div>

<div align="center">
<img src="./img/funlive6.jpg" width="300px" /><img/>
<img src="./img/funlive8.jpg" width="300px" /><img/>
</div>

### ビルド

``` bash
npm install
# ビルド:
npm run build

git submodule update --init --recursive

fab -H ubuntu@xx.xx.xx.xx deploy
```