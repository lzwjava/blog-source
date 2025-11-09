---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: دليل تهيئة غلاف غوستي
translated: true
type: note
---

### Ghostty وملف .bashrc على أوبونتو

تتصرف Ghostty بشكل مشابه لـ GNOME Terminal الافتراضي على أوبونتو (وتوزيعات لينكس الأخرى) عندما يتعلق الأمر بتحميل ملف `.bashrc`. افتراضيًا، تبدأ Ghostty **أصداف غير دخول تفاعلية** لـ bash، مما يعني أنها تستدعي ملف `~/.bashrc` مباشرة — تمامًا مثل GNOME Terminal. هذا هو السلوك القياسي لمعظم أطراف لينكس، حيث يتعامل ملف `.bashrc` مع إعداد الصدفة التفاعلية (مثل: الأسماء المستعارة، موجهات الأوامر، متغيرات البيئة لجلسات غير الدخول).

#### كيف يتم تحميل .bashrc
- عند فتح نافذة أو لسان تبويب جديدة في Ghostty، فإنها تنفذ `bash` (أو الصدفة الافتراضية لديك) كصدفة غير دخول.
- يتحقق bash عن وجود `~/.bashrc` ويستدعيه إذا كانت الصدفة تفاعلية (وهي كذلك افتراضيًا).
- إذا كان لديك ملف `~/.bash_profile` (عادةً لأصداف الدخول)، فل يتم استدعاؤه إلا إذا قمت بتكوين Ghostty بشكل صريح لبدء صدفة دخول (على سبيل المثال، بإضافة `initial-command = bash --login` إلى `~/.config/ghostty/config`).
- المشاكل المحتملة: يبلغ بعض المستخدمين عن عدم تحميل `.bashrc` عند الإطلاق الأول لمستخدمين جدد أو في إعدادات محددة (مثل جلسات SSH عن بُعد على أوبونتو). يمكن غالبًا إصلاح هذا من خلال التأكد من عدم وجود ملف `~/.bash_profile` متعارض، أو عن طريق استدعائه يدويًا في الإعدادات الخاصة بك. إضافة حارس في `.bashrc` مثل `[[ $- != *i* ]] && return` يمكن أن يمنع المشاكل في السياقات غير التفاعلية.

باختصار، نعم — Ghostty مطابقة تمامًا للأداة الطرفية الافتراضية من حيث استخدام `.bashrc` على أوبونتو، بنفس افتراضية عدم الدخول الافتراضية.

### Ghostty على macOS: .zprofile أم .bash_profile؟

على macOS، تتبع Ghostty تقليد النظام الأساسي (مثل Terminal.app) وتبدأ **أصداف الدخول** افتراضيًا، بغض النظر عن الصدفة المستخدمة. وهذا يؤثر على ملف التعريف الذي يتم تحميله:

- **إذا كنت تستخدم zsh (الافتراضي في macOS منذ كاتالينا)**: فإنه يستدعي `~/.zprofile` (لإعداد الدخول) *و* `~/.zshrc` (لإعداد التفاعل) في كل مرة يتم فيها فتح طرفية جديدة.
- **إذا كنت تستخدم bash**: فإنه يستدعي `~/.bash_profile` (صدفة دخول). لن يقوم bash باستدعاء `~/.bashrc` مباشرة هنا — حيث أن `~/.bashrc` مخصص فقط لأصداف غير الدخول التفاعلية. لتضمين محتوى `.bashrc`، أضف هذا إلى ملف `~/.bash_profile` الخاص بك:
  ```
  if [ -f ~/.bashrc ]; then . ~/.bashrc; fi
  ```

لذا، فإنه يحمل `~/.zprofile` للإعداد الافتراضي لـ zsh، أو `~/.bash_profile` إذا كنت تستخدم bash. يمكنك تبديل الصدفة أو التعديل عبر إعدادات Ghostty إذا لزم الأمر.

[Shell Integration - Ghostty](https://ghostty.org/docs/features/shell-integration)  
[macOS Login Shells - Ghostty](https://ghostty.org/docs/help/macos-login-shells)  
[Potential bug, .bashrc not read on startup - GitHub Discussion](https://github.com/ghostty-org/ghostty/discussions/3437)  
[Bash Startup Files - GNU Manual](https://www.gnu.org/software/bash/manual/bash.html#Bash-Startup-Files)