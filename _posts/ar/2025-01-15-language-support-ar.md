---
audio: false
generated: false
image: false
lang: ar
layout: post
title: 'دعم اللغة: الخطوط وتحويل النص إلى كلام'
translated: true
type: post
---

مدونتي الآن تدعم تسع لغات: اليابانية (`ja`), الإسبانية (`es`), الهندية (`hi`), الصينية (`zh`), الإنجليزية (`en`), الفرنسية (`fr`), الألمانية (`de`), العربية (`ar`), والصينية التقليدية (`hant`). يمكنك العثور على الموقع على [https://lzwjava.github.io](https://lzwjava.github.io)

عند التعامل مع العديد من اللغات في بيئة حاسوب، يتطلب ذلك الانتباه إلى العديد من الجوانب.

## عملية الخطوط

تتطلب اللغات المختلفة خطوط معينة للعرض بشكل صحيح، خاصة عند إنشاء مستندات PDF باستخدام LaTeX. يوضح الكود التالي المكتوب بلغة Python كيفية اختيار الخطوط المناسبة بناءً على نظام التشغيل واللغة:

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

يجب ملاحظة أن هذه الحلولة ليست دون عيوب. على سبيل المثال، قد لا تتم معالجة النص الهندي داخل كتل التعليقات البرمجية بشكل متوقع.

## التحويل من النص إلى الكلام

أستخدم Google Text-to-Speech لإنشاء إصدارات صوتية لمحتوى مدونتي. يوضح الكود التالي كيفية اختيار الكود المناسب لللغة لوحدة التحويل من النص إلى الكلام:

```python
            synthesis_input = texttospeech.SynthesisInput(text=chunk)
            if language_code == "en-US":
                voice_name = random.choice(["en-US-Journey-D", "en-US-Journey-F", "en-US-Journey-O"])
            elif language_code == "cmn-CN":
                voice_name = random.choice(["cmn-CN-Wavenet-A", "cmn-CN-Wavenet-B", "cmn-CN-Wavenet-C", "cmn-CN-Wavenet-D"])
            elif language_code == "es-ES":
                voice_name = random.choice(["es-ES-Journey-D", "es-ES-Journey-F", "es-ES-Journey-O"])
            elif language_code == "fr-FR":
                voice_name = random.choice(["fr-FR-Journey-D", "fr-FR-Journey-F", "fr-FR-Journey-O"])
            elif language_code == "yue-HK":
                voice_name = random.choice(["yue-HK-Standard-A", "yue-HK-Standard-B", "yue-HK-Standard-C", "yue-HK-Standard-D"])
            elif language_code == "ja-JP":
                voice_name = random.choice(["ja-JP-Neural2-B", "ja-JP-Neural2-C", "ja-JP-Neural2-D"])
            elif language_code == "hi-IN":
                voice_name = random.choice(["hi-IN-Wavenet-A", "hi-IN-Wavenet-B", "hi-IN-Wavenet-C", "hi-IN-Wavenet-D", "hi-IN-Wavenet-E", "hi-IN-Wavenet-F"])
            elif language_code == "de-DE":
                voice_name = random.choice(["de-DE-Journey-D", "de-DE-Journey-F", "de-DE-Journey-O"])
            elif language_code == "ar-XA":
                voice_name = random.choice(["ar-XA-Wavenet-A", "ar-XA-Wavenet-B", "ar-XA-Wavenet-C", "ar-XA-Wavenet-D"])

            text_to_speech(
                text=article_text,
                output_filename=output_filename,
                task=task,
                language_code=language_code,
                dry_run=dry_run,
                progress=progress
            )
```

الآن، يتم إنشاء الصوت للمحتوى الصيني والإنجليزي. لتوسيع الدعم إلى اللغات الأخرى، يجب إعداد الكود المناسب لللغات المراد دعمها.

## الملخص

تختلف اللغات في دو جانبين أساسيين: تمثيلها المكتوبة (الشكل) وصوتها (اللفظ). يهدف إعدادات اختيار الخطوط والتحويل من النص إلى الكلام إلى هذين الجانبين بناءً على الترتيب.