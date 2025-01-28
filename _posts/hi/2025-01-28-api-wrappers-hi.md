---
audio: true
lang: hi
layout: post
title: रैपर की जगह रॉ HTTP अनुरोध का उपयोग करें
translated: true
---

```python
import requests
import json
import time
def anuvadit_text(text, lakshya_bhasha, vishisht=False):
    if not text or not text.strip():
        return ""
    if lakshya_bhasha == 'en':
        print(f"  Anuvad ko chhod rahe hain Angrezi ke liye: {text[:50]}...")
        return text
    print(f"  Text ka anuvad kar rahe hain: {text[:50]}...")

    punarprayas = 3
    for prayas in range(punarprayas):
        try:
            pratikriya = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": create_translation_prompt(lakshya_bhasha, vishisht)},
                    {"role": "user", "content": text}
                ],
                stream=False
            )
            if not pratikriya or not pratikriya.choices or not pratikriya.choices[0].message.content:
                print(f"  Truti: Anuvad pratikriya khali ya apramanik hai: {pratikriya}")
            if pratikriya and pratikriya.choices:
                anuvadit_text = pratikriya.choices[0].message.content
                return anuvadit_text
            else:
                print(f"  Anuvad prayas {prayas + 1} par vifal raha.")
                if prayas == punarprayas - 1:
                    return None
        except Exception as e:
            print(f"  Anuvad truti ke sath vifal raha prayas {prayas + 1} par: {e}")
            if prayas == punarprayas - 1:
                return None
            time.sleep(1)  # Punarprayas karne se pehle pratiksha karein
    return None
```

Truti:

```bash
 Anuvad truti ke sath vifal raha prayas 1 par: Expecting value: line 5 column 1 (char 4)
```

Yeh truti darshaati hai ki DeepSeek API ek pratikriya lautaa raha hai jo valid JSON nahi hai, sambhavatay HTML ya kisi aur format mein. Yeh apratikshit hai, kyunki API se JSON pratikriya prapt honi chahiye. Samasya kaaran ek asthayi API samasya, dar rate limiting, yaa prompt ke sath koi samasya ho sakti hai. Isse sushobhit rup se sambhalna mahatvapurn hai, truti ko log karke aur sambhavataay punarprayas karke.