---
audio: false
generated: true
lang: ar
layout: post
title: إعادة تعريف نمط الفقرة للوزن المتوسط
translated: true
type: note
---

لتغيير بيئة `cvparagraph` بأكملها لاستخدام `\mdseries` بدلاً من `\bodyfontlight`، تحتاج إلى إعادة تعريف الأمر `\paragraphstyle`. أضف هذا في مقدمة المستند بعد تحميل صنف awesome-cv:

```latex
\renewcommand*{\paragraphstyle}{\fontsize{11pt}{1em}\mdseries\upshape\color{text}}
```

سيؤدي هذا إلى تغيير نمط الفقرة من:
- `\bodyfontlight` (ذي الوزن الخفيف)

إلى:
- `\mdseries` (ذي الوزن المتوسط، المشابه لنمط الوصف `\descriptionstyle`)

بهذه الطريقة، ستستخدم بيئة `cvparagraph` بأكملها سلسلة الخط ذات الوزن المتوسط كما يفعل `\descriptionstyle`.