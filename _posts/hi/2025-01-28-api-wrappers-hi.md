---
audio: false
generated: false
image: false
lang: hi
layout: post
title: मानसिकता है कि बच्चों की सांस सुखा हो गया है, जिससे वे सो रहे हैं। यह किताब
  उन माता-पिता के लिए है जिन्होंने अपने बच्चों के साथ ऐसे प्रभाव दिखाए जाने के कारण
  चिंता महसूस कर रहे हैं।
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

समस्या:

```bash
 अनुवाद करने में त्रुटि हुई 1 की प्रयास पर: मान्यता: पंक्ति 5 कोलम 1 (चर 4)
```

यह त्रुटि दर्शाती है कि DeepSeek API एक उत्तर लौटा है जो JSON नहीं है, शायद HTML या किसी अन्य स्वरूप है। यह अनुचित है, क्योंकि API जानकारी लौटाना उम्मीद है। इस समस्या का कारण शीघ्र समय में API समस्या, दर सीमित करना, या प्रोम्प्ट से समस्या हो सकती है। इसे सुप्रसीधित हास्तकर लोग करना जरूरी है, ताकि त्रुटि लॉग की जा सके और फिर से प्रयास किया जा सके।