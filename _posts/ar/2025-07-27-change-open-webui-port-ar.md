---
audio: false
generated: true
image: false
lang: ar
layout: post
title: تغيير منفذ واجهة الويب المفتوحة
translated: true
type: note
---

لتغيير المنفذ عند تشغيل Open WebUI باستخدام أمر `open-webui serve` (عادةً بعد التثبيت عبر pip)، استخدم علم `--port` متبوعًا برقم المنفذ الذي تريده. المنفذ الافتراضي هو 8080.

### الخطوات:
1. تأكد من تثبيت Open WebUI:  
   ```
   pip install open-webui
   ```

2. تشغيل الخادم على منفذ مختلف (مثال: 3000):  
   ```
   open-webui serve --port 3000
   ```

   - هذا سيجعل واجهة الويب متاحة على `http://localhost:3000` (أو عنوان IP الخادم الخاص بك مع المنفذ الجديد).
   - ملاحظة: متغير البيئة `PORT` يتم تجاهله عند استخدام أمر `serve`؛ يجب استخدام علم `--port` بدلاً من ذلك.

إذا كنت تستخدم Docker بدلاً من التثبيت المباشر:
- عيّن متغير البيئة `PORT`، مثال: `docker run -e PORT=3000 ...`.
- اربط المنفذ خارجيًا باستخدام `-p <host_port>:3000` (عدل حسب الحاجة).

للحصول على تفاصيل التثبيت الكاملة والإعدادات، راجع الوثائق الرسمية.

[Environment Variable Configuration | Open WebUI](https://docs.openwebui.com/getting-started/env-configuration/)  
[Quick Start | Open WebUI](https://docs.openwebui.com/getting-started/quick-start/)