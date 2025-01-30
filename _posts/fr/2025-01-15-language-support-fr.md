---
audio: false
lang: fr
layout: post
title: 'Prise en charge des langues : polices et synthèse vocale'
translated: true
---

Mon blog prend désormais en charge neuf langues : le japonais (`ja`), l'espagnol (`es`), l'hindi (`hi`), le chinois (`zh`), l'anglais (`en`), le français (`fr`), l'allemand (`de`), l'arabe (`ar`) et le chinois traditionnel (`hant`). Vous pouvez trouver le site à l'adresse [https://lzwjava.github.io](https://lzwjava.github.io)

Lorsque l'on traite plusieurs langues dans un environnement informatique, plusieurs aspects doivent être considérés.

## Gestion des Polices

Différentes langues nécessitent des polices spécifiques pour un rendu correct, notamment lors de la génération de PDFs à l'aide de LaTeX. Le code Python suivant montre comment sélectionner les polices appropriées en fonction du système d'exploitation et de la langue :

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

Il est important de noter que cette solution n'est pas parfaite. Par exemple, le texte en hindi à l'intérieur des blocs de commentaires de code pourrait ne pas se rendre comme prévu.

## Synthèse Vocale

J'utilise Google Text-to-Speech pour générer des versions audio de mes articles de blog. Le code suivant montre comment je sélectionne le code de langue approprié pour le moteur de synthèse vocale :

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

Actuellement, l'audio est généré pour le contenu chinois et anglais. Pour étendre la prise en charge à d'autres langues, les codes de langue correspondants doivent être configurés.

## Résumé

Les langues diffèrent principalement par deux aspects : leur représentation écrite (forme) et leur forme parlée (prononciation). La sélection des polices et les configurations de synthèse vocale répondent respectivement à ces deux aspects.