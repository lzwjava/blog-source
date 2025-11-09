---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-code-fast-1
title: पायथन डेटटाइम मॉड्यूल का अवलोकन
translated: true
type: note
---

### Python के datetime मॉड्यूल का अवलोकन

Python का `datetime` मॉड्यूल तारीखों, समय और टाइमस्टैम्प्स को संभालने के लिए कक्षाएं प्रदान करता है। यह स्टैंडर्ड लाइब्रेरी में है, इसलिए इंस्टॉलेशन की आवश्यकता नहीं है। प्रमुख कक्षाओं में शामिल हैं:
- `date`: तारीखों (वर्ष, महीना, दिन) को संभालता है।
- `time`: समय (घंटा, मिनट, सेकंड, माइक्रोसेकंड) को संभालता है।
- `datetime`: तारीख और समय को जोड़ता है।
- `timedelta`: एक अवधि का प्रतिनिधित्व करता है (जैसे, तारीख अंकगणित के लिए)।

यह लॉगिंग टाइमस्टैम्प्स, अवधि की गणना, या डिस्प्ले/आउटपुट के लिए तारीखों को फॉर्मेट करने जैसे कार्यों के लिए उपयोगी है।

### मॉड्यूल को इम्पोर्ट करना

आवश्यकतानुसार पूरे मॉड्यूल या विशिष्ट कक्षाओं को इम्पोर्ट करें:

```python
import datetime  # पूरा मॉड्यूल

# या विशिष्ट कक्षाओं को इम्पोर्ट करें
from datetime import datetime, date, time, timedelta
```

### वर्तमान तारीख और समय प्राप्त करना

वर्तमान स्थानीय तारीख और समय को एक `datetime` ऑब्जेक्ट के रूप में प्राप्त करने के लिए `datetime.now()` का उपयोग करें।

```python
import datetime

now = datetime.datetime.now()
print(now)  # आउटपुट: उदाहरण, 2023-10-05 14:30:45.123456
print(type(now))  # <class 'datetime.datetime'>
```

UTC समय के लिए, `datetime.utcnow()` का उपयोग करें (हालांकि टाइमज़ोन जागरूकता के लिए `datetime.timezone` से इम्पोर्ट के साथ `datetime.now(timezone.utc)` का उपयोग करना बेहतर है)।

### तारीख और समय ऑब्जेक्ट बनाना

उनके कंस्ट्रक्टर के साथ मैन्युअल रूप से ऑब्जेक्ट बनाएं।

```python
# तारीख: वर्ष, महीना, दिन
d = datetime.date(2023, 10, 5)
print(d)  # 2023-10-05

# समय: घंटा, मिनट, सेकंड, माइक्रोसेकंड (वैकल्पिक)
t = datetime.time(14, 30, 45)
print(t)  # 14:30:45

# डेटाटाइम: तारीख और समय को जोड़ता है
dt = datetime.datetime(2023, 10, 5, 14, 30, 45)
print(dt)  # 2023-10-05 14:30:45
```

जिन भागों की आवश्यकता नहीं है उन्हें छोड़ दें (उदाहरण के लिए, `datetime.datetime(2023, 10, 5)` आधी रात का एक डेटाटाइम बनाता है)।

### तारीखों को फॉर्मेट करना (strftime)

फॉर्मेट कोड (जैसे, वर्ष के लिए `%Y`, महीने के लिए `%m`) के साथ `strftime` का उपयोग करके तारीखों को स्ट्रिंग में बदलें।

```python
now = datetime.datetime.now()
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)  # उदाहरण, 2023-10-05 14:30:45

# सामान्य फॉर्मेट:
# %A: पूरा वीकडे (जैसे, Thursday)
# %B: पूरा महीना (जैसे, October)
# %Y-%m-%d: ISO तारीख
```

### स्ट्रिंग्स से तारीखों को पार्स करना (strptime)

मिलान फॉर्मेट के साथ `strptime` का उपयोग करके स्ट्रिंग्स को `datetime` ऑब्जेक्ट में बदलें।

```python
date_str = "2023-10-05 14:30:45"
parsed = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(parsed)  # 2023-10-05 14:30:45
print(type(parsed))  # <class 'datetime.datetime'>
```

फॉर्मेट को बिल्कुल मिलाएं, नहीं तो यह एक `ValueError` उठाएगा।

### timedelta के साथ तारीख अंकगणित

समय अंतराल जोड़ने या घटाने के लिए `timedelta` का उपयोग करें।

```python
now = datetime.datetime.now()
one_day = datetime.timedelta(days=1)
tomorrow = now + one_day
print(tomorrow)  # वर्तमान तारीख + 1 दिन

# घटाएं
yesterday = now - one_day

# भाग: दिन, सेकंड, माइक्रोसेकंड, मिलीसेकंड, मिनट, घंटे, सप्ताह
one_week = datetime.timedelta(weeks=1)
```

तारीखों के बीच अंतर के लिए:

```python
date1 = datetime.datetime(2023, 10, 5)
date2 = datetime.datetime(2023, 10, 10)
delta = date2 - date1
print(delta.days)  # 5
```

### टाइमज़ोन (उन्नत उपयोग)

टाइमज़ोन-जागरूक ऑपरेशन्स के लिए, `timezone` (Python 3.3+) का उपयोग करें। यह मॉड्यूल मूल रूप से टाइमज़ोन रूपांतरणों को संभालता नहीं है; मजबूत हैंडलिंग के लिए `pytz` लाइब्रेरी के साथ जोड़ा जा सकता है।

```python
from datetime import datetime, timezone

# Naive datetime (कोई टाइमज़ोन नहीं)
naive = datetime.now()

# UTC aware
utc = datetime.now(timezone.utc)

# कस्टम टाइमज़ोन (tzinfo की आवश्यकता होती है)
import pytz  # pip install pytz की आवश्यकता हो सकती है
eastern = pytz.timezone("US/Eastern")
eastern_time = naive.astimezone(eastern)
```

### सामान्य सुझाव और खतरे
- **अपरिवर्तनीय ऑब्जेक्ट**: `datetime` ऑब्जेक्ट्स को सीधे संशोधित नहीं किया जा सकता; अंकगणित नए बनाते हैं।
- **महीने के दिन**: लीप वर्षों में फरवरी के लिए 29 का उपयोग करें; यह मॉड्यूल लीप चेक के लिए `calendar` या `dateutil` के साथ इसे संभालता है।
- **प्रदर्शन**: लूप्स में बार-बार `now()` कॉल से बचें; मूल्य को स्टोर करें।
- **त्रुटियां**: अमान्य तारीखों (जैसे, `date(2023, 2, 30)` `ValueError` उठाता है) के लिए ध्यान दें।
- **लाइब्रेरी एक्सटेंशन**: उन्नत पार्सिंग के लिए, `dateutil` या `arrow` पैकेज पर विचार करें।

पूरी डॉक्यूमेंटेशन के लिए, Python की आधिकारिक डॉक्स [docs.python.org](https://docs.python.org/3/library/datetime.html) पर जांचें। इन उदाहरणों के साथ Python इंटरप्रेटर में अभ्यास करें।