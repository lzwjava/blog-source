---
audio: false
generated: true
lang: ar
layout: post
title: إصلاح وضع المستخدم في TeX Live tlmgr
translated: true
type: note
---

يشير الخطأ إلى أن وضع مستخدم `tlmgr` غير مهيأ على نظام Debian/Ubuntu الخاص بك. هذه مشكلة شائعة في تثبيتات TeX Live من مستودعات Ubuntu. إليك كيفية إصلاح ذلك:

## الحل 1: تهيئة وضع مستخدم tlmgr

أولاً، قم بتهيئة وضع المستخدم:

```bash
tlmgr init-usertree
```

إذا لم ينجح ذلك، جرب:

```bash
tlmgr --usermode init-usertree
```

## الحل 2: استخدم apt بدلاً من ذلك (موصى به لـ Ubuntu)

بما أنك تستخدم Ubuntu/Debian، فغالبًا ما يكون الأمر أسهل باستخدام مدير الحزم للنظام:

```bash
sudo apt update
sudo apt install texlive-fonts-extra
```

سيؤدي هذا إلى تثبيت FontAwesome5 مع حزم الخطوط الأخرى.

## الحل 3: تحقق مما إذا كان FontAwesome5 مثبتًا بالفعل

قد يكون مثبتًا لديك بالفعل. اختبر ذلك عن طريق إنشاء ملف LaTeX بسيط:

```latex
\documentclass{article}
\usepackage{fontawesome5}

\begin{document}
\faHome
\end{document}
```

قم بترجمته باستخدام:
```bash
pdflatex test.tex
```

## الحل 4: إذا كنت بحاجة إلى أحدث إصدار

إذا كنت بحاجة تحديدًا إلى أحدث إصدار من FontAwesome5، يمكنك:

1. تنزيل الحزمة يدويًا من CTAN
2. تثبيتها في دليل texmf المحلي الخاص بك:

```bash
mkdir -p ~/texmf/tex/latex/fontawesome5
# استخرج الحزمة التي تم تنزيلها إلى هذا الدليل
texhash ~/texmf
```

## فحص سريع

لمعرفة حزم TeX المثبتة لديك حاليًا:

```bash
dpkg -l | grep texlive
```

لمعظم المستخدمين، فإن `sudo apt install texlive-fonts-extra` هو الحل الأبسط الذي يتجنب مشاكل وضع مستخدم tlmgr تمامًا.