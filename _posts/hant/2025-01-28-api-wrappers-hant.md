---
audio: true
lang: hant
layout: post
title: 建議使用原始 HTTP 請求而非包裝器。
translated: true
---

python
import requests
import json
import time

def translate_text(text, target_language, special=False):
    if not text or not text.strip():
        return ""
    if target_language == 'en':
        print(f"  跳過英文翻譯: {text[:50]}...")
        return text
    print(f"  翻譯文本: {text[:50]}...")

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
                print(f"  錯誤: 翻譯回應為空或無效: {response}")
            if response and response.choices:
                translated_text = response.choices[0].message.content
                return translated_text
            else:
                print(f"  翻譯在第 {attempt + 1} 次嘗試失敗.")
                if attempt == retries - 1:
                    return None
        except Exception as e:
            print(f"  翻譯在第 {attempt + 1} 次嘗試失敗: {e}")
            if attempt == retries - 1:
                return None
            time.sleep(1)  # 等待後重試
    return None


錯誤:

bash
 翻譯在第 1 次嘗試失敗: Expecting value: line 5 column 1 (char 4)


此錯誤表示 DeepSeek API 返回的回應不是有效的 JSON，可能是 HTML 或其他格式。這是意外的，因為 API 應該返回 JSON。問題可能是暫時的 API 問題、速率限制或提示問題。重要的是要優雅地處理此錯誤，記錄錯誤並可能重試。