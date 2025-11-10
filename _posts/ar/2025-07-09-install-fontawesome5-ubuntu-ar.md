---
audio: false
generated: true
lang: ar
layout: post
title: تثبيت FontAwesome5 في LaTeX على أوبونتو
translated: true
type: note
---

لتركيب FontAwesome5 لـ LaTeX على أوبونتو، لديك عدة خيارات:

## الطريقة 1: استخدام tlmgr (مدير TeX Live)

إذا كان TeX Live مثبتًا لديك، يمكنك استخدام مدير الحزم:

```bash
sudo tlmgr update --self
sudo tlmgr install fontawesome5
```

## الطريقة 2: استخدام مدير الحزم apt

يوفر أوبونتو FontAwesome5 من خلال مستودعاته:

```bash
sudo apt update
sudo apt install texlive-fonts-extra
```

هذا يقوم بتثبيت مجموعة شاملة من الخطوط بما في ذلك FontAwesome5.

## الطريقة 3: التثبيت اليدوي

إذا لم تنجح الطرق المذكورة أعلاه، يمكنك التثبيت يدويًا:

1. حمّل حزمة FontAwesome5 من CTAN
2. استخرجها إلى دليل texmf المحلي لديك:

```bash
mkdir -p ~/texmf/tex/latex/fontawesome5
cd ~/texmf/tex/latex/fontawesome5
# استخرج الحزمة التي تم تحميلها هنا
```

3. حدّث قاعدة بيانات TeX:
```bash
texhash ~/texmf
```

## استخدام FontAwesome5 في LaTeX

بمجرد التثبيت، يمكنك استخدامه في مستندات LaTeX الخاصة بك:

```latex
\documentclass{article}
\usepackage{fontawesome5}

\begin{document}
\faHome \quad أيقونة البيت
\faEnvelope \quad أيقونة البريد الإلكتروني
\faGithub \quad أيقونة GitHub
\end{document}
```

## استكشاف الأخطاء وإصلاحها

إذا واجهت مشاكل:

1. تحقق مما إذا كان تثبيت TeX Live لديك محدثًا:
```bash
tlmgr --version
```

2. تحقق من تثبيت الحزمة:
```bash
tlmgr info fontawesome5
```

3. تأكد من أنك تستخدم XeLaTeX أو LuaLaTeX للحصول على دعم Unicode كامل مع FontAwesome5.

أسهل طريقة هي عادةً الطريقة 2 باستخدام `apt install texlive-fonts-extra` حيث أنها تتعامل مع التبعيات تلقائيًا.