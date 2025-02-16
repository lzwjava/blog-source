import os
import subprocess
import platform

def text_to_pdf_from_markdown(input_markdown_path, output_pdf_path, dry_run=False):
    if dry_run:
        print(f"Dry run: Would generate PDF from: {input_markdown_path}")
        return

    print(f"Generating PDF from: {input_markdown_path}")

    CJK_FONT = "Heiti SC"
    GEOMETRY = "left=1.4cm, top=.8cm, right=1.4cm, bottom=1.8cm, footskip=.5cm"

    if not os.path.exists(input_markdown_path):
        raise Exception(f"Input file does not exist: {input_markdown_path}")
    
    lang = os.path.basename(input_markdown_path).split('-')[-1].split('.')[0]
    
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

    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Pandoc error for {output_pdf_path}: {result.stderr}")
        # raise Exception(f"Pandoc failed for {input_markdown_path}")
        return False

    print(f"PDF content written to {output_pdf_path}")
    return True
