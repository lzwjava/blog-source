---
audio: false
generated: false
image: false
lang: ar
layout: post
title: استخدام Awesome-CV لإنشاء سيرة ذاتية احترافية
translated: true
type: post
---

### مقدمة

قبل استخدام [ZhiyeApp](https://www.zhiyeapp.com)، انتقلت إلى قالب [Awesome-CV](https://github.com/posquit0/Awesome-CV) القوي والقابل للتخصيص. هذا القالب القائم على LaTeX يجعل إنشاء السير الذاتية الاحترافية أمرًا سهلاً وقابلاً للتخصيص بدرجة كبيرة.

---

### لماذا Awesome-CV؟  
- قابل للتخصيص: يمكنك تخصيص الأقسام، الألوان، والتنسيق.  
- مظهر احترافي: تصميم أنيق مثالي لطلبات التوظيف.  
- سهل الاستخدام: يتطلب معرفة بسيطة بـ LaTeX.

---

### مثال سيرتي الذاتية

إليك نسخة مبسطة من ملف `resume.tex` الذي أستخدمه:

```latex
%-------------------------------------------------------------------------------
% الإعدادات
%-------------------------------------------------------------------------------
\documentclass[11pt, a4paper]{awesome-cv}
```

% هوامش الصفحة وإبراز الأقسام
\geometry{left=1.4cm, top=.8cm, right=1.4cm, bottom=1.8cm, footskip=.5cm}
\colorlet{awesome}{awesome-red}
\setbool{acvSectionColorHighlight}{true}

%-------------------------------------------------------------------------------
% المعلومات الشخصية
%-------------------------------------------------------------------------------
\name{زيوي}{لي}
\position{مهندس Full Stack{\enskip\cdotp\enskip}مهندس Backend}
\address{غوانغتشو، الصين}
\mobile{(+86) 132-6163-0925}
\email{lzwjava@gmail.com}
\homepage{https://lzwjava.github.io}
\github{lzwjava}
\linkedin{lzwjava}
\quote{``الحرية الحقيقة"}

%-------------------------------------------------------------------------------
\begin{document}

% العنوان والتذييل
\makecvheader[C]
\makecvfooter{\today}{Zhiwei Li~~~·~~~السيرة الذاتية}{\thepage}

% أقسام المحتوى
\input{resume/summary.tex}
\input{resume/experience.tex}
\input{resume/education.tex}
\input{resume/corporateprojects.tex}
\input{resume/personalprojects.tex}
\input{resume/blogposts.tex}
\input{resume/papers.tex}
\input{resume/books.tex}
\input{resume/skills.tex}
\input{resume/tools.tex}
\input{resume/knowledge.tex}
\input{resume/certificates.tex}

```latex
\end{document}
```

Makefile لأتمتة المهام

لأتمتة عملية إنشاء ملفات PDF، أستخدم ملف Makefile التالي:

```Makefile
.PHONY: awesome-cv
```

```makefile
CC = xelatex
EXAMPLES_DIR = awesome-cv
RESUME_DIR = awesome-cv/resume
RESUME_ZH_DIR = awesome-cv/resume-zh
RESUME_SRCS = $(shell find $(RESUME_DIR) -name '*.tex')
RESUME_ZH_SRCS = $(shell find $(RESUME_ZH_DIR) -name '*.tex')
```

awesome-cv: $(foreach x, coverletter resume-zh resume, $x.pdf)

```makefile
resume.pdf: $(EXAMPLES_DIR)/resume.tex $(RESUME_SRCS)
	$(CC) -output-directory=$(EXAMPLES_DIR) $<
```

تمت ترجمة الكود أعلاه إلى:

```makefile
resume.pdf: $(EXAMPLES_DIR)/resume.tex $(RESUME_SRCS)
	$(CC) -output-directory=$(EXAMPLES_DIR) $<
```

في هذا الكود:

- `resume.pdf` هو الملف الهدف الذي نريد إنشاءه.
- `$(EXAMPLES_DIR)/resume.tex` و `$(RESUME_SRCS)` هي الملفات المصدر التي يعتمد عليها `resume.pdf`.
- `$(CC)` هو الأمر الذي سيتم تنفيذه لإنشاء `resume.pdf`، حيث يتم تمرير الخيار `-output-directory=$(EXAMPLES_DIR)` لتحديد دليل الإخراج، و `$<` يشير إلى أول ملف مصدر في القائمة (`$(EXAMPLES_DIR)/resume.tex`).

resume-zh.pdf: $(EXAMPLES_DIR)/resume-zh.tex $(RESUME_ZH_SRCS)
	$(CC) -output-directory=$(EXAMPLES_DIR) $<

coverletter.pdf: $(EXAMPLES_DIR)/coverletter.tex
	$(CC) -output-directory=$(EXAMPLES_DIR) $<

```makefile
clean:
	rm -rf $(EXAMPLES_DIR)/*.pdf
```

### كيف يعمل

1. إنشاء ملفات PDF:
   - قم بتشغيل `make awesome-cv` لإنشاء ملفات PDF التالية:
     - `resume.pdf`: السيرة الذاتية باللغة الإنجليزية
     - `resume-zh.pdf`: السيرة الذاتية باللغة الصينية
     - `coverletter.pdf`: خطاب التغطية

2. التنظيف:
   - قم بتشغيل `make clean` لحذف جميع ملفات PDF التي تم إنشاؤها.

### الخلاصة

باستخدام Awesome-CV وإعداد Makefile هذا، يصبح إنشاء وصيانة السير الذاتية الاحترافية أمرًا سلسًا. سواء كنت تتقدم لوظائف تقنية أو تشارك إنجازاتك، يساعدك Awesome-CV على عرض عملك بشكل جميل وفعال.

تحقق من مستودع Awesome-CV لمزيد من التفاصيل: Awesome-CV على GitHub.