---
audio: false
generated: false
lang: fr
layout: post
title: Révision de code Web
translated: true
---

Voici le README.md du projet github [https://github.com/lzwjava/code-review-web](https://github.com/lzwjava/code-review-web).

---

# code-review-web

CodeReview est une plateforme professionnelle pour la révision de code, la communication et le partage. Les ingénieurs peuvent soumettre leur code pour une révision par des experts afin d'améliorer la qualité de leur code. Elle a été fondée par 6 passionnés d'Internet, dont moi.

![img](./img/cr1.jpg)

![img](./img/cr2.jpg)

# Projets

* [code-review-server](https://github.com/lzwjava/code-review-server)
* [code-review-web](https://github.com/lzwjava/code-review-web)

### Construction

``` bash
npm install
# surveillance :
node server.js
# construction :
npm run build
# déploiement
npm run deploy
# sous-module
git submodule init
git submodule update
```

### Débogage

Copiez apitest.conf dans /usr/local/nginx/conf/sites/. Importez sites/*.conf dans nginx.conf. Redémarrez nginx.

### Contributeurs

| auteur  | validations |
| ------------- | ------------- |
| lzwjava  | 302 |
| LeslieYQ | 73  |
| Martin | 52 |
| zangqilong | 4 |