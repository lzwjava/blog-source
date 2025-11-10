---
audio: false
generated: true
image: false
lang: hi
layout: post
title: गूगल जनरेटिव एआई छवि कॉन्फ़िग
translated: true
type: note
---

यहाँ एक त्वरित अवलोकन दिया गया है: Google Gen AI (Gemini/Imagen) Python SDK में `image_size` पैरामीटर सपोर्टेड नहीं है। इसके बजाय, आप मॉडल वेरिएंट (जिनमें से प्रत्येक की अपनी अंतर्निहित डिफ़ॉल्ट रिज़ॉल्यूशन होती है) के बीच चयन करते हैं, **एस्पेक्ट रेशियो** को नियंत्रित करते हैं, और—यदि आपको अधिक पिक्सेल काउंट की आवश्यकता है—तो एक **अपस्केल** लागू करते हैं। आप **कम्प्रेशन** और **आउटपुट फॉर्मेट** के साथ-साथ सामान्य "छवियों की संख्या," "नेगेटिव प्रॉम्प्ट," "सुरक्षा" और "व्यक्ति" सेटिंग्स को भी ट्वीक कर सकते हैं।

## मॉडल वेरिएंट

आप एक मॉडल नाम चुनते हैं—प्रत्येक वेरिएंट की अपनी डिफ़ॉल्ट रिज़ॉल्यूशन और प्रदर्शन प्रोफ़ाइल होती है:

* **imagen-3.0** परिवार:

  * `imagen-3.0-generate-002`
  * `imagen-3.0-generate-001`
  * `imagen-3.0-fast-generate-001`
  * `imagen-3.0-capability-001`
* **imagen-4.0 (Preview)** परिवार:

  * `imagen-4.0-generate-preview-06-06`
  * `imagen-4.0-fast-generate-preview-06-06`
  * `imagen-4.0-ultra-generate-preview-06-06`
* **लेगेसी**: `imagegeneration@002`, `@005`, `@006` ([Google Cloud][1])

## डिफ़ॉल्ट रिज़ॉल्यूशन

डिफ़ॉल्ट रूप से, इन मॉडलों से एक वर्गाकार ("1:1") आउटपुट **1024 × 1024 पिक्सेल** का होता है। यदि आपको छोटी फ़ाइल की आवश्यकता है, तो आप स्थानीय रूप से डाउनसैंपल कर सकते हैं; यदि आपको उच्च रिज़ॉल्यूशन की आवश्यकता है, तो नीचे **अपस्केलिंग** देखें। ([raymondcamden.com][2])

## एस्पेक्ट रेशियो

निरपेक्ष आयाम निर्दिष्ट करने के बजाय, अपने `GenerateImagesConfig` में `aspect_ratio` फ़ील्ड का उपयोग करें। समर्थित मान:

* `1:1` (वर्ग)
* `3:4` (लंबा, सोशल-मीडिया पोर्ट्रेट)
* `4:3` (क्लासिक फोटोग्राफी/TV)
* `16:9` (वाइडस्क्रीन लैंडस्केप)
* `9:16` (लंबा/पोर्ट्रेट, उदा. फोन बैकग्राउंड) ([Google Cloud][1], [Google AI for Developers][3])

आपको यही सूची समुदाय ट्यूटोरियल्स में दस्तावेज़ की गई मिलेगी:

* DataCamp, Imagen 3 के लिए ठीक इन्हीं पाँच अनुपातों की ओर इशारा करता है ([DataCamp][4])
* CodeSignal का गाइड भी Gemini/Imagen के लिए इनकी सूची देता है ([CodeSignal][5])

## अपस्केलिंग

यदि आपको वास्तविक "2K" या "4K" आउटपुट की आवश्यकता है, तो **अपस्केल** मोड को कॉल करें:

```python
from google.genai import types
config = types.GenerateImagesConfig(
    mode="upscale",
    upscale_config=types.UpscaleConfig(upscale_factor="x2"),
)
```

* `"x2"` प्रत्येक आयाम को दोगुना कर देता है (उदा. 1024 → 2048, लगभग 2K)
* `"x4"` चौगुना कर देता है (उदा. 1024 → 4096, लगभग 4K) ([Google Cloud][1])

## कम्प्रेशन और फॉर्मेट

* **JPEG क्वालिटी**: फ़ाइल आकार बनाम विस्तार के बीच ट्रेड-ऑफ़ के लिए `compression_quality` (0–100, डिफ़ॉल्ट 75) का उपयोग करें ([Google Cloud][1])
* **MIME प्रकार**: `output_options.mime_type` के माध्यम से, आप चुन सकते हैं
  `image/jpeg`, `image/png`, `image/gif`, `image/webp`, `image/bmp`, `image/tiff`, या `image/vnd.microsoft.icon` ([Google Cloud][6])

## अतिरिक्त कॉन्फ़िग विकल्प

बाकी सब कुछ `GenerateImagesConfig` में होता है:

```python
config = types.GenerateImagesConfig(
    number_of_images=1,           # कितनी छवियाँ जनरेट करनी हैं
    seed=1234,                    # निर्धारक आउटपुट के लिए
    enhance_prompt=True,          # LLM-आधारित प्रॉम्प्ट रिराइटिंग
    negative_prompt="exclude dogs",
    language="en",
    safety_filter_level="block_medium_and_above",  
    person_generation="allow_adult",
)
```

ये आपको यादृच्छिकता, प्रॉम्प्ट एन्हांसमेंट, सुरक्षा सीमा और इस बात को नियंत्रित करने देते हैं कि क्या मॉडल लोगों को शामिल कर सकता है। ([Google Cloud][1])

## सिफारिश

अपनी `image_size="2K"` लाइन को हटा दें—ऐसा कोई फ्लैग मौजूद नहीं है। इसके बजाय:

1. गति बनाम गुणवत्ता के लिए **सही मॉडल चुनें**।
2. फ़्रेमिंग के लिए **`aspect_ratio`** का उपयोग करें।
3. यदि आपको वास्तव में अधिक पिक्सेल काउंट की आवश्यकता है, तो बेस रिज़ॉल्यूशन पर जनरेट करें फिर बिल्ट-इन **अपस्केल** ("x2" या "x4") लागू करें।
4. छोटी फ़ाइलों के लिए **`compression_quality`** को ट्वीक करें या स्थानीय रूप से डाउनसैंपल करें।

इन नॉब्स के साथ, आप एक असमर्थित `image_size` पैरामीटर के बिना, वर्गाकार या सिनेमाई फ़्रेमिंग, छोटे या उच्च-रिज़ॉल्यूशन आउटपुट प्राप्त कर सकते हैं।

[1]: https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api "Generate images  |  Generative AI on Vertex AI  |  Google Cloud"
[2]: https://www.raymondcamden.com/2025/01/30/generative-ai-images-with-gemini-and-imagen-an-introduction?utm_source=chatgpt.com "Generative AI Images with Gemini and Imagen"
[3]: https://ai.google.dev/gemini-api/docs/imagen?utm_source=chatgpt.com "Generate images using Imagen | Gemini API | Google AI for ..."
[4]: https://www.datacamp.com/tutorial/imagen-3 "Imagen 3: A Guide With Examples in the Gemini API | DataCamp"
[5]: https://codesignal.com/learn/courses/creating-images-with-geminis-imagen-and-flask/lessons/generating-a-simple-image-with-geminis-imagen-and-flask?utm_source=chatgpt.com "Generating a Simple Image with Gemini's Imagen and Flask"
[6]: https://cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images?utm_source=chatgpt.com "Generate images using text prompts"