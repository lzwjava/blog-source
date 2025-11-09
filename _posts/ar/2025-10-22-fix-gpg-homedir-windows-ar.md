---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: إصلاح مسارات الدليل الرئيسي لـ GPG على نظام ويندوز
translated: true
type: note
---

نعم، أنت محق. في Git Bash على Windows (الذي يعمل في بيئة تشبه MSYS2/Cygwin)، يؤدي استخدام الشرطات المائلة للخلف (`\`) في مسار `--homedir` لأمر `gpg` إلى تفسير shell للوسيط بشكل خاطئ بسبب طريقة عمل أحرف الهروب وتحويل المسارات. هذا يشوّه المسار (على سبيل المثال، `C:\Users\me\.gnupg` قد يتحول إلى شيء غير صالح مثل `C:Usersme.gnupg` أو يتشوه أكثر أثناء التحويل التلقائي إلى تنسيق Windows)، مما يجعل الدليل غير قابل للحل. نتيجة لذلك، لا يستطيع GPG العثور على ملفات المفاتيح، مما يؤدي إلى خطأ "no secret key" (أو خطأ مشابه، مثل "No such file or directory" لملف `pubring.kbx`).

### الحل السريع
- استخدم الشرطات المائلة للأمام (`/`) مع بادئة محرك الأقراص بنمط MSYS2: `gpg --homedir /c/Users/me/.gnupg ...`
- يتم تحويل هذا تلقائيًا بواسطة MSYS2 إلى مسار Windows الصحيح (مثل `C:\Users\me\.gnupg`) عند تمريره إلى binary GPG الأصلي.
- تجنب استخدام أحرف محركات الأقراص مثل `c:/` بدون الشرطة المائلة الأولى `/` — حيث يتم التعامل معها على أنها مسارات نسبية، مما يؤدي إلى إضافة دليل العمل الحالي الخاص بك مسبقًا ويتسبب في نفس فشل البحث.

بالنسبة لمتغيرات البيئة مثل `GNUPGHOME`، تنطبق نفس القاعدة: عيّنها باستخدام `/` (على سبيل المثال، `export GNUPGHOME=/c/Users/me/.gnupg`).

[مسارات نظام الملفات في MSYS2](https://www.msys2.org/docs/filesystem-paths/)
[مناقشة GNUPGHOME في MSYS2](https://lists.gnupg.org/pipermail/gnupg-users/2025-February/067536.html)
[خطأ GPG --homedir على Windows/MSYS2](https://www.reddit.com/r/GnuPG/comments/1cl4dw8/bug_windows_homedir_with_drive_letter_treated_as/)