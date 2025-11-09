---
audio: false
generated: true
image: false
lang: hant
layout: post
model: mistralai/mistral-medium-3.1
title: 高效截斷 JSON 物件
translated: true
type: note
---

要從 JSON 物件（無論是陣列還是映射）中截斷前 `n` 個鍵，你可以使用以下方法。這在處理需要因應上下文限制（例如使用 LLM 生成測試案例時）而截斷的大型 JSON 回應時特別有用。

以下是一個示範如何截斷 JSON 物件前 `n` 個鍵的 Python 函數：

```python
import json

def truncate_json(json_obj, n):
    if isinstance(json_obj, list):
        # 從列表中截斷前 n 個元素
        return json_obj[n:]
    elif isinstance(json_obj, dict):
        # 從字典中截斷前 n 個鍵
        keys = list(json_obj.keys())
        for key in keys[:n]:
            del json_obj[key]
        return json_obj
    else:
        return json_obj

# 使用範例
json_str = '''
{
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}
'''

json_obj = json.loads(json_str)
n = 2  # 要截斷的鍵數量

truncated_json = truncate_json(json_obj, n)
print(json.dumps(truncated_json, indent=4))
```

### 說明

1. **函數定義**：`truncate_json` 函數接受一個 JSON 物件和整數 `n` 作為輸入。
2. **列表處理**：如果 JSON 物件是列表，則回傳移除前 `n` 個元素後的新列表。
3. **字典處理**：如果 JSON 物件是字典，則從字典中移除前 `n` 個鍵。
4. **使用範例**：此範例展示如何使用函數處理範例 JSON 物件。

### 範例輸出

對於給定的範例 JSON 物件和 `n = 2`，輸出將會是：

```json
{
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}
```

這種方法能確保 JSON 物件被適當截斷，使其更容易在 LLM 的上下文限制內處理。