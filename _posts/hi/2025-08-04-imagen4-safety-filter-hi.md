---
audio: false
generated: true
image: false
lang: hi
layout: post
title: ब्लॉक लो एंड अबव
translated: true
type: note
---

आप यह त्रुटि देख रहे हैं:

```
Only block_low_and_above is supported for safetySetting.
```

यह तब होता है जब आप **Imagen‑4** मॉडल्स के लिए `GenerateImagesConfig` में `safety_filter_level="BLOCK_MEDIUM_AND_ABOVE"` (या कोई अन्य मान) सेट करते हैं—लेकिन आपके अनुरोध के समय (अगस्त 2025) में, **API केवल `"BLOCK_LOW_AND_ABOVE"`** को ही इमेज सेफ्टी फ़िल्टरिंग के लिए अनुमति देता है ([Google Cloud][1])।

---

### ✅ अपने कोड को कैसे ठीक करें

बस `safety_filter_level` को सपोर्टेड वैल्यू पर अपडेट करें:

```python
from google import genai
from google.genai.types import GenerateImagesConfig

client = genai.Client()

image = client.models.generate_images(
    model="imagen-4.0-generate-preview-06-06",
    prompt="A dog reading a newspaper",
    config=GenerateImagesConfig(
        image_size="2K",
        number_of_images=1,
        safety_filter_level="BLOCK_LOW_AND_ABOVE",
        person_generation="ALLOW_ADULT",
    ),
)

image.generated_images[0].image.save("output-image.png")
print(
    f"Created image using {len(image.generated_images[0].image.image_bytes)} bytes"
)
```

* `safety_filter_level="BLOCK_LOW_AND_ABOVE"`: **Imagen 4** के लिए केवल यही सपोर्टेड है। `"BLOCK_MEDIUM_AND_ABOVE"` जैसे अन्य थ्रेशोल्ड 400 INVALID\_ARGUMENT त्रुटि का कारण बनेंगे ([Medium][2], [Google AI for Developers][3])।
* `number_of_images=1` एक्सप्लिसिट है ताकि यह स्पष्ट हो कि आप प्रति कॉल एक इमेज रिक्वेस्ट कर रहे हैं।

---

### 🧾 अन्य ऑप्शनल पैरामीटर्स:

* `person_generation="ALLOW_ADULT"` डिफ़ॉल्ट सेटिंग है, लेकिन इसे एक्सप्लिसिट रखना ठीक है (बच्चों को ब्लॉक करता है; वयस्क-डोमेन इमेजेज़ को अनुमति देता है) ([Google Cloud][1])।
* `image_size="2K"` आपके कोड के अनुसार वैलिड है—बस यह सुनिश्चित कर लें कि आपके SDK वर्जन ने इसे सपोर्ट किया है।

---

### TL;DR — क्विक चेकलिस्ट

| स्टेप | क्या करें                                                   |
| ---- | ------------------------------------------------------------ |
| ✅ 1  | safety\_filter\_level को `"BLOCK_LOW_AND_ABOVE"` में बदलें      |
| 🧾 2 | `person_generation="ALLOW_ADULT"` रखें (या डिफ़ॉल्ट के लिए छोड़ दें) |
| 🚫 3 | `"BLOCK_MEDIUM_AND_ABOVE"` या `"BLOCK_ONLY_HIGH"` का उपयोग न करें  |
| ⏱ 4  | जब तक Google और लेवल नहीं जोड़ता, सेफ्टी में फिर से बदलाव न करें      |

अगर आपको कोई अन्य त्रुटि मिलती है तो मुझे बताएं—मदद करके खुशी होगी!

[1]: https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api?utm_source=chatgpt.com "Generate images | Generative AI on Vertex AI"
[2]: https://medium.com/generative-ai/3-ways-to-try-googles-imagen-4-image-generator-if-you-re-outside-the-us-ee2a1895ca9b?utm_source=chatgpt.com "3 Ways to Try Google's Imagen 4 Image Generator if You're ..."
[3]: https://ai.google.dev/gemini-api/docs/migrate?utm_source=chatgpt.com "Migrate to the Google GenAI SDK - Gemini API"