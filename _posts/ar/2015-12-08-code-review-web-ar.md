---
audio: false
generated: false
image: false
lang: ar
layout: post
title: مراجعة الكود على الإنترنت
translated: true
---

هذا هو ملف README.md لمشروع جيت هاب [https://github.com/lzwjava/code-review-web](https://github.com/lzwjava/code-review-web).

---

# code-review-web

CodeReview هي منصة محترفة ل مراجعة الكود، و التواصل، و المشاراكة. يمكن للمهندسين تقديم كودهم لمراجعة الخبراء لتحسين جودة كودهم. تأسست من قبل ستة محبين للإنترنت، بما في ذلك أنا.

![img](./img/cr1.jpg)

![img](./img/cr2.jpg)

# Projects

* [code-review-server](https://github.com/lzwjava/code-review-server)
* [code-review-web](https://github.com/lzwjava/code-review-web)

### Building

``` bash
npm install
# watch:
node server.js
# build:
npm run build
# deploy
npm run deploy
# submodule
git submodule init
git submodule update
```

### Debug

Copy apitest.conf to /usr/local/nginx/conf/sites/ . Include sites/*.conf in nginx.conf. Restart nginx.

### Contributors

| author  | commits |
| ------------- | ------------- |
| lzwjava  | 302 |
| LeslieYQ | 73  |
|Martin|52|
|zangqilong|4|