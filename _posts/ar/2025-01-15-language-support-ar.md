---
audio: false
lang: ar
layout: post
title: 'دعم اللغة: الخطوط وتحويل النص إلى كلام'
translated: true
---

تدعم مدونتي الآن تسع لغات: اليابانية (`ja`)، الإسبانية (`es`)، الهندية (`hi`)، الصينية (`zh`)، الإنجليزية (`en`)، الفرنسية (`fr`)، الألمانية (`de`)، العربية (`ar`)، والصينية التقليدية (`hant`). يمكنك زيارة الموقع على الرابط التالي: [https://lzwjava.github.io](https://lzwjava.github.io)

عند التعامل مع لغات متعددة في بيئة حاسوبية، هناك عدة جوانب تحتاج إلى الاهتمام.

## التعامل مع الخطوط

تتطلب اللغات المختلفة خطوطًا محددة لعرض النص بشكل صحيح، خاصة عند إنشاء ملفات PDF باستخدام LaTeX. يوضح كود Python التالي كيفية اختيار الخطوط المناسبة بناءً على نظام التشغيل واللغة:

```python
    if platform.system() == "Darwin":
        if lang == "hi":
            CJK_FONT = "Kohinoor Devanagari"
        elif lang == "ar":
            CJK_FONT = "Geeza Pro"
        elif lang in ["en", "fr", "de", "es"]:
            CJK_FONT = "Helvetica"
        elif lang == "zh":
            CJK_FONT = "PingFang SC"
        elif lang == "hant":
            CJK_FONT = "PingFang TC"
        elif lang == "ja":
            CJK_FONT = "Hiragino Sans"
        else:
            CJK_FONT = "Arial Unicode MS"
    else:
        if lang == "hi":
            CJK_FONT = "Noto Sans Devanagari"
        elif lang == "ar":
            CJK_FONT = "Noto Naskh Arabic"
        elif lang in ["en", "fr", "de", "es"]:
            CJK_FONT = "DejaVu Sans"
        elif lang == "zh":
            CJK_FONT = "Noto Sans CJK SC"
        elif lang == "hant":
            CJK_FONT = "Noto Sans CJK TC"
        elif lang == "ja":
            CJK_FONT = "Noto Sans CJK JP"
        else:
            CJK_FONT = "Noto Sans"
    command = [
        'pandoc',
        input_markdown_path,
        '-o', output_pdf_path,
        '-f', 'markdown',
        '--pdf-engine', 'xelatex',
        '-V', f'romanfont={CJK_FONT}',
        '-V', f'mainfont={CJK_FONT}',
        '-V', f'CJKmainfont={CJK_FONT}',
        '-V', f'CJKsansfont={CJK_FONT}',
        '-V', f'CJKmonofont={CJK_FONT}',
        '-V', f'geometry:{GEOMETRY}',
        '-V', 'classoption=16pt',
        '-V', 'CJKoptions=Scale=1.1',
        '-V', 'linestretch=1.5'
    ]
```

من المهم ملاحظة أن هذا الحل ليس مثاليًا. على سبيل المثال، قد لا يتم عرض النص الهندي داخل تعليقات كتل الكود كما هو متوقع.

## تحويل النص إلى كلام

أستخدم خدمة Google Text-to-Speech لإنشاء نسخ صوتية من مقالاتي. يوضح مقتطف الكود التالي كيفية اختيار رمز اللغة المناسب لمحرك تحويل النص إلى كلام:

```python
            if filename.endswith('-zh.md'):
                language_code = "cmn-CN"
                voice_language_code = "cmn-CN"
            else:
                language_code = "en-US"
                voice_language_code = "en-US"
            
            text_to_speech(
                text=article_text, 
                output_filename=output_filename, 
                task=task, 
                language_code=language_code, 
                dry_run=dry_run,
                progress=progress
            )
```

حاليًا، يتم إنشاء الصوت للمحتوى الصيني والإنجليزي. لدعم لغات أخرى، يجب تكوين رموز اللغات المقابلة.