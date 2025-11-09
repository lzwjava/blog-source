---
audio: false
generated: true
image: false
lang: ar
layout: post
model: mistralai/mistral-medium-3.1
title: تقليم كائنات JSON بكفاءة
translated: true
type: note
---

لاقتطاع أول `n` مفاتيح من كائن JSON (سواء كان مصفوفة أو خريطة)، يمكنك استخدام النهج التالي. هذا مفيد بشكل خاص عند التعامل مع استجابات JSON كبيرة التي تحتاج إلى اقتطاع بسبب حدود السياق، مثل عند استخدام نموذج لغوي (LLM) لتوليد حالات اختبار.

إليك دالة Python توضح كيفية اقتطاع أول `n` مفاتيح من كائن JSON:

```python
import json

def truncate_json(json_obj, n):
    if isinstance(json_obj, list):
        # اقتطاع أول n عنصر من القائمة
        return json_obj[n:]
    elif isinstance(json_obj, dict):
        # اقتطاع أول n مفتاح من القاموس
        keys = list(json_obj.keys())
        for key in keys[:n]:
            del json_obj[key]
        return json_obj
    else:
        return json_obj

# مثال على الاستخدام
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
n = 2  # عدد المفاتيح المراد اقتطاعها

truncated_json = truncate_json(json_obj, n)
print(json.dumps(truncated_json, indent=4))
```

### الشرح

1. **تعريف الدالة**: تأخذ دالة `truncate_json` كائن JSON وعدد صحيح `n` كمدخلات.
2. **معالجة المصفوفات**: إذا كان كائن JSON عبارة عن قائمة، فإنها ترجع قائمة جديدة بعد إزالة أول `n` عناصر.
3. **معالجة القواميس**: إذا كان كائن JSON عبارة عن قاموس، فإنها تزيل أول `n` مفاتيح من القاموس.
4. **مثال على الاستخدام**: يوضح المثال كيفية استخدام الدالة مع كائن JSON نموذجي.

### مثال على الناتج

لكائن JSON المحدد في المثال و `n = 2`، سيكون الناتج:

```json
{
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}
```

هذا النهج يضمن اقتطاع كائن JSON بشكل مناسب، مما يسهل التعامل معه ضمن حدود سياق نموذج لغوي (LLM).