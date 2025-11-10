---
audio: false
generated: true
image: false
lang: hi
layout: post
title: पीआईएल इमेजिंग बैकएंड त्रुटि को ठीक करें
translated: true
type: note
---

यह त्रुटि इस बात का संकेत है कि या तो आपकी PIL इंस्टॉलेशन में इसका बाइनरी बैकेंड (`_imaging`) गायब है, या आप आधुनिक "Pillow" के बजाय गलती से पुराने "PIL" पैकेज का उपयोग कर रहे हैं। इसे ठीक करने का तरीका यहां बताया गया है:

1. **सुनिश्चित करें कि आप Python 3 पर हैं**
   यदि `python` कमांड Python 2 की ओर इशारा कर रहा है, तो Python 3 पर स्विच करें:

   ```bash
   python3 --version
   python3 scripts/content/avatar.py
   ```

2. **किसी भी पुराने PIL पैकेज को अनइंस्टॉल करें**

   ```bash
   # यह पुराने PIL को हटा देता है अगर यह pip के माध्यम से इंस्टॉल किया गया हो
   python3 -m pip uninstall -y PIL
   ```

3. **Pillow को (पुनः) इंस्टॉल करें**

   ```bash
   python3 -m pip install --upgrade --force-reinstall pillow
   ```

4. **आवश्यक सिस्टम लाइब्रेरीज़ इंस्टॉल करें**
   Ubuntu पर आपको इमेजिंग हेडर की आवश्यकता होगी ताकि Pillow अपना `_imaging` एक्सटेंशन बना सके:

   ```bash
   sudo apt update
   sudo apt install -y libjpeg-dev zlib1g-dev
   # फिर Pillow को पुनः इंस्टॉल करें ताकि यह उन लाइब्रेरीज़ के विरुद्ध पुनः कंपाइल हो
   python3 -m pip install --upgrade --force-reinstall pillow
   ```

5. **वर्चुअल एनवायरनमेंट का उपयोग करें (वैकल्पिक लेकिन अनुशंसित)**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install pillow
   python scripts/content/avatar.py
   ```

इसके बाद, `from PIL import Image` बिना `_imaging` इम्पोर्ट त्रुटि के काम करना चाहिए।