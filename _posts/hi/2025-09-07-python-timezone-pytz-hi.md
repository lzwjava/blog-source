---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-code-fast-1
title: पायथन टाइमज़ोन हैंडलिंग पीवाईटीज़ेड के साथ
translated: true
type: note
---

### pytz इंस्टॉल करना
pytz टाइमज़ोन-अवेयर डेटटाइम ऑब्जेक्ट्स को हैंडल करने के लिए एक तृतीय-पक्ष Python लाइब्रेरी है। ध्यान दें कि Python 3.9+ से, नए कोड के लिए बिल्ट-इन `zoneinfo` मॉड्यूल को प्राथमिकता दी जाती है (यह स्टैंडर्ड लाइब्रेरी में है और अपडेट्स को स्वचालित रूप से संभालता है), लेकिन pytz अभी भी व्यापक रूप से उपयोग किया जाता है।

pytz को इंस्टॉल करने के लिए, pip का उपयोग करें:
```
pip install pytz
```

### pytz के साथ बेसिक उपयोग
pytz Python के `datetime` मॉड्यूल के साथ काम करता है। मुख्य अवधारणाएँ:
- **टाइमज़ोन ऑब्जेक्ट्स**: टाइमज़ोन-अवेयर ऑब्जेक्ट बनाने के लिए `pytz.timezone()` का उपयोग करें (जैसे, "UTC" या "America/New_York" के लिए)।
- **लोकलाइज़ेशन**: एक naive `datetime` ऑब्जेक्ट से टाइमज़ोन जोड़ने के लिए `.localize()` का उपयोग करें।
- **कन्वर्जन**: टाइमज़ोन के बीच कन्वर्ट करने के लिए `.astimezone()` का उपयोग करें।
- **पिटफॉल**: डेलाइट सेविंग टाइम (DST) को सही ढंग से हैंडल करने के लिए सीधे `datetime` ऑब्जेक्ट्स पर `pytz` कंस्ट्रक्टर्स का उपयोग करने से बचें; हमेशा पहले लोकलाइज़ करें।

आवश्यक मॉड्यूल इम्पोर्ट करें:
```python
import datetime
import pytz
```

### उदाहरण

#### 1. किसी विशिष्ट टाइमज़ोन में वर्तमान समय प्राप्त करें
`pytz.utc` या विशिष्ट टाइमज़ोन का उपयोग करें। बेस्ट प्रैक्टिसेस के लिए हमेशा आंतरिक रूप से UTC के साथ काम करें।

```python
# वर्तमान UTC समय प्राप्त करें
utc_now = datetime.datetime.now(pytz.utc)
print(utc_now)  # उदा., 2023-10-15 14:30:00+00:00

# US Eastern टाइम में वर्तमान समय प्राप्त करें
eastern = pytz.timezone('US/Eastern')
eastern_now = datetime.datetime.now(eastern)
print(eastern_now)  # उदा., 2023-10-15 10:30:00-04:00 (DST के लिए एडजस्ट करता है)
```

#### 2. एक Naive डेटटाइम को लोकलाइज़ करना
एक naive (टाइमज़ोन-अनजान) डेटटाइम को टाइमज़ोन-अवेयर में बदलें।

```python
# एक naive डेटटाइम बनाएँ (उदा., 15 अक्टूबर, 2023, 12:00)
naive_dt = datetime.datetime(2023, 10, 15, 12, 0)
print(naive_dt)  # 2023-10-15 12:00:00

# US Eastern टाइम में लोकलाइज़ करें
eastern = pytz.timezone('US/Eastern')
aware_dt = eastern.localize(naive_dt)
print(aware_dt)  # 2023-10-15 12:00:00-04:00
```

#### 3. टाइमज़ोन के बीच कन्वर्ट करना
पहले एक डेटटाइम को लोकलाइज़ करें, फिर कन्वर्ट करें।

```python
# UTC समय से शुरू करें
utc_dt = pytz.utc.localize(datetime.datetime(2023, 10, 15, 14, 0))
print(utc_dt)  # 2023-10-15 14:00:00+00:00

# Pacific टाइम में कन्वर्ट करें
pacific = pytz.timezone('US/Pacific')
pacific_dt = utc_dt.astimezone(pacific)
print(pacific_dt)  # 2023-10-15 07:00:00-07:00
```

#### 4. टाइमज़ोन की सूची को हैंडल करना
pytz ओल्सन डेटाबेस से सामान्य टाइमज़ोन नामों को सपोर्ट करता है।

```python
# उपलब्ध टाइमज़ोन की सूची दें
print(pytz.all_timezones[:10])  # नमूना: ['Africa/Abidjan', 'Africa/Accra', ...]

# या देश-विशिष्ट
print(pytz.country_timezones['US'])  # ['America/New_York', 'America/Los_Angeles', ...]
```

### zoneinfo में माइग्रेशन (Python 3.9+ के लिए रिकमंडेड)
नए Python वर्जन के लिए, सरलता के लिए pytz के बजाय बिल्ट-इन `zoneinfo` का उपयोग करें:
```python
from zoneinfo import ZoneInfo
import datetime

# pytz उदाहरणों के समकक्ष
eastern_now = datetime.datetime.now(ZoneInfo('US/Eastern'))
aware_dt = datetime.datetime(2023, 10, 15, 12, 0).replace(tzinfo=ZoneInfo('US/Eastern'))
```

### सामान्य समस्याएं और टिप्स
- **अस्पष्ट समय**: DST ट्रांज़िशन के दौरान, `.localize()` में `is_dst` का उपयोग करें (उदा., `eastern.localize(naive_dt, is_dst=False)`)।
- **UTC नॉर्मलाइज़ेशन**: एरर से बचने के लिए अंकगणित से पहले UTC में कन्वर्ट करें।
- **pytz अपडेट करें**: यह IANA tzdata का उपयोग करता है; इसे pip के माध्यम से अपडेटेड रखें।
- अधिक जानकारी के लिए, [pytz डॉक्यूमेंटेशन](https://pythonhosted.org/pytz/) देखें। यदि आपको एरर आते हैं, तो डीबगिंग सहायता के लिए कोड स्निपेट पेस्ट करें।