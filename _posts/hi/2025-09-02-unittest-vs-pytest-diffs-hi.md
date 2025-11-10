---
audio: false
generated: true
image: false
lang: hi
layout: post
title: यूनिटटेस्ट बनाम पाइटेस्ट मुख्य अंतर
translated: true
type: note
---

यहाँ आपकी दैनिक टेस्टिंग में वास्तव में क्या बदलता है, उस पर केंद्रित एक स्पष्ट तुलना दी गई है।

# फिलॉसफी और स्टाइल

* **unittest**: xUnit स्टाइल (Java/JUnit जैसा)। क्लास-आधारित टेस्ट, `setUp/tearDown` जैसे लाइफसाइकल हुक, मेथड नाम `test_` से शुरू होने चाहिए।
* **pytest**: पाइथोनिक और मिनिमल। टेस्ट **फंक्शन** या क्लासेज, रिच फिक्स्चर्स, सादा `assert` जिसमें असेर्शन रिव्राइटिंग होती है।

# टेस्ट डिस्कवरी

* **unittest**: `python -m unittest discover` (या सूट लोड करें)। `test*.py` और `TestCase` सबक्लासेज ढूंढता है।
* **pytest**: `pytest` स्वचालित रूप से `test_*.py` और `*_test.py` ढूंढता है; `test_*` फंक्शन और `Test*` क्लासेज पर मेथड्स।

# असेर्शन

* **unittest**: कई विशिष्ट मेथड्स (`assertEqual`, `assertTrue`, `assertRaises`, …)।
* **pytest**: सादे `assert` का उपयोग करें और यह एक्सप्रेसिव डिफ्स प्रिंट करता है ("left vs right"), `pytest.raises` को सपोर्ट करता है।

# फिक्स्चर्स और सेटअप

* **unittest**: `setUp()/tearDown()`, `setUpClass/tearDownClass`, `setUpModule/tearDownModule`।
* **pytest**: **फिक्स्चर्स** स्कोप्स के साथ (फंक्शन/क्लास/मॉड्यूल/सेशन), डिपेंडेंसी इंजेक्शन, ऑटोयूज, फाइनलाइज़र। छोटे, पुन: प्रयोज्य सेटअप को प्रोत्साहित करता है।

# पैरामीट्राइजेशन

* **unittest**: कोई बिल्ट-इन नहीं; लूप्स/`subTest` या थर्ड-पार्टी लाइब्रेरीज का उपयोग करें।
* **pytest**: `@pytest.mark.parametrize` फर्स्ट-क्लास है (इनपुट्स का मैट्रिक्स, साफ रिपोर्टिंग)।

# स्किप्स, एक्सपेक्टेड फेल्योर, मार्कर्स

* **unittest**: `@skip`, `@skipIf`, `@expectedFailure`।
* **pytest**: समान विचार प्लस शक्तिशाली **मार्कर्स** (`@pytest.mark.slow`, `xfail`, `filterwarnings`, कस्टम मार्क्स) और कमांड-लाइन सिलेक्शन (`-m slow`)।

# प्लगइन्स और इकोसिस्टम

* **unittest**: बैटरीज-इन्क्लूडेड लेकिन लीन; एडवांस्ड फीचर्स के लिए एक्सटर्नल रनर्स/टूल्स पर निर्भर।
* **pytest**: विशाल प्लगइन इकोसिस्टम (`pytest-xdist` पैरेलल के लिए, `pytest-randomly`, `pytest-cov`, `pytest-mock`, `pytest-asyncio`, `pytest-django`, आदि)।

# मॉक्स

* **unittest**: `unittest.mock` स्टैंडर्ड है; हर जगह काम करता है।
* **pytest**: `unittest.mock` या `pytest-mock` के `mocker` फिक्स्चर का उपयोग करें (क्लीनर पैचिंग और ऑटो-टीयरडाउन)।

# एसिंक टेस्टिंग

* **unittest**: 3.8 से, `IsolatedAsyncioTestCase` है (ठीक है लेकिन वर्बोज़ है)।
* **pytest**: `pytest-asyncio` (या trio के प्लगइन) के साथ आपको `@pytest.mark.asyncio` और इवेंट लूप्स के लिए फिक्स्चर सपोर्ट मिलता है।

# परफॉर्मेंस और पैरेलल

* **unittest**: कोई बिल्ट-इन पैरेलल नहीं; `unittest-parallel`/CI ट्रिक्स का उपयोग करें।
* **pytest**: `pytest-xdist -n auto` गो-टू सॉल्यूशन है।

# IDE/CI/कवरेज

* दोनों IDE और CI के साथ इंटीग्रेट होते हैं। कवरेज `coverage.py` के माध्यम से:

  * **unittest**: `coverage run -m unittest` → `coverage report`।
  * **pytest**: `pytest --cov=your_pkg` के साथ `pytest-cov`।

# कब किसे चुनें

* **unittest चुनें** यदि:

  * आपको केवल स्टैंडर्ड लाइब्रेरी चाहिए (कोई एक्सटर्नल डिपेंडेंसी नहीं)।
  * आप लीगेसी/xUnit कोडबेस या सख्त संगठन नीतियों में प्लग इन कर रहे हैं।
* **pytest चुनें** यदि:

  * आप तेजी से टेस्ट लिखना, स्पष्ट फेल्योर और शक्तिशाली फिक्स्चर्स/पैरामीट्राइजेशन चाहते हैं।
  * आप इसके प्लगइन इकोसिस्टम और पैरेललाइजेशन से लाभान्वित होंगे।

# इंटरऑप और माइग्रेशन

आप **unittest** सूट्स को **pytest** के अंतर्गत चला सकते हैं (pytest `unittest.TestCase` ढूंढ लेता है)। यह आपको धीरे-धीरे माइग्रेट करने देता है:

1. रनर के रूप में `pytest` को इनवोक करना शुरू करें।
2. मौजूदा टेस्ट्स के साथ-साथ pytest टेस्ट्स जोड़ें।
3. फिक्स्चर्स/पैरामीट्राइज जहां मददगार हों, वहां इंट्रोड्यूस करें।
4 * वैकल्पिक रूप से बाद में पुराने `TestCase` को फंक्शन में रीफैक्टर करें।

# छोटे साइड-बाय-साइड उदाहरण

## वही टेस्ट

**unittest**

```python
import unittest

class TestMath(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3]

    def test_sum(self):
        self.assertEqual(sum(self.data), 6)

    def test_raises(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 0

if __name__ == "__main__":
    unittest.main()
```

**pytest**

```python
import pytest

@pytest.fixture
def data():
    return [1, 2, 3]

def test_sum(data):
    assert sum(data) == 6

def test_raises():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```

## पैरामीट्राइजेशन

**unittest (subTest)**

```python
import unittest

class TestParity(unittest.TestCase):
    def test_even(self):
        for n in [0, 2, 4]:
            with self.subTest(n=n):
                self.assertEqual(n % 2, 0)
```

**pytest**

```python
import pytest

@pytest.mark.parametrize("n", [0, 2, 4])
def test_even(n):
    assert n % 2 == 0
```

## मॉकिंग

**unittest.mock**

```python
from unittest.mock import patch

@patch("pkg.api.fetch_user", return_value={"id": 1})
def test_uses_api(mock_fetch):
    from pkg.service import get_user
    assert get_user(1)["id"] == 1
    mock_fetch.assert_called_once_with(1)
```

**pytest-mock**

```python
def test_uses_api(mocker):
    mock_fetch = mocker.patch("pkg.api.fetch_user", return_value={"id": 1})
    from pkg.service import get_user
    assert get_user(1)["id"] == 1
    mock_fetch.assert_called_once_with(1)
```

# प्रैक्टिकल सिफारिशें

* नई प्रोजेक्ट्स: स्पीड, रीडेबिलिटी और इकोसिस्टम के लिए डिफॉल्ट रूप से **pytest** चुनें।
* लीगेसी/स्टैंडर्ड लाइब्रेरी-ओनली एनवायरनमेंट: **unittest** के साथ बने रहें, लेकिन टेस्ट रीराइट किए बिना बेहतर आउटपुट और प्लगइन्स पाने के लिए इसे **pytest** के माध्यम से चलाने पर विचार करें।
* तेज CI के लिए जल्दी `pytest-xdist` जोड़ें, और कवरेज के लिए `pytest-cov`।
* बड़े क्लास सेटअप्स पर फिक्स्चर्स को प्राथमिकता दें; उन्हें छोटा और कंपोज़ेबल रखें।
* सूट्स को ऑर्गनाइज़ करने (`slow`, `integration`, `db`) और CI स्टेजेस में सबसेट चलाने के लिए मार्कर्स का उपयोग करें।

यदि आप चाहें, तो मुझे अपनी प्रोजेक्ट लेआउट और कंस्ट्रेंट्स बताएं (केवल स्टैंडर्ड लाइब्रेरी? पैरेलल चाहिए? एसिंक? Django/Flask/FastAPI?) और मैं आपके लिए एक मिनिमल, ओपिनियनेटेड टेस्ट सेटअप का स्केच तैयार करूंगा।