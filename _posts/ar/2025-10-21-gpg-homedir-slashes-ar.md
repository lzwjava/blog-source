---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: استخدم الشرطة المائلة للأمام لمجلد بي جي بي الرئيسي
translated: true
type: note
---

### فواصل المسارات لخيار `--homedir` في GPG باستخدام Git Bash (Windows)

في Git Bash على نظام Windows، **استخدم دائمًا الشرطة المائلة للأمام (`/`)** لمسار `--homedir`. يمثل Git Bash بيئة شبيهة بـUnix (مبنية على MSYS2)، لذا فهو يتوقع مسارات بنمط POSIX باستخدام `/` كفاصل. من المرجح أن تسبب الشرطة المائلة للخلف (`\`) أخطاء، نظرًا لأن GPG في هذا السياق لا يتعامل معها بشكل أصلي دون تهريب، وهو ما يشكل عبئًا غير ضروري.

#### لماذا `/`؟
- يقوم Git Bash بربط محركات أقراص Windows بهيكل شبيه بـUnix: `C:\Users\YourName` تصبح `/c/Users/YourName`.
- يتبع GPG (المضمن مع Git لنظام Windows) نفس الاصطلاح. يمكن لاستخدام `\` أن يؤدي إلى فشل في تحديد المسار أو أن يتطلب التهريب المزدوج (مثل `\\`)، وهو عرضة للخطأ.
- تستخدم الأمثلة الرسمية وإعدادات المجتمع (مثل تلك المستخدمة للتوقيع بـGit) `/` بشكل ثابت في Git Bash.

#### مثال للاستخدام
```
gpg --homedir /c/Users/YourName/.gnupg --list-secret-keys
```
- يشير هذا إلى مجلد GPG الافتراضي على محرك C:.
- لمجلد مخصص: `gpg --homedir /d/MyCustomGpgDir --full-generate-key` (على محرك D:).

#### اختبار سريع
في Git Bash:
1.  نفذ الأمر `pwd` — سيكون الناتج شيئًا مثل `/c/Users/YourName` (باستخدام `/` فقط).
2.  جرب `gpg --homedir /c/Users/YourName/.gnupg --version` (يعمل).
3.  قارن باستخدام `\`: `gpg --homedir C:\Users\YourName\.gnupg --version` (يفشل أو يعطي تحذيرًا).

إذا كنت تدمج الاستخدام مع موجه أوامر Windows أو PowerShell، فإنهما يقبلان كلاً من `/` و `\`، ولكن التزم باستخدام `/` في Git Bash للاتساق. للمزيد، راجع [دليل GnuPG لخيارات التهيئة](https://www.gnupg.org/documentation/manuals/gnupg/Configuration-Options.html).