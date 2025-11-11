---
audio: false
generated: true
lang: ar
layout: post
title: خيارات نافذة ويندوز
translated: true
type: note
---

بالإضافة إلى PowerShell وGit Bash وموجه أوامر Windows القياسي (الذي يُشار إليه غالبًا باسم "terminal")، لدى مستخدمي Windows عدة خيارات أخرى لبيئات bash أو shell. فيما يلي بعض البدائل البارزة:

- **Cygwin**: هذه مجموعة من الأدوات التي توفر بيئة شبيهة بـ Unix على Windows. وهي تتضمن shell من نوع bash، مما يسمح لك بتشغيل أوامر ونصوص bash بشكل أصلي على Windows. يقوم Cygwin بشكل أساسي بمحاكاة طبقة متوافقة مع POSIX، مما يجعله خيارًا شائعًا للمستخدمين المألوفين مع أنظمة Unix.

- **Windows Subsystem for Linux (WSL)**: يمكّنك WSL من تشغيل توزيعة Linux كاملة (مثل Ubuntu أو Debian أو Fedora) مباشرة على Windows. باستخدام WSL، يمكنك استخدام various Linux shells، بما في ذلك:
  - **Bash**: Shell الافتراضي في العديد من توزيعات Linux، متوفر عبر WSL.
  - **Zsh (Z Shell)**: shell قوي بميزات متقدمة مثل إكمال تبويب محسن وإمكانيات تخصيص، يمكن تثبيته ضمن توزيعة Linux على WSL.
  - **Fish (Friendly Interactive Shell)**: shell سهل الاستخدام بميزات مثل الاقتراحات التلقائية وتلوين بناء الجملة، يمكن تثبيته أيضًا عبر WSL.

- **Take Command**: shell تجاري مصمم خصيصًا لنظام Windows، يقدم تجربة سطر أوامر أكثر تقدمًا من موجه الأوامر الافتراضي. وهو يدعم البرمجة النصية المعززة وواجهة رسومية مع الحفاظ على التوافق مع أوامر Windows.

هذه الخيارات توسع قدرات سطر الأوامر على Windows، لتلائم التفضيلات المختلفة—سواء كنت تبحث عن تجربة bash شبيهة بـ Unix (عبر Cygwin أو WSL) أو بديل shell أصلي لنظام Windows (مثل Take Command). يمكن تثبيت وتكوين كل منها بناءً على احتياجاتك، مما يوفر مرونة تتجاوز shells المذكورة في الاستعلام.