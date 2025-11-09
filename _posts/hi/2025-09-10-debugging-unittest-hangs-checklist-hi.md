---
audio: false
date: 2025-09-10
generated: true
image: false
lang: hi
layout: post
model: openai/gpt-5
title: यूनिटटेस्ट हैंग होने की समस्या का समाधान करने की जाँचसूची
translated: true
type: note
---

`unittest` में हैंग होना आमतौर पर डेडलॉक (थ्रेड/एसिंक), अटका हुआ I/O, सबप्रोसेस/मल्टीप्रोसेसिंग समस्याओं, या नेटवर्क कॉल पर इंतजार कर रहे टेस्ट के कारण होता है। यहाँ एक संक्षिप्त चेकलिस्ट है जो *यह देखने में मदद करेगी कि यह कहाँ अटका है* और *इसे ठीक करेगी*—Python 3.9–3.11 पर काम करती है।

### 1) unittest को विस्तार से (और सही तरीके से) चलाएँ

```bash
# अगर xx.py, unittest.main() को कॉल करता है
python xx.py -v

# या डिस्कवरी का उपयोग करें (सुझाया गया)
python -m unittest -v
python -m unittest discover -v -s tests -p "test_*.py"
```

> नोट: `python -v` **इंटरप्रेटर इम्पोर्ट-वर्बोज़** है, टेस्ट-वर्बोज़ नहीं। टेस्ट नाम और प्रोग्रेस के लिए `-m unittest -v` का उपयोग करें।

### 2) faulthandler + डेव मोड चालू करें (हैंग होने पर स्टैक डंप, सख्त चेतावनियाँ)

```bash
# एक बार के लिए
python -X faulthandler -X dev -u -m unittest -v
# या env के जरिए
export PYTHONFAULTHANDLER=1
python -X dev -u -m unittest -v
```

* `-X faulthandler` Python को फेटल सिग्नल/टाइमआउट पर थ्रेड स्टैक ट्रेस प्रिंट करने देता है।
* `-X dev` चेतावनियों/त्रुटियों को और जोरदार बनाता है।
* `-u` stdout/stderr को अनबफर करता है ताकि आप प्रिंट्स को रियल टाइम में *देख* सकें।

### 3) जब यह अटका हुआ लगे तो एक ट्रेसबैक फोर्स करें

विकल्प A — दूसरे टर्मिनल से (Linux/macOS):

```bash
kill -SIGUSR1 <pid>  # faulthandler चालू होने पर, सभी थ्रेड स्टैक डंप कर देता है
```

विकल्प B — अपने टेस्ट बूटस्ट्रैप में जोड़ें (`xx.py` के सबसे ऊपर):

```python
import faulthandler, signal, sys
faulthandler.enable()
# SIGUSR1 पर स्टैक डंप करें:
faulthandler.register(signal.SIGUSR1, all_threads=True)
# 120s से अधिक हैंग होने पर ऑटो-डंप:
faulthandler.dump_traceback_later(120, repeat=True)
```

### 4) एक्सेक्यूशन को स्टेप-बाय-स्टेप ट्रेस करें (भारी लेकिन निर्णायक)

```bash
python -m trace --trace xx.py
# या
python -m trace --trace -m unittest discover -v
```

आपको निष्पादित होने वाली हर लाइन दिखाई देगी; जब आउटपुट "फ्रीज" हो जाए तो रुक जाएँ—वही आपका हैंग साइट है।

### 5) तुरंत डिबगर का उपयोग करें

```bash
python -m pdb xx.py         # अगर xx.py, unittest.main() को कॉल करता है
# संदिग्ध लाइन पर ब्रेक लगाएँ:
# (Pdb) b mymodule.py:123
# (Pdb) c
```

डिस्कवरी रन के लिए, संदिग्ध जगह पर `import pdb; pdb.set_trace()` जोड़ें।

### 6) आम कारण और त्वरित समाधान

* **macOS/Windows पर मल्टीप्रोसेसिंग**: हमेशा टेस्ट एंट्री को गार्ड करें।

  ```python
  if __name__ == "__main__":
      import unittest
      unittest.main()
  ```

  अगर आप macOS पर टेस्ट में प्रोसेस स्पॉन करते हैं:

  ```python
  import multiprocessing as mp
  if __name__ == "__main__":
      mp.set_start_method("fork")  # कभी-कभी डिफ़ॉल्ट "spawn" की तुलना में हैंग से बचाता है
  ```

  (यह केवल तभी करें जब आप जानते हों कि आपका कोड fork-safe है।)

* **थ्रेड डेडलॉक**: टाइमआउट के बिना `join()`, रिलीज़ नहीं हुए लॉक, या मेन थ्रेड पर इंतजार कर रहे बैकग्राउंड थ्रेड्स की जाँच करें। इसे बदलें:

  ```python
  t.join()
  ```

  इसके साथ:

  ```python
  t.join(timeout=5); assert not t.is_alive()
  ```

* **एसिंक टेस्ट**: सुनिश्चित करें कि आप `IsolatedAsyncioTestCase` (3.8+) या `asyncio.run()` का उपयोग कर रहे हैं। डबल इवेंट लूप या भूला हुआ `await` अक्सर हैंग करता है।

* **नेटवर्क कॉल**: **छोटे टाइमआउट** हर जगह जोड़ें:

  ```python
  requests.get(url, timeout=5)
  ```

* **stdin इंतजार**: `input()` हटा दें या टेस्ट में गार्ड करें; CI/stdin हमेशा के लिए ब्लॉक कर सकता है।

* **गलत मॉकिंग**: एक मॉक किया गया मेथड जो कभी `Future`/प्रॉमिस रिज़ॉल्व नहीं करता या एक स्टब किया गया सर्वर जो शुरू नहीं हुआ।

### 7) अतिरिक्त दृश्यता

* अगर लीक/स्पिन का संदेह है तो एलोकेशन देखें:

  ```bash
  python -X tracemalloc=25 -m unittest -v
  ```
* इम्पोर्ट नॉइज़ दिखाएँ (हैंग के लिए शायद ही कभी जरूरत हो):

  ```bash
  python -v -m unittest -v
  ```

### 8) अगर यह सिर्फ एक Python वर्जन पर हैंग होता है

* दोनों को आज़माएँ:

  ```bash
  pyenv local 3.11.9
  python -X faulthandler -X dev -m unittest -v

  pyenv local 3.9.19
  python -X faulthandler -X dev -m unittest -v
  ```

  अंतर आमतौर पर `multiprocessing`, `asyncio`, या C-extension व्यवहार के आसपास सामने आते हैं।

---

अगर आप `faulthandler` से ट्रेसबैक (या `trace --trace` से आखिरी लाइनें) पेस्ट करते हैं, तो मैं सटीक अपराधी की ओर इशारा करूँगा और एक लक्षित समाधान सुझाऊँगा।