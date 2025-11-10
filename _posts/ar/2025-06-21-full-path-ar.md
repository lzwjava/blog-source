---
audio: false
generated: true
lang: ar
layout: post
title: الحصول على المسار الكامل للملف في أوبونتو
translated: true
type: note
---

في أوبونتو، يمكنك الحصول على المسار الكامل لملف باستخدام الأمر `realpath` أو `readlink -f`. لمثالك مع `geckodriver`، يمكنك تشغيل:

```bash
realpath ./geckodriver
```

أو

```bash
readlink -f ./geckodriver
```

سيخرج كلا الأمرين المسار الكامل، على سبيل المثال:

```
/home/lzw/bin/geckodriver
```

أمر `realpath` مباشر وشائع الاستخدام لهذا الغرض. إذا لم يكن `realpath` مثبتًا، يمكنك تثبيته عبر:

```bash
sudo apt install realpath
```

بديلًا عن ذلك، `readlink -f` عادة ما يكون متاحًا افتراضيًا كجزء من coreutils.