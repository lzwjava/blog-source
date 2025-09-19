---
audio: false
generated: false
image: false
lang: hant
layout: post
title: 原始 HTTP 請求及封裝器
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
        print(f"  Skipping translation for English: {text[:50]}...")
        return text
    print(f"  Translating text: {text[:50]}...")

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
                print(f"  Error: Translation response is empty or invalid: {response}")
            if response and response.choices:
                translated_text = response.choices[0].message.content
                return translated_text
            else:
                print(f"  Translation failed on attempt {attempt + 1}.")
                if attempt == retries - 1:
                    return None
        except Exception as e:
            print(f"  Translation failed with error on attempt {attempt + 1}: {e}")
            if attempt == retries - 1:
                return None
            time.sleep(1)  # Wait before retrying
    return None
```

錯誤：

```bash
在嘗試1時發生錯誤：預期值：第5列第1列（字元4）
```

這個錯誤表示DeepSeek API返回的響應不是有效的JSON，可能是HTML或其他格式。這是預期的，API應該返回JSON。問題可能是API暫時問題、速率限制，或是提示問題。重要的是要處理這些錯誤，記錄錯誤並可能重試。