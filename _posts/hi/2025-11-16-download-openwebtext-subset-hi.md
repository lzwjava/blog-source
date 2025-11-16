---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: हगिंग फेस के माध्यम से ओपनवेबटेक्स्ट सबसेट डाउनलोड करना
translated: true
type: note
---

आप जिस डेटासेट की बात कर रहे हैं, वह Hugging Face पर `Skylion007/openwebtext` रेपो आईडी के तहत होस्ट किया गया है। विशिष्ट फ़ाइल `subsets/urlsf_subset00.tar` सार्वजनिक रूप से एक्सेसिबल है (किसी ऑथ की आवश्यकता नहीं है), इसलिए आप इसे Hugging Face CLI टूल (`huggingface-cli`) का उपयोग करके डाउनलोड कर सकते हैं। यहां बताया गया है कैसे:

### पूर्वापेक्षाएँ
- Hugging Face Hub CLI इंस्टॉल करें, अगर आपने पहले से नहीं किया है:
  ```
  pip install huggingface_hub
  ```
- (वैकल्पिक) यदि आपके पास `huggingface-cli` कमांड `hf` के रूप में एलियास्ड है (कुछ सिस्टम पर आम), तो आप उस शॉर्टहैंड का उपयोग कर सकते हैं। अन्यथा, पूर्ण `huggingface-cli` उपसर्ग का उपयोग करें।

### डाउनलोड कमांड
अपने टर्मिनल में यह चलाएं:
```
huggingface-cli download Skylion007/openwebtext subsets/urlsf_subset00.tar --local-dir ./openwebtext
```
- यह फ़ाइल को `./openwebtext/subsets/urlsf_subset00.tar` पर डाउनलोड कर देगा (आवश्यकता पड़ने पर `subsets` सबडिरेक्टरी बनाते हुए)।
- फ़ाइल काफी बड़ी है (~1.5 GB अनकंप्रेस्ड, लेकिन यह एक टारबॉल है), इसलिए सुनिश्चित करें कि आपके पास पर्याप्त डिस्क स्थान और एक स्थिर कनेक्शन है।
- यदि आप इसे रेपो संरचना के बिना डाउनलोड करना चाहते हैं (सीधे वर्तमान डिरेक्टरी में), `--repo-type dataset` जोड़ें (हालाँकि यहाँ यह निहित है) या `--local-dir` को एडजस्ट करें।

### Python का उपयोग करना (विकल्प)
यदि आप इसे Python में स्क्रिप्ट करना पसंद करते हैं (उदाहरण के लिए, `huggingface_hub` लाइब्रेरी के माध्यम से):
```python
from huggingface_hub import hf_hub_download

# वर्तमान डिरेक्टरी में डाउनलोड करें
hf_hub_download(
    repo_id="Skylion007/openwebtext",
    filename="subsets/urlsf_subset00.tar",
    local_dir="./openwebtext",  # वैकल्पिक: बेस डिरेक्टरी निर्दिष्ट करता है
    repo_type="dataset"
)
```
पहले लाइब्रेरी इंस्टॉल करें: `pip install huggingface_hub`.

### नोट्स
- यह OpenWebText (एक बड़ा वेब कॉर्पस) का एक सबसेट है। डाउनलोड करने के बाद, आपको `.tar` फ़ाइल को एक्सट्रैक्ट करने की आवश्यकता होगी (उदाहरण के लिए, `tar -xvf subsets/urlsf_subset00.tar`)।
- यदि डाउनलोड विफल हो जाता है (उदाहरण के लिए, नेटवर्क समस्याओं के कारण), पुनः प्रयास करें या कस्टम कैश लोकेशन निर्दिष्ट करने के लिए `--cache-dir` का उपयोग करें।
- पूर्ण डेटासेट या अन्य सबसेट्स के लिए, रेपो पेज चेक करें: https://huggingface.co/datasets/Skylion007/openwebtext.

यदि आपको कोई त्रुटियाँ आती हैं, तो डीबगिंग के लिए आउटपुट साझा करें!