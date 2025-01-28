---
audio: true
lang: zh
layout: post
title: 使用原始 HTTP 请求而不是封装库
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
        print(f"  跳过翻译英文: {text[:50]}...")
        return text
    print(f"  翻译文本: {text[:50]}...")

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
                print(f"  错误: 翻译响应为空或无效: {response}")
            if response and response.choices:
                translated_text = response.choices[0].message.content
                return translated_text
            else:
                print(f"  翻译在尝试 {attempt + 1} 失败。")
                if attempt == retries - 1:
                    return None
        except Exception as e:
            print(f"  翻译在尝试 {attempt + 1} 时出错: {e}")
            if attempt == retries - 1:
                return None
            time.sleep(1)  # 等待后重试
    return None
```

错误:

```bash
 翻译在尝试 1 时出错: 预期值: 第5行第1列 (字符4)
```

此错误表明 DeepSeek API 返回的响应不是有效的 JSON，可能是 HTML 或其他格式。这是意外的，因为 API 预计返回 JSON。问题可能是由于 API 的临时问题、速率限制或提示的问题。重要的是要优雅地处理此错误，记录错误并可能重试。