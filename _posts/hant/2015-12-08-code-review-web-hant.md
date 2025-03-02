---
audio: false
generated: false
lang: hant
layout: post
title: 程式碼審查網
translated: true
---

這是來自 GitHub 專案 [https://github.com/lzwjava/code-review-web](https://github.com/lzwjava/code-review-web) 的 README.md。

---

# code-review-web

CodeReview 是一個專業的程式碼評論、溝通和分享平台。工程師可以提交他們的程式碼給專家審查，以提高程式碼的質量。它由包括我在內的 6 名網絡愛好者創立。

![img](./img/cr1.jpg)

![img](./img/cr2.jpg)

# 專案

* [code-review-server](https://github.com/lzwjava/code-review-server)
* [code-review-web](https://github.com/lzwjava/code-review-web)

### 建立

``` bash
npm install
# 觀察:
node server.js
# 建立:
npm run build
# 部署
npm run deploy
# 子模組
git submodule init
git submodule update
```

### 檢錯

將 apitest.conf 複製到 /usr/local/nginx/conf/sites/ 下面。在 nginx.conf 中引入 sites/*.conf。重啟 nginx。

### 貢獻者

| 作者  | 提交 |
| ------------- | ------------- |
| lzwjava  | 302 |
| LeslieYQ | 73  |
| Martin | 52 |
| zangqilong | 4 |