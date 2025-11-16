---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: Python 3.13 रीजेक्स त्रुटि को ठीक करना
translated: true
type: note
---

आपके दिख रही त्रुटि का कारण **Python 3.13** का नियमित अभिव्यक्ति सिंटैक्स के प्रति पिछले संस्करणों की तुलना में अधिक सख्त होना है।

विशेष रूप से, `wikiextractor/extract.py` (लगभग लाइन 378) में यह पंक्ति अब Python 3.13 में अमान्य है:

```python
ExtLinkBracketedRegex = re.compile(
    '\\[(((?i)' + '|'.join(wgUrlProtocols) + ')' + EXT_LINK_URL_CLASS + r'+)\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\]',
    re.S | re.U)
```

समस्या स्ट्रिंग संयोजन के बाद स्ट्रिंग के बीच में रखे गए इनलाइन `(?i)` फ्लैग की है। Python 3.12/3.13 से शुरू होकर, **इनलाइन फ्लैग जैसे `(?i)` अब रेजेक्स पैटर्न की शुरुआत में ही अनुमति दी जाती है**, कहीं और नहीं।

### त्वरित सुधार (Python 3.13 पर काम करता है)

फ़ाइल को संपादित करें:

```bash
~/.local/lib/python3.13/site-packages/wikiextractor/extract.py
```

लाइन ~378 पर जाएं और टूटे हुए ब्लॉक को इस सही संस्करण से बदलें:

```python
# पुराना टूटा हुआ तरीका (Python 3.13 पर विफल)
# ExtLinkBracketedRegex = re.compile(
#     '\\[(((?i)' + '|'.join(wgUrlProtocols) + ')' + EXT_LINK_URL_CLASS + r'+)\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\]',
#     re.S | re.U)

# सही संस्करण – केस-असंवेदनशीलता फ्लैग को re.compile फ्लैग्स में ले जाएँ
protocol_pattern = '|'.join(wgUrlProtocols)
ExtLinkBracketedRegex = re.compile(
    r'\\['
    r'(((' + protocol_pattern + r')' + EXT_LINK_URL_CLASS + r'+)'
    r'\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\])',
    re.IGNORECASE | re.DOTALL | re.UNICODE
)
```

या और भी साफ-सुथरा (सुझाया गया):

```python
ExtLinkBracketedRegex = re.compile(
    r'\\['
    r'(((' + '|'.join(wgUrlProtocols) + r')' + EXT_LINK_URL_CLASS + r'+)'
    r'\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\])',
    re.I | re.S | re.U
)
```

`re.I`, `re.IGNORECASE` के समान है, और इसे पैटर्न के अंदर `(?i)` एम्बेड करने के बजाय एक फ्लैग के रूप में पास किया जा सकता है।

### वैकल्पिक समाधान

1. Python 3.11 या 3.12 का उपयोग करें (सबसे आसान अगर आप पैच नहीं करना चाहते)
   ```bash
   python3.11 -m pip install wikiextractor
   # फिर चलाएं python3.11 wikiextractor ...
   ```

2. बनाए रखे गए फोर्क का उपयोग करें जो पहले से ही Python 3.13 संगतता को ठीक कर चुका है:
   ```bash
   pip uninstall wikiextractor
   pip install git+https://github.com/attardi/wikiextractor.git
   ```

   Giuseppe Attardi के फोर्क को Python 3.12+ के लिए अपडेट किया गया है और यह 3.13 पर बिल्कुल ठीक काम करता है।

3. बहुत तेज़ आधुनिक विकल्प का उपयोग करें (बड़े डंप के लिए अत्यधिक सुझाया गया):
   ```bash
   pip install wikiextractor-ng   # या "wiki-dump-tools", "wikitextprocessor", आदि।
   ```

पैच लगाने या फिक्स्ड फोर्क पर स्विच करने के बाद, आपका कमांड फिर से काम करेगा:

```bash
wikiextractor *.bz2
```

अगर आप इसे स्वचालित रूप से ठीक करने के लिए एक-लाइनर पैच या सटीक `sed` कमांड चाहते हैं तो मुझे बताएं।