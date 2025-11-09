---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: دمج Git Bash مع Windows Terminal
translated: true
type: note
---

نعم، يمكن لـ Git Bash التشغيل في نافذة وحدة تحكم (يستخدم افتراضيًا طرفيته الخاصة MinTTY) ويتكامل بسلاسة مع Windows Terminal. كل ما تحتاجه هو إضافة ملف تعريف مخصص له في إعدادات Windows Terminal - وتوجيهه إلى الملف التنفيذي `bash.exe` في تثبيت Git الخاص بك (عادةً `C:\Program Files\Git\bin\bash.exe`). بمجرد إضافته، يمكنك تشغيله في علامة تبويب أو جزء جديد مثل أي shell آخر.

أنت مخطئ بشأن قيود Windows Terminal: فهو يدعم أكثر بكثير من مجرد PowerShell و Command Prompt. افتراضيًا، يتعامل مع هذين بالإضافة إلى توزيعات WSL، و Azure Cloud Shell، وحتى الأصداف المخصصة مثل Git Bash أو Cygwin. إنه مصمم ليكون مضيفًا مرنًا لأي بيئة سطر أوامر تقريبًا.

[إضافة Git-Bash إلى Windows Terminal الجديد](https://stackoverflow.com/questions/56839307/adding-git-bash-to-the-new-windows-terminal)  
[إضافة Git-Bash إلى Windows Terminal](https://www.timschaeps.be/post/adding-git-bash-to-the-new-windows-terminal/)  
[في Windows Terminal، كيف يمكنني إضافة bash كأحد خيارات shell؟](https://superuser.com/questions/1763652/in-windows-terminal-how-do-i-add-bash-as-one-of-the-shell-options)