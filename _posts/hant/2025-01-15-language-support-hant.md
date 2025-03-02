---
audio: false
generated: false
lang: hant
layout: post
title: 語言支援：字體與語音轉換
translated: true
---

我的部落格現在支援九種語言：日語（`ja`）、西班牙語（`es`）、印地語（`hi`）、中文（`zh`）、英文（`en`）、法文（`fr`）、德文（`de`）、阿拉伯文（`ar`）和繁體中文（`hant`）。你可以在 [https://lzwjava.github.io](https://lzwjava.github.io) 找到這個網站。

在處理電腦環境中的多語言時，有幾個方面需要考慮。

## 字體處理

不同語言需要特定字體才能正確顯示，特別是使用 LaTeX 生成 PDF 時。以下的 Python 程式碼展示了如何根據作業系統和語言選擇適當的字體：

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

請注意，這個解決方案並不完美。例如，Hindi 文字在程式碼區塊註釋中可能無法正確顯示。

## 文字轉語音

我使用 Google 文字轉語音來生成部落格文章的音頻版本。以下的程式碼片段展示了我如何選擇適當的語言代碼以針對文字轉語音引擎：

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

目前，生成音頻的語言僅限於中文和英文。要擴展支援其他語言，必須配置相應的語言代碼。

## 總結

語言在兩個主要方面有所不同：其書寫表示（形狀）和其語音形式（發音）。字體選擇和文字轉語音配置分別處理這兩個方面。