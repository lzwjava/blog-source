---
audio: false
generated: true
image: false
lang: hi
layout: post
title: मेकैब कॉन्फ़िग फ़ाइल पथ ठीक करें
translated: true
type: note
---

आपकी त्रुटि

```
RuntimeError: param.cpp(70) [ifs] no such file or directory: /usr/local/etc/mecabrc
```

का मतलब है **MeCab अपनी कॉन्फ़िगरेशन फ़ाइल** (`mecabrc`) **नहीं ढूंढ पा रहा है**।
macOS पर, यदि आपने हाल ही में Homebrew के माध्यम से MeCab इंस्टॉल किया है, तो संभावना है कि यह `/usr/local/` के बजाय `/opt/homebrew/` के अंतर्गत इंस्टॉल हुआ है, लेकिन Python बाइंडिंग अभी भी पुराने `/usr/local/etc/mecabrc` पथ को ढूंढ रही है।

इसे ठीक करने का तरीका यहां बताया गया है:

---

### 1. पता लगाएं कि `mecabrc` वास्तव में कहां है

चलाएं:

```bash
brew list mecab
```

या:

```bash
find /opt/homebrew -name mecabrc
```

आपको शायद कुछ इस तरह दिखेगा:

```
/opt/homebrew/etc/mecabrc
```

---

### 2. MeCab को सही mecabrc की ओर इंगित करें

आप अपने Python कोड में पथ निर्दिष्ट कर सकते हैं:

```python
import MeCab

t = MeCab.Tagger(f"-r /opt/homebrew/etc/mecabrc -d /opt/homebrew/lib/mecab/dic/ipadic")
print(t.parse("すもももももももものうち"))
```

---

### 3. या एक environment variable सेट करें

```bash
export MECABRC=/opt/homebrew/etc/mecabrc
```

फिर अपनी स्क्रिप्ट सामान्य रूप से चलाएं:

```bash
python try_mecab.py
```

---

### 4. यदि आप `/usr/local/etc/mecabrc` को काम करना चाहते हैं

आप इसकी symlink भी बना सकते हैं:

```bash
sudo mkdir -p /usr/local/etc
sudo ln -s /opt/homebrew/etc/mecabrc /usr/local/etc/mecabrc
```

लेकिन environment variable का तरीका अधिक साफ-सुथरा है।

---

यदि आप चाहें, तो मैं आपको **Homebrew पुनः इंस्टॉल + ipadic सेटअप** कमांड भी दे सकता हूं ताकि यह हर बार `-r` निर्दिष्ट किए बिना काम करे। इस तरह आपकी `try_mecab.py` साफ रहेगी।