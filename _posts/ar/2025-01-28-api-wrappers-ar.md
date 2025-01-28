---
audio: true
lang: ar
layout: post
title: التفضيل باستخدام طلبات HTTP الخام بدلاً من الأدوات المساعدة
translated: true
---

```python
import requests
import json
import time
def translate_text(text, target_language, special=False):
    if not text or not text.strip():
        return ""
    if target_language == 'en':
        print(f"  تخطي الترجمة للإنجليزية: {text[:50]}...")
        return text
    print(f"  ترجمة النص: {text[:50]}...")

    retries = 3
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": create_translation_prompt(target_language, special)},
                    {"role": "user", "content": text}
                ],
                stream=False
            )
            if not response or not response.choices or not response.choices[0].message.content:
                print(f"  خطأ: الرد على الترجمة فارغ أو غير صالح: {response}")
            if response and response.choices:
                translated_text = response.choices[0].message.content
                return translated_text
            else:
                print(f"  فشلت الترجمة في المحاولة {attempt + 1}.")
                if attempt == retries - 1:
                    return None
        except Exception as e:
            print(f"  فشلت الترجمة بخطأ في المحاولة {attempt + 1}: {e}")
            if attempt == retries - 1:
                return None
            time.sleep(1)  # انتظار قبل إعادة المحاولة
    return None
```

خطأ:

```bash
 فشلت الترجمة بخطأ في المحاولة 1: Expecting value: line 5 column 1 (char 4)
```

هذا الخطأ يشير إلى أن واجهة برمجة التطبيقات DeepSeek تعيد رداً غير صالح لـ JSON، وربما يكون عبارة عن HTML أو تنسيق آخر. هذا غير متوقع، حيث يتوقع من الواجهة إرجاع JSON. قد يكون المشكلة بسبب مشكلة مؤقتة في واجهة البرمجة، أو تحديد المعدل، أو مشكلة مع المحفز. من المهم معالجة ذلك بلباقة من خلال تسجيل الخطأ وإمكانية إعادة المحاولة.