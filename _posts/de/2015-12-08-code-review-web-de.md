---
audio: false
generated: false
image: false
lang: de
layout: post
title: Code-Review Web
translated: true
---

Dies ist die README.md aus dem GitHub-Projekt [https://github.com/lzwjava/code-review-web](https://github.com/lzwjava/code-review-web).

---

# code-review-web

CodeReview ist eine professionelle Plattform für Code-Review, Kommunikation und Austausch. Ingenieure können ihren Code zur Expertenprüfung einreichen, um die Qualität ihres Codes zu verbessern. Sie wurde von 6 Internet-Liebhabern, einschließlich mir, gegründet.

![img](./img/cr1.jpg)

![img](./img/cr2.jpg)

# Projekte

* [code-review-server](https://github.com/lzwjava/code-review-server)
* [code-review-web](https://github.com/lzwjava/code-review-web)

### Bauen

``` bash
npm install
# Überwachung:
node server.js
# Bauen:
npm run build
# Bereitstellen
npm run deploy
# Untermodul
git submodule init
git submodule update
```

### Debug

Kopieren Sie apitest.conf in /usr/local/nginx/conf/sites/. In nginx.conf werden die sites/*.conf importiert. Starten Sie nginx neu.

### Mitwirkende

| author  | Commits |
| ------------- | ------------- |
| lzwjava  | 302 |
| LeslieYQ | 73  |
|Martin|52|
|zangqilong|4|