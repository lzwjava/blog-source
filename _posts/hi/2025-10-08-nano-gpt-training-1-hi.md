---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: डिफ़ॉल्ट नैनोजीपीटी प्रशिक्षण पुनरावृत्तियाँ
translated: true
type: note
---

nanoGPT की डिफ़ॉल्ट कॉन्फ़िगरेशन में (जैसे, शेक्सपियर कैरेक्टर डेटासेट पर ट्रेनिंग), मॉडल कुल **5000 इटरेशन** तक चलता है।

यह `config/train_shakespeare_char.py` फ़ाइल में `max_iters = 5000` द्वारा सेट किया गया है। आप `train.py` चलाते समय कमांड लाइन से `--max_iters=<value>` का उपयोग करके इसे ओवरराइड कर सकते हैं।

[config/train_shakespeare_char.py](https://huggingface.co/nindanaoto/nanoGPT-BitNet158b/blob/main/config/train_shakespeare_char.py)