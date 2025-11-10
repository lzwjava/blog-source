---
audio: false
generated: true
image: false
lang: ar
layout: post
title: تهيئة إن جينكس على ماك أو إس هومبرو
translated: true
type: note
---

بالنسبة لـ Nginx المثبت عبر Homebrew على نظام macOS (كما هو موضح في مسار الملف الثنائي `/opt/homebrew/bin/nginx`)، فإن ملف التكوين الرئيسي يقع عادةً في:

```
/opt/homebrew/etc/nginx/nginx.conf
```

يحتوي هذا الدليل أيضًا على ملفات أخرى مرتبطة، مثل كتل الخادم في دليل فرعي `servers/` (مثال: `/opt/homebrew/etc/nginx/servers/`).

لتأكيد مسار ملف التكوين الدقيق الذي تستخدمه نسخة Nginx الخاصة بك، قم بتشغيل الأمر التالي في الطرفية:

```
nginx -t
```

سيؤدي هذا إلى اختبار التكوين وإخراج المسار إلى ملف `nginx.conf` الذي يستخدمه. بدلاً من ذلك، يمكنك استخدام `nginx -V` لرؤية تفاصيل وقت الترجمة، بما في ذلك بادئة مسار التكوين.

إذا كنت تستخدم جهاز Mac قديمًا يعتمد على معالج Intel حيث يقوم Homebrew بالتركيب في `/usr/local` بدلاً من ذلك، فسيكون المسار هو `/usr/local/etc/nginx/nginx.conf`، لكن المسار الثنائي الذي قدمته يؤكد موقع `/opt/homebrew`.

**المراجع**  
[Locate the nginx.conf file my nginx is actually using - Stack Overflow](https://stackoverflow.com/questions/19910042/locate-the-nginx-conf-file-my-nginx-is-actually-using)  
[Installing nginx in macOS using homebrew | by Ram - Medium](https://medium.com/@rprprasath05/installing-nginx-in-macos-ventura-using-homebrew-12b87a900a03)  
[Simple Configuration of NGINX on Mac - DEV Community](https://dev.to/arjavdave/simple-configuration-of-nginx-on-mac-3cg3)