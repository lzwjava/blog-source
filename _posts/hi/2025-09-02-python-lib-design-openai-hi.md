---
audio: false
generated: true
image: false
lang: hi
layout: post
title: ओपनएआई से पायथन लाइब्रेरी डिज़ाइन के सबक
translated: true
type: note
---

यहाँ `openai/openai-python` रिपॉजिटरी की एक त्वरित जांच और एक बेहतरीन Python लाइब्रेरी बनाने के लिए आप अपना सकने वाले सबक हैं।

# रिपॉजिटरी क्या दिखाती है (एक नज़र में)

*   **स्पष्ट "src लेआउट"**: कोड के लिए `src/openai`; शीर्ष-स्तरीय `tests/`, `examples/`, `scripts/`, `.github/`, `pyproject.toml`, `mypy.ini`, `noxfile.py`, आदि। यह अलगाव import पथों को साफ रखता है और test खोज को अनुमानित बनाता है। ([GitHub][1])
*   **टाइप किया गया पब्लिक सरफेस**: अनुरोध `TypedDict` का उपयोग करते हैं, प्रतिक्रियाएँ **Pydantic** मॉडल हैं; बेहतरीन Developer Experience और सुरक्षित refactors। ([GitHub][1])
*   **Sync + Async समानता**: `OpenAI` और `AsyncOpenAI` एक ही API साझा करते हैं; डिफॉल्ट ट्रांसपोर्ट `httpx` है, जिसमें वैकल्पिक `aiohttp` है। ([GitHub][1])
*   **फर्स्ट-क्लास स्ट्रीमिंग**: सिंक और एसिंक दोनों में सरल इटरेशन के साथ Server-Sent Events। ([GitHub][1])
*   **ऑटो-पैजिनेशन**: इटरेबल लिस्ट एंडपॉइंट्स ताकि उपयोगकर्ताओं को पेज लूप्स न बनाने पड़ें। ([GitHub][1])
*   **रियलटाइम/WebSocket क्लाइंट**: उदाहरणों और त्रुटि-हैंडलिंग मार्गदर्शन के साथ एक ऑप्ट-इन सब-क्लाइंट। ([GitHub][1])
*   **कोडजेन पाइपलाइन**: SDK एक OpenAPI स्पेक से जनरेट किया गया है (Stainless के माध्यम से), जो स्थिरता और प्रकार कवरेज लागू करता है। ([GitHub][1])

# डिज़ाइन टेकअवे जिन्हें आप दोबारा उपयोग कर सकते हैं

*   **"एक स्पष्ट तरीका" बनाए रखें**: एक ही `Client` (प्लस `AsyncClient`) एक्सपोज़ करें जिसमें मिरर मेथड नेम हों। उपयोगकर्ताओं को आश्चर्य नहीं होना चाहिए "मुझे किस क्लास का उपयोग करना चाहिए?" OpenAI SDK इसे `OpenAI` और `AsyncOpenAI` के साथ दिखाता है। ([GitHub][1])
*   **पोर्टेबल ट्रांसपोर्ट्स**: डिफॉल्ट रूप से `httpx` का उपयोग करें, लेकिन एक स्वैपेबल HTTP बैकएंड (जैसे, `aiohttp`) की अनुमति दें, ताकि हाई-कनकरेंसी उपयोगकर्ता सीमित न रहें। ([GitHub][1])
*   **टाइप किए गए अनुरोध + मॉडल**: टाइप किए गए अनुरोध पेलोड और समृद्ध प्रतिक्रिया मॉडल शिप करें। इससे आपको एडिटर ऑटोकम्पलीट, लिंट करने योग्य उदाहरण और सुरक्षित ब्रेकिंग चेंजेज मिलते हैं। ([GitHub][1])
*   **जीरो-फ्रिक्शन स्ट्रीमिंग**: स्ट्रीमिंग को एक सादे इटरेटर / एसिंक इटरेटर के रूप में डिज़ाइन करें। कस्टम इवेंट पंपों की आवश्यकता नहीं है। ([GitHub][1])
*   **इटरेटर-आधारित पैजिनेशन**: `for item in client.resource.list(limit=...)` एक्सपोज़ करें और पेजों को आलसी तरीके से फ़ेच करें। यह उपयोगकर्ता कोड को छोटा रखता है और साथ ही कुशल बना रहता है। ([GitHub][1])
*   **सबसिस्टम सब-क्लाइंट हैं**: विशेष सुविधाओं (जैसे, रियलटाइम) को एक स्पष्ट रूप से नामित नेमस्पेस (`client.beta.realtime`) के पीछे रखें ताकि मुख्य सतह साफ रहे। ([GitHub][1])
*   **जहाँ मदद मिले वहाँ जनरेट करें**: यदि आपकी API स्पेक-ड्रिवेन है, तो कोडजेन को उबाऊ, स्ट्रॉन्गली-टाइप्ड लेयर्स बनाने दें और एर्गोनोमिक बिट्स को हैंड-क्राफ्ट करें। ([GitHub][1])

# एक स्केलेटन जिसे आप कॉपी कर सकते हैं

```bash
yourlib/
  pyproject.toml
  noxfile.py
  mypy.ini
  README.md
  CHANGELOG.md
  SECURITY.md
  src/yourlib/
    __init__.py
    _version.py
    _types.py            # TypedDicts, enums
    _errors.py           # Exception hierarchy
    _http.py             # httpx client wrapper, retries, timeouts
    _pagination.py       # generic Pager[T]
    client.py            # Client + AsyncClient, auth, base URL
    resources/
      __init__.py
      widgets.py         # resource groups w/ sync+async methods
    streaming.py         # SSE helpers (sync/async)
  tests/
    test_client.py
    test_widgets.py
  examples/
    quickstart.py
    async_quickstart.py
```

## पब्लिक API (`src/yourlib/__init__.py`)

*   केवल वही री-एक्सपोर्ट करें जिसकी उपयोगकर्ताओं को आवश्यकता है:

```python
from .client import Client, AsyncClient
from ._errors import YourLibError, APIError, RateLimitError
__all__ = ["Client", "AsyncClient", "YourLibError", "APIError", "RateLimitError"]
```

## क्लाइंट शेप (सिंक और एसिंक)

*   समान मेथड नामों को मिरर करें; केवल `await`/`async` में अंतर होना चाहिए:

```python
# src/yourlib/client.py
import httpx
from .resources.widgets import Widgets
from ._http import HttpTransport

class Client:
    def __init__(self, api_key=None, base_url="https://api.example.com", http_client=None):
        self._transport = HttpTransport(api_key, base_url, http_client or httpx.Client(timeout=30))
        self.widgets = Widgets(self._transport)

class AsyncClient:
    def __init__(self, api_key=None, base_url="https://api.example.com", http_client=None):
        self._transport = HttpTransport(api_key, base_url, http_client or httpx.AsyncClient(timeout=30))
        self.widgets = Widgets(self._transport)
```

## पैजिनेशन पैटर्न

```python
# src/yourlib/_pagination.py
from typing import AsyncIterator, Iterator, Generic, TypeVar, Callable, Optional
T = TypeVar("T")
class Pager(Generic[T]):
    def __init__(self, fetch: Callable[..., dict], limit: int = 100):
        self._fetch = fetch
        self._limit = limit
        self._cursor = None
    def __iter__(self) -> Iterator[T]:
        while True:
            page = self._fetch(limit=self._limit, cursor=self._cursor)
            for item in page["data"]:
                yield item
            self._cursor = page.get("next_cursor")
            if not self._cursor:
                break
```

इसे इस तरह एक्सपोज़ करें कि उपयोगकर्ता `for item in client.widgets.list(limit=50): ...` कर सकें। (OpenAI का SDK भी यही तरीका अपनाता है। ([GitHub][1]))

## स्ट्रीमिंग पैटर्न (SSE)

*   `httpx` की स्ट्रीमिंग को एक छोटे इटरेटर के साथ लपेटें जो इवेंट्स यील्ड करे; एक एसिंक वेरिएंट को मिरर करें। इससे OpenAI SDK में देखे गए एर्गोनोमिक `for event in client.responses.create(..., stream=True)` यूजर एक्सपीरियंस मिलता है। ([GitHub][1])

# टूलिंग और रिलीज़ फ्लो जो स्केल करता है

*   **`pyproject.toml` (PEP 621)** मेटाडेटा के लिए; dev डिपेंडेंसीज़ को अलग से लॉक करें।
*   **टाइप चेकिंग**: टाइप्स शिप करें, CI में `mypy` चलाएँ (उनकी रिपो में `mypy.ini` है)। ([GitHub][1])
*   **टास्क रनर**: टेस्ट, लिंट, टाइपचेक, बिल्ड के लिए `nox` सेशन (वे `noxfile.py` का उपयोग करते हैं)। ([GitHub][1])
*   **CI**: Python वर्जन/प्लेटफ़ॉर्म पर टेस्ट चलाने के लिए `.github/` में GitHub Actions। ([GitHub][2])
*   **CHANGELOG** और **वर्जनिंग**: एक मानव-पठनीय लॉग रखें; रिलीज़ को ऑटोमेट करें (वे release-please का उपयोग करते हैं)। ([GitHub][1])
*   **सुरक्षा और योगदान दस्तावेज़**: रिपोर्टर्स और योगदानकर्ताओं के लिए अपेक्षाएँ निर्धारित करें। ([GitHub][1])

# डॉक्स और उदाहरण

*   **README उदाहरण** रन करने योग्य और कॉपी-पेस्ट फ्रेंडली होने चाहिए—सिंक, एसिंक, स्ट्रीमिंग, पैजिनेशन, और कोई भी "विशेष ट्रांसपोर्ट" (जैसे `aiohttp`)। OpenAI README प्रत्येक को संक्षेप में प्रदर्शित करती है। ([GitHub][1])
*   **API संदर्भ**: यदि कोड-जनरेटेड है, तो एक `api.md`/रिफरेंस साइट प्रकाशित करें और इसे रिलीज़ के साथ लॉकस्टेप में रखें। ([GitHub][1])
*   **उदाहरण फ़ोल्डर**: न्यूनतम, केंद्रित स्क्रिप्ट्स, और एक "पूर्ण" नमूना शामिल करें।

# एरर्स, रिट्रीज़ और टाइमआउट्स (क्या इम्प्लीमेंट करना है)

*   **एरर हायरार्की**: `YourLibError` → `APIError`, `AuthError`, `RateLimitError`, `TimeoutError`। HTTP स्टेटस कोड को एक्सेप्शन में मैप करें; अनुरोध आईडी शामिल करें।
*   **रिट्रीज़**: इडेम्पोटेंट ऑपरेशन्स को 429/5xx पर एक्सपोनेंशियल बैकऑफ + जिटर के साथ ऑटो-रिट्री करनी चाहिए।
*   **टाइमआउट्स**: समझदार डिफॉल्ट सेट करें और उन्हें क्लाइंट और प्रति-कॉल स्तर पर कॉन्फ़िगरेबल बनाएँ।
*   **लॉगिंग हुक्स**: स्ट्रक्चर्ड डिबग लॉगिंग बिना सीक्रेट्स लीक किए।

# पैकेजिंग और संगतता

*   **3–4 एक्टिव Python माइनरों का समर्थन करें** (जैसे, 3.9–3.13), और उन्हें CI में टेस्ट करें।
*   **इम्पोर्ट पर कोई साइड इफेक्ट नहीं**; नेटवर्क/क्लाइंट निर्माण को पहले उपयोग तक स्थगित करें।
*   **एनवायरनमेंट कॉन्फ़िगरेशन**: `API_KEY` env var स्वीकार करें लेकिन उपयोगकर्ताओं को क्रेडेंशियल्स एक्सप्लिसिटली पास करने भी दें (OpenAI `OPENAI_API_KEY` और एक `.env` टिप दिखाता है)। ([GitHub][1])
*   **स्थिर पब्लिक API**: इंटर्नल्स को प्राइवेट (`_module.py`) रखें, `__init__.py` में एक साफ-सुथरी सतह को री-एक्सपोर्ट करें।

# बचने के लिए नुकसान

*   सब कुछ एक ही मॉड्यूल में ठूंसना; संसाधन द्वारा विभाजित करें और सार्वजनिक आयात स्थिर रखें।
*   ट्रांसपोर्ट प्रकारों को लीक करना; आपके संसाधनों को सीधे `httpx` पर नहीं, बल्कि एक छोटे "ट्रांसपोर्ट" प्रोटोकॉल पर निर्भर होना चाहिए।
*   एसिंक को सेकंड-क्लास महसूस कराना; सुनिश्चित करें कि टेस्ट और उदाहरण दोनों को समान रूप से कवर करते हैं (OpenAI की समानता एक अच्छा मॉडल है)। ([GitHub][1])
*   स्ट्रीमिंग के लिए, उपयोगकर्ताओं को थ्रेड्स या कॉलबैक्स संभालने के लिए मजबूर न करें—इटरेटर सरल होते हैं। ([GitHub][1])

यदि आप चाहें, तो मैं इस संरचना को एक ठोस डोमेन (जैसे, आपकी आंतरिक REST सेवाओं के लिए एक टाइप्ड क्लाइंट, जिसमें सिंक/एसिंक, पैजिनेशन और स्ट्रीमिंग हो) के लिए स्कैफोल्ड कर सकता हूँ और रेडी-टू-रन `nox`, CI, और उदाहरण स्क्रिप्ट्स ड्रॉप इन कर सकता हूँ।

[1]: https://github.com/openai/openai-python "GitHub - openai/openai-python: The official Python library for the OpenAI API"
[2]: https://github.com/openai/openai-python/tree/main/.github "openai-python/.github at main · openai/openai-python · GitHub"