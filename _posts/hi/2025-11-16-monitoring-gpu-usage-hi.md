---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: nvidia-smi के साथ GPU उपयोग की निगरानी
translated: true
type: note
---

GPU उपयोग को समय के साथ `nvidia-smi` के साथ देखने के लिए, आपको केवल लूप फ्लैग की आवश्यकता है:

**बेसिक लाइव रिफ्रेश**

```
nvidia-smi -l 1
```

यह हर 1 सेकंड में अपडेट होता है। आप `1` को सेकंड में किसी भी अंतराल से बदल सकते हैं।

**यदि आप अधिक विस्तृत आँकड़े चाहते हैं (प्रति-प्रक्रिया उपयोग)**

```
nvidia-smi pmon -s um -d 1
```

यह हर सेकंड प्रति-प्रक्रिया GPU उपयोग (`u`) और मेमोरी (`m`) दिखाता है।

**यदि आप पूर्ण GPU आँकड़े बार-बार चाहते हैं**

```
nvidia-smi --query-gpu=timestamp,utilization.gpu,utilization.memory,memory.used,memory.total --format=csv -l 1
```

यह उपयोग और मेमोरी के साथ हर सेकंड एक कॉम्पैक्ट लाइन प्रिंट करता है।

मुझे बताएं यदि आप आउटपुट को एक फ़ाइल में लॉग करना चाहते हैं या कस्टम फॉर्मेट की आवश्यकता है।