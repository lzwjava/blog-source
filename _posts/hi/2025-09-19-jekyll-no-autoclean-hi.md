---
audio: false
generated: true
image: false
lang: hi
layout: post
model: openai/gpt-5
title: जेकिल बिल्ड में ऑटो-क्लीन सुविधा का अभाव
translated: true
type: note
---

Jekyll के पास स्वयं `--replace` या `--refresh` फ्लैग नहीं है। प्रत्येक `jekyll build` रन आपके द्वारा निर्दिष्ट `--destination` फ़ोल्डर में जेनरेट की गई फ़ाइलों को लिखेगा (या ओवरराइट करेगा), लेकिन यह **पुरानी फ़ाइलों को स्वचालित रूप से नहीं हटाता है** जो अब आपके स्रोत में मौजूद नहीं हैं। इसका मतलब है कि पुरानी फाइलें वहीं रह सकती हैं।

यदि आप एक साफ build आउटपुट चाहते हैं, तो आपको `jekyll build` चलाने से पहले डेस्टिनेशन डायरेक्टरी को स्वयं साफ करना होगा। दो सामान्य तरीके हैं:

**1. अपनी स्क्रिप्ट में मैन्युअल सफाई**
`jekyll build` को कॉल करने से पहले, डेस्टिनेशन डायरेक्टरी को हटा दें:

```python
import shutil

def run_jekyll(destination: str, extra_args: list[str]) -> int:
    # पुरानी फाइलें हटाएं
    dest_path = Path(destination)
    if dest_path.exists():
        shutil.rmtree(dest_path)

    command = [
        "jekyll",
        "build",
        "--destination",
        destination,
        *extra_args,
    ]
    completed = subprocess.run(command, check=False)
    return completed.returncode
```

**2. Jekyll की अपनी `_site` डायरेक्टरी का उपयोग करें**
यदि आप Jekyll को आपके प्रोजेक्ट रूट के अंतर्गत डिफ़ॉल्ट `_site` (कस्टम `--destination` के बजाय) का उपयोग करने देते हैं, तो रीबिल्ड करने से पहले आउटपुट को साफ करने के लिए `jekyll clean` उपलब्ध है:

```bash
jekyll clean && jekyll build
```

लेकिन `jekyll clean` केवल `_site` के बारे में जानता है, किसी कस्टम फ़ोल्डर के बारे में नहीं।

---

इसलिए:

* कोई बिल्ट-इन `--replace` नहीं है।
* यदि आप कस्टम डेस्टिनेशन (जैसे आपकी स्क्रिप्ट में) का उपयोग कर रहे हैं, और आप एक ताजा आउटपुट चाहते हैं, तो बिल्ड करने से पहले आपको इसे स्पष्ट रूप से डिलीट कर देना चाहिए।

क्या आप चाहेंगे कि मैं आपकी स्क्रिप्ट को ऐडजस्ट करूं ताकि उसमें एक `--clean` विकल्प (जैसे `jekyll clean`) हो जो बिल्ड करने से पहले डेस्टिनेशन को स्वचालित रूप से साफ कर दे?