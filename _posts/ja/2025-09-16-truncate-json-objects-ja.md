---
audio: false
generated: true
image: false
lang: ja
layout: post
model: mistralai/mistral-medium-3.1
title: 効率的なJSONオブジェクトの切り詰め
translated: true
type: note
---

JSONオブジェクト（配列またはマップ）から最初の`n`個のキーを切り詰めるには、以下のアプローチを使用できます。これは、LLM（言語モデル）でテストケースを生成する際など、コンテキストの制限により大きなJSONレスポンスを切り詰める必要がある場合に特に便利です。

以下は、JSONオブジェクトから最初の`n`個のキーを切り詰めるPython関数です：

```python
import json

def truncate_json(json_obj, n):
    if isinstance(json_obj, list):
        # リストから最初のn要素を切り詰める
        return json_obj[n:]
    elif isinstance(json_obj, dict):
        # 辞書から最初のnキーを切り詰める
        keys = list(json_obj.keys())
        for key in keys[:n]:
            del json_obj[key]
        return json_obj
    else:
        return json_obj

# 使用例
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
n = 2  # 切り詰めるキーの数

truncated_json = truncate_json(json_obj, n)
print(json.dumps(truncated_json, indent=4))
```

### 説明

1. **関数定義**: `truncate_json`関数は、JSONオブジェクトと整数`n`を入力として受け取ります。
2. **リスト処理**: JSONオブジェクトがリストの場合、最初の`n`要素を削除した新しいリストを返します。
3. **辞書処理**: JSONオブジェクトが辞書の場合、辞書から最初の`n`キーを削除します。
4. **使用例**: サンプルのJSONオブジェクトを使用した関数の使用方法を示しています。

### 出力例

指定されたサンプルJSONオブジェクトと`n = 2`の場合、出力は以下のようになります：

```json
{
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}
```

このアプローチにより、JSONオブジェクトが適切に切り詰められ、LLMのコンテキスト制限内で扱いやすくなります。