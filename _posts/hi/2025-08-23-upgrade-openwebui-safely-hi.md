---
audio: false
generated: true
image: false
lang: hi
layout: post
title: ओपन वेबयूआई को सुरक्षित रूप से अभी अपग्रेड करें
translated: true
type: note
---

आपको समझ गया। यहाँ Open WebUI को अपग्रेड करने के सुरक्षित और सीधे तरीके दिए गए हैं।

## यदि आपने `pip` के साथ इंस्टॉल किया है (आपका मामला)

```bash
# 1) (अनुशंसित) उस env को एक्टिवेट करें जिसे आप Open WebUI के लिए उपयोग करते हैं
#    उदाहरण के लिए conda:
conda activate open-webui
#    या venv:
# source ~/open-webui-venv/bin/activate

# 2) नवीनतम संस्करण में अपग्रेड करें
python3.11 -m pip install -U open-webui

# 3) (वैकल्पिक) यदि pip कैशिंग समस्या पैदा करती है
python3.11 -m pip cache purge
python3.11 -m pip install --no-cache-dir -U open-webui

# 4) जांचें कि आपको क्या मिला
python3.11 -m pip show open-webui
```

ऑफिसियल डॉक्स कहती हैं कि सिर्फ `pip install -U open-webui` नवीनतम रिलीज़ में अपग्रेड कर देगा। ([Open WebUI][1])

### अपने डेटा/सेटिंग्स को स्थायी रखें

जब आप सर्वर चलाते हैं, तो आप एक डेटा डायरेक्टरी को पिन कर सकते हैं ताकि अपग्रेड उसे प्रभावित न करें:

```bash
# macOS/Linux
DATA_DIR="$HOME/.open-webui" open-webui serve
# Windows (PowerShell)
$env:DATA_DIR="C:\open-webui\data"; open-webui serve
```

यह डॉक्स के मार्गदर्शन को दर्शाता है कि `DATA_DIR` सेट करें (या उसी वेरिएबल के साथ `uvx … @latest serve` का उपयोग करें) ताकि आपकी चैट्स/कॉन्फ़िग पैकेज इंस्टॉलेशन के बाहर सुरक्षित रहें। ([Open WebUI][2])

> टिप: यदि आपने पहले `DATA_DIR` के बिना चलाया था, तो अब इसका उपयोग शुरू करें; Open WebUI अब से इस फ़ोल्डर का उपयोग करेगा।

## यदि आपने Docker का उपयोग किया है (पूर्णता के लिए)

```bash
# पुराने कंटेनर को रोकें और हटाएं (डेटा नामित वॉल्यूम में है)
docker rm -f open-webui

# नवीनतम इमेज प्राप्त करें
docker pull ghcr.io/open-webui/open-webui:main

# अपने मौजूदा वॉल्यूम के साथ फिर से शुरू करें
docker run -d -p 3000:8080 \
  -v open-webui:/app/backend/data \
  --name open-webui \
  ghcr.io/open-webui/open-webui:main
```

यह प्रोजेक्ट का अनुशंसित मैन्युअल अपडेट फ्लो है; आपका डेटा `open-webui` Docker वॉल्यूम में स्थायी रहता है। ([Open WebUI][3])

## जांचें कि "नवीनतम" क्या है

आप अपग्रेड करने से पहले/बाद में GitHub Releases से नवीनतम टैग की पुष्टि कर सकते हैं। ([GitHub][4])

यदि कोई त्रुटि होती है (जैसे, Python वर्जन मिसमैच), सुनिश्चित करें कि आप pip विधि के लिए Python 3.11 पर हैं, जिसकी प्रोजेक्ट स्पष्ट रूप से सिफारिश करता है। ([GitHub][5])

क्या आप चाहते हैं कि मैं आपके वर्तमान env को जांचूं या किसी अपग्रेड त्रुटि आउटपुट की व्याख्या करूं? इसे यहां पेस्ट करें और मैं समस्या निवारण करूंगा।

[1]: https://docs.openwebui.com/getting-started/quick-start/?utm_source=chatgpt.com "️ Quick Start"
[2]: https://docs.openwebui.com/?utm_source=chatgpt.com "Open WebUI: Home"
[3]: https://docs.openwebui.com/getting-started/updating/?utm_source=chatgpt.com "Updating Open WebUI"
[4]: https://github.com/open-webui/open-webui/releases?utm_source=chatgpt.com "Releases · open-webui/open-webui"
[5]: https://github.com/open-webui/open-webui?utm_source=chatgpt.com "open-webui/open-webui: User-friendly AI Interface ..."