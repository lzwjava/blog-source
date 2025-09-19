---
audio: false
generated: false
image: false
lang: hi
layout: post
title: कोड समीक्षा वेब
translated: true
---

यह README.md है GitHub पर एक प्रोजेक्ट [https://github.com/lzwjava/code-review-web](https://github.com/lzwjava/code-review-web) से.

---

# code-review-web

CodeReview एक प्रोफेशनल प्लेटफॉर्म है कोड रिव्यू, संचार, और शेयर के लिए। इंजीनियर अपने कोड को विशेषज्ञ रिव्यू के लिए सबमिट कर सकते हैं अपने कोड की गुणवत्ता को बेहतर बनाने के लिए। इसे 6 इंटरनेट प्रेमी ने स्थापित किया था, जिसमें मैं भी शामिल हूँ।

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

apitest.conf को /usr/local/nginx/conf/sites/ के नीचे कॉपी करें। nginx.conf में sites/*.conf को इम्पोर्ट करें। nginx को रीस्टार्ट करें।

### Contributors

| author  | commits |
| ------------- | ------------- |
| lzwjava  | 302 |
| LeslieYQ | 73  |
|Martin|52|
|zangqilong|4|