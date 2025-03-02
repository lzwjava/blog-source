---
audio: false
generated: false
lang: hi
layout: post
title: 'भाषा सहायता: फॉन्ट्स और टेक्स्ट-टू-स्पीच'
translated: true
---

मेरा ब्लॉग अब नौ भाषाओं का समर्थन करता है: जापानी (`ja`), स्पैनिश (`es`), हिन्दी (`hi`), चीनी (`zh`), इंग्लिश (`en`), फ्रांसीसी (`fr`), जर्मन (`de`), अरबी (`ar`), और प्राचीन चीनी (`hant`). आप साइट को [https://lzwjava.github.io](https://lzwjava.github.io) पर फाउन्ड सकते हैं।

कंप्यूटर परायन माध्यम में कई भाषाओं के साथ काम करने में कई विषयों को समझाना ज़रूरी है।

## फॉन्ट हैंडलिंग

अलग-अलग भाषाओं के लिए व्यावहारिक प्रदर्शन के लिए विशेष फॉन्ट्स की आवश्यकता होती है, वेना जब लाटेक्स का उपयोग करके PDFs बनाई जाती हैं। निम्नलिखित Python कोड दिखाता है कि कार्यपाद और भाषा के आधार पर उपयोगी फॉन्ट्स कैसे चयन किया जा सकता है:

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

यह समाधान पूर्णतः नहीं हुआ है। उदाहरण के लिए, कोड ब्लॉक के आकार में हिन्दी टेक्स्ट का अनुकूलन यथावत हो सकता नहीं।

## टेक्स्ट-तू-स्पीच

मैं गूगल टेक्स्ट-तू-स्पीच का उपयोग करके मेरे ब्लॉग पोस्ट्स के ऑडियो प्रतिकारों की रचना करता हूँ। निम्नलिखित कोड स्निपेट दिखाता है कि कैसे वाक्यांकन इंज़न के लिए उपयोगी भाषा कोड चयन किया जाता है:

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

वर्तमान में, चीनी और इंग्लिश संदर्भों के लिए ऑडियो बनाया जाता है। दूसरे भाषाओं के लिए समर्थन को व्यापक करने के लिए वर्तमान भाषा कोड्स को कॉन्फ़िगर किया जाना चाहिए।

## सारान्सह

भाषाएं दो प्रमुख अंगों में अलग होती हैं: उनकी लेखनीय प्रतिनिधित्व (आकार) और उनकी बाती (व्यञ्जन). फॉन्ट चयन और टेक्स्ट-तू-स्पीच कॉन्फ़िगरेशन इन दो अंगों को प्रत्येक एक साथ समझती हैं।