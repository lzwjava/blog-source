---
audio: false
generated: true
lang: hi
layout: post
title: सेलेनियम गेकोड्राइवर उबंटू इंस्टालेशन
translated: true
type: note
---

Ubuntu पर Selenium Firefox ड्राइवर (geckodriver) इंस्टॉल करने के लिए, इन चरणों का पालन करें:

1. **Firefox इंस्टॉल करें** (यदि पहले से इंस्टॉल नहीं है):
   ```bash
   sudo apt update
   sudo apt install firefox
   ```

2. **geckodriver डाउनलोड करें**:
   - [geckodriver रिलीज़ पेज](https://github.com/mozilla/geckodriver/releases) पर जाएँ।
   - अपने Firefox वर्जन के साथ कंपेटिबल लेटेस्ट वर्जन चुनें। Ubuntu के लिए, Linux 64-bit वर्जन डाउनलोड करें (जैसे, `geckodriver-vX.XX.X-linux64.tar.gz`)।
   - डाउनलोड करने के लिए उदाहरण कमांड (`X.XX.X` को लेटेस्ट वर्जन से बदलें):
     ```bash
     wget https://github.com/mozilla/geckodriver/releases/download/vX.XX.X/geckodriver-vX.XX.X-linux64.tar.gz
     ```

3. **डाउनलोड की गई फ़ाइल को एक्सट्रैक्ट करें**:
   ```bash
   tar -xvzf geckodriver-vX.XX.X-linux64.tar.gz
   ```

4. **geckodriver को सिस्टम पथ पर मूव करें**:
   - एक्सट्रैक्ट किए गए `geckodriver` को `/usr/local/bin` पर मूव करें ताकि यह सिस्टम-वाइड एक्सेसिबल हो:
     ```bash
     sudo mv geckodriver /usr/local/bin/
     ```
   - इसे एक्जीक्यूटेबल बनाएँ:
     ```bash
     sudo chmod +x /usr/local/bin/geckodriver
     ```

5. **Python के लिए Selenium इंस्टॉल करें** (यदि Python उपयोग कर रहे हैं):
   ```bash
   pip install selenium
   ```

6. **इंस्टॉलेशन वेरिफाई करें**:
   - geckodriver वर्जन चेक करें:
     ```bash
     geckodriver --version
     ```
   - एक साधारण Python स्क्रिप्ट से टेस्ट करें:
     ```python
     from selenium import webdriver

     driver = webdriver.Firefox()
     driver.get("https://www.example.com")
     print(driver.title)
     driver.quit()
     ```

**नोट्स**:
- सुनिश्चित करें कि आपका Firefox वर्जन geckodriver वर्जन के साथ कंपेटिबल है (geckodriver GitHub पेज पर रिलीज़ नोट्स चेक करें)।
- यदि कोई इशू आए, तो सुनिश्चित करें कि `python3-pip` इंस्टॉल है:
  ```bash
  sudo apt install python3-pip
  ```
- यदि geckodriver नहीं मिल रहा है, तो अपने `PATH` में `/usr/local/bin` ऐड करें:
  ```bash
  export PATH=$PATH:/usr/local/bin
  ```

इससे Ubuntu पर Selenium Firefox ड्राइवर सेट अप हो जाना चाहिए। यदि कोई इशू आए तो बताएँ!

---

`geckodriver-v0.36.0-linux-aarch64.tar.gz` और `geckodriver-v0.36.0-linux64.tar.gz` के बीच का अंतर टार्गेट CPU आर्किटेक्चर में निहित है:

- **linux-aarch64**: यह 64-bit ARM आर्किटेक्चर (जैसे, ARMv8-A) के लिए है, जो आमतौर पर Raspberry Pi, कुछ सर्वर, या मॉडर्न ARM-आधारित Linux सिस्टम में उपयोग होते हैं। "aarch64" 64-bit ARM आर्किटेक्चर के लिए है।

- **linux64**: यह 64-bit x86 आर्किटेक्चर (जिसे x86_64 या AMD64 भी कहा जाता है) के लिए है, जो Linux चलाने वाले अधिकांश डेस्कटॉप और सर्वर PCs के लिए स्टैंडर्ड हैं।

**मुख्य बिंदु**:
- `linux-aarch64` चुनें यदि आपके सिस्टम में 64-bit ARM प्रोसेसर है।
- `linux64` चुनें यदि आपके सिस्टम में 64-bit x86 प्रोसेसर है।
- आप Linux पर अपने सिस्टम का आर्किटेक्चर `uname -m` चलाकर चेक कर सकते हैं। यदि यह `aarch64` आउटपुट करता है, तो ARM वर्जन का उपयोग करें; यदि यह `x86_64` आउटपुट करता है, तो linux64 वर्जन का उपयोग करें।

`.asc` फ़ाइलें संबंधित `.tar.gz` फ़ाइलों की अखंडता और प्रामाणिकता सत्यापित करने के लिए GPG सिग्नेचर हैं।