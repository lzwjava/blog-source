---
audio: false
generated: false
lang: ar
layout: post
title: 'مشكلات Markdown: Kramdown وXeLaTeX'
translated: true
---

لإنشاء ملفات PDF لمدونتي التي تعمل بـ Jekyll باستخدام Markdown، أستخدم الأمر التالي من Pandoc:

```python
command = [
    'pandoc',
    input_markdown_path,
    '-o', output_pdf_path,
    '-f', 'markdown',
    '--pdf-engine', 'xelatex',
    '--resource-path=.:assets',
    '-V', f'CJKmainfont={CJK_FONT}',
    '-V', f'CJKsansfont={CJK_FONT}',
    '-V', f'CJKmonofont={CJK_FONT}',
    '-V', f'geometry:{GEOMETRY}',
    '-V', 'classoption=16pt',
    '-V', 'CJKoptions=Scale=1.1',
    '-V', 'linestretch=1.5'
]
```

**ملاحظة:** الكود أعلاه مكتوب بلغة Python ويستخدم أداة `pandoc` لتحويل ملف Markdown إلى ملف PDF. تم الحفاظ على الكود كما هو لأنه يحتوي على أسماء أوامر وإعدادات تقنية لا تحتاج إلى ترجمة.

دعم كل من Kramdown و XeLaTeX

عند كتابة Markdown التي تحتاج إلى العمل مع kramdown (لإخراج HTML في Jekyll) وXeLaTeX (لإخراج PDF عبر Pandoc)، هناك بعض الاعتبارات التي يجب مراعاتها:

1. توافق مسار الصورة
	•	Kramdown (HTML): يفضل المسارات التي تبدأ بـ `/` للإشارة إلى الأصول.
	•	XeLaTeX (PDF): يفضل المسارات النسبية بدون `/` في البداية.

الحل: استخدم مسارات نسبية تعمل في كلا الحالتين:

```
![](assets/images/chatgpt/block.jpg)
``` 

(ملاحظة: الصور والعناصر المرئية مثل الروابط لا تحتاج إلى ترجمة، لذا تم تركها كما هي.)

2. التعامل مع سمات kramdown
	•	{:.responsive} خاص بـ kramdown لتنسيق مخرجات HTML.
	•	XeLaTeX لا يدعم هذه السمات وسيُظهر خطأ.

الحل: إزالة السمات الخاصة بـ kramdown في Markdown المخصصة لإنشاء ملفات PDF. على سبيل المثال:

```markdown
![](assets/images/chatgpt/block.jpg){: .responsive }
```

```
![](assets/images/chatgpt/block.jpg)
```

إذا كان `{:.responsive}` ضروريًا لتخطيط HTML في Jekyll، ففكر في إضافته بشكل انتقائي لإخراج الويب مع حذفه في عملية إنشاء ملف PDF.

سير العمل للتوافق المزدوج

1.	كتابة محتوى Markdown مع تقليل الاعتماد على الميزات الخاصة بـ kramdown.
2.	للتنسيق المتقدم في HTML، قم بتطبيق فئات CSS مباشرة في قوالب Jekyll بدلاً من تضمينها داخل Markdown.
3.	استخدم خيارات Pandoc للتحكم في تنسيق PDF مع الحفاظ على قابلية نقل Markdown.

باتباع هذه الممارسات، يظل محتوى Markdown متوافقًا عبر عرض HTML في Jekyll وإنشاء ملفات PDF باستخدام XeLaTeX، مما يضمن سير عمل سلس للنشر متعدد التنسيقات.