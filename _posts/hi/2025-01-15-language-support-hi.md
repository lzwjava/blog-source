---
audio: true
lang: hi
layout: post
title: 'भाषा समर्थन: फ़ॉन्ट और टेक्स्ट-टू-स्पीच'
translated: true
---

मेरा ब्लॉग अब नौ भाषाओं का समर्थन करता है: जापानी (`ja`), स्पैनिश (`es`), हिंदी (`hi`), चीनी (`zh`), अंग्रेजी (`en`), फ्रेंच (`fr`), जर्मन (`de`), अरबी (`ar`), और पारंपरिक चीनी (`hant`). आप साइट को यहां पा सकते हैं [https://lzwjava.github.io](https://lzwjava.github.io)

कंप्यूटर वातावरण में कई भाषाओं से निपटने में कई पहलुओं को ध्यान में रखना होगा।

## फॉन्ट हैंडलिंग

विभिन्न भाषाओं के लिए सही प्रतिपादन के लिए विशिष्ट फॉन्ट की आवश्यकता होती है, 特करीबन जब LaTeX का उपयोग करते हुए PDF बना रहे हों। निम्नलिखित Python कोड दिखाता है कि ऑपरेटिंग सिस्टम और भाषा के आधार पर उपयुक्त फॉन्ट कैसे चुनें:

python
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


यह ध्यान रखना महत्वपूर्ण है कि यह समाधान पूर्ण नहीं है। उदाहरण के लिए, कोड ब्लॉक टिप्पणियों में हिंदी पाठ अपेक्षित तरीके से प्रतिपादित नहीं हो सकता।

## टेक्स्ट-टू-स्पीच

मैं Google टेक्स्ट-टू-स्पीच का उपयोग करता हूं अपने ब्लॉग पोस्ट के ऑडियो संस्करण बनाने के लिए। निम्नलिखित कोड स्निपेट दिखाता है कि मैं टेक्स्ट-टू-स्पीच इंजन के लिए उपयुक्त भाषा कोड कैसे चुनता हूं:

python
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


वर्तमान में, ऑडियो चीनी और अंग्रेजी सामग्री के लिए बनाया जाता है। अन्य भाषाओं के लिए समर्थन बढ़ाने के लिए, संबंधित भाषा कोड को कॉन्फ़िगर किया जाना चाहिए।

## सारांश

भाषाएँ अपने लिखित प्रतिनिधित्व (आकार) और बोली जाने वाली रूप (उच्चारण) में अलग होती हैं। फॉन्ट चयन और टेक्स्ट-टू-स्पीच कॉन्फ़िगरेशन इन दो पहलुओं को क्रमशः संबोधित करते हैं।