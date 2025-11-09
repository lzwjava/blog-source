---
audio: false
generated: true
image: false
lang: hi
layout: post
model: mistralai/mistral-medium-3.1
title: JSON ऑब्जेक्ट्स का कुशलता से छोटा करना
translated: true
type: note
---

JSON ऑब्जेक्ट (चाहे वह array हो या map) के पहले `n` keys को छोटा करने के लिए, आप निम्नलिखित तरीका अपना सकते हैं। यह विशेष रूप से तब उपयोगी होता है जब बड़े JSON responses को context limits के कारण छोटा करने की आवश्यकता होती है, जैसे कि test cases जनरेट करने के लिए LLM (Language Model) का उपयोग करते समय।

यहाँ एक Python फ़ंक्शन है जो दर्शाता है कि JSON ऑब्जेक्ट के पहले `n` keys को कैसे छोटा किया जाए:

```python
import json

def truncate_json(json_obj, n):
    if isinstance(json_obj, list):
        # लिस्ट से पहले n elements को छोटा करें
        return json_obj[n:]
    elif isinstance(json_obj, dict):
        # डिक्शनरी से पहले n keys को छोटा करें
        keys = list(json_obj.keys())
        for key in keys[:n]:
            del json_obj[key]
        return json_obj
    else:
        return json_obj

# उदाहरण उपयोग
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
n = 2  # छोटी करने के लिए keys की संख्या

truncated_json = truncate_json(json_obj, n)
print(json.dumps(truncated_json, indent=4))
```

### व्याख्या

1.  **फ़ंक्शन परिभाषा**: `truncate_json` फ़ंक्शन एक JSON ऑब्जेक्ट और एक integer `n` को इनपुट के रूप में लेता है।
2.  **लिस्ट हैंडलिंग**: यदि JSON ऑब्जेक्ट एक लिस्ट है, तो यह पहले `n` elements को हटाकर एक नई लिस्ट रिटर्न करता है।
3.  **डिक्शनरी हैंडलिंग**: यदि JSON ऑब्जेक्ट एक डिक्शनरी है, तो यह डिक्शनरी से पहले `n` keys को हटा देता है।
4.  **उदाहरण उपयोग**: उदाहरण दर्शाता है कि एक sample JSON ऑब्जेक्ट के साथ फ़ंक्शन का उपयोग कैसे करें।

### उदाहरण आउटपुट

दिए गए उदाहरण JSON ऑब्जेक्ट और `n = 2` के लिए, आउटपुट होगा:

```json
{
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}
```

यह तरीका सुनिश्चित करता है कि JSON ऑब्जेक्ट को उचित रूप से छोटा किया गया है, जिससे इसे LLM की context limits के भीतर संभालना आसान हो जाता है।