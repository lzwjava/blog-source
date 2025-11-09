---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: المحررات النصية الافتراضية في آر إتش إي إل مينيمال
translated: true
type: note
---

في نظام Red Hat Enterprise Linux (RHEL)، خاصة في التثبيت الأدنى (الافتراضي لخوادم والإعدادات خفيفة الوزن)، محرر النصوص الوحيد المتاح مباشرة هو **vi**، المقدم من حزمة `vim-minimal`. هذا يمنحك تنفيذًا أساسيًا ومتوافقًا لأمر `vi` الكلاسيكي لتحرير الملفات في الطرفية.

- **`vim` الكامل** (الإصدار المحسن مع المزيد من الميزات، مثل تلوين الصيغة، إلخ) غير مثبت افتراضيًا. يمكنك إضافته باستخدام `sudo dnf install vim-enhanced`.
- **Nano** و **Emacs** غير مضمنين في التثبيت الأدنى. إنهما متوفران في المستودعات لكنهما يتطلبان تثبيتًا صريحًا:
  - لتثبيت Nano: `sudo dnf install nano`
  - لتثبيت Emacs: `sudo dnf install emacs`

هذا يحافظ على خفة التثبيت الأدنى (حوالي 200-300 حزمة إجمالاً) لإعطاء الأولوية للأمان والأداء. إذا كنت تقوم بتثبيت كامل لسطح المكتب أو الخادم (وليس أدنى)، فقد يتم سحب المزيد من الأدوات اعتمادًا على البيئة المحددة.

[بدء الاستخدام مع Nano (Red Hat)](https://www.redhat.com/en/blog/getting-started-nano)  
[لماذا يحتوي RHEL على إصدارين من vim مثبتين افتراضيًا؟](https://unix.stackexchange.com/questions/699071/why-rhel-has-two-vim-installed-by-default)  
[قائمة حزم RHEL 9](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/package_manifest/index)