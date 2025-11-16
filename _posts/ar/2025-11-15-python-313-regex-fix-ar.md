---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: إصلاح خطأ التعبير النمطي في بايثون ٣٫١٣
translated: true
type: note
---

الخطأ الذي تراه سببه أن **Python 3.13** أصبح أكثر تشددًا بشأن بناء جملة التعبيرات النمطية مقارنة بالإصدارات السابقة.

على وجه التحديد، هذا السطر في `wikiextractor/extract.py` (حوالي السطر 378) أصبح غير صالح في Python 3.13:

```python
ExtLinkBracketedRegex = re.compile(
    '\\[(((?i)' + '|'.join(wgUrlProtocols) + ')' + EXT_LINK_URL_CLASS + r'+)\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\]',
    re.S | re.U)
```

المشكلة هي علم `(?i)` المضمن الموضوع في منتصف السلسلة النصية بعد عملية التسلسل. بدءًا من Python 3.12/3.13، **لم يعد مسموحًا بالأعلام المضمنة مثل `(?i)` في أي مكان إلا في بداية نمط التعبير النمطي تمامًا**.

### الإصلاح السريع (يعمل على Python 3.13)

قم بتحرير الملف:

```bash
~/.local/lib/python3.13/site-packages/wikiextractor/extract.py
```

اذهب إلى السطر ~378 واستبدل الكتلة المعطلة بهذه النسخة المصححة:

```python
# الطريقة القديمة المعطلة (تفشل على Python 3.13)
# ExtLinkBracketedRegex = re.compile(
#     '\\[(((?i)' + '|'.join(wgUrlProtocols) + ')' + EXT_LINK_URL_CLASS + r'+)\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\]',
#     re.S | re.U)

# النسخة المصححة – انقل علم عدم التحسس للحالة إلى أعلام re.compile
protocol_pattern = '|'.join(wgUrlProtocols)
ExtLinkBracketedRegex = re.compile(
    r'\\['
    r'(((' + protocol_pattern + r')' + EXT_LINK_URL_CLASS + r'+)'
    r'\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\])',
    re.IGNORECASE | re.DOTALL | re.UNICODE
)
```

أو بشكل أنظف (موصى به):

```python
ExtLinkBracketedRegex = re.compile(
    r'\\['
    r'(((' + '|'.join(wgUrlProtocols) + r')' + EXT_LINK_URL_CLASS + r'+)'
    r'\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\])',
    re.I | re.S | re.U
)
```

`re.I` هو نفس `re.IGNORECASE`، ويمكن تمريره كعلم بدلاً من تضمين `(?i)` داخل النمط.

### الحلول البديلة

1.  استخدم Python 3.11 أو 3.12 (الأسهل إذا كنت لا تريد التصحيح)
    ```bash
    python3.11 -m pip install wikiextractor
    # ثم شغّل باستخدام python3.11 wikiextractor ...
    ```

2.  استخدم النسخة المُدارة (Fork) التي تم إصلاحها بالفعل لتتوافق مع Python 3.13:
    ```bash
    pip uninstall wikiextractor
    pip install git+https://github.com/attardi/wikiextractor.git
    ```

    نسخة Giuseppe Attardi المُدارة (Fork) تم تحديثها لتتوافق مع Python 3.12+ وتعمل بشكل مثالي على 3.13.

3.  استخدم البديل الحديث والسريع جدًا (موصى به بشدة لملفات الإلقاء (dumps) الكبيرة):
    ```bash
    pip install wikiextractor-ng   # أو "wiki-dump-tools", "wikitextprocessor"، إلخ.
    ```

بعد تطبيق التصحيح أو التبديل إلى النسخة المُدارة (Fork) المصححة، ستعمل أوامرك مرة أخرى:

```bash
wikiextractor *.bz2
```

أعلمني إذا كنت تريد أمر تصحيح من سطر واحد (one-liner) أو أمر `sed` المحدد لإصلاحه تلقائيًا.