---
audio: false
generated: true
image: false
lang: ar
layout: post
model: anthropic/claude-sonnet-4
title: تثبيت واستخدام xdotool على لينكس
translated: true
type: note
---

لتثبيت `xdotool` على نظام Linux الخاص بك، يمكنك استخدام مدير الحزم الخاص بتوزيعتك. بناءً على اسم المضيف الذي يظهر "XiaoXin"، فمن المرجح أنك تستخدم Ubuntu أو توزيعة مبنية على Debian. فيما يلي أوامر التثبيت للتوزيعات الشائعة لنظام Linux:

## Ubuntu/Debian:
```bash
sudo apt update
sudo apt install xdotool
```

## CentOS/RHEL/Fedora:
```bash
# للإصدارات الأحدث (dnf)
sudo dnf install xdotool

# للإصدارات الأقدم (yum)
sudo yum install xdotool
```

## Arch Linux:
```bash
sudo pacman -S xdotool
```

## openSUSE:
```bash
sudo zypper install xdotool
```

بعد التثبيت، يمكنك التحقق من عمل الأداة بتنفيذ:
```bash
xdotool --version
```

بمجرد التثبيت، يجب أن يصبح بإمكان نص Python الخاص بك استخدام `xdotool` لاسترداد عنوان المتصفح. تُستخدم أداة `xdotool` بشكل شائع لأتمتة مهام سطح المكتب X11، بما في ذلك الحصول على عناوين النوافذ، وهو ما يبدو أن النص الخاص بك يحاول القيام به.

إذا كنت لا تزال تواجه مشكلات بعد التثبيت، تأكد من:
1. أنك تشغل النص في بيئة X11 (وليس Wayland)
2. أن لديك نافذة متصفح نشطة مفتوحة
3. أن نافذة المتصفح لها التركيز أو تكون مرئية