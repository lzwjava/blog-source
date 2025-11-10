---
audio: false
generated: true
lang: ar
layout: post
title: إنشاء سيرة ذاتية داكنة باستخدام لاتك
translated: true
type: note
---

لدعم بناء `resume-en-dark.pdf` باستخدام `awesome-cv-dark.cls` الخاص بك، ستحتاج إلى:

### ✅ 1. إنشاء ملف مصدر LaTeX جديد للإصدار الداكن

انسخ `resume-en.tex` الحالي إلى ملف جديد يستخدم صنف السمة الداكنة:

#### `latex/en/resume-en-dark.tex`

```latex
%-------------------------------------------------------------------------------
% CONFIGURATIONS
%-------------------------------------------------------------------------------
\documentclass[11pt, a4paper]{../awesome-cv-dark} % استخدم الإصدار الداكن هنا

% تكبيش هوامش الصفحة
\geometry{left=1.4cm, top=.8cm, right=1.4cm, bottom=1.8cm, footskip=.5cm}

% اللون لإبراز النقاط
\colorlet{awesome}{awesome-red}

% تعيين إبراز القسم
\setbool{acvSectionColorHighlight}{true}

\usepackage{fontspec}
\usepackage{xeCJK}
\usepackage{ifthen}

% تضمين محتوى السيرة الذاتية الفعلي (نفس إصدارك العادي)
\input{resume-en-content.tex}
```

> ✅ يمكنك إعادة استخدام `resume-en-content.tex` الحالي لتجنب التكرار، أو نسخ/لصق المحتوى من `resume-en.tex`.

---

### ✅ 2. تحديث `Makefile`

أضف قاعدة جديدة في `Makefile` لبناء `resume-en-dark.pdf`.

ابحث عن هذا الجزء في `Makefile`:

```make
latex: $(foreach x, coverletter coverletter-zh resume-zh resume, $x.pdf)
```

عدله لتضمين السيرة الذاتية الداكنة:

```make
latex: $(foreach x, coverletter coverletter-zh resume-zh resume resume-en-dark, $x.pdf)
```

ثم أضف قاعدة البناء:

```make
resume-en-dark.pdf: $(RESUME_EN_DIR)/resume-en-dark.tex $(RESUME_SRCS)
	$(CC) -output-directory=$(RESUME_EN_DIR) $<
```

> 🔁 إذا كنت تحتفظ بجميع الأصول في نفس المجلد (`latex/en/resume-en/`)، فلن تحتاج إلى تحديث `RESUME_SRCS`.

---

### ✅ 3. اختياري: الإضافة إلى الهدف `copy`

إذا كنت تريد نسخ الملف المُنشأ إلى `assets/resume`، فحدث `copy`:

```make
	cp $(RESUME_EN_DIR)/resume-en-dark.pdf assets/resume/Zhiwei.Li.Resume.Dark.pdf
```

---

### ✅ 4. بناؤه

الآن يمكنك فقط تشغيل:

```bash
make resume-en-dark.pdf
```

---

أعلمني إذا كان المحتوى الخاص بك مشتركًا عبر السمات وتريد هيكلًا أكثر ذكاءً باستخدام ملفات `.tex` مشتركة مثل `resume-en-content.tex`.