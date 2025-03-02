---
audio: false
generated: false
lang: ja
layout: post
title: HTTP リクエストとラッパー
translated: true
---

```python
import requests
import json
import time

def 翻訳_テキスト(テキスト, ターゲット言語, special=False):
    if not テキスト or not テキスト.strip():
        return ""
    if ターゲット言語 == 'en':
        print(f"  English translation skipped: {テキスト[:50]}...")
        return テキスト
    print(f"  Translating text: {テキスト[:50]}...")

    retries = 3
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": create_translation_prompt(ターゲット言語, special)},
                    {"role": "user", "content": テキスト}
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

エラー:

```bash
 Translation failed with error on attempt 1: 期待される値がありません: 行 5 列 1 (char 4)
```

このエラーは、DeepSeek APIが有効なJSONではなくHTMLやその他の形式の応答を返していることを示しています。これは予期しないですが、APIが一時的な問題やレート制限の対象となっているか、プロンプトの問題が原因です。これを適切に処理するためには、エラーをログに記録し、必要に応じて再試行することが重要です。