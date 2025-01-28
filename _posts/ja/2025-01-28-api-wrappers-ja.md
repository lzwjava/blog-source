---
audio: true
lang: ja
layout: post
title: ラッパーではなく生のHTTPリクエストを使用する
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
        print(f"  英語の翻訳をスキップ: {text[:50]}...")
        return text
    print(f"  テキストを翻訳中: {text[:50]}...")

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
                print(f"  エラー: 翻訳レスポンスが空または無効: {response}")
            if response and response.choices:
                translated_text = response.choices[0].message.content
                return translated_text
            else:
                print(f"  翻訳は試行 {attempt + 1} で失敗しました。")
                if attempt == retries - 1:
                    return None
        except Exception as e:
            print(f"  翻訳は試行 {attempt + 1} でエラーに失敗しました: {e}")
            if attempt == retries - 1:
                return None
            time.sleep(1)  # 再試行前に待機
    return None
```

エラー:

```bash
 翻訳は試行 1 でエラーに失敗しました: Expecting value: line 5 column 1 (char 4)
```

このエラーは、DeepSeek APIが有効なJSONではないレスポンスを返していることを示しています。HTMLや他の形式の可能性があります。これは予期せぬ事態です。APIはJSONを返すことが期待されています。問題は一時的なAPIの問題、レート制限、またはプロンプトの問題による可能性があります。これをスムーズに処理するために、エラーをログに記録し、再試行することが重要です。