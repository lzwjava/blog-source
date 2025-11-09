---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: وضع الحلقة العكسية لإدخال رمز التعريف في GPG موضح
translated: true
type: note
---

### ما هو `--pinentry-mode loopback` في GPG؟

في جنو برايفسي جارد (GPG)، يتحكم الخيار `--pinentry-mode loopback` في كيفية تعامل الأداة مع مطالبات عبارة المرور أثناء عمليات التشفير أو فك التشفير أو التوقيع. يُعد Pinentry آلية GPG لإدخال عبارات المرور (مثل كلمات المرور للمفاتيح الخاصة) بشكل آمن، عادةً عبر نافذة حوار رسومية أو مطالبة طرفية أو واجهات أخرى.

#### المعنى الأساسي والغرض
- **وضع Loopback**: يضبط هذا وضع pinentry على سلوك "الارتجاع"، حيث لا يقوم GPG بتشغيل برنامج pinentry خارجي (مثل نافذة منبثقة رسومية). بدلاً من ذلك، يقوم بتقليد pinentry عن طريق إرسال الاستفسارات مباشرةً إلى العملية التي تستدعيه (مثل سكريبت أو تطبيق). وهذا يسمح بتوفير عبارة المرور برمجياً، مثل عبر الإدخال القياسي (STDIN)، أو متغيرات البيئة، أو الملفات، دون مطالبات تفاعلية من المستخدم.

- **لماذا تستخدمه؟**
  - مثالي للأتمتة: في سكريبتات Bash، أو خطوط أنابيب CI/CD (مثل GitHub Actions)، أو البيئات غير التفاعلية (مثل جلسات SSH) حيث لا يمكن ظهور نافذة حوار رسومية.
  - يتجنب التوقف عن العمل أو الفشل في الإعدادات غير التفاعلية.
  - منذ إصدار GnuPG 2.1.12، غالباً ما يُسمح بـ loopback افتراضياً مع `--allow-loopback-pinentry`، لكن تعيين `--pinentry-mode loopback` بشكل صريح يضمن استخدامه.

- **مثال شائع للاستخدام**:
  لفك تشفير ملف في سكريبت مع توفير عبارة المرور عبر STDIN:
  ```
  echo "your-passphrase" | gpg --pinentry-mode loopback --passphrase-fd 0 --decrypt encrypted-file.gpg > decrypted-file.txt
  ```
  - `--passphrase-fd 0`: يقرأ عبارة المرور من واصف الملف 0 (STDIN).
  - يؤدي هذا إلى المطالبة مرة واحدة (أو يستخدم ذاكرة التخزين المؤقت إذا تم تكوينها) ويعمل بشكل غير تفاعلي.

#### المحاذير المحتملة
- **ملاحظة أمنية**: يمكن أن يعرض Loopback عبارات المرور في قوائم العمليات أو السجلات إذا لم يتم التعامل معها بحذر — استخدمه فقط في بيئات موثوقة.
- **التكوين**: لتمكينه عالمياً، أضف `allow-loopback-pinentry` إلى ملف `~/.gnupg/gpg-agent.conf` وأعد التحميل باستخدام `gpgconf --reload gpg-agent`.
  - إذا استمر في المطالبة بشكل متكرر، تحقق من مهلات ذاكرة التخزين المؤقت في `gpg-agent.conf` (مثل `default-cache-ttl 3600` لمدة ساعة واحدة).

هذا الوضع مفيد بشكل خاص للمطورين الذين يدمجون GPG في أدوات مثل توقيع Git أو سير عمل Emacs.

#### المراجع
- [How do I use gpg --pinentry-mode loopback in a bash script?](https://stackoverflow.com/questions/77231645/how-do-i-use-gpg-pinentry-mode-loopback-in-a-bash-script)
- [Agent OPTION (GnuPG Manual)](https://www.gnupg.org/documentation/manuals/gnupg/Agent-OPTION.html)
- [GnuPG - ArchWiki](https://wiki.archlinux.org/title/GnuPG)