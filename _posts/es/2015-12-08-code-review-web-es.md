---
audio: false
generated: false
lang: es
layout: post
title: Revisión de Código Web
translated: true
---

Este es el README.md del proyecto de GitHub [https://github.com/lzwjava/code-review-web](https://github.com/lzwjava/code-review-web).

---

# code-review-web

CodeReview es una plataforma profesional para la revisión de código, comunicación y compartir. Los ingenieros pueden enviar su código para una revisión experta para mejorar la calidad de su código. Fue fundada por 6 amantes de Internet, incluido yo.

![img](./img/cr1.jpg)

![img](./img/cr2.jpg)

# Proyectos

* [code-review-server](https://github.com/lzwjava/code-review-server)
* [code-review-web](https://github.com/lzwjava/code-review-web)

### Construyendo

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

### Depuración

Copie apitest.conf en /usr/local/nginx/conf/sites/bajo. En nginx.conf, importe sites/*.conf. Reinicie nginx.

### Colaboradores

| autor  | commits |
| ------------- | ------------- |
| lzwjava  | 302 |
| LeslieYQ | 73  |
|Martin|52|
|zangqilong|4|