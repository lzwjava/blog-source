---
audio: true
lang: hant
layout: post
title: 語言支援：字體及語音轉文字
translated: true
---

我的博客現已支援九種語言：日語（`ja`）、西班牙語（`es`）、印地語（`hi`）、中文（`zh`）、英語（`en`）、法語（`fr`）、德語（`de`）、阿拉伯語（`ar`）和繁體中文（`hant`）。你可以在[https://lzwjava.github.io](https://lzwjava.github.io)找到網站。

在電腦環境中處理多種語言時，需要考慮幾個方面。

## 字體處理

不同語言需要特定字體才能正確渲染，特別是使用LaTeX生成PDF時。以下Python代碼示範了如何根據操作系統和語言選擇合適的字體：

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


需要注意的是，這個解決方案並不完美。例如，代碼塊註釋中的印地文文本可能無法按預期渲染。

## 語音合成

我使用Google語音合成來生成博客文章的音頻版本。以下代碼片段展示了我如何為語音合成引擎選擇合適的語言代碼：

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


目前，音頻僅針對中文和英文內容生成。要擴展對其他語言的支援，必須配置相應的語言代碼。

## 總結

語言在兩個主要方面有所不同：書寫表示（形狀）和語音形式（發音）。字體選擇和語音合成配置分別解決了這兩個方面的問題。