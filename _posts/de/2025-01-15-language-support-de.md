---
audio: false
generated: false
lang: de
layout: post
title: 'Unterstützte Sprachen: Schriftarten und Text-zu-Sprache'
translated: true
---

Mein Blog unterstützt nun neun Sprachen: Japanisch (`ja`), Spanisch (`es`), Hindi (`hi`), Chinesisch (`zh`), Englisch (`en`), Französisch (`fr`), Deutsch (`de`), Arabisch (`ar`) und Traditionelles Chinesisch (`hant`). Die Website finden Sie unter [https://lzwjava.github.io](https://lzwjava.github.io)

Beim Umgang mit mehreren Sprachen in einer Computerumgebung müssen mehrere Aspekte berücksichtigt werden.

## Schriftartenverwaltung

Verschiedene Sprachen erfordern spezifische Schriftarten für die korrekte Darstellung, insbesondere beim Erstellen von PDFs mit LaTeX. Der folgende Python-Code zeigt, wie geeignete Schriftarten basierend auf dem Betriebssystem und der Sprache ausgewählt werden:

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

Es ist wichtig zu beachten, dass diese Lösung nicht perfekt ist. Beispielsweise könnte Hindi-Text innerhalb von Codeblock-Kommentaren nicht wie erwartet gerendert werden.

## Text-zu-Sprache

Ich nutze Google Text-to-Speech, um Audioversionen meiner Blogbeiträge zu erstellen. Der folgende Codeausschnitt zeigt, wie ich den geeigneten Sprachcode für die Text-to-Speech-Engine auswähle:

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

Derzeit wird Audio für chinesische und englische Inhalte erzeugt. Um die Unterstützung für andere Sprachen zu erweitern, müssen die entsprechenden Sprachcodes konfiguriert werden.

## Zusammenfassung

Sprachen unterscheiden sich in zwei Hauptaspekten: ihrer geschriebenen Darstellung (Form) und ihrer gesprochenen Form (Aussprache). Die Schriftartenauswahl und die Text-to-Speech-Konfigurationen adressieren diese beiden Aspekte entsprechend.